---
layout: default
title: "PPMStereo: Pick-and-Play Memory Construction for Consistent Dynamic Stereo Matching"
---

# PPMStereo: Pick-and-Play Memory Construction for Consistent Dynamic Stereo Matching

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.20178" class="toolbar-btn" target="_blank">📄 arXiv: 2510.20178v1</a>
  <a href="https://arxiv.org/pdf/2510.20178.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.20178v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.20178v1', 'PPMStereo: Pick-and-Play Memory Construction for Consistent Dynamic Stereo Matching')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yun Wang, Junjie Hu, Qiaole Dong, Yongjian Zhang, Yanwei Fu, Tin Lun Lam, Dapeng Wu

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-23

**期刊**: NeurIPS 2025

**🔗 代码/项目**: [GITHUB](https://github.com/cocowy1/PPMStereo)

---

## 💡 一句话要点

**提出PPMStereo，通过Pick-and-Play记忆构建实现动态立体匹配中的时序一致性。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `动态立体匹配` `时序一致性` `深度估计` `记忆网络` `Pick-and-Play`

## 📋 核心要点

1. 现有立体匹配方法难以在计算效率和长期时序一致性建模之间取得平衡。
2. PPMStereo模仿人类决策过程，通过Pick-and-Play机制构建记忆，实现高效时空信息聚合。
3. 实验表明，PPMStereo在准确性和时序一致性方面均优于现有技术，且计算成本更低。

## 📝 摘要（中文）

从立体视频中进行时序一致的深度估计对于增强现实等实际应用至关重要，因为不一致的深度估计会破坏用户的沉浸感。尽管其重要性，但由于难以以计算高效的方式对长期时序一致性进行建模，这项任务仍然具有挑战性。先前的方法试图通过聚合时空信息来解决这个问题，但面临着一个根本的权衡：有限的时序建模只能提供适度的增益，而捕获长程依赖关系会显著增加计算成本。为了解决这个限制，我们引入了一个记忆缓冲区，用于建模长程时空一致性，同时实现高效的动态立体匹配。受到人类两阶段决策过程的启发，我们提出了一个用于动态立体匹配的Pick-and-Play记忆（PPM）构建模块，称为PPMStereo。PPM由一个“选择”过程（识别最相关的帧）和一个“播放”过程（自适应地加权所选帧以进行时空聚合）组成。这种两阶段协作过程维护了一个紧凑但信息量很大的记忆缓冲区，同时实现了时间上一致的信息聚合。大量的实验验证了PPMStereo的有效性，证明了其在准确性和时间一致性方面的最先进性能。值得注意的是，PPMStereo在Sintel clean/final上实现了0.62/1.11 TEPE（比BiDAStereo提高了17.3％和9.02％），同时降低了计算成本。

## 🔬 方法详解

**问题定义**：论文旨在解决动态立体匹配中，如何高效地建模长期时序一致性的问题。现有方法要么时序建模能力有限，要么计算复杂度过高，难以在实际应用中取得良好效果。这些方法无法有效地利用视频序列中的时间信息，导致深度估计结果在时间上不连贯，影响用户体验。

**核心思路**：论文的核心思路是借鉴人类的决策过程，通过一个两阶段的Pick-and-Play机制来构建一个记忆缓冲区。该记忆缓冲区存储了过去帧的信息，并能够根据当前帧的特征，选择性地提取和聚合相关信息，从而实现长期时序一致性的建模。这种方法能够在保证计算效率的同时，有效地利用时间信息。

**技术框架**：PPMStereo的整体框架包含以下几个主要模块：1) 特征提取模块：用于提取左右图像的特征。2) Pick模块：从记忆缓冲区中选择与当前帧最相关的帧。3) Play模块：根据选择的帧，自适应地加权记忆缓冲区中的信息，并与当前帧的特征进行聚合。4) 代价体构建与优化模块：基于聚合后的特征构建代价体，并使用3D卷积神经网络进行优化，最终得到视差图。

**关键创新**：PPMStereo的关键创新在于Pick-and-Play记忆构建模块。与现有方法直接聚合所有过去帧的信息不同，PPMStereo首先通过Pick模块选择最相关的帧，然后通过Play模块自适应地加权这些帧的信息。这种选择性的聚合方式能够有效地减少计算量，并提高时序一致性。

**关键设计**：Pick模块使用注意力机制来衡量过去帧与当前帧的相关性，选择相关性最高的K个帧。Play模块使用另一个注意力机制来学习每个被选择帧的权重，然后将这些帧的信息加权聚合到当前帧的特征中。损失函数包括视差预测损失和时序一致性损失，其中时序一致性损失鼓励相邻帧的视差预测结果保持一致。

## 📊 实验亮点

PPMStereo在Sintel数据集上取得了显著的性能提升。在Sintel clean和final数据集上，PPMStereo分别实现了0.62和1.11的TEPE（Temporal Endpoint Error），相比于BiDAStereo，分别提升了17.3%和9.02%。同时，PPMStereo在保持甚至降低计算成本的情况下，实现了更高的准确性和时序一致性，证明了其有效性。

## 🎯 应用场景

PPMStereo在增强现实、机器人导航、自动驾驶等领域具有广泛的应用前景。在增强现实中，时序一致的深度估计能够提供更稳定的虚拟物体叠加效果，提升用户体验。在机器人导航和自动驾驶中，准确且时序一致的深度信息对于环境感知和路径规划至关重要，可以提高系统的安全性和可靠性。未来，该技术可以进一步扩展到其他需要时序一致性深度估计的应用场景。

## 📄 摘要（原文）

> Temporally consistent depth estimation from stereo video is critical for real-world applications such as augmented reality, where inconsistent depth estimation disrupts the immersion of users. Despite its importance, this task remains challenging due to the difficulty in modeling long-term temporal consistency in a computationally efficient manner. Previous methods attempt to address this by aggregating spatio-temporal information but face a fundamental trade-off: limited temporal modeling provides only modest gains, whereas capturing long-range dependencies significantly increases computational cost. To address this limitation, we introduce a memory buffer for modeling long-range spatio-temporal consistency while achieving efficient dynamic stereo matching. Inspired by the two-stage decision-making process in humans, we propose a \textbf{P}ick-and-\textbf{P}lay \textbf{M}emory (PPM) construction module for dynamic \textbf{Stereo} matching, dubbed as \textbf{PPMStereo}. PPM consists of a `pick' process that identifies the most relevant frames and a `play' process that weights the selected frames adaptively for spatio-temporal aggregation. This two-stage collaborative process maintains a compact yet highly informative memory buffer while achieving temporally consistent information aggregation. Extensive experiments validate the effectiveness of PPMStereo, demonstrating state-of-the-art performance in both accuracy and temporal consistency. % Notably, PPMStereo achieves 0.62/1.11 TEPE on the Sintel clean/final (17.3\% \& 9.02\% improvements over BiDAStereo) with fewer computational costs. Codes are available at \textcolor{blue}{https://github.com/cocowy1/PPMStereo}.

