---
book_id: engineering-data-book-iii
source_file: "D:\\Knowledge-base\\books\\Engineering_Data_book\\第三部\\Engineering Data Book III OCR.pdf"
chapter: 11
chapter_title_en: Boiling Heat Transfer Inside Enhanced Tubes
chapter_title_zh: 强化管管内沸腾传热
source_pdf_pages: "307-328"
source_book_pages: "11-1 到 11-22"
status: publication_second_review_complete
ocr_quality: prose_usable_formula_ocr_untrusted
formula_check: all_23_numbered_equations_transcribed_against_source_pages
figure_check: source_pages_retained_figure_crops_pending
translation_scope: "第 11 章：强化管管内蒸发、微翅片管、扭带插入件、波纹管、多孔涂层、微翅片流动沸腾模型、扭带关联式"
---

# Chapter 11 Boiling Heat Transfer Inside Enhanced Tubes

# 第 11 章 强化管管内沸腾传热

## 来源追踪

| 项目 | 内容 |
|---|---|
| 原书 | Engineering Data Book III |
| 章节 | Chapter 11 |
| PDF 页码 | 307-328 |
| 书内页码 | 11-1 到 11-22 |
| 进度记录 | [progress.md](./progress.md) |

完整源页截图保留在 `assets/source-page-307.png` 到 `assets/source-page-328.png`，用于逐页二校和公式复核。正文只展示局部图表资产，避免整页原文图打断阅读。

## 摘要

本章描述强化管和管内插入件中的蒸发过程。涵盖垂直管和水平管中的蒸发。讨论的强化类型包括微翅片管、扭带插入件、波纹管和内部多孔涂层管。其他强化方式虽然存在，但已不再广泛使用（如铝星形插入件和内部高翅片管）、不适合强化沸腾传热，或缺乏充分的热性能文献。本章给出了微翅片管和扭带插入件的多种预测方法。

---

## 11.1 Introduction

## 11.1 引言

在**垂直管**中，强化蒸发最重要的应用和潜在收益在石化行业，即垂直热虹吸再沸器。这些设备通常蒸发 10% 至 35% 的液体，进口因蒸馏塔液位静压头而略有过冷。这意味着非共沸多组分混合物的蒸发也是关注重点，但文献中这类强化管的数据很少或没有。

在**水平管**中，最重要的应用是制冷、空调和热泵的直接膨胀蒸发器。在石化行业，水平管侧蒸发器偶尔使用但并非常态。在直接膨胀蒸发器中，流体在膨胀阀后进入管内，干度范围约 15% 至 100%（含过热区）。在循环式系统中，流体以饱和液体进入，约 20%–30% 被蒸发。本章主要聚焦于微翅片管——工业应用最广泛的强化类型。

本章重点介绍 1990 年以后的研究。1990 年前的全面论述参见 Thome (1990)，扭带蒸发的综述参见 Shatto and Peterson (1996)。

**面积基准约定**：强化管内沸腾传热系数基于最大内径处的名义面积定义——对微翅片管即翅根直径，对扭带插入件即光管内表面。

---

## 11.2 Types of Enhancement and Their Performance Ratios

## 11.2 强化类型与性能比

以下强化类型用于管内蒸发：

### 微翅片管

**图 11.1** 展示了微翅片管翅片截面照片。**图 11.2** 展示了特征几何——由最大内径 $d_f$、翅片数、螺旋角 $\alpha_f$（或轴向节距）、翅高 $e_f$、翅厚、截面形状和内表面积比定义。多数微翅片为近似梯形截面（圆顶、圆角翅根），其他形状包括三角形、矩形和螺旋形（无翅根间隔）。翅片效率在合金管中也接近 1.0，因为翅高通常仅 0.2–0.3 mm。

微翅片管最初在日本开发，1980 年代开始广泛使用，迅速取代了此前流行的星形插入管。无缝微翅片管通过在心棒上拉拔光铜管成形，翅高约 0.1–0.4 mm。最有利的螺旋角范围约 7°–23°，18° 最为普遍。焊接微翅片管由压花铜带成形，可生产更广泛的几何形状包括三维翅片。

### 扭带插入件

**图 11.3** 展示了扭带插入件的照片和几何示意图。扭曲比定义为带材旋转 180° 所需的轴向长度除以管内径。典型扭曲比为 3–5，无穷大扭曲比代表无扭曲的直带。扭带松装于管内，其表面积不计为传热面积。

### 波纹管

**图 11.4** 展示了波纹管照片及其特征尺寸。多数波纹管为单头波纹，由波纹深度 $e$ 和轴向节距 $p$（或螺旋角）定义。内表面积比略大于 1.0。波纹管可用铜、铜合金、碳钢、不锈钢和钛制造。

