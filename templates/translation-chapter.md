---
book_id:
source_file:
chapter:
chapter_title_en:
chapter_title_zh:
source_pdf_pages: []
source_book_pages: []
status: draft
ocr_quality: unknown
formula_check: pending
figure_check: pending
translation_scope:
---

# Chapter ... English Title

# 第 ... 章 中文标题

## 来源追溯

| 项目 | 内容 |
|---|---|
| 原书 |  |
| 章节 |  |
| PDF 页码 |  |
| 书内页码 |  |
| 进度记录 | `progress.md` |

## 使用规则

- 图表放在译文中第一次说明或引用的位置，尽量贴近原书阅读流。
- 块级公式使用 `$$...$$`。
- 正文中不要使用行内 `$...$`，当前预览器不会渲染。
- 正文中的简单数学符号直接写 Unicode 或 HTML，例如 `σ`、`ε`、`T<sub>abs</sub>`、`10<sup>-8</sup>`。
- 原式截图只放链接，不内嵌。实际章节中写成 Markdown 链接；模板里只保留占位示例。
- 术语在本章第一次出现时链接到 `glossary/terms.md` 的稳定锚点，后续重复出现不强制链接。

## 译文

### ... 原书小节标题

这里写忠实译文。

```markdown
![图 ... 原图](./assets/fig-...-original.png)
```

*图 ...：中文图题。*

原式截图：

```markdown
[eq-...-original.png](./assets/eq-...-original.png)
```

$$

$$

正文中解释符号时使用可直接阅读的形式，例如：

其中，σ 是 Stefan-Boltzmann 常数；T<sub>abs</sub> 是绝对温度；ε 是发射率。
