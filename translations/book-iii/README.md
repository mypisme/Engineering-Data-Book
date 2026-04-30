# Engineering Data Book III 总导航

本页是第三部的阅读地图。第三部是大型专题参考手册，当前按优先专题逐章推进，不按全书页码线性翻译。

## 章节入口

| 章节 | 主题 | 工程上主要解决的问题 | 快速入口 |
|---|---|---|---|
| Chapter 2 | 强化换热器设计考虑 | 强化管和插入件的热工收益、经济性、机械约束、行业应用和设计优化边界 | [译文](./ch02-design-considerations-for-enhanced-heat-exchangers/translation.md) / [解读](./ch02-design-considerations-for-enhanced-heat-exchangers/commentary.md) / [进度](./ch02-design-considerations-for-enhanced-heat-exchangers/progress.md) |
| Chapter 3 | 单相壳侧流动与传热 | Taborek/Delaware 壳侧流路分析、折流板管束几何、传热和压降修正、低翅片管束扩展 | [译文](./ch03-single-phase-shell-side-flows-and-heat-transfer/translation.md) / [解读](./ch03-single-phase-shell-side-flows-and-heat-transfer/commentary.md) / [进度](./ch03-single-phase-shell-side-flows-and-heat-transfer/progress.md) |
| Chapter 6 | 空冷换热器传热 | 空气侧传热和压降、圆管/扁管翅片换热器关联式、湿工况与结霜工况的性能处理 | [译文](./ch06-heat-transfer-to-air-cooled-heat-exchangers/translation.md) / [解读](./ch06-heat-transfer-to-air-cooled-heat-exchangers/commentary.md) / [进度](./ch06-heat-transfer-to-air-cooled-heat-exchangers/progress.md) |
| Chapter 8 | 管内冷凝 | 水平管内冷凝流型、局部冷凝传热系数、微翅片管、可凝混合物、过热区与过冷区 | [译文](./ch08-condensation-inside-tubes/translation.md) / [解读](./ch08-condensation-inside-tubes/commentary.md) / [进度](./ch08-condensation-inside-tubes/progress.md) |
| Chapter 10 | 光管管内沸腾传热 | 垂直/水平光管内流动沸腾、Chen/Shah/Gungor-Winterton/Steiner-Taborek 方法、水平管流型模型和过冷沸腾 | [译文](./ch10-boiling-heat-transfer-inside-plain-tubes/translation.md) / [解读](./ch10-boiling-heat-transfer-inside-plain-tubes/commentary.md) / [进度](./ch10-boiling-heat-transfer-inside-plain-tubes/progress.md) |
| Chapter 12 | 两相流型 | 垂直管和水平管流型、绝热流型图、水平管蒸发/冷凝流型边界、强化管和管束外两相流型 | [译文](./ch12-two-phase-flow-patterns/translation.md) / [解读](./ch12-two-phase-flow-patterns/commentary.md) / [进度](./ch12-two-phase-flow-patterns/progress.md) |

## 收口状态

| 章节 | 当前质量状态 | 说明 |
|---|---|---|
| Chapter 2 | 本轮总收口完成 | Table 2.1 已逐项对照局部源图复核；正文无整页原文图嵌入 |
| Chapter 3 | 本轮总收口完成 | Table 3.1、式（3.4.13）和式（3.5.7）已对照源图复核；正文无整页原文图嵌入 |
| Chapter 6 | 本轮出版级收口完成 | 主公式、Table 6.1、Table 6.2/6.3 和参考文献已收口；Table 6.1 实际计算前仍应回看局部源图核对跨页常数和适用范围 |
| Chapter 8 | 本轮总收口完成 | Shah 算例、式（8.1.29）和式（8.1.31）已对照源页复核；正文无整页原文图嵌入 |
| Chapter 10 | 出版级独立复核完成 | 全部编号公式已按源页二校；Table 10.1 已保留源图、完成可检索转写并修正脚注标记 |
| Chapter 12 | 出版级独立二校完成 | Fig. 12.1-Fig. 12.24 已裁切；全部编号公式已按源页二校；源书疑点保留记录，不等同于可执行流型判别库 |

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

### Chapter 10 光管管内沸腾传热

