from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BOOKS = [ROOT / "translations" / "book-ii", ROOT / "translations" / "book-iii"]
GLOSSARY = ROOT / "glossary"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def markdown_links(text: str):
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    pattern = re.compile(r"!\[[^\]]*\]\(([^)]+)\)|\[[^\]]+\]\(([^)]+)\)")
    for match in pattern.finditer(text):
        yield match.group(1) or match.group(2)


def markdown_heading_anchors(text: str) -> set[str]:
    anchors: set[str] = set(re.findall(r"<a\s+id=[\"']([^\"']+)[\"']", text))
    for line in text.splitlines():
        match = re.match(r"^(#{1,6})\s+(.+)$", line)
        if not match:
            continue
        title = match.group(2).strip().lower()
        title = re.sub(r"[`*_]+", "", title)
        title = re.sub(r"[^\w\u4e00-\u9fff\-\s]", "", title)
        title = re.sub(r"\s+", "-", title)
        anchors.add(title)
    return anchors


def check_links(errors: list[str]) -> None:
    files = [ROOT / "README.md"]
    files += sorted((ROOT / "docs").glob("*.md"))
    files += sorted((ROOT / "sources").glob("*.md"))
    for book in BOOKS:
        if not book.exists():
            continue
        files += sorted(book.glob("*.md"))
        files += sorted(book.glob("ch*/*.md"))
    files += sorted(GLOSSARY.glob("*.md"))

    anchor_cache: dict[Path, set[str]] = {}
    for md in files:
        text = read_text(md)
        for target in markdown_links(text):
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            if target.startswith("#"):
                dest = md
                anchor = target[1:]
            else:
                file_target, _, anchor = target.partition("#")
                if not file_target or file_target.startswith("D:"):
                    continue
                dest = (md.parent / file_target).resolve()
            if not dest.exists():
                errors.append(f"{md.relative_to(ROOT)}: missing link target {target}")
                continue
            if anchor and dest.suffix.lower() == ".md":
                if dest not in anchor_cache:
                    anchor_cache[dest] = markdown_heading_anchors(read_text(dest))
                if anchor not in anchor_cache[dest]:
                    errors.append(f"{md.relative_to(ROOT)}: missing anchor {target}")


def check_inline_math(errors: list[str]) -> None:
    files = []
    for book in BOOKS:
        if book.exists():
            files += sorted(book.glob("ch*/*.md"))
    files += sorted(GLOSSARY.glob("*.md"))
    for md in files:
        if md.name not in {"translation.md", "commentary.md", "terms.md", "symbols.md", "units.md"}:
            continue
        for lineno, line in enumerate(read_text(md).splitlines(), 1):
            stripped = line.replace("$$", "").replace(r"\$", "")
            if "$" in stripped:
                errors.append(f"{md.relative_to(ROOT)}:{lineno}: inline dollar math: {line[:120]}")


def check_chapter_assets(errors: list[str], warnings: list[str]) -> None:
    page_ranges = {
        ("book-ii", "ch01-basic-heat-transfer"): (8, 58),
        ("book-ii", "ch02-sensible-heat-transfer"): (59, 143),
        ("book-ii", "ch03-condensing-heat-transfer"): (144, 209),
        ("book-ii", "ch04-air-cool-heat-exchangers"): (210, 241),
        ("book-ii", "ch05-boiling-heat-transfer"): (242, 305),
        ("book-iii", "ch02-design-considerations-for-enhanced-heat-exchangers"): (37, 46),
        ("book-iii", "ch06-heat-transfer-to-air-cooled-heat-exchangers"): (121, 160),
        ("book-iii", "ch08-condensation-inside-tubes"): (213, 239),
    }
    for book in BOOKS:
        if not book.exists():
            continue
        for chapter in sorted(book.glob("ch*")):
            if not chapter.is_dir():
                continue
            assets = chapter / "assets"
            translation = chapter / "translation.md"
            progress = chapter / "progress.md"
            for required in ["README.md", "translation.md", "commentary.md", "progress.md"]:
                if not (chapter / required).exists():
                    errors.append(f"{chapter.relative_to(ROOT)}: missing {required}")
            if not assets.exists():
                errors.append(f"{chapter.relative_to(ROOT)}: missing assets directory")
                continue

            expected = page_ranges.get((book.name, chapter.name))
            if expected:
                source_pages = sorted(assets.glob("source-page-*.png"))
                expected_count = expected[1] - expected[0] + 1
                if len(source_pages) != expected_count:
                    errors.append(
                        f"{chapter.relative_to(ROOT)}: source page count {len(source_pages)} != expected {expected_count}"
                    )

            text = read_text(translation)
            for target in markdown_links(text):
                if not target.startswith("./assets/"):
                    continue
                asset = chapter / target.removeprefix("./")
                if not asset.exists():
                    errors.append(f"{translation.relative_to(ROOT)}: missing asset {target}")

            tags = re.findall(r"\\tag\{([^}]+)\}", text)
            if len(tags) != len(set(tags)):
                duplicates = sorted({tag for tag in tags if tags.count(tag) > 1})
                errors.append(f"{translation.relative_to(ROOT)}: duplicate equation tags {duplicates}")

            tag_prefix = chapter.name[2:4].lstrip("0")
            bad_tags = [tag for tag in tags if not tag.startswith(f"{tag_prefix}.")]
            if bad_tags:
                errors.append(f"{translation.relative_to(ROOT)}: equation tags outside chapter prefix {bad_tags[:10]}")

            progress_text = read_text(progress)
            if "出版级" not in progress_text:
                warnings.append(f"{progress.relative_to(ROOT)}: no publication-review record yet")

            if "待核" in text or "TODO" in text or "FIXME" in text:
                warnings.append(f"{translation.relative_to(ROOT)}: contains pending marker")


def check_glossary(errors: list[str], warnings: list[str]) -> None:
    term_text = read_text(GLOSSARY / "terms.md")
    anchors = re.findall(r'id="([^"]+)"', term_text)
    if len(anchors) != len(set(anchors)):
        duplicates = sorted({a for a in anchors if anchors.count(a) > 1})
        errors.append(f"glossary/terms.md: duplicate anchors {duplicates}")

    symbols = []
    for line in read_text(GLOSSARY / "symbols.md").splitlines():
        if not line.startswith("| ") or line.startswith("| 符号") or line.startswith("|---"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if cells:
            symbols.append(cells[0])
    duplicate_symbols = sorted({s for s in symbols if symbols.count(s) > 1})
    if duplicate_symbols:
        warnings.append(f"glossary/symbols.md: duplicate symbols need context review {duplicate_symbols}")


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    for md in ROOT.rglob("*.md"):
        text = read_text(md)
        if "\ufffd" in text:
            errors.append(f"{md.relative_to(ROOT)}: contains replacement character U+FFFD")
    check_links(errors)
    check_inline_math(errors)
    check_chapter_assets(errors, warnings)
    check_glossary(errors, warnings)

    if warnings:
        print("WARNINGS")
        for warning in warnings:
            print(f"- {warning}")
    if errors:
        print("ERRORS")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Publication verification passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
