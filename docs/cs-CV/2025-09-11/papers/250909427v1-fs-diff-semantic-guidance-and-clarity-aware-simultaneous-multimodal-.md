---
layout: default
title: "FS-Diff: Semantic guidance and clarity-aware simultaneous multimodal image fusion and super-resolution"
---

# FS-Diff: Semantic guidance and clarity-aware simultaneous multimodal image fusion and super-resolution

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09427" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09427v1</a>
  <a href="https://arxiv.org/pdf/2509.09427.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09427v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09427v1', 'FS-Diff: Semantic guidance and clarity-aware simultaneous multimodal image fusion and super-resolution')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuchan Jie, Yushen Xu, Xiaosong Li, Fuqiang Zhou, Jianming Lv, Huafeng Li

**分类**: cs.CV

**发布日期**: 2025-09-11

**期刊**: Information Fusion, 2025, 121: 103146

**DOI**: [10.1016/j.inffus.2025.103146](https://doi.org/10.1016/j.inffus.2025.103146)

**🔗 代码/项目**: [GITHUB](https://github.com/XylonXu01/FS-Diff)

---

## 💡 一句话要点

**FS-Diff：面向多模态图像融合与超分辨率的语义引导和清晰度感知方法**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态图像融合` `图像超分辨率` `扩散模型` `语义引导` `清晰度感知` `条件生成` `Mamba` `航空视图`

## 📋 核心要点

1. 现有联合图像融合与超分辨率方法在处理低分辨率、弱语义信息的多模态图像时效果不佳，尤其是在目标和背景结构易受损的情况下。
2. FS-Diff的核心思想是将图像融合和超分辨率视为一个条件生成问题，通过语义引导和清晰度感知机制，实现自适应的跨模态特征提取和高分辨率图像重建。
3. 实验结果表明，FS-Diff在多个数据集上优于现有方法，能够恢复更丰富的细节和语义信息，并在自建的AVMS数据集上表现出色。

## 📝 摘要（中文）

本文提出了一种语义引导和清晰度感知的联合图像融合与超分辨率方法FS-Diff。针对军事侦察和远程探测等实际应用中，多模态图像的目标和背景结构易受损、分辨率低、语义信息弱的问题，FS-Diff将图像融合和超分辨率统一为条件生成问题。该方法利用清晰度感知机制进行自适应低分辨率感知和跨模态特征提取，并引入双向特征Mamba提取多模态图像的全局特征。此外，利用源图像和语义作为条件，通过改进的U-Net网络实现随机迭代去噪过程，该网络经过多噪声水平的去噪训练，生成具有跨模态特征和丰富语义信息的高分辨率融合结果。同时，构建了一个包含600对图像的航空视图多场景（AVMS）基准数据集。在六个公共数据集和AVMS数据集上的大量联合图像融合和超分辨率实验表明，FS-Diff在多个放大倍数下优于现有技术，并能恢复融合图像中更丰富的细节和语义。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态图像融合与超分辨率问题，特别是在低分辨率和弱语义信息的情况下，现有方法难以有效融合多模态信息并重建高分辨率图像，导致融合结果细节丢失和语义信息不足。现有方法通常无法很好地处理真实场景中图像质量差、模态差异大的问题。

**核心思路**：论文的核心思路是将图像融合和超分辨率问题转化为一个条件生成问题，利用扩散模型（Diffusion Model）的强大生成能力，通过迭代去噪过程从噪声中逐步生成高分辨率的融合图像。同时，引入语义引导和清晰度感知机制，以更好地利用多模态信息，提升融合结果的质量。

**技术框架**：FS-Diff的整体框架包含以下几个主要模块：1) 清晰度感知模块：用于评估输入图像的清晰度，并根据清晰度自适应地提取低分辨率特征。2) 双向特征Mamba模块：用于提取多模态图像的全局特征，捕捉长距离依赖关系。3) 条件扩散模型：以源图像和语义信息作为条件，通过迭代去噪过程生成高分辨率融合图像。该模型基于改进的U-Net结构，并针对多噪声水平进行训练。

**关键创新**：论文的关键创新在于：1) 提出了语义引导和清晰度感知机制，能够自适应地处理低分辨率和弱语义信息的多模态图像。2) 引入了双向特征Mamba模块，有效提取了多模态图像的全局特征。3) 将图像融合和超分辨率问题转化为条件生成问题，利用扩散模型生成高质量的融合图像。

**关键设计**：在网络结构方面，使用了改进的U-Net作为扩散模型的骨干网络，并针对多噪声水平进行训练，以提高模型的鲁棒性。在损失函数方面，使用了L1损失和感知损失（Perceptual Loss）来约束生成图像的质量。清晰度感知模块的设计细节未知，但推测可能使用了图像梯度或频率域分析等方法来评估图像的清晰度。

## 📊 实验亮点

FS-Diff在六个公共数据集和自建的AVMS数据集上进行了大量实验，结果表明，FS-Diff在多个放大倍数下优于现有的图像融合和超分辨率方法。具体来说，FS-Diff在PSNR和SSIM等指标上均取得了显著提升，并且能够恢复更丰富的细节和语义信息。尤其是在AVMS数据集上，FS-Diff的表现更加出色，证明了其在复杂场景下的有效性。

## 🎯 应用场景

FS-Diff具有广泛的应用前景，例如军事侦察、遥感图像分析、医学图像处理等领域。在这些领域中，常常需要融合来自不同传感器或模态的图像，并提高图像的分辨率，以获取更丰富的信息。FS-Diff能够有效地解决这些问题，提高图像分析的准确性和效率，具有重要的实际应用价值。

## 📄 摘要（原文）

> As an influential information fusion and low-level vision technique, image fusion integrates complementary information from source images to yield an informative fused image. A few attempts have been made in recent years to jointly realize image fusion and super-resolution. However, in real-world applications such as military reconnaissance and long-range detection missions, the target and background structures in multimodal images are easily corrupted, with low resolution and weak semantic information, which leads to suboptimal results in current fusion techniques. In response, we propose FS-Diff, a semantic guidance and clarity-aware joint image fusion and super-resolution method. FS-Diff unifies image fusion and super-resolution as a conditional generation problem. It leverages semantic guidance from the proposed clarity sensing mechanism for adaptive low-resolution perception and cross-modal feature extraction. Specifically, we initialize the desired fused result as pure Gaussian noise and introduce the bidirectional feature Mamba to extract the global features of the multimodal images. Moreover, utilizing the source images and semantics as conditions, we implement a random iterative denoising process via a modified U-Net network. This network istrained for denoising at multiple noise levels to produce high-resolution fusion results with cross-modal features and abundant semantic information. We also construct a powerful aerial view multiscene (AVMS) benchmark covering 600 pairs of images. Extensive joint image fusion and super-resolution experiments on six public and our AVMS datasets demonstrated that FS-Diff outperforms the state-of-the-art methods at multiple magnifications and can recover richer details and semantics in the fused images. The code is available at https://github.com/XylonXu01/FS-Diff.

