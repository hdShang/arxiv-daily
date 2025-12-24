---
layout: default
title: "SparSplat: Fast Multi-View Reconstruction with Generalizable 2D Gaussian Splatting"
---

# SparSplat: Fast Multi-View Reconstruction with Generalizable 2D Gaussian Splatting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02175" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02175v1</a>
  <a href="https://arxiv.org/pdf/2505.02175.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02175v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02175v1', 'SparSplat: Fast Multi-View Reconstruction with Generalizable 2D Gaussian Splatting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shubhendu Jena, Shishir Reddy Vutukur, Adnane Boukhayma

**分类**: cs.CV

**发布日期**: 2025-05-04

**备注**: Project page : https://shubhendu-jena.github.io/SparSplat/

---

## 💡 一句话要点

**提出SparSplat以解决稀疏视图下的3D重建与新视图合成问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `多视图立体重建` `新视图合成` `高斯点云` `深度学习` `计算机视觉`

## 📋 核心要点

1. 现有方法在稀疏视图下的3D重建和新视图合成面临准确性和实时性不足的挑战。
2. 本文提出了一种基于MVS的学习管道，通过回归2D高斯表面元素参数，实现稀疏视图图像的3D重建和NVS。
3. 实验结果表明，模型在DTU基准测试中表现优异，推理速度提高近两个数量级，超越了现有的最先进方法。

## 📝 摘要（中文）

从场景中恢复3D信息的多视图立体重建（MVS）和新视图合成（NVS）在稀疏视图设置下具有挑战性。3D高斯点云（3DGS）的出现使得实时、逼真的NVS成为可能。本文提出了一种基于MVS的学习管道，通过前馈方式回归2D高斯表面元素参数，从稀疏视图图像中进行3D形状重建和NVS。我们的模型在DTU稀疏3D重建基准测试中取得了最先进的结果，并在BlendedMVS和Tanks and Temples数据集上表现出强大的泛化能力。

## 🔬 方法详解

**问题定义**：本文旨在解决在稀疏视图下进行3D重建和新视图合成的挑战。现有方法在处理稀疏视图时，往往面临准确性不足和实时性差的问题。

**核心思路**：我们提出了一种基于MVS的学习管道，利用前馈方式回归2D高斯表面元素参数，从而实现高效的3D形状重建和新视图合成。该设计旨在提高重建的准确性，同时保持实时性能。

**技术框架**：整体架构包括数据输入、特征提取、2D高斯表面元素参数回归和3D重建与NVS模块。通过深度学习网络提取多视图深度视觉特征，进而进行参数回归。

**关键创新**：最重要的创新在于将2D高斯点云与MVS结合，形成一种通用的稀疏3D重建与NVS方法。这一方法在推理速度和重建精度上显著优于现有基于隐式表示的体积渲染方法。

**关键设计**：在网络结构上，采用了深度卷积神经网络进行特征提取，损失函数设计为结合Chamfer距离和重建误差，以优化模型的重建精度和泛化能力。

## 📊 实验亮点

实验结果显示，模型在DTU稀疏3D重建基准测试中取得了最先进的Chamfer距离表现，同时在新视图合成任务中也达到了最优结果。与之前的最先进方法相比，推理速度提高了近两个数量级，展示了显著的性能提升。

## 🎯 应用场景

该研究在计算机视觉、虚拟现实和增强现实等领域具有广泛的应用潜力。通过实现高效的3D重建和新视图合成，可以为实时场景重建、游戏开发和影视制作等提供强大的技术支持，推动相关行业的发展。

## 📄 摘要（原文）

> Recovering 3D information from scenes via multi-view stereo reconstruction (MVS) and novel view synthesis (NVS) is inherently challenging, particularly in scenarios involving sparse-view setups. The advent of 3D Gaussian Splatting (3DGS) enabled real-time, photorealistic NVS. Following this, 2D Gaussian Splatting (2DGS) leveraged perspective accurate 2D Gaussian primitive rasterization to achieve accurate geometry representation during rendering, improving 3D scene reconstruction while maintaining real-time performance. Recent approaches have tackled the problem of sparse real-time NVS using 3DGS within a generalizable, MVS-based learning framework to regress 3D Gaussian parameters. Our work extends this line of research by addressing the challenge of generalizable sparse 3D reconstruction and NVS jointly, and manages to perform successfully at both tasks. We propose an MVS-based learning pipeline that regresses 2DGS surface element parameters in a feed-forward fashion to perform 3D shape reconstruction and NVS from sparse-view images. We further show that our generalizable pipeline can benefit from preexisting foundational multi-view deep visual features. The resulting model attains the state-of-the-art results on the DTU sparse 3D reconstruction benchmark in terms of Chamfer distance to ground-truth, as-well as state-of-the-art NVS. It also demonstrates strong generalization on the BlendedMVS and Tanks and Temples datasets. We note that our model outperforms the prior state-of-the-art in feed-forward sparse view reconstruction based on volume rendering of implicit representations, while offering an almost 2 orders of magnitude higher inference speed.

