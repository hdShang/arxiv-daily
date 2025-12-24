---
layout: default
title: "From Micro to Macro Flow Modeling: Characterizing Heterogeneity of Mixed-Autonomy Traffic"
---

# From Micro to Macro Flow Modeling: Characterizing Heterogeneity of Mixed-Autonomy Traffic

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09432" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09432v1</a>
  <a href="https://arxiv.org/pdf/2508.09432.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09432v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09432v1', 'From Micro to Macro Flow Modeling: Characterizing Heterogeneity of Mixed-Autonomy Traffic')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chenguang Zhao, Huan Yu

**分类**: eess.SY

**发布日期**: 2025-08-13

---

## 💡 一句话要点

**提出混合自主交通流异质性建模方法以解决流动性理解问题**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `混合自主交通` `交通流建模` `流动异质性` `拉格朗日轨迹` `智能交通系统` `交通动态校准` `数据驱动方法`

## 📋 核心要点

1. 现有方法主要在车辆层面分析AV的影响，缺乏对宏观交通流异质性的理解，尤其是在混合交通环境中。
2. 本文提出了一种通过拉格朗日轨迹数据推导交通异质性的方法，结合了车辆数量和交通属性的耦合守恒定律。
3. 实验结果显示，该模型在多个交通数据集上有效捕捉流动异质性，校准误差相较于基准模型降低了20%。

## 📝 摘要（中文）

大多数自主车辆（AV）的驾驶策略在车辆层面进行设计和分析，但它们对宏观交通流的整体影响仍不清楚，尤其是在AV与人类驾驶车辆（HV）交互时产生的流动异质性。现有的宏观流动模型验证技术依赖于高分辨率的时空数据，而这些数据在混合自主交通中很少可得。本文通过引入连续的交通异质性属性，填补了微观拉格朗日数据与宏观欧几里得交通模型之间的空白。我们通过两个耦合的守恒定律来表示交通流，并设计重建方法从拉格朗日车辆轨迹中推导交通属性。实验表明，该模型有效捕捉交通异质性，并将交通流动态的校准误差相较于基准模型降低了20%。

## 🔬 方法详解

**问题定义**：本文旨在解决混合自主交通流中流动异质性理解不足的问题。现有方法依赖高分辨率时空数据进行验证，但在实际应用中这些数据往往难以获得。

**核心思路**：论文通过引入连续的交通异质性属性，利用拉格朗日轨迹数据来验证和改进宏观交通流模型，填补微观与宏观之间的空白。

**技术框架**：整体架构包括两个主要模块：一是基于耦合守恒定律的交通流表示，二是从拉格朗日轨迹中重建交通属性的方法。重建方法分为数据丰富和数据稀缺两种情况，前者提取驾驶员期望速度和行为不确定性，后者则通过端到端映射进行推断。

**关键创新**：最重要的创新点在于提出了连续交通异质性属性的概念，并通过耦合守恒定律有效地将微观数据与宏观模型结合，显著提高了模型的适应性和准确性。

**关键设计**：在模型设计中，采用了特定的损失函数来优化交通属性的重建，确保在不同交通条件下的泛化能力，同时通过聚类分析将基本图散点聚合为基于属性的组。

## 📊 实验亮点

实验结果表明，提出的模型在多个交通数据集上有效捕捉交通异质性，能够将交通流动态的校准误差降低20%，相较于Aw-Rascle-Zhang模型基准表现出显著的提升。此外，该模型在不同未见交通条件下保持了几乎相同的准确性，显示出良好的泛化能力。

## 🎯 应用场景

该研究的潜在应用领域包括智能交通系统、交通流量预测和城市交通管理等。通过更好地理解混合自主交通流的异质性，能够为政策制定者和交通工程师提供更有效的决策支持，从而提升交通效率和安全性。未来，该方法可能在自动驾驶技术的推广和应用中发挥重要作用。

## 📄 摘要（原文）

> Most autonomous-vehicles (AVs) driving strategies are designed and analyzed at the vehicle level, yet their aggregate impact on macroscopic traffic flow is still not understood, particularly the flow heterogeneity that emerges when AVs interact with human-driven vehicles (HVs). Existing validation techniques for macroscopic flow models rely on high-resolution spatiotemporal data spanning entire road segments which are rarely available for mixed-autonomy traffic. AVs record detailed Lagrangian trajectories of the ego vehicle and surrounding traffic through onboard sensors. Leveraging these Lagrangian observations to validate mixed-autonomy flow models therefore remains an open research challenge. This paper closes the gap between microscopic Lagrangian data and macroscopic Euclidean traffic models by introducing a continuous traffic-heterogeneity attribute. We represent traffic flow with two coupled conservation laws with one for vehicle number and one for the traffic attribute. Reconstruction methods are designed to derive the traffic attribute from Lagrangian vehicle trajectories. When abundant trajectory data are available, we characterize traffic heterogeneity by extracting drivers' desired speed and local behavioral uncertainty from trajectories. In data-scarce mixed traffic, we design an end-to-end mapping that infers the traffic heterogeneity solely from trajectories in the current spatiotemporal region. Experiments across multiple traffic datasets show that the proposed model effectively captures traffic heterogeneity by clustering the fundamental diagram scatter into attribute-based groups. The calibration errors of traffic flow dynamics are also reduce by 20% relative to the Aw-Rascle-Zhang model benchmark. Detailed analyses further show that the model generalizes well, maintaining nearly the same accuracy when evaluated under a variety of previously unseen traffic conditions.

