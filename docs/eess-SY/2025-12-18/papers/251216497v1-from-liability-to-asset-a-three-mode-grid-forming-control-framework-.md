---
layout: default
title: From Liability to Asset: A Three-Mode Grid-Forming Control Framework for Centralized Data Center UPS Systems
---

# From Liability to Asset: A Three-Mode Grid-Forming Control Framework for Centralized Data Center UPS Systems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16497" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16497v1</a>
  <a href="https://arxiv.org/pdf/2512.16497.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16497v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16497v1', 'From Liability to Asset: A Three-Mode Grid-Forming Control Framework for Centralized Data Center UPS Systems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mohamed Shamseldein

**分类**: eess.SY

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**针对数据中心UPS系统，提出三模式电网重构控制框架，提升弱电网适应性。**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `数据中心` `不间断电源` `电网重构` `弱电网` `电力电子` `储能系统` `三模式控制`

## 📋 核心要点

1. 数据中心负载波动和故障易对弱电网造成冲击，传统UPS难以有效应对。
2. 提出三模式控制框架，通过直流母线调节、故障模式优先级控制和频率响应调制，增强系统鲁棒性。
3. 仿真结果表明，该方法显著降低了IT能量损失，改善了电压稳定性和电网适应性。

## 📝 摘要（中文）

人工智能负载正将大型数据中心转变为高度动态的电力电子负载；故障期间的行为和负载脉冲可能会给互联的弱电网带来压力。本文提出了一种集中式中压（MV）不间断电源（UPS）控制架构，该架构实现为三种运行模式：模式1调节直流母线并塑造正常运行的电网消耗；模式2通过UPS电池储能系统（UPS-BESS）缓冲和速率限制的故障后“软返回”来强制执行电流限制的故障模式P-Q优先级；模式3可选地通过电网消耗调制提供基于下垂的快速频率响应。基频平均dq仿真（50 MW模块，短路比（SCR）=1.5，0.5 p.u.三相骤降150毫秒）显示零未服务信息技术（IT）能量（0.00000 MWh vs. 0.00208 MWh用于瞬时中断基准），0.57 p.u.峰值逆变器电流（vs. 1.02 p.u.用于同步参考系锁相环（SRF-PLL）低电压穿越（LVRT）基线），0.20 p.u.的非零平均故障窗口电网消耗（vs.瞬时中断的近似0），以及一个周期后改善的稳定公共连接点（PCC）电压最小值0.79 p.u.（vs. 0.66 p.u.）。强制振荡案例研究应用1 Hz脉冲负载（+/- 0.25 p.u.），并表明正常运行整形滤波器过滤了电网看到的振荡，而UPS-BESS缓冲了脉冲分量。

## 🔬 方法详解

**问题定义**：数据中心UPS系统在面对动态负载和电网故障时，容易对电网造成冲击，尤其是在弱电网环境下。传统UPS控制策略在故障期间可能导致电压骤降、电流过载等问题，影响数据中心的稳定运行。现有方法难以兼顾正常运行时的电网友好性和故障时的快速响应能力。

**核心思路**：本文的核心思路是将UPS控制分解为三个不同的运行模式，分别针对正常运行、故障模式和频率响应进行优化。通过集中式控制架构，实现对UPS-BESS的协调控制，从而提高系统的整体性能和可靠性。这种分层控制策略能够更好地适应数据中心负载的动态变化和电网的各种扰动。

**技术框架**：该控制框架包含三个主要模式：
1. **模式1：直流母线调节**。该模式主要负责在正常运行期间调节直流母线电压，并对电网的电流进行整形，以减少对电网的干扰。
2. **模式2：故障模式P-Q优先级控制**。在电网发生故障时，该模式通过UPS-BESS提供缓冲，并采用电流限制的P-Q优先级控制策略，确保关键负载的供电。
3. **模式3：基于下垂的快速频率响应**。该模式可选，通过调制电网的电流消耗，提供快速的频率响应，以支持电网的稳定。

**关键创新**：该方法的主要创新在于提出了一个三模式的集中式UPS控制框架，能够根据不同的运行状态自动切换控制策略，从而实现对数据中心UPS系统的全面优化。与传统的单一控制策略相比，该框架能够更好地适应数据中心负载的动态变化和电网的各种扰动，提高了系统的整体性能和可靠性。

**关键设计**：
*   **模式切换逻辑**：根据电网电压、频率等参数，自动切换不同的控制模式。
*   **故障模式P-Q优先级控制**：根据负载的重要性，设置不同的有功功率（P）和无功功率（Q）优先级。
*   **软返回策略**：在故障恢复后，采用速率限制的“软返回”策略，避免对电网造成冲击。
*   **下垂控制参数**：根据电网的特性，合理设置下垂控制的参数，以实现快速的频率响应。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16497v1/simulation_results_pulse_ramp.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16497v1/simulation_results_pulse.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16497v1/simulation_results_stage1.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

仿真结果显示，与瞬时中断基准相比，该方法实现了零未服务IT能量。在0.5 p.u.三相骤降150毫秒的故障情况下，峰值逆变器电流降低至0.57 p.u.（基线为1.02 p.u.），故障期间的平均电网消耗为0.20 p.u.（基线近似为0），一个周期后的PCC电压最小值提升至0.79 p.u.（基线为0.66 p.u.）。

## 🎯 应用场景

该研究成果可应用于大型数据中心的中压UPS系统，尤其是在连接到弱电网的数据中心。通过提高数据中心对电网故障的适应能力，可以减少因电力问题导致的数据丢失和服务中断，保障数据中心的关键业务运行。此外，该技术还有潜力推广到其他需要高可靠性供电的场景，如医院、工厂等。

## 📄 摘要（原文）

> AI workloads are turning large data centers into highly dynamic power-electronic loads; fault-time behavior and workload pulsing can stress weak-grid points of interconnection. This paper proposes a centralized medium-voltage (MV) uninterruptible power supply (UPS) control architecture implemented as three operating modes: Mode 1 regulates a DC stiff bus and shapes normal-operation grid draw, Mode 2 enforces current-limited fault-mode P--Q priority with UPS battery energy storage system (UPS-BESS) buffering and a rate-limited post-fault "soft return," and Mode 3 optionally provides droop-based fast frequency response via grid-draw modulation. Fundamental-frequency averaged dq simulations (50 MW block, short-circuit ratio (SCR) = 1.5, 0.5 p.u. three-phase dip for 150~ms) show zero unserved information-technology (IT) energy (0.00000 MWh vs.0.00208 MWh for a momentary-cessation benchmark), a 0.57 p.u. peak inverter current (vs. 1.02 p.u. for a synchronous-reference-frame phase-locked loop (SRF-PLL) low-voltage ride-through (LVRT) baseline), a nonzero mean fault-window grid draw of 0.20~p.u. (vs.approx 0 for momentary cessation), and an improved settled point-of-common-coupling (PCC) voltage minimum of 0.79 p.u. after one cycle (vs. 0.66 p.u.). A forced-oscillation case study applies a 1 Hz pulsed load (+/- 0.25 p.u.) and shows that the normal-operation shaping filters the oscillation seen by the grid while the UPS-BESS buffers the pulsing component.

