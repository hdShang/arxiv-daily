---
layout: default
title: "MambaTAD: When State-Space Models Meet Long-Range Temporal Action Detection"
---

# MambaTAD: When State-Space Models Meet Long-Range Temporal Action Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.17929" class="toolbar-btn" target="_blank">📄 arXiv: 2511.17929v1</a>
  <a href="https://arxiv.org/pdf/2511.17929.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.17929v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.17929v1', 'MambaTAD: When State-Space Models Meet Long-Range Temporal Action Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hui Lu, Yi Yu, Shijian Lu, Deepu Rajan, Boon Poh Ng, Alex C. Kot, Xudong Jiang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-22

**期刊**: IEEE Transactions on Multimedia, 2025

---

## 💡 一句话要点

**MambaTAD：结合状态空间模型的长程时序动作检测方法**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `时序动作检测` `状态空间模型` `Mamba` `长程建模` `全局特征融合`

## 📋 核心要点

1. 现有TAD方法在处理长跨度动作时，面临全局感知不足和检测头效率低下的问题。
2. MambaTAD通过引入对角掩码双向状态空间模块和全局特征融合头，增强长程建模和全局特征检测能力。
3. 实验结果表明，MambaTAD在多个公开数据集上取得了优于现有方法的性能。

## 📝 摘要（中文）

时序动作检测(TAD)旨在通过确定未剪辑视频中动作的起始和结束帧来识别和定位动作。最近的结构化状态空间模型，如Mamba，由于其长程建模能力和线性计算复杂度，在TAD中展现出潜力。然而，结构化状态空间模型在TAD中常面临两个关键挑战：由递归处理引起的时间上下文衰减，以及全局视觉上下文建模期间的自元素冲突，这在处理长跨度动作实例时变得更加严重。此外，由于缺乏全局感知和低效的检测头，传统TAD方法难以检测长跨度动作实例。本文提出了MambaTAD，一种新的状态空间TAD模型，引入了长程建模和全局特征检测能力，以实现精确的时序动作检测。MambaTAD包含两个相互补充的新颖设计，以实现卓越的TAD性能。首先，它引入了一个对角掩码双向状态空间(DMBSS)模块，有效地促进了全局特征融合和时序动作检测。其次，它引入了一个全局特征融合头，通过多粒度特征和全局感知逐步细化检测。此外，MambaTAD使用一种新的状态空间时间适配器(SSTA)，以端到端单阶段的方式处理TAD，从而以线性复杂度降低网络参数和计算成本。大量实验表明，MambaTAD在多个公共基准测试中始终如一地实现了卓越的TAD性能。

## 🔬 方法详解

**问题定义**：论文旨在解决时序动作检测（TAD）中，现有方法在处理长跨度动作实例时，由于缺乏全局感知和低效的检测头而导致的检测精度下降问题。特别是，基于状态空间模型的方法在TAD中面临时间上下文衰减和自元素冲突的挑战。

**核心思路**：论文的核心思路是利用Mamba状态空间模型的长程建模能力，并设计新的模块来克服其在TAD任务中的局限性。通过引入对角掩码双向状态空间（DMBSS）模块和全局特征融合头，增强模型对全局上下文的理解和对长跨度动作的检测能力。

**技术框架**：MambaTAD采用端到端单阶段的检测框架。首先，使用状态空间时间适配器（SSTA）提取视频特征。然后，通过DMBSS模块进行全局特征融合和时序建模。最后，利用全局特征融合头，结合多粒度特征进行动作检测。

**关键创新**：论文的关键创新在于DMBSS模块和全局特征融合头的设计。DMBSS模块通过对角掩码机制，避免了自元素冲突，并促进了全局特征融合。全局特征融合头利用多粒度特征和全局感知，逐步细化检测结果，提高了检测精度。此外，SSTA的使用降低了参数量和计算复杂度。

**关键设计**：DMBSS模块的关键设计在于对角掩码，它阻止了同一时间步的特征之间的相互作用，从而避免了自元素冲突。全局特征融合头的关键设计在于多粒度特征的融合策略，它将不同尺度的特征结合起来，以获得更全面的上下文信息。SSTA通过线性复杂度降低了参数量和计算成本，具体实现细节未知。

## 📊 实验亮点

MambaTAD在多个公开TAD数据集上取得了显著的性能提升。具体数据未知，但论文强调其在多个基准测试中始终如一地实现了卓越的TAD性能，表明其具有良好的泛化能力和实用价值。相较于现有方法，MambaTAD在长跨度动作的检测方面表现出更强的优势。

## 🎯 应用场景

MambaTAD在视频监控、智能安防、体育赛事分析、视频内容理解等领域具有广泛的应用前景。它可以用于自动识别和定位视频中的异常行为、关键事件和感兴趣的动作，从而提高视频分析的效率和准确性。该研究的成果有助于推动视频理解和人工智能技术的发展。

## 📄 摘要（原文）

> Temporal Action Detection (TAD) aims to identify and localize actions by determining their starting and ending frames within untrimmed videos. Recent Structured State-Space Models such as Mamba have demonstrated potential in TAD due to their long-range modeling capability and linear computational complexity. On the other hand, structured state-space models often face two key challenges in TAD, namely, decay of temporal context due to recursive processing and self-element conflict during global visual context modeling, which become more severe while handling long-span action instances. Additionally, traditional methods for TAD struggle with detecting long-span action instances due to a lack of global awareness and inefficient detection heads. This paper presents MambaTAD, a new state-space TAD model that introduces long-range modeling and global feature detection capabilities for accurate temporal action detection. MambaTAD comprises two novel designs that complement each other with superior TAD performance. First, it introduces a Diagonal-Masked Bidirectional State-Space (DMBSS) module which effectively facilitates global feature fusion and temporal action detection. Second, it introduces a global feature fusion head that refines the detection progressively with multi-granularity features and global awareness. In addition, MambaTAD tackles TAD in an end-to-end one-stage manner using a new state-space temporal adapter(SSTA) which reduces network parameters and computation cost with linear complexity. Extensive experiments show that MambaTAD achieves superior TAD performance consistently across multiple public benchmarks.

