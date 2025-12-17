---
layout: default
title: Towards Label-Free Brain Tumor Segmentation: Unsupervised Learning with Multimodal MRI
---

# Towards Label-Free Brain Tumor Segmentation: Unsupervised Learning with Multimodal MRI

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.15684" class="toolbar-btn" target="_blank">📄 arXiv: 2510.15684v1</a>
  <a href="https://arxiv.org/pdf/2510.15684.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.15684v1" onclick="toggleFavorite(this, '2510.15684v1', 'Towards Label-Free Brain Tumor Segmentation: Unsupervised Learning with Multimodal MRI')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gerard Comas-Quiles, Carles Garcia-Cabrera, Julia Dietlmeier, Noel E. O'Connor, Ferran Marques

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-17

**备注**: 10 pages, 5 figures, BraTS GoAT 2025 challenge

---

## 💡 一句话要点

**提出基于多模态MRI的无监督脑肿瘤分割方法，解决标注数据稀缺问题。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `脑肿瘤分割` `无监督学习` `多模态MRI` `Vision Transformer` `异常检测`

## 📋 核心要点

1. 脑肿瘤分割依赖大量标注数据，但标注成本高昂且数据不一致，限制了模型的泛化能力。
2. 提出一种基于多模态 Vision Transformer 自编码器的无监督异常检测方法，仅使用健康脑部 MRI 进行训练。
3. 实验结果表明，该方法在肿瘤定位方面具有临床意义，并在异常检测率上达到了 89.4% 的性能。

## 📝 摘要（中文）

本文提出了一种新颖的多模态 Vision Transformer 自编码器 (MViT-AE)，用于磁共振成像 (MRI) 中的无监督脑肿瘤分割。该模型仅在健康脑部 MRI 上训练，通过重建误差图检测和定位肿瘤。这种无监督范式无需人工标注即可实现分割，解决了神经影像工作流程中的关键可扩展性瓶颈。该方法在 BraTS-GoAT 2025 Lighthouse 数据集上进行了评估，该数据集包含多种类型的肿瘤，如神经胶质瘤、脑膜瘤和儿童脑肿瘤。为了提高性能，引入了一种多模态早晚融合策略，利用多个 MRI 序列中的互补信息，以及一个集成 Segment Anything Model (SAM) 的后处理流程来细化预测的肿瘤轮廓。尽管无监督异常检测存在挑战，尤其是在检测小型或非增强病灶方面，但该方法实现了具有临床意义的肿瘤定位，在测试集上病灶方面的 Dice 相似系数分别为 0.437 (全肿瘤)、0.316 (肿瘤核心) 和 0.350 (增强肿瘤)，在验证集上的异常检测率为 89.4%。这些发现突出了基于 Transformer 的无监督模型作为神经肿瘤成像的可扩展、标签高效工具的潜力。

## 🔬 方法详解

**问题定义**：脑肿瘤分割任务通常需要大量的标注数据进行监督学习，然而，获取高质量的脑肿瘤标注数据成本高昂，且不同机构或专家之间的标注可能存在差异，导致数据不一致性。这限制了模型的泛化能力和实际应用。

**核心思路**：本文的核心思路是利用无监督异常检测方法，通过学习健康脑部 MRI 的分布，将肿瘤区域视为异常。模型仅在健康数据上训练，学习正常脑组织的特征表示，当输入包含肿瘤的 MRI 时，模型无法准确重建肿瘤区域，从而通过重建误差图定位肿瘤。

**技术框架**：整体框架包括三个主要阶段：1) 多模态 MRI 数据输入；2) MViT-AE 模型训练和推理，生成重建误差图；3) 后处理，利用 SAM 模型细化肿瘤轮廓。MViT-AE 模型采用 Vision Transformer 结构，并结合了多模态早晚融合策略，以充分利用不同 MRI 序列的信息。

**关键创新**：该方法最重要的技术创新点在于利用 Vision Transformer 结构进行无监督异常检测，并结合多模态融合和 SAM 后处理，实现了在没有标注数据的情况下进行脑肿瘤分割。与传统的监督学习方法相比，该方法无需人工标注，具有更好的可扩展性和泛化能力。

**关键设计**：MViT-AE 模型采用 Vision Transformer 作为主干网络，并针对多模态 MRI 数据设计了早晚融合策略。早融合将不同模态的数据在输入层进行拼接，晚融合则在编码器输出层进行特征融合。损失函数采用均方误差 (MSE) 作为重建损失，用于衡量重建图像与原始图像之间的差异。后处理阶段，利用 SAM 模型对重建误差图进行分割，并根据临床经验设置阈值，以去除假阳性区域。

## 📊 实验亮点

该方法在 BraTS-GoAT 2025 Lighthouse 数据集上进行了评估，取得了具有竞争力的结果。在测试集上，全肿瘤、肿瘤核心和增强肿瘤的 Dice 相似系数分别为 0.437、0.316 和 0.350。在验证集上，异常检测率达到了 89.4%。这些结果表明，该方法在无监督脑肿瘤分割方面具有潜力。

## 🎯 应用场景

该研究成果可应用于临床辅助诊断，帮助医生快速定位脑肿瘤区域，尤其是在标注数据稀缺的情况下。此外，该方法还可以扩展到其他医学影像分析任务，例如病灶检测、器官分割等，具有广泛的应用前景。未来，可以进一步研究如何提高模型对小型或非增强病灶的检测能力，以及如何将该方法与临床信息相结合，以提高诊断的准确性。

## 📄 摘要（原文）

> Unsupervised anomaly detection (UAD) presents a complementary alternative to supervised learning for brain tumor segmentation in magnetic resonance imaging (MRI), particularly when annotated datasets are limited, costly, or inconsistent. In this work, we propose a novel Multimodal Vision Transformer Autoencoder (MViT-AE) trained exclusively on healthy brain MRIs to detect and localize tumors via reconstruction-based error maps. This unsupervised paradigm enables segmentation without reliance on manual labels, addressing a key scalability bottleneck in neuroimaging workflows. Our method is evaluated in the BraTS-GoAT 2025 Lighthouse dataset, which includes various types of tumors such as gliomas, meningiomas, and pediatric brain tumors. To enhance performance, we introduce a multimodal early-late fusion strategy that leverages complementary information across multiple MRI sequences, and a post-processing pipeline that integrates the Segment Anything Model (SAM) to refine predicted tumor contours. Despite the known challenges of UAD, particularly in detecting small or non-enhancing lesions, our method achieves clinically meaningful tumor localization, with lesion-wise Dice Similarity Coefficient of 0.437 (Whole Tumor), 0.316 (Tumor Core), and 0.350 (Enhancing Tumor) on the test set, and an anomaly Detection Rate of 89.4% on the validation set. These findings highlight the potential of transformer-based unsupervised models to serve as scalable, label-efficient tools for neuro-oncological imaging.

