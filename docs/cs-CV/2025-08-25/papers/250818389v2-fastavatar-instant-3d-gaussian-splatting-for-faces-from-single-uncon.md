---
layout: default
title: "FastAvatar: Instant 3D Gaussian Splatting for Faces from Single Unconstrained Poses"
---

# FastAvatar: Instant 3D Gaussian Splatting for Faces from Single Unconstrained Poses

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18389" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18389v2</a>
  <a href="https://arxiv.org/pdf/2508.18389.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18389v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18389v2', 'FastAvatar: Instant 3D Gaussian Splatting for Faces from Single Unconstrained Poses')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hao Liang, Zhixuan Ge, Soumendu Majee, Ashish Tiwari, G. M. Dilshan Godaliyadda, Ashok Veeraraghavan, Guha Balakrishnan

**分类**: cs.CV

**发布日期**: 2025-08-25 (更新: 2025-11-25)

**备注**: 11 pages, 5 figures, website: https://hliang2.github.io/FastAvatar/

---

## 💡 一句话要点

**提出FastAvatar以解决单图3D人脸重建问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D人脸重建` `高斯结构` `快速算法` `虚拟现实` `表情动画`

## 📋 核心要点

1. 现有的3D人脸重建方法在处理单张图像时，往往面临速度慢和稳定性差的问题，尤其是在复杂姿态下。
2. FastAvatar通过两阶段设计，首先使用前馈网络预测粗略几何形状，然后进行测试时优化，快速且准确地重建3D人脸。
3. 实验结果表明，FastAvatar在重建质量上达到了24.01 dB PSNR和0.91 SSIM，且速度比传统方法快600倍，显著提升了性能。

## 📝 摘要（中文）

我们提出了FastAvatar，一种快速且稳健的算法，用于从单张任意姿态的图像中重建3D人脸。FastAvatar在单个NVIDIA A100 GPU上大约3秒内恢复出高质量的全头3D高斯头像。该方法采用两阶段设计：前馈编码器-解码器通过回归高斯结构预测粗略的人脸几何形状，随后轻量级的测试时优化阶段调整外观参数以实现照片级真实感渲染。这种混合策略结合了直接预测的速度和稳定性以及优化的准确性，即使在极端输入姿态下也能强有力地保持身份特征。FastAvatar在重建质量上达到了最新的技术水平（24.01 dB PSNR，0.91 SSIM），且运行速度比现有的每个主题优化方法快600倍以上。一旦重建完成，我们的头像支持照片级真实感的新视角合成和基于FLAME的表情动画，实现了从单张图像的可控重现。

## 🔬 方法详解

**问题定义**：本论文旨在解决从单张图像重建3D人脸的挑战，现有方法在速度和稳定性方面存在不足，尤其是在处理复杂姿态时。

**核心思路**：FastAvatar的核心思路是采用两阶段设计，首先通过前馈编码器-解码器预测粗略的人脸几何形状，然后在测试阶段进行优化，以实现高质量的渲染效果。

**技术框架**：整体架构分为两个主要模块：第一阶段是前馈编码器-解码器，用于回归高斯结构并预测人脸几何；第二阶段是轻量级的测试时优化，用于调整外观参数以实现真实感渲染。

**关键创新**：FastAvatar的创新在于结合了直接预测的速度和优化的准确性，能够在极端输入姿态下保持强大的身份特征，这是与现有方法的本质区别。

**关键设计**：在技术细节上，FastAvatar使用了特定的损失函数来平衡几何和外观的优化，同时采用了高效的网络结构以确保快速处理。具体参数设置和网络架构细节在论文中有详细描述。

## 📊 实验亮点

实验结果显示，FastAvatar在重建质量上达到了24.01 dB PSNR和0.91 SSIM，且运行速度比现有的每个主题优化方法快600倍，显著提升了3D人脸重建的效率和效果。

## 🎯 应用场景

该研究在虚拟现实、游戏开发和社交媒体等领域具有广泛的应用潜力。通过快速重建高质量的3D人脸头像，用户可以在各种场景中实现个性化的虚拟形象，增强互动体验。此外，基于FLAME的表情动画技术也为动画制作提供了新的可能性。

## 📄 摘要（原文）

> We present FastAvatar, a fast and robust algorithm for single-image 3D face reconstruction using 3D Gaussian Splatting (3DGS). Given a single input image from an arbitrary pose, FastAvatar recovers a high-quality, full-head 3DGS avatar in approximately 3 seconds on a single NVIDIA A100 GPU. We use a two-stage design: a feed-forward encoder-decoder predicts coarse face geometry by regressing Gaussian structure from a pose-invariant identity embedding, and a lightweight test-time refinement stage then optimizes the appearance parameters for photorealistic rendering. This hybrid strategy combines the speed and stability of direct prediction with the accuracy of optimization, enabling strong identity preservation even under extreme input poses. FastAvatar achieves state-of-the-art reconstruction quality (24.01 dB PSNR, 0.91 SSIM) while running over 600x faster than existing per-subject optimization methods (e.g., FlashAvatar, GaussianAvatars, GASP). Once reconstructed, our avatars support photorealistic novel-view synthesis and FLAME-guided expression animation, enabling controllable reenactment from a single image. By jointly offering high fidelity, robustness to pose, and rapid reconstruction, FastAvatar significantly broadens the applicability of 3DGS-based facial avatars.

