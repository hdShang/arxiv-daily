---
layout: default
title: "APML: Adaptive Probabilistic Matching Loss for Robust 3D Point Cloud Reconstruction"
---

# APML: Adaptive Probabilistic Matching Loss for Robust 3D Point Cloud Reconstruction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.08104" class="toolbar-btn" target="_blank">📄 arXiv: 2509.08104v1</a>
  <a href="https://arxiv.org/pdf/2509.08104.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.08104v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.08104v1', 'APML: Adaptive Probabilistic Matching Loss for Robust 3D Point Cloud Reconstruction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sasan Sharifipour, Constantino Álvarez Casado, Mohammad Sabokrou, Miguel Bordallo López

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-09

**备注**: 22 pages, 6 figures, conference, 7 tables, 15 formulas

**🔗 代码/项目**: [GITHUB](https://github.com/apm-loss/apml)

---

## 💡 一句话要点

**提出自适应概率匹配损失以解决3D点云重建问题**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `点云重建` `损失函数` `深度学习` `3D建模` `机器学习` `计算机视觉` `自适应算法`

## 📋 核心要点

1. 现有的点云损失函数常导致多对一的对应关系，影响模型在密集和稀疏区域的表现。
2. 本文提出自适应概率匹配损失（APML），通过Sinkhorn迭代实现完全可微分的一对一匹配，避免了手动调参。
3. 在ShapeNet基准和WiFi CSI测量生成3D人类点云的实验中，APML显示出更快的收敛和优越的空间分布，且无需额外超参数搜索。

## 📝 摘要（中文）

深度学习模型在点云预测任务（如形状补全和生成）中的训练，依赖于能够有效衡量预测点集与真实点集之间差异的损失函数。常用的损失函数如Chamfer距离、HyperCD和InfoCD依赖于最近邻分配，导致多对一的对应关系，造成密集区域的点拥挤和稀疏区域的覆盖不足。此外，这些损失函数由于索引选择涉及非可微分操作，可能影响基于梯度的优化。地球移动者距离（EMD）虽然能够强制一对一的对应关系并更有效地捕捉结构相似性，但其立方复杂度限制了实际应用。为此，本文提出了自适应概率匹配损失（APML），这是一个完全可微分的一对一匹配近似方法，利用Sinkhorn迭代在温度缩放的相似性矩阵上进行计算。APML在运行时间上接近二次，且避免了非可微分操作，集成到先进架构中时，表现出更快的收敛速度和优越的空间分布。

## 🔬 方法详解

**问题定义**：本文旨在解决现有点云预测任务中损失函数导致的多对一对应关系问题，影响了模型在不同密度区域的表现。

**核心思路**：提出自适应概率匹配损失（APML），通过Sinkhorn迭代在温度缩放的相似性矩阵上进行计算，实现一对一匹配的可微分近似。

**技术框架**：APML的整体架构包括温度计算模块、相似性矩阵生成模块和Sinkhorn迭代模块，确保了最小分配概率并避免了手动调参。

**关键创新**：APML的核心创新在于其完全可微分的设计，克服了传统损失函数的非可微分操作和高计算复杂度问题。

**关键设计**：通过分析温度参数，确保了分配概率的下限，设计了与现有Chamfer损失相当的近似运行时间，同时避免了多对一的点匹配问题。

## 📊 实验亮点

在ShapeNet基准测试中，APML集成到PoinTr、PCN和FoldingNet等先进架构中，显示出更快的收敛速度和优越的空间分布，尤其是在低密度区域。此外，APML在定量性能上与现有方法持平或有所提升，且无需额外的超参数搜索。

## 🎯 应用场景

该研究的潜在应用领域包括3D重建、机器人导航、虚拟现实和增强现实等。通过提高点云重建的精度和效率，APML能够在实际应用中显著提升模型的表现，推动相关技术的发展和应用。未来，APML的设计理念也可能扩展到其他领域的损失函数优化中。

## 📄 摘要（原文）

> Training deep learning models for point cloud prediction tasks such as shape completion and generation depends critically on loss functions that measure discrepancies between predicted and ground-truth point sets. Commonly used functions such as Chamfer Distance (CD), HyperCD, and InfoCD rely on nearest-neighbor assignments, which often induce many-to-one correspondences, leading to point congestion in dense regions and poor coverage in sparse regions. These losses also involve non-differentiable operations due to index selection, which may affect gradient-based optimization. Earth Mover Distance (EMD) enforces one-to-one correspondences and captures structural similarity more effectively, but its cubic computational complexity limits its practical use. We propose the Adaptive Probabilistic Matching Loss (APML), a fully differentiable approximation of one-to-one matching that leverages Sinkhorn iterations on a temperature-scaled similarity matrix derived from pairwise distances. We analytically compute the temperature to guarantee a minimum assignment probability, eliminating manual tuning. APML achieves near-quadratic runtime, comparable to Chamfer-based losses, and avoids non-differentiable operations. When integrated into state-of-the-art architectures (PoinTr, PCN, FoldingNet) on ShapeNet benchmarks and on a spatiotemporal Transformer (CSI2PC) that generates 3D human point clouds from WiFi CSI measurements, APM loss yields faster convergence, superior spatial distribution, especially in low-density regions, and improved or on-par quantitative performance without additional hyperparameter search. The code is available at: https://github.com/apm-loss/apml.

