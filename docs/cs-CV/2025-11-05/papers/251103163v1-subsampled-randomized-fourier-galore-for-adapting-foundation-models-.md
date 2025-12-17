---
layout: default
title: Subsampled Randomized Fourier GaLore for Adapting Foundation Models in Depth-Driven Liver Landmark Segmentation
---

# Subsampled Randomized Fourier GaLore for Adapting Foundation Models in Depth-Driven Liver Landmark Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.03163" class="toolbar-btn" target="_blank">📄 arXiv: 2511.03163v1</a>
  <a href="https://arxiv.org/pdf/2511.03163.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.03163v1" onclick="toggleFavorite(this, '2511.03163v1', 'Subsampled Randomized Fourier GaLore for Adapting Foundation Models in Depth-Driven Liver Landmark Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yun-Chen Lin, Jiayuan Huang, Hanyuan Zhang, Sergi Kavtaradze, Matthew J. Clarkson, Mobarak I. Hoque

**分类**: cs.CV

**发布日期**: 2025-11-05

**备注**: 12 pages

---

## 💡 一句话要点

**提出SRFT-GaLore，用于深度驱动的肝脏地标分割中高效自适应基础模型。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `肝脏地标分割` `深度学习` `腹腔镜手术` `SRFT-GaLore` `深度信息融合` `医学影像分析` `自适应基础模型`

## 📋 核心要点

1. 腹腔镜肝脏手术中，2D视频流限制了深度感知，使得地标定位变得复杂，现有方法难以有效融合RGB和深度特征。
2. 提出一种深度引导的肝脏地标分割框架，利用SAM2和DA2提取RGB和深度特征，并引入SRFT-GaLore高效微调SAM2。
3. 在L3D数据集上，Dice相似系数提升4.85%，平均对称表面距离减少11.78个点，并在LLSD数据集上表现出强大的跨数据集鲁棒性。

## 📝 摘要（中文）

本文提出了一种深度引导的肝脏地标分割框架，该框架通过视觉基础编码器整合语义和几何线索。利用Segment Anything Model V2 (SAM2) 编码器提取RGB特征，Depth Anything V2 (DA2) 编码器提取深度感知特征。为了高效地自适应SAM2，引入了SRFT-GaLore，一种新颖的低秩梯度投影方法，用Subsampled Randomized Fourier Transform (SRFT) 替代了计算成本高的SVD。这使得能够高效地微调高维注意力层，而不会牺牲表征能力。一个交叉注意力融合模块进一步整合了RGB和深度线索。为了评估跨数据集的泛化能力，构建了一个新的腹腔镜肝脏手术数据集(LLSD)作为外部验证基准。在公开的L3D数据集上，该方法在Dice相似系数上实现了4.85%的提升，在平均对称表面距离上减少了11.78个点。在LLSD数据集上的评估表明，该模型保持了竞争性的性能，并显著优于基于SAM的基线，证明了其强大的跨数据集鲁棒性和对未见手术环境的适应性。

## 🔬 方法详解

**问题定义**：在腹腔镜肝脏手术中，精确检测和分割解剖结构至关重要。然而，2D视频流缺乏深度信息，使得地标定位成为一项挑战。现有方法在融合RGB和深度特征以及将大规模视觉模型高效地适应手术领域方面存在不足，计算成本高昂，泛化能力有限。

**核心思路**：本文的核心思路是利用深度信息来增强肝脏地标的分割性能。通过结合RGB图像的语义信息和深度图像的几何信息，可以更准确地定位和分割肝脏地标。此外，通过引入SRFT-GaLore，可以高效地微调大规模视觉模型，使其适应手术领域，同时保持模型的表征能力。

**技术框架**：该框架包含以下主要模块：1) 使用Segment Anything Model V2 (SAM2) 编码器提取RGB特征；2) 使用Depth Anything V2 (DA2) 编码器提取深度感知特征；3) 使用SRFT-GaLore高效微调SAM2；4) 使用交叉注意力融合模块整合RGB和深度线索；5) 使用分割头进行肝脏地标分割。整体流程是先分别提取RGB和深度特征，然后通过SRFT-GaLore高效微调SAM2，再通过交叉注意力融合特征，最后进行分割。

**关键创新**：最重要的技术创新点是SRFT-GaLore，它是一种新颖的低秩梯度投影方法，用Subsampled Randomized Fourier Transform (SRFT) 替代了计算成本高的SVD。与现有方法的本质区别在于，SRFT-GaLore可以在不牺牲表征能力的情况下，高效地微调高维注意力层，从而降低计算成本，提高训练效率。

**关键设计**：SRFT-GaLore的关键设计在于使用Subsampled Randomized Fourier Transform (SRFT) 来近似SVD。具体来说，SRFT通过随机采样和傅里叶变换来降低计算复杂度，同时保留了SVD的主要信息。交叉注意力融合模块的关键设计在于使用注意力机制来动态地调整RGB和深度特征的权重，从而更好地融合两种模态的信息。损失函数采用Dice Loss和交叉熵损失的组合，以提高分割精度。

## 📊 实验亮点

在公开的L3D数据集上，该方法在Dice相似系数上实现了4.85%的提升，在平均对称表面距离上减少了11.78个点，显著优于D2GPLand。在LLSD数据集上的评估表明，该模型保持了竞争性的性能，并显著优于基于SAM的基线，证明了其强大的跨数据集鲁棒性和对未见手术环境的适应性。

## 🎯 应用场景

该研究成果可应用于计算机辅助腹腔镜肝脏手术，提高手术精度和效率，减少手术风险。通过精确的地标分割，医生可以更好地规划手术路径，避免损伤重要血管和组织。此外，该方法还可以推广到其他医学影像分割任务中，例如肿瘤分割、器官分割等，具有广泛的应用前景。

## 📄 摘要（原文）

> Accurate detection and delineation of anatomical structures in medical imaging are critical for computer-assisted interventions, particularly in laparoscopic liver surgery where 2D video streams limit depth perception and complicate landmark localization. While recent works have leveraged monocular depth cues for enhanced landmark detection, challenges remain in fusing RGB and depth features and in efficiently adapting large-scale vision models to surgical domains. We propose a depth-guided liver landmark segmentation framework integrating semantic and geometric cues via vision foundation encoders. We employ Segment Anything Model V2 (SAM2) encoder to extract RGB features and Depth Anything V2 (DA2) encoder to extract depth-aware features. To efficiently adapt SAM2, we introduce SRFT-GaLore, a novel low-rank gradient projection method that replaces the computationally expensive SVD with a Subsampled Randomized Fourier Transform (SRFT). This enables efficient fine-tuning of high-dimensional attention layers without sacrificing representational power. A cross-attention fusion module further integrates RGB and depth cues. To assess cross-dataset generalization, we also construct a new Laparoscopic Liver Surgical Dataset (LLSD) as an external validation benchmark. On the public L3D dataset, our method achieves a 4.85% improvement in Dice Similarity Coefficient and a 11.78-point reduction in Average Symmetric Surface Distance compared to the D2GPLand. To further assess generalization capability, we evaluate our model on LLSD dataset. Our model maintains competitive performance and significantly outperforms SAM-based baselines, demonstrating strong cross-dataset robustness and adaptability to unseen surgical environments. These results demonstrate that our SRFT-GaLore-enhanced dual-encoder framework enables scalable and precise segmentation under real-time, depth-constrained surgical settings.

