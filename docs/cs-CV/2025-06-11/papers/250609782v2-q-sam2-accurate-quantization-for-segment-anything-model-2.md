---
layout: default
title: "Q-SAM2: Accurate Quantization for Segment Anything Model 2"
---

# Q-SAM2: Accurate Quantization for Segment Anything Model 2

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09782" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09782v2</a>
  <a href="https://arxiv.org/pdf/2506.09782.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09782v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09782v2', 'Q-SAM2: Accurate Quantization for Segment Anything Model 2')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nicola Farronato, Florian Scheidegger, Mattia Rigotti, Cristiano Malossi, Michele Magno, Haotong Qin

**分类**: cs.CV, cs.AI

**发布日期**: 2025-06-11 (更新: 2025-11-24)

**备注**: 22 pages

---

## 💡 一句话要点

**提出Q-SAM2以解决SAM2模型在资源受限设备上的量化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `量化技术` `模型压缩` `图像分割` `深度学习` `边缘计算`

## 📋 核心要点

1. 现有的SAM2模型在资源受限设备上部署时面临高计算和内存成本的挑战。
2. Q-SAM2通过引入方差减少校准和可学习统计裁剪，提供了一种新的低位量化方法。
3. 实验结果显示，Q-SAM2在视频分割基准上提高了9.7 ppt的准确率，同时模型大小减少了8倍。

## 📝 摘要（中文）

Segment Anything Model 2 (SAM2) 是一个强大的可提示分割基础模型，但其高计算和内存成本在资源受限设备上部署时构成了主要障碍。本文提出了Q-SAM2，一种准确的低位量化方法，能够实现高压缩率和高保真度。为了解决量化过程中由于权重和激活分布复杂而导致的性能下降，Q-SAM2引入了两个新颖的贡献：方差减少校准（VRC），一种通过最小化小批量的弗罗贝尼乌斯范数来减少权重统计方差的初始化方法；可学习统计裁剪（LSC），一种量化感知训练（QAT）方法，通过学习动量稳定的裁剪因子来管理权重和激活中的异常值。综合实验表明，Q-SAM2在超低2位量化情况下实现了高精度推理和显著的效率提升，超越了现有的QAT方案。

## 🔬 方法详解

**问题定义**：本文旨在解决Segment Anything Model 2 (SAM2) 在资源受限设备上部署时的高计算和内存成本问题。现有的量化方法在处理权重和激活分布时容易导致性能下降，限制了模型的实际应用。

**核心思路**：Q-SAM2的核心思路是通过方差减少校准（VRC）和可学习统计裁剪（LSC）来优化量化过程。VRC通过最小化小批量的弗罗贝尼乌斯范数来降低权重的统计方差，而LSC则通过学习稳定的裁剪因子来处理权重和激活中的异常值，从而提高量化后的模型性能。

**技术框架**：Q-SAM2的整体架构包括两个主要模块：首先是方差减少校准模块，通过对小批量数据进行初始化来降低权重的方差；其次是可学习统计裁剪模块，在量化感知训练过程中动态调整裁剪因子，以适应权重和激活的变化。

**关键创新**：Q-SAM2的关键创新在于引入了方差减少校准和可学习统计裁剪，这两者有效地解决了现有量化方法在处理复杂权重和激活分布时的不足，显著提升了模型的推理精度和效率。

**关键设计**：在设计中，VRC模块的损失函数采用了弗罗贝尼乌斯范数，而LSC模块则通过动量学习机制来稳定裁剪因子的更新。此外，Q-SAM2在超低2位量化情况下，仍能保持较高的模型精度，显示出其设计的有效性。

## 📊 实验亮点

Q-SAM2在视频分割基准上实现了最高9.7 ppt的准确率提升，并在实例分割任务中提高了7.3 ppt的mIoU，相比于最佳竞争QAT模型，模型大小减少了8倍，显示出显著的性能优势。

## 🎯 应用场景

Q-SAM2的研究成果具有广泛的应用潜力，尤其是在移动设备、嵌入式系统和边缘计算等资源受限环境中。通过降低模型的计算和内存需求，Q-SAM2能够使得高性能的图像分割技术在实际应用中变得更加可行，推动智能设备在视觉理解领域的应用发展。

## 📄 摘要（原文）

> The Segment Anything Model 2 (SAM2) is a powerful foundation model for promptable segmentation. However, its high computational and memory costs are a major barrier to deployment on resource-constrained devices. In this paper, we present Q-SAM2, an accurate low-bit quantization method that achieves high compression and high fidelity. To address performance degradation arising from challenging weight and activation distributions during quantization, Q-SAM2 introduces two novel contributions: Variance-Reduced Calibration (VRC), an initialization method that reduces weight statistical variance by minimizing the Frobenius norm over a small calibration batch; and Learnable Statistical Clipping (LSC), a Quantization-Aware Training (QAT) method that learns momentum-stabilized clipping factors to manage outliers in weights and activations. Comprehensive experiments demonstrate that Q-SAM2 achieves highly accurate inference with substantial efficiency gains, significantly surpassing state-of-the-art general QAT schemes, particularly in the ultra-low 2-bit regime. Specifically, Q-SAM2 achieves an accuracy gain of up to 9.7 ppt in J&F on the video segmentation benchmark and 7.3 ppt in mIoU for instance segmentation over the best competing QAT model, all while achieving an 8x reduction in model size compared to the BF16 baseline.