| 节 | 主要内容 | 工程用途 | 入口 |
|---|---|---|---|
| 10.1 | 垂直管蒸发传热区域 | 识别单相液体、过冷沸腾、泡状/弹状/环状流、干涸后雾状流和单相蒸汽区 | [译文](./ch10-boiling-heat-transfer-inside-plain-tubes/translation.md#101-introduction) |
| 10.2 | 两相流动沸腾传热系数 | 建立核态沸腾贡献和对流沸腾贡献的叠加框架 | [译文](./ch10-boiling-heat-transfer-inside-plain-tubes/translation.md#102-two-phase-flow-boiling-heat-transfer-coefficient) |
| 10.3 | 垂直光管内流动沸腾 | 对比 Chen、Shah、Gungor-Winterton 和 Steiner-Taborek 垂直管方法 | [译文](./ch10-boiling-heat-transfer-inside-plain-tubes/translation.md#103-flow-boiling-inside-vertical-plain-tubes) |
| 10.4 | 水平光管内流动沸腾 | 处理分层、间歇、环状、局部干壁和混合物蒸发模型 | [译文](./ch10-boiling-heat-transfer-inside-plain-tubes/translation.md#104-flow-boiling-inside-horizontal-plain-tubes) |
| 10.5 | 水平管传热测量 | 判断电加热与热水加热实验数据的边界条件差异 | [译文](./ch10-boiling-heat-transfer-inside-plain-tubes/translation.md#105-heat-transfer-measurements-in-horizontal-tubes) |
| 10.6 | 过冷沸腾传热 | 把核态沸腾和对流沸腾按不同驱动温差分解 | [译文](./ch10-boiling-heat-transfer-inside-plain-tubes/translation.md#106-subcooled-boiling-heat-transfer) |

### Chapter 12 两相流型

| 节 | 主要内容 | 工程用途 | 入口 |
|---|---|---|---|
| 12.1 | 垂直管内流型 | 识别泡状、弹状、搅动、环状、束雾环状和雾状流 | [译文](./ch12-two-phase-flow-patterns/translation.md#121-flow-patterns-in-vertical-tubes) |
| 12.2 | 水平管内流型 | 理解重力分层下的分层、分层波状、间歇、环状和雾状流 | [译文](./ch12-two-phase-flow-patterns/translation.md#122-flow-patterns-in-horizontal-tubes) |
| 12.3 | 早期绝热流型图 | 使用 Fair、Hewitt-Roberts、Baker 和 Taitel-Dukler 图做基础流型判断 | [译文](./ch12-two-phase-flow-patterns/translation.md#123-older-adiabatic-flow-pattern-maps-for-vertical-and-horizontal-flows-in-tubes) |
| 12.4 | 水平管蒸发流型图 | 把 Kattan-Thome-Favrat、Thome-El Hajal 和 Wojtan-Ursenbacher-Thome 边界用于局部蒸发模型选择 | [译文](./ch12-two-phase-flow-patterns/translation.md#124-flow-pattern-map-for-evaporation-in-horizontal-tubes) |
| 12.5 | 水平管冷凝流型图 | 区分冷凝与蒸发在管顶液膜、雾状区和分层波状边界上的差异 | [译文](./ch12-two-phase-flow-patterns/translation.md#125-flow-pattern-map-for-condensation-in-horizontal-tubes) |
| 12.6 | 水平强化管内流型 | 判断微翅片、扭带和螺旋线插入件对间歇-环状转变的影响 | [译文](./ch12-two-phase-flow-patterns/translation.md#126-flow-patterns-in-horizontal-enhanced-tubes) |
| 12.7 | 水平管束外两相流型 | 了解 Grant-Chisholm 壳侧流型图和 Chisholm 阈值公式的适用风险 | [译文](./ch12-two-phase-flow-patterns/translation.md#127-flow-patterns-and-map-for-two-phase-flows-over-horizontal-tube-bundles) |

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
| 光管内沸腾该先选 Chen、Shah 还是 Steiner-Taborek？ | [第 10 章译文 10.3](./ch10-boiling-heat-transfer-inside-plain-tubes/translation.md#103-flow-boiling-inside-vertical-plain-tubes)、[第 10 章解读](./ch10-boiling-heat-transfer-inside-plain-tubes/commentary.md#method-differences) |
| 水平管蒸发为什么不能只看平均干度？ | [第 10 章译文 10.4](./ch10-boiling-heat-transfer-inside-plain-tubes/translation.md#104-flow-boiling-inside-horizontal-plain-tubes)、[第 10 章解读](./ch10-boiling-heat-transfer-inside-plain-tubes/commentary.md#为什么不能只看平均干度) |
| 管内沸腾和冷凝为什么要先判断流型？ | [第 12 章译文 12.1-12.4](./ch12-two-phase-flow-patterns/translation.md#121-flow-patterns-in-vertical-tubes)、[第 12 章解读](./ch12-two-phase-flow-patterns/commentary.md#流型决定模型边界) |
| Kattan-Thome-Favrat、Thome-El Hajal 和 Wojtan-Ursenbacher-Thome 图有什么关系？ | [第 12 章译文 12.4](./ch12-two-phase-flow-patterns/translation.md#124-flow-pattern-map-for-evaporation-in-horizontal-tubes)、[第 12 章解读](./ch12-two-phase-flow-patterns/commentary.md#kattan-thome-favrat-到-wojtan-ursenbacher-thome) |
| 水平管冷凝流型为什么不能当作蒸发反向过程？ | [第 12 章译文 12.5](./ch12-two-phase-flow-patterns/translation.md#125-flow-pattern-map-for-condensation-in-horizontal-tubes)、[第 12 章解读](./ch12-two-phase-flow-patterns/commentary.md#冷凝图不是蒸发图的简单反向) |

## 质量状态入口

| 范围 | 入口 |
|---|---|
| Chapter 2 进度与校对风险 | [progress.md](./ch02-design-considerations-for-enhanced-heat-exchangers/progress.md) |
| Chapter 3 进度与校对风险 | [progress.md](./ch03-single-phase-shell-side-flows-and-heat-transfer/progress.md) |
| Chapter 6 进度与校对风险 | [progress.md](./ch06-heat-transfer-to-air-cooled-heat-exchangers/progress.md) |
| Chapter 8 进度与校对风险 | [progress.md](./ch08-condensation-inside-tubes/progress.md) |
| Chapter 10 进度与校对风险 | [progress.md](./ch10-boiling-heat-transfer-inside-plain-tubes/progress.md) |
| Chapter 12 进度与校对风险 | [progress.md](./ch12-two-phase-flow-patterns/progress.md) |
| 第三部目录索引 | [book-iii-toc.md](../../sources/book-iii-toc.md) |
| 术语表 | [terms.md](../../glossary/terms.md) |
| 符号表 | [symbols.md](../../glossary/symbols.md) |
