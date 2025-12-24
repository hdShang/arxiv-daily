---
layout: default
title: "RAAG: Ratio Aware Adaptive Guidance"
---

# RAAG: Ratio Aware Adaptive Guidance

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03442" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03442v2</a>
  <a href="https://arxiv.org/pdf/2508.03442.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03442v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03442v2', 'RAAG: Ratio Aware Adaptive Guidance')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shangwen Zhu, Qianyu Peng, Yuting Hu, Zhantao Yang, Han Zhang, Zhao Pu, Andy Zheng, Zhilei Shu, Ruili Feng, Fan Cheng

**分类**: cs.CV

**发布日期**: 2025-08-05 (更新: 2025-09-26)

---

## 💡 一句话要点

**提出自适应引导方法以解决流式生成模型采样不稳定问题**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `流式生成模型` `自适应引导` `采样稳定性` `图像生成` `视频生成` `分类器无关引导` `生成质量提升`

## 📋 核心要点

1. 现有方法在推理过程中使用固定的引导尺度，导致早期采样不稳定，影响生成质量。
2. 提出了一种自适应引导调度，根据条件与无条件预测的比率动态调整引导尺度，以减少早期步骤的敏感性。
3. 实验结果显示，该方法在多个图像和视频模型上实现了最高3倍的采样速度提升，同时保持或改善了生成质量和语义一致性。

## 📝 摘要（中文）

基于流的生成模型取得了显著进展，分类器无关引导（CFG）已成为高保真生成的标准。然而，传统方法在推理过程中使用固定的强引导尺度，难以适应现代应用所需的快速、少步采样。本文揭示了这一冲突的根本原因：早期步骤对引导的敏感性导致的采样不稳定性。我们提出了一种简单且理论基础扎实的自适应引导调度，能够根据条件与无条件预测的比率动态调整引导尺度。实验表明，该方法在保持或提升图像质量的同时，实现了最高3倍的采样速度提升。

## 🔬 方法详解

**问题定义**：本文要解决的问题是流式生成模型在推理阶段使用固定引导尺度导致的早期采样不稳定性，进而影响生成图像的质量。现有方法在快速采样时未能适应条件与无条件预测比率的变化，导致错误的指数放大。

**核心思路**：论文的核心解决思路是提出一种自适应引导调度机制，能够根据条件与无条件预测的比率动态调整引导尺度。通过在早期步骤降低引导强度，减少对采样过程的敏感性，从而提高生成质量。

**技术框架**：整体架构包括数据预处理、模型训练和推理阶段。在推理阶段，采用自适应引导调度，根据实时计算的条件与无条件预测比率调整引导尺度。

**关键创新**：最重要的技术创新点在于提出了自适应引导调度机制，区别于传统方法的固定引导尺度，能够有效应对早期采样的不稳定性。

**关键设计**：在设计中，关键参数包括引导尺度的动态调整策略，损失函数的选择，以及与现有生成模型的兼容性设计，确保方法的轻量化和无推理开销。

## 📊 实验亮点

实验结果表明，提出的方法在多个最先进的图像（SD3.5、Qwen-Image）和视频（WAN2.1）模型上实现了最高3倍的采样速度提升，同时在质量、鲁棒性和语义一致性方面保持或改善了性能，显示出显著的优势。

## 🎯 应用场景

该研究的潜在应用领域包括图像生成、视频生成和其他基于流的生成任务。通过提高生成速度和质量，该方法可广泛应用于实时图像处理、虚拟现实和增强现实等场景，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Flow-based generative models have achieved remarkable progress, with classifier-free guidance (CFG) becoming the standard for high-fidelity generation. However, the conventional practice of applying a strong, fixed guidance scale throughout inference is poorly suited for the rapid, few-step sampling required by modern applications. In this work, we uncover the root cause of this conflict: a fundamental sampling instability where the earliest steps are acutely sensitive to guidance. We trace this to a significant spike in the ratio of conditional to unconditional predictions--a spike that we prove to be an inherent property of the training data distribution itself, making it a almost inevitable challenge. Applying a high, static guidance value during this volatile initial phase leads to an exponential amplification of error, degrading image quality. To resolve this, we propose a simple, theoretically grounded, adaptive guidance schedule that automatically dampens the guidance scale at early steps based on the evolving ratio. Our method is lightweight, incurs no inference overhead, and is compatible with standard frameworks. Experiments across state-of-the-art image (SD3.5, Qwen-Image) and video (WAN2.1) models show our approach enables up to 3x faster sampling while maintaining or improving quality, robustness, and semantic alignment. Our findings highlight that adapting guidance to the sampling process, rather than fixing it, is critical for unlocking the full potential of fast, flow-based models.

