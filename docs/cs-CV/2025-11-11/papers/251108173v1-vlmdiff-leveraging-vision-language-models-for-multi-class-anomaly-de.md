---
layout: default
title: VLMDiff: Leveraging Vision-Language Models for Multi-Class Anomaly Detection with Diffusion
---

# VLMDiff: Leveraging Vision-Language Models for Multi-Class Anomaly Detection with Diffusion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.08173" class="toolbar-btn" target="_blank">📄 arXiv: 2511.08173v1</a>
  <a href="https://arxiv.org/pdf/2511.08173.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.08173v1" onclick="toggleFavorite(this, '2511.08173v1', 'VLMDiff: Leveraging Vision-Language Models for Multi-Class Anomaly Detection with Diffusion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Samet Hicsonmez, Abd El Rahman Shabayek, Djamila Aouada

**分类**: cs.CV

**发布日期**: 2025-11-11

**备注**: WACV 2026

**🔗 代码/项目**: [GITHUB](https://github.com/giddyyupp/VLMDiff)

---

## 💡 一句话要点

**VLMDiff：利用视觉-语言模型和扩散模型进行多类别异常检测**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `视觉异常检测` `扩散模型` `视觉-语言模型` `无监督学习` `多类别分类`

## 📋 核心要点

1. 现有基于扩散的异常检测方法依赖合成噪声，泛化性受限，且需针对每个类别单独训练模型，扩展性差。
2. VLMDiff利用预训练的视觉-语言模型提取图像描述，作为扩散模型的条件，学习正常图像的鲁棒特征表示。
3. 实验表明，VLMDiff在Real-IAD和COCO-AD数据集上显著提升了像素级异常检测性能，优于现有扩散方法。

## 📝 摘要（中文）

本文提出了一种名为VLMDiff的新型无监督多类别视觉异常检测框架。该框架集成了潜在扩散模型（LDM）和视觉-语言模型（VLM），以增强异常定位和检测能力。具体而言，利用预训练的VLM通过简单的提示提取详细的图像描述，作为LDM训练的额外条件。与当前依赖合成噪声生成的扩散方法不同，VLMDiff利用VLM获取正常图像的描述，无需手动标注或额外训练，从而避免了泛化性问题和每个类别单独训练的需求。这些描述用于调节扩散模型，学习鲁棒的正常图像特征表示，以进行多类别异常检测。实验结果表明，该方法具有竞争力的性能，在Real-IAD数据集上，像素级区域重叠度（PRO）指标提升高达25个点，在COCO-AD数据集上提升8个点，优于最先进的基于扩散的方法。

## 🔬 方法详解

**问题定义**：论文旨在解决多类别真实世界图像中的视觉异常检测问题。现有基于扩散模型的异常检测方法通常依赖于合成噪声的生成，这限制了模型的泛化能力。此外，这些方法通常需要针对每个类别单独训练模型，这使得它们在处理多类别问题时缺乏可扩展性。

**核心思路**：VLMDiff的核心思路是利用预训练的视觉-语言模型（VLM）来获取正常图像的文本描述，并将这些描述作为潜在扩散模型（LDM）的额外条件。通过这种方式，模型可以学习到更鲁棒的正常图像特征表示，从而提高异常检测的准确性和泛化能力。

**技术框架**：VLMDiff的整体框架包括以下几个主要步骤：1) 使用预训练的VLM（例如CLIP）提取输入图像的文本描述；2) 将这些文本描述作为条件输入到LDM中；3) LDM学习正常图像的分布；4) 在推理阶段，通过比较输入图像与LDM重建图像之间的差异来检测异常。

**关键创新**：VLMDiff的关键创新在于利用VLM来获取图像的文本描述，从而避免了手动标注或额外训练的需要。这使得该方法能够更有效地处理多类别异常检测问题，并提高了模型的泛化能力。与传统的基于扩散模型的方法相比，VLMDiff不需要生成合成噪声，而是直接利用真实图像的文本描述来指导模型的训练。

**关键设计**：VLMDiff的关键设计包括：1) 使用预训练的CLIP模型作为VLM，以提取高质量的图像描述；2) 将文本描述嵌入到LDM的潜在空间中，作为额外的条件；3) 使用均方误差（MSE）作为损失函数，以衡量输入图像与LDM重建图像之间的差异。

## 📊 实验亮点

VLMDiff在Real-IAD和COCO-AD数据集上取得了显著的性能提升。在Real-IAD数据集上，像素级区域重叠度（PRO）指标提升高达25个点，在COCO-AD数据集上提升8个点。这些结果表明，VLMDiff优于现有的基于扩散模型的异常检测方法，具有很强的竞争力。

## 🎯 应用场景

VLMDiff可应用于工业质检、医疗影像分析、自动驾驶等领域。在工业质检中，可用于检测产品表面的缺陷；在医疗影像分析中，可用于辅助医生诊断疾病；在自动驾驶中，可用于检测道路上的异常物体。该研究具有重要的实际价值，有望提高相关领域的自动化水平和效率。

## 📄 摘要（原文）

> Detecting visual anomalies in diverse, multi-class real-world images is a significant challenge. We introduce \ours, a novel unsupervised multi-class visual anomaly detection framework. It integrates a Latent Diffusion Model (LDM) with a Vision-Language Model (VLM) for enhanced anomaly localization and detection. Specifically, a pre-trained VLM with a simple prompt extracts detailed image descriptions, serving as additional conditioning for LDM training. Current diffusion-based methods rely on synthetic noise generation, limiting their generalization and requiring per-class model training, which hinders scalability. \ours, however, leverages VLMs to obtain normal captions without manual annotations or additional training. These descriptions condition the diffusion model, learning a robust normal image feature representation for multi-class anomaly detection. Our method achieves competitive performance, improving the pixel-level Per-Region-Overlap (PRO) metric by up to 25 points on the Real-IAD dataset and 8 points on the COCO-AD dataset, outperforming state-of-the-art diffusion-based approaches. Code is available at https://github.com/giddyyupp/VLMDiff.

