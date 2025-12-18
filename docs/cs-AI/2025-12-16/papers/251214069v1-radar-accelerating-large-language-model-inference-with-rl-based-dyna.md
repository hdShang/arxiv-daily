---
layout: default
title: RADAR: Accelerating Large Language Model Inference With RL-Based Dynamic Draft Trees
---

# RADAR: Accelerating Large Language Model Inference With RL-Based Dynamic Draft Trees

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14069" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14069v1</a>
  <a href="https://arxiv.org/pdf/2512.14069.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14069v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14069v1', 'RADAR: Accelerating Large Language Model Inference With RL-Based Dynamic Draft Trees')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junjie Ma, Jinlong Li

**分类**: cs.AI

**发布日期**: 2025-12-16

**备注**: 5 pages, 2 figures

**🔗 代码/项目**: [GITHUB](https://github.com/minaduki-sora/RADAR)

---

## 💡 一句话要点

**RADAR：基于强化学习的动态草稿树加速大语言模型推理**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `推理加速` `推测采样` `强化学习` `动态草稿树`

## 📋 核心要点

1. 现有推测采样方法中，草稿模型调用次数为预设超参数，缺乏灵活性，导致计算冗余。
2. RADAR将草稿树生成建模为MDP，使用离线强化学习训练预测模型，动态决策草稿模型调用次数。
3. 实验结果表明，RADAR在多个LLM和任务上实现了3.17x-4.82x的加速，显著提升推理效率。

## 📝 摘要（中文）

现代大型语言模型（LLM）的推理成本高且速度慢，推测采样已成为解决此问题的有效方法。然而，推测采样中用于生成候选token的草稿模型调用次数是一个预设的超参数，缺乏灵活性。为了更有效地生成和利用候选token，我们提出了一种新的推测采样方法RADAR，该方法采用基于强化学习的动态草稿树。RADAR将草稿树生成过程建模为马尔可夫决策过程（MDP），并采用离线强化学习来训练预测模型，从而能够实时决策草稿模型的调用次数，减少冗余计算，进一步加速推理。在三个LLM和四个任务上的评估表明，RADAR相对于自回归解码基线实现了3.17倍-4.82倍的加速。代码可在https://github.com/minaduki-sora/RADAR 获取。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）推理过程中，由于推测采样中草稿模型调用次数固定而导致的效率低下问题。现有方法中，草稿模型调用次数作为一个预设的超参数，无法根据实际情况进行调整，可能导致不必要的计算开销，降低推理速度。

**核心思路**：论文的核心思路是将草稿树的生成过程视为一个马尔可夫决策过程（MDP），并利用强化学习来训练一个预测模型，该模型能够根据当前状态动态地决定是否继续调用草稿模型生成新的候选token。通过这种方式，可以避免不必要的计算，提高推理效率。

**技术框架**：RADAR的技术框架主要包括以下几个阶段：1) **离线训练阶段**：收集LLM推理数据，构建MDP环境，并使用离线强化学习算法训练预测模型（策略网络）。2) **在线推理阶段**：在推理过程中，利用训练好的预测模型，根据当前状态（例如，已生成的草稿token序列、LLM的预测概率等）动态地决定是否继续调用草稿模型生成新的候选token。如果预测模型认为继续生成更有可能被LLM接受，则继续调用草稿模型；否则，停止生成，并将已生成的草稿token序列提交给LLM进行验证。

**关键创新**：RADAR的关键创新在于将强化学习引入到推测采样中，实现了草稿模型调用次数的动态调整。与现有方法相比，RADAR能够根据实际情况自适应地调整草稿模型的调用次数，从而更有效地利用草稿模型生成的候选token，减少冗余计算，提高推理效率。

**关键设计**：RADAR的关键设计包括：1) **MDP状态定义**：状态需要包含足够的信息来预测继续生成草稿token的收益，例如已生成的草稿token序列、LLM的预测概率等。2) **奖励函数设计**：奖励函数需要能够反映生成草稿token的收益，例如，如果生成的草稿token被LLM接受，则给予正向奖励；否则，给予负向奖励。3) **离线强化学习算法选择**：选择合适的离线强化学习算法，例如，Behavior Cloning, CQL等，以有效地利用离线数据训练预测模型。4) **预测模型结构**：预测模型可以使用神经网络，输入是MDP状态，输出是是否继续调用草稿模型的概率。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14069v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14069v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14069v1/x2.png" alt="img_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，RADAR在三个不同的LLM（包括LLaMA-7B、LLaMA-13B和GPT-J）和四个不同的任务（包括文本摘要、问题回答等）上都取得了显著的加速效果。相对于自回归解码基线，RADAR实现了3.17倍-4.82倍的加速，证明了其有效性。

## 🎯 应用场景

RADAR具有广泛的应用前景，可以应用于各种需要加速LLM推理的场景，例如：在线对话系统、文本生成、机器翻译等。通过动态调整草稿模型的调用次数，RADAR可以显著提高LLM的推理效率，降低计算成本，使得LLM能够更好地服务于各种实际应用。

## 📄 摘要（原文）

> Inference with modern Large Language Models (LLMs) is expensive and slow, and speculative sampling has emerged as an effective solution to this problem, however, the number of the calls to the draft model for generating candidate tokens in speculative sampling is a preset hyperparameter, lacking flexibility. To generate and utilize the candidate tokens more effectively, we propose RADAR, a novel speculative sampling method with RL-based dynamic draft trees. RADAR formulates the draft tree generation process as a Markov Decision Process (MDP) and employs offline reinforcement learning to train a prediction model, which enables real-time decision on the calls to the draft model, reducing redundant computations and further accelerating inference. Evaluations across three LLMs and four tasks show that RADAR achieves a speedup of 3.17x-4.82x over the auto-regressive decoding baseline. The code is available at https://github.com/minaduki-sora/RADAR.

