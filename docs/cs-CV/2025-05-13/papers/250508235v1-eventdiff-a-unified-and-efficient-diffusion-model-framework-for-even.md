---
layout: default
title: "EventDiff: A Unified and Efficient Diffusion Model Framework for Event-based Video Frame Interpolation"
---

# EventDiff: A Unified and Efficient Diffusion Model Framework for Event-based Video Frame Interpolation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08235" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08235v1</a>
  <a href="https://arxiv.org/pdf/2505.08235.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08235v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08235v1', 'EventDiff: A Unified and Efficient Diffusion Model Framework for Event-based Video Frame Interpolation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hanle Zheng, Xujie Han, Zegang Peng, Shangbin Zhang, Guangxun Du, Zhuo Zou, Xilin Wang, Jibin Wu, Hao Guo, Lei Deng

**分类**: cs.CV

**发布日期**: 2025-05-13

---

## 💡 一句话要点

**提出EventDiff以解决事件驱动视频帧插值问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `视频帧插值` `事件相机` `扩散模型` `深度学习` `计算机视觉`

## 📋 核心要点

1. 现有的基于事件的VFI方法依赖于显式运动建模，导致在细微运动场景下的图像重建质量下降。
2. 本文提出EventDiff，通过事件-帧混合自编码器和去噪扩散过程，直接在潜在空间中进行插值，避免了显式运动估计。
3. 实验结果表明，EventDiff在多个合成和真实世界数据集上表现优异，相较于现有方法在PSNR上提升了1.98dB，并且推理速度提高了4.24倍。

## 📝 摘要（中文）

视频帧插值（VFI）是计算机视觉中的一项基本而具有挑战性的任务，尤其是在大运动、遮挡和光照变化的情况下。近年来，事件相机的进步为解决这些挑战提供了新机会。现有的基于事件的VFI方法通过手工设计的中间表示（如光流）成功恢复了大规模和复杂的运动，但在细微运动场景下的高保真图像重建上存在妥协。本文提出了EventDiff，一个统一且高效的基于事件的扩散模型框架，采用新颖的事件-帧混合自编码器（HAE）和轻量级的时空交叉注意力模块（STCA），有效融合动态事件流和静态帧。EventDiff直接在潜在空间中通过去噪扩散过程进行插值，展现出在多种复杂VFI场景下的鲁棒性。

## 🔬 方法详解

**问题定义**：本文旨在解决视频帧插值中的高运动、遮挡和光照变化等挑战，现有方法在细微运动场景下的重建效果不佳。

**核心思路**：EventDiff通过引入事件-帧混合自编码器（HAE）和去噪扩散过程，直接在潜在空间中进行插值，避免了传统方法对显式运动建模的依赖。

**技术框架**：整体架构包括事件-帧混合自编码器（HAE）和轻量级的时空交叉注意力（STCA）模块，分为两个阶段：首先预训练HAE，然后与扩散模型共同优化。

**关键创新**：最重要的创新在于通过去噪扩散过程进行插值，使得模型在多种复杂场景下更为鲁棒，显著提升了重建质量。

**关键设计**：在网络结构上，HAE结合了动态事件流和静态帧的特征，STCA模块则增强了时空信息的融合，损失函数设计上注重重建质量与稳定性。

## 📊 实验亮点

实验结果显示，EventDiff在Vimeo90K-Triplet数据集上相比现有最先进的基于事件的VFI方法提升了1.98dB的PSNR，并在SNU-FILM任务中表现优异，推理速度提高了4.24倍，展现了显著的性能优势。

## 🎯 应用场景

该研究具有广泛的应用潜力，尤其在视频处理、虚拟现实和增强现实等领域。通过提高视频帧插值的质量和速度，EventDiff能够为实时视频分析和生成提供更强大的支持，推动相关技术的发展。

## 📄 摘要（原文）

> Video Frame Interpolation (VFI) is a fundamental yet challenging task in computer vision, particularly under conditions involving large motion, occlusion, and lighting variation. Recent advancements in event cameras have opened up new opportunities for addressing these challenges. While existing event-based VFI methods have succeeded in recovering large and complex motions by leveraging handcrafted intermediate representations such as optical flow, these designs often compromise high-fidelity image reconstruction under subtle motion scenarios due to their reliance on explicit motion modeling. Meanwhile, diffusion models provide a promising alternative for VFI by reconstructing frames through a denoising process, eliminating the need for explicit motion estimation or warping operations. In this work, we propose EventDiff, a unified and efficient event-based diffusion model framework for VFI. EventDiff features a novel Event-Frame Hybrid AutoEncoder (HAE) equipped with a lightweight Spatial-Temporal Cross Attention (STCA) module that effectively fuses dynamic event streams with static frames. Unlike previous event-based VFI methods, EventDiff performs interpolation directly in the latent space via a denoising diffusion process, making it more robust across diverse and challenging VFI scenarios. Through a two-stage training strategy that first pretrains the HAE and then jointly optimizes it with the diffusion model, our method achieves state-of-the-art performance across multiple synthetic and real-world event VFI datasets. The proposed method outperforms existing state-of-the-art event-based VFI methods by up to 1.98dB in PSNR on Vimeo90K-Triplet and shows superior performance in SNU-FILM tasks with multiple difficulty levels. Compared to the emerging diffusion-based VFI approach, our method achieves up to 5.72dB PSNR gain on Vimeo90K-Triplet and 4.24X faster inference.

