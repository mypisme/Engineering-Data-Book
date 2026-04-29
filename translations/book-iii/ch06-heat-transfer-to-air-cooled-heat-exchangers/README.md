# Book III Chapter 6

# 第 6 章 空冷换热器传热

本目录收纳 `Engineering Data Book III` 第 6 章的译文、解读、进度记录和原文对照资产。

## 文件

| 文件 | 用途 | 状态 |
|---|---|---|
| [translation.md](./translation.md) | 忠实译文；图表随文放置；主公式用 LaTeX 转写；Table 6.1 采用局部源图、中文索引和可检索公式转写；Table 6.2、Table 6.3 已按源表复核 | 本轮出版级收口完成 |
| [commentary.md](./commentary.md) | 面向具备基础传热和换热器常识读者的深入解读 | 完整解读 |
| [progress.md](./progress.md) | 范围、资产、公式、图表和校对记录 | 本轮出版级收口记录 |
| [assets/](./assets/) | 原页、公式、图、表格和参考页截图 | 已生成 |

## 章节范围

| 项目 | 内容 |
|---|---|
| 原书 | Engineering Data Book III |
| 英文标题 | Heat Transfer to Air-Cooled Heat Exchangers |
| 中文标题 | 空冷换热器传热 |
| PDF 页码 | 121-160 |
| 书内页码 | 6-1 到 6-40 |

## 阅读顺序

建议先读 6.1，建立空气侧 j 因子、LMTD、ε-NTU、湿空气焓差和压降模型；再读 6.2-6.7，按圆管/扁管和不同翅片类型理解性能趋势；随后读 6.8 和 Table 6.1，判断实际设计应选哪类关联式；最后读 Example 6.1，把 LMTD 迭代和 ε-NTU 解法连起来。

若只关心空冷器软件建模，应优先阅读 6.1、6.8、Example 6.1 和 [commentary.md](./commentary.md) 中的“面向后续建模的抽象”。

## 格式约定

- 图和表放在首次说明或引用附近。
- 主公式以块级 LaTeX 重排。
- 原式截图在正文公式旁保留。
- Table 6.1 是 19 页大型关联式表，当前采用局部源图、中文索引和可检索公式转写并行保留；实际计算前应以局部源图核对跨页常数、特征长度和适用范围。
- 正文不使用行内美元数学写法，简单符号用 HTML 下标或 Unicode。
