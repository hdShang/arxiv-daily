---
layout: default
title: "OpenM3D: Open Vocabulary Multi-view Indoor 3D Object Detection without Human Annotations"
---

# OpenM3D: Open Vocabulary Multi-view Indoor 3D Object Detection without Human Annotations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.20063" class="toolbar-btn" target="_blank">📄 arXiv: 2508.20063v1</a>
  <a href="https://arxiv.org/pdf/2508.20063.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.20063v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.20063v1', 'OpenM3D: Open Vocabulary Multi-view Indoor 3D Object Detection without Human Annotations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Peng-Hao Hsu, Ke Zhang, Fu-En Wang, Tao Tu, Ming-Feng Li, Yu-Lun Liu, Albert Y. C. Chen, Min Sun, Cheng-Hao Kuo

**分类**: cs.CV

**发布日期**: 2025-08-27

**备注**: ICCV2025

---

## 💡 一句话要点

**提出OpenM3D以解决无人工注释的多视角室内3D物体检测问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `开放词汇` `3D物体检测` `无人工注释` `多视角图像` `伪框生成` `体素特征` `图嵌入技术` `室内场景`

## 📋 核心要点

1. 现有的3D物体检测方法多依赖于3D点云，图像基础的开放词汇检测探索较少，限制了应用场景。
2. OpenM3D通过无人工注释的方式，结合2D诱导体素特征和多视角图像，提出了一种高效的单阶段检测器。
3. 在ScanNet200和ARKitScenes基准测试中，OpenM3D在准确性和速度上均优于现有方法，展示了其实际应用潜力。

## 📝 摘要（中文）

开放词汇（OV）3D物体检测是一个新兴领域，但基于图像的方法探索仍然有限。我们提出OpenM3D，这是一种新颖的开放词汇多视角室内3D物体检测器，训练过程中无需人工注释。OpenM3D是一个单阶段检测器，采用ImGeoNet模型的2D诱导体素特征。为支持OV，它与无类别的3D定位损失和体素语义对齐损失共同训练。我们提出了一种3D伪框生成方法，利用图嵌入技术将2D分段组合成一致的3D结构。OpenM3D在ScanNet200和ARKitScenes基准测试中展示了优越的准确性和速度，且在准确性和速度上超越了强大的两阶段方法。

## 🔬 方法详解

**问题定义**：论文旨在解决开放词汇的多视角室内3D物体检测问题，现有方法多依赖人工注释和3D点云，限制了其应用和扩展性。

**核心思路**：OpenM3D通过无人工注释的训练方式，结合2D诱导体素特征和多视角图像，提出了一种高效的单阶段检测器，旨在提高检测精度和速度。

**技术框架**：整体架构包括伪框生成模块和特征对齐模块。伪框生成模块利用图嵌入技术将2D分段组合成一致的3D结构，特征对齐模块则从2D分段中采样多样的CLIP特征以对齐体素特征。

**关键创新**：最重要的技术创新在于提出了一种无人工注释的3D伪框生成方法，结合了图嵌入技术，显著提高了伪框的精度和召回率。

**关键设计**：论文设计了无类别的3D定位损失和体素语义对齐损失，以确保高质量目标的学习。此外，采用了ImGeoNet模型的2D诱导体素特征，提升了检测器的性能。

## 📊 实验亮点

OpenM3D在ScanNet200和ARKitScenes基准测试中展示了卓越的性能，检测速度为每场景0.3秒，准确性超越了强大的两阶段方法，显示出在准确性和速度上的显著提升。

## 🎯 应用场景

该研究的潜在应用领域包括智能家居、机器人导航和增强现实等场景。通过实现无人工注释的3D物体检测，OpenM3D能够在快速变化的环境中实时识别和定位物体，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Open-vocabulary (OV) 3D object detection is an emerging field, yet its exploration through image-based methods remains limited compared to 3D point cloud-based methods. We introduce OpenM3D, a novel open-vocabulary multi-view indoor 3D object detector trained without human annotations. In particular, OpenM3D is a single-stage detector adapting the 2D-induced voxel features from the ImGeoNet model. To support OV, it is jointly trained with a class-agnostic 3D localization loss requiring high-quality 3D pseudo boxes and a voxel-semantic alignment loss requiring diverse pre-trained CLIP features. We follow the training setting of OV-3DET where posed RGB-D images are given but no human annotations of 3D boxes or classes are available. We propose a 3D Pseudo Box Generation method using a graph embedding technique that combines 2D segments into coherent 3D structures. Our pseudo-boxes achieve higher precision and recall than other methods, including the method proposed in OV-3DET. We further sample diverse CLIP features from 2D segments associated with each coherent 3D structure to align with the corresponding voxel feature. The key to training a highly accurate single-stage detector requires both losses to be learned toward high-quality targets. At inference, OpenM3D, a highly efficient detector, requires only multi-view images for input and demonstrates superior accuracy and speed (0.3 sec. per scene) on ScanNet200 and ARKitScenes indoor benchmarks compared to existing methods. We outperform a strong two-stage method that leverages our class-agnostic detector with a ViT CLIP-based OV classifier and a baseline incorporating multi-view depth estimator on both accuracy and speed.

