---
layout: default
title: Plenodium: UnderWater 3D Scene Reconstruction with Plenoptic Medium Representation
---

# Plenodium: UnderWater 3D Scene Reconstruction with Plenoptic Medium Representation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21258" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21258v1</a>
  <a href="https://arxiv.org/pdf/2505.21258.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21258v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21258v1', 'Plenodium: UnderWater 3D Scene Reconstruction with Plenoptic Medium Representation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Changguanng Wu, Jiangxin Dong, Chengjian Li, Jinhui Tang

**分类**: cs.CV

**发布日期**: 2025-05-27

**🔗 代码/项目**: [PROJECT_PAGE](https://plenodium.github.io/)

---

## 💡 一句话要点

**提出Plenodium以解决水下3D场景重建问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `水下重建` `全光学介质` `3D表示` `深度学习` `球谐编码` `COLMAP` `图像处理`

## 📋 核心要点

1. 现有的水下场景重建方法多依赖于视角建模，导致在复杂环境中表现不佳，尤其是在光线散射严重的情况下。
2. 论文提出的Plenodium框架通过结合方向和位置的信息，利用球谐编码实现了更为准确的水下场景重建，并引入伪深度高斯补充来增强点云。
3. 实验结果显示，Plenodium在真实水下数据集上显著提高了3D重建的精度，相较于基线方法有明显的性能提升。

## 📝 摘要（中文）

我们提出了Plenodium（全光学介质），这是一个有效且高效的3D表示框架，能够联合建模物体和参与介质。与现有的仅依赖视角建模的介质表示方法不同，我们的新型全光学介质表示通过球谐编码结合了方向和位置的信息，从而实现了高精度的水下场景重建。为了解决退化水下环境中的初始化挑战，我们提出了伪深度高斯补充，以增强COLMAP生成的点云，并引入了深度排序正则化损失来优化场景几何和改善深度图的序列一致性。大量在真实水下数据集上的实验表明，我们的方法在3D重建中取得了显著的改进。

## 🔬 方法详解

**问题定义**：论文旨在解决水下场景重建中的初始化挑战和视角依赖建模的局限性，现有方法在复杂光学条件下表现不佳。

**核心思路**：通过引入全光学介质表示，结合方向和位置的信息，利用球谐编码来提高水下场景重建的准确性，同时采用伪深度高斯补充来增强点云的质量。

**技术框架**：整体框架包括数据采集、COLMAP点云生成、伪深度高斯补充、深度排序正则化损失优化等多个模块，形成一个闭环的重建流程。

**关键创新**：最重要的创新在于提出了全光学介质表示，能够同时处理物体和参与介质的信息，显著提高了重建精度，与传统方法相比具有本质的区别。

**关键设计**：在损失函数设计上，采用了深度排序正则化损失，以确保深度图的序列一致性，同时在网络结构上进行了优化，以适应水下环境的特殊需求。

## 📊 实验亮点

在真实水下数据集上的实验结果表明，Plenodium方法在3D重建精度上较基线方法提高了显著的性能，具体提升幅度达到XX%（具体数据待补充），展示了其在复杂水下环境中的优越性。

## 🎯 应用场景

该研究的潜在应用领域包括水下探测、海洋科学研究、考古学以及水下机器人导航等。通过提高水下3D重建的精度，Plenodium能够为这些领域提供更为可靠的数据支持，推动相关技术的发展与应用。

## 📄 摘要（原文）

> We present Plenodium (plenoptic medium), an effective and efficient 3D representation framework capable of jointly modeling both objects and participating media. In contrast to existing medium representations that rely solely on view-dependent modeling, our novel plenoptic medium representation incorporates both directional and positional information through spherical harmonics encoding, enabling highly accurate underwater scene reconstruction. To address the initialization challenge in degraded underwater environments, we propose the pseudo-depth Gaussian complementation to augment COLMAP-derived point clouds with robust depth priors. In addition, a depth ranking regularized loss is developed to optimize the geometry of the scene and improve the ordinal consistency of the depth maps. Extensive experiments on real-world underwater datasets demonstrate that our method achieves significant improvements in 3D reconstruction. Furthermore, we conduct a simulated dataset with ground truth and the controllable scattering medium to demonstrate the restoration capability of our method in underwater scenarios. Our code and dataset are available at https://plenodium.github.io/.

