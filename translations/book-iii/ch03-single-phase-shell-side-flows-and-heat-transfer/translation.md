---
book_id: engineering-data-book-iii
source_file: "D:\\Knowledge-base\\books\\Engineering_Data_book\\第三部\\Engineering Data Book III OCR.pdf"
chapter: 3
chapter_title_en: Single-Phase Shell-Side Flows and Heat Transfer
chapter_title_zh: 单相壳侧流动与传热
source_pdf_pages: "47-66"
source_book_pages: "3-1 到 3-20"
status: complete_engineering_reading_draft
ocr_quality: prose_checked_against_source_pages_formula_ocr_untrusted
formula_check: equations_3_3_1_to_3_6_6_transcribed_with_source_page_trace
figure_check: source_pages_and_local_figure_table_crops_inserted
translation_scope: "第 3 章：折流板管壳式换热器壳侧单相流动、Taborek/Delaware 法、传热与压降修正、低翅片管束扩展"
---

# Chapter 3 Single-Phase Shell-Side Flows and Heat Transfer

# 第 3 章 单相壳侧流动与传热

## 来源追踪

| 项目 | 内容 |
|---|---|
| 原书 | Engineering Data Book III |
| 章节 | Chapter 3 |
| PDF 页码 | 47-66 |
| 书内页码 | 3-1 到 3-20 |
| 进度记录 | [progress.md](./progress.md) |

完整源页截图保留在 `assets/source-page-47.png` 到 `assets/source-page-66.png`，用于逐页二校和公式复核。正文只展示局部图表资产，避免整页原文图打断阅读。

## 摘要

