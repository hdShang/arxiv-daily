---
layout: default
title: Scaling Reinforcement Learning for Content Moderation with Large Language Models
---

# Scaling Reinforcement Learning for Content Moderation with Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20061" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20061v1</a>
  <a href="https://arxiv.org/pdf/2512.20061.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20061v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20061v1', 'Scaling Reinforcement Learning for Content Moderation with Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hamed Firooz, Rui Liu, Yuchen Lu, Zhenyu Hou, Fangzhou Xiong, Xiaoyang Zhang, Changshu Jian, Zhicheng Zhu, Jiayuan Ma, Jacob Tao, Chaitali Gupta, Xiaochang Peng, Shike Mei, Hang Cui, Yang Qin, Shuo Tang, Jason Gaedtke, Arpit Mittal

**分类**: cs.AI

**发布日期**: 2025-12-23

---

## 💡 一句话要点

**利用强化学习和大型语言模型提升大规模内容审核的效率与准确性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `内容审核` `强化学习` `大型语言模型` `奖励塑造` `策略对齐`

## 📋 核心要点

1. 现有内容审核方法难以应对标签稀疏、策略演变和复杂推理等挑战，导致审核效率和准确性不足。
2. 论文提出利用强化学习（RL）训练大型语言模型（LLM），通过奖励塑造策略使其成为专业的、符合策略的分类器。
3. 实验表明，RL方法在内容审核任务上表现出良好的扩展性，数据效率比监督微调高出100倍。

## 📝 摘要（中文）

大规模内容审核是当前数字生态系统面临的最紧迫挑战之一，需要持续评估数十亿用户和AI生成的内容，以确定其是否违反政策。尽管大型语言模型（LLM）在基于策略的内容审核方面展现出巨大潜力，但在实际环境中训练这些系统以达到专家级准确率仍然面临诸多挑战，尤其是在标签稀疏、政策定义不断演变以及需要超越浅层模式匹配的细致推理的情况下。本文对使用强化学习（RL）进行内容分类的扩展性进行了全面的实证研究，系统地评估了多种RL训练方法和奖励塑造策略（包括可验证奖励和LLM作为评判框架），以将通用语言模型转化为在三个真实内容审核任务中专门的、符合策略的分类器。研究结果为工业级审核系统提供了可操作的见解，表明RL表现出类似Sigmoid的扩展行为，即性能随着训练数据、rollout和优化步骤的增加而平稳提高，然后逐渐饱和。此外，研究表明，RL在需要复杂策略推理的任务上显著提高了性能，同时实现了比监督微调高出100倍的数据效率，使其在专家标注稀缺或成本高昂的领域特别有效。

## 🔬 方法详解

**问题定义**：论文旨在解决大规模内容审核中，现有方法在标签稀疏、策略定义不断演变以及需要复杂推理的情况下，难以达到专家级准确率的问题。现有方法，如监督学习，需要大量的标注数据，成本高昂，且难以适应策略的快速变化。

**核心思路**：论文的核心思路是利用强化学习（RL）来训练大型语言模型（LLM），使其能够根据内容审核策略进行决策。通过奖励塑造策略，引导LLM学习符合策略的分类行为，从而在数据稀缺的情况下也能达到较高的准确率。这样设计的目的是为了提高数据效率，并使模型能够更好地适应不断变化的策略。

**技术框架**：整体框架包括以下几个主要模块：1）LLM作为Agent，负责对内容进行分类；2）环境，模拟内容审核场景，提供内容样本；3）奖励函数，根据LLM的分类结果和审核策略，给出奖励信号；4）RL算法，用于更新LLM的策略，使其能够获得更高的奖励。其中，奖励函数的设计至关重要，论文探索了多种奖励塑造策略，包括可验证奖励和LLM作为评判框架。

**关键创新**：最重要的技术创新点在于将强化学习应用于内容审核任务，并探索了多种有效的奖励塑造策略。与传统的监督学习方法相比，RL方法能够更好地利用未标注数据，提高数据效率，并适应策略的变化。此外，使用LLM作为评判框架，可以减少对人工标注的依赖。

**关键设计**：论文中，奖励函数的设计是关键。可验证奖励是指根据一些明确的规则或标准来判断LLM的分类结果是否正确，并给出相应的奖励。LLM作为评判框架是指使用另一个LLM来评估LLM的分类结果，并给出奖励信号。此外，论文还探索了不同的RL算法，如PPO等，以及不同的训练参数设置，以优化模型的性能。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20061v1/img/reward_hacking.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20061v1/img/instruction_halu.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20061v1/img/factuality_halu.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，RL方法在内容审核任务上表现出良好的扩展性，性能随着训练数据、rollout和优化步骤的增加而平稳提高。与监督微调相比，RL方法在需要复杂策略推理的任务上显著提高了性能，同时实现了高达100倍的数据效率。这表明RL方法在数据稀缺或标注成本高昂的场景下具有显著优势。

## 🎯 应用场景

该研究成果可应用于各种在线平台的内容审核系统，例如社交媒体、论坛、电商平台等。通过使用强化学习训练的LLM，可以自动识别和过滤违反政策的内容，减少人工审核的工作量，提高审核效率和准确性，从而维护健康的在线环境。

## 📄 摘要（原文）

> Content moderation at scale remains one of the most pressing challenges in today's digital ecosystem, where billions of user- and AI-generated artifacts must be continuously evaluated for policy violations. Although recent advances in large language models (LLMs) have demonstrated strong potential for policy-grounded moderation, the practical challenges of training these systems to achieve expert-level accuracy in real-world settings remain largely unexplored, particularly in regimes characterized by label sparsity, evolving policy definitions, and the need for nuanced reasoning beyond shallow pattern matching. In this work, we present a comprehensive empirical investigation of scaling reinforcement learning (RL) for content classification, systematically evaluating multiple RL training recipes and reward-shaping strategies-including verifiable rewards and LLM-as-judge frameworks-to transform general-purpose language models into specialized, policy-aligned classifiers across three real-world content moderation tasks. Our findings provide actionable insights for industrial-scale moderation systems, demonstrating that RL exhibits sigmoid-like scaling behavior in which performance improves smoothly with increased training data, rollouts, and optimization steps before gradually saturating. Moreover, we show that RL substantially improves performance on tasks requiring complex policy-grounded reasoning while achieving up to 100x higher data efficiency than supervised fine-tuning, making it particularly effective in domains where expert annotations are scarce or costly.

