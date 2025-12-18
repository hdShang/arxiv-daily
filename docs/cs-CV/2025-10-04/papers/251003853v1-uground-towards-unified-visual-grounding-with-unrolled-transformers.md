---
layout: default
title: UGround: Towards Unified Visual Grounding with Unrolled Transformers
---

# UGround: Towards Unified Visual Grounding with Unrolled Transformers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.03853" class="toolbar-btn" target="_blank">📄 arXiv: 2510.03853v1</a>
  <a href="https://arxiv.org/pdf/2510.03853.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.03853v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.03853v1', 'UGround: Towards Unified Visual Grounding with Unrolled Transformers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rui Qian, Xin Yin, Chuanhang Deng, Zhiyuan Peng, Jian Xiong, Wei Zhai, Dejing Dou

**分类**: cs.CV

**发布日期**: 2025-10-04

**备注**: https://github.com/rui-qian/UGround

**🔗 代码/项目**: [GITHUB](https://github.com/rui-qian/UGround)

---

## 💡 一句话要点

**UGround：提出基于解缠Transformer的统一视觉定位框架，解决误差累积和缺乏空间信息问题。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉定位` `解缠Transformer` `掩码提示` `随机跳跃连接` `强化学习` `语义分割` `多目标定位`

## 📋 核心要点

1. 现有视觉定位方法依赖固定Transformer最后一层，易累积误差且缺乏中间修正。
2. UGround通过随机跳跃连接动态选择Transformer中间层，并使用掩码作为提示，提供空间线索。
3. 实验表明，UGround在多种视觉定位任务上表现出色，包括推理分割和多目标定位。

## 📝 摘要（中文）

本文提出了一种统一的视觉定位范式UGround，它动态地选择解缠Transformer的中间层作为“mask as prompt”，从而区别于利用固定最后一层隐藏层作为“<SEG> as prompt”的现有主流方法。UGround解决了现有范式面临的两个主要挑战：(1) 依赖于固定的最后一层隐藏层，这会顺序放大逐层传播中产生的累积误差，而没有中间校正；(2) 使用<SEG>作为提示，这在没有明确空间线索（例如，坐标）的情况下，隐式地将文本嵌入投影到视觉空间中。UGround的核心是策略提示掩码（Policy-Prompted Masking），它包含两个关键组件：随机跳跃连接（SSC）和掩码作为提示（MasP）。SSC是一种强化学习策略，通过随机抽样，允许每个<SEG> token在解缠Transformer层中滑动，从而实现动态层选择，在该层中，它以跳跃连接的方式连接到视觉模型（例如，SAM）。给定选择的隐藏层，MasP使用从<SEG> token和图像token导出的相似性图作为软logit掩码来提示SAM生成掩码，通过其激活区域提供明确的空间线索。为了验证UGround的有效性，我们首次从属性的角度在一个框架内统一了视觉定位，涵盖了从传统的指代表达式分割到新提出的推理分割，从单目标到多目标，从正向查询到错误前提（空目标）。所有代码和模型都已公开。

## 🔬 方法详解

**问题定义**：现有视觉定位方法通常使用Transformer的最后一层隐藏层作为视觉特征，并将文本嵌入直接投影到视觉空间中。这种方法存在两个主要问题：一是依赖于最后一层，导致逐层传播的误差累积放大；二是缺乏明确的空间信息，难以准确定位目标。

**核心思路**：UGround的核心思路是动态选择Transformer的中间层作为视觉特征，并利用掩码作为提示，为视觉模型提供明确的空间线索。通过这种方式，可以减少误差累积，并提高定位的准确性。

**技术框架**：UGround的整体框架包括一个解缠Transformer和一个视觉模型（如SAM）。解缠Transformer用于提取图像的视觉特征，并生成<SEG> token的嵌入。然后，通过随机跳跃连接（SSC）策略，动态选择Transformer的中间层，并将该层的特征与<SEG> token的嵌入结合。最后，使用掩码作为提示（MasP），引导视觉模型生成目标的掩码。

**关键创新**：UGround的关键创新在于：(1) 动态选择Transformer的中间层，减少误差累积；(2) 使用掩码作为提示，提供明确的空间线索；(3) 提出随机跳跃连接（SSC）策略，实现动态层选择。与现有方法相比，UGround能够更准确地定位目标，并具有更强的鲁棒性。

**关键设计**：随机跳跃连接（SSC）策略使用强化学习来训练一个策略网络，该网络根据当前层的特征和<SEG> token的嵌入，决定是否跳过该层。掩码作为提示（MasP）使用<SEG> token和图像token之间的相似性图作为软logit掩码，引导视觉模型生成目标的掩码。损失函数包括分割损失和强化学习奖励。

## 📊 实验亮点

UGround在多个视觉定位任务上取得了显著的性能提升。例如，在推理分割任务上，UGround的性能超过了现有方法，证明了其在复杂场景下的定位能力。此外，UGround在多目标定位任务上也表现出色，能够同时定位多个目标，并生成准确的掩码。

## 🎯 应用场景

UGround具有广泛的应用前景，包括图像编辑、视频理解、机器人导航、自动驾驶等领域。例如，在图像编辑中，可以使用UGround准确定位目标，并进行精确的编辑操作。在机器人导航中，可以使用UGround识别和定位环境中的物体，从而实现自主导航。该研究的实际价值在于提高了视觉定位的准确性和鲁棒性，未来可能推动相关领域的发展。

## 📄 摘要（原文）

> We present UGround, a \textbf{U}nified visual \textbf{Ground}ing paradigm that dynamically selects intermediate layers across \textbf{U}nrolled transformers as ``mask as prompt'', diverging from the prevailing pipeline that leverages the fixed last hidden layer as ``\texttt{<SEG>} as prompt''. UGround addresses two primary challenges posed by the prevailing paradigm: (1) its reliance on the fixed last hidden layer, which sequentially amplifies cumulative errors arising from layer-by-layer propagation without intermediate correction, and (2) its use of \texttt{<SEG>} as a prompt, which implicitly projects textual embeddings into visual space without explicit spatial cues (\eg, coordinates). Central to UGround is Policy-Prompted Masking, which comprises two key components: Stochastic Skip Connection (SSC) and Mask as Prompt (MasP). SSC is a reinforcement learning policy that, via stochastic sampling, allows each \texttt{<SEG>} token to slide across unrolled transformer layers, enabling dynamic layer selection at which it connects to the vision model (\eg, SAM) in a skip-connection fashion. Given the selected hidden layer, MasP uses the similarity map derived from the \texttt{<SEG>} token and image tokens as a soft logit mask to prompt SAM for mask generation, offering explicit spatial cues through its activation regions. To validate the effectiveness of UGround, we, for the first time, have unified visual grounding within a single framework from an attribute perspective, spanning from traditional refer expression segmentation to newly proposed reasoning segmentation, single-target to multi-target, positive query to false premise (empty target). All codes and models are publicly available at \href{https://github.com/rui-qian/UGround}{https://github.com/rui-qian/UGround}.

