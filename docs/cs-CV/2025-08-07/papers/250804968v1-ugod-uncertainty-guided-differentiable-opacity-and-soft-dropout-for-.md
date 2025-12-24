---
layout: default
title: "UGOD: Uncertainty-Guided Differentiable Opacity and Soft Dropout for Enhanced Sparse-View 3DGS"
---

# UGOD: Uncertainty-Guided Differentiable Opacity and Soft Dropout for Enhanced Sparse-View 3DGS

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04968" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04968v1</a>
  <a href="https://arxiv.org/pdf/2508.04968.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04968v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04968v1', 'UGOD: Uncertainty-Guided Differentiable Opacity and Soft Dropout for Enhanced Sparse-View 3DGS')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhihao Guo, Peng Wang, Zidong Chen, Xiangyu Kong, Yan Lyu, Guanyu Gao, Liangxiu Han

**分类**: cs.CV, cs.AI

**发布日期**: 2025-08-07

**备注**: 11 pages, 5 figures

---

## 💡 一句话要点

**提出不确定性引导的可微透明度与软丢弃以提升稀疏视图3DGS**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D高斯点云` `新视图合成` `稀疏视图` `不确定性学习` `渲染质量提升` `计算机视觉` `图形学`

## 📋 核心要点

1. 现有3DGS方法对高斯的权重处理相同，导致在稀疏视图场景中容易出现过拟合，影响渲染质量。
2. 本文提出了一种基于学习不确定性的自适应加权方法，能够有效引导高斯透明度的更新和丢弃策略。
3. 实验结果显示，本文方法在多个数据集上实现了更高的重建质量，尤其在MipNeRF 360数据集上显著提升了PSNR。

## 📝 摘要（中文）

3D高斯点云（3DGS）因其通过3D高斯投影和混合实现的高效渲染而成为新视图合成（NVS）的竞争性方法。然而，大多数3DGS方法对高斯的权重处理相同，导致在稀疏视图场景中容易过拟合。为了解决这一问题，本文研究了高斯的自适应加权对渲染质量的影响，提出了学习的不确定性。该不确定性不仅引导高斯透明度的可微更新，同时通过软可微丢弃正则化，将原始不确定性转化为控制最终高斯投影和混合过程的连续丢弃概率。实验结果表明，本文方法在稀疏视图3D合成中优于现有方法，在大多数数据集上实现了更高质量的重建，尤其是在MipNeRF 360数据集上相比DropGaussian提高了3.27%的PSNR。

## 🔬 方法详解

**问题定义**：本文旨在解决现有3D高斯点云（3DGS）方法在稀疏视图场景中因高斯权重处理相同而导致的过拟合问题，影响渲染效果。

**核心思路**：通过引入学习的不确定性，本文提出自适应加权高斯的方法，能够在保持3DGS管道完整性的同时，优化高斯的透明度更新和丢弃策略。

**技术框架**：整体架构包括两个主要模块：首先是高斯的不确定性学习模块，其次是基于不确定性的软丢弃正则化模块。这两个模块协同工作，提升渲染质量。

**关键创新**：本文的主要创新在于将学习的不确定性引入到高斯的加权和丢弃策略中，显著区别于传统方法的均匀加权方式，提升了稀疏视图下的渲染效果。

**关键设计**：在参数设置上，采用了基于不确定性的连续丢弃概率，并设计了相应的损失函数以优化高斯的透明度更新，确保了模型的可微性和渲染质量的提升。

## 📊 实验亮点

实验结果表明，本文方法在多个广泛采用的数据集上均优于现有稀疏视图方法，尤其在MipNeRF 360数据集上相比DropGaussian实现了3.27%的PSNR提升，显示了显著的性能优势。

## 🎯 应用场景

该研究在新视图合成、计算机视觉和图形学等领域具有广泛的应用潜力。通过提升稀疏视图下的渲染质量，能够为虚拟现实、增强现实以及影视特效等应用提供更高效的解决方案，推动相关技术的发展和应用。

## 📄 摘要（原文）

> 3D Gaussian Splatting (3DGS) has become a competitive approach for novel view synthesis (NVS) due to its advanced rendering efficiency through 3D Gaussian projection and blending. However, Gaussians are treated equally weighted for rendering in most 3DGS methods, making them prone to overfitting, which is particularly the case in sparse-view scenarios. To address this, we investigate how adaptive weighting of Gaussians affects rendering quality, which is characterised by learned uncertainties proposed. This learned uncertainty serves two key purposes: first, it guides the differentiable update of Gaussian opacity while preserving the 3DGS pipeline integrity; second, the uncertainty undergoes soft differentiable dropout regularisation, which strategically transforms the original uncertainty into continuous drop probabilities that govern the final Gaussian projection and blending process for rendering. Extensive experimental results over widely adopted datasets demonstrate that our method outperforms rivals in sparse-view 3D synthesis, achieving higher quality reconstruction with fewer Gaussians in most datasets compared to existing sparse-view approaches, e.g., compared to DropGaussian, our method achieves 3.27\% PSNR improvements on the MipNeRF 360 dataset.

