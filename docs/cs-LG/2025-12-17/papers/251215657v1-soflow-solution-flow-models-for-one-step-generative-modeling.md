---
layout: default
title: SoFlow: Solution Flow Models for One-Step Generative Modeling
---

# SoFlow: Solution Flow Models for One-Step Generative Modeling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15657" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15657v1</a>
  <a href="https://arxiv.org/pdf/2512.15657.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15657v1" onclick="toggleFavorite(this, '2512.15657v1', 'SoFlow: Solution Flow Models for One-Step Generative Modeling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tianze Luo, Haotian Yuan, Zhuang Liu

**分类**: cs.LG, cs.CV

**发布日期**: 2025-12-17

**备注**: Our code is available at https://github.com/zlab-princeton/SoFlow

---

## 💡 一句话要点

**SoFlow：提出解决方案流模型，实现一步到位的生成建模，提升生成效率。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱四：生成式动作 (Generative Motion)**

**关键词**: `生成模型` `单步生成` `Flow Matching` `扩散模型` `图像生成` `无分类器引导` `解一致性` `速度场`

## 📋 核心要点

1. 扩散模型和Flow Matching模型的多步迭代过程是生成效率的主要瓶颈，限制了其在实际应用中的部署。
2. SoFlow通过分析速度ODE的解函数与速度函数关系，设计Flow Matching损失和解一致性损失，实现单步生成。
3. 实验表明，在ImageNet 256x256数据集上，SoFlow在相同训练条件下，FID-50K指标优于MeanFlow模型。

## 📝 摘要（中文）

扩散模型和Flow Matching模型中的多步去噪过程导致效率问题。本文提出了解决方案流模型（SoFlow），这是一个从头开始一步生成图像的框架。通过分析速度常微分方程（ODE）的速度函数和解函数之间的关系，我们提出了一个Flow Matching损失和一个解一致性损失来训练模型。Flow Matching损失允许模型在训练期间为无分类器引导（CFG）提供估计的速度场，从而提高生成性能。值得注意的是，我们的一致性损失不需要计算雅可比向量积（JVP），这是最近工作中常见的需求，但在PyTorch等深度学习框架中没有得到很好的优化。实验结果表明，在使用相同的Diffusion Transformer（DiT）架构和相同数量的训练epoch从头开始训练时，我们的模型在ImageNet 256x256数据集上实现了比MeanFlow模型更好的FID-50K分数。

## 🔬 方法详解

**问题定义**：现有扩散模型和Flow Matching模型依赖多步迭代的去噪过程进行图像生成，计算成本高昂，生成速度慢，难以满足实时性要求。因此，如何实现高效的单步图像生成是一个重要的研究问题。

**核心思路**：SoFlow的核心思想是直接学习速度常微分方程（ODE）的解，从而实现从噪声到图像的单步转换。通过建立速度场和解之间的直接关系，模型可以直接预测给定噪声对应的图像，无需迭代去噪。

**技术框架**：SoFlow框架主要包含以下几个部分：1) 一个神经网络模型，用于预测速度场；2) Flow Matching损失，用于训练模型预测准确的速度场；3) 解一致性损失，用于确保预测的解与速度场一致。训练过程中，模型接收随机噪声作为输入，预测对应的速度场和图像。Flow Matching损失和解一致性损失共同驱动模型学习单步生成的能力。

**关键创新**：SoFlow的关键创新在于：1) 提出了一种新的单步生成框架，避免了多步迭代过程；2) 设计了一种不需要计算雅可比向量积（JVP）的解一致性损失，降低了计算复杂度，更易于在深度学习框架中实现；3) 利用Flow Matching损失为无分类器引导（CFG）提供速度场估计，提升生成质量。

**关键设计**：SoFlow的关键设计包括：1) 使用Diffusion Transformer (DiT) 作为基础网络架构；2) Flow Matching损失采用标准形式，鼓励模型学习准确的速度场；3) 解一致性损失通过约束预测解与速度场的一致性，避免了JVP计算；4) 训练过程中，采用无分类器引导（CFG）策略，提升生成图像的多样性和质量。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15657v1/figures/teaser.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15657v1/x1.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15657v1/x2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

SoFlow在ImageNet 256x256数据集上取得了显著的实验结果。在相同的训练条件下（DiT架构，相同训练epoch），SoFlow的FID-50K分数优于MeanFlow模型，表明其在单步生成任务上的有效性。这一结果验证了SoFlow框架的优越性，并为高效图像生成提供了新的思路。

## 🎯 应用场景

SoFlow具有广泛的应用前景，包括图像生成、视频生成、3D内容生成等。其单步生成特性使其在需要实时生成内容的场景中具有优势，例如游戏、虚拟现实、增强现实等。此外，SoFlow还可以应用于图像编辑、图像修复等任务，提高效率和用户体验。未来，SoFlow有望成为一种通用的生成建模方法，推动相关领域的发展。

## 📄 摘要（原文）

> The multi-step denoising process in diffusion and Flow Matching models causes major efficiency issues, which motivates research on few-step generation. We present Solution Flow Models (SoFlow), a framework for one-step generation from scratch. By analyzing the relationship between the velocity function and the solution function of the velocity ordinary differential equation (ODE), we propose a Flow Matching loss and a solution consistency loss to train our models. The Flow Matching loss allows our models to provide estimated velocity fields for Classifier-Free Guidance (CFG) during training, which improves generation performance. Notably, our consistency loss does not require the calculation of the Jacobian-vector product (JVP), a common requirement in recent works that is not well-optimized in deep learning frameworks like PyTorch. Experimental results indicate that, when trained from scratch using the same Diffusion Transformer (DiT) architecture and an equal number of training epochs, our models achieve better FID-50K scores than MeanFlow models on the ImageNet 256x256 dataset.

