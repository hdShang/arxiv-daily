---
layout: default
title: Robust Underwater Localization of Buoyancy Driven microFloats Using Acoustic Time-of-Flight Measurements
---

# Robust Underwater Localization of Buoyancy Driven microFloats Using Acoustic Time-of-Flight Measurements

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.12233" class="toolbar-btn" target="_blank">📄 arXiv: 2512.12233v1</a>
  <a href="https://arxiv.org/pdf/2512.12233.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.12233v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.12233v1', 'Robust Underwater Localization of Buoyancy Driven microFloats Using Acoustic Time-of-Flight Measurements')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Murad Mehrab Abrar, Trevor W. Harrison

**分类**: cs.RO

**发布日期**: 2025-12-13

**备注**: 9 pages

**DOI**: [10.23919/OCEANS59106.2025.11245003](https://doi.org/10.23919/OCEANS59106.2025.11245003)

---

## 💡 一句话要点

**提出一种基于双向声学飞行时间测量的微浮标水下稳健定位方法**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `水下定位` `声学定位` `飞行时间测量` `微浮标` `非线性三边测量`

## 📋 核心要点

1. 现有水下定位方法难以兼顾低成本和高频位置更新，尤其是在小型自主平台上。
2. 该论文提出一种双向声学飞行时间(ToF)定位框架，结合非线性三边测量和基于几何成本与CRLB的滤波，提高定位精度。
3. 在普吉特海峡的实验表明，该方法能将定位中值误差降至4米以下，平均误差从139.29米降至12.07米。

## 📝 摘要（中文）

本文提出了一种稳健、低成本的水下定位流程，用于沿海水域中由浮力驱动的微浮标，这些平台需要高频的位置更新。该方法基于双向声学飞行时间(ToF)定位框架，结合了浮标到浮标和浮标到浮标的传输，从而增加了可用测量值的数量。该方法集成了非线性三边测量，并根据几何成本和Cramer-Rao下界(CRLB)对计算的位置估计进行过滤。这种方法消除了由多径效应和其他声学误差引起的ToF估计中的异常值，并在不依赖大量平滑的情况下提高了定位的鲁棒性。在美国华盛顿州普吉特海峡的两次现场部署中验证了该框架。定位流程实现了相对于GPS位置低于4米的定位中值误差。过滤技术显示平均误差从139.29米降低到12.07米，并改善了轨迹与GPS路径的对齐。此外，还展示了一种用于实验期间传输但未回收的浮标的时间差分到达(TDoA)定位方法。基于范围的声学定位技术被广泛使用，并且通常与硬件无关——这项工作旨在通过仔细的算法设计来提高定位频率和鲁棒性，从而最大限度地提高它们的效用。

## 🔬 方法详解

**问题定义**：论文旨在解决水下微浮标的稳健定位问题。现有方法在低成本自主平台上难以实现高频率、高精度的定位，容易受到多径效应等声学误差的影响，导致定位结果不稳定。

**核心思路**：核心思路是利用双向声学飞行时间测量，增加可用测量数据，并结合非线性三边测量和基于几何成本及CRLB的滤波方法，剔除异常值，提高定位的鲁棒性。双向测量可以提供更多冗余信息，滤波方法则可以有效抑制噪声和误差。

**技术框架**：整体框架包括以下几个主要阶段：1) 声学信号的发射和接收，包括浮标到浮标和浮标到浮标的双向传输；2) 飞行时间(ToF)的估计；3) 基于非线性三边测量的初始位置估计；4) 基于几何成本和CRLB的滤波，剔除异常值；5) 最终位置的输出。对于未回收的浮标，还采用了时间差分到达(TDoA)定位方法。

**关键创新**：关键创新在于双向声学测量和基于几何成本及CRLB的滤波相结合。双向测量增加了数据冗余，提高了定位的可靠性。滤波方法能够有效识别和剔除由于多径效应等因素引起的异常值，从而提高了定位的鲁棒性，而无需过度平滑。

**关键设计**：几何成本函数用于评估位置估计的合理性，CRLB则用于评估位置估计的理论精度。滤波过程根据几何成本和CRLB对位置估计进行加权，从而剔除不合理或精度较低的估计值。具体的参数设置（例如滤波阈值）需要根据实际环境进行调整。

## 📊 实验亮点

实验结果表明，该定位流程实现了相对于GPS位置低于4米的定位中值误差。通过引入滤波技术，平均误差从139.29米显著降低到12.07米，并且轨迹与GPS路径的对齐程度得到了显著改善。此外，该研究还展示了时间差分到达(TDoA)定位方法在未回收浮标定位中的应用。

## 🎯 应用场景

该研究成果可应用于海洋环境监测、水下机器人导航、水下传感器网络等领域。通过低成本的微浮标进行高频、高精度的水下定位，可以更有效地收集海洋数据，提高水下作业的效率和安全性。该方法还有潜力应用于其他水下自主平台的定位。

## 📄 摘要（原文）

> Accurate underwater localization remains a challenge for inexpensive autonomous platforms that require highfrequency position updates. In this paper, we present a robust, low-cost localization pipeline for buoyancy-driven microFloats operating in coastal waters. We build upon previous work by introducing a bidirectional acoustic Time-of-Flight (ToF) localization framework, which incorporates both float-to-buoy and buoy-to-float transmissions, thereby increasing the number of usable measurements. The method integrates nonlinear trilateration with a filtering of computed position estimates based on geometric cost and Cramer-Rao Lower Bounds (CRLB). This approach removes outliers caused by multipath effects and other acoustic errors from the ToF estimation and improves localization robustness without relying on heavy smoothing. We validate the framework in two field deployments in Puget Sound, Washington, USA. The localization pipeline achieves median positioning errors below 4 m relative to GPS positions. The filtering technique shows a reduction in mean error from 139.29 m to 12.07 m, and improved alignment of trajectories with GPS paths. Additionally, we demonstrate a Time-Difference-of-Arrival (TDoA) localization for unrecovered floats that were transmitting during the experiment. Range-based acoustic localization techniques are widely used and generally agnostic to hardware-this work aims to maximize their utility by improving positioning frequency and robustness through careful algorithmic design.

