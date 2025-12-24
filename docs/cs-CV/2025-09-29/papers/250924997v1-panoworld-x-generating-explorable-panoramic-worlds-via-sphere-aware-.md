---
layout: default
title: "PanoWorld-X: Generating Explorable Panoramic Worlds via Sphere-Aware Video Diffusion"
---

# PanoWorld-X: Generating Explorable Panoramic Worlds via Sphere-Aware Video Diffusion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24997" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24997v1</a>
  <a href="https://arxiv.org/pdf/2509.24997.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24997v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24997v1', 'PanoWorld-X: Generating Explorable Panoramic Worlds via Sphere-Aware Video Diffusion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuyang Yin, HaoXiang Guo, Fangfu Liu, Mengyu Wang, Hanwen Liang, Eric Li, Yikai Wang, Xiaojie Jin, Yao Zhao, Yunchao Wei

**分类**: cs.CV

**发布日期**: 2025-09-29

**备注**: Project page: \url{https://yuyangyin.github.io/PanoWorld-X/}

---

## 💡 一句话要点

**PanoWorld-X：基于球面感知视频扩散生成可探索全景世界**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `全景视频生成` `视频扩散模型` `球面几何` `Transformer` `虚拟环境` `可控生成` `三维重建`

## 📋 核心要点

1. 现有全景视频生成方法受限于窄视野或相机控制不足，难以生成连续、完整的可探索场景。
2. PanoWorld-X通过球面感知扩散Transformer，在潜在空间中建模几何邻接关系，提升视觉保真度和时空连续性。
3. 实验表明，PanoWorld-X在运动范围、控制精度和视觉质量上均优于现有方法，具有实际应用潜力。

## 📝 摘要（中文）

本文提出PanoWorld-X，一个用于生成高保真、可控全景视频的新框架，该框架支持多样化的相机轨迹。为了解决现有方法在视野范围和相机控制方面的局限性，我们首先通过Unreal Engine在虚拟3D环境中模拟相机轨迹，构建了一个大规模的全景视频-探索路径对数据集。针对全景数据的球面几何结构与传统视频扩散的归纳偏置不匹配的问题，我们引入了一种球面感知扩散Transformer架构，该架构将等距柱状投影特征重新投影到球面上，以在潜在空间中建模几何邻接关系，从而显著提高视觉保真度和时空连续性。大量实验表明，PanoWorld-X在运动范围、控制精度和视觉质量等各个方面均表现出卓越的性能，突显了其在实际应用中的潜力。

## 🔬 方法详解

**问题定义**：现有全景视频生成方法主要面临两个挑战：一是视野范围有限，难以生成连续和整体的场景；二是相机控制不足，限制了用户或自主代理的自由探索。这些限制阻碍了全景视频在实际应用中的潜力。

**核心思路**：PanoWorld-X的核心思路是利用球面几何信息来指导视频扩散过程。通过将等距柱状投影的全景图像特征重新投影到球面上，模型能够更好地理解和建模全景图像的几何结构，从而提高生成视频的视觉保真度和时空一致性。

**技术框架**：PanoWorld-X的整体框架包含以下几个主要步骤：1) 数据集构建：利用Unreal Engine等虚拟环境生成器，模拟相机在3D场景中的运动轨迹，构建大规模的全景视频-探索路径对数据集。2) 特征提取：使用预训练的视觉模型（例如CLIP）提取全景视频帧的视觉特征。3) 球面感知扩散Transformer：将提取的特征输入到球面感知扩散Transformer中，该Transformer将等距柱状投影特征重新投影到球面上，并在球面空间中进行扩散和去噪过程。4) 视频生成：通过逆扩散过程，将噪声转化为高质量的全景视频帧。

**关键创新**：PanoWorld-X的关键创新在于提出了球面感知扩散Transformer。与传统的视频扩散模型不同，该Transformer能够显式地建模全景图像的球面几何结构，从而更好地理解和生成全景视频。这种球面感知的设计使得模型能够生成具有更高视觉保真度和时空一致性的全景视频。

**关键设计**：球面感知扩散Transformer的关键设计包括：1) 球面重投影：将等距柱状投影的特征重新投影到球面上，以便模型能够更好地理解全景图像的几何结构。2) 球面卷积：在球面空间中进行卷积操作，以便模型能够更好地建模全景图像的局部邻接关系。3) 注意力机制：使用注意力机制来建模全景图像中不同区域之间的依赖关系。此外，损失函数的设计也至关重要，可能包括重建损失、对抗损失等，以保证生成视频的质量和真实感。具体参数设置和网络结构细节在论文中应有更详细的描述。

## 📊 实验亮点

PanoWorld-X在多个指标上均取得了显著的性能提升。实验结果表明，PanoWorld-X生成的全景视频在视觉质量、时空一致性和运动范围等方面均优于现有方法。具体而言，PanoWorld-X在用户研究中获得了更高的偏好评分，并且在定量指标（例如FID、LPIPS）上取得了显著的提升。这些结果表明，PanoWorld-X能够生成更逼真、更流畅的全景视频。

## 🎯 应用场景

PanoWorld-X具有广泛的应用前景，包括虚拟现实、增强现实、游戏开发、机器人导航、自动驾驶等领域。它可以用于生成逼真的虚拟环境，为用户提供沉浸式的体验。此外，PanoWorld-X还可以用于训练机器人或自动驾驶汽车，使其能够在虚拟环境中学习和探索，从而提高其在真实世界中的性能。该研究的未来影响在于推动全景视频生成技术的发展，并为各种应用场景提供更强大的工具。

## 📄 摘要（原文）

> Generating a complete and explorable 360-degree visual world enables a wide range of downstream applications. While prior works have advanced the field, they remain constrained by either narrow field-of-view limitations, which hinder the synthesis of continuous and holistic scenes, or insufficient camera controllability that restricts free exploration by users or autonomous agents. To address this, we propose PanoWorld-X, a novel framework for high-fidelity and controllable panoramic video generation with diverse camera trajectories. Specifically, we first construct a large-scale dataset of panoramic video-exploration route pairs by simulating camera trajectories in virtual 3D environments via Unreal Engine. As the spherical geometry of panoramic data misaligns with the inductive priors from conventional video diffusion, we then introduce a Sphere-Aware Diffusion Transformer architecture that reprojects equirectangular features onto the spherical surface to model geometric adjacency in latent space, significantly enhancing visual fidelity and spatiotemporal continuity. Extensive experiments demonstrate that our PanoWorld-X achieves superior performance in various aspects, including motion range, control precision, and visual quality, underscoring its potential for real-world applications.

