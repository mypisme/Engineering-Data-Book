# Engineering Data Book III 总导航

本页是第三部的阅读地图。第三部是大型专题参考手册，当前按优先专题逐章推进，不按全书页码线性翻译。

## 章节入口

| 章节 | 主题 | 工程上主要解决的问题 | 快速入口 |
|---|---|---|---|
| Chapter 2 | 强化换热器设计考虑 | 强化管和插入件的热工收益、经济性、机械约束、行业应用和设计优化边界 | [译文](./ch02-design-considerations-for-enhanced-heat-exchangers/translation.md) / [解读](./ch02-design-considerations-for-enhanced-heat-exchangers/commentary.md) / [进度](./ch02-design-considerations-for-enhanced-heat-exchangers/progress.md) |
| Chapter 3 | 单相壳侧流动与传热 | Taborek/Delaware 壳侧流路分析、折流板管束几何、传热和压降修正、低翅片管束扩展 | [译文](./ch03-single-phase-shell-side-flows-and-heat-transfer/translation.md) / [解读](./ch03-single-phase-shell-side-flows-and-heat-transfer/commentary.md) / [进度](./ch03-single-phase-shell-side-flows-and-heat-transfer/progress.md) |
| Chapter 6 | 空冷换热器传热 | 空气侧传热和压降、圆管/扁管翅片换热器关联式、湿工况与结霜工况的性能处理 | [译文](./ch06-heat-transfer-to-air-cooled-heat-exchangers/translation.md) / [解读](./ch06-heat-transfer-to-air-cooled-heat-exchangers/commentary.md) / [进度](./ch06-heat-transfer-to-air-cooled-heat-exchangers/progress.md) |
| Chapter 8 | 管内冷凝 | 水平管内冷凝流型、局部冷凝传热系数、微翅片管、可凝混合物、过热区与过冷区 | [译文](./ch08-condensation-inside-tubes/translation.md) / [解读](./ch08-condensation-inside-tubes/commentary.md) / [进度](./ch08-condensation-inside-tubes/progress.md) |

## 收口状态

| 章节 | 当前质量状态 | 说明 |
|---|---|---|
| Chapter 2 | 本轮总收口完成 | Table 2.1 已逐项对照局部源图复核；正文无整页原文图嵌入 |
| Chapter 3 | 本轮总收口完成 | Table 3.1、式（3.4.13）和式（3.5.7）已对照源图复核；正文无整页原文图嵌入 |
| Chapter 6 | 本轮出版级收口完成 | 主公式、Table 6.1、Table 6.2/6.3 和参考文献已收口；Table 6.1 实际计算前仍应回看局部源图核对跨页常数和适用范围 |
| Chapter 8 | 本轮总收口完成 | Shah 算例、式（8.1.29）和式（8.1.31）已对照源页复核；正文无整页原文图嵌入 |

## 逐节地图

### Chapter 2 强化换热器设计考虑

