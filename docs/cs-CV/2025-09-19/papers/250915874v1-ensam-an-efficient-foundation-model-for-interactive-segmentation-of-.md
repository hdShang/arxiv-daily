---
layout: default
title: "ENSAM: an efficient foundation model for interactive segmentation of 3D medical images"
---

# ENSAM: an efficient foundation model for interactive segmentation of 3D medical images

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15874" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15874v1</a>
  <a href="https://arxiv.org/pdf/2509.15874.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15874v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15874v1', 'ENSAM: an efficient foundation model for interactive segmentation of 3D medical images')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Elias Stenhede, Agnar Martin Bjørnstad, Arian Ranjbar

**分类**: cs.CV

**发布日期**: 2025-09-19

---

## 💡 一句话要点

**ENSAM：一种高效的三维医学图像交互分割基础模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `三维医学图像分割` `交互式分割` `基础模型` `轻量级模型` `深度学习`

## 📋 核心要点

1. 现有的三维医学图像分割方法通常需要大量的标注数据和计算资源，限制了其在数据稀缺和计算资源有限场景下的应用。
2. ENSAM通过结合SegResNet编码器、提示编码器和掩码解码器，并引入相对位置编码和归一化注意力等机制，实现了高效的三维医学图像交互分割。
3. 实验结果表明，ENSAM在有限的数据和计算资源下，能够优于或匹配现有的基线模型，并且相对位置编码和Muon优化器能够显著提升性能。

## 📝 摘要（中文）

本文提出了一种轻量级的、可提示的通用三维医学图像分割模型ENSAM（Equivariant, Normalized, Segment Anything Model）。ENSAM结合了基于SegResNet的编码器、提示编码器和掩码解码器，采用U-Net风格的架构，并使用潜在交叉注意力、相对位置编码、归一化注意力和Muon优化器进行训练。ENSAM旨在在有限的数据和计算预算下实现良好的性能，仅使用来自多种模态（CT、MRI、PET、超声、显微镜）的不到5000个volume，在单个32 GB GPU上于6小时内从头开始训练。在CVPR 2025 Foundation Models for Interactive 3D Biomedical Image Segmentation Challenge中，ENSAM在多模态三维医学图像的隐藏测试集上进行了评估，获得了2.404的DSC AUC、2.266的NSD AUC、0.627的最终DSC和0.597的最终NSD，优于之前发表的两个基线模型（VISTA3D、SAM-Med3D），并与第三个模型（SegVol）相匹配，在最终DSC方面超过了SegVol，但在其他三个指标上落后。在挑战赛的coreset track中，ENSAM在总共10个方法中排名第5，并且是在未使用预训练权重的方法中表现最佳的。消融研究证实，我们使用的相对位置编码和Muon优化器都显著加快了收敛速度并提高了分割质量。

## 🔬 方法详解

**问题定义**：三维医学图像分割旨在从三维医学图像中准确地分割出感兴趣的组织或器官。现有的方法通常依赖于大量的标注数据和强大的计算资源，这在实际应用中是一个挑战，尤其是在数据获取困难或计算资源有限的情况下。此外，如何有效地利用用户交互信息（例如，提示）来指导分割过程也是一个重要的研究问题。

**核心思路**：ENSAM的核心思路是设计一个轻量级、可提示的分割模型，使其能够在有限的数据和计算资源下实现良好的分割性能。通过结合SegResNet编码器、提示编码器和掩码解码器，并引入相对位置编码和归一化注意力等机制，ENSAM能够有效地利用图像信息和用户提示信息，从而实现准确的分割。

**技术框架**：ENSAM采用U-Net风格的架构，主要包含以下几个模块：1) SegResNet编码器：用于提取三维医学图像的特征；2) 提示编码器：用于编码用户提供的提示信息（例如，点或框）；3) 掩码解码器：用于生成分割掩码。这些模块通过潜在交叉注意力机制进行连接，从而实现图像特征和提示信息的融合。

**关键创新**：ENSAM的关键创新点在于其轻量级的设计和对用户提示信息的有效利用。与现有的方法相比，ENSAM能够在有限的数据和计算资源下实现具有竞争力的性能，并且能够通过用户交互来指导分割过程。此外，相对位置编码和归一化注意力的引入也显著提升了模型的性能。

**关键设计**：ENSAM的关键设计包括：1) 使用SegResNet作为编码器，以提取有效的图像特征；2) 引入相对位置编码，以更好地捕捉空间信息；3) 使用归一化注意力，以提高模型的鲁棒性；4) 使用Muon优化器进行训练，以加快收敛速度；5) 通过潜在交叉注意力机制融合图像特征和提示信息。

## 📊 实验亮点

ENSAM在CVPR 2025 Foundation Models for Interactive 3D Biomedical Image Segmentation Challenge中取得了优异的成绩，在隐藏测试集上获得了2.404的DSC AUC、2.266的NSD AUC、0.627的最终DSC和0.597的最终NSD，优于之前发表的两个基线模型（VISTA3D、SAM-Med3D），并在最终DSC方面超过了SegVol。消融研究表明，相对位置编码和Muon优化器能够显著提升性能。

## 🎯 应用场景

ENSAM具有广泛的应用前景，例如辅助医生进行疾病诊断、手术规划和治疗评估。该模型可以应用于多种医学影像模态，例如CT、MRI、PET和超声，从而实现对不同组织和器官的分割。此外，ENSAM的轻量级设计使其能够在移动设备或嵌入式系统上部署，从而实现床旁诊断和远程医疗。

## 📄 摘要（原文）

> We present ENSAM (Equivariant, Normalized, Segment Anything Model), a lightweight and promptable model for universal 3D medical image segmentation. ENSAM combines a SegResNet-based encoder with a prompt encoder and mask decoder in a U-Net-style architecture, using latent cross-attention, relative positional encoding, normalized attention, and the Muon optimizer for training. ENSAM is designed to achieve good performance under limited data and computational budgets, and is trained from scratch on under 5,000 volumes from multiple modalities (CT, MRI, PET, ultrasound, microscopy) on a single 32 GB GPU in 6 hours. As part of the CVPR 2025 Foundation Models for Interactive 3D Biomedical Image Segmentation Challenge, ENSAM was evaluated on hidden test set with multimodal 3D medical images, obtaining a DSC AUC of 2.404, NSD AUC of 2.266, final DSC of 0.627, and final NSD of 0.597, outperforming two previously published baseline models (VISTA3D, SAM-Med3D) and matching the third (SegVol), surpassing its performance in final DSC but trailing behind in the other three metrics. In the coreset track of the challenge, ENSAM ranks 5th of 10 overall and best among the approaches not utilizing pretrained weights. Ablation studies confirm that our use of relative positional encodings and the Muon optimizer each substantially speed up convergence and improve segmentation quality.

