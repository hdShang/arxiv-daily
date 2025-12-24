---
layout: default
title: "GraphGSOcc: Semantic-Geometric Graph Transformer with Dynamic-Static Decoupling for 3D Gaussian Splatting-based Occupancy Prediction"
---

# GraphGSOcc: Semantic-Geometric Graph Transformer with Dynamic-Static Decoupling for 3D Gaussian Splatting-based Occupancy Prediction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14825" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14825v2</a>
  <a href="https://arxiv.org/pdf/2506.14825.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14825v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14825v2', 'GraphGSOcc: Semantic-Geometric Graph Transformer with Dynamic-Static Decoupling for 3D Gaussian Splatting-based Occupancy Prediction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ke Song, Yunhe Wu, Chunchit Siu, Huiyuan Xiong

**分类**: cs.CV, cs.AI

**发布日期**: 2025-06-13 (更新: 2025-07-02)

---

## 💡 一句话要点

**提出GraphGSOcc以解决3D语义占用预测中的动态静态耦合问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `3D语义占用预测` `高斯点云` `图神经网络` `动态静态解耦` `自动驾驶` `特征聚合` `深度学习`

## 📋 核心要点

1. 现有3D高斯点云方法在特征聚合时未能充分考虑语义关联，导致预测精度不足。
2. 提出GraphGSOcc模型，通过动态构建双图结构，优化动态与静态对象的解耦，提升占用预测性能。
3. 在SurroundOcc数据集上，GraphGSOcc实现了25.20%的mIoU，相较于GaussianWorld提升了1.97%的mIoU，并减少了13.7%的GPU内存使用。

## 📝 摘要（中文）

针对自动驾驶中的3D语义占用预测任务，本文解决了现有3D高斯点云方法中的两个关键问题：一是统一特征聚合忽视了相似类别和区域间的语义关联，二是缺乏几何约束导致的边界模糊。我们提出了GraphGSOcc模型，结合语义和几何图形Transformer，并对动态与静态对象优化进行解耦。通过动态构建双图结构，优化特征聚合和语义关系编码，GraphGSOcc在多个占用基准测试中实现了最先进的性能，展示了显著的内存和精度提升。

## 🔬 方法详解

**问题定义**：本文旨在解决3D语义占用预测中的动态与静态对象耦合问题，现有方法在特征聚合和边界处理上存在不足，导致预测精度和效率低下。

**核心思路**：我们提出GraphGSOcc模型，通过结合语义和几何图Transformer，动态构建双图结构以优化特征聚合，同时解耦动态与静态对象的优化过程，从而提升预测性能。

**技术框架**：GraphGSOcc的整体架构包括双图结构的构建：几何图用于计算KNN搜索半径，语义图用于保留高相关节点。结合多尺度图注意力机制，优化边界细节和对象级拓扑。

**关键创新**：最重要的创新在于提出了双高斯图注意力机制，动态构建几何和语义图，显著改善了特征聚合的效果，并通过解耦动态与静态对象的优化，提升了整体预测性能。

**关键设计**：在模型设计中，采用了动态-静态解耦高斯注意力机制，设置了特定的损失函数以优化动态对象和静态场景的预测效果，同时在网络结构中引入了多尺度图注意力以增强特征表达能力。

## 📊 实验亮点

在SurroundOcc数据集上，GraphGSOcc实现了25.20%的mIoU，相较于基线GaussianWorld提升了1.97%的mIoU，同时GPU内存使用减少至6.8 GB，降低了13.7%。这些结果表明该模型在占用预测任务中的有效性和高效性。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、机器人导航和智能交通系统等。通过提升3D语义占用预测的精度和效率，GraphGSOcc能够为自动驾驶车辆提供更可靠的环境感知能力，进而推动智能交通的安全性和效率。未来，该方法也可能扩展到其他需要3D空间理解的领域，如增强现实和虚拟现实。

## 📄 摘要（原文）

> Addressing the task of 3D semantic occupancy prediction for autonomous driving, we tackle two key issues in existing 3D Gaussian Splatting (3DGS) methods: (1) unified feature aggregation neglecting semantic correlations among similar categories and across regions, (2) boundary ambiguities caused by the lack of geometric constraints in MLP iterative optimization and (3) biased issues in dynamic-static object coupling optimization. We propose the GraphGSOcc model, a novel framework that combines semantic and geometric graph Transformer and decouples dynamic-static objects optimization for 3D Gaussian Splatting-based Occupancy Prediction. We propose the Dual Gaussians Graph Attenntion, which dynamically constructs dual graph structures: a geometric graph adaptively calculating KNN search radii based on Gaussian poses, enabling large-scale Gaussians to aggregate features from broader neighborhoods while compact Gaussians focus on local geometric consistency; a semantic graph retaining top-M highly correlated nodes via cosine similarity to explicitly encode semantic relationships within and across instances. Coupled with the Multi-scale Graph Attention framework, fine-grained attention at lower layers optimizes boundary details, while coarsegrained attention at higher layers models object-level topology. On the other hand, we decouple dynamic and static objects by leveraging semantic probability distributions and design a Dynamic-Static Decoupled Gaussian Attention mechanism to optimize the prediction performance for both dynamic objects and static scenes. GraphGSOcc achieves state-ofthe-art performance on the SurroundOcc-nuScenes, Occ3D-nuScenes, OpenOcc and KITTI occupancy benchmarks. Experiments on the SurroundOcc dataset achieve an mIoU of 25.20%, reducing GPU memory to 6.8 GB, demonstrating a 1.97% mIoU improvement and 13.7% memory reduction compared to GaussianWorld.

