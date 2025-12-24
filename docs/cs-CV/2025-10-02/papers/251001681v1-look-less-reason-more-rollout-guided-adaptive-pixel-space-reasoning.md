---
layout: default
title: "Look Less, Reason More: Rollout-Guided Adaptive Pixel-Space Reasoning"
---

# Look Less, Reason More: Rollout-Guided Adaptive Pixel-Space Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.01681" class="toolbar-btn" target="_blank">📄 arXiv: 2510.01681v1</a>
  <a href="https://arxiv.org/pdf/2510.01681.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.01681v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.01681v1', 'Look Less, Reason More: Rollout-Guided Adaptive Pixel-Space Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xuchen Li, Xuzhao Li, Jiahui Gao, Renjie Pi, Shiyu Hu, Wentao Zhang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-02

**备注**: Preprint, Under review

---

## 💡 一句话要点

**提出基于Rollout引导的自适应像素空间推理框架，提升VLM在细粒度视觉任务上的效率和准确性。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `像素空间推理` `自适应推理` `强化学习` `多模态学习`

## 📋 核心要点

1. 现有VLM在处理细粒度视觉信息时存在信息损失和注意力不足的问题，导致性能瓶颈。
2. 提出一种自适应像素推理框架，通过rollout引导的强化学习动态决定何时使用像素级操作。
3. 实验表明，该模型在提高准确率的同时，显著降低了不必要的视觉操作，提升了效率。

## 📝 摘要（中文）

视觉-语言模型(VLM)在许多多模态任务中表现出色，但经常难以处理需要精确理解和处理细粒度视觉元素。这主要是由于图像编码过程中的信息丢失或对关键区域的关注不足。最近的研究表明，将像素级视觉信息纳入推理过程是有希望的，这使得VLM能够在思考过程中访问高分辨率的视觉细节。然而，这种像素级信息经常被过度使用，导致效率低下并分散对不相关视觉细节的注意力。为了解决这些挑战，我们提出了第一个自适应像素推理框架，该框架基于输入查询动态地确定必要的像素级操作。具体来说，我们首先应用操作感知的监督微调，以建立文本推理和视觉操作的基线能力，然后设计了一种新颖的rollout引导的强化学习框架，该框架依赖于模型自身响应的反馈，这使得VLM能够根据查询难度确定何时应调用像素操作。在广泛的多模态推理基准上的实验表明，我们的模型实现了卓越的性能，同时显著减少了不必要的视觉操作。令人印象深刻的是，我们的模型在HR-Bench 4K上实现了73.4%的准确率，同时保持了仅20.1%的工具使用率，与之前的方法相比，提高了准确率，同时降低了66.5%的工具使用率。

## 🔬 方法详解

**问题定义**：现有视觉-语言模型在处理需要精细视觉理解的任务时，往往过度依赖像素级信息，导致计算效率低下，并容易被无关信息干扰。因此，如何让模型在需要时才关注像素级细节，避免不必要的计算，是本文要解决的问题。

**核心思路**：本文的核心思路是让模型学会根据输入查询的难度，自适应地决定是否需要进行像素级操作。通过强化学习，模型可以根据自身的反馈来学习何时以及如何使用像素级信息，从而在保证准确率的同时，降低计算成本。

**技术框架**：该框架包含两个主要阶段：首先，进行操作感知的监督微调，使模型具备基本的文本推理和视觉操作能力。然后，使用rollout引导的强化学习，让模型学习根据查询难度动态决定是否调用像素操作。强化学习的目标是最大化奖励，奖励基于模型的准确率和工具使用率。

**关键创新**：该方法最重要的创新点在于提出了rollout引导的强化学习框架，该框架允许模型根据自身的反馈来学习何时使用像素级操作。与以往方法相比，该方法能够更有效地利用像素级信息，避免过度使用，从而提高效率和准确率。

**关键设计**：在强化学习中，奖励函数的设计至关重要。本文的奖励函数综合考虑了模型的准确率和工具使用率，鼓励模型在保证准确率的前提下，尽可能减少工具的使用。Rollout策略用于估计不同动作的长期回报，从而指导模型的学习。

## 📊 实验亮点

该模型在HR-Bench 4K数据集上取得了73.4%的准确率，同时工具使用率仅为20.1%。与之前的方法相比，准确率得到了显著提升，同时工具使用率降低了66.5%。这些结果表明，该模型能够有效地利用像素级信息，并在保证准确率的同时，显著降低计算成本。

## 🎯 应用场景

该研究成果可应用于需要细粒度视觉理解的各种场景，例如图像编辑、视觉问答、机器人导航等。通过自适应地利用像素级信息，可以提高模型在这些任务中的性能和效率，使其能够更好地理解和处理复杂的视觉信息。该方法还可以推广到其他需要权衡计算成本和性能的任务中。

## 📄 摘要（原文）

> Vision-Language Models (VLMs) excel at many multimodal tasks, yet they frequently struggle with tasks requiring precise understanding and handling of fine-grained visual elements. This is mainly due to information loss during image encoding or insufficient attention to critical regions. Recent work has shown promise by incorporating pixel-level visual information into the reasoning process, enabling VLMs to access high-resolution visual details during their thought process. However, this pixel-level information is often overused, leading to inefficiency and distraction from irrelevant visual details. To address these challenges, we propose the first framework for adaptive pixel reasoning that dynamically determines necessary pixel-level operations based on the input query. Specifically, we first apply operation-aware supervised fine-tuning to establish baseline competence in textual reasoning and visual operations, then design a novel rollout-guided reinforcement learning framework relying on feedback of the model's own responses, which enables the VLM to determine when pixel operations should be invoked based on query difficulty. Experiments on extensive multimodal reasoning benchmarks show that our model achieves superior performance while significantly reducing unnecessary visual operations. Impressively, our model achieves 73.4\% accuracy on HR-Bench 4K while maintaining a tool usage ratio of only 20.1\%, improving accuracy and simultaneously reducing tool usage by 66.5\% compared to the previous methods.