### 强化性能比（定性指南）

相对于相同直径光管、相同质量通量和热通量：

| 强化类型 | 传热强化比 | 压降比 | 备注 |
|---|---|---|---|
| **微翅片管**（水平） | 低质量通量 3–4 倍；高质量通量趋近面积比 | 低质量通量约 1.0；高质量通量最大约 1.5 | 传热/压降比非常有利 |
| **微翅片管**（垂直） | 与水平相似或略低 | 微翅片摩擦增量相比静压头可忽略 | 可直接使用光管设计方法 |
| **扭带插入件** | 1.2–1.5 倍 | 高达 2.0（带材分隔流道） | 可改装既有光管设备 |
| **波纹管** | 1.2–1.8 倍 | 约 2 倍光管 | 高质量通量下性能接近微翅片 |
| **多孔涂层管** | 5–10 倍（垂直管） | 垂直管中可忽略 | 仅对环状流有效，分层流中部分干涸 |

---

## 11.3 Flow Boiling in Vertical Microfin Tubes

## 11.3 垂直微翅片管流动沸腾

Kattan, Thome and Favrat (1995) 对 R-134a 在一根微翅片管（最大内径 11.90 mm，螺旋角 18°，翅高 0.25 mm，60 翅片，面积比 1.74）中进行了垂直上升流和水平流的对比试验。采用热水加热和修正 Wilson 图法获取准局部传热数据。

- 低质量通量和低干度下，垂直管强化弱于水平管（垂直光管无分层流不利效应）
- 高质量通量下，两种取向强化水平相似，至少等于或大于面积增加
- **图 11.5**：201.2 kg/m²s，干度 0.23–0.5，强化比约 2 倍以上
- **图 11.6**：301.6 kg/m²s，垂直微翅片管性能略低于水平

**工程意义**：用垂直微翅片管束替换光管管束时，管数减少使质量通量、热通量和出口干度提高，可进一步改善传热约 50%。

---

## 11.4 Flow Boiling with Twisted Tape Inserts in Vertical Tubes

## 11.4 垂直扭带插入件流动沸腾

扭带插入件的独特优势是无需更换管束即可提高既有蒸发器的热能力。

Jensen and Bensler (1986) 研究了不同扭曲比对 R-113 垂直上升流沸腾的影响（管内径 8.10 mm，电加热）。**图 11.7** 显示：高干度下强化可达 40%，低干度下约 10%。旋流效应在低质量通量和低热通量下预期更有效。

---

## 11.5 Flow Boiling Inside Vertical Tubes with Internal Porous Coatings

## 11.5 垂直管内部多孔涂层流动沸腾

在垂直蒸发器管内壁施加薄多孔涂层可显著改善性能。商用 High Flux 管（原 Union Carbide，现 UOP）可在内壁或外壁施加涂层。

**图 11.8** 展示了液氧在 18.7 mm 内径 High Flux 管中的管内沸腾数据（约 1.01 bar）：
- 传热系数几乎不随干度和质量通量变化（核态沸腾主导）
- 强化比约 **10 倍**
- 池沸腾曲线与流动沸腾数据吻合良好 → 可用池沸腾数据设计垂直热虹吸再沸器

---

## 11.6 Flow Boiling of Pure Fluids Inside Enhanced Horizontal Tubes

## 11.6 纯流体在强化水平管中的流动沸腾

**表 11.1** 列出了 1990 年以来水平强化管中纯制冷剂（和共沸混合物）蒸发的实验研究，包括试验条件、管型和翅片几何参数。

> 表中符号说明：
> - $\dot{m}$ (kg/m²s)：基于最大内径的质量通量
> - Max ID：翅根或波纹根部内径
> - No./Angle/Ht./AR：翅片数/螺旋角/翅高(mm)/面积比
> - Microfin*：带切口的三维微翅片

### 关键实验研究摘要

**Eckels and Pate (1991a)**：单根微翅片管中 R-134a 和 R-12 蒸发。低质量通量强化比 2.3–2.6 倍，高质量通量 1.7–1.9 倍（面积比 1.5）。

**Thors and Bogart (1994)**：3/8 in. 和 5/8 in. 两种管径的光管、微翅片和波纹管对比（**图 11.9**）。75 翅微翅片管强化比接近 4。波纹管在高质量通量下性能接近微翅片管但压降惩罚更大。

**Chamra and Webb (1995)**：带切口的三维微翅片管（15° 螺旋角），低质量通量强化比高达 3.5，200 kg/m²s 时降至 1.7。环状流中蒸发与冷凝传热系数相似。

