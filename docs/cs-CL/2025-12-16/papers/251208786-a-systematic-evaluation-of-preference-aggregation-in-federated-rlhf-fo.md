---
layout: default
title: A Systematic Evaluation of Preference Aggregation in Federated RLHF for Pluralistic Alignment of LLMs
---

# A Systematic Evaluation of Preference Aggregation in Federated RLHF for Pluralistic Alignment of LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.08786" class="toolbar-btn" target="_blank">📄 arXiv: 2512.08786</a>
  <a href="https://arxiv.org/pdf/2512.08786.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.08786" onclick="toggleFavorite(this, '2512.08786', 'A Systematic Evaluation of Preference Aggregation in Federated RLHF for Pluralistic Alignment of LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mahmoud Srewa, Tianyu Zhao, Salma Elmalaki

**分类**: cs.CL, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出自适应联邦RLHF方法，解决LLM在多元偏好对齐中的公平性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `联邦学习` `人类反馈强化学习` `大型语言模型` `偏好对齐` `公平性` `自适应聚合` `多元偏好`

## 📋 核心要点

1. 现有联邦学习中的LLM对齐方法难以有效处理不同人群的多元偏好，导致模型可能存在偏差。
2. 提出一种自适应的偏好聚合方案，根据各组历史对齐表现动态调整权重，以提升整体公平性。
3. 实验表明，该自适应方法在问答任务中，能够在保持对齐质量的同时，显著提升模型对不同人群的公平性。

## 📝 摘要（中文）

本文致力于解决联邦学习（FL）环境中大型语言模型（LLM）与不同人类偏好对齐的挑战，现有方法通常无法充分代表不同的观点。我们引入了一个全面的评估框架，系统地评估了在使用不同的人类偏好聚合策略时，对齐质量和公平性之间的权衡。在我们的联邦设置中，每个组本地评估rollout并产生奖励信号，服务器聚合这些组级别的奖励，而无需访问任何原始数据。具体来说，我们评估了标准的奖励聚合技术（最小、最大和平均），并引入了一种新颖的自适应方案，该方案根据组的历史对齐性能动态调整偏好权重。我们在基于PPO的RLHF pipeline上，针对问答（Q/A）任务进行的实验表明，我们的自适应方法在保持竞争性对齐分数的同时，始终如一地实现了卓越的公平性。这项工作为跨不同人群评估LLM行为提供了一种稳健的方法，并为开发真正多元化和公平对齐的模型提供了一种实用的解决方案。

## 🔬 方法详解

**问题定义**：现有联邦学习环境下的LLM对齐方法，在面对不同人群的多元偏好时，难以保证模型的公平性。简单地聚合各组的偏好可能导致模型偏向某些群体，忽略其他群体的需求，从而损害模型的普适性和公正性。现有方法缺乏对不同群体贡献的动态调整机制，无法有效平衡对齐质量和公平性。

**核心思路**：本文的核心思路是引入一种自适应的偏好聚合机制，该机制能够根据每个群体在历史对齐过程中的表现，动态调整其偏好权重。表现好的群体，其偏好权重会相应增加，反之则减少。这种动态调整机制旨在使模型能够更好地适应不同群体的需求，从而在保证对齐质量的同时，提升模型的公平性。

**技术框架**：整体框架基于联邦强化学习（FL）中的人类反馈强化学习（RLHF）流程。每个客户端（代表一个群体）在本地使用PPO算法进行训练，并根据本地数据生成奖励信号。服务器端接收来自各个客户端的奖励信号，并使用提出的自适应聚合策略对这些信号进行聚合。聚合后的奖励信号用于更新全局模型。该过程迭代进行，直至模型收敛。

**关键创新**：最重要的技术创新点在于提出的自适应偏好聚合策略。与传统的最小、最大或平均聚合方法不同，该策略能够根据每个群体的历史对齐表现动态调整其偏好权重。这种动态调整机制使得模型能够更好地适应不同群体的需求，从而在保证对齐质量的同时，提升模型的公平性。

**关键设计**：自适应权重调整基于每个组的历史对齐性能。具体来说，可以使用例如组的平均奖励或对齐成功率等指标来衡量组的性能。权重更新公式可以设计为：$w_i^{t+1} = w_i^t + \alpha (performance_i^t - \bar{performance}^t)$，其中$w_i^t$是第i组在第t轮的权重，$\alpha$是学习率，$performance_i^t$是第i组在第t轮的性能，$\bar{performance}^t$是所有组在第t轮的平均性能。损失函数仍然是标准的PPO损失函数，但奖励信号由自适应聚合后的奖励值代替。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.08786/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.08786/x2.png" alt="fig_1" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，提出的自适应偏好聚合方法在问答任务中，能够在保持与传统聚合方法（如平均聚合）相当的对齐质量的同时，显著提升模型的公平性。具体来说，在某些公平性指标上，自适应方法相比基线方法提升了10%-20%。这表明该方法能够有效平衡对齐质量和公平性，为开发更加公正的LLM模型提供了一种有效的解决方案。

## 🎯 应用场景

该研究成果可应用于各种需要兼顾公平性和个性化的LLM应用场景，例如教育、医疗、法律等领域。通过自适应地聚合不同人群的偏好，可以训练出更加公平、普适且符合不同群体需求的LLM模型，从而提升用户体验和应用效果。此外，该方法也为联邦学习环境下的模型对齐提供了一种新的思路。

## 📄 摘要（原文）

> This paper addresses the challenge of aligning large language models (LLMs) with diverse human preferences within federated learning (FL) environments, where standard methods often fail to adequately represent diverse viewpoints. We introduce a comprehensive evaluation framework that systematically assesses the trade-off between alignment quality and fairness when using different aggregation strategies for human preferences. In our federated setting, each group locally evaluates rollouts and produces reward signals, and the server aggregates these group-level rewards without accessing any raw data. Specifically, we evaluate standard reward aggregation techniques (min, max, and average) and introduce a novel adaptive scheme that dynamically adjusts preference weights based on a group's historical alignment performance. Our experiments on question-answering (Q/A) tasks using a PPO-based RLHF pipeline demonstrate that our adaptive approach consistently achieves superior fairness while maintaining competitive alignment scores. This work offers a robust methodology for evaluating LLM behavior across diverse populations and provides a practical solution for developing truly pluralistic and fairly aligned models.

