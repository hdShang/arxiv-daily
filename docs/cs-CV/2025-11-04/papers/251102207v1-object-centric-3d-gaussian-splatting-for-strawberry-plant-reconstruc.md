---
layout: default
title: Object-Centric 3D Gaussian Splatting for Strawberry Plant Reconstruction and Phenotyping
---

# Object-Centric 3D Gaussian Splatting for Strawberry Plant Reconstruction and Phenotyping

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.02207" class="toolbar-btn" target="_blank">📄 arXiv: 2511.02207v1</a>
  <a href="https://arxiv.org/pdf/2511.02207.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.02207v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.02207v1', 'Object-Centric 3D Gaussian Splatting for Strawberry Plant Reconstruction and Phenotyping')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiajia Li, Keyi Zhu, Qianwen Zhang, Dong Chen, Qi Sun, Zhaojian Li

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-04

**备注**: 11 pages, 4 figures, 3 tables

---

## 💡 一句话要点

**提出对象中心3D高斯溅射方法，用于草莓植株重建与表型分析**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D高斯溅射` `植物重建` `表型分析` `对象中心` `图像分割` `SAM-2` `精准农业`

## 📋 核心要点

1. 现有3D高斯溅射方法重建包含背景的完整场景，引入噪声并增加计算成本，不利于后续植物性状分析。
2. 提出一种对象中心3D重建框架，利用SAM-2和alpha通道掩蔽进行预处理，实现干净的草莓植株重建。
3. 实验表明，该方法在准确性和效率上优于传统流程，为草莓植株表型分析提供可扩展的非破坏性方案。

## 📝 摘要（中文）

草莓是美国最具经济价值的水果之一。植物表型分析在选择优良品种方面起着至关重要的作用，它能表征植物的形态、冠层结构和生长动态等特征。然而，传统的植物表型分析方法耗时、费力且常常具有破坏性。近年来，神经渲染技术，特别是神经辐射场（NeRF）和3D高斯溅射（3DGS），已成为高保真3D重建的强大框架。通过捕获目标植物周围的多视角图像或视频序列，这些方法能够对复杂的植物结构进行非破坏性重建。为了解决现有3DGS方法重建包含背景元素的整个场景，导致噪声增加、计算成本上升并使下游性状分析复杂化的问题，我们提出了一种新的对象中心3D重建框架，该框架结合了利用Segment Anything Model v2（SAM-2）和alpha通道背景掩蔽的预处理流程，以实现干净的草莓植株重建。该方法产生更精确的几何表示，同时显著减少计算时间。通过无背景重建，我们的算法可以使用DBSCAN聚类和主成分分析（PCA）自动估计重要的植物性状，例如株高和冠层宽度。实验结果表明，我们的方法在准确性和效率方面均优于传统流程，为草莓植株表型分析提供了一种可扩展的非破坏性解决方案。

## 🔬 方法详解

**问题定义**：现有基于3D高斯溅射的植物重建方法通常重建整个场景，包括植物周围的背景。这导致重建结果包含大量噪声，增加了计算负担，并且使得后续的植物表型分析变得更加困难。因此，需要一种方法能够精确地重建植物本身，去除背景干扰，从而提高重建精度和效率。

**核心思路**：论文的核心思路是采用对象中心的方法，即首先将植物从背景中分割出来，然后仅对植物进行3D重建。通过这种方式，可以避免背景噪声的干扰，提高重建精度，并减少计算量。论文利用Segment Anything Model v2 (SAM-2) 进行图像分割，并结合alpha通道掩蔽技术，实现对草莓植株的精确分割。

**技术框架**：该框架主要包含以下几个阶段：1) **图像采集**：从多个角度拍摄草莓植株的图像。2) **图像分割**：使用SAM-2模型对图像进行分割，将草莓植株从背景中分离出来。3) **背景掩蔽**：利用alpha通道掩蔽技术，将背景区域设置为透明。4) **3D高斯溅射重建**：使用3D高斯溅射算法对分割后的草莓植株进行3D重建。5) **性状分析**：利用DBSCAN聚类和主成分分析（PCA）等方法，从重建的3D模型中提取植物的性状参数，如株高和冠层宽度。

**关键创新**：该论文的关键创新在于将对象中心的思想引入到基于3D高斯溅射的植物重建中。通过结合SAM-2和alpha通道掩蔽技术，实现了对植物的精确分割和背景去除，从而提高了重建精度和效率。这是与现有方法最本质的区别。

**关键设计**：在图像分割阶段，使用了Segment Anything Model v2 (SAM-2)，这是一个强大的图像分割模型，能够有效地将草莓植株从复杂的背景中分割出来。在背景掩蔽阶段，使用了alpha通道掩蔽技术，将背景区域设置为透明，从而避免了背景噪声的干扰。在性状分析阶段，使用了DBSCAN聚类和主成分分析（PCA）等方法，从重建的3D模型中提取植物的性状参数。这些参数的选择和配置对重建效果和性状分析的准确性至关重要，但论文中没有详细说明具体的参数设置。

## 📊 实验亮点

实验结果表明，该方法在草莓植株重建的准确性和效率方面均优于传统流程。通过引入对象中心重建策略，显著减少了计算时间，并提高了重建模型的精度。该方法能够自动估计重要的植物性状，例如株高和冠层宽度，为草莓植株表型分析提供了一种可扩展的非破坏性解决方案。具体的性能数据和提升幅度在摘要中没有明确给出。

## 🎯 应用场景

该研究成果可应用于精准农业领域，实现对草莓等农作物的非破坏性、高通量表型分析。通过自动提取植物的形态特征，可以辅助育种家选择优良品种，提高产量和品质。此外，该方法还可扩展到其他植物的3D重建和表型分析，具有广阔的应用前景。

## 📄 摘要（原文）

> Strawberries are among the most economically significant fruits in the United States, generating over $2 billion in annual farm-gate sales and accounting for approximately 13% of the total fruit production value. Plant phenotyping plays a vital role in selecting superior cultivars by characterizing plant traits such as morphology, canopy structure, and growth dynamics. However, traditional plant phenotyping methods are time-consuming, labor-intensive, and often destructive. Recently, neural rendering techniques, notably Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS), have emerged as powerful frameworks for high-fidelity 3D reconstruction. By capturing a sequence of multi-view images or videos around a target plant, these methods enable non-destructive reconstruction of complex plant architectures. Despite their promise, most current applications of 3DGS in agricultural domains reconstruct the entire scene, including background elements, which introduces noise, increases computational costs, and complicates downstream trait analysis. To address this limitation, we propose a novel object-centric 3D reconstruction framework incorporating a preprocessing pipeline that leverages the Segment Anything Model v2 (SAM-2) and alpha channel background masking to achieve clean strawberry plant reconstructions. This approach produces more accurate geometric representations while substantially reducing computational time. With a background-free reconstruction, our algorithm can automatically estimate important plant traits, such as plant height and canopy width, using DBSCAN clustering and Principal Component Analysis (PCA). Experimental results show that our method outperforms conventional pipelines in both accuracy and efficiency, offering a scalable and non-destructive solution for strawberry plant phenotyping.

