---
layout: default
title: "GeoERM: Geometry-Aware Multi-Task Representation Learning on Riemannian Manifolds"
---

# GeoERM: Geometry-Aware Multi-Task Representation Learning on Riemannian Manifolds

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02972" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02972v1</a>
  <a href="https://arxiv.org/pdf/2505.02972.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02972v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02972v1', 'GeoERM: Geometry-Aware Multi-Task Representation Learning on Riemannian Manifolds')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aoran Chen, Yang Feng

**分类**: stat.ML, cs.LG, stat.ME

**发布日期**: 2025-05-05

---

## 💡 一句话要点

**提出GeoERM以解决多任务学习中的几何不一致问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多任务学习` `黎曼流形` `几何感知` `鲁棒性` `活动识别` `对抗学习` `矩阵分解`

## 📋 核心要点

1. 现有的多任务学习方法通常忽视潜在表示的几何特性，导致在任务异质性和对抗性情况下的鲁棒性不足。
2. 本文提出的GeoERM框架通过在黎曼流形上嵌入共享表示，并进行显式的流形操作来优化表示，提升了学习效果。
3. 实验结果表明，GeoERM在合成任务和可穿戴传感器活动识别基准上均显著提高了准确性，减少了负迁移现象。

## 📝 摘要（中文）

多任务学习（MTL）旨在通过发现相关任务间的共享结构来提升统计能力和学习效率。然而，现有的MTL表示方法通常将潜在表示矩阵视为普通欧几里得空间中的点，忽视了其非欧几里得几何特性，从而在任务异质性或对抗性情况下牺牲了鲁棒性。为此，本文提出了GeoERM，一个几何感知的MTL框架，该框架在其自然的黎曼流形上嵌入共享表示，并通过显式的流形操作进行优化。每个训练周期执行（i）尊重搜索空间内在曲率的黎曼梯度步骤，随后（ii）高效的极点回缩以保持在流形上，确保每次迭代的几何保真性。该过程适用于广泛的矩阵分解MTL模型，并保持与欧几里得基线相同的每次迭代成本。在一系列具有任务异质性的合成实验和可穿戴传感器活动识别基准上，GeoERM始终提高了估计准确性，减少了负迁移，并在对抗标签噪声下保持稳定，超越了领先的MTL和单任务替代方案。

## 🔬 方法详解

**问题定义**：本文旨在解决多任务学习中潜在表示的几何特性被忽视的问题，现有方法在处理异质任务时表现出鲁棒性不足的缺陷。

**核心思路**：GeoERM框架通过在黎曼流形上嵌入共享表示，利用流形的几何特性进行优化，从而提高学习的稳定性和准确性。

**技术框架**：GeoERM的整体架构包括两个主要模块：第一，进行黎曼梯度步骤以适应流形的内在曲率；第二，执行极点回缩以确保每次迭代都保持在流形上。

**关键创新**：GeoERM的主要创新在于将多任务学习的表示优化问题转化为黎曼流形上的优化问题，显著提升了对任务异质性和对抗性噪声的鲁棒性。

**关键设计**：在损失函数设计上，GeoERM采用了适应流形的损失计算方式，并在每次迭代中保持与欧几里得基线相同的计算成本，确保了高效性。具体的参数设置和网络结构细节在实验部分进行了详细描述。

## 📊 实验亮点

在一系列实验中，GeoERM在合成任务和可穿戴传感器活动识别基准上均显著提高了估计准确性，减少了负迁移现象。在对抗标签噪声的情况下，GeoERM的表现也保持稳定，超越了现有的多任务学习和单任务学习方法。

## 🎯 应用场景

GeoERM的研究成果具有广泛的应用潜力，特别是在需要处理异质任务的领域，如医疗诊断、智能监控和人机交互等。通过提升多任务学习的鲁棒性和准确性，GeoERM能够为这些领域提供更可靠的解决方案，推动相关技术的发展。

## 📄 摘要（原文）

> Multi-Task Learning (MTL) seeks to boost statistical power and learning efficiency by discovering structure shared across related tasks. State-of-the-art MTL representation methods, however, usually treat the latent representation matrix as a point in ordinary Euclidean space, ignoring its often non-Euclidean geometry, thus sacrificing robustness when tasks are heterogeneous or even adversarial. We propose GeoERM, a geometry-aware MTL framework that embeds the shared representation on its natural Riemannian manifold and optimizes it via explicit manifold operations. Each training cycle performs (i) a Riemannian gradient step that respects the intrinsic curvature of the search space, followed by (ii) an efficient polar retraction to remain on the manifold, guaranteeing geometric fidelity at every iteration. The procedure applies to a broad class of matrix-factorized MTL models and retains the same per-iteration cost as Euclidean baselines. Across a set of synthetic experiments with task heterogeneity and on a wearable-sensor activity-recognition benchmark, GeoERM consistently improves estimation accuracy, reduces negative transfer, and remains stable under adversarial label noise, outperforming leading MTL and single-task alternatives.

