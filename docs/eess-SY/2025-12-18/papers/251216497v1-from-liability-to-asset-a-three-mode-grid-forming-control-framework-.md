---
layout: default
title: "From Liability to Asset: A Three-Mode Grid-Forming Control Framework for Centralized Data Center UPS Systems"
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

**针对数据中心UPS系统，提出三模电网重构控制框架，提升弱电网适应性。**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `数据中心` `不间断电源` `电网重构` `弱电网` `电力电子` `智能电网` `故障穿越`

## 📋 核心要点

1. 数据中心负载波动和故障易对弱电网造成冲击，现有UPS系统在应对此类问题时存在不足。
2. 提出三模控制框架，通过不同模式分别实现稳压、故障保护和频率响应，提升系统鲁棒性。
3. 仿真结果表明，该方法能有效减少能量损失，降低逆变器电流峰值，并改善电网电压稳定性。

## 📝 摘要（中文）

人工智能负载正将大型数据中心转变为高度动态的电力电子负载；故障期间的行为和负载脉冲可能会给互联的弱电网带来压力。本文提出了一种集中式中压（MV）不间断电源（UPS）控制架构，该架构实现为三种运行模式：模式1调节直流母线并塑造正常运行的电网吸取功率；模式2通过UPS电池储能系统（UPS-BESS）缓冲和速率限制的故障后“软返回”来强制执行电流限制的故障模式P-Q优先级；模式3可选地通过电网吸取功率调制提供基于下垂的快速频率响应。基频平均dq仿真（50 MW模块，短路比（SCR）= 1.5，0.5 p.u.三相骤降150毫秒）显示零未服务的信息技术（IT）能量（0.00000 MWh，而瞬时中断基准为0.00208 MWh），0.57 p.u.峰值逆变器电流（而同步参考系锁相环（SRF-PLL）低电压穿越（LVRT）基线为1.02 p.u.），0.20 p.u.的非零平均故障窗口电网吸取功率（而瞬时中断约为0），以及改善的稳定公共连接点（PCC）电压最小值，在一个周期后为0.79 p.u.（而0.66 p.u.）。强制振荡案例研究应用1 Hz脉冲负载（+/- 0.25 p.u.），表明正常运行整形滤波器滤除了电网看到的振荡，而UPS-BESS缓冲了脉冲分量。

## 🔬 方法详解

**问题定义**：数据中心UPS系统需要应对日益增长的动态负载和潜在的电网故障，尤其是在弱电网环境下。传统UPS系统在故障期间可能导致电压骤降、电流过载，甚至信息技术设备停机，影响数据中心的可靠运行。现有方法，如基于同步参考系锁相环（SRF-PLL）的低电压穿越（LVRT）技术，在故障期间可能导致逆变器电流过大，且无法有效支撑电网电压。

**核心思路**：本文的核心思路是将UPS系统设计为具有三种运行模式的智能电网重构单元。通过集中式控制，UPS系统可以根据电网状态和负载需求，灵活切换不同的运行模式，从而实现对电网的支撑和保护。这种方法旨在将UPS系统从单纯的备用电源转变为电网的积极参与者，提高电网的稳定性和可靠性。

**技术框架**：该控制框架包含三个主要模式：
1. **模式1（正常运行）**：调节直流母线电压，并对电网吸取的功率进行整形，以减少谐波和提高功率因数。
2. **模式2（故障模式）**：在电网发生故障时，限制逆变器电流，并根据P-Q优先级向电网注入有功和无功功率，同时利用UPS-BESS提供缓冲，并采用速率限制的“软返回”策略，避免故障恢复时的冲击。
3. **模式3（可选，快速频率响应）**：通过调制电网吸取的功率，提供基于下垂控制的快速频率响应，以支撑电网频率稳定。

**关键创新**：该方法的关键创新在于将UPS系统视为一个可编程的电网支撑单元，通过集中式控制实现多种运行模式的切换，从而在正常运行、故障和频率扰动等不同工况下都能有效支撑电网。与传统的被动式UPS系统相比，该方法能够更积极地参与电网的稳定控制。

**关键设计**：
*   **模式切换策略**：根据电网电压、频率和负载需求，设计合理的模式切换策略，确保系统在不同工况下都能平稳运行。
*   **故障模式下的P-Q优先级控制**：根据电网需求，合理分配有功和无功功率的优先级，以最大程度地支撑电网电压。
*   **速率限制的“软返回”策略**：在故障恢复时，限制逆变器电流的上升速率，避免对电网造成冲击。
*   **正常运行模式下的功率整形滤波器**：设计合适的滤波器，减少电网吸取功率的谐波含量。

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

仿真结果表明，与瞬时中断基准相比，该方法实现了零未服务的信息技术能量（0.00000 MWh vs. 0.00208 MWh）。逆变器峰值电流从1.02 p.u.（SRF-PLL LVRT基线）降低到0.57 p.u.。故障期间的平均电网吸取功率为0.20 p.u.，而瞬时中断约为0。公共连接点（PCC）电压最小值在一个周期后提高到0.79 p.u.，而基线为0.66 p.u.。

## 🎯 应用场景

该研究成果可应用于大型数据中心、工业园区等对电力可靠性要求高的场景。通过将UPS系统升级为智能电网支撑单元，可以提高电网的稳定性和可靠性，减少因电网故障造成的经济损失。未来，该技术有望推广到更多分布式电源接入的场景，促进智能电网的发展。

## 📄 摘要（原文）

> AI workloads are turning large data centers into highly dynamic power-electronic loads; fault-time behavior and workload pulsing can stress weak-grid points of interconnection. This paper proposes a centralized medium-voltage (MV) uninterruptible power supply (UPS) control architecture implemented as three operating modes: Mode 1 regulates a DC stiff bus and shapes normal-operation grid draw, Mode 2 enforces current-limited fault-mode P--Q priority with UPS battery energy storage system (UPS-BESS) buffering and a rate-limited post-fault "soft return," and Mode 3 optionally provides droop-based fast frequency response via grid-draw modulation. Fundamental-frequency averaged dq simulations (50 MW block, short-circuit ratio (SCR) = 1.5, 0.5 p.u. three-phase dip for 150~ms) show zero unserved information-technology (IT) energy (0.00000 MWh vs.0.00208 MWh for a momentary-cessation benchmark), a 0.57 p.u. peak inverter current (vs. 1.02 p.u. for a synchronous-reference-frame phase-locked loop (SRF-PLL) low-voltage ride-through (LVRT) baseline), a nonzero mean fault-window grid draw of 0.20~p.u. (vs.approx 0 for momentary cessation), and an improved settled point-of-common-coupling (PCC) voltage minimum of 0.79 p.u. after one cycle (vs. 0.66 p.u.). A forced-oscillation case study applies a 1 Hz pulsed load (+/- 0.25 p.u.) and shows that the normal-operation shaping filters the oscillation seen by the grid while the UPS-BESS buffers the pulsing component.

