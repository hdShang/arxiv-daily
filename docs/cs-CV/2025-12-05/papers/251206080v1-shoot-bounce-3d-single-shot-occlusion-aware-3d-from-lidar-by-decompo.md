---
layout: default
title: Shoot-Bounce-3D: Single-Shot Occlusion-Aware 3D from Lidar by Decomposing Two-Bounce Light
---

# Shoot-Bounce-3D: Single-Shot Occlusion-Aware 3D from Lidar by Decomposing Two-Bounce Light

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.06080" class="toolbar-btn" target="_blank">📄 arXiv: 2512.06080v1</a>
  <a href="https://arxiv.org/pdf/2512.06080.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.06080v1" onclick="toggleFavorite(this, '2512.06080v1', 'Shoot-Bounce-3D: Single-Shot Occlusion-Aware 3D from Lidar by Decomposing Two-Bounce Light')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tzofi Klinghoffer, Siddharth Somasundaram, Xiaoyu Xiang, Yuchen Fan, Christian Richardt, Akshat Dave, Ramesh Raskar, Rakesh Ranjan

**分类**: cs.CV

**发布日期**: 2025-12-05

**备注**: SIGGRAPH Asia 2025. Project page: https://shoot-bounce-3d.github.io

---

## 💡 一句话要点

**Shoot-Bounce-3D：利用单光子激光雷达和双次反射光进行遮挡感知的三维重建**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `单光子激光雷达` `三维重建` `遮挡感知` `双次反射光` `光传输反演`

## 📋 核心要点

1. 现有单光子激光雷达在复杂场景下的三维重建，尤其是在遮挡和镜面反射存在时，面临光路复杂难以解析的问题。
2. 提出Shoot-Bounce-3D，利用单光子激光雷达获取的双次反射光信息，通过数据驱动方法学习光传输先验，分解多重反射光。
3. 通过大规模模拟数据集训练，实验证明该方法能够有效推断遮挡和镜面场景中的三维几何形状，实现单次测量重建。

## 📝 摘要（中文）

本文提出了一种利用单光子激光雷达进行三维场景重建的方法，尤其是在存在遮挡区域和镜面反射材料的情况下。该方法利用激光雷达发射到场景中并直接反射回传感器的光来估计深度。此外，它还利用在场景中多次反射后到达传感器的多重反射光。这种多重反射光包含可用于恢复密集深度、遮挡几何形状和材料属性的额外信息。与以往单光子激光雷达逐点扫描的方法不同，本文关注更具挑战性的同时照射多个场景点的场景。由于多路复用照明、双次反射光、阴影和镜面反射的综合影响，光传输的复杂性难以进行解析反演。因此，本文提出了一种数据驱动的方法来反演单光子激光雷达中的光传输。为了实现这种方法，本文创建了第一个大规模的室内场景激光雷达瞬态模拟数据集（约10万个）。利用该数据集学习复杂光传输的先验知识，从而将测量的双次反射光分解为来自每个激光点的组成部分。最后，实验证明了如何利用这种分解的光来推断具有遮挡和镜子的场景中的三维几何形状。

## 🔬 方法详解

**问题定义**：论文旨在解决单次测量下单光子激光雷达三维重建中，由于遮挡和镜面反射导致光路复杂，难以准确重建场景几何的问题。现有方法通常依赖逐点扫描，效率较低，且难以处理复杂光路带来的干扰。

**核心思路**：论文的核心思路是利用单光子激光雷达能够捕获的双次反射光信息，这些信息包含了场景中被遮挡区域和镜面反射的信息。通过学习光传输的先验知识，将复杂的双次反射光分解为各个激光点贡献的组成部分，从而推断出场景的完整几何信息。

**技术框架**：整体框架包含以下几个主要阶段：1) 大规模模拟数据集生成：创建包含各种室内场景和光照条件的激光雷达瞬态数据。2) 光传输先验学习：利用生成的数据集训练神经网络，学习复杂光传输的模式和规律。3) 双次反射光分解：利用训练好的网络，将测量的双次反射光分解为各个激光点对应的贡献。4) 三维几何推断：利用分解后的光信息，推断场景的三维几何形状。

**关键创新**：最重要的创新点在于提出了一个数据驱动的方法来反演单光子激光雷达中的光传输。与传统的解析方法相比，该方法能够更好地处理复杂的光路和非线性效应，从而更准确地重建场景几何。此外，大规模模拟数据集的构建也为该方法的训练和验证提供了有力支持。

**关键设计**：论文构建了大规模的模拟数据集，包含约10万个激光雷达瞬态数据，涵盖了各种室内场景和光照条件。网络结构方面，具体细节未知，但其目标是学习一个能够将复杂双次反射光分解为各个激光点贡献的模型。损失函数的设计也至关重要，需要能够有效地引导网络学习光传输的先验知识。

## 📊 实验亮点

论文通过实验验证了该方法在遮挡和镜面反射场景下的三维重建能力。实验结果表明，该方法能够有效地分解双次反射光，并准确地推断出被遮挡区域和镜面的几何形状。虽然论文中没有给出具体的性能指标，但实验结果直观地展示了该方法在复杂场景下的优势。

## 🎯 应用场景

该研究成果可应用于自动驾驶、机器人导航、三维场景重建、室内地图构建等领域。尤其是在光线条件复杂、存在遮挡和镜面反射的环境中，该方法能够提供更准确和完整的三维信息，提高系统的感知能力和鲁棒性。未来，该技术有望进一步拓展到文物保护、医疗诊断等领域。

## 📄 摘要（原文）

> 3D scene reconstruction from a single measurement is challenging, especially in the presence of occluded regions and specular materials, such as mirrors. We address these challenges by leveraging single-photon lidars. These lidars estimate depth from light that is emitted into the scene and reflected directly back to the sensor. However, they can also measure light that bounces multiple times in the scene before reaching the sensor. This multi-bounce light contains additional information that can be used to recover dense depth, occluded geometry, and material properties. Prior work with single-photon lidar, however, has only demonstrated these use cases when a laser sequentially illuminates one scene point at a time. We instead focus on the more practical - and challenging - scenario of illuminating multiple scene points simultaneously. The complexity of light transport due to the combined effects of multiplexed illumination, two-bounce light, shadows, and specular reflections is challenging to invert analytically. Instead, we propose a data-driven method to invert light transport in single-photon lidar. To enable this approach, we create the first large-scale simulated dataset of ~100k lidar transients for indoor scenes. We use this dataset to learn a prior on complex light transport, enabling measured two-bounce light to be decomposed into the constituent contributions from each laser spot. Finally, we experimentally demonstrate how this decomposed light can be used to infer 3D geometry in scenes with occlusions and mirrors from a single measurement. Our code and dataset are released at https://shoot-bounce-3d.github.io.

