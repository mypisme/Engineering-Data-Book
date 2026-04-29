# Chapter 6 Progress

## 范围

| 项目 | 内容 |
|---|---|
| 原书 | Engineering Data Book III |
| 章节 | Chapter 6 Heat Transfer to Air-Cooled Heat Exchangers |
| 当前完成范围 | Chapter 6 全章译文、解读、术语联动、图表资产、主公式、Table 6.1、Example 6.1 和参考文献的本轮出版级收口 |
| 当前页码 | PDF 121-160；书内页码 6-1 到 6-40 |
| 源 PDF | `D:\Knowledge-base\books\Engineering_Data_book\第三部\Engineering Data Book III OCR.pdf` |

## 文件状态

| 文件 | 用途 | 状态 |
|---|---|---|
| [README.md](./README.md) | 章节入口和阅读说明 | 完成 |
| [translation.md](./translation.md) | 忠实译文；图表随文插入；主公式转写；Table 6.1 采用局部源图、中文索引和可检索公式转写；Table 6.2/6.3 已按源表复核；参考文献已整理 | 本轮出版级收口完成 |
| [commentary.md](./commentary.md) | 面向有基础传热和换热器背景读者的深入解读 | 完整解读 |
| [assets/](./assets/) | 原页、公式、图、表格截图 | 已生成 80 个资产：40 张原页、16 张公式、3 张图、21 张表格 |

## 翻译进度

| 节 | 英文标题 | 中文标题 | 译文 | 解读 | 状态说明 |
|---|---|---|---|---|---|
| 6.1 | Introduction and Background | 引言与背景 | 完成 | 完成 | j 因子、LMTD、ε-NTU、UA 热阻链、湿空气焓差、压降和风机功率已整理 |
| 6.2 | Performance of plain-fin, round-tube heat exchangers | 平片圆管换热器性能 | 完成 | 完成 | 翅片间距、管排数、湿表面冷凝液、相对湿度和部分湿表面已整理 |
| 6.3 | Performance of louvered-fin, round-tube heat exchangers | 百叶翅片圆管换热器性能 | 完成 | 完成 | 翅片间距、热尾迹、管径、湿工况、亲水涂层和相对湿度已整理 |
| 6.4 | Performance of slit-fin, round-tube heat exchanger | 开缝翅片圆管换热器性能 | 完成 | 完成 | 开缝翅片干/湿工况、冷凝液滞留和涂层效应已整理 |
| 6.5 | Performance of wavy-fin, round-tube heat exchanger | 波纹翅片圆管换热器性能 | 完成 | 完成 | 顺列/错列布置、波形诱导扰动、湿工况几何影响已整理 |
| 6.6 | Performance of louvered-fin, flat-tube heat exchanger | 百叶翅片扁管换热器性能 | 完成 | 完成 | 紧凑扁管、边界层再启动、百叶几何和湿/结霜研究已整理 |
| 6.7 | Performance of slit-fin, flat-tube heat exchanger | 开缝翅片扁管换热器性能 | 完成 | 完成 | 矩形错列条翅片和汽车蒸发器湿工况研究已整理 |
| 6.8 | Predicting Air-Side Thermal-Hydraulic Performance | 预测空气侧热工水力性能 | 完成 | 完成 | Table 6.1 已完成中文索引、可检索公式转写和 19 张局部表格源图追溯；关联式选择原则已翻译 |
| Example 6.1 | Annular-fin-tube heat exchanger example | 环形翅片管换热器算例 | 完成 | 完成 | LMTD 和 ε-NTU 方程组已按源表复核，修正 r<sub>ii</sub>/r<sub>i</sub>/r<sub>o</sub> 变量体系和热阻量级 |
| 6.9 | Nomenclature | 符号说明 | 完成 | 完成 | 已整理为中文符号说明，并保留原页截图入口 |
| 6.10 | References | 参考文献 | 完成 | 不单独解读 | 已按原书参考文献页整理为正文条目，原页截图继续保留作追溯 |

## 公式清单

| 编号 | 位置 | LaTeX 转写 | 原式截图 | 状态 |
|---|---|---|---|---|
| (6.1.1)-(6.1.15) | 6.1 | j 因子、能量平衡、LMTD、ε-NTU、UA 热阻链、焓势法、压降和风机功率 | `eq-6-1-original.png` 到 `eq-6-15-original.png`；源页 122-126 | 已按源页复核；修正式（6.1.6）、式（6.1.7）、式（6.1.11）、式（6.1.12）、式（6.1.14）和式（6.1.15） |
| Example 6.1 | 例题 | LMTD 与 ε-NTU 方程组 | [eq-example-6-1-lmtd-original.png](./assets/eq-example-6-1-lmtd-original.png) | 已按源页 152 和表 6.2/6.3 复核 |
| Table 6.1 | 6.8 | 大型 j/f 关联式表 | [table-6-1-part-01-original.png](./assets/table-6-1-part-01-original.png) 至 [table-6-1-part-19-original.png](./assets/table-6-1-part-19-original.png) | 已完成中文索引和可检索公式转写；局部源图保留为计算前核对底稿 |
| Table 6.2 | Example 6.1 | LMTD 解法方程组 | [table-6-2-original.png](./assets/table-6-2-original.png) | 已按源表复核；变量体系 r<sub>ii</sub>/r<sub>i</sub>/r<sub>o</sub> 已修正 |
| Table 6.3 | Example 6.1 | ε-NTU 解法方程组 | [table-6-3-original.png](./assets/table-6-3-original.png) | 已按源表复核；与表 6.2 共用前置方程 |

