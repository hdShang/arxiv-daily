---
layout: default
title: ViewMask-1-to-3: Multi-View Consistent Image Generation via Multimodal Diffusion Models
---

# ViewMask-1-to-3: Multi-View Consistent Image Generation via Multimodal Diffusion Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14099" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14099v1</a>
  <a href="https://arxiv.org/pdf/2512.14099.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14099v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14099v1', 'ViewMask-1-to-3: Multi-View Consistent Image Generation via Multimodal Diffusion Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ruishu Zhu, Zhihao Huang, Jiacheng Sun, Ping Luo, Hongyuan Zhang, Xuelong Li

**分类**: cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**ViewMask-1-to-3：基于多模态扩散模型实现多视角一致的图像生成**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多视角图像生成` `离散扩散模型` `跨视角一致性` `MAGVIT-v2` `自注意力`

## 📋 核心要点

1. 现有方法在单图和文本描述生成多视角图像时，难以保持视角间的几何一致性，通常依赖3D感知架构或专用扩散模型。
2. ViewMask-1-to-3将多视角图像生成建模为离散序列预测问题，利用掩码token预测和自注意力实现跨视角一致性。
3. 实验表明，ViewMask-1-to-3在多视角图像生成任务上取得了优异的性能，在PSNR、SSIM和LPIPS指标上均排名第一。

## 📝 摘要（中文）

本文提出ViewMask-1-to-3，一种利用离散扩散模型进行多视角图像生成的创新方法。与在潜在空间中操作的连续扩散方法不同，ViewMask-1-to-3将多视角合成问题建模为离散序列建模问题，其中每个视角表示为通过MAGVIT-v2 tokenization获得的视觉tokens。通过基于掩码token预测统一语言和视觉，该方法能够通过文本输入和迭代token解掩码逐步生成多个视角。ViewMask-1-to-3通过简单的随机掩码结合自注意力实现跨视角一致性，无需复杂的3D几何约束或专门的注意力架构。实验结果表明，离散扩散为现有的多视角生成方法提供了一种可行且简单的替代方案，在GSO和3D-FUTURE数据集上，ViewMask-1-to-3在PSNR、SSIM和LPIPS指标上平均排名第一，同时保持了架构的简洁性。

## 🔬 方法详解

**问题定义**：论文旨在解决从单张图像和文本描述生成多个视角一致图像的问题。现有方法通常依赖于复杂的3D感知架构或需要大量多视角训练数据的专用扩散模型，并且难以保证生成图像在不同视角下的几何一致性。

**核心思路**：论文的核心思路是将多视角图像生成问题转化为一个离散序列建模问题，并利用离散扩散模型逐步生成不同视角的图像。通过将图像表示为离散的视觉tokens，并结合掩码token预测和自注意力机制，实现跨视角的一致性。

**技术框架**：ViewMask-1-to-3的整体框架包括以下几个主要步骤：1) 使用MAGVIT-v2将输入图像和文本描述转换为视觉和文本tokens；2) 对视觉tokens进行随机掩码；3) 使用离散扩散模型，通过迭代token解掩码的方式逐步生成不同视角的图像；4) 利用自注意力机制增强跨视角的一致性。

**关键创新**：该方法最重要的创新点在于将离散扩散模型应用于多视角图像生成任务，并提出了一种简单有效的跨视角一致性保持方法。与传统的连续扩散模型相比，离散扩散模型更易于训练和推理，并且不需要复杂的几何约束或专门的注意力架构。

**关键设计**：ViewMask-1-to-3的关键设计包括：1) 使用MAGVIT-v2进行tokenization，将图像转换为离散的视觉tokens；2) 采用随机掩码策略，对视觉tokens进行随机遮盖；3) 使用Transformer架构作为离散扩散模型的主干网络，进行token预测；4) 利用自注意力机制，增强不同视角之间的信息交互，从而提高跨视角一致性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14099v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14099v1/figs/files/training.jpg" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14099v1/figs/files/infer.jpg" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，ViewMask-1-to-3在GSO和3D-FUTURE数据集上，在PSNR、SSIM和LPIPS指标上平均排名第一，超越了现有的多视角图像生成方法。这表明ViewMask-1-to-3能够生成更高质量、更一致的多视角图像，并且具有更强的泛化能力。该方法在保持架构简洁性的同时，实现了显著的性能提升。

## 🎯 应用场景

ViewMask-1-to-3在三维重建、虚拟现实、游戏开发等领域具有广泛的应用前景。它可以用于从单张图像生成不同视角的图像，从而帮助用户更好地理解和感知三维场景。此外，该方法还可以用于生成具有特定风格或内容的图像，为创意设计提供更多可能性。未来，该技术有望应用于自动驾驶、机器人导航等领域，提升系统的环境感知能力。

## 📄 摘要（原文）

> Multi-view image generation from a single image and text description remains challenging due to the difficulty of maintaining geometric consistency across different viewpoints. Existing approaches typically rely on 3D-aware architectures or specialized diffusion models that require extensive multi-view training data and complex geometric priors. In this work, we introduce ViewMask-1-to-3, a pioneering approach to apply discrete diffusion models to multi-view image generation. Unlike continuous diffusion methods that operate in latent spaces, ViewMask-1-to-3 formulates multi-view synthesis as a discrete sequence modeling problem, where each viewpoint is represented as visual tokens obtained through MAGVIT-v2 tokenization. By unifying language and vision through masked token prediction, our approach enables progressive generation of multiple viewpoints through iterative token unmasking with text input. ViewMask-1-to-3 achieves cross-view consistency through simple random masking combined with self-attention, eliminating the requirement for complex 3D geometric constraints or specialized attention architectures. Our approach demonstrates that discrete diffusion provides a viable and simple alternative to existing multi-view generation methods, ranking first on average across GSO and 3D-FUTURE datasets in terms of PSNR, SSIM, and LPIPS, while maintaining architectural simplicity.