**Nidegger, Thome and Favrat (1997) / Zürcher et al. (1997a)**：R-134a 在微翅片管和光管中的局部传热系数对比（4.4°C）。全干度范围均观察到强化。

**Zürcher et al. (1997b)**：不锈钢微翅片管中氨蒸发（**图 11.10**）。低干度强化 2.2 倍，高干度强化 7.7 倍，平均强化比 4–5（面积比 1.33）。极低质量通量下强化减弱（流动保持分层）。

**Lallemand, Branescu and Haberschill (2001)**：R-22 在光管和两种微翅片管中的蒸发。**图 11.11** 显示干涸起始干度随质量通量的变化（0.65–0.85）。微翅片管仅将干涸起始点微弱推移到更高干度。

---

## 11.7 Flow Boiling of Zeotropic Mixtures Inside Enhanced Horizontal Tubes

## 11.7 非共沸混合物在强化水平管中的流动沸腾

### 数据处理注意事项

对非共沸混合物蒸发，焓变包含分凝潜热和沿泡点曲线加给两相的显热。必须使用混合物焓曲线计算局部干度和泡点温度 $T_{\text{bub}}$，局部传热系数定义为 $\alpha = q/(T_{\text{wall}} - T_{\text{bub}})$。**许多文献数据未正确使用焓曲线**，使用时必须验证。

**表 11.2** 列出了 1990 年以来非共沸混合物在强化管中蒸发的实验研究。

### 关键实验研究

**Zürcher, Thome and Favrat (1998a, 1998b)**：R-407C 和 R-134a 在微翅片管中的对比（**图 11.12**）。300 kg/m²s 时两种流体性能相近，但低质量通量下 R-407C 显著低于 R-134a（传质阻力效应）。

**Ebisu and Torikoshi (1998)**：R-407C 在人字形微翅片管中蒸发。传热系数比常规螺旋微翅片管高 90%，但压降更大。

---

## 11.8 Flow Boiling Models for Horizontal Microfin Tubes

## 11.8 水平微翅片管流动沸腾模型

### 11.8.1 Fujii 关联式

Fujii et al. (1993) 提出以下微翅片关联式：

$$
\text{Nu}_{\text{mf}} = \frac{\alpha_{\text{mf}}\,d_{\text{mean}}}{k_L} = \text{Nu}_L\left(4.6/X_{tt}\right)
\tag{11.8.1}
$$

其中液相 Nusselt 数 $\text{Nu}_L$ 的关联式为：

$$
\text{Nu}_L = 0.045\,\text{Re}_L^{0.8}\,\text{Pr}_L^{0.4}
\tag{11.8.2}
$$

液相 Reynolds 数基于液体质量分数：

$$
\text{Re}_L = \dot{m}(1 - x)\,d_{\text{mean}}/\mu_L
\tag{11.8.3}
$$

两相均湍流的 Martinelli 参数 $X_{tt}$：

$$
X_{tt} = \left(\frac{1-x}{x}\right)^{0.9}\left(\frac{\rho_G}{\rho_L}\right)^{0.5}\left(\frac{\mu_L}{\mu_G}\right)^{0.1}
\tag{11.8.4}
$$

> **注意**：这些方程未使用最大内径，而是 $d_{\text{mean}}$（半翅高处的平均直径）。$\text{Nu}_L$ 中系数 0.045 是对该特定微翅片管拟合单相数据得到的（而非通用 Dittus-Boelter 系数 0.023）。因此**该方法不具通用性**，仅适用于该特定微翅片管几何。

### 11.8.2 Thome-Kattan-Favrat 微翅片流动沸腾模型

Thome, Kattan and Favrat (1997) 提出了一个新的微翅片流动沸腾模型，有效干度范围 0.15–0.81，热通量 2–47 kW/m²，质量通量 100–501 kg/m²s。

局部微翅片流动沸腾传热系数 $\alpha_{\text{mf}}$ 由渐近模型确定：

$$
\alpha_{\text{mf}} = E_{\text{mf}}\left[(\alpha_{\text{nb}})^3 + (E_{\text{RB}}\,\alpha_{\text{cb}})^3\right]^{1/3}
\tag{11.8.5}
$$

#### 核态沸腾项

$\alpha_{\text{nb}}$ 用 Cooper (1984) 有量纲核态池沸腾关联式（纯流体）计算：

$$
\alpha_{\text{nb}} = 55\,p_r^{0.12}\left(-\log_{10}p_r\right)^{-0.55}\,M^{-0.5}\,q^{0.67}
\tag{11.8.6}
$$

