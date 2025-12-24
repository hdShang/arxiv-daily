---
layout: default
title: Emergent temporal abstractions in autoregressive models enable hierarchical reinforcement learning
---

# Emergent temporal abstractions in autoregressive models enable hierarchical reinforcement learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20605" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20605v1</a>
  <a href="https://arxiv.org/pdf/2512.20605.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20605v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20605v1', 'Emergent temporal abstractions in autoregressive models enable hierarchical reinforcement learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Seijin Kobayashi, Yanick Schimpf, Maximilian Schlegel, Angelika Steger, Maciej Wolczyk, Johannes von Oswald, Nino Scherre, Kaitlin Maile, Guillaume Lajoie, Blake A. Richards, Rif A. Saurous, James Manyika, Blaise Agüera y Arcas, Alexander Meulemans, João Sacramento

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-23

---

## 💡 一句话要点

**提出内部强化学习，利用自回归模型中的时间抽象实现分层强化学习**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自回归模型` `强化学习` `分层强化学习` `时间抽象` `内部强化学习`

## 📋 核心要点

1. 传统强化学习在自回归模型中逐token采样动作效率低，尤其在奖励稀疏时面临挑战。
2. 提出内部强化学习，在高阶模型中学习时间抽象动作，控制底层自回归模型的激活。
3. 实验表明，该方法能有效压缩长序列动作，从稀疏奖励中学习，优于标准强化学习。

## 📝 摘要（中文）

本文提出了一种在自回归模型内部表示中进行动作和探索的方法，以克服传统强化学习中token-by-token采样导致的学习效率低下的问题，尤其是在奖励稀疏的情况下。该方法引入了一个高阶非因果序列模型，其输出控制基础自回归模型的残差流激活，从而发现时间抽象动作。实验表明，该高阶模型能够将长激活序列块压缩到内部控制器上，每个控制器执行一系列行为上有意义的动作，这些动作在长时间尺度上展开，并伴随一个学习到的终止条件。通过直接内部控制器强化，即“内部强化学习”，可以在标准强化学习微调失败的情况下从稀疏奖励中学习。该研究表明了在自回归模型中进行潜在动作生成和强化的优势，并认为内部强化学习是实现基础模型中分层强化学习的一种有前景的途径。

## 🔬 方法详解

**问题定义**：现有的大规模自回归模型在强化学习微调时，通常采用逐token生成动作的方式进行探索。这种方式在奖励稀疏的环境下效率极低，因为模型需要花费大量时间才能探索到有意义的动作序列。因此，如何提高自回归模型在强化学习中的探索效率，尤其是在奖励稀疏的环境下，是本文要解决的核心问题。

**核心思路**：本文的核心思路是在自回归模型的内部表示中进行动作和探索，而不是直接在输出空间中逐token生成动作。具体来说，通过引入一个高阶非因果序列模型，该模型学习控制底层自回归模型的残差流激活，从而实现对时间抽象动作的建模。这样，高阶模型可以一次性生成一个动作序列，而不是逐token生成，从而提高了探索效率。

**技术框架**：整体框架包含两个主要部分：一个基础的自回归模型和一个高阶非因果序列模型。基础自回归模型负责生成底层的动作序列，而高阶模型则负责生成控制信号，这些控制信号作用于基础模型的残差流激活，从而影响基础模型的行为。在高阶模型训练过程中，采用强化学习算法，直接对高阶模型的控制器进行强化，使其能够生成更有利于任务完成的控制信号。

**关键创新**：最重要的创新点在于提出了“内部强化学习”的概念，即直接在自回归模型的内部表示中进行强化学习。与传统的强化学习方法不同，内部强化学习不需要直接对输出空间中的动作进行强化，而是通过对内部控制器的强化，间接地影响模型的行为。这种方法能够更好地利用自回归模型的内部表示，从而提高学习效率。

**关键设计**：高阶模型采用非因果序列模型，允许模型在生成控制信号时考虑未来的信息。高阶模型的损失函数包括两部分：一部分是标准的强化学习损失，用于优化控制器的行为；另一部分是正则化损失，用于约束控制器的输出，使其更加平滑和可解释。此外，高阶模型还学习一个终止条件，用于判断何时停止当前控制器的执行，从而实现对动作序列的分割。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20605v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20605v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20605v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，在网格世界和MuJoCo任务中，该方法能够有效地学习时间抽象动作，并在稀疏奖励环境下取得显著的性能提升。与标准的强化学习微调方法相比，内部强化学习能够更快地学习到有效的策略，并在某些任务中取得更高的奖励。

## 🎯 应用场景

该研究成果可应用于机器人控制、游戏AI等领域，尤其是在需要长时间规划和稀疏奖励的环境下。通过学习时间抽象动作，可以显著提高智能体的学习效率和泛化能力，使其能够更好地适应复杂多变的环境。未来，该方法有望应用于更广泛的领域，例如自然语言处理和计算机视觉。

## 📄 摘要（原文）

> Large-scale autoregressive models pretrained on next-token prediction and finetuned with reinforcement learning (RL) have achieved unprecedented success on many problem domains. During RL, these models explore by generating new outputs, one token at a time. However, sampling actions token-by-token can result in highly inefficient learning, particularly when rewards are sparse. Here, we show that it is possible to overcome this problem by acting and exploring within the internal representations of an autoregressive model. Specifically, to discover temporally-abstract actions, we introduce a higher-order, non-causal sequence model whose outputs control the residual stream activations of a base autoregressive model. On grid world and MuJoCo-based tasks with hierarchical structure, we find that the higher-order model learns to compress long activation sequence chunks onto internal controllers. Critically, each controller executes a sequence of behaviorally meaningful actions that unfold over long timescales and are accompanied with a learned termination condition, such that composing multiple controllers over time leads to efficient exploration on novel tasks. We show that direct internal controller reinforcement, a process we term "internal RL", enables learning from sparse rewards in cases where standard RL finetuning fails. Our results demonstrate the benefits of latent action generation and reinforcement in autoregressive models, suggesting internal RL as a promising avenue for realizing hierarchical RL within foundation models.

