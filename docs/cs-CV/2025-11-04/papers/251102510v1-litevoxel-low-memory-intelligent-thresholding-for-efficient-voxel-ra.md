---
layout: default
title: "LiteVoxel: Low-memory Intelligent Thresholding for Efficient Voxel Rasterization"
---

# LiteVoxel: Low-memory Intelligent Thresholding for Efficient Voxel Rasterization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.02510" class="toolbar-btn" target="_blank">📄 arXiv: 2511.02510v1</a>
  <a href="https://arxiv.org/pdf/2511.02510.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.02510v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.02510v1', 'LiteVoxel: Low-memory Intelligent Thresholding for Efficient Voxel Rasterization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jee Won Lee, Jongseong Brad Choi

**分类**: cs.CV

**发布日期**: 2025-11-04

---

## 💡 一句话要点

**提出LiteVoxel以解决稀疏体素光栅化中的低频内容不足问题**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `稀疏体素光栅化` `低频内容处理` `显存优化` `自调节训练` `计算机视觉` `虚拟现实` `场景重建`

## 📋 核心要点

1. 现有的稀疏体素光栅化方法在处理低频内容时容易出现不足，且显存使用不够高效。
2. LiteVoxel通过自调节训练管道和逆Sobel重加权，增强了对低频内容的敏感性，并优化了显存使用。
3. 实验结果显示，LiteVoxel在多个数据集上减少了低频区域的错误，同时保持了与强SVRaster管道相当的性能。

## 📝 摘要（中文）

稀疏体素光栅化是一种快速且可微分的场景重建替代方案，但在处理低频内容时表现不佳，并且依赖脆弱的修剪启发式方法，可能导致显存膨胀。本文提出LiteVoxel，一个自调节的训练管道，使得稀疏体素光栅化更加稳定且内存占用更低。通过逆Sobel重加权和中期训练的伽马斜坡，使损失函数对低频内容更加敏感，确保几何体稳定后再调整梯度预算。采用深度分位数修剪逻辑替代固定阈值，并通过EMA-滞后保护和基于光线足迹的优先级驱动细分来优化结构。实验结果表明，LiteVoxel在保持PSNR/SSIM、训练时间和FPS与强SVRaster管道相当的同时，显著减少了40%-60%的峰值显存，并保留了低频细节。

## 🔬 方法详解

**问题定义**：本文旨在解决稀疏体素光栅化在处理低频内容时的不足，以及显存使用不当的问题。现有方法依赖于脆弱的修剪启发式，容易导致显存膨胀和边界不稳定。

**核心思路**：LiteVoxel的核心思路是通过自调节的训练管道和逆Sobel重加权，使得损失函数对低频内容更加敏感，从而在几何体稳定后再进行梯度预算的调整。

**技术框架**：LiteVoxel的整体架构包括自调节训练管道、逆Sobel重加权、深度分位数修剪逻辑、EMA-滞后保护和基于光线足迹的细分模块。每个模块协同工作，以实现更高效的光栅化过程。

**关键创新**：LiteVoxel的主要创新在于引入了深度分位数修剪逻辑和逆Sobel重加权，使得光栅化过程更加稳定，并显著降低了显存使用。与现有方法相比，LiteVoxel在处理低频内容时表现更佳。

**关键设计**：在损失函数设计上，采用逆Sobel重加权，并结合中期训练的伽马斜坡。深度分位数修剪逻辑替代了固定阈值，确保了在最大混合权重下的稳定性。同时，EMA-滞后保护和光线足迹优先级驱动细分进一步优化了结构。

## 📊 实验亮点

LiteVoxel在多个数据集上的实验结果显示，显存峰值减少了约40%-60%，同时在低频区域的错误得到了显著缓解。与强SVRaster管道相比，LiteVoxel在PSNR/SSIM、训练时间和FPS等性能指标上保持了相当的水平，展现了其在内存效率和感知质量上的优势。

## 🎯 应用场景

LiteVoxel的研究成果在计算机视觉、虚拟现实和游戏开发等领域具有广泛的应用潜力。通过提高稀疏体素光栅化的效率和稳定性，该方法能够支持更复杂的场景重建任务，减少显存需求，从而使得高质量的实时渲染成为可能。未来，LiteVoxel可能推动更多基于体素的技术进步，提升用户体验。

## 📄 摘要（原文）

> Sparse-voxel rasterization is a fast, differentiable alternative for optimization-based scene reconstruction, but it tends to underfit low-frequency content, depends on brittle pruning heuristics, and can overgrow in ways that inflate VRAM. We introduce LiteVoxel, a self-tuning training pipeline that makes SV rasterization both steadier and lighter. Our loss is made low-frequency aware via an inverse-Sobel reweighting with a mid-training gamma-ramp, shifting gradient budget to flat regions only after geometry stabilize. Adaptation replaces fixed thresholds with a depth-quantile pruning logic on maximum blending weight, stabilized by EMA-hysteresis guards and refines structure through ray-footprint-based, priority-driven subdivision under an explicit growth budget. Ablations and full-system results across Mip-NeRF 360 (6scenes) and Tanks & Temples (3scenes) datasets show mitigation of errors in low-frequency regions and boundary instability while keeping PSNR/SSIM, training time, and FPS comparable to a strong SVRaster pipeline. Crucially, LiteVoxel reduces peak VRAM by ~40%-60% and preserves low-frequency detail that prior setups miss, enabling more predictable, memory-efficient training without sacrificing perceptual quality.

