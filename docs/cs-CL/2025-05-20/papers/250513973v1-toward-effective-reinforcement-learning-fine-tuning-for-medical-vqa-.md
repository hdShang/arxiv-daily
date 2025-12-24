---
layout: default
title: Toward Effective Reinforcement Learning Fine-Tuning for Medical VQA in Vision-Language Models
---

# Toward Effective Reinforcement Learning Fine-Tuning for Medical VQA in Vision-Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13973" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13973v1</a>
  <a href="https://arxiv.org/pdf/2505.13973.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13973v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13973v1', 'Toward Effective Reinforcement Learning Fine-Tuning for Medical VQA in Vision-Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenhui Zhu, Xuanzhao Dong, Xin Li, Peijie Qiu, Xiwen Chen, Abolfazl Razi, Aris Sotiras, Yi Su, Yalin Wang

**分类**: cs.CL, cs.AI, cs.CV

**发布日期**: 2025-05-20

---

## 💡 一句话要点

**提出强化学习微调方法以提升医学视觉问答性能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

## 📋 核心要点

1. 现有的强化学习微调方法在医学视觉问答任务中难以实现临床期望的模型行为，存在多方面的挑战。
2. 本文提出了一种基于GRPO的强化学习微调方法，重点关注模型初始化、语义对齐、奖励机制及偏差等因素。
3. 实验结果显示，GRPO方法在准确性和推理质量上均显著优于传统的监督微调，提供了新的微调策略。
4. method_zh

## 📝 摘要（中文）

近年来，基于强化学习的微调方法改变了多模态大语言模型（MLLMs）的发展轨迹，尤其是在引入群体相对策略优化（GRPO）后。然而，直接将其应用于医学任务仍面临挑战，难以实现临床期望的模型行为。为此，本文探讨了影响医学视觉问答（VQA）中强化学习微调有效性的四个关键维度，包括基础模型初始化策略、医学语义对齐的作用、基于长度的奖励对长链推理的影响以及偏差的影响。通过广泛的实验，我们分析了这些因素对医学MLLMs的影响，提供了模型领域特定微调的新见解。此外，结果表明，基于GRPO的强化学习微调在准确性和推理质量上均优于标准的监督微调（SFT）。

## 📄 摘要（原文）

> Recently, reinforcement learning (RL)-based tuning has shifted the trajectory of Multimodal Large Language Models (MLLMs), particularly following the introduction of Group Relative Policy Optimization (GRPO). However, directly applying it to medical tasks remains challenging for achieving clinically grounded model behavior. Motivated by the need to align model response with clinical expectations, we investigate four critical dimensions that affect the effectiveness of RL-based tuning in medical visual question answering (VQA): base model initialization strategy, the role of medical semantic alignment, the impact of length-based rewards on long-chain reasoning, and the influence of bias. We conduct extensive experiments to analyze these factors for medical MLLMs, providing new insights into how models are domain-specifically fine-tuned. Additionally, our results also demonstrate that GRPO-based RL tuning consistently outperforms standard supervised fine-tuning (SFT) in both accuracy and reasoning quality.

