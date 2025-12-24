---
layout: default
title: "ShinkaEvolve: Towards Open-Ended And Sample-Efficient Program Evolution"
---

# ShinkaEvolve: Towards Open-Ended And Sample-Efficient Program Evolution

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.19349" class="toolbar-btn" target="_blank">📄 arXiv: 2509.19349v1</a>
  <a href="https://arxiv.org/pdf/2509.19349.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.19349v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.19349v1', 'ShinkaEvolve: Towards Open-Ended And Sample-Efficient Program Evolution')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Robert Tjarko Lange, Yuki Imajuku, Edoardo Cetin

**分类**: cs.CL, cs.LG

**发布日期**: 2025-09-17

**备注**: 52 pages, 14 figures

---

## 💡 一句话要点

**ShinkaEvolve：提出一种高效、开源的程序进化框架，用于解决科学发现中的样本效率问题。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `程序进化` `大型语言模型` `科学发现` `样本效率` `开源框架`

## 📋 核心要点

1. 现有代码进化方法样本效率低，且多为闭源，限制了其在科学发现中的应用。
2. ShinkaEvolve通过父代抽样、代码新颖性拒绝抽样和bandit LLM集成选择策略，提升样本效率。
3. 实验表明，ShinkaEvolve在圆形packing、数学推理和竞争性编程等任务上均有提升。

## 📝 摘要（中文）

本文介绍ShinkaEvolve，这是一个新的开源框架，它利用大型语言模型（LLM）以最先进的性能和前所未有的效率来推进科学发现。LLM推理计算的扩展使得广义科学发现取得了显著进展。这些方法依赖于进化代理框架，利用LLM作为变异算子来生成候选解决方案。然而，当前的代码进化方法存在关键限制：样本效率低，需要数千个样本才能识别有效的解决方案，并且仍然是闭源的，阻碍了广泛采用和扩展。ShinkaEvolve通过引入三个关键创新来解决这些限制：一种平衡探索和利用的父代抽样技术，用于有效搜索空间探索的代码新颖性拒绝抽样，以及一种基于bandit的LLM集成选择策略。我们在各种任务中评估ShinkaEvolve，证明了样本效率和解决方案质量的持续改进。ShinkaEvolve仅使用150个样本就发现了一种新的最先进的圆形 packing 解决方案，为AIME数学推理任务设计了高性能的代理框架，识别了对ALE-Bench竞争性编程解决方案的改进，并发现了新的混合专家负载平衡损失函数，从而阐明了优化策略的空间。我们的结果表明，ShinkaEvolve具有广泛的适用性和卓越的样本效率。通过提供开源可访问性和成本效益，这项工作使各种计算问题上的开放式发现民主化。

## 🔬 方法详解

**问题定义**：论文旨在解决程序进化中样本效率低下的问题，尤其是在利用大型语言模型（LLM）进行科学发现时。现有的基于LLM的程序进化方法通常需要大量的样本才能找到有效的解决方案，这限制了它们在计算资源有限或评估成本高昂的场景中的应用。此外，许多现有方法是闭源的，阻碍了研究人员的进一步改进和扩展。

**核心思路**：ShinkaEvolve的核心思路是通过更智能的搜索策略来提高样本的利用率，从而在更少的样本下找到更好的解决方案。具体来说，它通过平衡探索和利用的父代抽样策略，鼓励探索新的代码变异，同时保留有希望的解决方案。此外，通过代码新颖性拒绝抽样，避免重复探索相似的解决方案，从而更有效地覆盖搜索空间。最后，使用bandit算法动态选择最适合当前任务的LLM，进一步提高效率。

**技术框架**：ShinkaEvolve的整体框架是一个进化循环，包括以下几个主要阶段：1) 初始化：生成一组初始代码解决方案。2) 父代选择：使用父代抽样策略选择用于变异的父代。3) 代码变异：使用LLM作为变异算子，生成新的代码解决方案。4) 代码新颖性评估：使用代码新颖性拒绝抽样，过滤掉相似的解决方案。5) 评估：评估新代码解决方案的性能。6) LLM选择：使用bandit算法选择下一个迭代中使用的LLM。7) 重复步骤2-6，直到达到停止条件。

**关键创新**：ShinkaEvolve的关键创新在于其三个核心组件：1) 平衡探索和利用的父代抽样策略：该策略旨在选择既有潜力又具有多样性的父代，从而促进更有效的搜索。2) 代码新颖性拒绝抽样：通过拒绝与现有解决方案过于相似的候选方案，避免浪费计算资源在已经探索过的区域。3) 基于bandit的LLM集成选择策略：根据不同LLM在不同任务上的表现，动态选择最合适的LLM，从而提高整体性能。

**关键设计**：父代抽样策略可能涉及基于性能和多样性的评分函数，用于选择父代。代码新颖性拒绝抽样可能使用代码相似度度量（例如，编辑距离或语义相似度）来确定候选方案是否足够新颖。基于bandit的LLM集成选择策略可能使用Thompson Sampling或UCB等算法来平衡探索和利用，并根据LLM的性能动态调整选择概率。具体的损失函数和网络结构取决于具体的应用场景。

## 📊 实验亮点

ShinkaEvolve在多个任务上表现出色。在圆形packing问题中，仅用150个样本就找到了新的state-of-the-art解决方案。在AIME数学推理任务中，设计了高性能的代理框架。在ALE-Bench竞争性编程中，发现了对现有解决方案的改进。此外，还发现了新的混合专家负载平衡损失函数，揭示了优化策略的新方向。

## 🎯 应用场景

ShinkaEvolve可应用于各种科学发现和优化问题，例如新算法设计、自动化程序修复、超参数优化、以及寻找新的数学公式或物理定律。其高样本效率使其特别适用于评估成本高昂或数据获取困难的场景。该框架的开源特性促进了社区合作和进一步发展，有望加速科学研究的进程。

## 📄 摘要（原文）

> We introduce ShinkaEvolve: a new open-source framework leveraging large language models (LLMs) to advance scientific discovery with state-of-the-art performance and unprecedented efficiency. Recent advances in scaling inference time compute of LLMs have enabled significant progress in generalized scientific discovery. These approaches rely on evolutionary agentic harnesses that leverage LLMs as mutation operators to generate candidate solutions. However, current code evolution methods suffer from critical limitations: they are sample inefficient, requiring thousands of samples to identify effective solutions, and remain closed-source, hindering broad adoption and extension. ShinkaEvolve addresses these limitations, introducing three key innovations: a parent sampling technique balancing exploration and exploitation, code novelty rejection-sampling for efficient search space exploration, and a bandit-based LLM ensemble selection strategy. We evaluate ShinkaEvolve across diverse tasks, demonstrating consistent improvements in sample efficiency and solution quality. ShinkaEvolve discovers a new state-of-the-art circle packing solution using only 150 samples, designs high-performing agentic harnesses for AIME mathematical reasoning tasks, identifies improvements to ALE-Bench competitive programming solutions, and discovers novel mixture-of-expert load balancing loss functions that illuminate the space of optimization strategies. Our results demonstrate that ShinkaEvolve achieves broad applicability with exceptional sample efficiency. By providing open-source accessibility and cost-efficiency, this work democratizes open-ended discovery across diverse computational problems.

