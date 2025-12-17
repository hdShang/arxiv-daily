---
layout: default
title: GraphFusion3D: Dynamic Graph Attention Convolution with Adaptive Cross-Modal Transformer for 3D Object Detection
---

# GraphFusion3D: Dynamic Graph Attention Convolution with Adaptive Cross-Modal Transformer for 3D Object Detection

**arXiv**: [2512.02991v1](https://arxiv.org/abs/2512.02991) | [PDF](https://arxiv.org/pdf/2512.02991.pdf)

**作者**: Md Sohag Mia, Md Nahid Hasan, Tawhid Ahmed, Muhammad Abdullah Adnan

---

## 💡 一句话要点

**提出GraphFusion3D框架，结合自适应跨模态Transformer和动态图注意力卷积，以解决3D点云目标检测中的稀疏性和上下文关系问题。**

**关键词**: `3D目标检测` `多模态融合` `图注意力网络` `自适应Transformer` `点云处理`

## 📋 核心要点

1. 核心问题：点云数据稀疏、结构不完整、语义信息有限，且难以捕获远距离对象间的上下文关系。
2. 方法要点：引入自适应跨模态Transformer融合图像特征，增强点云几何和语义信息；使用图推理模块通过多尺度图注意力动态建模邻域关系。
3. 实验或效果：在SUN RGB-D和ScanNetV2数据集上取得显著性能提升，优于现有方法。

## 📄 摘要（原文）

> Despite significant progress in 3D object detection, point clouds remain challenging due to sparse data, incomplete structures, and limited semantic information. Capturing contextual relationships between distant objects presents additional difficulties. To address these challenges, we propose GraphFusion3D, a unified framework combining multi-modal fusion with advanced feature learning. Our approach introduces the Adaptive Cross-Modal Transformer (ACMT), which adaptively integrates image features into point representations to enrich both geometric and semantic information. For proposal refinement, we introduce the Graph Reasoning Module (GRM), a novel mechanism that models neighborhood relationships to simultaneously capture local geometric structures and global semantic context. The module employs multi-scale graph attention to dynamically weight both spatial proximity and feature similarity between proposals. We further employ a cascade decoder that progressively refines detections through multi-stage predictions. Extensive experiments on SUN RGB-D (70.6\% AP$_{25}$ and 51.2\% AP$_{50}$) and ScanNetV2 (75.1\% AP$_{25}$ and 60.8\% AP$_{50}$) demonstrate a substantial performance improvement over existing approaches.