## 图表清单

| 编号 | 中文图题 | 文件 | 状态 |
|---|---|---|---|
| Fig. 6.1 | 典型翅片管换热器 | [fig-6-1-original.png](./assets/fig-6-1-original.png) | 已随文插入 |
| Fig. 6.2 | 各类翅片及几何参数 | [fig-6-2-original.png](./assets/fig-6-2-original.png) | 已随文插入 |
| Fig. 6.3 | 环形翅片管换热器 | [fig-6-3-original.png](./assets/fig-6-3-original.png) | 已随文插入 |
| Table 6.1 | 换热器关联式 | `table-6-1-part-01-original.png` 到 `table-6-1-part-19-original.png` | 已随文插入并补中文索引和可检索公式转写 |
| Table 6.2 | LMTD 解法方程组 | [table-6-2-original.png](./assets/table-6-2-original.png) | 已随文插入 |
| Table 6.3 | ε-NTU 解法方程组 | [table-6-3-original.png](./assets/table-6-3-original.png) | 已随文插入 |

## 原页截图

- `source-page-121.png` 到 `source-page-160.png`

## 已核修事项

| 项目 | 处理 |
|---|---|
| 第三部目录结构 | 新建 `translations/book-iii/README.md` 和第 6 章目录，结构沿用 Book II 章节标准 |
| 原页追溯 | 已生成 PDF 121-160 全部原页截图 |
| 图表裁切 | Fig. 6.1-Fig. 6.3 已裁为局部图；Table 6.1 旋转裁切为可读横向局部图 |
| 公式截图 | 式 (6.1.1)-(6.1.15) 和 Example 6.1 核心公式保留原式截图 |
| 大型表格 | Table 6.1 跨 19 页，已补中文转写索引和可检索公式转写；原局部表格截图继续作为计算前核对底稿 |
| 行内数学 | 正文避免行内美元符号，使用 HTML 下标、Unicode 或块级公式 |
| 术语联动 | 第一次出现的重要空气侧术语已链接 glossary，并补充新术语 |

## 出版级复核记录

| 日期 | 项目 | 结论 |
|---|---|---|
| 2026-04-26 | 第三部第 6 章初始落地 | 章节结构、原页截图、主图、主公式截图和译文/解读/进度文件已建立 |
| 2026-04-26 | OCR 风险评估 | PDF 121-132、152-160 正文 OCR 可用；PDF 133-151 的 Table 6.1 公式 OCR 基本不可用，已改用局部截图追溯 |
| 2026-04-26 | 工程阅读初版 | 6.1-6.10 全部章节内容已覆盖；Table 6.1 已补中文转写索引；Table 6.2、Table 6.3 作为原表截图保留 |
| 2026-04-26 | 表格补强 | 根据复核质疑修正完成口径：第 6 章不能只称“完整翻译”；当时已补全 Table 6.1 中文索引，本轮收口继续补强为局部源图、索引和可检索公式转写并行 |
| 2026-04-26 | 公式转写补强 | 式 (6.1.13)、Table 6.1、Table 6.2 和 Table 6.3 已补可检索公式转写，原截图保留为源页核对依据 |
| 2026-04-28 | 已完成章节总收口检查 | 未发现整页 source-page 原文图以图片形式嵌入正文；当轮识别出第 6 章需单独收口的主公式、Table 6.1、Table 6.2/6.3 和参考文献项 |
| 2026-04-28 | 第 6 章出版级收口 | 按源页修正主公式、Example 6.1 变量体系和热阻量级；Table 6.1 改为局部源图、中文索引和可检索公式转写并行；参考文献已整理为正文条目 |

## 校对提示

第 6 章当前版本已完成本轮出版级收口。后续维护提示：

- Table 6.1 作为大型关联式表，实际代入计算前应同时查看局部源图，重点核对跨页常数、特征长度和适用范围。
- Example 6.1 中 Table 6.2 的 A<sub>min</sub> 行按原表保留 L 记号；上下文管长为 L<sub>c</sub>，工程复算时需按题设几何统一解释。
- 若后续把 Table 6.1 转成可执行计算库，应逐条建立单元测试，不要直接把 Markdown 公式当作已验证代码。

后续校对不得用 OCR 文本直接覆盖表格公式，应以当前局部截图和本次转写并行核对。

## 验证记录

| 日期 | 检查 | 结果 |
|---|---|---|
| 2026-04-26 | 章节资产生成 | 已生成 80 个资产：40 张源页、16 张公式、3 张图、21 张表格 |
| 2026-04-26 | Markdown 链接、术语锚点、行内数学检查 | 通过：`python scripts\verify_book_ii_publication.py` |
| 2026-04-28 | 已完成章节总收口检查 | 正文无 `source-page` 整页图片嵌入；已识别第 6 章需单独出版级收口 |
| 2026-04-28 | 主公式与 Example 6.1 源页复核 | 式（6.1.1）到式（6.1.15）、Table 6.2 和 Table 6.3 已按源页/源表复核 |
