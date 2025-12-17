---
layout: default
title: ViewMask-1-to-3: Multi-View Consistent Image Generation via Multimodal Diffusion Models
---

# ViewMask-1-to-3: Multi-View Consistent Image Generation via Multimodal Diffusion Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14099" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14099</a>
  <a href="https://arxiv.org/pdf/2512.14099.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14099" onclick="toggleFavorite(this, '2512.14099', 'ViewMask-1-to-3: Multi-View Consistent Image Generation via Multimodal Diffusion Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ruishu Zhu, Zhihao Huang, Jiacheng Sun, Ping Luo, Hongyuan Zhang, Xuelong Li

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**ViewMask-1-to-3：基于多模态扩散模型实现多视角一致的图像生成**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多视角图像生成` `离散扩散模型` `跨视角一致性` `多模态学习` `MAGVIT-v2`

## 📋 核心要点

1. 现有方法在单图文条件下生成多视角图像时，难以保证视角间几何一致性，且依赖大量多视角数据和复杂几何先验。
2. ViewMask-1-to-3将多视角生成转化为离散序列建模，通过掩码token预测统一语言和视觉信息，迭代生成多视角。
3. 该方法通过随机掩码和自注意力实现跨视角一致性，无需复杂3D约束，在GSO和3D-FUTURE数据集上取得了领先的性能。

## 📝 摘要（中文）

本文提出ViewMask-1-to-3，一种利用离散扩散模型进行多视角图像生成的创新方法。针对从单张图像和文本描述生成多视角图像时难以保持几何一致性的挑战，现有方法通常依赖于3D感知架构或专门的扩散模型，这些方法需要大量的多视角训练数据和复杂的几何先验。ViewMask-1-to-3将多视角合成问题转化为离散序列建模问题，通过MAGVIT-v2标记化将每个视角表示为视觉token。通过掩码token预测统一语言和视觉，该方法能够通过迭代token解掩码和文本输入逐步生成多个视角。ViewMask-1-to-3通过简单的随机掩码和自注意力实现跨视角一致性，无需复杂的3D几何约束或专门的注意力架构。实验结果表明，离散扩散为现有的多视角生成方法提供了一种可行且简单的替代方案，在GSO和3D-FUTURE数据集上，PSNR、SSIM和LPIPS指标均排名第一，同时保持了架构的简洁性。

## 🔬 方法详解

**问题定义**：论文旨在解决从单张图像和文本描述生成多个视角图像时，如何保证生成图像在不同视角下几何一致性的问题。现有方法通常依赖于3D感知架构或专门设计的扩散模型，这些方法需要大量的多视角训练数据，并且需要复杂的几何先验知识，限制了其应用范围和效率。

**核心思路**：论文的核心思路是将多视角图像生成问题转化为一个离散序列建模问题。通过将每个视角表示为离散的视觉token，并利用掩码token预测的方式，将语言和视觉信息统一起来。通过迭代地解掩码token，逐步生成多个视角，从而实现多视角图像的生成。

**技术框架**：ViewMask-1-to-3的整体框架基于离散扩散模型。首先，使用MAGVIT-v2将输入图像和文本描述转换为视觉token和文本token。然后，通过随机掩码的方式，将部分视觉token进行掩盖。接下来，利用Transformer架构，结合文本token和未被掩盖的视觉token，预测被掩盖的视觉token。通过迭代地进行掩码和预测，逐步生成完整的多视角图像。

**关键创新**：该方法最重要的创新点在于将多视角图像生成问题转化为离散序列建模问题，并利用离散扩散模型进行求解。与传统的连续扩散模型相比，离散扩散模型不需要在潜在空间中进行操作，而是直接在token空间中进行操作，从而简化了模型的复杂性。此外，该方法通过简单的随机掩码和自注意力机制，实现了跨视角的一致性，避免了使用复杂的3D几何约束。

**关键设计**：ViewMask-1-to-3的关键设计包括：1) 使用MAGVIT-v2进行token化，将图像和文本转换为离散的token序列；2) 采用随机掩码策略，对视觉token进行掩盖；3) 使用Transformer架构，结合文本token和未被掩盖的视觉token，预测被掩盖的视觉token；4) 通过迭代地进行掩码和预测，逐步生成完整的多视角图像。损失函数主要包括token预测的交叉熵损失。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14099/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14099/figs/files/training.jpg" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14099/figs/files/infer.jpg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

ViewMask-1-to-3在GSO和3D-FUTURE数据集上取得了显著的性能提升，在PSNR、SSIM和LPIPS指标上均排名第一。实验结果表明，该方法能够有效地生成多视角一致的图像，并且具有较高的图像质量。与现有方法相比，ViewMask-1-to-3在保持架构简洁性的同时，实现了更好的性能。

## 🎯 应用场景

ViewMask-1-to-3在3D内容生成、虚拟现实、增强现实、游戏开发等领域具有广泛的应用前景。它可以根据单张图像和文本描述生成多个视角的图像，从而为用户提供更加沉浸式的体验。此外，该方法还可以用于生成用于3D重建或SLAM的训练数据，从而提高3D视觉算法的性能。未来，该方法有望应用于自动驾驶、机器人导航等领域。

## 📄 摘要（原文）

> Multi-view image generation from a single image and text description remains challenging due to the difficulty of maintaining geometric consistency across different viewpoints. Existing approaches typically rely on 3D-aware architectures or specialized diffusion models that require extensive multi-view training data and complex geometric priors. In this work, we introduce ViewMask-1-to-3, a pioneering approach to apply discrete diffusion models to multi-view image generation. Unlike continuous diffusion methods that operate in latent spaces, ViewMask-1-to-3 formulates multi-view synthesis as a discrete sequence modeling problem, where each viewpoint is represented as visual tokens obtained through MAGVIT-v2 tokenization. By unifying language and vision through masked token prediction, our approach enables progressive generation of multiple viewpoints through iterative token unmasking with text input. ViewMask-1-to-3 achieves cross-view consistency through simple random masking combined with self-attention, eliminating the requirement for complex 3D geometric constraints or specialized attention architectures. Our approach demonstrates that discrete diffusion provides a viable and simple alternative to existing multi-view generation methods, ranking first on average across GSO and 3D-FUTURE datasets in terms of PSNR, SSIM, and LPIPS, while maintaining architectural simplicity.

