---
layout: default
title: "Writing-RL: Advancing Long-form Writing via Adaptive Curriculum Reinforcement Learning"
---

# Writing-RL: Advancing Long-form Writing via Adaptive Curriculum Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05760" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05760v1</a>
  <a href="https://arxiv.org/pdf/2506.05760.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05760v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05760v1', 'Writing-RL: Advancing Long-form Writing via Adaptive Curriculum Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xuanyu Lei, Chenliang Li, Yuning Wu, Kaiming Liu, Weizhou Shen, Peng Li, Ming Yan, Ji Zhang, Fei Huang, Yang Liu

**分类**: cs.CL

**发布日期**: 2025-06-06

**备注**: Work in progress

---

## 💡 一句话要点

**提出Writing-RL框架以提升长篇写作能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长篇写作` `强化学习` `自适应课程` `数据选择` `奖励机制` `模型泛化` `长上下文训练`

## 📋 核心要点

1. 现有的监督微调方法在长篇写作中面临数据饱和和学习能力受限的问题，限制了模型的表现。
2. 本文提出Writing-RL框架，通过自适应课程强化学习，优化长篇写作能力，包含数据选择、奖励机制和任务调度等核心思想。
3. 实验结果显示，使用该框架的模型在长篇写作任务上显著超越传统SFT基线，并在长输入推理任务中展现出良好的泛化能力。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）的进步使得长篇写作表现显著提升，但现有的监督微调（SFT）方法存在数据饱和和学习能力受限等问题。本文提出了Writing-RL：一种自适应课程强化学习框架，以超越SFT提升长篇写作能力。该框架包含三个关键组件：关注边际的数据选择策略，优先选择具有高学习潜力的样本；成对比较奖励机制，在缺乏可验证奖励的情况下提供区分性学习信号；动态参考调度方法，根据模型性能的变化自适应调整任务难度。实验结果表明，基于7B规模写作模型的RL框架在长篇写作性能上显著优于强基线SFT。此外，使用长输出RL训练的模型在长输入推理任务上也表现出良好的泛化能力，可能为重新思考长上下文训练提供了新的视角。

## 🔬 方法详解

**问题定义**：本文旨在解决现有长篇写作模型在监督微调过程中面临的数据饱和和学习能力受限的问题，这些问题导致模型在生成长文本时的表现不佳。

**核心思路**：提出Writing-RL框架，通过自适应课程强化学习，优化长篇写作能力。该框架通过动态调整学习任务的难度和奖励机制，提升模型的学习效率和生成质量。

**技术框架**：整体架构包括三个主要模块：1) 边际数据选择策略，优先选择高学习潜力样本；2) 成对比较奖励机制，提供区分性学习信号；3) 动态参考调度方法，根据模型性能变化自适应调整任务难度。

**关键创新**：最重要的技术创新在于引入了动态参考调度和成对比较奖励机制，这与传统的监督微调方法有本质区别，后者通常依赖固定的奖励信号。

**关键设计**：在数据选择中，采用边际数据选择策略，确保模型接触到具有挑战性的样本；在奖励机制中，设计成对比较奖励，以在缺乏明确奖励的情况下仍能提供有效的学习信号。

## 📊 实验亮点

实验结果表明，使用Writing-RL框架的模型在长篇写作任务上表现显著优于传统的SFT基线，具体提升幅度达到XX%（具体数据未知）。此外，这些模型在长输入推理任务中也展现出良好的泛化能力，表明其训练效果的广泛适用性。

## 🎯 应用场景

该研究的潜在应用领域包括教育、内容创作和自动化写作等。通过提升长篇写作能力，Writing-RL框架可以帮助用户生成更高质量的文本，满足不同场景下的写作需求，未来可能对内容生成行业产生深远影响。

## 📄 摘要（原文）

> Recent advances in Large Language Models (LLMs) have enabled strong performance in long-form writing, yet existing supervised fine-tuning (SFT) approaches suffer from limitations such as data saturation and restricted learning capacity bounded by teacher signals. In this work, we present Writing-RL: an Adaptive Curriculum Reinforcement Learning framework to advance long-form writing capabilities beyond SFT. The framework consists of three key components: Margin-aware Data Selection strategy that prioritizes samples with high learning potential, Pairwise Comparison Reward mechanism that provides discriminative learning signals in the absence of verifiable rewards, and Dynamic Reference Scheduling approach, which plays a particularly critical role by adaptively adjusting task difficulty based on evolving model performance. Experiments on 7B-scale writer models show that our RL framework largely improves long-form writing performance over strong SFT baselines. Furthermore, we observe that models trained with long-output RL generalize surprisingly well to long-input reasoning tasks, potentially offering a promising perspective for rethinking long-context training.

