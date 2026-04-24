# Engineering Data Book 翻译与理解

这个仓库用于整理 Wolverine / Engineering Data Book 系列资料的中文翻译、术语沉淀和理解解读。

核心目标是形成忠实、可校对、可长期维护的中文工程阅读资料。`D:\codehub\AirCooledUnitSelection` 是重要应用背景，但不是本仓库的主线；它只用于帮助判断哪些章节需要优先理解、哪些概念需要解释得更扎实。

## 当前样板章

已用 `Engineering Data II` 第 1 章形成 Markdown 样板章：

- [第 1 章译文](translations/book-ii/ch01-basic-heat-transfer/translation.md)
- [第 1 章解读](translations/book-ii/ch01-basic-heat-transfer/commentary.md)
- [第 1 章进度记录](translations/book-ii/ch01-basic-heat-transfer/progress.md)

## 工作流文档

- [翻译工作流](docs/workflow.md)
- [后续章节开发计划](docs/development-plan.md)
- [验证清单](docs/verification.md)

这个样板章已经验证 Markdown 可以承载以下内容：

- 忠实译文
- 独立的章节理解和解读
- LaTeX 公式转写
- 原书公式截图链接
- 就地插入的原书图示截图
- 术语表
- OCR 与公式校对状态
- 原页追溯

## 推荐目录

```text
sources/        书源信息、OCR 状态、目录索引
translations/   分书、分章的译文与解读
glossary/       术语、符号、单位
templates/      章节样稿模板
figures/        后续可放全局重绘图或跨章节图表
tables/         后续可放大型表格 CSV/XLSX
```

## 暂定原则

- 先忠实翻译，再做理解解读。
- 译文、公式、图表都必须能追溯到原书页码。
- OCR 内容不能直接信任，公式、上下标、图表编号必须人工核对。
- 不确定的公式先保留截图链接和待核对标记，不猜。
- 默认按原书章节组织文件；若单章过长，再按原书大段落拆成 part 文件。
- 译文和解读分离，译文文件尽量保持原书阅读流。
- 重要术语在每章第一次出现时链接到术语表。
- 正文中不使用行内 `$...$` 数学写法；块级公式使用 `$$...$$`，正文简单符号用 Unicode/HTML。