其中 $\alpha_{\text{nb}}$ 单位 W/m²K，$p_r$ 为对比压力，$M$ 为分子量，$q$ 为基于**全部内表面积**（非名义内径面积）的局部热通量（W/m²）。微翅片翅片效率假定为 100%。

#### 对流沸腾项

对流沸腾传热系数 $\alpha_{\text{cb}}$ 使用 Kattan, Thome and Favrat (1998c) 光管环状液膜湍流关联式：

$$
\alpha_{\text{cb}} = 0.0133\left(\text{Re}_L\right)_{\text{film}}^{0.69}\,\text{Pr}_L^{0.4}\left(k_L/\delta\right)
\tag{11.8.7}
$$

其中 $k_L$ 为液体热导率。常数 0.0133 和 0.69 为光管值（非微翅片数据拟合），已被证明可预测 R-123、R-134a、R-502、R-402A、R-404A、R-407C 和氨的流动沸腾数据。

液膜 Reynolds 数由环状液膜中液体平均速度确定：

$$
\left(\text{Re}_L\right)_{\text{film}} = \frac{4\dot{m}(1-x)\delta}{(1-\varepsilon)\mu_L}
\tag{11.8.8}
$$

其中 $\dot{m}$ 为总质量通量，$\varepsilon$ 为局部空隙率，$\delta$ 为局部液膜厚度（忽略微翅片影响），$x$ 为局部干度，$\mu_L$ 为液体动力粘度。

#### 空隙率

局部空隙率使用 Rouhani and Axelsson (1970) 漂移流模型关联式：

$$
\varepsilon = \left(\frac{x}{\rho_G}\right)\left\{\left[1 + 0.12(1-x)\right]\left(\frac{x}{\rho_G} + \frac{1-x}{\rho_L}\right) + \frac{1.18(1-x)\left[g\sigma(\rho_L - \rho_G)\right]^{0.25}}{\dot{m}^2\,\rho_L^{0.5}}\right\}^{-1}
\tag{11.8.9}
$$

其中 $g$ 为重力加速度（9.81 m/s²），$\sigma$ 为表面张力（全部 SI 单位）。

#### 液膜厚度

局部环状液膜厚度由液相截面积计算，假定均匀分布、忽略微翅片：

$$
\delta = \frac{(1-\varepsilon)\,d_f}{4}
\tag{11.8.10}
$$

$d_f$ 为微翅片管翅根处最大内径。

#### Ravigururajan-Bergles 强化因子

引入 Ravigururajan and Bergles (1985) 单相湍流肋管强化因子 $E_{\text{RB}}$，以考虑微翅片对对流沸腾系数的强化效应：

$$
E_{\text{RB}} = \left\{1 + \left[2.64\,\text{Re}_{\text{RB}}^{0.036}\,\text{Pr}_L^{-0.024}\left(\frac{e_f}{d_f}\right)^{0.212}\left(\frac{p_f}{d_f}\right)^{-0.21}\left(\frac{\alpha_f}{90°}\right)^{0.29}\right]^7\right\}^{1/7}
\tag{11.8.11}
$$

其中 $e_f$ 为微翅片高度（m），$p_f$ 为翅到翅的轴向节距（m），$\alpha_f$ 为微翅片螺旋角（°），$\text{Pr}_L$ 为液体 Prandtl 数。$\text{Re}_{\text{RB}}$ 为液相管流 Reynolds 数：

$$
\text{Re}_{\text{RB}} = \frac{\dot{m}(1-x)\,d_f}{\mu_L}
\tag{11.8.12}
$$

#### 微翅片附加强化因子

$E_{\text{RB}}$ 是管流（非液膜流）强化因子。为补偿 Gregorig 效应（液膜从翅顶向翅根汇聚加速蒸发）和质量通量效应，引入附加因子 $E_{\text{mf}}$（唯一基于微翅片试验数据拟合的因子）：

$$
E_{\text{mf}} = 1.89\left(\dot{m}/\dot{m}_{\text{ref}}\right)^2 - 3.7\left(\dot{m}/\dot{m}_{\text{ref}}\right) + 3.02
\tag{11.8.13}
$$

其中 $\dot{m}_{\text{ref}}$ 为用于无量纲化的参考值，取测试最大值 $\dot{m}_{\text{ref}} = 500$ kg/m²s。

**适用范围**：$E_{\text{mf}}$ 在 100 kg/m²s 时高达 2.36，在 500 kg/m²s 时低至 1.21，覆盖直接膨胀蒸发器的典型质量通量范围 50–500 kg/m²s。

