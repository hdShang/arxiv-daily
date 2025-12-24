---
layout: default
title: "Your Reward Function for RL is Your Best PRM for Search: Unifying RL and Search-Based TTS"
---

# Your Reward Function for RL is Your Best PRM for Search: Unifying RL and Search-Based TTS

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14313" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14313v2</a>
  <a href="https://arxiv.org/pdf/2508.14313.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14313v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14313v2', 'Your Reward Function for RL is Your Best PRM for Search: Unifying RL and Search-Based TTS')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Can Jin, Yang Zhou, Qixin Zhang, Hongwu Peng, Di Zhang, Marco Pavone, Ligong Han, Zhang-Wei Hong, Tong Che, Dimitris N. Metaxas

**分类**: cs.LG, cs.AI

**发布日期**: 2025-08-19 (更新: 2025-08-22)

---

## 💡 一句话要点

**提出AIRL-S以统一强化学习与基于搜索的测试时缩放问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `搜索算法` `过程奖励模型` `对抗性学习` `动态优化` `推理能力` `大型语言模型`

## 📋 核心要点

1. 现有的强化学习方法在优化稀疏奖励时面临不稳定和低样本效率的问题，基于搜索的技术则依赖昂贵的标签数据，且在分布转移时表现不佳。
2. 本文提出AIRL-S，通过对抗性逆强化学习和群体相对策略优化，直接从正确推理轨迹中学习动态过程奖励模型，消除了对标记数据的需求。
3. 在八个基准测试中，AIRL-S平均提升9%的性能，且在多个搜索算法中表现优于所有基于标记数据训练的基线过程奖励模型。

## 📝 摘要（中文）

测试时缩放（TTS）在大型语言模型（LLMs）中面临两大主要挑战：一是强化学习（RL）方法优化稀疏的基于结果的奖励，导致不稳定和低样本效率；二是基于搜索的技术依赖独立训练的静态过程奖励模型（PRMs），需要昂贵的人工或LLM生成标签，并在分布转移下表现不佳。本文提出AIRL-S，首次自然统一RL和基于搜索的TTS。我们利用对抗性逆强化学习（AIRL）结合群体相对策略优化（GRPO），直接从正确推理轨迹中学习动态PRM，消除了对标记中间过程数据的需求。在推理时，生成的PRM同时作为RL回滚的评论者和有效指导搜索程序的启发式方法，增强了跨任务泛化能力。实验结果表明，该方法在八个基准测试中平均提升9%，与GPT-4o相匹配。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在测试时缩放中的两大挑战：强化学习方法的不稳定性和低样本效率，以及基于搜索的技术对标记数据的依赖和在分布转移下的性能下降。

**核心思路**：论文的核心思路是将强化学习训练中学习到的奖励函数视为指导下游搜索的理想过程奖励模型（PRM），通过对抗性逆强化学习（AIRL）和群体相对策略优化（GRPO）来实现这一目标。

**技术框架**：整体架构包括两个主要模块：首先是通过AIRL学习动态PRM，其次是在推理阶段将该PRM用于强化学习回滚和搜索程序的指导。

**关键创新**：最重要的创新在于将RL和基于搜索的方法自然统一，利用动态PRM消除了对标记中间过程数据的需求，增强了模型的适应性和泛化能力。

**关键设计**：在技术细节上，采用了对抗性学习的损失函数和动态更新的策略优化方法，确保PRM能够实时反映正确的推理轨迹，从而提高模型的整体性能。

## 📊 实验亮点

实验结果显示，AIRL-S在八个基准测试中平均提升9%的性能，成功匹配GPT-4o的表现。此外，在多个搜索算法中，AIRL-S的动态PRM始终优于所有基于标记数据训练的基线PRM，展现出显著的优势。

## 🎯 应用场景

该研究的潜在应用领域包括复杂推理任务、自然语言处理和自动代码生成等。通过提供一种更为稳健和经济高效的解决方案，AIRL-S能够在多种实际场景中提升大型语言模型的推理能力，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Test-time scaling (TTS) for large language models (LLMs) has thus far fallen into two largely separate paradigms: (1) reinforcement learning (RL) methods that optimize sparse outcome-based rewards, yet suffer from instability and low sample efficiency; and (2) search-based techniques guided by independently trained, static process reward models (PRMs), which require expensive human- or LLM-generated labels and often degrade under distribution shifts. In this paper, we introduce AIRL-S, the first natural unification of RL-based and search-based TTS. Central to AIRL-S is the insight that the reward function learned during RL training inherently represents the ideal PRM for guiding downstream search. Specifically, we leverage adversarial inverse reinforcement learning (AIRL) combined with group relative policy optimization (GRPO) to learn a dense, dynamic PRM directly from correct reasoning traces, entirely eliminating the need for labeled intermediate process data. At inference, the resulting PRM simultaneously serves as the critic for RL rollouts and as a heuristic to effectively guide search procedures, facilitating robust reasoning chain extension, mitigating reward hacking, and enhancing cross-task generalization. Experimental results across eight benchmarks, including mathematics, scientific reasoning, and code generation, demonstrate that our unified approach improves performance by 9 % on average over the base model, matching GPT-4o. Furthermore, when integrated into multiple search algorithms, our PRM consistently outperforms all baseline PRMs trained with labeled data. These results underscore that, indeed, your reward function for RL is your best PRM for search, providing a robust and cost-effective solution to complex reasoning tasks in LLMs.