| 节 | 主要内容 | 工程用途 | 入口 |
|---|---|---|---|
| 2.1 | 强化管和插入件的应用背景 | 建立强化换热器为何可降低本体和安装总成本的背景 | [译文](./ch02-design-considerations-for-enhanced-heat-exchangers/translation.md#21-introduction) |
| 2.2 | 热工与经济优势 | 判断既有设备改造、新建设备、合金管和成本比较的收益 | [译文](./ch02-design-considerations-for-enhanced-heat-exchangers/translation.md#22-thermal-and-economic-advantages-of-heat-transfer-augmentations) |
| 2.3 | 热工设计和优化考虑 | 避免用光管约束限制强化设备，正确处理污垢面积比和软件输入 | [译文](./ch02-design-considerations-for-enhanced-heat-exchangers/translation.md#23-thermal-design-and-optimization-considerations) |
| 2.4 | 机械设计和制造考虑 | 检查壁厚、胀接/焊接、U 形弯曲和固定管板平均金属温差 | [译文](./ch02-design-considerations-for-enhanced-heat-exchangers/translation.md#24-mechanical-design-and-construction-considerations) |
| 2.5-2.11 | 行业应用 | 对照制冷空调、石化、电厂、地热和食品加工等场景识别强化机会 | [译文](./ch02-design-considerations-for-enhanced-heat-exchangers/translation.md#25-refrigeration-and-air-conditioning-system-applications) |

### Chapter 3 单相壳侧流动与传热

| 节 | 主要内容 | 工程用途 | 入口 |
|---|---|---|---|
| 3.1 | Taborek/Delaware 法背景和适用边界 | 明确本章适用于单弓形折流板主线壳侧设计 | [译文](./ch03-single-phase-shell-side-flows-and-heat-transfer/translation.md#31-introduction) |
| 3.2 | A/B/C/E/F 壳侧流股 | 识别横掠流、泄漏流、管束旁路和管程隔板旁路的作用 | [译文](./ch03-single-phase-shell-side-flows-and-heat-transfer/translation.md#32-stream-analysis-of-flow-distribution-in-a-baffled-heat-exchanger) |
| 3.3 | 管束和壳体几何 | 建立壳径、管束限径、折流板切口、间隙、布管和管数估算输入 | [译文](./ch03-single-phase-shell-side-flows-and-heat-transfer/translation.md#33-definition-of-bundle-and-shell-geometries) |
| 3.4 | 壳侧传热流路分析 | 用 J 修正因子从理想管束传热系数得到实际壳侧系数 | [译文](./ch03-single-phase-shell-side-flows-and-heat-transfer/translation.md#34-stream-analysis-of-heat-transfer-in-a-baffled-heat-exchanger) |
| 3.5 | 壳侧压降流路分析 | 分解横掠流、窗口流和端区压降并施加 R 修正因子 | [译文](./ch03-single-phase-shell-side-flows-and-heat-transfer/translation.md#35-stream-analysis-of-shell-side-pressure-drop-in-a-baffled-heat-exchanger) |
| 3.6 | 低翅片管束扩展 | 把光管 Taborek 方法扩展到整体低翅片管束 | [译文](./ch03-single-phase-shell-side-flows-and-heat-transfer/translation.md#36-stream-analysis-applied-to-low-finned-tube-bundles) |

### Chapter 6 空冷换热器传热

| 节 | 主要内容 | 工程用途 | 入口 |
|---|---|---|---|
| 6.1 | 空气侧分析背景、j 因子、LMTD、ε-NTU、湿空气焓差、压降和风机功率 | 把空气侧换热器建模框架从 Book II 的高翅片空冷器扩展到紧凑式圆管/扁管翅片换热器 | [译文](./ch06-heat-transfer-to-air-cooled-heat-exchangers/translation.md#61-introduction-and-background) |
| 6.2 | 平片圆管换热器性能 | 判断翅片间距、管排数、湿表面冷凝液和亲水性对 j/f 因子的影响 | [译文](./ch06-heat-transfer-to-air-cooled-heat-exchangers/translation.md#62-performance-of-plain-fin-round-tube-heat-exchangers) |
| 6.3 | 百叶翅片圆管换热器性能 | 理解低 Re 下热尾迹、管径、湿工况和涂层对空气侧性能的影响 | [译文](./ch06-heat-transfer-to-air-cooled-heat-exchangers/translation.md#63-performance-of-louvered-fin-round-tube-heat-exchangers) |
| 6.4 | 开缝翅片圆管换热器性能 | 处理开缝翅片在干/湿工况下的冷凝液滞留和压降变化 | [译文](./ch06-heat-transfer-to-air-cooled-heat-exchangers/translation.md#64-performance-of-slit-fin-round-tube-heat-exchanger) |
| 6.5 | 波纹翅片圆管换热器性能 | 区分顺列/错列布置和波形诱导扰动对传热与摩擦的影响 | [译文](./ch06-heat-transfer-to-air-cooled-heat-exchangers/translation.md#65-performance-of-wavy-fin-round-tube-heat-exchanger) |
| 6.6 | 百叶翅片扁管换热器性能 | 理解紧凑扁管百叶翅片的边界层再启动、百叶导流和冷凝排水问题 | [译文](./ch06-heat-transfer-to-air-cooled-heat-exchangers/translation.md#66-performance-of-louvered-fin-flat-tube-heat-exchanger) |
| 6.7 | 开缝翅片扁管换热器性能 | 使用矩形错列条翅片关联式或汽车蒸发器湿工况研究作为参考 | [译文](./ch06-heat-transfer-to-air-cooled-heat-exchangers/translation.md#67-performance-of-slit-fin-flat-tube-heat-exchanger) |
| 6.8 | 空气侧热工水力性能预测 | 为不同翅片/管型和干、湿、结霜表面选择合适的 j/f 关联式 | [译文](./ch06-heat-transfer-to-air-cooled-heat-exchangers/translation.md#68-predicting-air-side-thermal-hydraulic-performance) |
| 6.9 | 符号说明 | 统一本章与空气侧文献常用符号 | [译文](./ch06-heat-transfer-to-air-cooled-heat-exchangers/translation.md#69-nomenclature) |
| Example 6.1 | 环形翅片管换热器 LMTD 与 ε-NTU 算例 | 展示同一几何下 LMTD 迭代法和 ε-NTU 法如何得到同一热负荷 | [译文](./ch06-heat-transfer-to-air-cooled-heat-exchangers/translation.md#example-61) |

### Chapter 8 管内冷凝

| 节 | 主要内容 | 工程用途 | 入口 |
|---|---|---|---|
| 8.1 | 水平管内冷凝、流型、纯蒸汽冷凝模型、Thome-El Hajal-Cavallini 方法 | 按局部干度、质量通量和流型选择冷凝传热模型 | [译文](./ch08-condensation-inside-tubes/translation.md#81-condensation-inside-horizontal-tubes) |
| 8.2 | 水平微翅片管内冷凝 | 判断微翅片强化在不同质量通量和流型下的适用性 | [译文](./ch08-condensation-inside-tubes/translation.md#82-condensation-in-horizontal-microfin-tubes) |
| 8.3 | 水平管内可凝混合物冷凝 | 用 Silver-Bell-Ghaly 和非共沸混合物模型估算温度滑移影响 | [译文](./ch08-condensation-inside-tubes/translation.md#83-condensation-of-condensable-mixtures-in-horizontal-tubes) |
| 8.4 | 过热蒸汽冷凝 | 判断去过热区壁面是否已发生边界层冷凝 | [译文](./ch08-condensation-inside-tubes/translation.md#84-condensation-of-superheated-vapor) |
| 8.5 | 冷凝液过冷 | 将末端过冷区切换为单相液体传热和压降模型 | [译文](./ch08-condensation-inside-tubes/translation.md#85-subcooling-of-condensate) |

## 按工程问题查找

| 我想解决的问题 | 建议阅读 |
|---|---|
| 强化管贵，为什么整台设备反而可能更便宜？ | [第 2 章译文 2.2](./ch02-design-considerations-for-enhanced-heat-exchangers/translation.md#22-thermal-and-economic-advantages-of-heat-transfer-augmentations)、[第 2 章解读](./ch02-design-considerations-for-enhanced-heat-exchangers/commentary.md#设计判断主线) |
| 强化换热器设计时最容易犯什么软件输入错误？ | [第 2 章译文 2.3](./ch02-design-considerations-for-enhanced-heat-exchangers/translation.md#23-thermal-design-and-optimization-considerations)、[第 2 章解读](./ch02-design-considerations-for-enhanced-heat-exchangers/commentary.md#污垢处理是常见错误点) |
| 壳侧 Delaware/Taborek 法中为什么要分 A/B/C/E/F 流股？ | [第 3 章译文 3.2](./ch03-single-phase-shell-side-flows-and-heat-transfer/translation.md#32-stream-analysis-of-flow-distribution-in-a-baffled-heat-exchanger)、[第 3 章解读](./ch03-single-phase-shell-side-flows-and-heat-transfer/commentary.md#设计判断主线) |
| 折流板间隙、旁路和密封条会怎样影响壳侧传热与压降？ | [第 3 章译文 3.4](./ch03-single-phase-shell-side-flows-and-heat-transfer/translation.md#34-stream-analysis-of-heat-transfer-in-a-baffled-heat-exchanger)、[第 3 章译文 3.5](./ch03-single-phase-shell-side-flows-and-heat-transfer/translation.md#35-stream-analysis-of-shell-side-pressure-drop-in-a-baffled-heat-exchanger) |
| 为什么空气侧文献常用 Colburn j 因子而不是直接用 Nu？ | [6.1 引言与背景](./ch06-heat-transfer-to-air-cooled-heat-exchangers/translation.md#61-introduction-and-background)、[第 6 章解读](./ch06-heat-transfer-to-air-cooled-heat-exchangers/commentary.md#j-因子是空气侧文献的通用接口) |
| 空冷器用 LMTD 还是 ε-NTU？ | [6.1 换热器模型方程](./ch06-heat-transfer-to-air-cooled-heat-exchangers/translation.md#换热器模型方程)、[Example 6.1](./ch06-heat-transfer-to-air-cooled-heat-exchangers/translation.md#example-61) |
| 湿表面为什么可能增加压降、但不一定提高显热 j 因子？ | [6.2 平片圆管](./ch06-heat-transfer-to-air-cooled-heat-exchangers/translation.md#62-performance-of-plain-fin-round-tube-heat-exchangers)、[第 6 章解读](./ch06-heat-transfer-to-air-cooled-heat-exchangers/commentary.md#湿工况不是简单的粗糙度修正) |
| 不同翅片类型该选哪类关联式？ | [6.8 性能预测](./ch06-heat-transfer-to-air-cooled-heat-exchangers/translation.md#68-predicting-air-side-thermal-hydraulic-performance)、[Table 6.1](./ch06-heat-transfer-to-air-cooled-heat-exchangers/translation.md#table-61) |
| Book II 第 4 章和 Book III 第 6 章有什么区别？ | [第 6 章解读](./ch06-heat-transfer-to-air-cooled-heat-exchangers/commentary.md#和-book-ii-第-4-章的关系) |
| 管内冷凝局部系数为什么必须先看流型？ | [第 8 章译文 8.1](./ch08-condensation-inside-tubes/translation.md#81-condensation-inside-horizontal-tubes)、[第 8 章解读](./ch08-condensation-inside-tubes/commentary.md#流型决定模型边界) |
| 可凝混合物冷凝为什么会比纯流体低？ | [第 8 章译文 8.3](./ch08-condensation-inside-tubes/translation.md#83-condensation-of-condensable-mixtures-in-horizontal-tubes)、[第 8 章解读](./ch08-condensation-inside-tubes/commentary.md#混合物冷凝的附加热阻) |

## 质量状态入口

| 范围 | 入口 |
|---|---|
| Chapter 2 进度与校对风险 | [progress.md](./ch02-design-considerations-for-enhanced-heat-exchangers/progress.md) |
| Chapter 3 进度与校对风险 | [progress.md](./ch03-single-phase-shell-side-flows-and-heat-transfer/progress.md) |
| Chapter 6 进度与校对风险 | [progress.md](./ch06-heat-transfer-to-air-cooled-heat-exchangers/progress.md) |
| Chapter 8 进度与校对风险 | [progress.md](./ch08-condensation-inside-tubes/progress.md) |
| 第三部目录索引 | [book-iii-toc.md](../../sources/book-iii-toc.md) |
| 术语表 | [terms.md](../../glossary/terms.md) |
| 符号表 | [symbols.md](../../glossary/symbols.md) |
