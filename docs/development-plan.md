# 后续章节开发计划

本文记录后续章节推进顺序和迭代策略，避免上下文压缩后丢失方向。

## 当前基准

已确认以 `Engineering Data II` 第 1 章作为格式基准，并以第 2-5 章验证了更长章节、更多图表公式、相变专题和例题页追溯的可行性：

- 章节级组织，而不是小节级目录。
- `translation.md`、`commentary.md`、`progress.md` 分离。
- 图表就地插入。
- 块级公式用 LaTeX，原式截图用链接。
- 正文不用行内 `$...$`，简单符号用 Unicode/HTML。
- 术语首次出现链接到术语表。

基准章节：

- [Book II Chapter 1 translation](../translations/book-ii/ch01-basic-heat-transfer/translation.md)
- [Book II Chapter 1 commentary](../translations/book-ii/ch01-basic-heat-transfer/commentary.md)
- [Book II Chapter 1 progress](../translations/book-ii/ch01-basic-heat-transfer/progress.md)
- [Book II Chapter 2 translation](../translations/book-ii/ch02-sensible-heat-transfer/translation.md)
- [Book II Chapter 2 commentary](../translations/book-ii/ch02-sensible-heat-transfer/commentary.md)
- [Book II Chapter 2 progress](../translations/book-ii/ch02-sensible-heat-transfer/progress.md)
- [Book II Chapter 3 translation](../translations/book-ii/ch03-condensing-heat-transfer/translation.md)
- [Book II Chapter 3 commentary](../translations/book-ii/ch03-condensing-heat-transfer/commentary.md)
- [Book II Chapter 3 progress](../translations/book-ii/ch03-condensing-heat-transfer/progress.md)
- [Book II Chapter 4 translation](../translations/book-ii/ch04-air-cool-heat-exchangers/translation.md)
- [Book II Chapter 4 commentary](../translations/book-ii/ch04-air-cool-heat-exchangers/commentary.md)
- [Book II Chapter 4 progress](../translations/book-ii/ch04-air-cool-heat-exchangers/progress.md)
- [Book II Chapter 5 translation](../translations/book-ii/ch05-boiling-heat-transfer/translation.md)
- [Book II Chapter 5 commentary](../translations/book-ii/ch05-boiling-heat-transfer/commentary.md)
- [Book II Chapter 5 progress](../translations/book-ii/ch05-boiling-heat-transfer/progress.md)

## 第一阶段：完成 Book II Chapter 1

目标：把 `Chapter 1 Basic Heat Transfer` 做成完整样板章。

当前状态：已完成。第 1 章已经具备完整译文、独立解读、术语链接、公式转写、原式截图链接、随文图表和进度记录。

推进顺序：

| 顺序 | 原书小节 | 中文暂译 | 状态 |
|---|---|---|---|
| 1 | 1.1 Basic Mechanisms of Heat Transfer | 传热的基本机制 | 完成 |
| 2 | 1.2 Basic Heat Exchanger Equations | 换热器基本方程 | 完成 |
| 3 | 1.3 The Mean Temperature Difference | 平均温差 | 完成 |
| 4 | 1.4 Construction of Shell and Tube Heat Exchangers | 管壳式换热器结构 | 完成 |
| 5 | 1.5 Application of Extended Surfaces to Heat Exchangers | 扩展表面在换热器中的应用 | 完成 |
| 6 | 1.6 Fouling in Heat Exchangers | 换热器污垢 | 完成 |

每完成一个小节：

- 更新 `translation.md`
- 更新 `commentary.md`
- 更新 `progress.md`
- 补充 `assets/`
- 补充术语、符号、单位
- 跑链接和锚点检查

## 第二阶段：建立两本书目录索引

目标：在大规模翻译前建立可导航的目录索引。

当前状态：已完成，见 [Engineering Data II 目录索引](../sources/book-ii-toc.md) 和 [Engineering Data Book III 目录索引](../sources/book-iii-toc.md)。

交付物：

```text
sources/book-ii-toc.md
sources/book-iii-toc.md
```

每章记录：

- 原文标题
- 中文暂译
- PDF 页码范围
- 书内页码范围
- 关键词
- 优先级
- 当前状态

优先级：

- P0：基础必读，影响后续理解
- P1：核心专题，优先翻译
- P2：参考专题，需要时推进
- P3：暂缓

## 第三阶段：Book II 主线推进

Book II 更适合做基础主线，推荐按章节顺序推进：

1. Chapter 1 Basic Heat Transfer（完成）
2. Chapter 2 Sensible Heat Transfer（完成）
3. Chapter 3 Condensing Heat Transfer（完成）
4. Chapter 4 Trufin Tubes in Air-Cool Heat Exchangers（完成）
5. Chapter 5 Trufin Tubes in Boiling Heat Transfer（完成）

每章都沿用同一结构：

```text
translations/book-ii/chXX-slug/
  README.md
  translation.md
  commentary.md
  progress.md
  assets/
```

## 第四阶段：Book III 专题推进

Book III 是大型参考手册，不建议线性从第一页翻到最后一页。建议按专题推进：

| 优先级 | 章节 | 主题 |
|---|---|---|
| P1 | Chapter 6 | Heat Transfer to Air-Cooled Heat Exchangers |
| P1 | Chapter 8 | Condensation Inside Tubes |
| P1 | Chapter 10 | Boiling Heat Transfer Inside Plain Tubes |
| P1 | Chapter 12 | Two-Phase Flow Patterns |
| P1 | Chapter 13 | Two-Phase Pressure Drop |
| P2 | Chapter 15 | Thermodynamics of Refrigerant Mixtures and Refrigerant-Oil Mixtures |
| P2 | Chapter 16 | Effects of Oil on Thermal Performance of Heat Exchangers |

Book III 每章仍按章节目录组织，但可以按小节逐步填充 `translation.md` 和 `commentary.md`。

## 迭代节奏

建议每次只推进一个小节或一个自然页段。标准迭代：

1. 确认页码范围。
2. 抽取 OCR 文本。
3. 生成资产。
4. 写译文。
5. 写解读。
6. 更新进度。
7. 更新 glossary。
8. 验证链接。

完成 3-5 个小节后做一次术语统一。完成一章后做一次章节总览和二次校对。

## 下一步

Book II 第 1-5 章已形成连续主线，两本书目录索引也已补齐。下一步建议从 Book III 的 P1 专题中选择一个章节进入翻译：

```text
Chapter 6  Heat Transfer to Air-Cooled Heat Exchangers
Chapter 8  Condensation Inside Tubes
Chapter 10 Boiling Heat Transfer Inside Plain Tubes
Chapter 12 Two-Phase Flow Patterns
Chapter 13 Two-Phase Pressure Drop
```

优先选择与 `D:\codehub\AirCooledUnitSelection` 当前问题最接近的章节；若主线仍围绕空冷器，建议先做 Chapter 6。

进入后续章节前保留一条质量复核原则：

- 新章节按 Chapter 1 的文件结构和公式/图表格式执行。
- 每章完成时运行 [验证清单](./verification.md)。
- 正式发布前再做一次工程数值复读；这不是章节交付阻塞项，而是出版级校对层。
