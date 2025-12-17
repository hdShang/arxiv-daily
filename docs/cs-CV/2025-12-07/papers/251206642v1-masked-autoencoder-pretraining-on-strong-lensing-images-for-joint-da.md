---
layout: default
title: Masked Autoencoder Pretraining on Strong-Lensing Images for Joint Dark-Matter Model Classification and Super-Resolution
---

# Masked Autoencoder Pretraining on Strong-Lensing Images for Joint Dark-Matter Model Classification and Super-Resolution

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.06642" class="toolbar-btn" target="_blank">📄 arXiv: 2512.06642v1</a>
  <a href="https://arxiv.org/pdf/2512.06642.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.06642v1" onclick="toggleFavorite(this, '2512.06642v1', 'Masked Autoencoder Pretraining on Strong-Lensing Images for Joint Dark-Matter Model Classification and Super-Resolution')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Achmad Ardani Prasha, Clavino Ourizqi Rachmadi, Muhamad Fauzan Ibnu Syahlan, Naufal Rahfi Anugerah, Nanda Garin Raditya, Putri Amelia, Sabrina Laila Mutiara, Hilman Syachr Ramadhan

**分类**: cs.CV, astro-ph.CO, astro-ph.IM, cs.AI, cs.LG

**发布日期**: 2025-12-07

**备注**: 21 pages, 7 figures, 3 table

---

## 💡 一句话要点

**提出基于掩码自编码器的强引力透镜图像预训练方法，用于暗物质模型分类和超分辨率重建。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强引力透镜` `掩码自编码器` `预训练` `暗物质模型分类` `超分辨率` `Vision Transformer` `图像重建`

## 📋 核心要点

1. 分析低分辨率、高噪声的强引力透镜图像以揭示暗物质子结构的影响是一项挑战。
2. 利用掩码自编码器（MAE）在模拟的强引力透镜图像上进行预训练，学习可泛化的图像表示。
3. 实验表明，该方法在暗物质模型分类和超分辨率重建任务上均优于从头训练的模型。

## 📝 摘要（中文）

强引力透镜可以揭示星系中暗物质子结构的影响，但从噪声较大的低分辨率图像中分析这些影响极具挑战性。本文提出了一种基于掩码自编码器（MAE）的预训练策略，该策略在DeepLense ML4SCI基准测试中模拟的强引力透镜图像上进行，以学习可泛化的表示，用于两个下游任务：（i）对潜在的暗物质模型（冷暗物质、类轴子或无子结构）进行分类；（ii）通过超分辨率增强低分辨率透镜图像。我们使用掩码图像建模目标预训练Vision Transformer编码器，然后针对每个任务分别微调编码器。结果表明，MAE预训练与适当的掩码比例调整相结合，产生了一个共享编码器，其性能与从头开始训练的ViT相匹配或超过。具体而言，在90%的掩码比例下，微调后的分类器实现了0.968的宏平均AUC和88.65%的准确率，而从头开始训练的基线分别为0.957和82.46%。对于超分辨率（16x16到64x64），MAE预训练模型重建的图像的PSNR约为33 dB，SSIM为0.961，略优于从头开始训练。我们对MAE掩码比例进行了消融研究，揭示了一个一致的权衡：较高的掩码比例提高了分类性能，但略微降低了重建保真度。我们的研究结果表明，在富含物理信息的模拟数据上进行MAE预训练，为多个强引力透镜分析任务提供了一个灵活、可重用的编码器。

## 🔬 方法详解

**问题定义**：论文旨在解决从低分辨率、高噪声的强引力透镜图像中准确分类暗物质模型（冷暗物质、类轴子或无子结构）并进行超分辨率重建的问题。现有方法在处理此类图像时，由于图像质量差，特征提取困难，导致分类精度和重建质量不高。

**核心思路**：论文的核心思路是利用掩码自编码器（MAE）进行预训练，学习图像的通用表示。通过在大量模拟的强引力透镜图像上进行预训练，使模型能够捕捉到图像中的关键特征，从而提高下游任务的性能。掩码图像建模迫使模型理解图像的上下文信息，即使部分图像被遮盖也能进行重建，从而增强模型的鲁棒性。

**技术框架**：整体框架包括三个主要阶段：1) 使用模拟的强引力透镜图像数据集进行MAE预训练，训练一个Vision Transformer (ViT) 编码器。2) 将预训练的ViT编码器应用于两个下游任务：暗物质模型分类和超分辨率重建。3) 分别针对每个下游任务对编码器进行微调。对于分类任务，在编码器后添加分类头；对于超分辨率任务，使用解码器将编码器的输出映射到高分辨率图像。

**关键创新**：最重要的技术创新点在于将MAE预训练方法应用于强引力透镜图像分析。与传统的从头开始训练相比，MAE预训练能够学习到更具泛化能力的图像表示，从而提高下游任务的性能。此外，论文还研究了掩码比例对预训练效果的影响，发现适当的掩码比例可以提高分类性能，但可能会略微降低重建保真度。

**关键设计**：论文使用了Vision Transformer (ViT) 作为编码器，并采用了掩码图像建模作为预训练目标。关键参数包括掩码比例（mask ratio），实验表明90%的掩码比例在分类任务上表现最佳。损失函数方面，预训练阶段使用像素级别的均方误差（MSE）作为重建损失。在下游任务中，分类任务使用交叉熵损失，超分辨率任务使用PSNR和SSIM作为评价指标。

## 📊 实验亮点

实验结果表明，在90%的掩码比例下，MAE预训练的分类器在暗物质模型分类任务中实现了0.968的宏平均AUC和88.65%的准确率，显著优于从头开始训练的基线（AUC 0.957，准确率 82.46%）。对于超分辨率任务，MAE预训练模型重建的图像的PSNR约为33 dB，SSIM为0.961，略优于从头开始训练的模型。

## 🎯 应用场景

该研究成果可应用于天文图像处理、暗物质研究等领域。通过提高强引力透镜图像的分析精度，可以更准确地研究暗物质的性质和分布，从而加深我们对宇宙结构的理解。此外，该方法还可以推广到其他低分辨率、高噪声的图像处理任务中，例如医学图像分析。

## 📄 摘要（原文）

> Strong gravitational lensing can reveal the influence of dark-matter substructure in galaxies, but analyzing these effects from noisy, low-resolution images poses a significant challenge. In this work, we propose a masked autoencoder (MAE) pretraining strategy on simulated strong-lensing images from the DeepLense ML4SCI benchmark to learn generalizable representations for two downstream tasks: (i) classifying the underlying dark matter model (cold dark matter, axion-like, or no substructure) and (ii) enhancing low-resolution lensed images via super-resolution. We pretrain a Vision Transformer encoder using a masked image modeling objective, then fine-tune the encoder separately for each task. Our results show that MAE pretraining, when combined with appropriate mask ratio tuning, yields a shared encoder that matches or exceeds a ViT trained from scratch. Specifically, at a 90% mask ratio, the fine-tuned classifier achieves macro AUC of 0.968 and accuracy of 88.65%, compared to the scratch baseline (AUC 0.957, accuracy 82.46%). For super-resolution (16x16 to 64x64), the MAE-pretrained model reconstructs images with PSNR ~33 dB and SSIM 0.961, modestly improving over scratch training. We ablate the MAE mask ratio, revealing a consistent trade-off: higher mask ratios improve classification but slightly degrade reconstruction fidelity. Our findings demonstrate that MAE pretraining on physics-rich simulations provides a flexible, reusable encoder for multiple strong-lensing analysis tasks.

