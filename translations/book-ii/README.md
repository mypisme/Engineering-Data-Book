# Engineering Data II 总导航

本页是第二部的阅读地图。它用于快速判断“某章某节大概解决什么工程问题”，并直接跳转到对应译文、解读或复核记录。

## 使用方式

- 想按原书顺序读：从“章节入口”进入各章。
- 想查某一节做什么：看“逐节地图”，点击对应译文锚点。
- 想按工程问题反查：看“按问题查找”。
- 想确认质量状态：看各章 `progress.md` 或总复核记录 [Book II 出版级复核记录](../../docs/book-ii-publication-review.md)。

## 章节入口

| 章节 | 主题 | 工程上主要解决的问题 | 快速入口 |
|---|---|---|---|
| Chapter 1 | 基础传热 | 建立总传热系数、LMTD、污垢、翅片效率和翅片热阻这些后续章节共用语言 | [译文](./ch01-basic-heat-transfer/translation.md) / [解读](./ch01-basic-heat-transfer/commentary.md) / [进度](./ch01-basic-heat-transfer/progress.md) |
| Chapter 2 | 显热传热 | 单相显热管壳式换热器、低/中翅片 Trufin、Delaware 壳侧校核和两个设计例题 | [译文](./ch02-sensible-heat-transfer/translation.md) / [解读](./ch02-sensible-heat-transfer/commentary.md) / [进度](./ch02-sensible-heat-transfer/progress.md) |
| Chapter 3 | 冷凝传热 | 管内/管外冷凝、两相压降、壳侧冷凝器构型、纯组分与多组分冷凝设计 | [译文](./ch03-condensing-heat-transfer/translation.md) / [解读](./ch03-condensing-heat-transfer/commentary.md) / [进度](./ch03-condensing-heat-transfer/progress.md) |
| Chapter 4 | 空冷器 | 高翅片 Trufin 空冷器、风机限制、空气侧传热压降和初步设计表 | [译文](./ch04-air-cool-heat-exchangers/translation.md) / [解读](./ch04-air-cool-heat-exchangers/commentary.md) / [进度](./ch04-air-cool-heat-exchangers/progress.md) |
| Chapter 5 | 沸腾传热 | 沸腾曲线、蒸发器/再沸器、管内外沸腾、热虹吸、Trufin 管外沸腾例题 | [译文](./ch05-boiling-heat-transfer/translation.md) / [解读](./ch05-boiling-heat-transfer/commentary.md) / [进度](./ch05-boiling-heat-transfer/progress.md) |

## 逐节地图

### Chapter 1 基础传热

