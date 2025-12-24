---
layout: default
title: "Uni3R: Unified 3D Reconstruction and Semantic Understanding via Generalizable Gaussian Splatting from Unposed Multi-View Images"
---

# Uni3R: Unified 3D Reconstruction and Semantic Understanding via Generalizable Gaussian Splatting from Unposed Multi-View Images

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03643" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03643v3</a>
  <a href="https://arxiv.org/pdf/2508.03643.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03643v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03643v3', 'Uni3R: Unified 3D Reconstruction and Semantic Understanding via Generalizable Gaussian Splatting from Unposed Multi-View Images')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiangyu Sun, Haoyi Jiang, Liu Liu, Seungtae Nam, Gyeongjin Kang, Xinjie Wang, Wei Sui, Zhizhong Su, Wenyu Liu, Xinggang Wang, Eunbyung Park

**分类**: cs.CV

**发布日期**: 2025-08-05 (更新: 2025-08-11)

**备注**: The code is available at https://github.com/HorizonRobotics/Uni3R

**🔗 代码/项目**: [GITHUB](https://github.com/HorizonRobotics/Uni3R)

---

## 💡 一句话要点

**提出Uni3R以解决无姿态多视图图像的3D重建与语义理解问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D重建` `语义理解` `多视图图像` `高斯原语` `跨视图变换器` `开放词汇` `计算机视觉`

## 📋 核心要点

1. 现有方法通常将3D重建与语义理解分开，导致可扩展性和通用性不足。
2. Uni3R通过跨视图变换器整合多视图信息，联合重建3D场景并进行语义理解。
3. 实验结果显示，Uni3R在RE10K和ScanNet等基准上取得了显著的性能提升。

## 📝 摘要（中文）

从稀疏的2D视图重建和语义解释3D场景仍然是计算机视觉中的一个基本挑战。传统方法通常将语义理解与重建分离，或需要昂贵的逐场景优化，从而限制了它们的可扩展性和通用性。本文提出了Uni3R，一种新颖的前馈框架，能够从无姿态的多视图图像中联合重建统一的3D场景表示，并丰富开放词汇语义。该方法利用跨视图变换器有效整合任意多视图输入的信息，回归一组带有语义特征场的3D高斯原语。这种统一表示促进了高保真新视图合成、开放词汇3D语义分割和深度预测，所有这些都在单个前馈过程中完成。大量实验表明，Uni3R在多个基准上建立了新的最先进水平，包括RE10K上的25.07 PSNR和ScanNet上的55.84 mIoU。

## 🔬 方法详解

**问题定义**：本文旨在解决从无姿态多视图图像中重建3D场景及其语义理解的问题。现有方法往往将重建与语义理解分开，导致效率低下和可扩展性不足。

**核心思路**：Uni3R的核心思路是通过一个前馈框架，利用跨视图变换器有效整合多视图信息，直接回归带有语义特征的3D高斯原语，从而实现3D重建与语义理解的统一。

**技术框架**：Uni3R的整体架构包括多个模块：首先，跨视图变换器接收多视图输入，整合信息；然后，通过回归网络生成3D高斯原语；最后，利用生成的统一表示进行新视图合成、语义分割和深度预测。

**关键创新**：Uni3R的主要创新在于其将3D重建与开放词汇语义理解结合在一个前馈框架中，克服了传统方法的局限性，实现了更高的效率和准确性。

**关键设计**：在设计中，Uni3R采用了特定的损失函数以优化语义特征的学习，并使用了高效的网络结构来处理多视图输入，确保了模型的高效性和准确性。

## 📊 实验亮点

Uni3R在多个基准测试中表现出色，RE10K上达到25.07 PSNR，ScanNet上达到55.84 mIoU，均创下新的最先进水平，显示出其在3D重建和语义理解领域的显著优势。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、虚拟现实、增强现实等场景，其中需要从多视角图像中快速重建3D环境并进行语义分析。其实际价值在于提升了3D重建的效率和准确性，未来可能推动相关技术的广泛应用。

## 📄 摘要（原文）

> Reconstructing and semantically interpreting 3D scenes from sparse 2D views remains a fundamental challenge in computer vision. Conventional methods often decouple semantic understanding from reconstruction or necessitate costly per-scene optimization, thereby restricting their scalability and generalizability. In this paper, we introduce Uni3R, a novel feed-forward framework that jointly reconstructs a unified 3D scene representation enriched with open-vocabulary semantics, directly from unposed multi-view images. Our approach leverages a Cross-View Transformer to robustly integrate information across arbitrary multi-view inputs, which then regresses a set of 3D Gaussian primitives endowed with semantic feature fields. This unified representation facilitates high-fidelity novel view synthesis, open-vocabulary 3D semantic segmentation, and depth prediction, all within a single, feed-forward pass. Extensive experiments demonstrate that Uni3R establishes a new state-of-the-art across multiple benchmarks, including 25.07 PSNR on RE10K and 55.84 mIoU on ScanNet. Our work signifies a novel paradigm towards generalizable, unified 3D scene reconstruction and understanding. The code is available at https://github.com/HorizonRobotics/Uni3R.

