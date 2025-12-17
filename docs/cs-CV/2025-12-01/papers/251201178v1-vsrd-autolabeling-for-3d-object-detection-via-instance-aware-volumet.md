---
layout: default
title: VSRD++: Autolabeling for 3D Object Detection via Instance-Aware Volumetric Silhouette Rendering
---

# VSRD++: Autolabeling for 3D Object Detection via Instance-Aware Volumetric Silhouette Rendering

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.01178" class="toolbar-btn" target="_blank">📄 arXiv: 2512.01178v1</a>
  <a href="https://arxiv.org/pdf/2512.01178.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.01178v1" onclick="toggleFavorite(this, '2512.01178v1', 'VSRD++: Autolabeling for 3D Object Detection via Instance-Aware Volumetric Silhouette Rendering')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zihua Liu, Hiroki Sakuma, Masatoshi Okutomi

**分类**: cs.CV

**发布日期**: 2025-12-01

**备注**: arXiv admin note: text overlap with arXiv:2404.00149

**🔗 代码/项目**: [GITHUB](https://github.com/Magicboomliu/VSRD_plus_plus)

---

## 💡 一句话要点

**提出VSRD++以解决单目3D物体检测中的标注依赖问题**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `单目3D检测` `弱监督学习` `体积渲染` `动态物体` `自动标注`

## 📋 核心要点

1. 现有的单目3D物体检测方法严重依赖于大量的3D标注，获取这些标注的过程既耗时又费力。
2. 本文提出了一种弱监督框架VSRD++，通过实例感知的体积轮廓渲染实现多视角3D自动标注，消除了对3D标注的依赖。
3. 在KITTI-360数据集上的实验结果显示，VSRD++在静态和动态场景下均显著优于现有的弱监督方法。

## 📝 摘要（中文）

单目3D物体检测是3D场景理解中的一项基础而具有挑战性的任务。现有方法通常依赖于大量的3D标注，这些标注通常通过劳动密集型的LiDAR点云标注过程获得。为了解决这一问题，本文提出了VSRD++，一种新颖的弱监督框架，消除了对3D标注的依赖，并利用基于神经场的体积渲染与弱2D监督相结合。VSRD++包括两个阶段：多视角3D自动标注和后续的单目3D检测器训练。通过实例感知的体积轮廓渲染，将物体表面表示为带符号距离场(SDF)并渲染为实例掩码。大量实验表明，VSRD++在KITTI-360数据集上显著优于现有的弱监督单目3D物体检测方法。

## 🔬 方法详解

**问题定义**：本文旨在解决单目3D物体检测中对3D标注的依赖问题。现有方法通常需要大量的3D标注，这一过程既耗时又费力，限制了其在实际应用中的推广。

**核心思路**：VSRD++的核心思路是通过弱监督学习，利用2D监督信息和神经场的体积渲染技术，自动生成3D标注，从而减少对人工标注的需求。

**技术框架**：VSRD++的整体架构分为两个主要阶段：第一阶段是多视角3D自动标注，第二阶段是基于优化后的3D边界框进行单目3D检测器的训练。多视角自动标注阶段使用带符号距离场(SDF)表示物体表面，并通过实例感知的体积轮廓渲染生成实例掩码。

**关键创新**：VSRD++的关键创新在于引入了带符号距离场(SDF)与残差距离场(RDF)的结合，优化3D边界框，并通过动态物体的速度信息和置信度分配来解决几何不一致性问题。这一方法在动态场景中表现尤为突出。

**关键设计**：在设计上，VSRD++采用了3D属性初始化模块来初始化动态边界框参数，并通过优化的损失函数来提高伪标签的质量。此外，模型还考虑了动态物体的速度信息，以增强对动态场景的适应性。

## 📊 实验亮点

在KITTI-360数据集上的实验结果显示，VSRD++在静态场景中相较于现有弱监督方法提升了XX%，在动态场景中提升了YY%。这一显著的性能提升证明了VSRD++在单目3D物体检测中的有效性和优越性。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、机器人导航和增强现实等。通过减少对3D标注的依赖，VSRD++能够加速3D物体检测模型的训练过程，降低人工标注成本，提升模型在复杂场景中的适应能力，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Monocular 3D object detection is a fundamental yet challenging task in 3D scene understanding. Existing approaches heavily depend on supervised learning with extensive 3D annotations, which are often acquired from LiDAR point clouds through labor-intensive labeling processes. To tackle this problem, we propose VSRD++, a novel weakly supervised framework for monocular 3D object detection that eliminates the reliance on 3D annotations and leverages neural-field-based volumetric rendering with weak 2D supervision. VSRD++ consists of a two-stage pipeline: multi-view 3D autolabeling and subsequent monocular 3D detector training. In the multi-view autolabeling stage, object surfaces are represented as signed distance fields (SDFs) and rendered as instance masks via the proposed instance-aware volumetric silhouette rendering. To optimize 3D bounding boxes, we decompose each instance's SDF into a cuboid SDF and a residual distance field (RDF) that captures deviations from the cuboid. To address the geometry inconsistency commonly observed in volume rendering methods applied to dynamic objects, we model the dynamic objects by including velocity into bounding box attributes as well as assigning confidence to each pseudo-label. Moreover, we also employ a 3D attribute initialization module to initialize the dynamic bounding box parameters. In the monocular 3D object detection phase, the optimized 3D bounding boxes serve as pseudo labels for training monocular 3D object detectors. Extensive experiments on the KITTI-360 dataset demonstrate that VSRD++ significantly outperforms existing weakly supervised approaches for monocular 3D object detection on both static and dynamic scenes. Code is available at https://github.com/Magicboomliu/VSRD_plus_plus

