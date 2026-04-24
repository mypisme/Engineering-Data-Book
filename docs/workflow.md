# 翻译工作流

本文是后续章节开发的操作规范。上下文压缩或换会话后，优先阅读本文、对应章节的 `progress.md`，再继续工作。

## 核心原则

- 忠实翻译优先，解读单独写在 `commentary.md`。
- 默认按原书章节组织目录，不按小节拆成大量文件。
- 图表在译文中就地插入，贴近原书阅读流。
- 公式主体使用 LaTeX 块级公式；原公式截图只作为链接。
- 正文和表格中禁止行内 `$...$` 数学写法，因为当前预览器不会渲染。
- 正文中的简单数学符号直接写 Unicode 或 HTML，例如 `σ`、`ε`、`ΔT`、`T<sub>abs</sub>`、`10<sup>-8</sup>`。
- 每章维护 `translation.md`、`commentary.md`、`progress.md` 和 `assets/`。
- 所有术语、符号、单位逐步进入 `glossary/`。

## 章节目录标准

```text
translations/book-ii/ch01-basic-heat-transfer/
  README.md
  translation.md
  commentary.md
  progress.md
  assets/
  tables/
```

`README.md` 说明本章文件用途和当前范围。  
`translation.md` 写忠实译文，图表就地插入。  
`commentary.md` 写深入解读，不重复译文。  
`progress.md` 记录页码、状态、公式、图表、原页截图和校对提示。  
`assets/` 保存原页截图、公式截图、图表截图。  
`tables/` 保存大型表格的 CSV/XLSX，只有需要时创建。

## 单章开发步骤

1. 确认章节或小节边界：记录 PDF 页码和书内页码。
2. 创建章节目录：复制 `templates/translation-chapter.md`、`templates/commentary-chapter.md`、`templates/progress-chapter.md`。
3. 抽取 OCR 文本：只作为初稿来源，不直接信任。
4. 生成原页截图：命名为 `source-page-000.png`。
5. 裁剪图表和公式：图表命名为 `fig-...-original.png`，公式命名为 `eq-...-original.png`。
6. 写 `translation.md`：忠实翻译，图表放到原文说明附近。
7. 写 `commentary.md`：解释概念、公式来源、图表读法、常见误解和前后关系。
8. 更新 `progress.md`：公式清单、图表清单、原页截图、已核修事项和校对提示。
9. 更新 `glossary/terms.md`、`glossary/symbols.md`、`glossary/units.md`。
10. 运行链接和锚点检查。

## 数学与公式格式

块级公式：

```markdown
原式截图：[eq-1-12-original.png](./assets/eq-1-12-original.png)

$$
\frac{Q}{A}=\sigma\varepsilon T_{\mathrm{abs}}^4
\tag{1.12}
$$
```

正文解释：

```markdown
其中，σ 是 Stefan-Boltzmann 常数，T<sub>abs</sub> 是绝对温度，ε 是发射率。
```

不要把简单符号写成行内 LaTeX；这类写法在当前预览器中不会渲染，读者会直接看到源码。

## 图表格式

```markdown
![图 1.14 典型饱和池沸腾曲线](./assets/fig-1-14-original.png)

*图 1.14：典型饱和池沸腾曲线。*
```

图应放在第一次说明或引用它的位置。章节末尾只在 `progress.md` 维护图表清单。

## 术语联动

本章第一次出现的重要术语链接到术语表：

```markdown
[导热](../../../glossary/terms.md#term-conduction)
```

术语表使用稳定锚点：

```markdown
| <a id="term-conduction"></a>conduction | 导热 | ... |
```

后续重复出现同一术语时，不必每次链接，避免影响阅读。

## 完成标准

一个小节或章节初稿完成至少满足：

- 目标页码范围内无明显漏段。
- 图表已就地插入；大型图表确需延后时，必须在 `progress.md` 说明原因和原页位置。
- 公式有块级 LaTeX 转写和原式截图链接；确需延后时，必须保留可追溯截图和明确原因。
- 正文中没有行内 `$...$` 数学写法。
- 新术语、符号、单位已进入 `glossary/`；暂不入库的边界情况要在 `progress.md` 的校对提示中说明。
- Markdown 本地链接和术语锚点检查通过。

## 恢复上下文步骤

换会话后按以下顺序恢复：

1. 读 `README.md`。
2. 读本文 `docs/workflow.md`。
3. 读 `docs/development-plan.md`。
4. 读当前章节的 `progress.md`。
5. 打开当前章节的 `translation.md` 和 `commentary.md`。
6. 按 `progress.md` 的完成状态和校对提示继续。
