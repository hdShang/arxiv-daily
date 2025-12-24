---
layout: default
title: KineDex: Learning Tactile-Informed Visuomotor Policies via Kinesthetic Teaching for Dexterous Manipulation
---

# KineDex: Learning Tactile-Informed Visuomotor Policies via Kinesthetic Teaching for Dexterous Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.01974" class="toolbar-btn" target="_blank">📄 arXiv: 2505.01974v1</a>
  <a href="https://arxiv.org/pdf/2505.01974.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.01974v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.01974v1', 'KineDex: Learning Tactile-Informed Visuomotor Policies via Kinesthetic Teaching for Dexterous Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Di Zhang, Chengbo Yuan, Chuan Wen, Hai Zhang, Junqiao Zhao, Yang Gao

**分类**: cs.RO

**发布日期**: 2025-05-04

---

## 💡 一句话要点

**提出KineDex以解决精细触觉信息缺失问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `灵巧操作` `触觉反馈` `动觉教学` `视觉运动策略` `力控制` `机器人技术` `数据收集效率`

## 📋 核心要点

1. 现有方法在收集触觉信息时面临运动学不匹配和缺乏实时反馈的问题，限制了灵巧操作的精度。
2. KineDex通过手把手的动觉教学，将操作员的动作直接转移到灵巧手上，收集富含触觉反馈的演示数据。
3. 在一系列接触密集的操作任务中，KineDex的成功率达到74.4%，相比于不使用力控制的变体提升了57.7%。

## 📝 摘要（中文）

收集富含细粒度触觉信息的演示对于灵巧操作至关重要，尤其是在需要精确力控制和物理交互的接触密集任务中。现有方法主要集中在遥操作或基于视频的重定向，但常常面临运动学不匹配和缺乏实时触觉反馈的问题，限制了高保真触觉数据的获取。为此，我们提出KineDex，一种手把手的动觉教学范式，直接将操作员的动作转移到灵巧手上，从而收集富含准确触觉反馈的物理基础演示。基于这些演示，我们训练了一个使用触觉增强输入的视觉运动策略，并在部署过程中实施力控制，以实现精确的接触密集操作。

## 🔬 方法详解

**问题定义**：本论文旨在解决在灵巧操作中收集高保真触觉信息的困难，现有方法在实时反馈和运动学匹配方面存在显著不足。

**核心思路**：KineDex采用手把手的动觉教学方式，直接将操作员的动作传递给机器人手，从而实现高质量的触觉数据收集。

**技术框架**：KineDex的整体架构包括数据收集、视觉观察预处理（使用修复技术处理人手遮挡）、以及基于触觉增强输入的视觉运动策略训练和力控制实施。

**关键创新**：KineDex的主要创新在于其动觉教学范式，能够有效克服传统遥操作方法的局限性，提供更高的触觉数据质量和收集效率。

**关键设计**：在数据收集过程中，采用了修复技术来处理视觉观察中的遮挡问题，并在训练过程中使用触觉增强输入，确保策略能够在接触密集的任务中实现精确的力控制。

## 📊 实验亮点

KineDex在一系列接触密集的操作任务中取得了74.4%的平均成功率，相比于不使用力控制的变体提升了57.7%。在与遥操作的对比实验中，KineDex在数据收集效率上提高了两倍，成功率接近100%，而遥操作的成功率不足50%。

## 🎯 应用场景

KineDex的研究成果在机器人灵巧操作、自动化装配、医疗手术辅助等领域具有广泛的应用潜力。通过提高触觉信息的获取效率和精度，该方法能够显著提升机器人在复杂环境中的操作能力，推动智能制造和人机协作的发展。

## 📄 摘要（原文）

> Collecting demonstrations enriched with fine-grained tactile information is critical for dexterous manipulation, particularly in contact-rich tasks that require precise force control and physical interaction. While prior works primarily focus on teleoperation or video-based retargeting, they often suffer from kinematic mismatches and the absence of real-time tactile feedback, hindering the acquisition of high-fidelity tactile data. To mitigate this issue, we propose KineDex, a hand-over-hand kinesthetic teaching paradigm in which the operator's motion is directly transferred to the dexterous hand, enabling the collection of physically grounded demonstrations enriched with accurate tactile feedback. To resolve occlusions from human hand, we apply inpainting technique to preprocess the visual observations. Based on these demonstrations, we then train a visuomotor policy using tactile-augmented inputs and implement force control during deployment for precise contact-rich manipulation. We evaluate KineDex on a suite of challenging contact-rich manipulation tasks, including particularly difficult scenarios such as squeezing toothpaste onto a toothbrush, which require precise multi-finger coordination and stable force regulation. Across these tasks, KineDex achieves an average success rate of 74.4%, representing a 57.7% improvement over the variant without force control. Comparative experiments with teleoperation and user studies further validate the advantages of KineDex in data collection efficiency and operability. Specifically, KineDex collects data over twice as fast as teleoperation across two tasks of varying difficulty, while maintaining a near-100% success rate, compared to under 50% for teleoperation.

