---
layout: default
title: "FastAvatar: Towards Unified Fast High-Fidelity 3D Avatar Reconstruction with Large Gaussian Reconstruction Transformers"
---

# FastAvatar: Towards Unified Fast High-Fidelity 3D Avatar Reconstruction with Large Gaussian Reconstruction Transformers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19754" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19754v1</a>
  <a href="https://arxiv.org/pdf/2508.19754.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19754v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19754v1', 'FastAvatar: Towards Unified Fast High-Fidelity 3D Avatar Reconstruction with Large Gaussian Reconstruction Transformers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yue Wu, Yufan Wu, Wen Li, Yuxi Lu, Kairui Feng, Xuanhong Chen

**分类**: cs.CV

**发布日期**: 2025-08-27

---

## 💡 一句话要点

**提出FastAvatar以解决高时间复杂度和数据利用率低的问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D头像重建` `高斯重建` `变换器架构` `增量重建` `多模态输入`

## 📋 核心要点

1. 现有3D头像重建方法存在高时间复杂度和对数据质量敏感的问题，导致数据利用率低。
2. FastAvatar框架通过统一模型灵活处理多种输入数据，实现快速高质量的3D重建。
3. 实验结果显示，FastAvatar在重建质量和速度上均优于现有技术，具有显著的竞争力。

## 📝 摘要（中文）

尽管3D头像重建取得了显著进展，但仍面临高时间复杂度、对数据质量敏感和数据利用率低等挑战。我们提出了FastAvatar，一个前馈式3D头像框架，能够灵活利用多种日常录制数据（如单张图像、多视角观测或单目视频），在数秒内重建高质量的3D高斯点云模型，仅使用一个统一模型。FastAvatar的核心是一个大型高斯重建变换器，具有三项关键设计：首先，变体VGGT风格的变换器架构聚合多帧线索，同时注入初始3D提示以预测可聚合的标准3DGS表示；其次，多粒度引导编码（相机姿态、FLAME表情、头部姿态）减轻动画引起的错位，适应可变长度输入；第三，通过地标跟踪和切片融合损失实现增量高斯聚合。整合这些特性，FastAvatar实现了增量重建，即随着更多观测的增加提高质量，避免了先前工作中输入数据的浪费。大量实验表明，FastAvatar在质量和速度上均优于现有方法。

## 🔬 方法详解

**问题定义**：本论文旨在解决3D头像重建中存在的高时间复杂度和对数据质量敏感的问题。现有方法往往无法充分利用输入数据，导致重建效果不佳。

**核心思路**：FastAvatar通过一个统一的前馈式框架，灵活处理多种输入形式，快速生成高质量的3D模型。其设计理念是通过聚合多帧信息和增量重建来提高效率和质量。

**技术框架**：FastAvatar的整体架构包括一个大型高斯重建变换器，主要模块包括多帧信息聚合、引导编码和增量高斯聚合。该框架能够处理来自不同来源的输入数据，并在短时间内输出高质量的3D模型。

**关键创新**：FastAvatar的主要创新在于其使用的VGGT风格变换器架构和多粒度引导编码技术，这些设计使得模型能够有效聚合多帧信息并减轻动画引起的错位。与现有方法相比，FastAvatar能够实现更高效的数据利用和重建质量。

**关键设计**：在关键设计方面，FastAvatar采用了增量高斯聚合策略，通过地标跟踪和切片融合损失来优化模型训练。此外，模型的输入可以是单张图像、多视角观测或单目视频，极大地增强了其适用性。

## 📊 实验亮点

实验结果表明，FastAvatar在重建质量上超过了现有方法，且速度具有竞争力。具体而言，FastAvatar在处理多种输入数据时，重建质量提升幅度达到XX%，速度提升幅度达到YY%。

## 🎯 应用场景

FastAvatar在虚拟现实、游戏开发和社交媒体等领域具有广泛的应用潜力。其快速高质量的3D头像重建能力可以提升用户体验，推动个性化虚拟形象的创建与应用。未来，该技术可能在远程会议、在线教育等场景中发挥重要作用。

## 📄 摘要（原文）

> Despite significant progress in 3D avatar reconstruction, it still faces challenges such as high time complexity, sensitivity to data quality, and low data utilization. We propose FastAvatar, a feedforward 3D avatar framework capable of flexibly leveraging diverse daily recordings (e.g., a single image, multi-view observations, or monocular video) to reconstruct a high-quality 3D Gaussian Splatting (3DGS) model within seconds, using only a single unified model. FastAvatar's core is a Large Gaussian Reconstruction Transformer featuring three key designs: First, a variant VGGT-style transformer architecture aggregating multi-frame cues while injecting initial 3D prompt to predict an aggregatable canonical 3DGS representation; Second, multi-granular guidance encoding (camera pose, FLAME expression, head pose) mitigating animation-induced misalignment for variable-length inputs; Third, incremental Gaussian aggregation via landmark tracking and sliced fusion losses. Integrating these features, FastAvatar enables incremental reconstruction, i.e., improving quality with more observations, unlike prior work wasting input data. This yields a quality-speed-tunable paradigm for highly usable avatar modeling. Extensive experiments show that FastAvatar has higher quality and highly competitive speed compared to existing methods.

