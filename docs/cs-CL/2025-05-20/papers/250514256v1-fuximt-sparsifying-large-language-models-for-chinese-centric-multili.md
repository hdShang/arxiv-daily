---
layout: default
title: FuxiMT: Sparsifying Large Language Models for Chinese-Centric Multilingual Machine Translation
---

# FuxiMT: Sparsifying Large Language Models for Chinese-Centric Multilingual Machine Translation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14256" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14256v1</a>
  <a href="https://arxiv.org/pdf/2505.14256.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14256v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14256v1', 'FuxiMT: Sparsifying Large Language Models for Chinese-Centric Multilingual Machine Translation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shaolin Zhu, Tianyu Dong, Bo Li, Deyi Xiong

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-20

---

## 💡 一句话要点

**提出FuxiMT以解决中文为中心的多语言机器翻译问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多语言翻译` `稀疏模型` `机器翻译` `中文处理` `课程学习` `专家混合模型` `低资源翻译`

## 📋 核心要点

1. 现有的多语言机器翻译模型在低资源语言对的翻译性能较差，尤其是中文为中心的场景中。
2. FuxiMT通过稀疏化的大型语言模型和课程学习策略，采用两阶段训练方法，提升了多语言翻译的效果。
3. 实验结果显示，FuxiMT在低资源场景下的表现显著优于现有的最先进模型，尤其在零-shot翻译任务中表现突出。

## 📝 摘要（中文）

本文提出了一种新颖的中文为中心的多语言机器翻译模型FuxiMT，该模型基于稀疏的大型语言模型（LLM）。我们采用两阶段策略训练FuxiMT，首先在大规模中文语料上进行预训练，然后在包含65种语言的大型平行数据集上进行多语言微调。FuxiMT结合了专家混合模型（MoEs）并采用了课程学习策略，以在不同资源水平下实现稳健的性能。实验结果表明，FuxiMT在低资源场景下显著超越了强基线，包括最先进的LLM和机器翻译模型。此外，FuxiMT在未见语言对的零-shot翻译能力上表现出色，显示出其在平行数据稀缺或不可用情况下弥合沟通差距的潜力。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多语言机器翻译模型在低资源语言对翻译中的不足，特别是在中文为中心的翻译场景中，现有方法往往无法有效利用稀缺的平行数据。

**核心思路**：FuxiMT的核心思路是通过稀疏化的大型语言模型（LLM）结合专家混合模型（MoEs）和课程学习策略，提升模型在多语言翻译中的表现，尤其是在低资源情况下的翻译能力。

**技术框架**：FuxiMT的整体架构分为两个主要阶段：首先在大规模中文语料上进行预训练，然后在包含65种语言的平行数据集上进行多语言微调。模型通过Mixture-of-Experts机制动态选择专家，以适应不同的翻译任务。

**关键创新**：FuxiMT的主要创新在于结合了稀疏化的LLM与MoEs，允许模型在不同资源水平下灵活调整，同时通过课程学习策略增强了模型的学习能力和适应性。与现有方法相比，FuxiMT在低资源场景下的表现更为优越。

**关键设计**：在模型设计中，FuxiMT采用了动态选择专家的机制，设置了适应不同语言对的损失函数，并优化了网络结构以提高翻译精度和效率。

## 📊 实验亮点

实验结果表明，FuxiMT在低资源场景下的翻译性能显著优于现有的最先进模型，尤其在零-shot翻译任务中，FuxiMT能够有效处理未见语言对，展示出高达XX%的性能提升，具体数据待补充。

## 🎯 应用场景

FuxiMT的研究成果在多语言机器翻译领域具有广泛的应用潜力，尤其适用于中文与其他语言之间的翻译。其在低资源语言对的优越表现，能够帮助解决全球范围内的语言沟通障碍，促进跨文化交流与合作。未来，该模型有望在教育、国际贸易和旅游等多个领域发挥重要作用。

## 📄 摘要（原文）

> In this paper, we present FuxiMT, a novel Chinese-centric multilingual machine translation model powered by a sparsified large language model (LLM). We adopt a two-stage strategy to train FuxiMT. We first pre-train the model on a massive Chinese corpus and then conduct multilingual fine-tuning on a large parallel dataset encompassing 65 languages. FuxiMT incorporates Mixture-of-Experts (MoEs) and employs a curriculum learning strategy for robust performance across various resource levels. Experimental results demonstrate that FuxiMT significantly outperforms strong baselines, including state-of-the-art LLMs and machine translation models, particularly under low-resource scenarios. Furthermore, FuxiMT exhibits remarkable zero-shot translation capabilities for unseen language pairs, indicating its potential to bridge communication gaps where parallel data are scarce or unavailable.

