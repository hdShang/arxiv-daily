---
layout: default
title: Adaptive Deep Reasoning: Triggering Deep Thinking When Needed
---

# Adaptive Deep Reasoning: Triggering Deep Thinking When Needed

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20101" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20101v2</a>
  <a href="https://arxiv.org/pdf/2505.20101.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20101v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20101v2', 'Adaptive Deep Reasoning: Triggering Deep Thinking When Needed')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yunhao Wang, Yuhao Zhang, Tinghao Yu, Can Xu, Feng Zhang, Fengzong Lian

**分类**: cs.CL

**发布日期**: 2025-05-26 (更新: 2025-05-27)

---

## 💡 一句话要点

**提出自适应深度推理以解决计算成本高的问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自适应推理` `长链推理` `短链推理` `强化学习` `计算效率` `大型语言模型` `推理优化`

## 📋 核心要点

1. 现有方法在推理效率上存在不足，尤其是在长链推理时计算成本显著增加，限制了实际应用。
2. 本文提出了一种自适应推理方法，能够根据问题复杂性自动切换短链和长链推理，提升推理效率。
3. 实验结果表明，该模型在数学数据集上能够动态切换推理模式，且性能保持稳定，展示了良好的实用性。

## 📝 摘要（中文）

大型语言模型（LLMs）在处理复杂任务时展现出卓越的长链推理能力，但推理步骤的增加显著提高了计算成本，给实际应用带来挑战。近期的研究集中在通过缩短链式思维（CoT）推理过程来优化推理效率，然而这些方法仍需初始推理阶段。本文提出了一种新方法，能够根据问题复杂性自主切换短链和长链推理。通过对基础模型进行监督微调，使其具备长链和短链推理能力，并结合强化学习平衡两者的生成，最终在数学数据集上的评估显示该模型能够动态切换推理模式，同时保持性能不大幅下降。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在长链推理中计算成本高的问题。现有方法虽然能缩短推理长度，但仍需手动控制推理模式，缺乏灵活性。

**核心思路**：提出一种自适应推理方法，通过监督微调和强化学习，使模型能够根据问题复杂性自主选择推理链的长度，从而提高推理效率。

**技术框架**：整体架构包括两个主要阶段：首先进行监督微调，使模型具备长链和短链推理能力；其次通过强化学习优化推理生成，结合长短自适应的奖励策略和基于logit的推理模式切换损失。

**关键创新**：最重要的创新在于引入了长短自适应的奖励策略和logit基础的推理模式切换损失，使模型能够在推理过程中动态调整，提升了推理的灵活性和效率。

**关键设计**：在参数设置上，采用了长短自适应的奖励机制来评估提示复杂性，并通过损失函数优化初始token选择，确保推理类型的选择更为合理。整体网络结构设计上，强化学习与传统的监督学习相结合，形成了新的训练策略。

## 📊 实验亮点

实验结果显示，所提模型在数学数据集上能够有效地在长链和短链推理之间切换，且在性能上与基线模型相比，保持了相似的准确率，展示了良好的灵活性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、自动化推理工具和教育辅助软件等。通过提高推理效率，该方法能够在实际应用中降低计算成本，提升用户体验，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Large language models (LLMs) have shown impressive capabilities in handling complex tasks through long-chain reasoning. However, the extensive reasoning steps involved can significantly increase computational costs, posing challenges for real-world deployment. Recent efforts have focused on optimizing reasoning efficiency by shortening the Chain-of-Thought (CoT) reasoning processes through various approaches, such as length-aware prompt engineering, supervised fine-tuning on CoT data with variable lengths, and reinforcement learning with length penalties. Although these methods effectively reduce reasoning length, they still necessitate an initial reasoning phase. More recent approaches have attempted to integrate long-chain and short-chain reasoning abilities into a single model, yet they still rely on manual control to toggle between short and long CoT. In this work, we propose a novel approach that autonomously switches between short and long reasoning chains based on problem complexity. Our method begins with supervised fine-tuning of the base model to equip both long-chain and short-chain reasoning abilities. We then employ reinforcement learning to further balance short and long CoT generation while maintaining accuracy through two key strategies: first, integrating reinforcement learning with a long-short adaptive group-wise reward strategy to assess prompt complexity and provide corresponding rewards; second, implementing a logit-based reasoning mode switching loss to optimize the model's initial token choice, thereby guiding the selection of the reasoning type. Evaluations on mathematical datasets demonstrate that our model can dynamically switch between long-chain and short-chain reasoning modes without substantially sacrificing performance. This advancement enhances the practicality of reasoning in large language models for real-world applications.

