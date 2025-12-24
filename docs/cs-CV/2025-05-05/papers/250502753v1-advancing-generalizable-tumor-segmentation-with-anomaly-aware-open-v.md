---
layout: default
title: Advancing Generalizable Tumor Segmentation with Anomaly-Aware Open-Vocabulary Attention Maps and Frozen Foundation Diffusion Models
---

# Advancing Generalizable Tumor Segmentation with Anomaly-Aware Open-Vocabulary Attention Maps and Frozen Foundation Diffusion Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02753" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02753v1</a>
  <a href="https://arxiv.org/pdf/2505.02753.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02753v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02753v1', 'Advancing Generalizable Tumor Segmentation with Anomaly-Aware Open-Vocabulary Attention Maps and Frozen Foundation Diffusion Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yankai Jiang, Peng Zhang, Donglin Yang, Yuan Tian, Hai Lin, Xiaosong Wang

**分类**: cs.CV

**发布日期**: 2025-05-05

**备注**: This paper is accepted to CVPR 2025

**🔗 代码/项目**: [GITHUB](https://github.com/Yankai96/DiffuGTS)

---

## 💡 一句话要点

**提出DiffuGTS以解决肿瘤分割的通用性问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `肿瘤分割` `零-shot学习` `医学影像` `扩散模型` `异常检测` `深度学习` `图像处理`

## 📋 核心要点

1. 现有的肿瘤分割方法在分割质量和适用性上存在显著不足，难以实现跨解剖区域的通用性。
2. 本研究提出DiffuGTS框架，利用冻结的医学扩散模型和异常感知开放词汇注意力图，实现高效的零-shot肿瘤分割。
3. 在四个数据集和七种肿瘤类别的实验中，DiffuGTS的表现超越了现有最先进模型，显示出显著的性能提升。

## 📝 摘要（中文）

本论文探讨了通用肿瘤分割，旨在训练一个单一模型实现零-shot肿瘤分割，适用于多种解剖区域。现有方法在分割质量、可扩展性和适用成像模态方面存在局限。我们提出了一种新框架DiffuGTS，利用冻结的医学基础扩散模型的内部表示作为高效的零-shot学习器，通过基于文本提示的异常感知开放词汇注意力图实现通用异常分割。此外，DiffuGTS通过潜在空间修复将病理区域转化为高质量的伪健康对应物，并应用新颖的像素级和特征级残差学习方法，显著提升分割掩膜的质量和泛化能力。综合实验表明，我们的方法在多个零-shot设置下超越了当前最先进的模型。

## 🔬 方法详解

**问题定义**：本论文旨在解决肿瘤分割的通用性问题，现有方法在不同解剖区域的适用性和分割质量上存在局限，无法实现有效的零-shot学习。

**核心思路**：我们提出的DiffuGTS框架利用冻结的医学基础扩散模型的内部表示，结合异常感知开放词汇注意力图，允许模型在没有预定义类别的情况下进行异常分割。

**技术框架**：DiffuGTS的整体架构包括两个主要模块：首先是基于文本提示生成的开放词汇注意力图，其次是通过潜在空间修复技术生成高质量的伪健康图像，最终通过残差学习提升分割效果。

**关键创新**：DiffuGTS的创新在于其利用冻结扩散模型的内部表示作为零-shot学习器，并引入异常感知的开放词汇注意力图，突破了传统方法的限制。

**关键设计**：在模型设计中，我们采用了像素级和特征级的残差学习方法，优化了损失函数和网络结构，以确保分割掩膜的高质量和泛化能力。通过这些设计，DiffuGTS在多个数据集上表现出色。

## 📊 实验亮点

在四个数据集和七种肿瘤类别的实验中，DiffuGTS的性能显著优于当前最先进的模型，特别是在零-shot设置下，分割质量提升幅度达到XX%（具体数据待补充），展示了其强大的通用性和适应性。

## 🎯 应用场景

该研究的潜在应用领域包括医学影像分析、肿瘤检测与诊断等。通过实现高效的零-shot肿瘤分割，DiffuGTS能够帮助医生在不同解剖区域快速识别肿瘤，提高诊断效率和准确性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> We explore Generalizable Tumor Segmentation, aiming to train a single model for zero-shot tumor segmentation across diverse anatomical regions. Existing methods face limitations related to segmentation quality, scalability, and the range of applicable imaging modalities. In this paper, we uncover the potential of the internal representations within frozen medical foundation diffusion models as highly efficient zero-shot learners for tumor segmentation by introducing a novel framework named DiffuGTS. DiffuGTS creates anomaly-aware open-vocabulary attention maps based on text prompts to enable generalizable anomaly segmentation without being restricted by a predefined training category list. To further improve and refine anomaly segmentation masks, DiffuGTS leverages the diffusion model, transforming pathological regions into high-quality pseudo-healthy counterparts through latent space inpainting, and applies a novel pixel-level and feature-level residual learning approach, resulting in segmentation masks with significantly enhanced quality and generalization. Comprehensive experiments on four datasets and seven tumor categories demonstrate the superior performance of our method, surpassing current state-of-the-art models across multiple zero-shot settings. Codes are available at https://github.com/Yankai96/DiffuGTS.

