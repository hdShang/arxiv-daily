---
layout: default
title: ViewMask-1-to-3: Multi-View Consistent Image Generation via Multimodal Diffusion Models
---

# ViewMask-1-to-3: Multi-View Consistent Image Generation via Multimodal Diffusion Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14099" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14099v1</a>
  <a href="https://arxiv.org/pdf/2512.14099.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14099v1" onclick="toggleFavorite(this, '2512.14099v1', 'ViewMask-1-to-3: Multi-View Consistent Image Generation via Multimodal Diffusion Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ruishu Zhu, Zhihao Huang, Jiacheng Sun, Ping Luo, Hongyuan Zhang, Xuelong Li

**分类**: cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**ViewMask-1-to-3：基于多模态扩散模型实现多视角一致的图像生成**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多视角图像生成` `离散扩散模型` `多模态学习` `跨视角一致性` `MAGVIT-v2` `Transformer` `掩码token预测`

## 📋 核心要点

1. 现有方法在单图文条件下生成多视角图像时，难以保证视角间的几何一致性，且依赖大量多视角数据和复杂几何先验。
2. ViewMask-1-to-3将多视角图像生成转化为离散序列建模，通过掩码token预测统一语言和视觉信息，迭代生成多视角。
3. 实验表明，该方法在GSO和3D-FUTURE数据集上，PSNR、SSIM和LPIPS指标均排名第一，证明了离散扩散的有效性。

## 📝 摘要（中文）

本文提出ViewMask-1-to-3，一种利用离散扩散模型进行多视角图像生成的新方法。针对从单张图像和文本描述生成多视角图像时难以保持几何一致性的问题，现有方法通常依赖于3D感知架构或专门的扩散模型，这些方法需要大量的多视角训练数据和复杂的几何先验。ViewMask-1-to-3将多视角合成问题转化为离散序列建模问题，通过MAGVIT-v2标记化将每个视角表示为视觉tokens。通过掩码token预测统一语言和视觉，该方法能够通过迭代token解掩码和文本输入逐步生成多个视角。ViewMask-1-to-3通过简单的随机掩码和自注意力实现跨视角一致性，无需复杂的3D几何约束或专门的注意力架构。实验表明，离散扩散为现有的多视角生成方法提供了一种可行且简单的替代方案，在GSO和3D-FUTURE数据集上，ViewMask-1-to-3在PSNR、SSIM和LPIPS指标上均排名第一，同时保持了架构的简洁性。

## 🔬 方法详解

**问题定义**：论文旨在解决从单张图像和文本描述生成多个视角一致的图像这一难题。现有方法，如基于3D感知架构或特定扩散模型的方法，通常需要大量的多视角训练数据以及复杂的几何先验知识，这限制了它们的应用范围和效率。

**核心思路**：ViewMask-1-to-3的核心思路是将多视角图像生成问题转化为一个离散序列建模问题。通过将每个视角表示为视觉tokens，并利用掩码token预测的方式，将语言和视觉信息统一起来，从而实现多视角的逐步生成。这种方法避免了对复杂3D几何约束的依赖，简化了模型设计。

**技术框架**：ViewMask-1-to-3的整体框架包括以下几个主要步骤：1) 使用MAGVIT-v2将输入图像和文本描述转换为视觉和文本tokens。2) 对视觉tokens进行随机掩码。3) 利用Transformer架构，通过自注意力机制学习tokens之间的关系，并预测被掩码的tokens。4) 迭代进行token解掩码，逐步生成多个视角。

**关键创新**：ViewMask-1-to-3的关键创新在于它将离散扩散模型应用于多视角图像生成。与传统的连续扩散模型不同，该方法直接在token空间进行操作，避免了对潜在空间的复杂推理。此外，通过简单的随机掩码和自注意力机制，实现了跨视角的一致性，无需复杂的3D几何约束或专门的注意力架构。

**关键设计**：ViewMask-1-to-3的关键设计包括：1) 使用MAGVIT-v2进行token化，将图像和文本转换为统一的tokens表示。2) 采用随机掩码策略，增加模型的鲁棒性。3) 使用Transformer架构，利用自注意力机制学习tokens之间的关系。4) 通过迭代token解掩码，逐步生成多个视角。损失函数主要基于token预测的交叉熵损失。

## 📊 实验亮点

ViewMask-1-to-3在GSO和3D-FUTURE数据集上取得了显著的性能提升，在PSNR、SSIM和LPIPS指标上均排名第一。这表明该方法在多视角图像生成方面具有优越的性能，并且能够有效地保持视角间的一致性。此外，该方法还具有架构简洁的优点，易于实现和部署。

## 🎯 应用场景

ViewMask-1-to-3在虚拟现实、增强现实、游戏开发等领域具有广泛的应用前景。它可以根据单张图像和文本描述生成逼真的多视角图像，为用户提供更沉浸式的体验。此外，该方法还可以应用于3D模型重建、场景理解等任务，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Multi-view image generation from a single image and text description remains challenging due to the difficulty of maintaining geometric consistency across different viewpoints. Existing approaches typically rely on 3D-aware architectures or specialized diffusion models that require extensive multi-view training data and complex geometric priors. In this work, we introduce ViewMask-1-to-3, a pioneering approach to apply discrete diffusion models to multi-view image generation. Unlike continuous diffusion methods that operate in latent spaces, ViewMask-1-to-3 formulates multi-view synthesis as a discrete sequence modeling problem, where each viewpoint is represented as visual tokens obtained through MAGVIT-v2 tokenization. By unifying language and vision through masked token prediction, our approach enables progressive generation of multiple viewpoints through iterative token unmasking with text input. ViewMask-1-to-3 achieves cross-view consistency through simple random masking combined with self-attention, eliminating the requirement for complex 3D geometric constraints or specialized attention architectures. Our approach demonstrates that discrete diffusion provides a viable and simple alternative to existing multi-view generation methods, ranking first on average across GSO and 3D-FUTURE datasets in terms of PSNR, SSIM, and LPIPS, while maintaining architectural simplicity.

