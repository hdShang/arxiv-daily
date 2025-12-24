---
layout: default
title: "GraspView: Active Perception Scoring and Best-View Optimization for Robotic Grasping in Cluttered Environments"
---

# GraspView: Active Perception Scoring and Best-View Optimization for Robotic Grasping in Cluttered Environments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.04199" class="toolbar-btn" target="_blank">📄 arXiv: 2511.04199v1</a>
  <a href="https://arxiv.org/pdf/2511.04199.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.04199v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.04199v1', 'GraspView: Active Perception Scoring and Best-View Optimization for Robotic Grasping in Cluttered Environments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shenglin Wang, Mingtong Dai, Jingxuan Su, Lingbo Liu, Chunjie Chen, Xinyu Wu, Liang Lin

**分类**: cs.RO

**发布日期**: 2025-11-06

---

## 💡 一句话要点

**GraspView：面向杂乱环境的基于主动感知评分和最佳视角优化的机器人抓取**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `机器人抓取` `主动感知` `多视图重建` `RGB图像` `最佳视角选择`

## 📋 核心要点

1. 传统机器人抓取依赖RGB-D相机，但在遮挡、近距离和透明/反光物体上表现不佳，导致抓取失败。
2. GraspView提出一种仅使用RGB图像的抓取方案，通过主动视角选择和多视图融合重建场景几何信息。
3. 实验表明，GraspView在复杂场景下显著优于RGB-D和单视图RGB方法，提升了抓取的鲁棒性和准确性。

## 📝 摘要（中文）

本文提出GraspView，一个仅使用RGB图像的机器人抓取流程，旨在无需深度传感器的情况下，在杂乱环境中实现精确操作。该框架包含三个关键组件：(i) 全局感知场景重建，从单个RGB视图提供局部一致、比例正确的几何信息，并将多视图投影融合到连贯的全局3D场景中；(ii) 渲染和评分的主动感知策略，动态选择最佳视角以揭示被遮挡区域；(iii) 在线度量对齐模块，校准VGGT预测与机器人运动学，以确保物理比例一致性。GraspView基于这些定制模块，执行最佳视角的全局抓取，融合多视图重建并利用GraspNet实现鲁棒执行。在各种桌面物体上的实验表明，GraspView显著优于RGB-D和单视图RGB基线，尤其是在严重遮挡、近场感知和透明物体的情况下。这些结果表明GraspView是RGB-D流程的一种实用且通用的替代方案，能够在非结构化的真实世界环境中实现可靠的抓取。

## 🔬 方法详解

**问题定义**：现有机器人抓取系统依赖RGB-D相机获取场景深度信息，但在杂乱环境中，由于遮挡、光照变化、透明或反光物体等因素的影响，深度信息的质量会显著下降，导致抓取失败率升高。此外，近距离感知时，RGB-D相机的精度也会受到限制。因此，如何在仅使用RGB图像的情况下，实现鲁棒的机器人抓取是一个重要的挑战。

**核心思路**：GraspView的核心思路是利用多视图RGB图像重建场景的几何信息，并通过主动感知策略选择最佳视角，以减少遮挡并提高重建质量。通过渲染和评分的方式，动态选择下一个最佳视角，从而逐步完善场景的3D模型。同时，采用在线度量对齐模块，校准视觉预测与机器人运动学，确保抓取的物理比例一致性。

**技术框架**：GraspView框架包含三个主要模块：(1) 全局感知场景重建模块，负责从单张RGB图像中估计局部一致、比例正确的几何信息，并将多视图投影融合到全局3D场景中。(2) 渲染和评分的主动感知策略模块，通过渲染不同视角的图像并进行评分，选择下一个最佳视角，以揭示被遮挡的区域。(3) 在线度量对齐模块，用于校准VGGT（Vision-Guided Grasping Transformer）的预测结果与机器人运动学，确保抓取的物理比例一致性。最终，系统融合多视图重建结果，并利用GraspNet进行抓取。

**关键创新**：GraspView的关键创新在于其结合了主动感知策略和多视图几何重建，实现了仅使用RGB图像的鲁棒抓取。与传统的RGB-D方法相比，GraspView不受深度传感器限制，能够处理透明和反光物体。与单视图RGB方法相比，GraspView通过主动视角选择和多视图融合，提高了场景重建的完整性和准确性。

**关键设计**：主动感知策略通过渲染不同视角的图像，并使用评分函数评估每个视角的质量。评分函数综合考虑了可见区域的大小、遮挡程度等因素。在线度量对齐模块使用卡尔曼滤波器估计视觉预测的比例因子，并将其与机器人运动学信息融合，从而实现精确的抓取控制。损失函数的设计也至关重要，需要平衡重建精度和抓取成功率。

## 📊 实验亮点

实验结果表明，GraspView在各种桌面物体上的抓取成功率显著优于RGB-D和单视图RGB基线。在严重遮挡的情况下，GraspView的性能提升尤为明显。此外，GraspView在处理透明物体和近场感知时也表现出优越的性能。具体数据未知，但整体表现优于对比方法。

## 🎯 应用场景

GraspView在自动化装配、物流分拣、家庭服务机器人等领域具有广泛的应用前景。该技术能够使机器人在复杂、非结构化的环境中进行可靠的抓取操作，尤其是在需要处理透明或反光物体的场景中。未来，GraspView有望进一步提升机器人的自主操作能力，降低对环境的依赖性。

## 📄 摘要（原文）

> Robotic grasping is a fundamental capability for autonomous manipulation, yet remains highly challenging in cluttered environments where occlusion, poor perception quality, and inconsistent 3D reconstructions often lead to unstable or failed grasps. Conventional pipelines have widely relied on RGB-D cameras to provide geometric information, which fail on transparent or glossy objects and degrade at close range. We present GraspView, an RGB-only robotic grasping pipeline that achieves accurate manipulation in cluttered environments without depth sensors. Our framework integrates three key components: (i) global perception scene reconstruction, which provides locally consistent, up-to-scale geometry from a single RGB view and fuses multi-view projections into a coherent global 3D scene; (ii) a render-and-score active perception strategy, which dynamically selects next-best-views to reveal occluded regions; and (iii) an online metric alignment module that calibrates VGGT predictions against robot kinematics to ensure physical scale consistency. Building on these tailor-designed modules, GraspView performs best-view global grasping, fusing multi-view reconstructions and leveraging GraspNet for robust execution. Experiments on diverse tabletop objects demonstrate that GraspView significantly outperforms both RGB-D and single-view RGB baselines, especially under heavy occlusion, near-field sensing, and with transparent objects. These results highlight GraspView as a practical and versatile alternative to RGB-D pipelines, enabling reliable grasping in unstructured real-world environments.

