---
layout: default
title: "DM-FNet: Unified multimodal medical image fusion via diffusion process-trained encoder-decoder"
---

# DM-FNet: Unified multimodal medical image fusion via diffusion process-trained encoder-decoder

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15218" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15218v1</a>
  <a href="https://arxiv.org/pdf/2506.15218.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15218v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15218v1', 'DM-FNet: Unified multimodal medical image fusion via diffusion process-trained encoder-decoder')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dan He, Weisheng Li, Guofen Wang, Yuping Huang, Shiqiang Liu

**分类**: cs.CV

**发布日期**: 2025-06-18

**备注**: This paper has been accepted by IEEE Transactions on Multimedia (TMM) in March 2025

**🔗 代码/项目**: [GITHUB](https://github.com/HeDan-11/DM-FNet)

---

## 💡 一句话要点

**提出DM-FNet以解决多模态医学图像融合质量不足的问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态医学图像融合` `扩散模型` `UNet` `图像重建` `特征交互` `医学影像学` `深度学习`

## 📋 核心要点

1. 现有多模态医学图像融合方法在细节特征捕捉和跨模态特征交互方面存在不足，导致融合图像质量不理想。
2. 本研究提出DM-FNet，通过两阶段扩散模型训练UNet进行图像重建，增强特征表示能力，提升融合效果。
3. 实验结果显示，DM-FNet在多个医学图像类型上表现优异，融合图像在亮度、纹理和边缘清晰度等方面均有显著提升。

## 📝 摘要（中文）

多模态医学图像融合（MMIF）提取多源图像中最有意义的信息，从而实现更全面和准确的诊断。高质量的融合结果需要在亮度、颜色、对比度和细节之间进行精确平衡，以确保融合图像有效展示相关的解剖结构并反映组织的功能状态。然而，现有MMIF方法在常规训练中捕捉细节特征的能力有限，且跨模态特征交互不足，导致融合图像质量不理想。为了解决这些问题，本研究提出了一种基于扩散模型的两阶段融合网络DM-FNet，旨在实现统一的MMIF。实验结果表明，该方法在多种医学图像类型上表现优异，融合图像保持适当的亮度、丰富的纹理和清晰的边缘。

## 🔬 方法详解

**问题定义**：本论文旨在解决多模态医学图像融合（MMIF）中存在的细节特征捕捉不足和跨模态特征交互不充分的问题，导致融合图像质量不佳。

**核心思路**：提出DM-FNet，通过两阶段的扩散模型训练，首先重建图像以捕捉细节信息，然后在融合阶段增强特征识别能力，从而实现高质量的图像融合。

**技术框架**：DM-FNet的整体架构分为两个阶段：第一阶段使用扩散过程训练UNet进行图像重建，第二阶段将不同步骤的噪声图像输入融合网络，结合三个关键融合模块自适应处理不同模态的医学图像。

**关键创新**：该方法的创新点在于结合扩散模型与UNet架构，利用逐步去噪的方式捕捉多层次特征，并通过融合网络增强特征交互能力，显著提升了融合图像的质量。

**关键设计**：在设计中，采用了混合损失函数以协调融合图像的亮度、颜色、对比度和细节，同时集成了三个关键融合模块，以适应不同模态的医学图像处理需求。

## 📊 实验亮点

实验结果表明，DM-FNet在多个医学图像类型上的客观评估指标上表现优异，融合图像在亮度、放射性示踪剂分布、纹理丰富度和边缘清晰度等方面均有显著提升，展示了该方法的有效性和优越性。

## 🎯 应用场景

该研究具有广泛的应用潜力，尤其在医学影像学领域，可以用于提高不同模态医学图像的融合质量，从而辅助医生进行更准确的诊断和治疗决策。未来，该方法也可能扩展到其他领域，如多模态数据分析和计算机视觉等。

## 📄 摘要（原文）

> Multimodal medical image fusion (MMIF) extracts the most meaningful information from multiple source images, enabling a more comprehensive and accurate diagnosis. Achieving high-quality fusion results requires a careful balance of brightness, color, contrast, and detail; this ensures that the fused images effectively display relevant anatomical structures and reflect the functional status of the tissues. However, existing MMIF methods have limited capacity to capture detailed features during conventional training and suffer from insufficient cross-modal feature interaction, leading to suboptimal fused image quality. To address these issues, this study proposes a two-stage diffusion model-based fusion network (DM-FNet) to achieve unified MMIF. In Stage I, a diffusion process trains UNet for image reconstruction. UNet captures detailed information through progressive denoising and represents multilevel data, providing a rich set of feature representations for the subsequent fusion network. In Stage II, noisy images at various steps are input into the fusion network to enhance the model's feature recognition capability. Three key fusion modules are also integrated to process medical images from different modalities adaptively. Ultimately, the robust network structure and a hybrid loss function are integrated to harmonize the fused image's brightness, color, contrast, and detail, enhancing its quality and information density. The experimental results across various medical image types demonstrate that the proposed method performs exceptionally well regarding objective evaluation metrics. The fused image preserves appropriate brightness, a comprehensive distribution of radioactive tracers, rich textures, and clear edges. The code is available at https://github.com/HeDan-11/DM-FNet.

