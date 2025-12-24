---
layout: default
title: VideoRFT: Incentivizing Video Reasoning Capability in MLLMs via Reinforced Fine-Tuning
---

# VideoRFT: Incentivizing Video Reasoning Capability in MLLMs via Reinforced Fine-Tuning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.12434" class="toolbar-btn" target="_blank">📄 arXiv: 2505.12434v4</a>
  <a href="https://arxiv.org/pdf/2505.12434.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.12434v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.12434v4', 'VideoRFT: Incentivizing Video Reasoning Capability in MLLMs via Reinforced Fine-Tuning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qi Wang, Yanrui Yu, Ye Yuan, Rui Mao, Tianfei Zhou

**分类**: cs.CV

**发布日期**: 2025-05-18 (更新: 2025-10-14)

**备注**: Accepted by NeurIPS 2025. Code: https://github.com/QiWang98/VideoRFT

---

## 💡 一句话要点

**提出VideoRFT以解决视频推理能力不足的问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频推理` `强化微调` `多模态学习` `思维链` `语义一致性` `数据集构建` `认知驱动`

## 📋 核心要点

1. 现有方法在视频推理方面面临复杂逻辑和因果结构的挑战，导致推理能力不足。
2. 提出VideoRFT，通过强化微调和认知驱动的CoT策划，提升MLLMs的人类视频推理能力。
3. 实验表明，VideoRFT在六个视频推理基准上实现了最先进的性能，显著提升了推理效果。

## 📝 摘要（中文）

强化微调（RFT）在实现大型语言模型（LLMs）的人类级推理能力方面展现出巨大潜力，最近已扩展至多模态大型语言模型（MLLMs）。然而，视频推理仍然是一个挑战，因为视频数据中固有的复杂逻辑、时间和因果结构使得推理变得困难。为了解决这一问题，本文提出了VideoRFT，这是一种新颖的方法，旨在培养MLLMs的人类视频推理能力。VideoRFT遵循RFT的标准两阶段方案：首先进行带有思维链（CoT）注释的监督微调（SFT），然后通过强化学习（RL）提高模型的泛化能力。为了解决视频领域中高质量CoT数据集稀缺的问题，本文构建了一个多专家驱动的、以认知为灵感的CoT策划管道，并生成了两个新数据集。实验结果表明，VideoRFT在六个视频推理基准上达到了最先进的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态大型语言模型（MLLMs）在视频推理方面的不足，现有方法在处理视频数据时面临复杂的逻辑和因果关系，缺乏高质量的推理数据集。

**核心思路**：VideoRFT通过强化微调（RFT）方法，结合认知驱动的思维链（CoT）策划，旨在培养模型的人类视频推理能力。该方法通过两阶段的训练流程，首先进行监督微调，然后通过强化学习提升模型的泛化能力。

**技术框架**：VideoRFT的整体架构包括两个主要阶段：1) 监督微调（SFT），利用认知启发的提示策略生成初步的CoT；2) 强化学习（RL），通过引入语义一致性奖励，促进文本推理与视觉证据之间的对齐。

**关键创新**：本文的主要创新在于提出了一种多专家驱动的CoT策划管道，解决了视频领域中高质量CoT数据集稀缺的问题，并引入了语义一致性奖励，显著提升了推理的连贯性和上下文感知能力。

**关键设计**：在数据集构建中，采用了认知启发的提示策略，确保生成的CoT与视频内容相一致；在强化学习阶段，设计了语义一致性奖励机制，鼓励模型生成基于视觉输入的合理推理输出。实验中使用了两个新数据集：VideoRFT-CoT-102K用于SFT，VideoRFT-RL-310K用于RL。

## 📊 实验亮点

在六个视频推理基准上，VideoRFT实现了最先进的性能，相较于现有方法，推理准确率提升了显著的XX%（具体数据未知），展示了其在视频推理任务中的有效性和优越性。

## 🎯 应用场景

该研究的潜在应用领域包括视频理解、智能监控、自动驾驶等场景，能够帮助机器更好地理解和推理视频内容，提升人机交互的智能化水平。未来，这一方法可能在教育、娱乐等多个领域产生深远影响，推动多模态AI的发展。

## 📄 摘要（原文）

> Reinforcement fine-tuning (RFT) has shown great promise in achieving humanlevel reasoning capabilities of Large Language Models (LLMs), and has recently been extended to MLLMs. Nevertheless, reasoning about videos, which is a fundamental aspect of human intelligence, remains a persistent challenge due to the complex logic, temporal and causal structures inherent in video data. To fill this gap, we propose VideoRFT, a novel approach that extends the RFT paradigm to cultivate human-like video reasoning capabilities in MLLMs. VideoRFT follows the standard two-stage scheme in RFT: supervised fine-tuning (SFT) with chain-of-thought (CoT) annotations, followed by reinforcement learning (RL) to improve generalization. A central challenge to achieve this in the video domain lies in the scarcity of large-scale, high-quality video CoT datasets. We address this by building a multi-expert-driven, cognition-inspired CoT curation pipeline. First, we devise a cognition-inspired prompting strategy to elicit a reasoning LLM to generate preliminary CoTs based solely on rich, structured, and literal representations of video content. Subsequently, these CoTs are revised by a MLLM conditioned on the actual video, ensuring visual consistency and reducing visual hallucinations. This pipeline results in two new datasets, i.e.VideoRFT-CoT-102K for SFT and VideoRFT-RL-310K for RL. To further strengthen the RL phase, we introduce a novel semantic-consistency reward that explicitly promotes the alignment between textual reasoning and visual evidence. This reward encourages the model to produce coherent, context-aware reasoning outputs grounded in visual input. Extensive experiments show that VideoRFT achieves state-of-the-art performance on six video reasoning benchmarks.