| 节 | 主要内容 | 工程用途 | 入口 |
|---|---|---|---|
| 1.1 | 导热、单相对流、两相流、冷凝、汽化、辐射的基本机制 | 给后续显热、冷凝、沸腾章节建立物理图像和术语基础 | [译文](./ch01-basic-heat-transfer/translation.md#11-basic-mechanisms-of-heat-transfer) |
| 1.2 | 总传热系数、污垢热阻、面积基准和设计积分 | 把换热器拆成串联热阻账本，理解 U<sub>o</sub>/U<sub>i</sub> 为什么不能混用 | [译文](./ch01-basic-heat-transfer/translation.md#12-basic-heat-exchanger-equations) |
| 1.3 | LMTD 和构型修正因子 F | 处理冷热流体沿程温差变化，并识别构型导致的温差惩罚 | [译文](./ch01-basic-heat-transfer/translation.md#13-the-mean-temperature-difference) |
| 1.4 | 管壳式换热器结构、热应力、振动、冲蚀和流股分配 | 把热计算和机械约束、清洗维护、成本放到同一个设计判断中 | [译文](./ch01-basic-heat-transfer/translation.md#14-construction-of-shell-and-tube-heat-exchangers) |
| 1.5 | 扩展表面、翅片效率、等效面积、翅片热阻法 | 判断翅片面积增加是否真的降低总热阻 | [译文](./ch01-basic-heat-transfer/translation.md#15-application-of-extended-surfaces-to-heat-exchangers) |
| 1.6 | 污垢类型、污垢热阻表、材料和清洗策略 | 为设计裕量、流速选择、材质选择和可清洗性提供边界 | [译文](./ch01-basic-heat-transfer/translation.md#16-fouling-in-heat-exchangers) |
| Table 1.1 | 管内流动冲蚀速度限制 | 估算水、液体、气体和干蒸汽的最大设计速度 | [译文](./ch01-basic-heat-transfer/translation.md#table-11-erosion-limits) |
| Table 1.2 | 典型过程污垢热阻 | 选择不同水质、化工、炼油和润滑油工况的污垢热阻 | [译文](./ch01-basic-heat-transfer/translation.md#table-12-fouling-resistances-for-typical-process-applications) |

### Chapter 2 显热传热

| 节 | 主要内容 | 工程用途 | 入口 |
|---|---|---|---|
| 2.1 | 低/中翅片 Trufin 管的应用范围和管型说明 | 判断显热管壳式换热器中是否适合用低/中翅片管 | [译文](./ch02-sensible-heat-transfer/translation.md#21-heat-exchangers-with-low--and-medium-finned-trufin) |
| 2.2 | 基本设计方程、总传热系数、翅片效率、F 因子 | 把第 1 章基础方程落到低/中翅片 Trufin 换热器 | [译文](./ch02-sensible-heat-transfer/translation.md#22-basic-equations-for-heat-exchanger-design) |
| 2.3 | 横掠 Trufin 管束的传热、压降和污垢影响 | 估算壳侧横流传热和压降，并理解管束污垢风险 | [译文](./ch02-sensible-heat-transfer/translation.md#23-heat-transfer-and-pressure-drop-during-flow-across-banks-of-trufin-tubes) |
| 2.4 | 管内单相传热压降和管内两相传热 | 处理管侧显热流动、黏度修正和两相传热的基本估算 | [译文](./ch02-sensible-heat-transfer/translation.md#24-heat-transfer-and-pressure-drop-inside-tubes) |
| 2.5 | 管壳式换热器初步设计原则和尺寸估算 | 从热负荷和 U 值走到壳径、管长、管程和初步布置 | [译文](./ch02-sensible-heat-transfer/translation.md#25-preliminary-design-of-shell-and-tube-heat-exchangers) |
| 2.6 | Delaware 法壳侧几何、传热和压降校核 | 对管壳式换热器壳侧做更可靠的 rating，而不只用理想横流 | [译文](./ch02-sensible-heat-transfer/translation.md#26-delaware-method-for-shell-side-rating-of-shell-and-tube-heat-exchangers) |
| 2.7 | 压缩机后冷器和瓦斯油-原油换热器设计例题 | 通过完整算例串联热负荷、面积、Delaware 校核和压降限制 | [译文](./ch02-sensible-heat-transfer/translation.md#27-examples-of-design-problems-for-low--and-medium-finned-trufin-in-shell-and-tube-heat-exchangers) |

### Chapter 3 冷凝传热

| 节 | 主要内容 | 工程用途 | 入口 |
|---|---|---|---|
| 3.1 | 冷凝方式、Trufin 冷凝应用范围和可用管型 | 判断低/中翅片管在冷凝中主要是增面积还是改善排液 | [译文](./ch03-condensing-heat-transfer/translation.md#31-trufin-tubes-in-condensing-heat-transfer) |
| 3.2 | 高翅片 Trufin 管内冷凝、两相流型、压降和 MTD | 处理管内冷凝时的干度、空隙率、流型、摩擦/加速/静压项 | [译文](./ch03-condensing-heat-transfer/translation.md#32-condensation-of-vapor-inside-high-finned-trufin-tubes) |
| 3.3 | 低/中翅片管外壳侧冷凝、过热、过冷、管束修正和壳侧压降 | 设计壳侧冷凝器时处理构型、冷凝系数、积分过冷和压降倍率 | [译文](./ch03-condensing-heat-transfer/translation.md#33-condensation-of-vapor-outside-low--and-medium-finned-trufin) |
| 3.4 | 纯组分与多组分冷凝器设计例题 | 把热负荷、壳径管长、传热系数、Delaware 压降和 Silver 修正串起来 | [译文](./ch03-condensing-heat-transfer/translation.md#34-examples-of-design-problems-for-low--and-medium-finned-trufin-in-shell-and-tube-condensers) |

### Chapter 4 空气冷却换热器

| 节 | 主要内容 | 工程用途 | 入口 |
|---|---|---|---|
| 4.1 | 高翅片 Trufin、直接/间接空冷、鼓风式/引风式、风机和低温控制 | 判断空冷器构型、风机布置、再循环、防冻和控制方式 | [译文](./ch04-air-cool-heat-exchangers/translation.md#41-heat-exchangers-with-high-finned-trufin-tubes) |
| 4.2 | 高翅片管翅片效率、翅片热阻、污垢和双金属接触热阻 | 判断空气侧强化面积、翅片材料、接触热阻和高温界面风险 | [译文](./ch04-air-cool-heat-exchangers/translation.md#42-heat-transfer-with-high-finned-trufin-tubes) |
| 4.3 | 空气横流传热、V<sub>face</sub>/V<sub>max</sub>、MTD 修正、空气侧压降 | 计算高翅片管束空气侧传热和风机静压需求 | [译文](./ch04-air-cool-heat-exchangers/translation.md#43-heat-transfer-and-pressure-drop-in-high-finned-trufin-tube-banks) |
| 4.4 | 初步设计流程、热力学限制、速率限制和管排数交叉点 | 快速确定空冷器迎风面积、管排数、管程数和合理速度区间 | [译文](./ch04-air-cool-heat-exchangers/translation.md#44-preliminary-design-procedures) |
| 4.5 | 最终设计迭代 | 用正式传热/压降关联式验证初设，并调整管束、风机和管侧约束 | [译文](./ch04-air-cool-heat-exchangers/translation.md#45-final-design) |

### Chapter 5 沸腾传热

| 节 | 主要内容 | 工程用途 | 入口 |
|---|---|---|---|
| 5.1 | 沸腾曲线、成核、核态沸腾、临界热流、膜态沸腾和管内沸腾 | 建立沸腾传热的工作区间，避免把所有沸腾都当成单一公式问题 | [译文](./ch05-boiling-heat-transfer/translation.md#51-trufin-in-boiling-heat-transfer) |
| 5.2 | 蒸发器/再沸器类型和适用场景 | 选择釜式、热虹吸、强制循环、降膜等蒸发器构型 | [译文](./ch05-boiling-heat-transfer/translation.md#52-vaporizers---types-and-usage) |
| 5.3 | 池沸腾、管束外沸腾、管内沸腾和混合物沸腾传热关联 | 估算不同沸腾位置和流动状态下的沸腾侧传热系数 | [译文](./ch05-boiling-heat-transfer/translation.md#53-boiling-heat-transfer) |
| 5.4 | 垂直管内和水平壳侧降膜传热、干斑和液膜破裂 | 处理薄膜蒸发器中润湿、液膜稳定和传热失效边界 | [译文](./ch05-boiling-heat-transfer/translation.md#54-falling-film-heat-transfer) |
| 5.5 | 特殊强化表面和翅片上沸腾 | 判断 Trufin 或其他强化表面在低温差洁净沸腾中的价值与风险 | [译文](./ch05-boiling-heat-transfer/translation.md#55-special-surfaces) |
| 5.6 | 管侧和壳侧沸腾压降 | 把两相压降、静压头和循环驱动力纳入再沸器设计 | [译文](./ch05-boiling-heat-transfer/translation.md#56-pressure-drop) |
| 5.7 | 沸腾工况污垢 | 判断污垢裕量为什么可能降低沸腾驱动力，而不是越大越安全 | [译文](./ch05-boiling-heat-transfer/translation.md#57-fouling) |
| 5.8 | 再沸器设计步骤 | 选择再沸器类型，并组织池式、管内/热虹吸再沸器的设计流程 | [译文](./ch05-boiling-heat-transfer/translation.md#58-design-procedures) |
| 5.9 | 特殊考虑和例题说明 | 说明例题范围、设计边界和后续 5.10 的使用方式 | [译文](./ch05-boiling-heat-transfer/translation.md#59-special-considerations) |
| 5.10 | 釜式再沸器、管内热虹吸和 Trufin 管外沸腾例题 | 通过三个算例理解面积基准、热阻分配、压降和强化表面收益 | [译文](./ch05-boiling-heat-transfer/translation.md#510-example-of-design-problems-for-trufin-in-boiling-heat-transfer) |
| Table 5.1 | Borishanski 核态池沸腾参数 | 给式 (5.11) 和核态池沸腾简式提供物性参数 | [译文](./ch05-boiling-heat-transfer/translation.md#table-51) |

## 按工程问题查找

| 我想解决的问题 | 建议阅读 |
|---|---|
| 总传热系数 U 应该按哪一侧面积为基准？ | [1.2 换热器基本方程](./ch01-basic-heat-transfer/translation.md#12-basic-heat-exchanger-equations)、[2.2 基本设计方程](./ch02-sensible-heat-transfer/translation.md#22-basic-equations-for-heat-exchanger-design)、[5.10 Trufin 沸腾例题](./ch05-boiling-heat-transfer/translation.md#510-example-of-design-problems-for-trufin-in-boiling-heat-transfer) |
| LMTD 和 F 因子什么时候会成为限制？ | [1.3 平均温差](./ch01-basic-heat-transfer/translation.md#13-the-mean-temperature-difference)、[2.2.3 F 因子](./ch02-sensible-heat-transfer/translation.md#223-mean-temperature-difference-f-factors)、[4.3 横流 MTD](./ch04-air-cool-heat-exchangers/translation.md#432-mean-temperature-difference-in-crossflow) |
| 低/中翅片 Trufin 管适合什么显热服务？ | [2.1 应用范围](./ch02-sensible-heat-transfer/translation.md#21-heat-exchangers-with-low--and-medium-finned-trufin)、[2.7 设计例题](./ch02-sensible-heat-transfer/translation.md#27-examples-of-design-problems-for-low--and-medium-finned-trufin-in-shell-and-tube-heat-exchangers) |
| Delaware 法为什么需要那么多几何参数？ | [2.6 Delaware 法](./ch02-sensible-heat-transfer/translation.md#26-delaware-method-for-shell-side-rating-of-shell-and-tube-heat-exchangers)、[第 2 章解读](./ch02-sensible-heat-transfer/commentary.md#delaware-法的本质) |
| 冷凝器壳侧压降为什么会压垮常规 E 壳设计？ | [3.3 壳侧冷凝](./ch03-condensing-heat-transfer/translation.md#33-condensation-of-vapor-outside-low--and-medium-finned-trufin)、[3.4 纯组分冷凝例题](./ch03-condensing-heat-transfer/translation.md#341-condenser-design-for-a-pure-component-example-problem) |
| 多组分冷凝为什么不能直接套纯组分冷凝系数？ | [3.4.2 多组分冷凝例题](./ch03-condensing-heat-transfer/translation.md#342-condenser-design-for-a-multi-component-mixture-example-problem)、[第 3 章解读](./ch03-condensing-heat-transfer/commentary.md#纯组分与多组分冷凝的差别) |
| 空冷器中 V<sub>face</sub> 和 V<sub>max</sub> 有什么区别？ | [4.3 空气侧传热压降](./ch04-air-cool-heat-exchangers/translation.md#43-heat-transfer-and-pressure-drop-in-high-finned-trufin-tube-banks)、[第 4 章解读](./ch04-air-cool-heat-exchangers/commentary.md#vface-与-vmax-的区别) |
| 空冷器为什么主要受风机静压限制？ | [4.1 设备说明](./ch04-air-cool-heat-exchangers/translation.md#413-description-of-equipment)、[4.4 基本限制](./ch04-air-cool-heat-exchangers/translation.md#443-fundamental-limitations-controlling-air-cooled-heat-exchanger-design) |
| 如何快速估算空冷器迎风面积和管排数？ | [4.4 初步设计程序](./ch04-air-cool-heat-exchangers/translation.md#44-preliminary-design-procedures) |
| 沸腾曲线上哪些区间适合设计运行？ | [5.1 沸腾曲线](./ch05-boiling-heat-transfer/translation.md#51-trufin-in-boiling-heat-transfer)、[第 5 章解读](./ch05-boiling-heat-transfer/commentary.md#沸腾曲线是全章地图) |
| 再沸器应该选釜式还是热虹吸？ | [5.2 蒸发器类型](./ch05-boiling-heat-transfer/translation.md#52-vaporizers---types-and-usage)、[5.8 再沸器设计步骤](./ch05-boiling-heat-transfer/translation.md#58-design-procedures) |
| 热虹吸再沸器为什么同时是传热问题和压降问题？ | [5.6 压降](./ch05-boiling-heat-transfer/translation.md#56-pressure-drop)、[5.10.2 管内热虹吸例题](./ch05-boiling-heat-transfer/translation.md#5102-in-tube-thermosyphon---example-problem) |
| Trufin 管外沸腾的收益从哪里来？ | [5.5 特殊表面](./ch05-boiling-heat-transfer/translation.md#55-special-surfaces)、[5.10.3 管外沸腾例题](./ch05-boiling-heat-transfer/translation.md#5103-boiling-outside-trufin-tubes---example-problem) |
| 哪些地方已经发现原书算术疑点？ | [Book II 出版级复核记录](../../docs/book-ii-publication-review.md)、[3.4.1 冷凝器压降疑点](./ch03-condensing-heat-transfer/translation.md#341-condenser-design-for-a-pure-component-example-problem)、[5.10.3 沸腾初算疑点](./ch05-boiling-heat-transfer/translation.md#5103-boiling-outside-trufin-tubes---example-problem) |

## 质量状态入口

| 范围 | 入口 |
|---|---|
| 第二部总复核 | [Book II 出版级复核记录](../../docs/book-ii-publication-review.md) |
| 术语表 | [terms.md](../../glossary/terms.md) |
| 符号表 | [symbols.md](../../glossary/symbols.md) |
| 原书目录索引 | [book-ii-toc.md](../../sources/book-ii-toc.md) |
