---
layout: default
title: Differentiable NMS via Sinkhorn Matching for End-to-End Fabric Defect Detection
---

# Differentiable NMS via Sinkhorn Matching for End-to-End Fabric Defect Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07040" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07040v1</a>
  <a href="https://arxiv.org/pdf/2505.07040.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07040v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07040v1', 'Differentiable NMS via Sinkhorn Matching for End-to-End Fabric Defect Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhengyang Lu, Bingjie Lu, Weifan Wang, Feng Wang

**分类**: cs.CV

**发布日期**: 2025-05-11

---

## 💡 一句话要点

**提出可微分NMS框架以解决织物缺陷检测问题**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `织物缺陷检测` `可微分NMS` `端到端学习` `Sinkhorn-Knopp算法` `深度学习` `图像处理` `质量控制`

## 📋 核心要点

1. 现有的织物缺陷检测方法在梯度流和像素级标注获取上存在显著不足，限制了端到端学习的有效性。
2. 本文提出了一种可微分NMS框架，通过将NMS转化为可微分的二分匹配问题，保持了网络中的梯度流畅性。
3. 在Tianchi数据集上的实验结果显示，该方法在定位精度上显著提升，且适用于实时工业应用。

## 📝 摘要（中文）

织物缺陷检测面临两个基本挑战：传统的非极大值抑制（NMS）破坏了梯度流，阻碍了真正的端到端学习；在工业规模上获取像素级标注成本过高。为了解决这些问题，本文提出了一种可微分NMS框架，通过端到端优化实现更高的定位精度。我们将NMS重新表述为可微分的二分匹配问题，并通过Sinkhorn-Knopp算法求解，确保网络中的梯度流畅。该方法针对织物缺陷的不规则形态和模糊边界，综合考虑提议质量、特征相似性和空间关系。我们的熵约束掩膜精炼机制通过原则性的不确定性建模进一步提升了定位精度。在Tianchi织物缺陷数据集上的大量实验表明，该方法在性能上显著优于现有方法，同时保持适合工业部署的实时速度。

## 🔬 方法详解

**问题定义**：本文旨在解决传统非极大值抑制（NMS）在织物缺陷检测中的梯度流问题，以及工业规模下获取像素级标注的高成本。

**核心思路**：通过将NMS重新表述为可微分的二分匹配问题，利用Sinkhorn-Knopp算法实现端到端优化，从而保持梯度流畅性并提升定位精度。

**技术框架**：整体架构包括数据输入、特征提取、可微分NMS模块和熵约束掩膜精炼机制。特征提取使用深度学习网络，NMS模块通过Sinkhorn-Knopp算法进行优化，掩膜精炼机制则用于进一步提高定位精度。

**关键创新**：最重要的创新点在于将NMS转化为可微分形式，解决了传统方法中梯度流断裂的问题，使得整个网络可以进行端到端训练。

**关键设计**：在设计中，采用了熵约束损失函数来建模不确定性，并在网络结构中集成了特征相似性和空间关系的考虑，以提升对织物缺陷的检测能力。

## 📊 实验亮点

在Tianchi织物缺陷数据集上的实验结果显示，本文方法在定位精度上相比现有方法提升了显著的性能，且保持实时处理速度，适合工业应用。

## 🎯 应用场景

该研究的潜在应用领域包括纺织工业中的质量控制和缺陷检测，能够有效提高生产效率和产品质量。未来，该框架还可扩展至其他物体检测任务，具有广泛的实际价值和影响力。

## 📄 摘要（原文）

> Fabric defect detection confronts two fundamental challenges. First, conventional non-maximum suppression disrupts gradient flow, which hinders genuine end-to-end learning. Second, acquiring pixel-level annotations at industrial scale is prohibitively costly. Addressing these limitations, we propose a differentiable NMS framework for fabric defect detection that achieves superior localization precision through end-to-end optimization. We reformulate NMS as a differentiable bipartite matching problem solved through the Sinkhorn-Knopp algorithm, maintaining uninterrupted gradient flow throughout the network. This approach specifically targets the irregular morphologies and ambiguous boundaries of fabric defects by integrating proposal quality, feature similarity, and spatial relationships. Our entropy-constrained mask refinement mechanism further enhances localization precision through principled uncertainty modeling. Extensive experiments on the Tianchi fabric defect dataset demonstrate significant performance improvements over existing methods while maintaining real-time speeds suitable for industrial deployment. The framework exhibits remarkable adaptability across different architectures and generalizes effectively to general object detection tasks.

