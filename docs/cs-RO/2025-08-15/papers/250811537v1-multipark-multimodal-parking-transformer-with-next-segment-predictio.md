---
layout: default
title: "MultiPark: Multimodal Parking Transformer with Next-Segment Prediction"
---

# MultiPark: Multimodal Parking Transformer with Next-Segment Prediction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.11537" class="toolbar-btn" target="_blank">📄 arXiv: 2508.11537v1</a>
  <a href="https://arxiv.org/pdf/2508.11537.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.11537v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.11537v1', 'MultiPark: Multimodal Parking Transformer with Next-Segment Prediction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Han Zheng, Zikang Zhou, Guli Zhang, Zhepei Wang, Kaixuan Wang, Peiliang Li, Shaojie Shen, Ming Yang, Tong Qin

**分类**: cs.RO

**发布日期**: 2025-08-15

---

## 💡 一句话要点

**提出MultiPark以解决复杂停车行为的多模态预测问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `停车行为预测` `自回归变换器` `模仿学习` `智能交通` `自动驾驶` `复杂环境`

## 📋 核心要点

1. 现有的模仿学习方法在停车行为的多样性和复杂性上存在不足，无法有效处理无车道开放空间中的多模态停车场景。
2. 本文提出MultiPark，通过自回归变换器和下段预测范式，增强了对复杂停车行为的建模能力，并引入了目标导向的损失函数以减少因果混淆。
3. 在真实世界数据集上的评估显示，MultiPark在多种停车场景中表现出色，超越了现有的最先进方法，证明了其实际应用的有效性。

## 📝 摘要（中文）

在高度受限的空间中，准确安全地停车仍然是一个关键挑战。与结构化驾驶环境不同，停车需要执行复杂的操作，如频繁换挡和转向饱和。尽管最近的模仿学习方法在停车方面取得了良好效果，但现有研究忽视了无车道开放空间中停车行为的多模态特性，未能在相同情况下推导出多个合理的解决方案。为了解决这些挑战，本文提出了MultiPark，一个用于多模态停车的自回归变换器。通过引入数据高效的下段预测范式，MultiPark能够处理充满急转弯的路径，实现空间泛化和时间外推。此外，我们设计了可学习的停车查询，分解为齿轮、纵向和横向组件，平行解码多样的停车行为。实验证明，MultiPark在各种场景下实现了最先进的性能，并在实际车辆上部署，进一步验证了其在真实停车环境中的鲁棒性。

## 🔬 方法详解

**问题定义**：本文旨在解决在无车道开放空间中停车行为的多模态预测问题。现有的模仿学习方法存在因果混淆，难以在多样化停车场景中进行有效泛化。

**核心思路**：MultiPark通过引入自回归变换器和数据高效的下段预测范式，能够处理复杂的停车路径，并通过目标导向的损失函数来减少因果混淆，从而提高模型的泛化能力。

**技术框架**：MultiPark的整体架构包括多个模块：自回归变换器用于建模停车行为，下段预测模块用于空间泛化和时间外推，学习查询模块则分解为齿轮、纵向和横向组件，平行解码多样的停车行为。

**关键创新**：最重要的技术创新在于引入了下段预测范式和目标导向的损失函数，这与传统的模仿学习方法不同，能够有效处理复杂的停车场景并减少因果混淆。

**关键设计**：在损失函数设计上，采用了目标导向的姿态和自我中心的碰撞损失，超越了纯粹的模仿损失。此外，学习查询的设计使得模型能够并行解码多种停车行为，增强了模型的灵活性和适应性。

## 📊 实验亮点

在真实世界数据集上的评估中，MultiPark在多种停车场景中实现了最先进的性能，相较于现有基线方法，性能提升幅度达到XX%（具体数据未知），证明了其在复杂停车环境中的有效性和鲁棒性。

## 🎯 应用场景

MultiPark的研究成果在自动驾驶和智能停车系统中具有广泛的应用潜力。其多模态停车行为的建模能力可以提升自动驾驶车辆在复杂环境中的停车效率和安全性，未来可能推动智能交通系统的发展，改善城市交通管理。

## 📄 摘要（原文）

> Parking accurately and safely in highly constrained spaces remains a critical challenge. Unlike structured driving environments, parking requires executing complex maneuvers such as frequent gear shifts and steering saturation. Recent attempts to employ imitation learning (IL) for parking have achieved promising results. However, existing works ignore the multimodal nature of parking behavior in lane-free open space, failing to derive multiple plausible solutions under the same situation. Notably, IL-based methods encompass inherent causal confusion, so enabling a neural network to generalize across diverse parking scenarios is particularly difficult. To address these challenges, we propose MultiPark, an autoregressive transformer for multimodal parking. To handle paths filled with abrupt turning points, we introduce a data-efficient next-segment prediction paradigm, enabling spatial generalization and temporal extrapolation. Furthermore, we design learnable parking queries factorized into gear, longitudinal, and lateral components, parallelly decoding diverse parking behaviors. To mitigate causal confusion in IL, our method employs target-centric pose and ego-centric collision as outcome-oriented loss across all modalities beyond pure imitation loss. Evaluations on real-world datasets demonstrate that MultiPark achieves state-of-the-art performance across various scenarios. We deploy MultiPark on a production vehicle, further confirming our approach's robustness in real-world parking environments.

