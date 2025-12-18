---
layout: default
title: VASA-3D: Lifelike Audio-Driven Gaussian Head Avatars from a Single Image
---

# VASA-3D: Lifelike Audio-Driven Gaussian Head Avatars from a Single Image

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14677" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14677v1</a>
  <a href="https://arxiv.org/pdf/2512.14677.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14677v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14677v1', 'VASA-3D: Lifelike Audio-Driven Gaussian Head Avatars from a Single Image')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sicheng Xu, Guojun Chen, Jiaolong Yang, Yizhong Zhang, Yu Deng, Steve Lin, Baining Guo

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-16

**备注**: NeurIPS 2025 paper. Project webpage: https://www.microsoft.com/en-us/research/project/vasa-3d/

---

## 💡 一句话要点

**VASA-3D：基于单张图像的逼真音频驱动高斯头部化身生成**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `3D头部化身` `音频驱动` `单张图像重建` `运动潜在空间` `人脸表情建模`

## 📋 核心要点

1. 现有方法难以从单张图像生成具有细微表情的逼真3D头部化身，尤其是在音频驱动的情况下。
2. VASA-3D的核心在于将VASA-1的2D运动潜在空间迁移到3D头部模型，并利用单张图像进行个性化定制。
3. 实验表明，VASA-3D能够生成逼真的3D说话头部，并支持高达75 FPS的自由视点视频生成。

## 📝 摘要（中文）

本文提出VASA-3D，一种音频驱动的单张图像3D头部化身生成器。该研究解决了两个主要挑战：捕捉真实人脸中细微的表情细节，以及从单张人像图像重建复杂的3D头部化身。为了准确地建模表情细节，VASA-3D利用了VASA-1的运动潜在空间，该方法在2D说话头部中产生了卓越的真实感和生动性。本文工作的一个关键要素是将这种运动潜在空间转化为3D，这是通过设计一个以运动潜在空间为条件的3D头部模型来实现的。通过一个优化框架来实现该模型对单张图像的定制，该框架采用了从输入图像合成的参考头部的大量视频帧。该优化采用了对伪影和生成训练数据中有限的姿态覆盖具有鲁棒性的各种训练损失。实验表明，VASA-3D生成了逼真的3D说话头部，这是现有技术无法实现的，并且它支持以高达75 FPS的速度在线生成512x512自由视点视频，从而促进了与逼真3D化身更具沉浸感的互动。

## 🔬 方法详解

**问题定义**：论文旨在解决从单张人像图像生成逼真、音频驱动的3D头部化身的问题。现有方法在捕捉细微表情细节和实现高真实感方面存在不足，并且难以从有限的单张图像数据中重建复杂的3D结构。

**核心思路**：论文的核心思路是利用VASA-1在2D说话头部生成方面的优势，将其运动潜在空间迁移到3D头部模型中。通过将3D头部模型与VASA-1的运动潜在空间相结合，可以更好地捕捉和表达面部表情的细微变化。同时，通过优化框架，利用从单张输入图像合成的视频帧，实现模型的个性化定制。

**技术框架**：VASA-3D的整体框架包含以下几个主要阶段：1) 利用VASA-1的运动潜在空间生成2D说话头部视频；2) 设计一个以运动潜在空间为条件的3D头部模型；3) 通过优化框架，利用从单张输入图像合成的视频帧，对3D头部模型进行个性化定制；4) 利用训练好的3D头部模型，根据输入的音频生成逼真的3D说话头部视频。

**关键创新**：最重要的技术创新点在于将VASA-1的2D运动潜在空间成功地迁移到3D头部模型中。这种迁移使得VASA-3D能够更好地捕捉和表达面部表情的细微变化，从而生成更逼真的3D说话头部。与现有方法相比，VASA-3D能够从单张图像中重建更复杂的3D结构，并生成更高质量的音频驱动的3D头部化身。

**关键设计**：在优化框架中，论文采用了多种训练损失，以提高模型的鲁棒性，并减少伪影。这些损失函数包括：图像重建损失、运动损失和正则化损失。此外，论文还设计了一种特殊的网络结构，用于将运动潜在空间映射到3D头部模型的参数空间。具体的参数设置和网络结构细节在论文中有详细描述。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14677v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14677v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14677v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，VASA-3D能够生成比现有技术更逼真的3D说话头部。它可以支持以高达75 FPS的速度在线生成512x512自由视点视频。与现有方法相比，VASA-3D在面部表情的真实感和细节方面有显著提升。通过消融实验，验证了各个模块对最终性能的贡献。

## 🎯 应用场景

VASA-3D具有广泛的应用前景，包括虚拟现实、增强现实、游戏、在线会议、数字人等领域。它可以用于创建个性化的3D化身，从而增强用户在虚拟环境中的沉浸感和互动性。此外，VASA-3D还可以用于生成逼真的数字替身，用于远程呈现和虚拟助手等应用。该技术有望在未来改变人与计算机的交互方式。

## 📄 摘要（原文）

> We propose VASA-3D, an audio-driven, single-shot 3D head avatar generator. This research tackles two major challenges: capturing the subtle expression details present in real human faces, and reconstructing an intricate 3D head avatar from a single portrait image. To accurately model expression details, VASA-3D leverages the motion latent of VASA-1, a method that yields exceptional realism and vividness in 2D talking heads. A critical element of our work is translating this motion latent to 3D, which is accomplished by devising a 3D head model that is conditioned on the motion latent. Customization of this model to a single image is achieved through an optimization framework that employs numerous video frames of the reference head synthesized from the input image. The optimization takes various training losses robust to artifacts and limited pose coverage in the generated training data. Our experiment shows that VASA-3D produces realistic 3D talking heads that cannot be achieved by prior art, and it supports the online generation of 512x512 free-viewpoint videos at up to 75 FPS, facilitating more immersive engagements with lifelike 3D avatars.

