---
layout: default
title: "From General to Targeted Rewards: Surpassing GPT-4 in Open-Ended Long-Context Generation"
---

# From General to Targeted Rewards: Surpassing GPT-4 in Open-Ended Long-Context Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16024" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16024v1</a>
  <a href="https://arxiv.org/pdf/2506.16024.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16024v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16024v1', 'From General to Targeted Rewards: Surpassing GPT-4 in Open-Ended Long-Context Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhihan Guo, Jiele Wu, Wenqian Cui, Yifei Zhang, Minda Hu, Yufei Wang, Irwin King

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-19

---

## 💡 一句话要点

**提出ProxyReward以提升长文本生成模型的表现**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长文本生成` `强化学习` `奖励信号` `数据集生成` `信息评估`

## 📋 核心要点

1. 现有长文本生成方法主要依赖一般性评估作为奖励信号，导致生成内容的准确性和信息完整性不足。
2. 本文提出ProxyReward框架，通过简单提示生成数据集，并提供针对特定问题的奖励信号，提升生成模型的表现。
3. 实验结果显示，ProxyReward在Open-LTG任务上超越了GPT-4-Turbo，提升幅度达到20%，并优于LLM-as-a-Judge方法。

## 📝 摘要（中文）

当前对大型语言模型（LLMs）在长文本生成（Open-LTG）方面的研究仍显不足，尤其是在缺乏高质量参考数据的情况下。现有方法主要依赖于一般性评估作为奖励信号，导致生成准确性受限。为此，本文提出了ProxyReward，一个基于强化学习的框架，包含数据集生成和奖励信号计算方法。通过简单提示生成ProxyReward数据集，模型能够自动创建内容，避免了大量标注数据的需求。同时，ProxyReward信号为特定问题提供了针对性的信息全面性和准确性评估。实验结果表明，ProxyReward在Open-LTG任务上超越了GPT-4-Turbo，显著提升了20%的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决长文本生成任务中缺乏高质量参考数据的问题，现有方法依赖一般性评估，导致生成内容的准确性和信息完整性不足。

**核心思路**：提出ProxyReward框架，通过简单提示生成数据集，避免了对大量标注数据的依赖，同时提供针对性奖励信号，以提升生成模型的表现。

**技术框架**：ProxyReward框架包括两个主要模块：ProxyReward数据集生成和ProxyReward信号计算。数据集生成通过简单的提示自动创建内容，而信号计算则针对特定问题评估生成内容的全面性和准确性。

**关键创新**：ProxyReward的核心创新在于其数据集生成和奖励信号计算方法，区别于传统方法仅依赖一般性评估，提供了更为精准的反馈机制。

**关键设计**：在ProxyReward框架中，数据集生成采用简单提示，确保生成内容的多样性和相关性；奖励信号计算则专注于信息的全面性和准确性，确保模型在特定问题上的表现得到有效提升。

## 📊 实验亮点

实验结果表明，ProxyReward在Open-LTG任务上超越了GPT-4-Turbo，性能提升幅度达到20%。此外，ProxyReward还优于传统的LLM-as-a-Judge方法，展示了其在长文本生成中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括教育、内容创作和客户服务等，能够帮助生成更为准确和丰富的长文本内容，提升用户体验。未来，ProxyReward框架有望在更多复杂的开放式问题生成任务中得到应用，推动自然语言处理技术的发展。

## 📄 摘要（原文）

> Current research on long-form context in Large Language Models (LLMs) primarily focuses on the understanding of long-contexts, the Open-ended Long Text Generation (Open-LTG) remains insufficiently explored. Training a long-context generation model requires curation of gold standard reference data, which is typically nonexistent for informative Open-LTG tasks. However, previous methods only utilize general assessments as reward signals, which limits accuracy. To bridge this gap, we introduce ProxyReward, an innovative reinforcement learning (RL) based framework, which includes a dataset and a reward signal computation method. Firstly, ProxyReward Dataset generation is accomplished through simple prompts that enables the model to create automatically, obviating extensive labeled data or significant manual effort. Secondly, ProxyReward Signal offers a targeted evaluation of information comprehensiveness and accuracy for specific questions. The experimental results indicate that our method ProxyReward surpasses even GPT-4-Turbo. It can significantly enhance performance by 20% on the Open-LTG task when training widely used open-source models, while also surpassing the LLM-as-a-Judge approach. Our work presents effective methods to enhance the ability of LLMs to address complex open-ended questions posed by human.

