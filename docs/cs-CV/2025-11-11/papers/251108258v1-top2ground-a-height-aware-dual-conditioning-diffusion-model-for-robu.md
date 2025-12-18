---
layout: default
title: Top2Ground: A Height-Aware Dual Conditioning Diffusion Model for Robust Aerial-to-Ground View Generation
---

# Top2Ground: A Height-Aware Dual Conditioning Diffusion Model for Robust Aerial-to-Ground View Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.08258" class="toolbar-btn" target="_blank">📄 arXiv: 2511.08258v1</a>
  <a href="https://arxiv.org/pdf/2511.08258.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.08258v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.08258v1', 'Top2Ground: A Height-Aware Dual Conditioning Diffusion Model for Robust Aerial-to-Ground View Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jae Joong Lee, Bedrich Benes

**分类**: cs.CV

**发布日期**: 2025-11-11

---

## 💡 一句话要点

**提出Top2Ground，一种高程感知双重条件扩散模型，用于稳健的航拍图到地视图生成。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `航拍图像` `地视图生成` `扩散模型` `VAE` `CLIP` `条件生成` `高度图`

## 📋 核心要点

1. 从航拍图像生成地视图图像极具挑战性，主要由于视角差异大、遮挡严重以及视野范围有限。
2. Top2Ground的核心思想是利用扩散模型，并结合VAE编码的空间特征（包含高度信息）和CLIP语义嵌入进行条件控制。
3. 实验结果表明，Top2Ground在CVUSA、CVACT和Auto Arborist数据集上，SSIM指标平均提升7.3%，泛化能力强。

## 📝 摘要（中文）

本文提出Top2Ground，一种新颖的基于扩散模型的方法，用于直接从航拍图像生成逼真的地视图图像，而无需依赖深度图或3D体素等中间表示。该方法通过VAE编码的空间特征（源自航拍RGB图像和估计的高度图）和基于CLIP的语义嵌入的联合表示来调节去噪过程。这种设计确保了生成结果在几何上受到场景3D结构的约束，并在语义上与其内容保持一致。在CVUSA、CVACT和Auto Arborist三个不同的数据集上评估了Top2Ground。结果表明，该方法在三个基准数据集上的SSIM平均提高了7.3%，表明Top2Ground可以稳健地处理宽视野和窄视野，突出了其强大的泛化能力。

## 🔬 方法详解

**问题定义**：论文旨在解决从航拍图像生成对应地视图图像的问题。现有方法通常依赖于中间表示，如深度图或3D体素，这可能引入额外的误差，并且计算成本较高。此外，视角差异大、遮挡严重和视野范围有限等因素也增加了生成高质量地视图图像的难度。

**核心思路**：Top2Ground的核心思路是直接利用扩散模型从航拍图像生成地视图图像，避免使用中间表示。通过将VAE编码的空间特征（包含高度信息）和CLIP语义嵌入作为条件输入到扩散模型中，实现几何约束和语义一致性。高度信息能够提供场景的3D结构信息，CLIP语义嵌入则保证生成图像的内容与航拍图像一致。

**技术框架**：Top2Ground的整体框架包括以下几个主要模块：1) 航拍图像和高度图编码：使用VAE编码航拍RGB图像和估计的高度图，提取空间特征。2) 语义嵌入：使用CLIP模型提取航拍图像的语义嵌入。3) 扩散模型：使用扩散模型进行图像生成，并将VAE编码的空间特征和CLIP语义嵌入作为条件输入。4) 图像解码：使用VAE解码器将扩散模型生成的潜在表示解码为地视图图像。

**关键创新**：Top2Ground的关键创新在于其双重条件控制机制。一方面，利用VAE编码的空间特征（包含高度信息）对生成过程进行几何约束，确保生成的地视图图像在几何结构上与航拍图像一致。另一方面，利用CLIP语义嵌入对生成过程进行语义约束，保证生成的地视图图像在内容上与航拍图像一致。这种双重条件控制机制能够有效地提高生成地视图图像的质量和真实感。

**关键设计**：在VAE编码器和解码器方面，使用了标准的卷积神经网络结构。高度图的估计方法未知，论文中未详细描述。扩散模型采用U-Net结构，并将VAE编码的空间特征和CLIP语义嵌入通过自适应归一化（Adaptive Normalization）的方式融入到U-Net的每一层中。损失函数包括VAE的重构损失和扩散模型的噪声预测损失。

## 📊 实验亮点

Top2Ground在CVUSA、CVACT和Auto Arborist三个数据集上进行了评估，实验结果表明，该方法在三个基准数据集上的SSIM平均提高了7.3%。尤其是在处理具有挑战性的CVUSA数据集时，Top2Ground表现出更强的鲁棒性和泛化能力，能够生成更逼真、更准确的地视图图像。

## 🎯 应用场景

Top2Ground技术可应用于城市规划、自动驾驶、环境监测、灾害评估等领域。例如，在城市规划中，可以利用航拍图像生成地视图图像，辅助设计师进行方案设计和可视化展示。在自动驾驶中，可以利用航拍图像生成车辆周围的场景图像，提高车辆的感知能力。该技术还可用于构建更真实的虚拟现实和增强现实体验。

## 📄 摘要（原文）

> Generating ground-level images from aerial views is a challenging task due to extreme viewpoint disparity, occlusions, and a limited field of view. We introduce Top2Ground, a novel diffusion-based method that directly generates photorealistic ground-view images from aerial input images without relying on intermediate representations such as depth maps or 3D voxels. Specifically, we condition the denoising process on a joint representation of VAE-encoded spatial features (derived from aerial RGB images and an estimated height map) and CLIP-based semantic embeddings. This design ensures the generation is both geometrically constrained by the scene's 3D structure and semantically consistent with its content. We evaluate Top2Ground on three diverse datasets: CVUSA, CVACT, and the Auto Arborist. Our approach shows 7.3% average improvement in SSIM across three benchmark datasets, showing Top2Ground can robustly handle both wide and narrow fields of view, highlighting its strong generalization capabilities.

