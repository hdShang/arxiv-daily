---
layout: default
title: "DualPhys-GS: Dual Physically-Guided 3D Gaussian Splatting for Underwater Scene Reconstruction"
---

# DualPhys-GS: Dual Physically-Guided 3D Gaussian Splatting for Underwater Scene Reconstruction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09610" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09610v1</a>
  <a href="https://arxiv.org/pdf/2508.09610.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09610v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09610v1', 'DualPhys-GS: Dual Physically-Guided 3D Gaussian Splatting for Underwater Scene Reconstruction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiachen Li, Guangzhi Han, Jin Wan, Yuan Gao, Delong Han

**分类**: cs.GR

**发布日期**: 2025-08-13

**备注**: 12 pages, 4 figures

---

## 💡 一句话要点

**提出DualPhys-GS以解决水下场景重建中的光衰减与散射问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `水下重建` `光衰减` `散射建模` `特征引导` `深度学习` `多尺度处理` `机器人视觉`

## 📋 核心要点

1. 现有水下重建方法无法有效处理水中光衰减和散射，导致重建效果不佳。
2. 提出DualPhys-GS框架，通过双路径优化机制和双特征引导建模，提升水下重建质量。
3. 实验结果显示，该方法在悬浮物密集区域和长距离场景中显著优于现有技术。

## 📝 摘要（中文）

在水下场景的3D重建中，传统基于大气光学模型的方法无法有效处理水介质特有的光波长选择性衰减和悬浮颗粒散射，导致颜色失真、几何伪影和长距离崩溃现象。为此，我们提出了DualPhys-GS框架，通过双路径优化机制实现高质量的水下重建。该方法进一步发展了双特征引导的衰减-散射建模机制，结合RGB特征和深度信息的RGB引导衰减优化模型能够处理边缘和结构细节。同时，多尺度深度感知散射模型利用特征金字塔网络和注意力机制捕捉不同尺度的散射效应。实验结果表明，我们的方法在多个指标上优于现有方法，尤其是在悬浮物密集区域和长距离场景中，重建质量显著提高。

## 🔬 方法详解

**问题定义**：本论文旨在解决水下场景重建中由于光波长选择性衰减和悬浮颗粒散射导致的颜色失真和几何伪影等问题。现有方法在这些特性下表现不佳，尤其在长距离场景中容易出现崩溃现象。

**核心思路**：我们提出的DualPhys-GS框架通过双路径优化机制，结合RGB引导的衰减优化模型和多尺度深度感知散射模型，旨在提高水下重建的质量和准确性。这样的设计能够有效处理水下特有的光学特性，保持结构细节和边缘清晰度。

**技术框架**：该框架主要包括两个模块：RGB引导衰减优化模型和多尺度深度感知散射模型。前者结合RGB特征和深度信息，后者利用特征金字塔网络和注意力机制，捕捉不同尺度的散射效应。整体流程通过特定损失函数进行优化，确保物理一致性和结构清晰度。

**关键创新**：本研究的核心创新在于提出了双特征引导的衰减-散射建模机制，能够动态调整散射和衰减参数，适应不同水体类型的特征。这一机制显著提升了重建效果，尤其是在复杂水下环境中。

**关键设计**：我们设计了多种损失函数，包括衰减散射一致性损失、水体类型自适应损失、边缘感知散射损失和多尺度特征损失，以确保物理一致性、动态调整权重和保持结构边缘的清晰度。

## 📊 实验亮点

实验结果表明，DualPhys-GS方法在多个指标上超越了现有技术，尤其在悬浮物密集区域和长距离场景中，重建质量提升显著。具体性能数据未提供，但整体效果明显优于基线方法。

## 🎯 应用场景

该研究具有广泛的应用潜力，尤其在水下探测、海洋科学研究和水下机器人导航等领域。通过提高水下场景的重建质量，可以更好地支持水下环境的监测与分析，推动相关技术的发展与应用。

## 📄 摘要（原文）

> In 3D reconstruction of underwater scenes, traditional methods based on atmospheric optical models cannot effectively deal with the selective attenuation of light wavelengths and the effect of suspended particle scattering, which are unique to the water medium, and lead to color distortion, geometric artifacts, and collapsing phenomena at long distances. We propose the DualPhys-GS framework to achieve high-quality underwater reconstruction through a dual-path optimization mechanism. Our approach further develops a dual feature-guided attenuation-scattering modeling mechanism, the RGB-guided attenuation optimization model combines RGB features and depth information and can handle edge and structural details. In contrast, the multi-scale depth-aware scattering model captures scattering effects at different scales using a feature pyramid network and an attention mechanism. Meanwhile, we design several special loss functions. The attenuation scattering consistency loss ensures physical consistency. The water body type adaptive loss dynamically adjusts the weighting coefficients. The edge-aware scattering loss is used to maintain the sharpness of structural edges. The multi-scale feature loss helps to capture global and local structural information. In addition, we design a scene adaptive mechanism that can automatically identify the water-body-type characteristics (e.g., clear coral reef waters or turbid coastal waters) and dynamically adjust the scattering and attenuation parameters and optimization strategies. Experimental results show that our method outperforms existing methods in several metrics, especially in suspended matter-dense regions and long-distance scenes, and the reconstruction quality is significantly improved.

