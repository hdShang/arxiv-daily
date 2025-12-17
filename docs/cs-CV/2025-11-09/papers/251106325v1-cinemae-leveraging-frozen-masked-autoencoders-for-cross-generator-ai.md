---
layout: default
title: CINEMAE: Leveraging Frozen Masked Autoencoders for Cross-Generator AI Image Detection
---

# CINEMAE: Leveraging Frozen Masked Autoencoders for Cross-Generator AI Image Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.06325" class="toolbar-btn" target="_blank">📄 arXiv: 2511.06325v1</a>
  <a href="https://arxiv.org/pdf/2511.06325.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.06325v1" onclick="toggleFavorite(this, '2511.06325v1', 'CINEMAE: Leveraging Frozen Masked Autoencoders for Cross-Generator AI Image Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Minsuk Jang, Hyeonseo Jeong, Minseok Son, Changick Kim

**分类**: cs.CV, cs.AI, cs.CY

**发布日期**: 2025-11-09

---

## 💡 一句话要点

**CINEMAE：利用冻结的掩码自编码器进行跨生成器AI图像检测**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `AIGC图像检测` `掩码自编码器` `跨生成器泛化` `语义一致性` `负对数似然`

## 📋 核心要点

1. 现有基于上下文的检测器在AI生成文本方面表现出色，但基于图像的检测器容易过拟合于特定生成器的伪影。
2. CINEMAE利用掩码自编码器(MAE)重建图像块的能力，通过计算条件负对数似然来量化局部语义异常。
3. 实验表明，CINEMAE在跨生成器泛化方面表现出色，仅在Stable Diffusion v1.4上训练，在GenImage基准测试中取得了显著的性能提升。

## 📝 摘要（中文）

本文提出了一种新的AIGC图像检测范式CINEMAE，它将文本检测方法的核心原则应用于视觉领域。核心思想是，掩码自编码器(MAE)在可见上下文的条件下重建被掩盖的图像块，从而自然地编码了语义一致性期望。论文将这个重建过程形式化为概率问题，计算条件负对数似然(NLL, p(masked \| visible))来量化局部语义异常。通过学习融合这些patch级别的统计信息和全局MAE特征，CINEMAE实现了强大的跨生成器泛化能力。仅在Stable Diffusion v1.4上训练，该方法在GenImage基准测试中的所有八个未见过的生成器上都达到了95%以上的准确率，大大优于最先进的检测器。这表明，上下文条件重建不确定性为AIGC检测提供了一个鲁棒的、可转移的信号。

## 🔬 方法详解

**问题定义**：现有AIGC图像检测方法容易过拟合于特定生成器的伪影，导致跨生成器的泛化能力较差。它们难以捕捉到不同生成器之间共享的、更本质的AI生成图像的特征。因此，需要一种能够提取与生成器无关的、更通用的AIGC图像特征的检测方法。

**核心思路**：论文的核心思路是利用掩码自编码器(MAE)的重建能力来衡量图像的语义一致性。MAE在训练过程中学习了图像的上下文信息，能够根据可见的图像块来预测被掩盖的图像块。如果图像是AI生成的，那么MAE的重建误差可能会更大，因为AI生成的图像可能存在语义上的不一致性。通过量化这种重建误差，可以有效地检测AI生成的图像。

**技术框架**：CINEMAE的整体框架包括以下几个主要模块：1) 使用预训练的冻结MAE提取图像特征；2) 计算每个图像块的条件负对数似然(NLL)作为局部语义异常的度量；3) 将patch级别的NLL统计信息与全局MAE特征进行融合；4) 使用一个学习到的融合模块（例如，MLP）来预测图像是否为AI生成。

**关键创新**：CINEMAE的关键创新在于将MAE的重建能力应用于AIGC图像检测，并利用条件负对数似然来量化局部语义异常。与以往依赖于生成器特定伪影的检测方法不同，CINEMAE关注的是图像的语义一致性，从而实现了更好的跨生成器泛化能力。

**关键设计**：论文使用了预训练的MAE模型，并将其参数冻结，以避免过拟合于特定生成器。条件负对数似然(NLL)的计算是基于MAE的重建误差，具体来说，就是计算被掩盖的图像块的真实像素值与MAE预测值之间的交叉熵损失。融合模块可以使用简单的多层感知机(MLP)来实现，其输入是patch级别的NLL统计信息和全局MAE特征，输出是图像为AI生成的概率。

## 📊 实验亮点

CINEMAE在GenImage基准测试中表现出色，仅使用Stable Diffusion v1.4进行训练，在八个未见过的生成器上实现了超过95%的准确率。与最先进的检测器相比，CINEMAE在跨生成器泛化能力方面取得了显著的提升，证明了其方法的有效性和鲁棒性。

## 🎯 应用场景

CINEMAE可应用于检测社交媒体、新闻网站等平台上的AI生成图像，以防止虚假信息的传播和恶意内容的生成。该技术还有助于保护知识产权，防止未经授权的AI生成图像被用于商业用途。此外，该研究可以促进对AI生成图像的安全性和伦理问题的进一步研究。

## 📄 摘要（原文）

> While context-based detectors have achieved strong generalization for AI-generated text by measuring distributional inconsistencies, image-based detectors still struggle with overfitting to generator-specific artifacts. We introduce CINEMAE, a novel paradigm for AIGC image detection that adapts the core principles of text detection methods to the visual domain. Our key insight is that Masked AutoEncoder (MAE), trained to reconstruct masked patches conditioned on visible context, naturally encodes semantic consistency expectations. We formalize this reconstruction process probabilistically, computing conditional Negative Log-Likelihood (NLL, p(masked \| visible)) to quantify local semantic anomalies. By aggregating these patch-level statistics with global MAE features through learned fusion, CINEMAE achieves strong cross-generator generalization. Trained exclusively on Stable Diffusion v1.4, our method achieves over 95% accuracy on all eight unseen generators in the GenImage benchmark, substantially outperforming state-of-the-art detectors. This demonstrates that context-conditional reconstruction uncertainty provides a robust, transferable signal for AIGC detection.

