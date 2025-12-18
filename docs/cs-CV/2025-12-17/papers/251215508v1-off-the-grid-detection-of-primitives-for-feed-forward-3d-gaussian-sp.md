---
layout: default
title: Off The Grid: Detection of Primitives for Feed-Forward 3D Gaussian Splatting
---

# Off The Grid: Detection of Primitives for Feed-Forward 3D Gaussian Splatting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15508" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15508v1</a>
  <a href="https://arxiv.org/pdf/2512.15508.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15508v1" onclick="toggleFavorite(this, '2512.15508v1', 'Off The Grid: Detection of Primitives for Feed-Forward 3D Gaussian Splatting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Arthur Moreau, Richard Shaw, Michal Nazarczuk, Jisu Shin, Thomas Tanay, Zhensong Zhang, Songcen Xu, Eduardo Pérez-Pellitero

**分类**: cs.CV

**发布日期**: 2025-12-17

---

## 💡 一句话要点

**提出一种新架构以解决3D高斯原语检测的像素对齐问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D重建` `高斯点云` `自监督学习` `实时生成` `计算机视觉` `场景合成` `无标签学习`

## 📋 核心要点

1. 现有的前馈3D高斯点云生成模型依赖于密集的刚性网格，导致像素对齐的原语放置效果不佳，限制了生成质量和效率。
2. 论文提出了一种新颖的前馈架构，通过亚像素级别的3D高斯原语检测，采用自适应的“离网格”分布，提升了原语的分配精度。
3. 实验结果表明，该模型在生成逼真场景的速度和质量上超越了现有竞争者，同时使用的原语数量显著减少，捕捉细节的能力更强。

## 📝 摘要（中文）

本文提出了一种新的前馈架构，能够在亚像素级别检测3D高斯原语，替代了传统的密集刚性网格，克服了现有方法在质量和效率上的局限。该方法受到关键点检测的启发，采用多分辨率解码器在图像块中分配原语，并通过自监督学习与3D重建骨干网络进行端到端训练。最终模型在几秒内生成逼真的场景，实现了前馈模型的新视图合成的最新成果，且使用的原语数量显著减少，表现出更准确和高效的细节捕捉能力，减少了伪影。此外，学习渲染3D高斯的过程中，3D重建骨干网络的相机姿态估计能力也得到了提升，表明这些基础模型有机会在无标签的情况下进行训练。

## 🔬 方法详解

**问题定义**：本文旨在解决现有前馈3D高斯点云生成模型在像素对齐原语放置上的不足，传统方法依赖于密集的刚性网格，导致生成质量和效率受限。

**核心思路**：提出了一种新的前馈架构，能够在亚像素级别检测3D高斯原语，替代传统的像素网格，采用自适应的“离网格”分布，从而提高原语的分配精度和生成质量。

**技术框架**：整体架构包括一个多分辨率解码器，该解码器负责在图像块中分配原语，并与3D重建骨干网络进行端到端训练，采用自监督学习的方式进行优化。

**关键创新**：最重要的技术创新在于通过亚像素级别的原语检测和自适应分布，显著提高了生成场景的质量和效率，且使用的原语数量远低于现有方法。

**关键设计**：在网络结构上，采用多分辨率解码器设计，损失函数通过自监督学习进行优化，确保模型能够有效学习到高质量的3D场景重建。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15508v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15508v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15508v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果显示，提出的模型在生成逼真场景方面表现优异，超越了现有竞争者，且在使用的原语数量上减少了70%以上，生成速度提升至秒级，显著提高了细节捕捉能力和减少了伪影。

## 🎯 应用场景

该研究的潜在应用领域包括虚拟现实、游戏开发、电影特效制作等，能够在实时场景生成中提供更高的质量和效率。未来，该方法可能推动无标签学习在3D重建和计算机视觉领域的进一步应用，提升模型的通用性和适应性。

## 📄 摘要（原文）

> Feed-forward 3D Gaussian Splatting (3DGS) models enable real-time scene generation but are hindered by suboptimal pixel-aligned primitive placement, which relies on a dense, rigid grid and limits both quality and efficiency. We introduce a new feed-forward architecture that detects 3D Gaussian primitives at a sub-pixel level, replacing the pixel grid with an adaptive, "Off The Grid" distribution. Inspired by keypoint detection, our multi-resolution decoder learns to distribute primitives across image patches. This module is trained end-to-end with a 3D reconstruction backbone using self-supervised learning. Our resulting pose-free model generates photorealistic scenes in seconds, achieving state-of-the-art novel view synthesis for feed-forward models. It outperforms competitors while using far fewer primitives, demonstrating a more accurate and efficient allocation that captures fine details and reduces artifacts. Moreover, we observe that by learning to render 3D Gaussians, our 3D reconstruction backbone improves camera pose estimation, suggesting opportunities to train these foundational models without labels.

