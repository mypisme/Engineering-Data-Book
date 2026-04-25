# Chapter 2 Progress

## 范围

| 项目 | 内容 |
|---|---|
| 原书 | Engineering Data II |
| 章节 | Chapter 2 Sensible Heat Transfer |
| 当前完成范围 | Chapter 2 全章译文、解读、术语联动、图表公式资产 |
| 当前页码 | PDF 59-143；书内页码 57-141 |
| 源 PDF | `D:\Knowledge-base\books\Engineering_Data_book\第二部\Engineering Data II OCR.pdf` |

## 文件状态

| 文件 | 用途 | 状态 |
|---|---|---|
| [README.md](./README.md) | 章节入口和阅读说明 | 完成 |
| [translation.md](./translation.md) | 忠实译文；图表随文插入；公式用 LaTeX 转写并链接原式截图 | 第 2 章完整草稿完成 |
| [commentary.md](./commentary.md) | 面向有基础传热和数学背景读者的深入解读 | 第 2 章完整草稿完成 |
| [assets/](./assets/) | 原页、公式、图、表、符号表和参考文献截图 | 已生成本章所需资产；当前 200 个文件 |

## 翻译进度

| 节 | 英文标题 | 中文标题 | 译文 | 解读 | 状态说明 |
|---|---|---|---|---|---|
| 2.1 | Heat Exchangers with Low- and Medium-Finned Trufin | 采用低翅片和中翅片 Trufin 管的换热器 | 完成 | 完成 | 应用范围、低/中翅片管说明、Turbo-Chil 简述已整理 |
| 2.2 | Basic Equations for Heat Exchanger Design | 换热器设计的基本方程 | 完成 | 完成 | 总传热系数、翅片效率、MTD、F 因子已转写 |
| 2.3 | Heat Transfer and Pressure Drop During Flow Across Banks of Trufin Tubes | 横掠 Trufin 管束时的传热与压降 | 完成 | 完成 | j 因子、摩擦因子、污垢判断已整理 |
| 2.4 | Heat Transfer and Pressure Drop Inside Tubes | 管内传热与压降 | 完成 | 完成 | 层流、湍流、过渡流、两相传热公式已转写 |
| 2.5 | Preliminary Design of Shell and Tube Heat Exchangers | 管壳式换热器的初步设计 | 完成 | 完成 | 初步选型、流股分配、面积估算和设计流程已整理 |
| 2.6 | Delaware Method for Shell-Side Rating of Shell and Tube Heat Exchangers | 管壳式换热器壳侧校核的 Delaware 法 | 完成 | 完成 | 几何参数、壳侧传热、壳侧压降完整转写 |
| 2.7 | Examples of Design Problems for Low- and Medium-Finned Trufin in Shell and Tube Heat Exchangers | 低翅片和中翅片 Trufin 管壳式换热器设计例题 | 完成 | 完成 | 两个例题按设计逻辑翻译整理，并保留原页对照 |
| Nomenclature | Nomenclature | 符号说明 | 完成 | 不单独解读 | 原页截图保留，常用符号在正文和 glossary 中补充 |
| Bibliography | Bibliography | 参考文献 | 完成 | 不单独解读 | 原页截图保留，正文概述主要文献来源 |

## 公式状态

| 编号 | 位置 | 转写状态 | 原式对照 |
|---|---|---|---|
| (2.1)-(2.14) | 2.2 | 已转写 | `eq-2-1-original.png` 至 `eq-2-14-original.png` |
| (2.15)-(2.18) | 2.3 | 已转写 | `eq-2-15-original.png` 至 `eq-2-18-original.png` |
| (2.19)-(2.31) | 2.4 | 已转写 | `eq-2-19-original.png` 至 `eq-2-31-original.png`，含 `eq-2-23A-original.png` |
| (2.32)-(2.37) | 2.5 | 已转写 | `eq-2-32-original.png` 至 `eq-2-37-original.png` |
| (2.38)-(2.53) | 2.6.2 | 已转写 | `eq-2-38-original.png` 至 `eq-2-53-original.png` |
| (2.54)-(2.60) | 2.6.3-2.6.4 | 已转写 | `eq-2-54-original.png` 至 `eq-2-60-original.png` |

## 图表状态

| 类型 | 范围 | 状态 |
|---|---|---|
| 产品与管型图 | Fig. 2.1-Fig. 2.3 | 已随文插入 |
| 平均温差与 F 因子图 | Fig. 2.4-Fig. 2.12 | 已随文插入 |
| 管束传热和压降图 | Fig. 2.13-Fig. 2.17 | 已随文插入 |
| 管内传热和压降图 | Fig. 2.18-Fig. 2.20 | 已随文插入 |
| 初步设计图 | Fig. 2.21-Fig. 2.26 | 已随文插入 |
| Delaware 几何和修正因子图 | Fig. 2.27-Fig. 2.39 | 已随文插入 |
| 表格 | Table 2.1-Table 2.7 | 已链接原表截图；超长管数表按原表页保留 |
| 附录性页 | Nomenclature、Bibliography | 已链接原页截图 |

## 已核修事项

| 项目 | 处理 |
|---|---|
| 图表位置 | 图不集中放在图示层，已尽量放在首次说明或引用位置 |
| 公式截图 | 公式正文只放 LaTeX，原式截图以链接形式保留 |
| 行内数学 | 正文避免行内数学美元符号，使用 HTML 下标、Unicode 或块级公式 |
| 术语联动 | 显热传热、Trufin 管、壳侧、管侧、Colburn j 因子、Delaware 法等首次出现已链接 glossary |
| 长表处理 | 表 2.6 为大规模管数表，保留原表多页截图，正文说明用途；避免人工重排造成数值污染 |
| 例题处理 | 例题正文已补充初估面积、Delaware 几何、壳侧传热、总传热系数、管长、壳侧压降、管侧压降和最终设计参数；原页链接用于复核 |
| 公式复核 | 式 (2.34) 和 (2.35) 已对照原式截图；原书二者均为同向不等式，译文按原式保留 |
| 图表裁切 | Fig. 2.26、Fig. 2.33 已由正文页误裁重切为局部图表截图 |

## 校对提示

第 2 章当前已经形成可阅读、可追溯、可继续迭代的完整草稿。正式发布前建议做出版级二次校对，重点是：

- Delaware 几何方程中的英制单位一致性复核。
- 例题 2.7.1 和 2.7.2 的密集算术过程逐行复算。
- 表 2.1 到表 2.7 的数值是否需要转写为结构化表格。

这些属于质量复核层，不是当前章节结构或内容缺口。

## 验证记录

| 日期 | 检查 | 结果 |
|---|---|---|
| 2026-04-25 | Markdown UTF-8、本地链接、术语锚点、行内数学检查 | 通过 |
| 2026-04-25 | 式 (2.34)/(2.35) 原式截图复核；Fig. 2.26、Fig. 2.33 局部裁切复核 | 通过 |
