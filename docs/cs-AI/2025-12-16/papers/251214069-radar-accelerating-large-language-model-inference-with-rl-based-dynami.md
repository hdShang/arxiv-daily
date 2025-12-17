---
layout: default
title: RADAR: Accelerating Large Language Model Inference With RL-Based Dynamic Draft Trees
---

# RADAR: Accelerating Large Language Model Inference With RL-Based Dynamic Draft Trees

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14069" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14069</a>
  <a href="https://arxiv.org/pdf/2512.14069.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14069" onclick="toggleFavorite(this, '2512.14069', 'RADAR: Accelerating Large Language Model Inference With RL-Based Dynamic Draft Trees')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junjie Ma, Jinlong Li

**分类**: cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出基于强化学习动态草稿树的RADAR，加速大语言模型推理。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `推理加速` `推测采样` `强化学习` `动态草稿树`

## 📋 核心要点

1. 现有推测采样方法中，草稿模型调用次数为预设超参数，缺乏灵活性，导致计算冗余。
2. RADAR将草稿树生成过程建模为MDP，利用离线强化学习训练预测模型，动态决策草稿模型调用次数。
3. 实验结果表明，RADAR在多个LLM和任务上实现了显著的推理加速，最高可达4.82倍。

## 📝 摘要（中文）

现代大型语言模型（LLM）的推理成本高且速度慢，推测采样已成为解决此问题的有效方法。然而，推测采样中用于生成候选token的草稿模型调用次数是一个预设的超参数，缺乏灵活性。为了更有效地生成和利用候选token，我们提出了一种新的推测采样方法RADAR，它采用基于强化学习的动态草稿树。RADAR将草稿树生成过程形式化为一个马尔可夫决策过程（MDP），并采用离线强化学习来训练预测模型，从而能够实时决策草稿模型的调用次数，减少冗余计算，进一步加速推理。在三个LLM和四个任务上的评估表明，RADAR相对于自回归解码基线实现了3.17倍-4.82倍的加速。代码可在该URL获得。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型推理速度慢、成本高的问题。现有的推测采样方法虽然能加速推理，但其草稿模型调用次数是预先设定的超参数，无法根据实际情况动态调整，导致在某些情况下产生不必要的计算冗余，效率不高。

**核心思路**：论文的核心思路是将草稿树的生成过程视为一个马尔可夫决策过程（MDP），并利用强化学习来训练一个策略，该策略能够根据当前状态动态地决定是否继续调用草稿模型生成候选token。通过这种方式，可以避免不必要的草稿模型调用，从而提高推理效率。

**技术框架**：RADAR的整体框架包含以下几个主要模块：1) **状态表示**：定义MDP的状态，包括当前已生成的token序列、草稿模型的置信度等信息。2) **动作空间**：定义MDP的动作，例如“继续调用草稿模型”或“停止调用草稿模型”。3) **奖励函数**：设计奖励函数，鼓励生成准确的候选token，并惩罚不必要的草稿模型调用。4) **强化学习模型**：使用离线强化学习算法训练一个策略模型，该模型根据当前状态输出最优动作。5) **推理过程**：在推理过程中，根据策略模型的输出动态地生成草稿树，并利用目标模型进行验证。

**关键创新**：RADAR的关键创新在于将强化学习引入到推测采样中，实现了草稿模型调用次数的动态调整。与传统的推测采样方法相比，RADAR能够根据实际情况自适应地调整草稿树的深度，从而更有效地利用草稿模型生成的候选token，减少冗余计算。

**关键设计**：论文使用离线强化学习算法来训练策略模型，避免了在线探索带来的高成本。具体来说，作者首先收集大量的草稿树生成数据，然后使用这些数据来训练一个Q函数，该Q函数用于评估不同状态-动作对的价值。在推理过程中，策略模型根据Q函数的输出选择最优动作。奖励函数的设计至关重要，作者设计了一个综合考虑准确性和效率的奖励函数，以平衡生成准确token和减少计算开销之间的关系。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14069/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14069/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14069/x2.png" alt="img_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，RADAR在三个不同的LLM（包括LLaMA-7B、LLaMA-13B和GPT-2）和四个不同的任务上均取得了显著的加速效果。相对于自回归解码基线，RADAR实现了3.17倍到4.82倍的加速。这些结果表明，RADAR能够有效地减少冗余计算，提高推理效率。

## 🎯 应用场景

RADAR具有广泛的应用前景，可用于加速各种基于大型语言模型的应用，例如文本生成、机器翻译、对话系统等。通过提高推理效率，RADAR可以降低部署和运行大型语言模型的成本，使其更容易被广泛应用。此外，RADAR的动态草稿树生成方法也可以应用于其他需要进行序列决策的任务中。

## 📄 摘要（原文）

> Inference with modern Large Language Models (LLMs) is expensive and slow, and speculative sampling has emerged as an effective solution to this problem, however, the number of the calls to the draft model for generating candidate tokens in speculative sampling is a preset hyperparameter, lacking flexibility. To generate and utilize the candidate tokens more effectively, we propose RADAR, a novel speculative sampling method with RL-based dynamic draft trees. RADAR formulates the draft tree generation process as a Markov Decision Process (MDP) and employs offline reinforcement learning to train a prediction model, which enables real-time decision on the calls to the draft model, reducing redundant computations and further accelerating inference. Evaluations across three LLMs and four tasks show that RADAR achieves a speedup of 3.17x-4.82x over the auto-regressive decoding baseline. The code is available atthis https URL.

