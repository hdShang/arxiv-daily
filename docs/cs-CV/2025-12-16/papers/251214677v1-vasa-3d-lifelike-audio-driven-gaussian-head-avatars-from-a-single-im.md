---
layout: default
title: VASA-3D: Lifelike Audio-Driven Gaussian Head Avatars from a Single Image
---

# VASA-3D: Lifelike Audio-Driven Gaussian Head Avatars from a Single Image

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14677" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14677v1</a>
  <a href="https://arxiv.org/pdf/2512.14677.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14677v1" onclick="toggleFavorite(this, '2512.14677v1', 'VASA-3D: Lifelike Audio-Driven Gaussian Head Avatars from a Single Image')" title="添加到收藏夹">☆ 收藏</button>
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

**关键词**: `3D头部化身` `音频驱动` `单张图像` `表情建模` `高斯头部` `自由视点视频` `VASA-1` `运动潜在空间`

## 📋 核心要点

1. 现有方法难以从单张图像生成具有细微表情的逼真3D头部化身，尤其是在捕捉真实感和细节方面存在挑战。
2. VASA-3D的核心思想是将VASA-1的2D运动潜在空间迁移到3D头部模型，从而实现对表情细节的精确建模和控制。
3. 实验结果表明，VASA-3D能够生成逼真的3D说话头部，并支持高达75 FPS的自由视点视频生成，显著提升了用户体验。

## 📝 摘要（中文）

本文提出VASA-3D，一种音频驱动的、单张图像3D头部化身生成器。该研究旨在解决两个主要挑战：捕捉真实人脸中细微的表情细节，以及从单张人像图像中重建复杂的3D头部化身。为了准确地建模表情细节，VASA-3D利用了VASA-1的运动潜在空间，该方法在2D说话头部生成方面表现出卓越的真实感和生动性。本文的关键在于将这种运动潜在空间转化为3D，这通过设计一个以运动潜在空间为条件的3D头部模型来实现。通过一个优化框架，利用从输入图像合成的参考头部的大量视频帧，实现对该模型的单张图像定制。该优化过程采用了对伪影和生成训练数据中有限的姿态覆盖具有鲁棒性的各种训练损失。实验表明，VASA-3D生成了逼真的3D说话头部，这是现有技术无法实现的，并且它支持以高达75 FPS的速度在线生成512x512自由视点视频，从而促进了与逼真3D化身更具沉浸感的互动。

## 🔬 方法详解

**问题定义**：论文旨在解决从单张图像生成逼真且具有细微表情的3D头部化身的问题。现有方法在捕捉真实人脸的细微表情细节以及从单张图像重建复杂的3D头部化身方面存在困难，生成的3D化身往往缺乏真实感和生动性。

**核心思路**：论文的核心思路是将VASA-1在2D说话头部生成方面的优势，即其优秀的运动潜在空间，迁移到3D头部模型的构建中。通过将3D头部模型与VASA-1的运动潜在空间相结合，可以实现对表情细节的精确建模和控制，从而生成更逼真的3D头部化身。这种设计思路的关键在于利用2D领域的先进技术来提升3D头部化身的生成质量。

**技术框架**：VASA-3D的整体框架包含以下几个主要模块：1) 利用VASA-1的运动潜在空间来驱动3D头部模型的形变；2) 设计一个以运动潜在空间为条件的3D头部模型；3) 通过优化框架，利用从输入图像合成的参考头部视频帧，实现对3D头部模型的单张图像定制；4) 使用对伪影和有限姿态覆盖具有鲁棒性的训练损失进行优化。整个流程从单张图像开始，经过一系列处理，最终生成逼真的3D说话头部。

**关键创新**：VASA-3D最重要的技术创新点在于将2D说话头部生成领域的先进技术（VASA-1的运动潜在空间）成功地迁移到3D头部化身生成中。与现有方法相比，VASA-3D能够更准确地捕捉和建模人脸的细微表情细节，从而生成更逼真、更生动的3D头部化身。此外，VASA-3D还提出了一种有效的单张图像定制方法，使得用户可以使用自己的照片快速生成个性化的3D化身。

**关键设计**：在关键设计方面，论文采用了以下技术细节：1) 设计了一个以运动潜在空间为条件的3D头部模型，该模型能够根据VASA-1的运动潜在空间进行形变，从而实现对表情的控制；2) 提出了一个优化框架，该框架利用从输入图像合成的参考头部视频帧来定制3D头部模型，并采用各种对伪影和有限姿态覆盖具有鲁棒性的训练损失，例如光度一致性损失、landmark损失等；3) 为了提高生成速度，VASA-3D采用了高斯头部表示，并进行了优化，最终实现了高达75 FPS的自由视点视频生成。

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

VASA-3D实验结果表明，其生成的3D说话头部在真实感和生动性方面超越了现有技术。VASA-3D支持以高达75 FPS的速度在线生成512x512自由视点视频，这使得用户可以与3D化身进行更流畅、更自然的互动。通过单张图像即可生成个性化3D化身，极大地降低了使用门槛。这些实验结果充分证明了VASA-3D在3D头部化身生成领域的领先地位。

## 🎯 应用场景

VASA-3D具有广泛的应用前景，例如虚拟会议、在线教育、游戏、社交媒体等。它可以用于创建个性化的3D虚拟形象，提升用户在虚拟环境中的沉浸感和互动体验。此外，VASA-3D还可以应用于数字内容创作，例如电影、动画等，为角色设计和动画制作提供新的工具和方法。未来，VASA-3D有望成为元宇宙等新兴领域的重要组成部分。

## 📄 摘要（原文）

> We propose VASA-3D, an audio-driven, single-shot 3D head avatar generator. This research tackles two major challenges: capturing the subtle expression details present in real human faces, and reconstructing an intricate 3D head avatar from a single portrait image. To accurately model expression details, VASA-3D leverages the motion latent of VASA-1, a method that yields exceptional realism and vividness in 2D talking heads. A critical element of our work is translating this motion latent to 3D, which is accomplished by devising a 3D head model that is conditioned on the motion latent. Customization of this model to a single image is achieved through an optimization framework that employs numerous video frames of the reference head synthesized from the input image. The optimization takes various training losses robust to artifacts and limited pose coverage in the generated training data. Our experiment shows that VASA-3D produces realistic 3D talking heads that cannot be achieved by prior art, and it supports the online generation of 512x512 free-viewpoint videos at up to 75 FPS, facilitating more immersive engagements with lifelike 3D avatars.

