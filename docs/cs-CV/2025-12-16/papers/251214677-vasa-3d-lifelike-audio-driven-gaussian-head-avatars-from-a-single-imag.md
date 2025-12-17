---
layout: default
title: VASA-3D: Lifelike Audio-Driven Gaussian Head Avatars from a Single Image
---

# VASA-3D: Lifelike Audio-Driven Gaussian Head Avatars from a Single Image

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14677" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14677</a>
  <a href="https://arxiv.org/pdf/2512.14677.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14677" onclick="toggleFavorite(this, '2512.14677', 'VASA-3D: Lifelike Audio-Driven Gaussian Head Avatars from a Single Image')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sicheng Xu, Guojun Chen, Jiaolong Yang, Yizhong Zhang, Yu Deng, Steve Lin, Baining Guo

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**VASA-3D：基于单张图像的逼真音频驱动高斯头部化身生成**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `3D头部化身` `音频驱动` `单张图像重建` `高斯头部` `运动潜在空间` `表情建模` `自由视点视频`

## 📋 核心要点

1. 现有方法难以从单张图像生成具有真实表情细节的3D头部化身，尤其是在捕捉细微的面部运动方面。
2. VASA-3D的核心思想是将VASA-1的2D运动潜在空间迁移到3D头部模型，从而驱动3D化身的表情。
3. 实验表明，VASA-3D能够生成逼真的3D说话头部，并支持高达75 FPS的自由视点视频生成，优于现有技术。

## 📝 摘要（中文）

本文提出VASA-3D，一种音频驱动的单张图像3D头部化身生成器。该研究旨在解决两个主要挑战：捕捉真实人脸中细微的表情细节，以及从单张人像图像重建复杂的3D头部化身。为了准确地建模表情细节，VASA-3D利用了VASA-1的运动潜在空间，该方法在2D说话头部生成方面表现出卓越的真实感和生动性。本文的关键在于将这种运动潜在空间转化为3D，这是通过设计一个以运动潜在空间为条件的3D头部模型来实现的。通过一个优化框架，利用从输入图像合成的参考头部的大量视频帧，实现对该模型的单张图像定制。该优化框架采用了对伪影和生成训练数据中有限姿态覆盖具有鲁棒性的各种训练损失。实验表明，VASA-3D生成了逼真的3D说话头部，这是现有技术无法实现的，并且它支持以高达75 FPS的速度在线生成512x512自由视点视频，从而促进了与逼真3D化身更具沉浸感的互动。

## 🔬 方法详解

**问题定义**：论文旨在解决从单张人像图像生成逼真且可控的3D头部化身的问题。现有方法在捕捉细微表情细节和处理单张图像的3D重建方面存在不足，生成的3D化身真实感较差，难以满足高质量应用的需求。

**核心思路**：论文的核心思路是利用VASA-1在2D说话头部生成方面的优势，将其学习到的运动潜在空间迁移到3D头部模型。通过将3D头部模型与2D运动潜在空间解耦，可以实现对3D化身表情的精确控制，并提高生成结果的真实感。

**技术框架**：VASA-3D的整体框架包含以下几个主要阶段：1) 利用VASA-1的运动潜在空间提取表情信息；2) 设计一个以运动潜在空间为条件的3D头部模型；3) 通过优化框架，利用从单张输入图像合成的视频帧，对3D头部模型进行个性化定制；4) 使用鲁棒的损失函数进行训练，以克服伪影和有限姿态覆盖的问题。

**关键创新**：该论文最重要的技术创新点在于将2D运动潜在空间成功迁移到3D头部模型，从而实现了对3D化身表情的精确控制。与现有方法相比，VASA-3D能够生成更逼真、更生动的3D说话头部，并且支持自由视点视频生成。

**关键设计**：论文的关键设计包括：1) 使用高斯头部表示3D模型；2) 设计了以运动潜在空间为条件的3D头部模型结构；3) 采用了多种损失函数，包括光度一致性损失、正则化损失等，以提高生成结果的质量和鲁棒性；4) 使用了从单张图像合成的视频帧进行训练，以克服数据稀缺的问题。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14677/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14677/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14677/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

VASA-3D在生成逼真3D说话头部方面取得了显著成果，能够生成具有细微表情细节的3D化身。实验结果表明，VASA-3D生成的3D头部化身在真实感和生动性方面优于现有技术。此外，VASA-3D还支持以高达75 FPS的速度在线生成512x512自由视点视频，为实时应用提供了可能。

## 🎯 应用场景

VASA-3D具有广泛的应用前景，包括虚拟会议、游戏、社交媒体、教育和娱乐等领域。它可以用于创建个性化的3D化身，增强用户在虚拟环境中的沉浸感和互动性。此外，该技术还可以应用于数字内容创作，例如生成逼真的虚拟角色和动画。

## 📄 摘要（原文）

> We propose VASA-3D, an audio-driven, single-shot 3D head avatar generator. This research tackles two major challenges: capturing the subtle expression details present in real human faces, and reconstructing an intricate 3D head avatar from a single portrait image. To accurately model expression details, VASA-3D leverages the motion latent of VASA-1, a method that yields exceptional realism and vividness in 2D talking heads. A critical element of our work is translating this motion latent to 3D, which is accomplished by devising a 3D head model that is conditioned on the motion latent. Customization of this model to a single image is achieved through an optimization framework that employs numerous video frames of the reference head synthesized from the input image. The optimization takes various training losses robust to artifacts and limited pose coverage in the generated training data. Our experiment shows that VASA-3D produces realistic 3D talking heads that cannot be achieved by prior art, and it supports the online generation of 512x512 free-viewpoint videos at up to 75 FPS, facilitating more immersive engagements with lifelike 3D avatars.

