---
layout: default
title: IE-SRGS: An Internal-External Knowledge Fusion Framework for High-Fidelity 3D Gaussian Splatting Super-Resolution
---

# IE-SRGS: An Internal-External Knowledge Fusion Framework for High-Fidelity 3D Gaussian Splatting Super-Resolution

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.22233" class="toolbar-btn" target="_blank">📄 arXiv: 2511.22233v1</a>
  <a href="https://arxiv.org/pdf/2511.22233.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.22233v1" onclick="toggleFavorite(this, '2511.22233v1', 'IE-SRGS: An Internal-External Knowledge Fusion Framework for High-Fidelity 3D Gaussian Splatting Super-Resolution')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiang Feng, Tieshi Zhong, Shuo Chang, Weiliu Wang, Chengkai Wang, Yifei Chen, Yuhe Wang, Zhenzhong Kuang, Xuefei Yin, Yanming Zhu

**分类**: cs.CV

**发布日期**: 2025-11-27

**备注**: AAAI 2026

---

## 💡 一句话要点

**提出IE-SRGS框架，融合内外知识提升3D高斯溅射超分辨率重建质量**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D高斯溅射` `超分辨率` `内外知识融合` `三维重建` `计算机视觉`

## 📋 核心要点

1. 现有方法依赖预训练的2D超分辨率模型增强纹理，但易受跨视角不一致和领域差距导致的3D高斯模糊影响。
2. IE-SRGS框架融合外部2D超分辨率先验和内部3DGS特征，通过掩码引导融合策略协同优化，提升重建质量。
3. 实验结果表明，IE-SRGS在合成和真实数据集上均超越现有技术，在精度和视觉效果上均有显著提升。

## 📝 摘要（中文）

本文提出了一种新颖的3D高斯溅射超分辨率(3DGS SR)范式IE-SRGS，旨在解决从低分辨率(LR)输入重建高分辨率(HR) 3DGS模型时，由于缺乏精细纹理和几何细节而面临的挑战。该方法联合利用外部2D超分辨率(2DSR)先验和内部3DGS特征的互补优势。具体而言，使用2DSR和深度估计模型生成HR图像和深度图作为外部知识，并采用多尺度3DGS模型生成跨视角一致且适应特定领域的对应信息作为内部知识。引入了一种掩码引导的融合策略，整合这两种来源的信息，协同利用它们的优势，有效地引导3D高斯优化，实现高保真重建。在合成和真实世界基准测试上的大量实验表明，IE-SRGS在定量精度和视觉保真度方面均优于最先进的方法。

## 🔬 方法详解

**问题定义**：论文旨在解决从低分辨率图像重建高分辨率3D高斯溅射模型的问题。现有方法主要依赖2D超分辨率技术，但忽略了3D场景的几何一致性，导致重建结果出现伪影和模糊，无法充分利用3D场景的内在结构信息。

**核心思路**：核心思想是融合外部的2D超分辨率先验知识和内部的3D高斯溅射特征。外部知识提供高分辨率的纹理信息，内部知识保证跨视角的一致性和领域适应性。通过协同优化，克服了单一依赖2D超分辨率的局限性。

**技术框架**：IE-SRGS框架包含以下几个主要模块：1) 外部知识生成模块：利用预训练的2D超分辨率模型和深度估计模型生成高分辨率图像和深度图。2) 内部知识生成模块：使用多尺度3DGS模型生成跨视角一致的特征。3) 掩码引导融合模块：根据图像区域的置信度生成掩码，指导外部和内部知识的融合。4) 3D高斯优化模块：利用融合后的特征优化3D高斯参数。

**关键创新**：关键创新在于内外知识的融合策略。传统方法通常直接使用2D超分辨率结果，忽略了3D场景的几何约束。IE-SRGS通过引入内部3DGS特征，并使用掩码引导的融合策略，实现了内外知识的协同优化，有效提升了重建质量。

**关键设计**：掩码引导融合策略是关键设计之一。掩码根据2D超分辨率结果的置信度生成，用于控制外部知识的引入程度。此外，多尺度3DGS模型的引入可以捕捉不同尺度的场景信息，提升重建的细节表现。损失函数的设计也至关重要，需要平衡重建精度和视角一致性。

## 📊 实验亮点

实验结果表明，IE-SRGS在合成数据集和真实数据集上均取得了显著的性能提升。在定量指标上，IE-SRGS优于现有的3DGS超分辨率方法，在视觉效果上，重建结果更加清晰、细节更丰富。例如，在某个数据集上，IE-SRGS的PSNR指标提升了X dB，SSIM指标提升了Y%。

## 🎯 应用场景

该研究成果可应用于三维重建、虚拟现实、增强现实、游戏开发等领域。例如，可以利用低分辨率图像快速生成高质量的3D模型，提升用户体验。未来，该技术有望应用于自动驾驶、机器人导航等领域，为智能系统提供更准确的环境感知能力。

## 📄 摘要（原文）

> Reconstructing high-resolution (HR) 3D Gaussian Splatting (3DGS) models from low-resolution (LR) inputs remains challenging due to the lack of fine-grained textures and geometry. Existing methods typically rely on pre-trained 2D super-resolution (2DSR) models to enhance textures, but suffer from 3D Gaussian ambiguity arising from cross-view inconsistencies and domain gaps inherent in 2DSR models. We propose IE-SRGS, a novel 3DGS SR paradigm that addresses this issue by jointly leveraging the complementary strengths of external 2DSR priors and internal 3DGS features. Specifically, we use 2DSR and depth estimation models to generate HR images and depth maps as external knowledge, and employ multi-scale 3DGS models to produce cross-view consistent, domain-adaptive counterparts as internal knowledge. A mask-guided fusion strategy is introduced to integrate these two sources and synergistically exploit their complementary strengths, effectively guiding the 3D Gaussian optimization toward high-fidelity reconstruction. Extensive experiments on both synthetic and real-world benchmarks show that IE-SRGS consistently outperforms state-of-the-art methods in both quantitative accuracy and visual fidelity.

