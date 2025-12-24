---
layout: default
title: "Skywork-VL Reward: An Effective Reward Model for Multimodal Understanding and Reasoning"
---

# Skywork-VL Reward: An Effective Reward Model for Multimodal Understanding and Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07263" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07263v2</a>
  <a href="https://arxiv.org/pdf/2505.07263.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07263v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07263v2', 'Skywork-VL Reward: An Effective Reward Model for Multimodal Understanding and Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaokun Wang, Peiyu Wang, Jiangbo Pei, Wei Shen, Yi Peng, Yunzhuo Hao, Weijie Qiu, Ai Jian, Tianyidan Xie, Xuchen Song, Yang Liu, Yahui Zhou

**分类**: cs.CV

**发布日期**: 2025-05-12 (更新: 2025-06-09)

---

## 💡 一句话要点

**提出Skywork-VL Reward以提升多模态理解与推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态理解` `奖励模型` `推理能力` `偏好数据集` `深度学习`

## 📋 核心要点

1. 现有的多模态理解和推理模型在奖励信号的生成和利用上存在不足，限制了其性能。
2. 论文提出的Skywork-VL Reward通过构建大规模多模态偏好数据集和设计新的奖励模型架构，解决了这一问题。
3. 实验结果显示，Skywork-VL Reward在多模态VL-RewardBench上达到了最先进的水平，并在文本单一的RewardBench上表现出色。

## 📝 摘要（中文）

我们提出了Skywork-VL Reward，这是一种多模态奖励模型，为多模态理解和推理任务提供奖励信号。我们的技术方法包括两个关键组件：首先，构建了一个覆盖广泛任务和场景的大规模多模态偏好数据集，收集了来自标准视觉语言模型(VLMs)和先进VLM推理器的响应。其次，设计了基于Qwen2.5-VL-7B-Instruct的奖励模型架构，集成了奖励头，并在成对偏好数据上应用多阶段微调。实验评估表明，Skywork-VL Reward在多模态VL-RewardBench上达到了最先进的结果，并在文本单一的RewardBench基准上表现出竞争力。此外，基于Skywork-VL Reward构建的偏好数据在训练混合偏好优化(MPO)中证明了其高效性，显著提升了多模态推理能力。我们的结果强调了Skywork-VL Reward在通用可靠的多模态对齐奖励模型方面的重要进展。该模型已公开发布，以促进透明性和可重复性。

## 🔬 方法详解

**问题定义**：本论文旨在解决多模态理解与推理任务中奖励信号生成的不足，现有方法在多样性和有效性上存在挑战。

**核心思路**：论文的核心思路是通过构建大规模的多模态偏好数据集，结合先进的奖励模型架构，来提升多模态任务的性能。这样的设计旨在更好地捕捉用户偏好，提供更精准的奖励信号。

**技术框架**：整体架构包括两个主要模块：一是多模态偏好数据集的构建，二是基于Qwen2.5-VL-7B-Instruct的奖励模型，后者集成了奖励头并采用多阶段微调策略。

**关键创新**：最重要的技术创新点在于构建了一个覆盖广泛任务的大规模多模态偏好数据集，并设计了基于成对偏好数据的多阶段微调机制，显著提升了模型的推理能力。

**关键设计**：在模型设计中，采用了成对排名损失函数进行训练，确保模型能够有效学习用户的偏好，并通过奖励头的集成提升了模型的适应性和准确性。

## 📊 实验亮点

实验结果表明，Skywork-VL Reward在多模态VL-RewardBench上达到了最先进的结果，具体性能数据未提供，但显示出显著的提升。此外，该模型在文本单一的RewardBench基准上也展现了竞争力，证明了其广泛适用性。

## 🎯 应用场景

Skywork-VL Reward的研究成果在多个领域具有潜在应用价值，包括智能助手、自动问答系统和多模态内容生成等。通过提升多模态理解与推理能力，该模型能够为用户提供更智能、更个性化的服务，推动人机交互的进步。未来，该模型的进一步优化和应用可能会在更广泛的场景中发挥重要作用。

## 📄 摘要（原文）

> We propose Skywork-VL Reward, a multimodal reward model that provides reward signals for both multimodal understanding and reasoning tasks. Our technical approach comprises two key components: First, we construct a large-scale multimodal preference dataset that covers a wide range of tasks and scenarios, with responses collected from both standard vision-language models (VLMs) and advanced VLM reasoners. Second, we design a reward model architecture based on Qwen2.5-VL-7B-Instruct, integrating a reward head and applying multi-stage fine-tuning using pairwise ranking loss on pairwise preference data. Experimental evaluations show that Skywork-VL Reward achieves state-of-the-art results on multimodal VL-RewardBench and exhibits competitive performance on the text-only RewardBench benchmark. Furthermore, preference data constructed based on our Skywork-VL Reward proves highly effective for training Mixed Preference Optimization (MPO), leading to significant improvements in multimodal reasoning capabilities. Our results underscore Skywork-VL Reward as a significant advancement toward general-purpose, reliable reward models for multimodal alignment. Our model has been publicly released to promote transparency and reproducibility.

