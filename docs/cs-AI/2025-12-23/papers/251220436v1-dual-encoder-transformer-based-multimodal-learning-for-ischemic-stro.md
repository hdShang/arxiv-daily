---
layout: default
title: Dual-Encoder Transformer-Based Multimodal Learning for Ischemic Stroke Lesion Segmentation Using Diffusion MRI
---

# Dual-Encoder Transformer-Based Multimodal Learning for Ischemic Stroke Lesion Segmentation Using Diffusion MRI

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20436" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20436v1</a>
  <a href="https://arxiv.org/pdf/2512.20436.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20436v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20436v1', 'Dual-Encoder Transformer-Based Multimodal Learning for Ischemic Stroke Lesion Segmentation Using Diffusion MRI')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Muhammad Usman, Azka Rehman, Muhammad Mutti Ur Rehman, Abd Ur Rehman, Muhammad Umar Farooq

**分类**: eess.IV, cs.AI, cs.CV

**发布日期**: 2025-12-23

---

## 💡 一句话要点

**提出基于双编码器Transformer的Ischemic Stroke病灶分割方法，提升DWI和ADC图像的分割精度。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `缺血性卒中` `病灶分割` `弥散磁共振成像` `Transformer` `双编码器` `多模态学习` `TransUNet`

## 📋 核心要点

1. 缺血性卒中病灶分割是临床决策的关键，但DWI和ADC图像的病灶外观差异大，自动分割面临挑战。
2. 论文提出一种双编码器TransUNet架构，分别学习DWI和ADC的模态特定表示，并结合相邻切片信息。
3. 实验结果表明，该方法优于卷积和传统Transformer模型，在ISLES 2022数据集上Dice系数达到85.4%。

## 📝 摘要（中文）

本研究针对弥散磁共振成像(MRI)中缺血性卒中病灶的精确分割问题，该分割对于临床决策和结果评估至关重要。弥散加权成像(DWI)和表观弥散系数(ADC)扫描提供了关于急性和亚急性缺血性变化的互补信息。然而，由于病灶外观的多样性，自动病灶描绘仍然具有挑战性。本研究利用ISLES 2022数据集，探索了基于多模态弥散MRI的缺血性卒中病灶分割。对包括U-Net变体、Swin-UNet和TransUNet在内的几种最先进的卷积和基于Transformer的架构进行了基准测试。基于性能，提出了一种双编码器TransUNet架构，以学习来自DWI和ADC输入的模态特定表示。为了整合空间上下文，使用三切片输入配置集成了相邻切片信息。所有模型都在统一框架下进行训练，并使用Dice相似系数(DSC)进行评估。结果表明，基于Transformer的模型优于卷积基线，并且所提出的双编码器TransUNet实现了最佳性能，在测试集上达到了85.4%的Dice分数。该框架为基于弥散MRI的自动缺血性卒中病灶分割提供了一个鲁棒的解决方案。

## 🔬 方法详解

**问题定义**：论文旨在解决缺血性卒中病灶在弥散MRI图像（DWI和ADC）上的自动精确分割问题。现有方法，如传统的卷积神经网络（CNN）和一些Transformer网络，在处理病灶外观多样性和模态信息融合方面存在局限性，导致分割精度不高。

**核心思路**：论文的核心思路是利用双编码器TransUNet架构，分别对DWI和ADC两种模态的图像进行特征提取，学习模态特定的表示。同时，为了更好地利用空间上下文信息，将相邻切片的信息融入到模型输入中，从而提高分割的准确性。

**技术框架**：整体框架基于TransUNet，包含两个独立的编码器分支和一个共享的解码器。每个编码器分支负责提取对应模态（DWI或ADC）的特征。编码器采用Transformer结构，能够捕捉长距离依赖关系。解码器将两个编码器的特征融合，并逐步恢复空间分辨率，最终输出分割结果。此外，模型输入采用三切片配置，即当前切片及其相邻的两个切片，以提供更丰富的空间上下文信息。

**关键创新**：该方法最重要的创新点在于采用了双编码器结构，能够针对DWI和ADC两种模态的特点，学习更具判别性的特征表示。与单编码器结构相比，双编码器能够更好地捕捉不同模态之间的互补信息，从而提高分割精度。

**关键设计**：模型使用了Transformer作为编码器的核心组件，利用自注意力机制捕捉长距离依赖关系。输入数据采用三切片配置，以提供空间上下文信息。损失函数未知，但通常会采用Dice Loss或Cross-Entropy Loss等分割任务常用的损失函数。具体的Transformer参数设置（如层数、头数等）未知。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20436v1/Figures/implementationscheme.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20436v1/Figures/dualencoder1slice.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20436v1/Figures/duaencoder3slice.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，所提出的双编码器TransUNet在ISLES 2022数据集上取得了最佳性能，Dice系数达到了85.4%。相比于传统的卷积神经网络（如U-Net及其变体）和单编码器TransUNet，该方法在分割精度上有了显著提升，证明了双编码器结构和模态特定特征学习的有效性。

## 🎯 应用场景

该研究成果可应用于临床辅助诊断，帮助医生更准确、快速地分割缺血性卒中病灶，从而制定更有效的治疗方案。此外，该技术还可用于卒中患者的预后评估和疗效监测，具有重要的临床应用价值。未来，该方法可以推广到其他脑部疾病的病灶分割任务中。

## 📄 摘要（原文）

> Accurate segmentation of ischemic stroke lesions from diffusion magnetic resonance imaging (MRI) is essential for clinical decision-making and outcome assessment. Diffusion-Weighted Imaging (DWI) and Apparent Diffusion Coefficient (ADC) scans provide complementary information on acute and sub-acute ischemic changes; however, automated lesion delineation remains challenging due to variability in lesion appearance.
>   In this work, we study ischemic stroke lesion segmentation using multimodal diffusion MRI from the ISLES 2022 dataset. Several state-of-the-art convolutional and transformer-based architectures, including U-Net variants, Swin-UNet, and TransUNet, are benchmarked. Based on performance, a dual-encoder TransUNet architecture is proposed to learn modality-specific representations from DWI and ADC inputs. To incorporate spatial context, adjacent slice information is integrated using a three-slice input configuration.
>   All models are trained under a unified framework and evaluated using the Dice Similarity Coefficient (DSC). Results show that transformer-based models outperform convolutional baselines, and the proposed dual-encoder TransUNet achieves the best performance, reaching a Dice score of 85.4% on the test set. The proposed framework offers a robust solution for automated ischemic stroke lesion segmentation from diffusion MRI.