本章介绍 Taborek（1983）针对单弓形折流板管壳式换热器单相[壳侧](../../../glossary/terms.md#term-shell-side)流动提出的设计方法。Taborek 版本的 [Delaware 法](../../../glossary/terms.md#term-delaware-method)被认为是公开文献中最准确、可靠且完整的方法之一。本章先给出带折流板换热器壳侧单相流动的基本理论，再完整说明 Taborek 方法如何应用于光管和整体低翅片管，例如 Wolverine Tube S/T Trufin 管。该方法依据管束几何和尺寸描述，预测壳侧传热系数和压降。

## 3.1 Introduction

## 3.1 引言

液体和气体横掠管束的单相流动，是许多换热器应用中都会遇到的重要传热过程。与管内单相传热相比，壳侧流动，也就是流体在壳体约束下横掠带折流板管束外侧的流动，要复杂得多，因为它受到许多几何因素影响，并存在多种可能的流路。

Tinker（1951）最早给出了这一过程的物理描述。该描述后来被用于发展通常称为 Delaware 法的壳侧设计方法；该方法由 Bell（1960，1963）提出，并在 Bell（1986）中重新发表。Taborek（1983）针对单弓形折流板管壳式换热器的单相壳侧流动提出了新的设计版本，主要适用于 TEMA E 壳程，并说明如何扩展到 TEMA J 壳程、F 壳程以及无窗口管的 E 壳程。

本章给出带折流板 E 壳换热器壳侧单相流动的基本理论，并进一步说明 Taborek 方法。该方法适用于单弓形折流板管束。特殊应用中还会使用双弓形折流板、三弓形折流板、盘环形折流板、杆式折流板和螺旋折流板；这些较少使用的几何形式不在本章处理范围内。本章先说明光管方法，再说明它对整体低翅片管的扩展。

## 3.2 Stream Analysis of Flow Distribution in a Baffled Heat Exchanger

## 3.2 带折流板换热器中的流量分布流路分析

在带折流板的[管壳式换热器](../../../glossary/terms.md#term-shell-and-tube-heat-exchanger)中，只有一部分壳侧流体真正按理想流路横掠管束、且方向垂直于管轴。其余流量会通过旁路区域流动。流体总是趋向于从入口到出口阻力较小的流路。在典型设计中，非理想流可占总流量的 40% 以内，因此必须把这些流路对传热和压降的影响计入设计。

Tinker（1951）首先直观描述了单弓形折流板实际换热器中的这些流路，如图 3.1 所示。他把总流量分成若干个以字母标识的流股。

![Fig. 3.1 Tinker 描述的带折流板换热器壳侧流路局部图](./assets/fig-3-1-original.png)

**A 流股：管孔泄漏流。** 管孔泄漏流是从一个折流板分室流到下一个分室、并穿过折流板上过大管孔与管外径之间环形开口的流动，如图 3.2 所示。驱动力是相邻折流板分室之间的压差。泄漏通道由折流板孔径与管外径之差形成的直径间隙决定。如果管子胀接到折流板中，则直径间隙为零。减小该直径间隙可降低该旁路流；间隙为零时，该流股被完全消除。

![Fig. 3.2 管孔泄漏流 A 示意图局部图](./assets/fig-3-2-original.png)

**B 流股：横掠管束流。** 横掠流是理想化的流动，方向垂直于管轴并横掠管束。这是带折流板管壳式换热器中最希望得到的流路，如图 3.1 所示。

**C 流股：管束旁路流。** 管束旁路流穿过管束外缘与壳体内壁之间的环形开口，如图 3.3 所示。该流路的直径间隙等于壳体内径减去管束外管限径。可通过减小壳体内径与管束外管限径之间的直径间隙来降低该旁路流，也可在管束周边安装成对密封条，阻挡该流路并迫使流体返回管束内部。

![Fig. 3.3 管束旁路流 C 示意图局部图](./assets/fig-3-3-original.png)

**E 流股：壳体-折流板旁路流。** 壳体-折流板旁路流指折流板外缘与壳体内壁之间间隙中的流动，如图 3.4 所示。直径间隙等于壳体内径减去折流板直径，可通过把壳体与折流板之间的制造间隙减小到可行下限来降低。

![Fig. 3.4 壳体-折流板旁路流 E 示意图局部图](./assets/fig-3-4-original.png)

**F 流股：管程隔板通道旁路流。** 多管程换热器为布置封头中的管程隔板，会在管束和管板上省去部分管子，从而形成开通道。沿流动方向布置的这类开通道会产生 F 流股，如图 3.1 所示。只有与流动方向一致的管程隔板通道才产生旁路；与流动方向垂直的通道不产生旁路。该旁路流只出现在部分多管程布管中，可通过在每条旁路通道中布置若干根假管来消除，使流体重新进入管束。

## 3.3 Definition of Bundle and Shell Geometries

## 3.3 管束和壳体几何定义

图 3.5 给出了两端为固定管板的单弓形折流板管壳式管束几何。壳侧流体从管束一端到另一端完成一个壳程，折流板引导流体横掠管束。这是制冷和石化换热器中常见构型。入口、中央和出口折流板间距分别记为 L<sub>bi</sub>、L<sub>bc</sub> 和 L<sub>bo</sub>。L<sub>bi</sub> 和 L<sub>bo</sub> 通常与 L<sub>bc</sub> 相等，除非第一和最后一个折流板分室必须加大，以容纳相应的壳侧接管。

![Fig. 3.5 单弓形管壳式换热器折流板间距局部图](./assets/fig-3-5-original.png)

折流板布置由入口、中央和出口折流板间距以及有效管长确定。有效管长 L<sub>ta</sub> 等于总管长减去两块管板厚度之和。折流板数量必须为整数，折流板间距也由这些值确定。对 U 形管换热器，用于确定折流板间距的有效长度包括直管段长度加 D<sub>s</sub>/2，其中 D<sub>s</sub> 是壳体内径。因此，U 形弯头处的折流板间距应包括该分室中的直管长度再加 D<sub>s</sub>/2。

图 3.5、图 3.6 和图 3.7 取自 Taborek（1983），定义了主要换热器尺寸。D<sub>otl</sub> 是外管限径，D<sub>ctl</sub> 是管中心线限径；注意 D<sub>ctl</sub> = D<sub>otl</sub> - D<sub>t</sub>，其中 D<sub>t</sub> 为管外径。折流板切口高度为 L<sub>bch</sub>，折流板切口 B<sub>c</sub> 定义为 (L<sub>bch</sub>/D<sub>s</sub>) × 100%，也就是按壳体内径百分比表示。壳体内径 D<sub>s</sub> 与外管限径 D<sub>otl</sub> 之间的直径间隙为 L<sub>bb</sub>，其中 L<sub>bb</sub>/2 是该旁路通道的宽度。图中还示出了宽度为 L<sub>p</sub> 的管程隔板通道。壳体内径 D<sub>s</sub> 与折流板直径 D<sub>b</sub> 之间的直径间隙为 L<sub>sb</sub>，对应单侧间隙 L<sub>sb</sub>/2。

![Fig. 3.6 折流板和管束几何局部图](./assets/fig-3-6-original.png)

![Fig. 3.7 折流板切口和间隙局部图](./assets/fig-3-7-original.png)

上述尺寸 D<sub>s</sub>、D<sub>otl</sub>、折流板切口、L<sub>bb</sub> 和 L<sub>sb</sub> 可从换热器布管图获得。如果 D<sub>otl</sub> 未知，可按下列典型 TEMA 取值估算 L<sub>bb</sub>：当 D<sub>s</sub> < 300 mm 时取 9.525 mm；当 D<sub>s</sub> > 1000 mm 时取 15.875 mm；当 D<sub>s</sub> 在 300 到 1000 mm 之间时取 12.7 mm。这些值是 TEMA 换热器规格的典型值，但直接膨胀蒸发器常采用更小间隙。

如果 L<sub>sb</sub> 未知，可取 D<sub>s</sub> < 400 mm 时 L<sub>sb</sub> = 2.0 mm；更大壳体可取 L<sub>sb</sub> = 1.6 + 0.004D<sub>s</sub>，单位为 mm。若折流板孔与管外径之间的直径间隙未知，可采用 TEMA 最大值 0.794 mm，或采用 0.397 到 0.794 mm 范围内的较小值。该间隙等于折流板孔径减去 D<sub>t</sub>。减小该间隙可显著改善热工性能。

Taborek 设计方法处理图 3.8 所示的三种布管：30°、45° 和 90°，不包括 60° 布管。管间距 L<sub>tp</sub> 定义为管束中相邻管中心距。平行于流动方向的节距为 L<sub>pp</sub>，垂直于流动方向的节距为 L<sub>pn</sub>。

![Fig. 3.8 布管形式局部图](./assets/fig-3-8-original.png)

给定壳径内可容纳的管数取决于若干几何因素、尺寸和间隙，主要包括布管形式（三角形、正方形或旋转正方形）和管间距。Taborek（1983）给出了一个适用于固定管板、单管程、且入口和出口接管区域不抽管时的简单估算式：

$$
N_{tt}
=
\frac{0.7854D_{ctl}^2}
{C_lL_{tp}^2}
\tag{3.3.1}
$$

其中 N<sub>tt</sub> 是管数，D<sub>ctl</sub> 是管中心线限径，L<sub>tp</sub> 是管间距。对 90° 正方形布管和 45° 旋转正方形布管，常数 C<sub>l</sub> = 1.0；对 30° 三角形布管，C<sub>l</sub> = 0.866。多管程设计（2、4 等）很常见，其管数通常少于上式结果。推荐使用管数计算软件获得准确估计，因为入口接管处常因设置防冲板而抽管，抽管数量又取决于接管直径。准确管数会提高传热和压降计算精度。

## 3.4 Stream Analysis of Heat Transfer in a Baffled Heat Exchanger

## 3.4 带折流板换热器中的传热流路分析

单相壳侧流动的流路分析传热系数 α<sub>ss</sub> 为：

$$
\alpha_{ss}
=
\left(J_CJ_LJ_BJ_RJ_SJ_\mu\right)\alpha_1
\tag{3.4.1}
$$

其中 α<sub>1</sub> 是理想管束传热系数，按全部流量都横掠管束计算，也就是全部流量都假定属于 B 流股。J<sub>C</sub>、J<sub>L</sub>、J<sub>B</sub>、J<sub>R</sub> 和 J<sub>S</sub> 是泄漏和旁路流影响修正因子，J<sub>μ</sub> 是壁面黏度修正因子。下文说明这些修正因子和理想管束传热关联式。α<sub>ss</sub> 是整个管束的平均值，作用面积为管外侧传热面积。关联式采用平均主体物性。

### 3.4.1 Baffle Cut Correction Factor (J<sub>C</sub>)

### 3.4.1 折流板切口修正因子 J<sub>C</sub>

折流板切口修正因子 J<sub>C</sub> 反映窗口流对传热的非理想影响。窗口流速度不等于横掠管束速度，随折流板切口大小和折流板间距不同，可高于或低于横掠流速度。此外，窗口流部分方向沿管长，换热效果低于横掠流。因此，J<sub>C</sub> 是折流板切口、外管限径和窗口流面积的函数，计算式为：

$$
J_C
=
0.55+0.72F_C
\tag{3.4.2}
$$

其中：

$$
F_C
=
1-2F_W
\tag{3.4.3}
$$

F<sub>W</sub> 是窗口占据的截面积分数：

$$
F_W
=
\frac{\theta_{ctl}}{360}
-
\frac{\sin\theta_{ctl}}{2\pi}
\tag{3.4.4}
$$

折流板切口相对于换热器中心线的角度 θ<sub>ctl</sub> 以度计：

$$
\theta_{ctl}
=
2\cos^{-1}
\left\{
\frac{D_s}{D_{ctl}}
\left[
1-2\left(\frac{B_c}{100}\right)
\right]
\right\}
\tag{3.4.5}
$$

上述表达式适用于折流板切口为壳体直径 15% 到 45% 的范围。通常不建议采用该范围以外的折流板切口，因为会造成流量分布不良。在良好设计中，J<sub>C</sub> 通常在 0.65 到 1.175 之间。

### 3.4.2 Baffle Leakage Correction Factor (J<sub>L</sub>)

### 3.4.2 折流板泄漏修正因子 J<sub>L</sub>

相邻折流板分室之间的压差，会驱动一部分流体穿过折流板上的管孔间隙（A 流股），以及穿过壳体与折流板边缘之间的环形间隙（E 流股）。这些流股会减少横掠管束的 B 流股，从而同时降低传热系数和压降。E 流股对热工设计尤其不利，因为它基本不参与有效传热。折流板泄漏修正因子为：

$$
J_L
=
0.44(1-r_s)
+
\left[
1-0.44(1-r_s)
\right]
\exp(-2.2r_{lm})
\tag{3.4.6}
$$

其中：

$$
r_s
=
\frac{S_{sb}}{S_{sb}+S_{tb}}
\tag{3.4.7}
$$

以及：

$$
r_{lm}
=
\frac{S_{sb}+S_{tb}}{S_m}
\tag{3.4.8}
$$

壳体-折流板泄漏面积 S<sub>sb</sub>、N<sub>tt</sub>(1-F<sub>W</sub>) 个管孔对应的管-折流板孔泄漏面积 S<sub>tb</sub>，以及管束中心线处横掠流面积 S<sub>m</sub> 为：

$$
S_{sb}
=
0.00436D_sL_{sb}(360-\theta_{ds})
\tag{3.4.9}
$$

$$
S_{tb}
=
\left[
\frac{\pi}{4}
\left((D_t+L_{tb})^2-D_t^2\right)
\right]
N_{tt}(1-F_W)
\tag{3.4.10}
$$

$$
S_m
=
L_{bc}
\left[
L_{bb}
+
\frac{D_{ctl}}{L_{tp,eff}}
(L_{tp}-D_t)
\right]
\tag{3.4.11}
$$

式中，L<sub>sb</sub> 是壳体到折流板的直径间隙。折流板切口角 θ<sub>ds</sub> 以度计：

$$
\theta_{ds}
=
2\cos^{-1}
\left[
1-2\left(\frac{B_c}{100}\right)
\right]
\tag{3.4.12}
$$

L<sub>bc</sub> 为中央折流板间距，L<sub>bb</sub> 为旁路通道直径间隙。有效管间距 L<sub>tp,eff</sub> 对 30° 和 90° 布管等于 L<sub>tp</sub>，对 45° 错列布管等于 0.707L<sub>tp</sub>。对比例适当的换热器，J<sub>L</sub> 通常大于 0.7 到 0.9；应避免 J<sub>L</sub> 小于 0.6。J<sub>L</sub> 最大值为 1.0。制冷冷水机组和水冷冷凝器因制造公差和间隙小于 TEMA 标准，通常可达到 0.85 到 0.90。

### 3.4.3 Bundle Bypass Correction Factor (J<sub>B</sub>)

### 3.4.3 管束旁路修正因子 J<sub>B</sub>

管束旁路修正因子 J<sub>B</sub> 反映壳体内壁与管束之间流动（C 流股）以及沿流动方向的管程隔板通道旁路流（F 流股）的不利影响。F 流股并不总是存在，且可通过在管程隔板通道中布置假管完全消除。C 流股可通过提高管束与壳体配合紧密程度来降低，也可在管束周边布置密封条；密封条成对安装，最多可达到在两个折流板切口之间每两排横掠管排设置一对。管束旁路修正因子为：

$$
J_B
=
\exp
\left[
-C_{bh}F_{sbp}
\left(1-\sqrt[3]{2r_{ss}}\right)
\right]
\tag{3.4.13}
$$

经验因子 C<sub>bh</sub> 在层流（Re ≤ 100）时取 1.35，在过渡和湍流（Re > 100）时取 1.25。计算该式需要旁路面积与横掠流面积之比 F<sub>sbp</sub>，以及密封条对数 N<sub>ss</sub> 与一个折流板区段内折流板尖端之间横掠管排数 N<sub>tcc</sub> 的比值 r<sub>ss</sub>。首先：

$$
F_{sbp}
=
\frac{S_b}{S_m}
\tag{3.4.14}
$$

其中 S<sub>m</sub> 已在前文给出，S<sub>b</sub> 为旁路面积：

$$
S_b
=
L_{bc}
\left[
(D_s-D_{otl})+L_{pl}
\right]
\tag{3.4.15}
$$

L<sub>pl</sub> 表示管间旁路通道宽度。没有管程隔板通道，或该通道垂直于流动方向时，取 L<sub>pl</sub> = 0；当管程隔板通道平行于流动方向时，L<sub>pl</sub> 等于该通道实际尺寸的一半，也可近似取为管外径 D<sub>t</sub>。r<sub>ss</sub> 为：

$$
r_{ss}
=
\frac{N_{ss}}{N_{tcc}}
\tag{3.4.16}
$$

N<sub>tcc</sub> 由下式得到：

$$
N_{tcc}
=
\frac{D_s}{L_{pp}}
\left[
1-2\left(\frac{B_c}{100}\right)
\right]
\tag{3.4.17}
$$

其中，对 30° 布管 L<sub>pp</sub> = 0.866L<sub>tp</sub>，对 90° 布管 L<sub>pp</sub> = L<sub>tp</sub>，对 45° 布管 L<sub>pp</sub> = 0.707L<sub>tp</sub>。当 r<sub>ss</sub> ≥ 1/2 时，J<sub>B</sub> 的上限为 1。

### 3.4.4 Unequal Baffle Spacing Correction Factor (J<sub>S</sub>)

### 3.4.4 不等折流板间距修正因子 J<sub>S</sub>

不等折流板间距修正因子 J<sub>S</sub> 反映入口折流板间距 L<sub>bi</sub> 和/或出口折流板间距 L<sub>bo</sub> 大于中央折流板间距 L<sub>bc</sub> 时的不利影响。有些换热器为了布置壳侧接管，并避免与本体法兰或第一块折流板重叠，会把入口和出口接管分室的折流板间距做得大于中央折流板间距。这样会降低这些分室中的流速并降低传热。若入口和出口间距大于中央间距，则 J<sub>S</sub> < 1.0；若三者相等，则无需修正，J<sub>S</sub> = 1.0。J<sub>S</sub> 直接由流速影响确定：

$$
J_S
=
\frac{
(N_b-1)
+(L_{bi}/L_{bc})^{1-n}
+(L_{bo}/L_{bc})^{1-n}
}{
(N_b-1)
+(L_{bi}/L_{bc})
+(L_{bo}/L_{bc})
}
\tag{3.4.18}
$$

其中，湍流取 n = 0.6，层流取 n = 1/3。折流板分室数 N<sub>b</sub> 由有效管长和折流板间距确定。

### 3.4.5 Laminar Flow Correction Factor (J<sub>R</sub>)

### 3.4.5 层流修正因子 J<sub>R</sub>

在层流中，流动沿通道热发展时会在边界层中形成不利温度梯度，从而降低传热。层流修正因子 J<sub>R</sub> 计入该影响。对壳侧层流，J<sub>R</sub> < 1.0，即 Re ≤ 100；对 Re > 100，不需要修正，J<sub>R</sub> = 1.0。当 Re ≤ 20 时：

$$
J_R
=
(J_R)_{20}
=
\left(
\frac{10}{N_c}
\right)^{0.18}
\tag{3.4.19}
$$

其中 N<sub>c</sub> 是整个换热器中流动横掠的总管排数：

$$
N_c
=
(N_{tcc}+N_{tcw})(N_b+1)
\tag{3.4.20}
$$

折流板尖端之间的横掠管排数 N<sub>tcc</sub> 已在前文给出；窗口区横掠管排数 N<sub>tcw</sub> 为：

$$
N_{tcw}
=
\frac{0.8}{L_{pp}}
\left[
D_s\left(\frac{B_c}{100}\right)
-
\frac{D_s-D_{ctl}}{2}
\right]
\tag{3.4.21}
$$

当 20 < Re < 100 时，J<sub>R</sub> 按下式线性插值：

$$
J_R
=
(J_R)_{20}
+
\left(
\frac{20-Re}{80}
\right)
\left[
(J_R)_{20}-1
\right]
\tag{3.4.22}
$$

所有情况下，J<sub>R</sub> 的最小值为 0.4。

### 3.4.6 Wall Viscosity Correction Factor (J<sub>μ</sub>)

### 3.4.6 壁面黏度修正因子 J<sub>μ</sub>

传热和压降关联式通常用进出口温度平均值下的主体物性计算。对液体加热和冷却，主体流体温度与壁温之间物性变化的影响用黏度比 J<sub>μ</sub> 修正，即主体黏度 μ 与壁温黏度 μ<sub>wall</sub> 之比：

$$
J_\mu
=
\left(
\frac{\mu}{\mu_{wall}}
\right)^m
\tag{3.4.23}
$$

壳侧流体被加热时，该修正因子大于 1.0；被冷却时相反。液体加热和冷却通常取指数 m = 0.14。对气体，气体被冷却时不需要修正；气体被加热时采用基于温度而非黏度的修正：

$$
J_\mu
=
\left(
\frac{T+273}{T_{wall}+273}
\right)^{0.25}
\tag{3.4.24}
$$

其中 T 是主体温度，T<sub>wall</sub> 是壁温。必须先通过初步传热计算得到壁温，再确定壁温下的黏度。

### 3.4.7 Ideal Tube Bank Heat Transfer Coefficient (α<sub>1</sub>)

### 3.4.7 理想管束传热系数 α<sub>1</sub>

理想管束传热系数 α<sub>1</sub> 按全部流量都横掠管束计算，也就是换热器内全部流量均假定属于 B 流股且没有旁路流：

$$
\alpha_1
=
j_1c_p\dot mPr^{-2/3}
\tag{3.4.25}
$$

流体质量通量 \dot m 基于通过最小法向流通面积的总流量 M，单位为 kg/m<sup>2</sup>s。Pr 为普朗特数。传热因子 j<sub>1</sub> 为：

$$
j_1
=
a_1
\left(
\frac{1.33}{L_{tp}/D_t}
\right)^a
Re^{a_2}
\tag{3.4.26}
$$

其中：

$$
a
=
\frac{a_3}
{1+0.14Re^{a_4}}
\tag{3.4.27}
$$

a<sub>1</sub>、a<sub>2</sub>、a<sub>3</sub> 和 a<sub>4</sub> 的取值列于 Taborek（1983）给出的表 3.1。上述方法中的壳侧横掠流质量通量按管束最大横截面处计算：

$$
\dot m
=
\frac{M}{S_m}
\tag{3.4.28}
$$

其中 M 为壳侧质量流率，单位 kg/s，S<sub>m</sub> 已在前文定义。壳侧 Reynolds 数为：

$$
Re
=
\frac{D_t\dot m}{\mu}
\tag{3.4.29}
$$

Prandtl 数定义为：

$$
Pr
=
\frac{c_p\mu}{k}
\tag{3.4.30}
$$

物性，包括黏度 μ、定压比热 c<sub>p</sub> 和导热系数 k，均在平均主体流体温度下评价。有效管长 L<sub>ta</sub> 用于计算实际外侧传热面积 A<sub>o</sub>：

$$
A_o
=
\pi D_tL_{ta}N_{tt}
\tag{3.4.31}
$$

其中 N<sub>tt</sub> 为管束管数。

![Table 3.1 j1 和 f1 计算用经验系数局部图](./assets/table-3-1-original.png)

### Table 3.1 Empirical coefficients for calculation of j<sub>1</sub> and f<sub>1</sub>

### 表 3.1 j<sub>1</sub> 和 f<sub>1</sub> 计算用经验系数

| 布管角 | Re 范围 | a<sub>1</sub> | a<sub>2</sub> | a<sub>3</sub> | a<sub>4</sub> | b<sub>1</sub> | b<sub>2</sub> | b<sub>3</sub> | b<sub>4</sub> |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 30° | 10<sup>5</sup>-10<sup>4</sup> | 0.321 | -0.388 | 1.450 | 0.519 | 0.372 | -0.123 | 7.00 | 0.500 |
| 30° | 10<sup>4</sup>-10<sup>3</sup> | 0.321 | -0.388 | 1.450 | 0.519 | 0.486 | -0.152 | 7.00 | 0.500 |
| 30° | 10<sup>3</sup>-10<sup>2</sup> | 0.593 | -0.477 | 1.450 | 0.519 | 4.570 | -0.476 | 7.00 | 0.500 |
| 30° | 10<sup>2</sup>-10 | 1.360 | -0.657 | 1.450 | 0.519 | 45.10 | -0.973 | 7.00 | 0.500 |
| 30° | <10 | 1.400 | -0.667 | 1.450 | 0.519 | 48.00 | -1.000 | 7.00 | 0.500 |
| 45° | 10<sup>5</sup>-10<sup>4</sup> | 0.370 | -0.396 | 1.930 | 0.500 | 0.303 | -0.126 | 6.59 | 0.520 |
| 45° | 10<sup>4</sup>-10<sup>3</sup> | 0.370 | -0.396 | 1.930 | 0.500 | 0.333 | -0.136 | 6.59 | 0.520 |
| 45° | 10<sup>3</sup>-10<sup>2</sup> | 0.730 | -0.500 | 1.930 | 0.500 | 3.500 | -0.476 | 6.59 | 0.520 |
| 45° | 10<sup>2</sup>-10 | 0.498 | -0.656 | 1.930 | 0.500 | 26.20 | -0.913 | 6.59 | 0.520 |
| 45° | <10 | 1.550 | -0.667 | 1.930 | 0.500 | 32.00 | -1.000 | 6.59 | 0.520 |
| 90° | 10<sup>5</sup>-10<sup>4</sup> | 0.370 | -0.395 | 1.187 | 0.370 | 0.391 | -0.148 | 6.30 | 0.378 |
| 90° | 10<sup>4</sup>-10<sup>3</sup> | 0.107 | -0.266 | 1.187 | 0.370 | 0.0815 | +0.022 | 6.30 | 0.378 |
| 90° | 10<sup>3</sup>-10<sup>2</sup> | 0.408 | -0.460 | 1.187 | 0.370 | 6.0900 | -0.602 | 6.30 | 0.378 |
| 90° | 10<sup>2</sup>-10 | 0.900 | -0.631 | 1.187 | 0.370 | 32.100 | -0.963 | 6.30 | 0.378 |
| 90° | <10 | 0.970 | -0.667 | 1.187 | 0.370 | 35.000 | -1.000 | 6.30 | 0.378 |

## 3.5 Stream Analysis of Shell-Side Pressure Drop in a Baffled Heat Exchanger

## 3.5 带折流板换热器中的壳侧压降流路分析

![Fig. 3.9 壳侧流动压降区域局部图](./assets/fig-3-9-original.png)

壳侧流动压降等于入口接管压降、管束压降和出口接管压降之和。入口和出口接管压降可近似为各等于 2 个速度头。管束压降等于横掠流压降 Δp<sub>c</sub>、窗口流压降 Δp<sub>w</sub> 和两个端部区域（第一和最后一个折流板分室）压降 Δp<sub>e</sub> 之和，如图 3.9 所示。不包括接管或防冲板时，管束总压降为：

$$
\Delta p_{total}
=
\Delta p_c+\Delta p_w+\Delta p_e
\tag{3.5.1}
$$

折流板尖端之间横掠管束的压降 Δp<sub>c</sub>，以中央折流板间距 L<sub>bc</sub> 下一个折流板分室的理想管束压降 Δp<sub>b1</sub> 为基础。该压降覆盖中央折流板分室中折流板切口之间的横掠流区域。所有中央折流板分室中的压降为：

$$
\Delta p_c
=
\Delta p_{b1}(N_b-1)R_BR_L
\tag{3.5.2}
$$

其中 Δp<sub>b1</sub> 是 N<sub>b</sub> 个分室中单个折流板分室的理想管束压降，并基于前文定义的质量通量。其表达式为：

$$
\Delta p_{b1}
=
0.002f_1N_{tc}
\frac{\dot m^2}{\rho}
R_\mu
\tag{3.5.3}
$$

摩擦因子 f<sub>1</sub> 为：

$$
f_1
=
b_1
\left(
\frac{1.33}{L_{tp}/D_t}
\right)^b
Re^{b_2}
\tag{3.5.4}
$$

其中：

$$
b
=
\frac{b_3}
{1+0.14Re^{b_4}}
\tag{3.5.5}
$$

经验常数 b、b<sub>1</sub>、b<sub>2</sub>、b<sub>3</sub> 和 b<sub>4</sub> 来自表 3.1。压降中的黏度修正因子 R<sub>μ</sub> 为：

$$
R_\mu
=
\left(
\frac{\mu}{\mu_w}
\right)^{-m}
\tag{3.5.6}
$$

m 的取值同前。旁路压降修正因子 R<sub>B</sub> 为：

$$
R_B
=
\exp
\left[
-C_{bp}F_{sbp}
\left(1-\sqrt[3]{2r_{ss}}\right)
\right]
\tag{3.5.7}
$$

当 r<sub>ss</sub> ≥ 1/2 时，R<sub>B</sub> 取上限 1。F<sub>sbp</sub> 已在前文定义。经验因子 C<sub>bp</sub> 对层流（Re ≤ 100）取 4.5，对过渡和湍流（Re > 100）取 3.7。泄漏压降修正因子 R<sub>L</sub> 为：

$$
R_L
=
\exp
\left[
-1.33(1+r_s)r_{lm}^{p}
\right]
\tag{3.5.8}
$$

r<sub>s</sub> 和 r<sub>lm</sub> 已在前文定义，指数 p 为：

$$
p
=
-0.15(1+r_s)+0.8
\tag{3.5.9}
$$

对湍流（Re > 100），所有 N<sub>b</sub> 个窗口区的压降和质量通量为：

$$
\Delta p_w
=
N_b
\left[
(2+0.6N_{tcw})
\frac{0.001\dot m_w^2}{2\rho}
\right]
R_LR_\mu
\tag{3.5.10}
$$

$$
\dot m_w
=
\frac{M}{\sqrt{S_mS_w}}
\tag{3.5.11}
$$

其中 M 为壳侧质量流率，单位 kg/s。S<sub>m</sub> 和 S<sub>w</sub> 由前文相应表达式求得。式中的 0.6 表示摩擦效应，因子 2 表示窗口内流动转向产生的速度头。对层流（Re ≤ 100），对应表达式为：

$$
\Delta p_w
=
N_b
\left\{
26
\left(
\frac{\dot m_w\mu}{\rho}
\right)
\left[
\frac{N_{tcw}}{L_{tp}-D_t}
+
\frac{L_{bc}}{D_w^2}
\right]
+
\left[
\frac{0.002\dot m_w^2}{2\rho}
\right]
\right\}
R_LR_\mu
\tag{3.5.12}
$$

括号内第一项表示横掠流贡献，第二项表示纵向流贡献。折流板窗口的水力直径为：

$$
D_w
=
\frac{4S_w}
{\pi D_tN_{tw}+(\pi D_s\theta_{ds}/360)}
\tag{3.5.13}
$$

θ<sub>ds</sub> 已在前文定义。N<sub>tw</sub> 是窗口中的管数，由总管数 N<sub>tt</sub> 确定：

$$
N_{tw}
=
N_{tt}F_W
\tag{3.5.14}
$$

S<sub>w</sub> 是窗口净流通面积：

$$
S_w
=
S_{wg}-S_{wt}
\tag{3.5.15}
$$

窗口中 N<sub>tw</sub> 根管占据的面积 S<sub>wt</sub> 为：

$$
S_{wt}
=
N_{tw}
\left(
\frac{\pi}{4}D_t^2
\right)
\tag{3.5.16}
$$

不考虑窗口中管子时的窗口总流通面积 S<sub>wg</sub> 为：

$$
S_{wg}
=
\frac{\pi D_s^2}{4}
\left(
\frac{\theta_{ds}}{360}
-
\frac{\sin\theta_{ds}}{2\pi}
\right)
\tag{3.5.17}
$$

管束两个端部区域的压降为：

$$
\Delta p_e
=
\Delta p_{b1}
\left(
1+\frac{N_{tcw}}{N_{tcc}}
\right)
R_BR_S
\tag{3.5.18}
$$

入口和/或出口折流板间距相对于中央折流板间距不等时，压降修正因子 R<sub>S</sub> 为：

$$
R_S
=
\left(
\frac{L_{bc}}{L_{bo}}
\right)^{2-n}
+
\left(
\frac{L_{bc}}{L_{bi}}
\right)^{2-n}
\tag{3.5.19}
$$

N<sub>tcw</sub> 和 N<sub>tcc</sub> 已在前文定义，Δp<sub>b1</sub>、R<sub>B</sub> 和 R<sub>μ</sub> 的计算方法也已给出。所有折流板间距相等时，R<sub>S</sub> = 2。上式中，层流（Re < 100）取 n = 1，湍流取 n = 0.2。

## 3.6 Stream Analysis Applied to Low Finned Tube Bundles

## 3.6 流路分析在低翅片管束中的应用

本节采用 Taborek（1983）的修正，把上述光管方法应用于整体低翅片管束。

### 3.6.1 Low Finned Tubes and Applications

### 3.6.1 低翅片管及其应用

[低翅片管](../../../glossary/terms.md#term-low-finned-tube)是适用于壳侧单相流动的优良传热强化形式，对液体流动有效，对气体流动通常更有利。图 3.10 给出了整体低翅片管的几何示意。其特征尺寸包括：光管端管径 D<sub>t</sub>；翅顶管径 D<sub>fo</sub>，通常等于 D<sub>t</sub>；翅根直径 D<sub>fr</sub>；翅片区管内径 D<sub>ti</sub>；翅片厚度 L<sub>fs</sub>；每米翅片数 N<sub>f</sub>；以及单位长度实际润湿面积 A<sub>of</sub>。

![Fig. 3.10 整体低翅片管几何局部图](./assets/fig-3-10-original.png)

图 3.11 是 Wolverine Tube 若干低翅片管的照片。整体低翅片管几乎可用常见换热管材料制造。常见翅片密度为每米 630 片到 1000 片以上，通常按每英寸翅片数定义，例如 19 fpi、26 fpi、28 fpi 和 30 fpi 管。典型最大翅高约 1.5 mm，翅厚常约 0.3 mm。整体低翅片管的尺寸表可从 Wolverine Tube Inc. 网站获得。

![Fig. 3.11 Wolverine Tube 低翅片管样品局部图](./assets/fig-3-11-original.png)

对许多单相流动，采用整体低翅片管比采用光管更有利。低翅片管适用于壳侧（外侧）传热系数远小于管侧传热系数的应用，也适用于壳侧[污垢热阻](../../../glossary/terms.md#term-fouling-resistance)控制设计的应用。前一种情况常出现在：壳侧流动处于湍流低端、过渡流或层流区；允许压降低，需要采用较大折流板切口和较大折流板间距；或管内采用螺旋翅片、内肋等传热强化结构时。

低翅片管另一个重要优点是它对壳侧污垢热阻具有有利影响。壳侧污垢系数施加在总润湿面积上，而该面积约为光管的 3 到 4 倍；若采用与光管设计相同的污垢系数值，则有效污垢热阻被降低到原来的约 1/3 到 1/4。对污垢系数较大或污垢热阻显著的场合，即使污垢系数只是中等水平，低翅片管的大面积比也可显著提高总传热系数。因此，使用低翅片管的作用包括提高壳侧传热系数、降低壳侧污垢热阻、提高管侧速度和传热系数；同时，翅片区管内径 D<sub>ti</sub> 小于管端光管段内径。

需要注意，当采用外低翅片管时，应使用翅片区管内径 D<sub>ti</sub> 来确定管侧传热系数和压降。最有效的低翅片几何可通过比较几种翅片密度确定。如果腐蚀裕量重要，应使用较厚翅片。若腐蚀裕量很大，则翅片可能并不适用，因为翅片可能会被腐蚀消耗掉。

### 3.6.2 Heat Transfer and Pressure Drops with Low Finned Tubes

### 3.6.2 低翅片管传热和压降

Taborek（1983）在同一文献中把光管流路分析方法扩展到整体低翅片管束。下文给出对上述设计方程的修改。低翅片管束壳侧传热系数随后用于计算总传热系数，此时必须计入低翅片的[翅片效率](../../../glossary/terms.md#term-fin-efficiency)。

**输入数据。** 为计算低翅片管束壳侧热工性能，还需要以下附加信息：

| 项目 | 符号 |
|---|---|
| 翅顶直径 | D<sub>fo</sub> |
| 翅根直径 | D<sub>fr</sub> |
| 单位管长翅片数 | N<sub>f</sub> |
| 平均翅片厚度（按矩形轮廓假定） | L<sub>fs</sub> |
| 低翅片管单位长度润湿面积 | A<sub>of</sub> |
| 管-折流板孔间隙 | L<sub>tb</sub> |

确定 L<sub>tb</sub> 时，用 D<sub>fo</sub> 代替 D<sub>t</sub>。通常 D<sub>fo</sub> 等于或略小于 D<sub>t</sub>。

**传热和流动几何。** 对低翅片管束壳侧传热系数 α<sub>ss</sub> 所采用的总传热面积为 A<sub>o</sub>。对低翅片管：

$$
A_o
=
A_{of}L_{ta}N_{tt}
\tag{3.6.1}
$$

整体低翅片管的等效投影面积小于相同直径光管，因为沿流动方向相邻翅片之间存在开口。因此，“熔平”或等效投影直径 D<sub>req</sub> 是管几何和翅片密度的函数：

$$
D_{req}
=
D_{fr}+2L_{fh}N_fL_{fs}
\tag{3.6.2}
$$

翅高 L<sub>fh</sub> 为：

$$
L_{fh}
=
\frac{D_{fo}-D_{fr}}{2}
\tag{3.6.3}
$$

因此，在光管管束关联式和几何方程中，凡出现光管直径 D<sub>t</sub>，均按下列规则用 D<sub>req</sub> 或指定直径替换：

| 计算项 | 替换规则 |
|---|---|
| S<sub>m</sub> 计算 | 用 D<sub>req</sub> 代替 D<sub>t</sub> |
| Re 计算 | 用 D<sub>req</sub> 代替 D<sub>t</sub> |
| S<sub>wt</sub> 计算 | 用 D<sub>fo</sub> 代替 D<sub>t</sub> |

**理想管束 j<sub>1</sub>。** 对 Re > 1000，光管方法可直接用于低翅片管，但 Re 应用 D<sub>req</sub> 而非 D<sub>t</sub> 计算。当 Re < 1000 时，翅片上的层流边界层开始重叠并降低传热。该影响按下式修正，仅适用于 Re < 1000：

$$
j_1
=
J_fj_{1,plain}
\tag{3.6.4}
$$

Taborek（1983）给出了 J<sub>f</sub> 随 log Re 从 Re = 20 到 Re = 1000 变化的图线，其中 Re = 1000 时 J<sub>f</sub> = 1.0。这里将该曲线拟合为：

$$
J_f
=
0.58+0.42
\left(
\frac{\log(Re/20)}
{\log(1000/20)}
\right)
\tag{3.6.5}
$$

**理想管束 f<sub>1</sub>。** 与相同光管管束相比，低翅片管束具有更大的等效横掠流面积，因为翅片之间提供了额外流通面积。低翅片管的摩擦因子约为光管的 1.4 倍；不过，沿流动方向翅片间开口增大流通面积而导致的较低速度，已在 Reynolds 数 Re 中计入。低翅片管束摩擦因子计算时，先使用低翅片管的 Re 和 D<sub>req</sub>，按光管关联式计算 f<sub>1,plain</sub>，然后乘以 1.4：

$$
f_1
=
1.4f_{1,plain}
\tag{3.6.6}
$$

**算例。** Taborek（1983）中有一个详细六页算例，建议读者参考。
