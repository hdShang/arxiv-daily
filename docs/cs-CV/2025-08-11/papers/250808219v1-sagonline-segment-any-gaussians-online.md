---
layout: default
title: "SAGOnline: Segment Any Gaussians Online"
---

# SAGOnline: Segment Any Gaussians Online

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08219" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08219v1</a>
  <a href="https://arxiv.org/pdf/2508.08219.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08219v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08219v1', 'SAGOnline: Segment Any Gaussians Online')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wentao Sun, Quanyun Wu, Hanqing Xu, Kyle Gao, Zhengsen Xu, Yiping Chen, Dedong Zhang, Lingfei Ma, John S. Zelek, Jonathan Li

**分类**: cs.CV

**发布日期**: 2025-08-11

**备注**: 19 pages, 10 figures

---

## 💡 一句话要点

**提出SAGOnline以解决高效3D分割问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D分割` `高斯表示` `实时处理` `视频基础模型` `多物体跟踪` `增强现实` `虚拟现实`

## 📋 核心要点

1. 现有3D分割方法计算成本高，空间推理能力有限，无法同时跟踪多个物体。
2. 提出SAGOnline框架，结合视频基础模型实现2D掩码传播，并通过GPU加速生成3D掩码。
3. 在NVOS和Spin-NeRF基准测试中，SAGOnline分别取得92.7%和95.2%的mIoU，推理速度显著提升。

## 📝 摘要（中文）

3D高斯点云表示（3DGS）在明确的3D场景表示中展现出强大的能力，但实现高效且一致的3D分割仍然面临挑战。现有方法存在计算成本高、3D空间推理能力有限以及无法同时跟踪多个物体等问题。本文提出了一种轻量级的零样本框架SAGOnline，旨在实时进行高斯场景的3D分割。通过两个关键创新，SAGOnline有效解决了这些问题：一是采用解耦策略，结合视频基础模型（如SAM2）实现合成视图间一致的2D掩码传播；二是开发了GPU加速的3D掩码生成和高斯级实例标记算法，为3D原语分配唯一标识符，从而实现无损的多物体跟踪和分割。SAGOnline在NVOS和Spin-NeRF基准测试中取得了最先进的性能，推理速度比现有方法快15至1500倍。

## 🔬 方法详解

**问题定义**：本文旨在解决高效且一致的3D分割问题，现有方法在计算成本、空间推理和多物体跟踪方面存在显著不足。

**核心思路**：SAGOnline通过解耦策略和GPU加速技术，结合视频基础模型，实现高效的3D分割和跟踪。这样的设计使得系统能够在实时场景中处理复杂的3D数据。

**技术框架**：SAGOnline的整体架构包括两个主要模块：一是基于视频基础模型的2D掩码传播，二是GPU加速的3D掩码生成与实例标记。这两个模块协同工作，实现了高效的3D分割。

**关键创新**：SAGOnline的主要创新在于将视频基础模型有效适应于3D场景，并实现高斯原语的显式标记，支持同时的分割与跟踪。这与现有方法的单一处理方式形成了鲜明对比。

**关键设计**：在参数设置上，SAGOnline采用了高效的GPU计算资源，损失函数设计上注重多物体的无损跟踪，网络结构则通过解耦设计提升了处理速度和准确性。

## 📊 实验亮点

SAGOnline在NVOS和Spin-NeRF基准测试中分别取得92.7%和95.2%的mIoU，推理速度达到27毫秒每帧，相较于Feature3DGS、OmniSeg3D-gs和SA3D提升了15至1500倍，展现出卓越的性能和效率。

## 🎯 应用场景

SAGOnline的研究成果在增强现实（AR）、虚拟现实（VR）和机器人等领域具有广泛的应用潜力。通过实时的3D场景理解和分割，能够提升人机交互的自然性和智能化水平，为未来的智能系统提供支持。

## 📄 摘要（原文）

> 3D Gaussian Splatting (3DGS) has emerged as a powerful paradigm for explicit 3D scene representation, yet achieving efficient and consistent 3D segmentation remains challenging. Current methods suffer from prohibitive computational costs, limited 3D spatial reasoning, and an inability to track multiple objects simultaneously. We present Segment Any Gaussians Online (SAGOnline), a lightweight and zero-shot framework for real-time 3D segmentation in Gaussian scenes that addresses these limitations through two key innovations: (1) a decoupled strategy that integrates video foundation models (e.g., SAM2) for view-consistent 2D mask propagation across synthesized views; and (2) a GPU-accelerated 3D mask generation and Gaussian-level instance labeling algorithm that assigns unique identifiers to 3D primitives, enabling lossless multi-object tracking and segmentation across views. SAGOnline achieves state-of-the-art performance on NVOS (92.7% mIoU) and Spin-NeRF (95.2% mIoU) benchmarks, outperforming Feature3DGS, OmniSeg3D-gs, and SA3D by 15--1500 times in inference speed (27 ms/frame). Qualitative results demonstrate robust multi-object segmentation and tracking in complex scenes. Our contributions include: (i) a lightweight and zero-shot framework for 3D segmentation in Gaussian scenes, (ii) explicit labeling of Gaussian primitives enabling simultaneous segmentation and tracking, and (iii) the effective adaptation of 2D video foundation models to the 3D domain. This work allows real-time rendering and 3D scene understanding, paving the way for practical AR/VR and robotic applications.

