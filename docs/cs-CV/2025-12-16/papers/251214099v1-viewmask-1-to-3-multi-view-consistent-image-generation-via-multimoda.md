---
layout: default
title: ViewMask-1-to-3: Multi-View Consistent Image Generation via Multimodal Diffusion Models
---

# ViewMask-1-to-3: Multi-View Consistent Image Generation via Multimodal Diffusion Models

**arXiv**: [2512.14099v1](https://arxiv.org/abs/2512.14099) | [PDF](https://arxiv.org/pdf/2512.14099.pdf)

**作者**: Ruishu Zhu, Zhihao Huang, Jiacheng Sun, Ping Luo, Hongyuan Zhang, Xuelong Li

**分类**: cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出ViewMask-1-to-3，通过离散扩散模型解决单图像生成多视角一致图像的挑战。**

**关键词**: `多视角图像生成` `离散扩散模型` `序列建模` `掩码标记预测` `几何一致性` `MAGVIT-v2标记化` `多模态融合` `自注意力机制`

## 📋 核心要点

1. 现有方法依赖3D架构或专用扩散模型，需大量多视角数据和复杂几何先验，导致实现复杂且成本高。
2. ViewMask-1-to-3将多视角生成建模为离散序列问题，使用MAGVIT-v2标记化和掩码预测，通过随机掩码与自注意力确保一致性。
3. 在GSO和3D-FUTURE数据集上，该方法在PSNR、SSIM和LPIPS指标上平均排名第一，验证了离散扩散的有效性和简洁性。

## 📝 摘要（中文）

从单张图像和文本描述生成多视角图像一直面临几何一致性难以保持的挑战。现有方法通常依赖3D感知架构或专用扩散模型，需要大量多视角训练数据和复杂几何先验。本文提出ViewMask-1-to-3，首次将离散扩散模型应用于多视角图像生成。与在潜在空间操作的连续扩散方法不同，ViewMask-1-to-3将多视角合成建模为离散序列建模问题，每个视角通过MAGVIT-v2标记化表示为视觉标记。通过掩码标记预测统一语言和视觉，该方法能够通过文本输入的迭代标记解掩码逐步生成多个视角。ViewMask-1-to-3通过简单随机掩码结合自注意力实现跨视角一致性，无需复杂3D几何约束或专用注意力架构。实验表明，离散扩散为现有多视角生成方法提供了可行且简单的替代方案，在GSO和3D-FUTURE数据集上平均PSNR、SSIM和LPIPS指标排名第一，同时保持架构简洁性。

## 🔬 方法详解

ViewMask-1-to-3的整体框架基于离散扩散模型，将多视角图像生成转化为序列建模任务。首先，使用MAGVIT-v2将每个视角图像标记化为视觉标记序列，结合文本输入形成多模态序列。关键创新点在于采用掩码标记预测机制，通过迭代解掩码逐步生成多视角图像，并利用随机掩码和自注意力机制实现跨视角几何一致性，无需额外3D约束。与现有方法的主要区别在于：它避免了连续扩散模型的潜在空间操作，简化了架构；不依赖复杂3D几何先验或专用注意力模块，降低了实现难度和计算成本。

## 📊 实验亮点

在GSO和3D-FUTURE数据集上的实验结果显示，ViewMask-1-to-3在PSNR、SSIM和LPIPS指标上平均排名第一，显著优于现有方法，证明了离散扩散模型在多视角生成中的高效性和简洁架构优势。

## 🎯 应用场景

该研究在计算机视觉和机器人领域有广泛应用潜力，如虚拟现实中的场景重建、增强现实的物体展示、机器人导航的环境感知，以及游戏和影视制作中的多视角内容生成，能高效生成一致的多视角图像，提升真实感和交互性。

## 📄 摘要（原文）

> Multi-view image generation from a single image and text description remains challenging due to the difficulty of maintaining geometric consistency across different viewpoints. Existing approaches typically rely on 3D-aware architectures or specialized diffusion models that require extensive multi-view training data and complex geometric priors. In this work, we introduce ViewMask-1-to-3, a pioneering approach to apply discrete diffusion models to multi-view image generation. Unlike continuous diffusion methods that operate in latent spaces, ViewMask-1-to-3 formulates multi-view synthesis as a discrete sequence modeling problem, where each viewpoint is represented as visual tokens obtained through MAGVIT-v2 tokenization. By unifying language and vision through masked token prediction, our approach enables progressive generation of multiple viewpoints through iterative token unmasking with text input. ViewMask-1-to-3 achieves cross-view consistency through simple random masking combined with self-attention, eliminating the requirement for complex 3D geometric constraints or specialized attention architectures. Our approach demonstrates that discrete diffusion provides a viable and simple alternative to existing multi-view generation methods, ranking first on average across GSO and 3D-FUTURE datasets in terms of PSNR, SSIM, and LPIPS, while maintaining architectural simplicity.

