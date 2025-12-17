---
layout: default
title: DriveGen3D: Boosting Feed-Forward Driving Scene Generation with Efficient Video Diffusion
---

# DriveGen3D: Boosting Feed-Forward Driving Scene Generation with Efficient Video Diffusion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.15264" class="toolbar-btn" target="_blank">📄 arXiv: 2510.15264v1</a>
  <a href="https://arxiv.org/pdf/2510.15264.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.15264v1" onclick="toggleFavorite(this, '2510.15264v1', 'DriveGen3D: Boosting Feed-Forward Driving Scene Generation with Efficient Video Diffusion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weijie Wang, Jiagang Zhu, Zeyu Zhang, Xiaofeng Wang, Zheng Zhu, Guosheng Zhao, Chaojun Ni, Haoxiao Wang, Guan Huang, Xinze Chen, Yukun Zhou, Wenkang Qin, Duochao Shi, Haoyun Li, Guanghong Jia, Jiwen Lu

**分类**: cs.CV

**发布日期**: 2025-10-17

**备注**: Accepted by NeurIPS Workshop on Next Practices in Video Generation and Evaluation (Short Paper Track)

---

## 💡 一句话要点

**DriveGen3D：通过高效视频扩散加速前馈式驾驶场景生成**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `驾驶场景生成` `3D重建` `视频扩散模型` `动态场景` `自动驾驶仿真`

## 📋 核心要点

1. 现有驾驶场景生成方法在计算效率、3D表示和时序一致性方面存在局限性，难以生成高质量、长时序的动态3D场景。
2. DriveGen3D通过结合高效视频扩散模型FastDrive-DiT和快速3D重建模块FastRecon3D，实现了高质量、可控的动态3D驾驶场景生成。
3. 实验表明，DriveGen3D能够实时生成长时驾驶视频和对应的动态3D场景，并在novel view synthesis上取得了优异的性能指标。

## 📝 摘要（中文）

DriveGen3D是一个新颖的框架，旨在生成高质量且高度可控的动态3D驾驶场景，解决了现有方法的关键局限性。目前驾驶场景合成方法要么在长时间序列生成中面临巨大的计算需求，要么专注于长时间视频合成而缺乏3D表示，要么仅限于静态单场景重建。DriveGen3D通过多模态条件控制，将加速的长时视频生成与大规模动态场景重建相结合，弥合了这一方法论差距。DriveGen3D引入了一个统一的流程，包含两个专门的组件：FastDrive-DiT，一个高效的视频扩散Transformer，用于在文本和鸟瞰图（BEV）布局指导下进行高分辨率、时间一致的视频合成；以及FastRecon3D，一个前馈重建模块，可以快速构建跨时间的3D高斯表示，确保时空一致性。这些组件共同实现了扩展驾驶视频（高达424x800，12 FPS）和相应动态3D场景的实时生成，在novel view synthesis上实现了0.811的SSIM和22.84的PSNR，同时保持了参数效率。

## 🔬 方法详解

**问题定义**：现有方法在生成动态3D驾驶场景时，面临计算量大、缺乏3D表示或时序一致性差等问题。具体来说，基于扩散模型的方法计算成本高昂，难以生成长时视频；而一些方法虽然可以生成长时视频，但缺乏3D信息；另一些方法则仅限于静态场景的重建，无法处理动态场景。

**核心思路**：DriveGen3D的核心思路是将高效的视频扩散模型与快速3D重建模块相结合，从而实现高质量、可控的动态3D驾驶场景生成。通过视频扩散模型生成具有时序一致性的视频，然后利用3D重建模块将视频转换为动态3D场景。

**技术框架**：DriveGen3D包含两个主要模块：FastDrive-DiT和FastRecon3D。FastDrive-DiT是一个基于扩散Transformer的视频生成模型，用于生成高分辨率、时间一致的驾驶视频，它接受文本和鸟瞰图（BEV）布局作为条件输入。FastRecon3D是一个前馈重建模块，用于快速构建跨时间的3D高斯表示，从而实现动态3D场景的重建。

**关键创新**：DriveGen3D的关键创新在于将高效的视频扩散模型与快速3D重建模块相结合，从而实现了动态3D驾驶场景的实时生成。此外，该框架还采用了多模态条件控制，可以根据文本和BEV布局生成不同的驾驶场景。

**关键设计**：FastDrive-DiT采用了扩散Transformer架构，并针对视频生成进行了优化，例如使用高效的注意力机制和时间卷积。FastRecon3D采用了前馈网络结构，可以快速地从视频中重建3D场景。损失函数方面，可能使用了重建损失、时间一致性损失等。

## 📊 实验亮点

DriveGen3D能够以12 FPS的速度实时生成424x800分辨率的驾驶视频和对应的动态3D场景。在novel view synthesis任务中，DriveGen3D取得了0.811的SSIM和22.84的PSNR，表明其生成的场景具有高质量和时空一致性。同时，该方法保持了参数效率，降低了计算成本。

## 🎯 应用场景

DriveGen3D可应用于自动驾驶仿真、游戏开发、虚拟现实等领域。它可以生成各种逼真的驾驶场景，用于训练自动驾驶系统、创建游戏世界或提供沉浸式虚拟体验。该研究有助于推动自动驾驶技术的发展，并为相关产业带来新的机遇。

## 📄 摘要（原文）

> We present DriveGen3D, a novel framework for generating high-quality and highly controllable dynamic 3D driving scenes that addresses critical limitations in existing methodologies. Current approaches to driving scene synthesis either suffer from prohibitive computational demands for extended temporal generation, focus exclusively on prolonged video synthesis without 3D representation, or restrict themselves to static single-scene reconstruction. Our work bridges this methodological gap by integrating accelerated long-term video generation with large-scale dynamic scene reconstruction through multimodal conditional control. DriveGen3D introduces a unified pipeline consisting of two specialized components: FastDrive-DiT, an efficient video diffusion transformer for high-resolution, temporally coherent video synthesis under text and Bird's-Eye-View (BEV) layout guidance; and FastRecon3D, a feed-forward reconstruction module that rapidly builds 3D Gaussian representations across time, ensuring spatial-temporal consistency. Together, these components enable real-time generation of extended driving videos (up to $424\times800$ at 12 FPS) and corresponding dynamic 3D scenes, achieving SSIM of 0.811 and PSNR of 22.84 on novel view synthesis, all while maintaining parameter efficiency.

