---
layout: default
title: DM3D: Deformable Mamba via Offset-Guided Gaussian Sequencing for Point Cloud Understanding
---

# DM3D: Deformable Mamba via Offset-Guided Gaussian Sequencing for Point Cloud Understanding

**arXiv**: [2512.03424v1](https://arxiv.org/abs/2512.03424) | [PDF](https://arxiv.org/pdf/2512.03424.pdf)

**作者**: Bin Liu, Chunyang Wang, Xuelian Liu

---

## 💡 一句话要点

**提出DM3D，通过偏移引导的高斯排序实现点云自适应序列化，以解决状态空间模型在点云理解中的顺序依赖问题。**

**关键词**: `点云理解` `状态空间模型` `自适应序列化` `高斯排序` `变形扫描` `频率融合`

## 📋 核心要点

1. 核心问题：状态空间模型依赖输入顺序，与点云不规则性冲突，现有序列化策略无法适应几何结构。
2. 方法要点：引入偏移引导的高斯排序机制，结合局部重采样和全局重排序，实现端到端优化。
3. 实验或效果：在分类、少样本学习和部件分割任务上达到最先进性能，验证自适应序列化的有效性。

## 📄 摘要（原文）

> State Space Models (SSMs) demonstrate significant potential for long-sequence modeling, but their reliance on input order conflicts with the irregular nature of point clouds. Existing approaches often rely on predefined serialization strategies, which cannot adjust based on diverse geometric structures. To overcome this limitation, we propose \textbf{DM3D}, a deformable Mamba architecture for point cloud understanding. Specifically, DM3D introduces an offset-guided Gaussian sequencing mechanism that unifies local resampling and global reordering within a deformable scan. The Gaussian-based KNN Resampling (GKR) enhances structural awareness by adaptively reorganizing neighboring points, while the Gaussian-based Differentiable Reordering (GDR) enables end-to-end optimization of serialization order. Furthermore, a Tri-Path Frequency Fusion module enhances feature complementarity and reduces aliasing. Together, these components enable structure-adaptive serialization of point clouds. Extensive experiments on benchmark datasets show that DM3D achieves state-of-the-art performance in classification, few-shot learning, and part segmentation, demonstrating that adaptive serialization effectively unlocks the potential of SSMs for point cloud understanding.

