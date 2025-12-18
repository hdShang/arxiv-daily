---
layout: default
title: Beyond Majority Voting: Towards Fine-grained and More Reliable Reward Signal for Test-Time Reinforcement Learning
---

# Beyond Majority Voting: Towards Fine-grained and More Reliable Reward Signal for Test-Time Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15146" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15146v1</a>
  <a href="https://arxiv.org/pdf/2512.15146.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15146v1" onclick="toggleFavorite(this, '2512.15146v1', 'Beyond Majority Voting: Towards Fine-grained and More Reliable Reward Signal for Test-Time Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weiqin Wang, Yile Wang, Kehao Chen, Hui Huang

**分类**: cs.CL

**发布日期**: 2025-12-17

**🔗 代码/项目**: [GITHUB](https://github.com/szu-tera/SCOPE)

---

## 💡 一句话要点

**提出SCOPE框架，通过细粒度置信度加权伪标签提升测试时强化学习性能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `测试时强化学习` `伪标签` `置信度加权` `动态子群划分` `大型语言模型`

## 📋 核心要点

1. 现有测试时强化学习依赖多数投票产生伪标签，易受确认偏差和奖励稀疏性影响，限制了性能。
2. SCOPE框架通过整合模型置信度和动态子群划分，生成更可靠的细粒度伪标签，鼓励更广泛的探索。
3. 实验结果表明，SCOPE在多个基准测试中显著优于现有方法，证明了其有效性。

## 📝 摘要（中文）

本文提出了一种名为子群特定步进式置信度加权伪标签估计(SCOPE)的框架，旨在解决测试时强化学习中多数投票策略引起的确认偏差和稀疏奖励问题。该框架集成了模型置信度和动态子群划分，利用步进式置信度进行伪标签推导，优先考虑高质量的推理路径。同时，通过平衡推理质量和探索多样性，将候选输出池动态划分为独立的子群，并通过重复采样为每个子群推导出局部共识，从而提供多样化的监督目标，鼓励更广泛的探索。实验结果表明，SCOPE在各种模型和基准测试中均优于现有方法，在AIME 2025和AMC上分别实现了13.1%和8.1%的相对改进。

## 🔬 方法详解

**问题定义**：现有测试时强化学习方法，特别是那些依赖多数投票结果作为伪标签的方法，存在确认偏差和奖励稀疏的问题。确认偏差指的是模型倾向于强化已有的错误认知，而奖励稀疏则使得模型难以有效学习，尤其是在复杂的推理任务中。这些问题限制了大型语言模型(LLMs)的推理能力。

**核心思路**：SCOPE的核心思路是通过更细粒度的置信度加权伪标签估计来解决上述问题。它不简单地依赖多数投票，而是考虑每个推理步骤的置信度，并动态地将候选输出划分为多个子群，在每个子群内寻找局部共识。这样做的目的是减少确认偏差，并提供更多样化的监督信号，从而鼓励更广泛的探索。

**技术框架**：SCOPE框架主要包含两个核心模块：步进式置信度加权和动态子群划分。首先，框架计算每个推理步骤的置信度，并将其用于伪标签的推导，优先考虑高质量的推理路径。然后，框架动态地将候选输出池划分为多个独立的子群，每个子群代表一种可能的推理路径。最后，通过对每个子群进行重复采样，得到局部共识，作为该子群的监督目标。

**关键创新**：SCOPE的关键创新在于其细粒度的置信度加权和动态子群划分策略。与传统的多数投票方法相比，SCOPE能够更准确地评估每个推理步骤的质量，并根据置信度进行加权。此外，动态子群划分策略能够有效地平衡推理质量和探索多样性，从而避免陷入局部最优。

**关键设计**：在步进式置信度加权方面，论文可能使用了某种形式的置信度评分函数，例如softmax概率或logits的某种变换。在动态子群划分方面，论文可能使用了某种聚类算法或基于相似度的划分策略，以确保每个子群内的输出具有一定的相似性。具体的损失函数可能包括交叉熵损失或类似的度量，用于衡量模型输出与伪标签之间的差异。论文开源的代码可以提供更详细的参数设置和网络结构信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15146v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15146v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15146v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

SCOPE在AIME 2025和AMC等具有挑战性的基准测试中取得了显著的性能提升。具体而言，SCOPE在AIME 2025上实现了13.1%的相对改进，在AMC上实现了8.1%的相对改进。这些结果表明，SCOPE能够有效地解决测试时强化学习中的确认偏差和奖励稀疏问题，并显著提高模型的推理能力。

## 🎯 应用场景

SCOPE框架可应用于各种需要测试时强化学习的场景，例如自然语言处理中的问答系统、对话生成、代码生成等。通过提高模型的推理能力和鲁棒性，SCOPE可以提升这些应用在实际场景中的性能和用户体验。此外，该方法也可以推广到其他领域，例如机器人控制和游戏AI。

## 📄 摘要（原文）

> Test-time reinforcement learning mitigates the reliance on annotated data by using majority voting results as pseudo-labels, emerging as a complementary direction to reinforcement learning with verifiable rewards (RLVR) for improving reasoning ability of large language models (LLMs). However, this voting strategy often induces confirmation bias and suffers from sparse rewards, limiting the overall performance. In this work, we propose subgroup-specific step-wise confidence-weighted pseudo-label estimation (SCOPE), a framework integrating model confidence and dynamic subgroup partitioning to address these issues. Specifically, SCOPE integrates the proposed step-wise confidence into pseudo label deduction, prioritizing high-quality reasoning paths over simple frequency count. Furthermore, it dynamically partitions the candidate outputs pool into independent subgroups by balancing reasoning quality against exploration diversity. By deriving local consensus via repeat sampling for each sub group, SCOPE provides diverse supervision targets to encourage broader exploration. We conduct experiments across various models and benchmarks, experimental results show that SCOPE consistently outperforms recent baselines. Notably, SCOPE achieving relative improvements of 13.1\% on challenging AIME 2025 and 8.1\% on AMC. The code is released at \href{https://github.com/szu-tera/SCOPE}{https://github.com/szu-tera/SCOPE}.

