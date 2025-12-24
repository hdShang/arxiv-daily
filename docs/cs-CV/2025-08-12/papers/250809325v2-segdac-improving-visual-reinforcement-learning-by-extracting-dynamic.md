---
layout: default
title: "SegDAC: Improving Visual Reinforcement Learning by Extracting Dynamic Objectc-Centric Representations from Pretrained Vision Models"
---

# SegDAC: Improving Visual Reinforcement Learning by Extracting Dynamic Objectc-Centric Representations from Pretrained Vision Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09325" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09325v2</a>
  <a href="https://arxiv.org/pdf/2508.09325.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09325v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09325v2', 'SegDAC: Improving Visual Reinforcement Learning by Extracting Dynamic Objectc-Centric Representations from Pretrained Vision Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alexandre Brown, Glen Berseth

**分类**: cs.CV, cs.AI, cs.LG, cs.RO

**发布日期**: 2025-08-12 (更新: 2025-10-17)

---

## 💡 一句话要点

**提出SegDAC以解决视觉强化学习中的动态对象表示问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视觉强化学习` `动态对象表示` `分割驱动方法` `样本效率` `视觉泛化`

## 📋 核心要点

1. 现有视觉强化学习方法在高维输入中提取有效表示的能力不足，导致样本效率低下。
2. SegDAC通过使用SAM进行对象中心分解和YOLO-World进行图像分割，提出了一种新的分割驱动的演员-评论家方法。
3. 在Maniskill3基准上，SegDAC在视觉泛化方面表现优异，最困难设置下性能翻倍，样本效率显著提升。

## 📝 摘要（中文）

视觉强化学习（RL）面临从高维输入中提取有用表示的挑战，同时还需在稀疏和噪声奖励中学习有效控制。尽管存在大型感知模型，但将其有效整合到RL中以实现视觉泛化和提高样本效率仍然困难。我们提出了SegDAC，一种基于分割驱动的演员-评论家方法。SegDAC利用Segment Anything（SAM）进行对象中心分解，并通过文本输入将图像分割过程与YOLO-World结合。它包含一种新颖的基于变换器的架构，支持每个时间步动态数量的分段，并通过在线RL有效学习关注哪些分段，而无需使用人工标签。通过在Maniskill3上评估SegDAC，该基准涵盖了在强视觉扰动下的多样化操作任务，我们证明SegDAC在视觉泛化方面显著优于之前的方法，在最困难的设置下性能翻倍，并在所有评估任务中与之前的方法在样本效率上持平或超越。

## 🔬 方法详解

**问题定义**：本论文旨在解决视觉强化学习中从高维输入中提取动态对象表示的困难。现有方法在视觉泛化和样本效率方面存在显著不足，尤其是在处理复杂的操作任务时。

**核心思路**：SegDAC的核心思路是利用Segment Anything（SAM）进行对象中心分解，并结合YOLO-World通过文本输入增强图像分割过程。该方法通过动态调整关注的对象分段，提升了学习效率和泛化能力。

**技术框架**：SegDAC采用基于变换器的架构，支持在每个时间步动态调整分段数量。主要模块包括对象分解、图像分割和在线强化学习，形成一个闭环的学习系统。

**关键创新**：SegDAC的主要创新在于其动态分段选择机制，能够在没有人工标签的情况下，通过在线学习自动识别重要的对象分段，从而显著提高了样本效率和视觉泛化能力。

**关键设计**：在设计上，SegDAC使用了特定的损失函数来优化分段选择，并采用了变换器网络结构以支持动态输入。关键参数设置包括分段数量的动态调整和与YOLO-World的有效结合。

## 📊 实验亮点

SegDAC在Maniskill3基准测试中表现出色，在最困难的设置下实现了性能翻倍，并在所有评估任务中与之前的方法在样本效率上持平或超越，展示了其在视觉泛化方面的显著优势。

## 🎯 应用场景

该研究的潜在应用领域包括机器人操作、自动驾驶、智能监控等场景，能够在复杂环境中实现更高效的决策和控制。未来，SegDAC的技术可以扩展到更多的视觉任务中，推动视觉强化学习的进一步发展。

## 📄 摘要（原文）

> Visual reinforcement learning (RL) is challenging due to the need to extract useful representations from high-dimensional inputs while learning effective control from sparse and noisy rewards. Although large perception models exist, integrating them effectively into RL for visual generalization and improved sample efficiency remains difficult. We propose SegDAC, a Segmentation-Driven Actor-Critic method. SegDAC uses Segment Anything (SAM) for object-centric decomposition and YOLO-World to ground the image segmentation process via text inputs. It includes a novel transformer-based architecture that supports a dynamic number of segments at each time step and effectively learns which segments to focus on using online RL, without using human labels. By evaluating SegDAC over a challenging visual generalization benchmark using Maniskill3, which covers diverse manipulation tasks under strong visual perturbations, we demonstrate that SegDAC achieves significantly better visual generalization, doubling prior performance on the hardest setting and matching or surpassing prior methods in sample efficiency across all evaluated tasks.

