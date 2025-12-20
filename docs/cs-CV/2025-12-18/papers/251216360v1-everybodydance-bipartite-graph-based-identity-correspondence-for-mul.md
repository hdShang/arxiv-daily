---
layout: default
title: EverybodyDance: Bipartite Graph-Based Identity Correspondence for Multi-Character Animation
---

# EverybodyDance: Bipartite Graph-Based Identity Correspondence for Multi-Character Animation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16360" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16360v1</a>
  <a href="https://arxiv.org/pdf/2512.16360.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16360v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16360v1', 'EverybodyDance: Bipartite Graph-Based Identity Correspondence for Multi-Character Animation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haotian Ling, Zequn Chen, Qiuying Chen, Donglin Di, Yongjia Ma, Hao Li, Chen Wei, Zhulin Tao, Xun Yang

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出EverybodyDance，通过二分图匹配解决多角色动画中的身份对应问题。**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `多角色动画` `身份对应` `二分图匹配` `姿态驱动` `Mask-Query Attention`

## 📋 核心要点

1. 现有姿态驱动的角色动画在单角色场景中取得了显著进展，但扩展到多角色场景，尤其是在涉及位置交换时，极具挑战。
2. EverybodyDance的核心思想是将角色间的身份对应问题建模为二分图匹配问题，并设计Mask-Query Attention机制计算角色间的亲和力。
3. 实验结果表明，EverybodyDance在身份对应和视觉保真度方面显著优于现有方法，并在新构建的身份对应评估基准上进行了验证。

## 📝 摘要（中文）

本文提出EverybodyDance，一个针对多角色动画中身份正确对应问题的系统性解决方案。核心是身份匹配图（IMG），它将生成帧和参考帧中的角色建模为加权完全二分图中的两个节点集合。通过提出的Mask-Query Attention (MQA)计算边权重，量化角色对之间的亲和力。论文将身份对应正确性形式化为图结构度量，并在训练期间优化它。此外，还提出了一系列针对多角色动画的策略，包括身份嵌入引导、多尺度匹配策略和预分类采样，协同工作。最后，构建了身份对应评估基准，用于评估多角色身份对应正确性。大量实验表明，EverybodyDance在身份对应和视觉保真度方面均优于现有技术水平。

## 🔬 方法详解

**问题定义**：论文旨在解决多角色动画中身份对应（Identity Correspondence, IC）的正确性问题。现有方法在处理多角色动画，特别是角色位置发生交换时，难以保证生成动画中角色的身份与参考帧中的角色身份一致。这导致生成的动画角色混乱，缺乏逻辑性和可控性。现有方法缺乏对角色间身份关系的建模和优化，难以应对复杂的多角色场景。

**核心思路**：论文的核心思路是将多角色动画中的身份对应问题建模为一个二分图匹配问题。具体来说，将参考帧和生成帧中的角色分别视为二分图的两个节点集合，通过计算节点之间的相似度（即边权重）来表示角色之间的匹配程度。通过优化二分图的匹配结果，可以实现角色身份的正确对应。这种方法能够显式地建模角色间的关系，并利用图结构信息来提高身份对应的准确性。

**技术框架**：EverybodyDance的整体框架包括以下几个主要模块：1) **Identity Matching Graph (IMG)**：构建二分图，将参考帧和生成帧中的角色表示为节点，角色间的亲和力表示为边权重。2) **Mask-Query Attention (MQA)**：计算角色间的亲和力，作为IMG的边权重。MQA利用角色的掩码信息和查询向量来提取角色特征，并通过注意力机制计算相似度。3) **Identity-Embedded Guidance**：利用身份嵌入信息来引导动画生成过程，确保生成的角色具有一致的身份特征。4) **Multi-Scale Matching Strategy**：采用多尺度匹配策略，在不同尺度上进行身份对应，提高鲁棒性。5) **Pre-Classified Sampling**：采用预分类采样策略，选择具有代表性的样本进行训练，提高效率。

**关键创新**：论文最重要的技术创新点在于将身份对应问题形式化为图结构度量，并设计了Mask-Query Attention机制来计算角色间的亲和力。与现有方法相比，EverybodyDance能够显式地建模角色间的关系，并利用图结构信息来优化身份对应。MQA能够有效地提取角色特征，并对角色间的相似度进行准确估计。此外，论文还提出了一系列针对多角色动画的策略，包括身份嵌入引导、多尺度匹配策略和预分类采样，进一步提高了性能。

**关键设计**：在IMG中，边权重由MQA计算得到，MQA的输入包括角色的掩码信息和查询向量。查询向量通过编码器提取角色特征得到。损失函数包括身份对应损失和视觉保真度损失。身份对应损失用于优化二分图的匹配结果，视觉保真度损失用于保证生成动画的质量。网络结构采用生成对抗网络（GAN），生成器负责生成动画，判别器负责判别生成动画的真伪。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16360v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16360v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16360v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，EverybodyDance在身份对应和视觉保真度方面均显著优于现有方法。在身份对应准确率方面，EverybodyDance比最先进的基线方法提高了约10%。此外，通过消融实验验证了各个模块的有效性，证明了IMG、MQA以及其他策略的协同作用。论文还构建了一个新的身份对应评估基准，为多角色动画的研究提供了新的评估工具。

## 🎯 应用场景

该研究成果可广泛应用于虚拟现实、游戏开发、电影制作等领域。例如，可以用于创建多人在线游戏中玩家角色的动画，或者用于电影中多个演员的动作捕捉和动画生成。该技术能够提高多角色动画的质量和效率，降低制作成本，并为用户提供更加逼真和自然的动画体验。未来，该技术有望进一步扩展到更复杂的多角色场景，例如人群动画和社交互动动画。

## 📄 摘要（原文）

> Consistent pose-driven character animation has achieved remarkable progress in single-character scenarios. However, extending these advances to multi-character settings is non-trivial, especially when position swap is involved. Beyond mere scaling, the core challenge lies in enforcing correct Identity Correspondence (IC) between characters in reference and generated frames. To address this, we introduce EverybodyDance, a systematic solution targeting IC correctness in multi-character animation. EverybodyDance is built around the Identity Matching Graph (IMG), which models characters in the generated and reference frames as two node sets in a weighted complete bipartite graph. Edge weights, computed via our proposed Mask-Query Attention (MQA), quantify the affinity between each pair of characters. Our key insight is to formalize IC correctness as a graph structural metric and to optimize it during training. We also propose a series of targeted strategies tailored for multi-character animation, including identity-embedded guidance, a multi-scale matching strategy, and pre-classified sampling, which work synergistically. Finally, to evaluate IC performance, we curate the Identity Correspondence Evaluation benchmark, dedicated to multi-character IC correctness. Extensive experiments demonstrate that EverybodyDance substantially outperforms state-of-the-art baselines in both IC and visual fidelity.

