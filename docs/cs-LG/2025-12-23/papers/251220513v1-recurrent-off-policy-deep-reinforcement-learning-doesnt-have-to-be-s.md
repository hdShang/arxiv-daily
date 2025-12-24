---
layout: default
title: Recurrent Off-Policy Deep Reinforcement Learning Doesn't Have to be Slow
---

# Recurrent Off-Policy Deep Reinforcement Learning Doesn't Have to be Slow

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20513" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20513v1</a>
  <a href="https://arxiv.org/pdf/2512.20513.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20513v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20513v1', 'Recurrent Off-Policy Deep Reinforcement Learning Doesn\'t Have to be Slow')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tyler Clark, Christine Evers, Jonathon Hare

**分类**: cs.LG

**发布日期**: 2025-12-23

---

## 💡 一句话要点

**提出RISE，通过简化编码提升图像Off-Policy强化学习中循环网络的效率**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `循环神经网络` `深度强化学习` `Off-Policy学习` `图像编码` `计算效率`

## 📋 核心要点

1. 循环Off-Policy深度强化学习计算量大，限制了其应用。
2. RISE通过可学习和非学习编码器，降低循环网络的计算负担。
3. RISE集成到现有算法后，Atari基准测试中IQM性能提升35.6%。

## 📝 摘要（中文）

循环Off-Policy深度强化学习模型虽然能达到顶尖性能，但由于其高昂的计算需求而常常被搁置。为了解决这个问题，我们引入了RISE（Recurrent Integration via Simplified Encodings），这是一种新颖的方法，它可以通过使用可学习和不可学习的编码器层，在任何基于图像的Off-Policy强化学习设置中利用循环网络，而不会产生显著的计算开销。当将RISE集成到领先的非循环Off-Policy强化学习算法中时，我们观察到在Atari基准测试中，人类归一化的四分位间距平均值（IQM）性能提高了35.6%。我们分析了各种实现策略，以突出我们提出的框架的多功能性和潜力。

## 🔬 方法详解

**问题定义**：论文旨在解决循环Off-Policy深度强化学习模型计算复杂度高的问题。现有的循环模型虽然性能优异，但其计算需求使得它们在实际应用中受到限制，尤其是在资源受限的环境下。因此，如何在保证性能的同时降低计算成本是本研究要解决的核心问题。

**核心思路**：RISE的核心思路是通过简化编码过程来降低循环网络的计算负担。具体来说，RISE利用可学习和不可学习的编码器层，将原始图像数据转换为更紧凑、更易于处理的表示形式。这种简化的表示形式可以减少循环网络的输入维度，从而降低计算复杂度。同时，通过结合可学习和不可学习的编码器，RISE能够在保证信息完整性的前提下，进一步优化编码效率。

**技术框架**：RISE框架主要包含以下几个模块：1) 图像输入模块：接收原始图像数据作为输入。2) 编码器模块：包含可学习和不可学习的编码器层，用于将原始图像数据转换为简化表示。3) 循环网络模块：接收编码器模块的输出，利用循环神经网络对时间序列信息进行建模。4) 策略/价值函数模块：根据循环网络的输出，预测策略或价值函数。整个框架可以与现有的Off-Policy强化学习算法相结合，实现高效的循环Off-Policy深度强化学习。

**关键创新**：RISE的关键创新在于其简化的编码方式。与传统的直接将原始图像输入循环网络的方法不同，RISE通过编码器层提取图像的关键特征，并将其转换为更紧凑的表示形式。这种简化编码不仅降低了计算复杂度，还有助于循环网络更好地捕捉时间序列信息。此外，RISE结合了可学习和不可学习的编码器，进一步提高了编码效率和信息完整性。

**关键设计**：RISE的关键设计包括：1) 编码器结构：可以选择不同的编码器结构，如卷积神经网络、线性层等。可学习编码器通过反向传播进行优化，不可学习编码器则采用预定义的变换，如随机投影。2) 编码维度：需要根据具体任务和计算资源选择合适的编码维度，以平衡性能和计算复杂度。3) 损失函数：RISE可以与现有的Off-Policy强化学习算法的损失函数相结合，共同优化整个模型。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20513v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20513v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20513v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，将RISE集成到领先的非循环Off-Policy强化学习算法中，可以在Atari基准测试中实现显著的性能提升。具体来说，人类归一化的四分位间距平均值（IQM）性能提高了35.6%。这一结果表明，RISE能够有效地降低循环网络的计算负担，并在保证性能的同时提高强化学习算法的效率。

## 🎯 应用场景

RISE具有广泛的应用前景，尤其是在需要处理高维图像数据的强化学习任务中。例如，它可以应用于机器人控制、自动驾驶、游戏AI等领域。通过降低循环网络的计算负担，RISE使得循环Off-Policy深度强化学习模型能够在资源受限的环境下部署，从而推动这些技术在实际场景中的应用。未来，RISE还可以与其他优化技术相结合，进一步提高强化学习算法的效率和性能。

## 📄 摘要（原文）

> Recurrent off-policy deep reinforcement learning models achieve state-of-the-art performance but are often sidelined due to their high computational demands. In response, we introduce RISE (Recurrent Integration via Simplified Encodings), a novel approach that can leverage recurrent networks in any image-based off-policy RL setting without significant computational overheads via using both learnable and non-learnable encoder layers. When integrating RISE into leading non-recurrent off-policy RL algorithms, we observe a 35.6% human-normalized interquartile mean (IQM) performance improvement across the Atari benchmark. We analyze various implementation strategies to highlight the versatility and potential of our proposed framework.

