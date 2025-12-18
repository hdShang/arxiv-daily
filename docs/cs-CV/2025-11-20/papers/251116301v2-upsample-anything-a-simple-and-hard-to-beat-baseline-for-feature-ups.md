---
layout: default
title: Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling
---

# Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.16301" class="toolbar-btn" target="_blank">📄 arXiv: 2511.16301v2</a>
  <a href="https://arxiv.org/pdf/2511.16301.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.16301v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.16301v2', 'Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Minseok Seo, Mark Hamilton, Changick Kim

**分类**: cs.CV

**发布日期**: 2025-11-20 (更新: 2025-11-24)

**备注**: 15 pages, 12 figures

**🔗 代码/项目**: [PROJECT_PAGE](https://seominseok0429.github.io/Upsample-Anything/)

---

## 💡 一句话要点

**提出Upsample Anything，一种无需训练的特征上采样通用基线方法**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `特征上采样` `测试时优化` `高斯核` `视觉基础模型` `语义分割` `深度估计` `像素级任务`

## 📋 核心要点

1. 视觉基础模型虽强大，但其特征图下采样限制了其在像素级任务中的应用。
2. Upsample Anything通过测试时优化学习各向异性高斯核，实现高效特征上采样。
3. 该方法在语义分割、深度估计等任务上取得了SOTA性能，且速度快。

## 📝 摘要（中文）

本文提出了一种轻量级的测试时优化（TTO）框架，名为Upsample Anything，该框架无需任何训练即可将低分辨率特征恢复为高分辨率的像素级输出。尽管视觉基础模型在各种下游任务中表现出强大的泛化能力，但它们的表示通常被下采样14x/16x（例如，ViT），这限制了它们在像素级应用中的直接使用。现有的特征上采样方法依赖于数据集特定的重新训练或繁重的隐式优化，限制了可扩展性和泛化能力。Upsample Anything通过一个简单的逐图像优化来解决这些问题，该优化学习一个结合空间和范围线索的各向异性高斯核，有效地桥接了高斯溅射和联合双边上采样。学习到的核充当一个通用的、边缘感知的算子，可以无缝地跨架构和模态传输，从而实现特征、深度或概率图的精确高分辨率重建。它在每张224x224图像上仅运行约0.419秒，并在语义分割、深度估计以及深度和概率图上采样方面实现了最先进的性能。

## 🔬 方法详解

**问题定义**：现有视觉基础模型（如ViT）提取的特征图通常被大幅下采样，直接应用于像素级任务（如语义分割、深度估计）时精度受限。现有的特征上采样方法通常需要针对特定数据集进行重新训练，或者依赖计算量大的隐式优化，泛化能力和效率都存在问题。

**核心思路**：Upsample Anything的核心思路是学习一个各向异性高斯核，该核能够根据输入图像的局部空间和范围信息自适应地进行特征上采样。通过在测试时对每个图像进行优化，学习到的高斯核能够有效地将低分辨率特征图恢复到高分辨率，同时保持边缘清晰。

**技术框架**：Upsample Anything的整体框架包括以下步骤：1) 输入低分辨率特征图；2) 初始化一个各向异性高斯核；3) 通过优化算法（如梯度下降）学习高斯核的参数，优化目标是使上采样后的特征图尽可能地逼近真实的高分辨率特征图（如果没有真实值，则使用一些先验知识或正则化项）；4) 使用学习到的高斯核对低分辨率特征图进行上采样，得到高分辨率的像素级输出。

**关键创新**：Upsample Anything的关键创新在于：1) 提出了一种无需训练的特征上采样方法，避免了数据集依赖和重新训练的需要；2) 使用各向异性高斯核，能够自适应地处理不同图像的局部特征，实现边缘感知的上采样；3) 将高斯溅射和联合双边上采样的思想结合起来，提高了上采样的精度和效率。

**关键设计**：各向异性高斯核的参数包括空间尺度、范围尺度和旋转角度等。优化目标通常包括一个重建损失（衡量上采样后的特征图与真实特征图的差异）和一个正则化项（防止过拟合）。优化算法可以使用Adam等常用的梯度下降算法。论文中提到运行时间约为0.419秒/224x224图像，表明该方法具有较高的效率。

## 📊 实验亮点

Upsample Anything在语义分割、深度估计以及深度和概率图上采样等任务上取得了state-of-the-art的性能。该方法无需训练，运行速度快（约0.419秒/224x224图像），并且能够跨架构和模态进行迁移，具有很强的通用性。实验结果表明，Upsample Anything是一种简单而有效的特征上采样方法。

## 🎯 应用场景

Upsample Anything具有广泛的应用前景，可用于提升各种视觉基础模型在像素级任务中的性能，例如语义分割、深度估计、目标检测等。该方法无需训练的特性使其能够快速部署到新的数据集和任务中，具有很高的实际价值。未来，该方法可以进一步扩展到其他模态的数据上采样，例如音频、文本等。

## 📄 摘要（原文）

> We present \textbf{Upsample Anything}, a lightweight test-time optimization (TTO) framework that restores low-resolution features to high-resolution, pixel-wise outputs without any training. Although Vision Foundation Models demonstrate strong generalization across diverse downstream tasks, their representations are typically downsampled by 14x/16x (e.g., ViT), which limits their direct use in pixel-level applications. Existing feature upsampling approaches depend on dataset-specific retraining or heavy implicit optimization, restricting scalability and generalization. Upsample Anything addresses these issues through a simple per-image optimization that learns an anisotropic Gaussian kernel combining spatial and range cues, effectively bridging Gaussian Splatting and Joint Bilateral Upsampling. The learned kernel acts as a universal, edge-aware operator that transfers seamlessly across architectures and modalities, enabling precise high-resolution reconstruction of features, depth, or probability maps. It runs in only $\approx0.419 \text{s}$ per 224x224 image and achieves state-of-the-art performance on semantic segmentation, depth estimation, and both depth and probability map upsampling. \textbf{Project page:} \href{https://seominseok0429.github.io/Upsample-Anything/}{https://seominseok0429.github.io/Upsample-Anything/}

