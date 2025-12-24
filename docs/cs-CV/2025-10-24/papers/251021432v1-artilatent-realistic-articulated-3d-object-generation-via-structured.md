---
layout: default
title: "ArtiLatent: Realistic Articulated 3D Object Generation via Structured Latents"
---

# ArtiLatent: Realistic Articulated 3D Object Generation via Structured Latents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.21432" class="toolbar-btn" target="_blank">📄 arXiv: 2510.21432v1</a>
  <a href="https://arxiv.org/pdf/2510.21432.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.21432v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.21432v1', 'ArtiLatent: Realistic Articulated 3D Object Generation via Structured Latents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Honghua Chen, Yushi Lan, Yongwei Chen, Xingang Pan

**分类**: cs.CV, cs.GR

**发布日期**: 2025-10-24

**备注**: accepted to SIGGRAPH Asia; Project page: https://chenhonghua.github.io/MyProjects/ArtiLatent/

---

## 💡 一句话要点

**ArtiLatent：通过结构化隐空间生成逼真可动3D物体**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱四：生成式动作 (Generative Motion)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `3D物体生成` `可动物体` `隐空间表示` `扩散模型` `铰接感知` `几何建模` `外观建模`

## 📋 核心要点

1. 现有方法难以生成具有精细几何、精确铰接和逼真外观的可动3D物体，尤其是在铰接状态变化时保持视觉一致性。
2. ArtiLatent通过结构化隐空间联合建模部件几何和铰接动态，利用隐扩散模型生成多样且物理可信的样本。
3. 实验表明，ArtiLatent在几何一致性和外观保真度上优于现有方法，尤其在铰接状态变化时能保持视觉真实感。

## 📝 摘要（中文）

我们提出了ArtiLatent，一个生成框架，用于合成具有精细几何形状、精确铰接和逼真外观的人造3D物体。我们的方法通过变分自编码器将稀疏体素表示和相关的铰接属性（包括关节类型、轴、原点、范围和部件类别）嵌入到统一的隐空间中，从而联合建模部件几何形状和铰接动态。然后，在这个空间上训练一个隐扩散模型，以实现多样但物理上合理的采样。为了重建逼真的3D形状，我们引入了一个铰接感知高斯解码器，该解码器考虑了铰接相关的可见性变化（例如，打开抽屉时露出内部）。通过将外观解码建立在铰接状态的基础上，我们的方法为静态姿势中通常被遮挡的区域分配合理的纹理特征，从而显著提高了各种铰接配置中的视觉真实感。在PartNet-Mobility和ACD数据集中，对类似家具的物体进行的大量实验表明，ArtiLatent在几何一致性和外观保真度方面优于现有方法。我们的框架为可动3D物体的合成和操作提供了一个可扩展的解决方案。

## 🔬 方法详解

**问题定义**：论文旨在解决生成具有真实感的可动3D物体的问题。现有方法在生成具有复杂几何形状、精确铰接和逼真外观的3D物体方面存在困难，尤其是在处理铰接部件的遮挡和纹理变化时，难以保证视觉一致性。

**核心思路**：论文的核心思路是将部件的几何形状和铰接属性编码到统一的隐空间中，并利用隐扩散模型生成多样化的样本。通过铰接感知的高斯解码器，考虑铰接状态对可见性的影响，从而为通常被遮挡的区域分配合理的纹理特征，提高视觉真实感。

**技术框架**：ArtiLatent框架包含以下主要模块：1) 变分自编码器（VAE），用于将稀疏体素表示和铰接属性编码到隐空间；2) 隐扩散模型，用于在隐空间中生成新的样本；3) 铰接感知高斯解码器，用于将隐空间中的样本解码为3D形状，并考虑铰接状态对可见性的影响。整体流程是先通过VAE将3D物体编码到隐空间，然后利用隐扩散模型生成新的隐空间向量，最后通过铰接感知高斯解码器将隐空间向量解码为3D物体。

**关键创新**：该论文的关键创新在于：1) 提出了一个统一的隐空间来联合建模部件几何形状和铰接动态；2) 引入了铰接感知高斯解码器，考虑了铰接状态对可见性的影响，从而提高了视觉真实感；3) 利用隐扩散模型生成多样化的样本。与现有方法相比，ArtiLatent能够生成更逼真、更具几何一致性的可动3D物体。

**关键设计**：论文使用了稀疏体素表示来表示3D物体的几何形状。铰接属性包括关节类型、轴、原点、范围和部件类别。变分自编码器的损失函数包括重建损失和KL散度。隐扩散模型使用U-Net架构。铰接感知高斯解码器通过将铰接状态作为条件输入来调整解码过程。

## 📊 实验亮点

实验结果表明，ArtiLatent在PartNet-Mobility和ACD数据集上，在几何一致性和外观保真度方面均优于现有方法。通过铰接感知解码器，ArtiLatent能够为通常被遮挡的区域分配合理的纹理特征，显著提高了视觉真实感。定性和定量结果都证明了ArtiLatent的有效性。

## 🎯 应用场景

ArtiLatent可应用于游戏开发、虚拟现实、机器人仿真等领域，为这些领域提供高质量、可定制的可动3D物体资源。该研究有助于提升虚拟环境的真实感和交互性，并为机器人操作和规划提供更逼真的环境模型。未来，该技术可扩展到更复杂的物体和场景，并应用于自动驾驶、智能家居等领域。

## 📄 摘要（原文）

> We propose ArtiLatent, a generative framework that synthesizes human-made 3D objects with fine-grained geometry, accurate articulation, and realistic appearance. Our approach jointly models part geometry and articulation dynamics by embedding sparse voxel representations and associated articulation properties, including joint type, axis, origin, range, and part category, into a unified latent space via a variational autoencoder. A latent diffusion model is then trained over this space to enable diverse yet physically plausible sampling. To reconstruct photorealistic 3D shapes, we introduce an articulation-aware Gaussian decoder that accounts for articulation-dependent visibility changes (e.g., revealing the interior of a drawer when opened). By conditioning appearance decoding on articulation state, our method assigns plausible texture features to regions that are typically occluded in static poses, significantly improving visual realism across articulation configurations. Extensive experiments on furniture-like objects from PartNet-Mobility and ACD datasets demonstrate that ArtiLatent outperforms existing approaches in geometric consistency and appearance fidelity. Our framework provides a scalable solution for articulated 3D object synthesis and manipulation.

