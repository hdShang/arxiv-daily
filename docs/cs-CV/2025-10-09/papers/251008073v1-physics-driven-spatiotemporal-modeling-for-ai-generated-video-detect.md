---
layout: default
title: Physics-Driven Spatiotemporal Modeling for AI-Generated Video Detection
---

# Physics-Driven Spatiotemporal Modeling for AI-Generated Video Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.08073" class="toolbar-btn" target="_blank">📄 arXiv: 2510.08073v1</a>
  <a href="https://arxiv.org/pdf/2510.08073.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.08073v1" onclick="toggleFavorite(this, '2510.08073v1', 'Physics-Driven Spatiotemporal Modeling for AI-Generated Video Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shuhai Zhang, ZiHao Lian, Jiahao Yang, Daiyuan Li, Guoxuan Pang, Feng Liu, Bo Han, Shutao Li, Mingkui Tan

**分类**: cs.CV, cs.LG

**发布日期**: 2025-10-09

**备注**: Accepted at NeurIPS 2025 spotlight

**🔗 代码/项目**: [GITHUB](https://github.com/ZSHsh98/NSG-VD)

---

## 💡 一句话要点

**提出基于物理驱动的时空建模方法，用于检测AI生成视频**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `AI生成视频检测` `物理驱动建模` `时空梯度` `概率流守恒` `扩散模型`

## 📋 核心要点

1. 现有AI生成视频检测方法难以有效建模高维时空动态，且难以捕捉违反物理定律的细微异常。
2. 论文提出基于概率流守恒原理的物理驱动方法，通过归一化时空梯度（NSG）显式捕获视频动态偏差。
3. 实验结果表明，NSG-VD在召回率和F1-Score上显著优于现有方法，验证了其卓越的检测性能。

## 📝 摘要（中文）

AI生成的视频已经达到了近乎完美的视觉真实度（例如Sora），因此迫切需要可靠的检测机制。然而，检测此类视频面临着建模高维时空动态以及识别违反物理定律的细微异常的重大挑战。本文提出了一种基于概率流守恒原理的物理驱动的AI生成视频检测范例。具体来说，我们提出了一种名为归一化时空梯度（NSG）的统计量，它量化了空间概率梯度与时间密度变化的比率，从而显式地捕获了与自然视频动态的偏差。利用预训练的扩散模型，我们开发了一种NSG估计器，通过空间梯度近似和运动感知的时间建模，无需复杂的运动分解，同时保留了物理约束。在此基础上，我们提出了一种基于NSG的视频检测方法（NSG-VD），该方法计算测试视频和真实视频的NSG特征之间的最大均值差异（MMD）作为检测指标。最后，我们推导了真实视频和生成视频之间NSG特征距离的上限，证明了由于分布偏移，生成视频表现出放大的差异。大量实验证实，NSG-VD在召回率上比最先进的基线高出16.00%，在F1-Score上高出10.75%，验证了NSG-VD的卓越性能。

## 🔬 方法详解

**问题定义**：当前AI生成视频检测方法难以有效建模视频中的高维时空动态，并且难以捕捉到违反物理定律的细微异常。现有方法通常依赖于学习视频中的统计特征，但缺乏对视频内在物理规律的约束，导致检测性能受限。

**核心思路**：论文的核心思路是利用概率流守恒原理，将视频视为概率密度随时间演化的过程。通过量化空间概率梯度与时间密度变化的比率，即归一化时空梯度（NSG），可以显式地捕获AI生成视频中与自然视频动态的偏差。这种方法能够有效地检测出违反物理规律的异常。

**技术框架**：NSG-VD方法的整体框架包括以下几个主要阶段：1) 利用预训练的扩散模型提取视频的空间梯度信息；2) 通过运动感知的时间建模，估计视频的时间密度变化；3) 计算归一化时空梯度（NSG）特征；4) 使用最大均值差异（MMD）度量测试视频和真实视频的NSG特征之间的差异，作为检测指标。

**关键创新**：该方法最重要的技术创新点在于提出了归一化时空梯度（NSG）这一统计量，它能够显式地捕获AI生成视频中违反物理规律的动态偏差。与现有方法相比，NSG-VD方法更加关注视频内在的物理规律，从而能够更有效地检测AI生成视频。此外，该方法利用预训练的扩散模型进行空间梯度近似，避免了复杂的运动分解，同时保留了物理约束。

**关键设计**：NSG的计算公式为空间概率梯度与时间密度变化的比率。空间概率梯度通过预训练扩散模型估计，时间密度变化通过运动感知的时间建模实现。MMD度量用于计算测试视频和真实视频的NSG特征之间的差异，作为检测指标。论文还推导了真实视频和生成视频之间NSG特征距离的上限，证明了生成视频由于分布偏移会表现出放大的差异。

## 📊 实验亮点

实验结果表明，NSG-VD方法在AI生成视频检测任务中取得了显著的性能提升。具体来说，在Recall指标上，NSG-VD比最先进的基线方法高出16.00%，在F1-Score指标上高出10.75%。这些结果验证了NSG-VD方法在检测AI生成视频方面的卓越性能。

## 🎯 应用场景

该研究成果可应用于内容安全领域，例如检测和识别深度伪造视频，防止虚假信息的传播。此外，该方法还可用于视频监控、智能交通等领域，用于检测异常事件或行为，提高系统的安全性和可靠性。未来，该方法可以进一步扩展到其他类型的AI生成内容检测，例如图像、音频等。

## 📄 摘要（原文）

> AI-generated videos have achieved near-perfect visual realism (e.g., Sora), urgently necessitating reliable detection mechanisms. However, detecting such videos faces significant challenges in modeling high-dimensional spatiotemporal dynamics and identifying subtle anomalies that violate physical laws. In this paper, we propose a physics-driven AI-generated video detection paradigm based on probability flow conservation principles. Specifically, we propose a statistic called Normalized Spatiotemporal Gradient (NSG), which quantifies the ratio of spatial probability gradients to temporal density changes, explicitly capturing deviations from natural video dynamics. Leveraging pre-trained diffusion models, we develop an NSG estimator through spatial gradients approximation and motion-aware temporal modeling without complex motion decomposition while preserving physical constraints. Building on this, we propose an NSG-based video detection method (NSG-VD) that computes the Maximum Mean Discrepancy (MMD) between NSG features of the test and real videos as a detection metric. Last, we derive an upper bound of NSG feature distances between real and generated videos, proving that generated videos exhibit amplified discrepancies due to distributional shifts. Extensive experiments confirm that NSG-VD outperforms state-of-the-art baselines by 16.00% in Recall and 10.75% in F1-Score, validating the superior performance of NSG-VD. The source code is available at https://github.com/ZSHsh98/NSG-VD.

