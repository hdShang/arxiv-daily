---
layout: default
title: Hand-Shadow Poser
---

# Hand-Shadow Poser

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07012" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07012v1</a>
  <a href="https://arxiv.org/pdf/2505.07012.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07012v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07012v1', 'Hand-Shadow Poser')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hao Xu, Yinqiao Wang, Niloy J. Mitra, Shuaicheng Liu, Pheng-Ann Heng, Chi-Wing Fu

**分类**: cs.CG, cs.AI

**发布日期**: 2025-05-11

**备注**: SIGGRAPH 2025 (ACM TOG)

**DOI**: [10.1145/3730836](https://doi.org/10.1145/3730836)

---

## 💡 一句话要点

**提出Hand-Shadow Poser以解决手影艺术中的姿态生成问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `手影艺术` `姿态生成` `逆问题` `计算机视觉` `深度学习` `影子特征` `手形状假设` `DINOv2评估`

## 📋 核心要点

1. 核心问题：现有方法在生成手影时面临巨大设计空间和解剖约束的挑战，且输入缺乏颜色和纹理信息。
2. 方法要点：提出的Hand-Shadow Poser通过三阶段管道，分别处理手的形状假设、粗略姿态推断和姿态优化。
3. 实验或效果：通过与多个基线的比较，证明该方法在210个多样化影子形状中有效生成手姿态，成功率超过85%。

## 📝 摘要（中文）

手影艺术是一种迷人的艺术形式，通过手影在墙壁上重现富有表现力的形状。本文研究了一个逆问题：给定目标形状，寻找左右手的姿态，以最佳方式产生与输入相似的影子。由于3D手姿态的设计空间巨大且受解剖限制，且输入是无色无纹理的，因此该问题并不简单。为应对这些挑战，本文设计了Hand-Shadow Poser，一个三阶段的管道，解耦了解剖约束和语义约束。通过广泛的基准测试和用户研究，证明了该方法在超过85%的基准案例中有效生成双手姿态。

## 🔬 方法详解

**问题定义**：本文旨在解决给定目标形状时，如何找到左右手的最佳姿态以产生相似影子的逆问题。现有方法在处理3D手姿态时面临设计空间巨大和解剖限制的痛点，同时输入缺乏颜色和纹理信息，增加了难度。

**核心思路**：论文的核心思路是通过三阶段管道来解耦解剖约束和语义约束。首先生成多样的手形状假设，然后推断粗略姿态，最后优化姿态以确保物理合理性和影子特征的保留。

**技术框架**：整体架构包括三个主要模块：生成手形状假设的生成模块、基于相似性推断粗略姿态的对齐模块，以及优化手姿态的细化模块。

**关键创新**：最重要的技术创新在于设计了一个可在通用公共手数据上训练的管道，避免了对专门训练数据集的需求。此外，提出了一种基于DINOv2的新评估指标。

**关键设计**：在关键设计方面，采用了多样性和合理性相结合的假设生成策略，使用相似性驱动的策略选择假设，并在优化阶段注重影子特征的保留。

## 📊 实验亮点

实验结果显示，Hand-Shadow Poser在210个多样化影子形状的基准测试中，成功生成双手姿态的比例超过85%。与多个基线方法相比，该方法在影子形状的生成上表现出显著的提升，验证了其有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括艺术创作、动画制作和虚拟现实等。通过生成自然的手影姿态，可以为艺术家和设计师提供新的创作工具，同时在教育和娱乐领域也具有重要价值。未来，该技术可能会影响手势识别和人机交互的研究方向。

## 📄 摘要（原文）

> Hand shadow art is a captivating art form, creatively using hand shadows to reproduce expressive shapes on the wall. In this work, we study an inverse problem: given a target shape, find the poses of left and right hands that together best produce a shadow resembling the input. This problem is nontrivial, since the design space of 3D hand poses is huge while being restrictive due to anatomical constraints. Also, we need to attend to the input's shape and crucial features, though the input is colorless and textureless. To meet these challenges, we design Hand-Shadow Poser, a three-stage pipeline, to decouple the anatomical constraints (by hand) and semantic constraints (by shadow shape): (i) a generative hand assignment module to explore diverse but reasonable left/right-hand shape hypotheses; (ii) a generalized hand-shadow alignment module to infer coarse hand poses with a similarity-driven strategy for selecting hypotheses; and (iii) a shadow-feature-aware refinement module to optimize the hand poses for physical plausibility and shadow feature preservation. Further, we design our pipeline to be trainable on generic public hand data, thus avoiding the need for any specialized training dataset. For method validation, we build a benchmark of 210 diverse shadow shapes of varying complexity and a comprehensive set of metrics, including a novel DINOv2-based evaluation metric. Through extensive comparisons with multiple baselines and user studies, our approach is demonstrated to effectively generate bimanual hand poses for a large variety of hand shapes for over 85% of the benchmark cases.