**模型精度**（R-134a + R-123，362 个局部数据点）：

| 流体 | 标准偏差 | 平均偏差 | 均值偏差 |
|---|---|---|---|
| R-134a | 18.5% | 12.8% | 2.0% |
| R-123 | 12.9% | 11.8% | 6.4% |

**图 11.13** 展示了模型与 R-134a 测试数据在 200 kg/m²s 下的对比。**图 11.14** 展示了预测的局部强化比随质量通量的变化：低质量通量下强化大，高质量通量下趋近面积比。

**干涸处理**：模型覆盖干度至 0.85（假定为干涸起始点）。$x > 0.85$ 时，传热系数在 $x = 0.85$ 处的值和 $x = 1$ 处的气相传热系数之间线性内插，后者用 Ravigururajan and Bergles (1985) 单相肋管关联式计算。

#### 微翅片强化机理总结

1. 微翅片的单相效应增加对流贡献
2. 附加内表面积增加核态沸腾贡献
3. Gregorig 效应增强环状液膜蒸发
4. 低质量通量下将分层波状流（部分润湿）转化为环状流（完全润湿）

---

## 11.9 Correlation for Horizontal Tubes with Twisted Tape Insert

## 11.9 水平扭带插入件关联式

Kedzierski and Kim (1998) 基于一种扭带（$Y = 4.15$）的五种纯流体和两种共沸混合物的实验数据（1401 个数据点）提出了以下关联式。扭曲比 $Y$ 定义为带材旋转 180° 的管轴向长度除以管内径 $d_i$。

扭带流动沸腾传热系数 $\alpha_{tt}$（基于光管内径 $d_i$）与对比压力 $p_r$ 的关联式：

$$
\frac{\alpha_{tt}\,d_i}{k_L} = 1.356\,\text{Sw}^{c_1}\,\text{Pr}_L^{c_2}\,p_r^{c_3}\left(-\log_{10}p_r\right)^{c_4}\,\text{Bo}^{c_5}
\tag{11.9.1}
$$

旋流数 Sw：

$$
\text{Sw} = \frac{\text{Re}_s}{\sqrt{Y}}
\tag{11.9.2}
$$

旋流 Reynolds 数 $\text{Re}_s$：

$$
\text{Re}_s = \text{Re}_{L,t}\,\frac{\sqrt{1 + \left(\dfrac{\pi}{2Y}\right)^2}}{1 - \dfrac{4t}{\pi d_i}}
\tag{11.9.3}
$$

其中 $t$ 为扭带厚度。全液流 Reynolds 数 $\text{Re}_{L,t}$：

$$
\text{Re}_{L,t} = \frac{\rho_L\,\dot{m}\,d_i}{\mu_L}
\tag{11.9.4}
$$

沸腾数 Bo：

$$
\text{Bo} = \frac{q}{\dot{m}\,h_{LG}}
\tag{11.9.5}
$$

其中 $h_{LG}$ 为潜热，$q$ 为局部热通量，$\dot{m}$ 为总质量通量。

经验指数为干度 $x$ 的函数：

$$
c_1 = 0.993 - 1.18\,x + 0.899\,x^2
\tag{11.9.6}
$$

$$
c_2 = 1.108 - 2.366\,x + 1.451\,x^2
\tag{11.9.7}
$$

$$
c_3 = -2.383 + 5.255\,x - 1.791\,x^2
\tag{11.9.8}
$$

$$
c_4 = -3.195 + 6.668\,x
\tag{11.9.9}
$$

$$
c_5 = 1.073 - 2.679\,x + 1.443\,x^2
\tag{11.9.10}
$$

共使用 **15 个经验常数**。该方法与 Agrawal, Varma and Lal (1986) 的 R-12 数据（扭曲比 5.58）吻合良好。

> **校核注 [11.9.4]**：源页 328 公式图像**清晰显示** $\text{Re}_{L,t} = \rho_L \dot{m} d_i / \mu_L$，ρ_L 确实存在于分子中，并非 OCR 误读。译文忠实保留原书写法。但需注意：若 $\dot{m}$ 为质量通量（kg/m²s），则 $\rho_L \dot{m} d_i / \mu_L$ 的量纲为 [kg/m³ · kg/(m²·s) · m / (Pa·s)] = [kg/(m·s)]，**不是无量纲 Reynolds 数**。推测原书中 $\dot{m}$ 在此式可能实际表示的是体积通量或平均速度（m/s），使得 $\rho_L \dot{m} d_i / \mu_L$ 量纲正确。读者实施时应参照 Kedzierski and Kim (1998) 原论文确认定义。
