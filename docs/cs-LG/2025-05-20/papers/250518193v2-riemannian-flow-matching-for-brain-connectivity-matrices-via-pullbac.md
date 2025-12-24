---
layout: default
title: Riemannian Flow Matching for Brain Connectivity Matrices via Pullback Geometry
---

# Riemannian Flow Matching for Brain Connectivity Matrices via Pullback Geometry

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.18193" class="toolbar-btn" target="_blank">📄 arXiv: 2505.18193v2</a>
  <a href="https://arxiv.org/pdf/2505.18193.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.18193v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.18193v2', 'Riemannian Flow Matching for Brain Connectivity Matrices via Pullback Geometry')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Antoine Collas, Ce Ju, Nicolas Salvy, Bertrand Thirion

**分类**: cs.LG, eess.SP, stat.ML

**发布日期**: 2025-05-20 (更新: 2025-10-23)

**备注**: Accepted at NeurIPS 2025

**🔗 代码/项目**: [GITHUB](https://github.com/antoinecollas/DiffeoCFM)

---

## 💡 一句话要点

**提出DiffeoCFM以解决脑连接矩阵生成问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `脑连接矩阵` `黎曼流形` `条件流匹配` `数据增强` `功能连接性` `神经科学` `机器学习`

## 📋 核心要点

1. 现有方法在生成脑连接矩阵时面临计算效率低下的问题，尤其是在处理黎曼流形时。
2. 本文提出DiffeoCFM，通过拉回度量在矩阵流形上实现条件流匹配，提升了生成建模的效率。
3. 在多个大规模数据集上，DiffeoCFM实现了快速训练，并在性能上超过了现有的最先进方法。

## 📝 摘要（中文）

生成现实的脑连接矩阵对于分析脑组织的群体异质性、理解疾病以及在挑战性分类问题中增强数据至关重要。功能连接矩阵位于受限空间，如对称正定矩阵或相关矩阵，这些可以建模为黎曼流形。然而，使用黎曼工具通常需要重新定义核心操作（测地线、范数、积分），使得生成建模计算效率低下。本文提出DiffeoCFM，一种通过利用欧几里得空间上的全局微分同胚诱导的拉回度量，在矩阵流形上实现条件流匹配（CFM）的方法。我们展示了使用这种度量的黎曼CFM等同于在数据变换后应用标准CFM。这一等价性允许高效的向量场学习和使用标准ODE求解器进行快速采样。我们在三个大规模fMRI数据集和两个EEG运动想象数据集上评估DiffeoCFM，结果显示其训练快速且性能达到最先进水平，同时保持流形约束。

## 🔬 方法详解

**问题定义**：本文旨在解决生成脑连接矩阵的效率问题，现有方法在黎曼流形上进行操作时计算复杂度较高，导致生成建模效率低下。

**核心思路**：DiffeoCFM通过利用全局微分同胚诱导的拉回度量，使得在矩阵流形上进行条件流匹配成为可能，从而提高了计算效率。

**技术框架**：整体架构包括数据变换、拉回度量的应用、向量场学习和快速采样四个主要模块。首先对输入数据进行变换，然后应用拉回度量进行流匹配，接着进行向量场的学习，最后使用ODE求解器进行快速采样。

**关键创新**：DiffeoCFM的核心创新在于将黎曼CFM与标准CFM之间建立了等价性，从而避免了传统黎曼方法的计算瓶颈，显著提升了效率。

**关键设计**：在实现中，采用了矩阵对数和标准化Cholesky分解作为不同设置的基础，确保了生成的矩阵符合流形约束，同时优化了损失函数以适应流匹配的需求。

## 📊 实验亮点

DiffeoCFM在三个大规模fMRI数据集（ADNI、ABIDE、OASIS-3）和两个EEG数据集（BNCI2014-002和BNCI2015-001）上进行了评估，结果显示其训练速度显著提升，并在性能上达到了最先进水平，具体提升幅度未知。

## 🎯 应用场景

该研究的潜在应用领域包括脑科学研究、临床诊断和个性化医疗等。通过生成高质量的脑连接矩阵，研究人员可以更好地分析脑功能和结构的变化，进而推动对神经疾病的理解和治疗。此外，该方法在其他需要处理矩阵流形的领域也具有广泛的应用前景。

## 📄 摘要（原文）

> Generating realistic brain connectivity matrices is key to analyzing population heterogeneity in brain organization, understanding disease, and augmenting data in challenging classification problems. Functional connectivity matrices lie in constrained spaces, such as the set of symmetric positive definite or correlation matrices, that can be modeled as Riemannian manifolds. However, using Riemannian tools typically requires redefining core operations (geodesics, norms, integration), making generative modeling computationally inefficient. In this work, we propose DiffeoCFM, an approach that enables conditional flow matching (CFM) on matrix manifolds by exploiting pullback metrics induced by global diffeomorphisms on Euclidean spaces. We show that Riemannian CFM with such metrics is equivalent to applying standard CFM after data transformation. This equivalence allows efficient vector field learning, and fast sampling with standard ODE solvers. We instantiate DiffeoCFM with two different settings: the matrix logarithm for covariance matrices and the normalized Cholesky decomposition for correlation matrices. We evaluate DiffeoCFM on three large-scale fMRI datasets with more than 4600 scans from 2800 subjects (ADNI, ABIDE, OASIS-3) and two EEG motor imagery datasets with over 30000 trials from 26 subjects (BNCI2014-002 and BNCI2015-001). It enables fast training and achieves state-of-the-art performance, all while preserving manifold constraints. Code: https://github.com/antoinecollas/DiffeoCFM

