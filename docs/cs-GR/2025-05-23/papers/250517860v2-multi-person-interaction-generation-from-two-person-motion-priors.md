---
layout: default
title: Multi-Person Interaction Generation from Two-Person Motion Priors
---

# Multi-Person Interaction Generation from Two-Person Motion Priors

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.17860" class="toolbar-btn" target="_blank">📄 arXiv: 2505.17860v2</a>
  <a href="https://arxiv.org/pdf/2505.17860.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.17860v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.17860v2', 'Multi-Person Interaction Generation from Two-Person Motion Priors')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenning Xu, Shiyu Fan, Paul Henderson, Edmond S. L. Ho

**分类**: cs.GR, cs.CV, cs.LG

**发布日期**: 2025-05-23 (更新: 2025-07-26)

**备注**: SIGGRAPH 2025 Conference Papers, project page at http://wenningxu.github.io/multicharacter/

---

## 💡 一句话要点

**提出图驱动交互采样以解决多人人体交互生成问题**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)** **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `多人人体交互` `运动生成` `图驱动方法` `扩散模型` `运动捕捉` `机器人技术` `虚拟现实`

## 📋 核心要点

1. 现有方法在多人人体交互生成方面探索不足，导致生成的动作缺乏多样性和真实感。
2. 本文提出的图驱动交互采样方法，通过将复杂交互分解为双人交互图，创新性地实现了多人人体交互的生成。
3. 实验结果显示，该方法在生成多种交互时，显著减少了身体部位交叉等伪影，超越了现有技术。

## 📝 摘要（中文）

生成逼真的人类动作并进行高层次控制是社会理解、机器人技术和动画中的关键任务。尽管高质量的运动捕捉数据日益可用，建模多人人体交互仍然是一个较少探索的领域。本文提出了一种图驱动的交互采样方法，通过利用现有的双人运动扩散模型作为运动先验，生成真实且多样的多人人体交互。我们将复杂的多人人体交互在空间和时间上分离为双人交互的图结构，从而将生成任务分解为基于彼此动作的单人运动生成。同时，为减少生成多人人体交互时的伪影，我们在扩散采样方案中引入了两个图依赖的引导项。实验表明，我们的方法在生成多种双人和多人人体交互时，能够有效减少伪影，且不产生重复的个体动作。

## 🔬 方法详解

**问题定义**：本文旨在解决多人人体交互生成中的真实感和多样性不足的问题。现有方法往往专注于单一的双人交互，难以有效扩展到多人人体交互，导致生成结果的质量和多样性不足。

**核心思路**：论文的核心思路是将复杂的多人人体交互分解为双人交互的图结构，称为成对交互图，从而实现基于彼此动作的单人运动生成。这种设计使得生成过程更为灵活且易于控制。

**技术框架**：整体架构包括两个主要模块：首先是成对交互图的构建，其次是基于图结构的扩散采样过程。通过将多人人体交互转化为双人交互的组合，能够有效利用现有的双人运动模型。

**关键创新**：最重要的技术创新在于引入了图驱动的交互采样方法，能够在不训练新模型的情况下，利用已有的双人运动扩散模型生成多人人体交互。这一方法显著提高了生成的多样性和质量。

**关键设计**：在技术细节上，论文设计了两个图依赖的引导项，以减少生成过程中可能出现的身体部位交叉等伪影。此外，损失函数的设计也考虑了生成动作的连贯性和真实感，确保生成结果的自然流畅。

## 📊 实验亮点

实验结果表明，提出的方法在生成多种双人和多人人体交互时，能够有效减少身体部位交叉等伪影，相较于现有方法，生成质量提升显著，具体性能数据未提供，但实验表明一致性优于基线方法。

## 🎯 应用场景

该研究的潜在应用领域包括社交机器人、虚拟现实、动画制作等。通过生成高质量的多人人体交互，能够提升人机交互的自然性和真实感，推动相关领域的发展。未来，该技术可能在游戏设计、影视制作等方面发挥重要作用。

## 📄 摘要（原文）

> Generating realistic human motion with high-level controls is a crucial task for social understanding, robotics, and animation. With high-quality MOCAP data becoming more available recently, a wide range of data-driven approaches have been presented. However, modelling multi-person interactions still remains a less explored area. In this paper, we present Graph-driven Interaction Sampling, a method that can generate realistic and diverse multi-person interactions by leveraging existing two-person motion diffusion models as motion priors. Instead of training a new model specific to multi-person interaction synthesis, our key insight is to spatially and temporally separate complex multi-person interactions into a graph structure of two-person interactions, which we name the Pairwise Interaction Graph. We thus decompose the generation task into simultaneous single-person motion generation conditioned on one other's motion. In addition, to reduce artifacts such as interpenetrations of body parts in generated multi-person interactions, we introduce two graph-dependent guidance terms into the diffusion sampling scheme. Unlike previous work, our method can produce various high-quality multi-person interactions without having repetitive individual motions. Extensive experiments demonstrate that our approach consistently outperforms existing methods in reducing artifacts when generating a wide range of two-person and multi-person interactions.

