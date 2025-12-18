---
layout: default
title: PFF-Net: Patch Feature Fitting for Point Cloud Normal Estimation
---

# PFF-Net: Patch Feature Fitting for Point Cloud Normal Estimation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.21365" class="toolbar-btn" target="_blank">📄 arXiv: 2511.21365v1</a>
  <a href="https://arxiv.org/pdf/2511.21365.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.21365v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.21365v1', 'PFF-Net: Patch Feature Fitting for Point Cloud Normal Estimation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qing Li, Huifang Feng, Kanle Shi, Yue Gao, Yi Fang, Yu-Shen Liu, Zhizhong Han

**分类**: cs.CV

**发布日期**: 2025-11-26

**备注**: Accepted by TVCG

---

## 💡 一句话要点

**提出PFF-Net，通过多尺度patch特征拟合实现鲁棒的点云法向量估计。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `点云法向量估计` `多尺度特征` `特征拟合` `点云处理` `三维重建`

## 📋 核心要点

1. 现有方法难以选择合适的邻域大小，且参数量大，难以准确高效地预测各种点云的法向量。
2. 提出Patch Feature Fitting (PFF)网络，通过多尺度特征聚合和跨尺度特征补偿，逼近最优几何描述。
3. 实验表明，PFF-Net在合成和真实数据集上均取得了SOTA性能，同时降低了参数量和运行时间。

## 📝 摘要（中文）

本文提出了一种新的点云法向量鲁棒估计的特征提取方法。针对不同数据或几何形状难以确定合适邻域大小的问题，本文融合来自不同邻域大小的多尺度特征。通过多尺度特征建模patch特征拟合(PFF)，以逼近法向量估计的最佳几何描述，并通过多尺度特征聚合和跨尺度特征补偿实现逼近过程。特征聚合模块逐步将不同尺度的patch特征聚合到patch中心，并通过移除远离中心的点来缩小patch大小，从而精确捕获广泛范围内的结构特征，并描述高度详细的几何形状。特征补偿模块确保了来自早期较大尺度层的特征的可重用性，并揭示了不同patch大小中的相关信息。基于多尺度特征聚合的逼近策略使模型能够实现不同局部patch的尺度自适应，并提供最佳的特征描述。大量实验表明，该方法在合成和真实世界数据集上均实现了最先进的性能，同时减少了网络参数和运行时间。

## 🔬 方法详解

**问题定义**：点云法向量估计是三维视觉中的基本问题。现有方法依赖于构建局部patch来提供中心周围的上下文信息，但当处理不同的数据或几何形状时，确定合适的邻域大小是一个挑战。现有方法通常采用各种参数繁重的策略从输入patch中提取完整的特征描述，但在准确有效地预测各种点云的法向量方面仍然存在困难。

**核心思路**：本文的核心思路是利用多尺度patch特征拟合（PFF）来解决邻域大小选择的问题。通过融合来自不同邻域大小的特征，模型能够自适应地处理不同尺度和几何形状的点云数据。PFF旨在逼近法向量估计的最佳几何描述，从而提高法向量估计的准确性和鲁棒性。

**技术框架**：PFF-Net的整体框架包括多尺度特征提取、特征聚合模块和特征补偿模块。首先，从不同尺度的邻域提取patch特征。然后，特征聚合模块逐步聚合不同尺度的patch特征到patch中心，并缩小patch大小。特征补偿模块则确保了来自早期较大尺度层的特征的可重用性，并揭示不同patch大小中的相关信息。最后，利用聚合和补偿后的特征进行法向量估计。

**关键创新**：该方法最重要的创新点在于提出了多尺度patch特征拟合的思想，通过聚合和补偿不同尺度的特征，实现了对不同局部patch的尺度自适应。与现有方法相比，PFF-Net不需要手动选择邻域大小，而是通过网络自动学习最优的特征表示。此外，特征补偿模块的设计也提高了特征的利用率，减少了冗余计算。

**关键设计**：在网络结构方面，具体使用了哪些卷积层、池化层、激活函数等信息未知。损失函数的设计也未知。多尺度特征提取的具体尺度选择策略也未知。特征聚合模块和特征补偿模块的具体实现细节，例如聚合方式（加权平均、拼接等）和补偿方式（残差连接、注意力机制等）也未知。

## 📊 实验亮点

实验结果表明，PFF-Net在合成和真实数据集上均取得了state-of-the-art的性能。与现有方法相比，PFF-Net在保证精度的同时，显著减少了网络参数和运行时间，更易于部署和应用。具体的性能提升数据和对比基线未知。

## 🎯 应用场景

该研究成果可广泛应用于三维重建、SLAM、机器人导航、自动驾驶等领域。准确的点云法向量估计是这些应用的基础，能够提高场景理解和物体识别的精度。此外，该方法在处理复杂几何形状和噪声数据方面的鲁棒性，使其在实际应用中具有更高的价值。

## 📄 摘要（原文）

> Estimating the normal of a point requires constructing a local patch to provide center-surrounding context, but determining the appropriate neighborhood size is difficult when dealing with different data or geometries. Existing methods commonly employ various parameter-heavy strategies to extract a full feature description from the input patch. However, they still have difficulties in accurately and efficiently predicting normals for various point clouds. In this work, we present a new idea of feature extraction for robust normal estimation of point clouds. We use the fusion of multi-scale features from different neighborhood sizes to address the issue of selecting reasonable patch sizes for various data or geometries. We seek to model a patch feature fitting (PFF) based on multi-scale features to approximate the optimal geometric description for normal estimation and implement the approximation process via multi-scale feature aggregation and cross-scale feature compensation. The feature aggregation module progressively aggregates the patch features of different scales to the center of the patch and shrinks the patch size by removing points far from the center. It not only enables the network to precisely capture the structure characteristic in a wide range, but also describes highly detailed geometries. The feature compensation module ensures the reusability of features from earlier layers of large scales and reveals associated information in different patch sizes. Our approximation strategy based on aggregating the features of multiple scales enables the model to achieve scale adaptation of varying local patches and deliver the optimal feature description. Extensive experiments demonstrate that our method achieves state-of-the-art performance on both synthetic and real-world datasets with fewer network parameters and running time.

