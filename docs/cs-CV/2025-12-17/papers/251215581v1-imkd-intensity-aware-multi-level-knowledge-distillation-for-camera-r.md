---
layout: default
title: IMKD: Intensity-Aware Multi-Level Knowledge Distillation for Camera-Radar Fusion
---

# IMKD: Intensity-Aware Multi-Level Knowledge Distillation for Camera-Radar Fusion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15581" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15581v1</a>
  <a href="https://arxiv.org/pdf/2512.15581.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15581v1" onclick="toggleFavorite(this, '2512.15581v1', 'IMKD: Intensity-Aware Multi-Level Knowledge Distillation for Camera-Radar Fusion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shashank Mishra, Karan Patil, Didier Stricker, Jason Rambach

**分类**: cs.CV, cs.LG

**发布日期**: 2025-12-17

**备注**: Accepted at IEEE/CVF Winter Conference on Applications of Computer Vision (WACV) 2026. 22 pages, 8 figures. Includes supplementary material

**🔗 代码/项目**: [GITHUB](https://github.com/dfki-av/IMKD/)

---

## 💡 一句话要点

**提出IMKD，通过强度感知多层知识蒸馏提升雷达-相机融合3D目标检测性能。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `雷达相机融合` `知识蒸馏` `3D目标检测` `自动驾驶` `多模态学习`

## 📋 核心要点

1. 现有知识蒸馏方法直接将模态特定特征传递给每个传感器，可能扭曲其独特性并降低其优势。
2. IMKD通过强度感知的多层知识蒸馏，在保留传感器特性的同时，增强雷达和相机之间的互补优势。
3. 在nuScenes数据集上，IMKD的NDS达到67.0%，mAP达到61.0%，超越了现有的基于知识蒸馏的雷达相机融合方法。

## 📝 摘要（中文）

本文提出了一种名为IMKD的雷达-相机融合框架，该框架基于多层知识蒸馏，旨在保留每个传感器固有的特性，同时增强它们的互补优势。IMKD采用三阶段、强度感知的蒸馏策略，以丰富整个架构中的融合表示：（1）LiDAR到雷达的强度感知特征蒸馏，以增强雷达表示的细粒度结构线索；（2）LiDAR到融合特征的强度引导蒸馏，有选择地突出融合层面的有用几何和深度信息，促进模态之间的互补性，而不是强制对齐；（3）相机-雷达强度引导融合机制，促进有效的特征对齐和校准。在nuScenes基准上的大量实验表明，IMKD达到了67.0%的NDS和61.0%的mAP，优于所有先前的基于蒸馏的雷达-相机融合方法。代码和模型已公开。

## 🔬 方法详解

**问题定义**：现有的雷达-相机融合方法在进行知识蒸馏时，通常直接将LiDAR的特征迁移到雷达和相机分支，这可能导致模态特定信息的损失，降低了各个传感器的独立性能。因此，如何有效地利用LiDAR的知识，同时保留雷达和相机各自的优势，是一个关键问题。

**核心思路**：IMKD的核心思路是采用强度感知的多层知识蒸馏策略，有选择地将LiDAR的知识传递给雷达和融合特征，从而增强雷达的结构信息，并促进雷达和相机之间的互补性。通过强度信息引导特征蒸馏，可以更加关注重要的几何和深度信息，避免强制对齐不同模态的特征。

**技术框架**：IMKD框架包含三个主要阶段：（1）LiDAR-to-Radar强度感知特征蒸馏：利用LiDAR的强度信息，增强雷达特征的结构信息。（2）LiDAR-to-Fused特征强度引导蒸馏：利用LiDAR的强度信息，选择性地突出融合层面的几何和深度信息。（3）相机-雷达强度引导融合机制：促进相机和雷达特征的有效对齐和校准。整体架构旨在保留每个传感器的固有特性，同时增强它们的互补优势。

**关键创新**：IMKD的关键创新在于强度感知的多层知识蒸馏策略。与传统的直接特征蒸馏不同，IMKD利用强度信息来引导特征的传递，从而更加关注重要的结构和几何信息。这种方法可以有效地增强雷达的结构信息，并促进雷达和相机之间的互补性。

**关键设计**：在LiDAR-to-Radar蒸馏中，使用强度信息作为权重，来指导雷达特征的学习，使得雷达特征更加关注LiDAR中强度较高的区域，从而增强雷达对结构信息的感知能力。在LiDAR-to-Fused蒸馏中，同样使用强度信息来选择性地突出融合层面的几何和深度信息，避免强制对齐不同模态的特征。相机-雷达强度引导融合机制，通过强度信息来指导特征的对齐和校准，从而提高融合效果。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15581v1/figures/KD_Comparison_2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15581v1/figures/IMKD_Arch_1.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15581v1/figures/Intensity_Aware_LiRa.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

IMKD在nuScenes数据集上取得了显著的性能提升，NDS达到67.0%，mAP达到61.0%，超越了所有现有的基于知识蒸馏的雷达相机融合方法。这些结果表明，IMKD的强度感知多层知识蒸馏策略能够有效地提升雷达-相机融合的3D目标检测性能。

## 🎯 应用场景

IMKD在自动驾驶领域具有广泛的应用前景，可以提升雷达-相机融合的3D目标检测性能，从而提高自动驾驶系统的感知能力和安全性。此外，该方法也可以应用于机器人、智能交通等领域，提升多传感器融合系统的性能。

## 📄 摘要（原文）

> High-performance Radar-Camera 3D object detection can be achieved by leveraging knowledge distillation without using LiDAR at inference time. However, existing distillation methods typically transfer modality-specific features directly to each sensor, which can distort their unique characteristics and degrade their individual strengths. To address this, we introduce IMKD, a radar-camera fusion framework based on multi-level knowledge distillation that preserves each sensor's intrinsic characteristics while amplifying their complementary strengths. IMKD applies a three-stage, intensity-aware distillation strategy to enrich the fused representation across the architecture: (1) LiDAR-to-Radar intensity-aware feature distillation to enhance radar representations with fine-grained structural cues, (2) LiDAR-to-Fused feature intensity-guided distillation to selectively highlight useful geometry and depth information at the fusion level, fostering complementarity between the modalities rather than forcing them to align, and (3) Camera-Radar intensity-guided fusion mechanism that facilitates effective feature alignment and calibration. Extensive experiments on the nuScenes benchmark show that IMKD reaches 67.0% NDS and 61.0% mAP, outperforming all prior distillation-based radar-camera fusion methods. Our code and models are available at https://github.com/dfki-av/IMKD/.

