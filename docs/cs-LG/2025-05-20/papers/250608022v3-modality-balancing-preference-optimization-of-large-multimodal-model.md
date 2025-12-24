---
layout: default
title: Modality-Balancing Preference Optimization of Large Multimodal Models by Adversarial Negative Mining
---

# Modality-Balancing Preference Optimization of Large Multimodal Models by Adversarial Negative Mining

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.08022" class="toolbar-btn" target="_blank">📄 arXiv: 2506.08022v3</a>
  <a href="https://arxiv.org/pdf/2506.08022.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.08022v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.08022v3', 'Modality-Balancing Preference Optimization of Large Multimodal Models by Adversarial Negative Mining')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chenxi Liu, Tianyi Xiong, Yanshuo Chen, Ruibo Chen, Yihan Wu, Junfeng Guo, Tianyi Zhou, Heng Huang

**分类**: cs.LG, cs.AI, cs.CL, cs.CV

**发布日期**: 2025-05-20 (更新: 2025-10-08)

---

## 💡 一句话要点

**提出多模态平衡偏好优化方法以解决模态失衡问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态模型` `偏好优化` `模态失衡` `对抗性学习` `视觉-语言任务` `在线学习` `生成模型`

## 📋 核心要点

1. 现有的偏好优化方法未能有效抑制大型语言模型（LLM）在训练数据中的内部偏见，导致模态失衡问题。
2. 本文提出的模态平衡偏好优化（MBPO）框架，通过对抗性扰动生成难负样本，构建更有效的离线偏好数据集。
3. 实验结果显示，MBPO在挑战性的视觉-语言任务中显著提升了模型性能，并有效减少了幻觉现象。

## 📝 摘要（中文）

大型多模态模型（LMMs）的任务适应性和对齐能力已通过指令调优和偏好优化显著提升。然而，现有LMMs在推理过程中仍面临模态失衡的问题，导致语言优先偏见超过视觉输入，从而限制了其在下游任务中的泛化能力并引发幻觉。本文提出了一种新颖的偏好学习框架——模态平衡偏好优化（MBPO），通过生成对抗性负样本来构建更有效的离线偏好数据集，并利用在线生成的响应进行训练。实验表明，MBPO在视觉-语言任务上显著提升了LMM的性能，并有效减少了幻觉现象。

## 🔬 方法详解

**问题定义**：本文旨在解决大型多模态模型（LMMs）在推理过程中存在的模态失衡问题，现有方法未能有效抑制LLM的内部偏见，导致模型在视觉输入上的表现不佳。

**核心思路**：提出模态平衡偏好优化（MBPO）框架，通过生成对抗性负样本来增强训练数据的多样性，并结合在线生成的响应进行模型训练，以改善模型的推理能力。

**技术框架**：MBPO的整体架构包括两个主要模块：首先，通过对抗性扰动生成难负样本，构建离线偏好数据集；其次，利用在线生成的响应进行训练，结合GRPO方法进行模型优化。

**关键创新**：MBPO的核心创新在于生成对抗性负样本的能力，这一方法有效地增强了训练数据的代表性，与传统的偏好优化方法相比，能够更好地应对模态失衡问题。

**关键设计**：在MBPO中，关键参数包括对抗性扰动的强度和生成负样本的策略，同时采用易于验证的封闭式任务来生成在线响应，确保训练过程中的反馈有效性。

## 📊 实验亮点

实验结果表明，MBPO在多个视觉-语言任务上相较于基线模型提升了性能，具体表现为在某些任务上准确率提高了10%以上，同时有效减少了幻觉现象的发生，显示出其在实际应用中的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括视觉问答、图像描述生成和多模态检索等任务，能够显著提升多模态模型在实际场景中的表现。未来，MBPO方法有望在更广泛的多模态应用中发挥重要作用，推动智能系统的进一步发展。

## 📄 摘要（原文）

> The task adaptation and alignment of Large Multimodal Models (LMMs) have been significantly advanced by instruction tuning and further strengthened by recent preference optimization. Yet, most LMMs still suffer from severe modality imbalance during reasoning, i.e., outweighing language prior biases over visual inputs, which bottlenecks their generalization to downstream tasks and causes hallucinations. However, existing preference optimization approaches for LMMs do not focus on restraining the internal biases of their Large Language Model (LLM) backbones when curating the training data. Moreover, they heavily rely on offline data and lack the capacity to explore diverse responses adaptive to dynamic distributional shifts during training. Meanwhile, Group Relative Policy Optimization (GRPO), a recent method using online-generated data and verified rewards to improve reasoning capabilities, remains largely underexplored in LMM alignment. In this paper, we propose a novel preference learning framework, Modality-Balancing Preference Optimization (MBPO), to address the modality imbalance in LMMs. MBPO constructs a more effective offline preference dataset by generating hard negatives, i.e., rejected responses misled by LLM biases due to limited usage of visual information, through adversarial perturbation of input images. Moreover, MBPO leverages the easy-to-verify nature of close-ended tasks to generate online responses with verified rewards. GRPO is then employed to train the model with offline-online hybrid data. Extensive experiments demonstrate that MBPO can enhance LMM performance on challenging vision-language tasks and effectively reduce hallucinations.

