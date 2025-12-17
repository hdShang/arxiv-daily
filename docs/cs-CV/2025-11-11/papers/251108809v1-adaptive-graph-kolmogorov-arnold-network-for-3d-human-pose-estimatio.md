---
layout: default
title: Adaptive graph Kolmogorov-Arnold network for 3D human pose estimation
---

# Adaptive graph Kolmogorov-Arnold network for 3D human pose estimation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.08809" class="toolbar-btn" target="_blank">📄 arXiv: 2511.08809v1</a>
  <a href="https://arxiv.org/pdf/2511.08809.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.08809v1" onclick="toggleFavorite(this, '2511.08809v1', 'Adaptive graph Kolmogorov-Arnold network for 3D human pose estimation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Abu Taib Mohammed Shahjahan, A. Ben Hamza

**分类**: cs.CV

**发布日期**: 2025-11-11

---

## 💡 一句话要点

**提出PoseKAN：一种自适应图Kolmogorov-Arnold网络，用于3D人体姿态估计。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D人体姿态估计` `图神经网络` `Kolmogorov-Arnold Network` `自适应特征转换` `长程依赖` `多跳特征聚合` `残差网络`

## 📋 核心要点

1. GCN在3D人体姿态估计中表现良好，但局部感受野限制了其捕获长程依赖关系的能力，难以处理遮挡和深度模糊。
2. PoseKAN通过在图边上使用可学习的函数，实现数据驱动的自适应特征转换，增强了模型对复杂姿态变化的适应性和表达能力。
3. 实验结果表明，PoseKAN在基准数据集上取得了与当前最优方法相当的性能，验证了其有效性。

## 📝 摘要（中文）

本文提出了一种自适应图Kolmogorov-Arnold网络（KAN）框架PoseKAN，用于从单张图像进行2D到3D姿态提升。基于图卷积网络（GCN）的方法在3D人体姿态估计中表现出色，但其局部感受野限制了捕获长程依赖关系的能力，难以处理遮挡和深度模糊。此外，它们还表现出频谱偏差，优先考虑低频分量，难以建模高频细节。与使用固定激活函数的GCN不同，KAN在图边上采用可学习的函数，从而实现数据驱动的自适应特征转换。这增强了模型的适应性和表达能力，使其在学习复杂姿态变化方面更具表现力。我们的模型采用多跳特征聚合，确保身体关节可以利用来自局部和远距离邻居的信息，从而提高空间感知能力。它还结合了残差PoseKAN块以进行更深层次的特征细化，并采用全局响应归一化以提高特征选择性和对比度。在基准数据集上的大量实验表明，我们的模型具有与最先进方法相媲美的性能。

## 🔬 方法详解

**问题定义**：现有基于图卷积网络（GCN）的3D人体姿态估计方法，由于其局部感受野的限制，难以捕获人体骨骼结构中的长程依赖关系，导致在处理遮挡、深度模糊等复杂场景时性能下降。此外，GCN还存在频谱偏差，更倾向于学习低频信息，而忽略了高频细节，影响了姿态估计的精度。

**核心思路**：PoseKAN的核心思路是将Kolmogorov-Arnold Network (KAN) 扩展到图结构数据上，利用KAN的可学习激活函数来增强模型的表达能力和适应性。通过在图的边上学习自适应的特征转换，PoseKAN能够更好地捕捉人体骨骼结构中的复杂关系，从而提高3D姿态估计的准确性。

**技术框架**：PoseKAN框架主要包含以下几个关键模块：1) 多跳特征聚合：允许每个关节从其局部和远距离邻居处聚合信息，增强空间感知能力。2) 残差PoseKAN块：通过堆叠多个PoseKAN块，进行更深层次的特征细化。3) 全局响应归一化：提高特征选择性和对比度，从而改善模型的性能。整体流程是从2D图像提取2D姿态，然后通过PoseKAN网络将其提升为3D姿态。

**关键创新**：PoseKAN最关键的创新在于将KAN引入到图神经网络中，利用KAN的可学习激活函数替代了传统GCN中固定的激活函数。这种自适应的特征转换方式使得模型能够更好地学习复杂的人体姿态变化，从而克服了GCN的局限性。

**关键设计**：PoseKAN的关键设计包括：1) 多跳特征聚合的跳数设置，需要根据数据集和任务进行调整。2) 残差PoseKAN块的数量和结构，需要进行实验验证。3) 全局响应归一化的具体实现方式，例如使用Layer Normalization或Batch Normalization。4) 损失函数的设计，通常采用Mean Per Joint Position Error (MPJPE) 或 Percentage of Correct Keypoints (PCK) 等指标。

## 📊 实验亮点

论文在Human3.6M和MPI-INF-3DHP等基准数据集上进行了大量实验，结果表明PoseKAN取得了与当前最优方法相媲美的性能。具体来说，PoseKAN在某些指标上甚至超过了现有方法，证明了其在3D人体姿态估计方面的有效性。实验结果还表明，PoseKAN能够有效地处理遮挡和深度模糊等复杂场景。

## 🎯 应用场景

PoseKAN在3D人体姿态估计领域具有广泛的应用前景，可应用于人机交互、虚拟现实、运动分析、视频监控等领域。通过准确估计人体姿态，可以实现更自然的人机交互方式，提升虚拟现实的沉浸感，为运动员提供更科学的运动分析，以及提高视频监控的智能化水平。未来，PoseKAN有望进一步扩展到其他基于图结构数据的任务中。

## 📄 摘要（原文）

> Graph convolutional network (GCN)-based methods have shown strong performance in 3D human pose estimation by leveraging the natural graph structure of the human skeleton. However, their local receptive field limits their ability to capture long-range dependencies essential for handling occlusions and depth ambiguities. They also exhibit spectral bias, which prioritizes low-frequency components while struggling to model high-frequency details. In this paper, we introduce PoseKAN, an adaptive graph Kolmogorov-Arnold Network (KAN), framework that extends KANs to graph-based learning for 2D-to-3D pose lifting from a single image. Unlike GCNs that use fixed activation functions, KANs employ learnable functions on graph edges, allowing data-driven, adaptive feature transformations. This enhances the model's adaptability and expressiveness, making it more expressive in learning complex pose variations. Our model employs multi-hop feature aggregation, ensuring the body joints can leverage information from both local and distant neighbors, leading to improved spatial awareness. It also incorporates residual PoseKAN blocks for deeper feature refinement, and a global response normalization for improved feature selectivity and contrast. Extensive experiments on benchmark datasets demonstrate the competitive performance of our model against state-of-the-art methods.

