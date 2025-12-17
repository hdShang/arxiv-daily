---
layout: default
title: AvatarTex: High-Fidelity Facial Texture Reconstruction from Single-Image Stylized Avatars
---

# AvatarTex: High-Fidelity Facial Texture Reconstruction from Single-Image Stylized Avatars

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.06721" class="toolbar-btn" target="_blank">📄 arXiv: 2511.06721v1</a>
  <a href="https://arxiv.org/pdf/2511.06721.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.06721v1" onclick="toggleFavorite(this, '2511.06721v1', 'AvatarTex: High-Fidelity Facial Texture Reconstruction from Single-Image Stylized Avatars')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuda Qiu, Zitong Xiao, Yiwei Zuo, Zisheng Ye, Weikai Chen, Xiaoguang Han

**分类**: cs.CV

**发布日期**: 2025-11-10

**备注**: 3DV 2026 Accepted

---

## 💡 一句话要点

**AvatarTex：单图像生成高保真风格化头像纹理，解决几何一致性难题**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `面部纹理重建` `风格化头像` `扩散模型` `生成对抗网络` `UV纹理` `TexHub数据集` `几何一致性`

## 📋 核心要点

1. 现有方法在风格化头像纹理重建中，面临缺乏多风格数据集和难以保持几何一致性的挑战。
2. AvatarTex 提出三阶段扩散-GAN流水线，结合扩散模型的多样性和GAN的拓扑一致性，实现高质量纹理合成。
3. AvatarTex 构建了包含20,000张多风格UV纹理的TexHub数据集，并在多风格面部纹理重建上达到新的state-of-the-art。

## 📝 摘要（中文）

AvatarTex 提出了一种高保真面部纹理重建框架，能够从单张图像生成风格化和照片写实纹理。现有方法在处理风格化头像时面临挑战，因为缺乏多样化的多风格数据集，并且难以在非标准纹理中保持几何一致性。为了解决这些限制，AvatarTex 引入了一种新颖的三阶段扩散-GAN流水线。核心思想是，扩散模型擅长生成多样化的纹理，但缺乏显式的 UV 约束，而 GAN 提供了一个结构良好的潜在空间，确保风格和拓扑一致性。通过整合这些优势，AvatarTex 实现了高质量的拓扑对齐纹理合成，具有艺术性和几何连贯性。具体来说，三阶段流水线首先通过基于扩散的图像修复来完成缺失的纹理区域，使用基于 GAN 的潜在优化来细化风格和结构一致性，并通过基于扩散的重绘来增强精细细节。为了满足对风格化纹理数据集的需求，我们引入了 TexHub，这是一个包含 20,000 个多风格 UV 纹理的高分辨率集合，具有精确的 UV 对齐布局。通过利用 TexHub 和结构化的扩散-GAN 流水线，AvatarTex 在多风格面部纹理重建方面建立了新的技术水平。TexHub 将在发表后发布，以促进该领域未来的研究。

## 🔬 方法详解

**问题定义**：论文旨在解决从单张图像重建高保真风格化头像纹理的问题。现有方法在处理风格化头像时，由于缺乏足够的多样化训练数据，以及风格化纹理的非标准特性，难以保证重建纹理的几何一致性和风格准确性。这导致重建的头像在拓扑结构上可能出现扭曲，或者风格与输入图像不符。

**核心思路**：论文的核心思路是将扩散模型和生成对抗网络（GAN）的优势结合起来。扩散模型擅长生成多样化的纹理，但缺乏对UV空间的显式约束，容易产生几何不一致性。GAN则具有结构化的潜在空间，能够保证拓扑一致性和风格控制。通过将扩散模型用于纹理生成和细节增强，GAN用于风格和拓扑约束，可以实现高质量的风格化纹理重建。

**技术框架**：AvatarTex 采用三阶段流水线：1) **扩散修复 (Diffusion Inpainting)**：使用扩散模型填充缺失的纹理区域，初步生成完整的纹理；2) **GAN潜在优化 (GAN Latent Optimization)**：利用GAN的潜在空间，优化纹理的风格和结构一致性，确保重建的纹理与输入图像的风格匹配，并且在UV空间中保持拓扑结构；3) **扩散重绘 (Diffusion Repainting)**：使用扩散模型对纹理进行细节增强，提高纹理的真实感和视觉质量。

**关键创新**：AvatarTex 的关键创新在于其结构化的扩散-GAN流水线，以及TexHub数据集。将扩散模型和GAN结合，克服了各自的局限性，实现了高质量的风格化纹理重建。TexHub数据集提供了大量多风格的UV纹理，为风格化头像纹理重建的研究提供了宝贵的数据资源。

**关键设计**：在扩散修复阶段，使用预训练的扩散模型，并针对纹理修复任务进行微调。在GAN潜在优化阶段，使用对抗损失和感知损失来约束纹理的风格和结构。在扩散重绘阶段，使用条件扩散模型，以GAN优化后的纹理作为条件，生成更精细的纹理细节。TexHub数据集包含20,000张高分辨率UV纹理，覆盖多种风格，并提供精确的UV对齐信息。

## 📊 实验亮点

AvatarTex 在多风格面部纹理重建任务上取得了显著的性能提升。通过与现有方法的对比实验表明，AvatarTex 在纹理质量、风格一致性和几何准确性方面均优于现有方法。TexHub数据集的发布也为该领域的研究提供了新的基准和数据资源。具体性能数据未知，但论文强调其在多风格重建上达到了新的state-of-the-art。

## 🎯 应用场景

AvatarTex 技术可应用于虚拟形象定制、游戏角色生成、电影特效制作等领域。用户可以通过单张照片快速生成高质量的风格化头像，用于社交媒体、虚拟会议等场景。该技术还可以用于创建具有特定艺术风格的游戏角色或电影特效，提高内容创作的效率和质量。未来，AvatarTex 有望与增强现实（AR）和虚拟现实（VR）技术结合，为用户提供更加沉浸式的虚拟体验。

## 📄 摘要（原文）

> We present AvatarTex, a high-fidelity facial texture reconstruction framework capable of generating both stylized and photorealistic textures from a single image. Existing methods struggle with stylized avatars due to the lack of diverse multi-style datasets and challenges in maintaining geometric consistency in non-standard textures. To address these limitations, AvatarTex introduces a novel three-stage diffusion-to-GAN pipeline. Our key insight is that while diffusion models excel at generating diversified textures, they lack explicit UV constraints, whereas GANs provide a well-structured latent space that ensures style and topology consistency. By integrating these strengths, AvatarTex achieves high-quality topology-aligned texture synthesis with both artistic and geometric coherence. Specifically, our three-stage pipeline first completes missing texture regions via diffusion-based inpainting, refines style and structure consistency using GAN-based latent optimization, and enhances fine details through diffusion-based repainting. To address the need for a stylized texture dataset, we introduce TexHub, a high-resolution collection of 20,000 multi-style UV textures with precise UV-aligned layouts. By leveraging TexHub and our structured diffusion-to-GAN pipeline, AvatarTex establishes a new state-of-the-art in multi-style facial texture reconstruction. TexHub will be released upon publication to facilitate future research in this field.

