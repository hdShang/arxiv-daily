---
layout: default
title: Physics-Grounded Attached Shadow Detection Using Approximate 3D Geometry and Light Direction
---

# Physics-Grounded Attached Shadow Detection Using Approximate 3D Geometry and Light Direction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.06179" class="toolbar-btn" target="_blank">📄 arXiv: 2512.06179v1</a>
  <a href="https://arxiv.org/pdf/2512.06179.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.06179v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.06179v1', 'Physics-Grounded Attached Shadow Detection Using Approximate 3D Geometry and Light Direction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shilin Hu, Jingyi Xu, Sagnik Das, Dimitris Samaras, Hieu Le

**分类**: cs.CV

**发布日期**: 2025-12-05

---

## 💡 一句话要点

**提出基于近似3D几何和光照方向的物理约束阴影检测方法**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `依附阴影检测` `投射阴影检测` `光照估计` `几何推理` `阴影分割`

## 📋 核心要点

1. 现有阴影检测方法主要关注投射阴影，忽略了依附阴影，缺乏针对依附阴影的专用数据集和模型。
2. 该论文提出了一种联合检测投射阴影和依附阴影的框架，通过场景光照和几何体的相互关系进行推理。
3. 实验结果表明，该方法通过迭代的几何-光照推理，显著提高了依附阴影的检测性能，BER降低至少33%。

## 📝 摘要（中文）

本文提出了一种联合检测依附阴影和投射阴影的框架，通过推理场景光照和几何体的相互关系来实现。该系统包含一个阴影检测模块，分别预测两种阴影类型，以及一个光照估计模块，从检测到的阴影中推断光照方向。估计的光照方向与表面法线相结合，可以推导出几何一致的部分地图，识别可能发生自遮挡的区域。该部分地图被反馈以细化阴影预测，形成一个闭环推理过程，迭代地改进阴影分割和光照估计。为了训练该方法，构建了一个包含1458张图像的数据集，分别标注了投射阴影和依附阴影，从而能够对两者进行训练和定量评估。实验结果表明，这种迭代的几何-光照推理显著提高了依附阴影的检测，BER降低至少33%，同时保持了强大的完整阴影和投射阴影性能。

## 🔬 方法详解

**问题定义**：论文旨在解决依附阴影检测问题。现有阴影检测方法主要集中于投射阴影，忽略了依附阴影的重要性，并且缺乏专门用于依附阴影检测的数据集和模型。这导致现有方法在理解场景三维结构和进行更高级的场景理解方面存在局限性。

**核心思路**：论文的核心思路是利用场景的几何信息和光照信息之间的相互关系来提高依附阴影的检测精度。通过迭代地估计光照方向，并结合表面法线信息，生成一个几何一致的部分地图，用于指导阴影检测，从而实现更准确的依附阴影分割。

**技术框架**：该方法包含两个主要模块：阴影检测模块和光照估计模块。阴影检测模块负责分别预测投射阴影和依附阴影。光照估计模块从检测到的阴影中推断光照方向。估计的光照方向与表面法线结合，生成几何一致的部分地图。该部分地图被反馈到阴影检测模块，用于细化阴影预测，形成一个闭环推理过程。

**关键创新**：该方法最重要的创新点在于利用几何信息和光照信息之间的相互约束关系，通过迭代推理来提高依附阴影的检测精度。与现有方法相比，该方法不仅考虑了阴影的外观特征，还考虑了阴影与场景几何结构之间的物理关系，从而能够更准确地检测依附阴影。

**关键设计**：该方法使用了一个包含1458张图像的数据集进行训练，该数据集分别标注了投射阴影和依附阴影。损失函数的设计需要同时考虑投射阴影和依附阴影的检测精度，以及光照估计的准确性。具体的网络结构和参数设置在论文中没有详细描述，属于未知信息。

## 📊 实验亮点

实验结果表明，该方法在依附阴影检测方面取得了显著的提升，BER（贝叶斯错误率）降低了至少33%。同时，该方法在投射阴影和完整阴影的检测方面也保持了良好的性能。这些结果表明，通过迭代的几何-光照推理，可以有效地提高阴影检测的准确性。

## 🎯 应用场景

该研究成果可应用于机器人视觉、自动驾驶、三维重建等领域。准确的阴影检测能够帮助机器人更好地理解周围环境，提高自动驾驶系统的安全性，并改善三维重建的质量。该方法还有潜力应用于图像编辑和增强现实等领域，例如，可以用于在图像中添加或修改阴影，以增强图像的真实感。

## 📄 摘要（原文）

> Attached shadows occur on the surface of the occluder where light cannot reach because of self-occlusion. They are crucial for defining the three-dimensional structure of objects and enhancing scene understanding. Yet existing shadow detection methods mainly target cast shadows, and there are no dedicated datasets or models for detecting attached shadows. To address this gap, we introduce a framework that jointly detects cast and attached shadows by reasoning about their mutual relationship with scene illumination and geometry. Our system consists of a shadow detection module that predicts both shadow types separately, and a light estimation module that infers the light direction from the detected shadows. The estimated light direction, combined with surface normals, allows us to derive a geometry-consistent partial map that identifies regions likely to be self-occluded. This partial map is then fed back to refine shadow predictions, forming a closed-loop reasoning process that iteratively improves both shadow segmentation and light estimation. In order to train our method, we have constructed a dataset of 1,458 images with separate annotations for cast and attached shadows, enabling training and quantitative evaluation of both. Experimental results demonstrate that this iterative geometry-illumination reasoning substantially improves the detection of attached shadows, with at least 33% BER reduction, while maintaining strong full and cast shadow performance.

