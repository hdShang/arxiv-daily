---
layout: default
title: "THE-Pose: Topological Prior with Hybrid Graph Fusion for Estimating Category-Level 6D Object Pose"
---

# THE-Pose: Topological Prior with Hybrid Graph Fusion for Estimating Category-Level 6D Object Pose

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.10251" class="toolbar-btn" target="_blank">📄 arXiv: 2512.10251v1</a>
  <a href="https://arxiv.org/pdf/2512.10251.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.10251v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.10251v1', 'THE-Pose: Topological Prior with Hybrid Graph Fusion for Estimating Category-Level 6D Object Pose')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Eunho Lee, Chaehyeon Song, Seunghoon Jeong, Ayoung Kim

**分类**: cs.CV

**发布日期**: 2025-12-11

**🔗 代码/项目**: [GITHUB](https://github.com/EHxxx/THE-Pose)

---

## 💡 一句话要点

**THE-Pose：融合拓扑先验与混合图的类别级6D位姿估计**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `6D位姿估计` `类别级位姿估计` `拓扑先验` `图卷积网络` `混合图融合` `机器人视觉` `三维重建`

## 📋 核心要点

1. 现有3D图卷积方法在类别级位姿估计中，难以有效利用全局上下文信息，对复杂物体和遮挡场景鲁棒性不足。
2. THE-Pose通过表面嵌入提取拓扑特征，并设计混合图融合模块，将2D图像上下文与3D几何结构相结合。
3. 实验结果表明，THE-Pose在REAL275数据集上显著优于现有方法，尤其是在复杂物体和遮挡场景下。

## 📝 摘要（中文）

本文提出了一种新的类别级6D物体位姿估计框架THE-Pose，该框架利用表面嵌入的拓扑先验和混合图融合来解决类内差异带来的鲁棒性问题。现有基于3D图卷积（3D-GC）的方法仅关注局部几何和深度信息，难以处理复杂物体和视觉歧义。THE-Pose从图像域提取一致且不变的拓扑特征，有效克服了现有3D-GC方法的局限性。提出的混合图融合（HGF）模块自适应地将拓扑特征与点云特征融合，无缝连接2D图像上下文和3D几何结构。融合后的特征确保了对未见或复杂物体的稳定性，即使在严重遮挡下也能保持性能。在REAL275数据集上的大量实验表明，THE-Pose相比于3D-GC基线（HS-Pose）提升了35.8%，并且在所有关键指标上超越了先前的SOTA方法7.2%。

## 🔬 方法详解

**问题定义**：类别级6D物体位姿估计旨在预测属于同一类别的物体的精确位姿，由于类内差异大、遮挡严重等问题，现有方法难以保证鲁棒性和准确性。特别是基于3D图卷积的方法，过度依赖局部几何信息，忽略了全局上下文，导致在复杂场景下性能下降。

**核心思路**：本文的核心思路是利用拓扑先验来增强位姿估计的鲁棒性。拓扑特征对物体的形变和遮挡具有不变性，能够提供更稳定的全局上下文信息。通过将拓扑特征与局部几何特征融合，可以有效克服现有方法的局限性。

**技术框架**：THE-Pose框架主要包含以下几个模块：1) 拓扑特征提取模块：从输入图像中提取拓扑特征，例如环路、孔洞等。2) 点云特征提取模块：从3D点云中提取几何特征。3) 混合图融合（HGF）模块：自适应地将拓扑特征和点云特征融合。4) 位姿估计模块：利用融合后的特征估计物体的6D位姿。

**关键创新**：最重要的创新点在于拓扑先验的引入和混合图融合模块的设计。传统的位姿估计方法主要依赖于几何信息，而THE-Pose通过引入拓扑信息，增强了对物体形变和遮挡的鲁棒性。混合图融合模块能够自适应地学习拓扑特征和几何特征之间的关系，从而实现更有效的特征融合。

**关键设计**：拓扑特征提取模块使用预训练的深度学习模型提取图像特征，然后通过拓扑保持的降维方法将特征映射到低维空间。混合图融合模块使用注意力机制来学习拓扑特征和几何特征的权重，从而实现自适应的特征融合。位姿估计模块使用回归网络预测物体的旋转和平移。

## 📊 实验亮点

THE-Pose在REAL275数据集上取得了显著的性能提升。相比于3D-GC基线（HS-Pose），THE-Pose在所有关键指标上提升了35.8%。与之前的SOTA方法相比，THE-Pose也取得了7.2%的提升。这些结果表明，THE-Pose在类别级6D位姿估计方面具有显著的优势，尤其是在处理复杂物体和遮挡场景时。

## 🎯 应用场景

该研究成果可应用于机器人抓取、自动驾驶、增强现实等领域。在机器人抓取中，准确的位姿估计可以帮助机器人更好地识别和抓取物体。在自动驾驶中，可以用于车辆和行人的精确感知。在增强现实中，可以实现虚拟物体与真实场景的无缝融合。未来，该方法可以进一步扩展到更复杂的场景和物体类别，具有广阔的应用前景。

## 📄 摘要（原文）

> Category-level object pose estimation requires both global context and local structure to ensure robustness against intra-class variations. However, 3D graph convolution (3D-GC) methods only focus on local geometry and depth information, making them vulnerable to complex objects and visual ambiguities. To address this, we present THE-Pose, a novel category-level 6D pose estimation framework that leverages a topological prior via surface embedding and hybrid graph fusion. Specifically, we extract consistent and invariant topological features from the image domain, effectively overcoming the limitations inherent in existing 3D-GC based methods. Our Hybrid Graph Fusion (HGF) module adaptively integrates the topological features with point-cloud features, seamlessly bridging 2D image context and 3D geometric structure. These fused features ensure stability for unseen or complicated objects, even under significant occlusions. Extensive experiments on the REAL275 dataset show that THE-Pose achieves a 35.8% improvement over the 3D-GC baseline (HS-Pose) and surpasses the previous state-of-the-art by 7.2% across all key metrics. The code is avaialbe on https://github.com/EHxxx/THE-Pose

