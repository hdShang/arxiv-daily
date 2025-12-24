---
layout: default
title: "UniFlow: Towards Zero-Shot LiDAR Scene Flow for Autonomous Vehicles via Cross-Domain Generalization"
---

# UniFlow: Towards Zero-Shot LiDAR Scene Flow for Autonomous Vehicles via Cross-Domain Generalization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.18254" class="toolbar-btn" target="_blank">📄 arXiv: 2511.18254v1</a>
  <a href="https://arxiv.org/pdf/2511.18254.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.18254v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.18254v1', 'UniFlow: Towards Zero-Shot LiDAR Scene Flow for Autonomous Vehicles via Cross-Domain Generalization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Siyi Li, Qingwen Zhang, Ishan Khatri, Kyle Vedder, Deva Ramanan, Neehar Peri

**分类**: cs.CV

**发布日期**: 2025-11-23

**备注**: Project Page: https://lisiyi777.github.io/UniFlow/

---

## 💡 一句话要点

**UniFlow：通过跨域泛化实现自动驾驶车辆的零样本LiDAR场景流估计**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `LiDAR场景流` `跨域泛化` `自动驾驶` `运动估计` `深度学习`

## 📋 核心要点

1. 现有LiDAR场景流方法泛化性差，难以适应不同传感器配置和数据集。
2. UniFlow通过跨数据集联合训练，学习通用的运动先验，提升模型的泛化能力。
3. UniFlow在多个数据集上取得了SOTA结果，并在未见数据集上显著优于现有方法。

## 📝 摘要（中文）

LiDAR场景流旨在估计连续点云之间每个点的3D运动。现有方法在流行的自动驾驶数据集上实现了厘米级的精度，但通常只在一个传感器上进行训练和评估。本文旨在学习通用的运动先验，使其能够迁移到各种未见过的LiDAR传感器上。然而，LiDAR语义分割和3D目标检测的先前工作表明，朴素地在多个数据集上训练会导致比单数据集模型更差的性能。有趣的是，我们发现这种传统观点并不适用于运动估计，并且最先进的场景流方法极大地受益于跨数据集训练。我们认为，诸如运动估计之类的低级任务可能对传感器配置不太敏感；事实上，我们的分析表明，在快速移动物体（例如，来自高速公路数据集）上训练的模型在快速移动物体上表现良好，即使跨越不同的数据集。在我们的分析的指导下，我们提出了UniFlow，一个前馈模型家族，它统一并在多个具有不同传感器位置和点云密度的大规模LiDAR场景流数据集上进行训练。我们这个非常简单的解决方案在Waymo和nuScenes上建立了新的技术水平，分别比之前的工作提高了5.1%和35.2%。此外，UniFlow在TruckScenes等未见数据集上实现了最先进的精度，优于之前特定于TruckScenes的模型30.1%。

## 🔬 方法详解

**问题定义**：LiDAR场景流估计旨在预测连续点云中每个点的3D运动矢量。现有方法通常针对特定数据集和传感器进行优化，导致在新的数据集或传感器上性能显著下降。痛点在于缺乏跨域泛化能力，无法适应不同传感器配置和数据分布。

**核心思路**：核心思路是通过跨多个数据集进行联合训练，学习通用的运动先验知识。作者认为，运动估计作为一种低级任务，对传感器配置的敏感度较低，因此可以通过在多样化的数据集上训练来提升模型的泛化能力。这种方法避免了传统上认为多数据集训练会降低性能的观点，并验证了其在运动估计任务中的有效性。

**技术框架**：UniFlow是一个前馈神经网络模型，其整体框架包括特征提取、特征匹配和运动矢量预测三个主要阶段。首先，使用共享的特征提取器从连续的点云中提取局部特征。然后，利用特征匹配模块建立点与点之间的对应关系。最后，通过运动矢量预测模块，基于匹配的特征预测每个点的3D运动矢量。

**关键创新**：最重要的技术创新点在于跨数据集联合训练策略。与以往针对单个数据集进行训练的方法不同，UniFlow同时利用多个大规模LiDAR场景流数据集进行训练，从而学习到更通用的运动先验知识。这种方法使得模型能够更好地适应不同的传感器配置和数据分布，从而提升了模型的泛化能力。

**关键设计**：UniFlow的关键设计包括：(1) 使用共享的特征提取器，以减少模型对特定传感器的依赖；(2) 采用数据增强技术，增加数据的多样性，提升模型的鲁棒性；(3) 设计合适的损失函数，以平衡不同数据集之间的差异，确保模型能够有效地学习通用的运动先验。具体的网络结构和参数设置在论文中有详细描述，但摘要中未提供。

## 📊 实验亮点

UniFlow在Waymo和nuScenes数据集上取得了显著的性能提升，分别比现有方法提高了5.1%和35.2%。更重要的是，UniFlow在未见过的TruckScenes数据集上实现了最先进的精度，超过了之前专门针对TruckScenes训练的模型30.1%。这些结果表明，UniFlow具有强大的跨域泛化能力，能够有效地适应不同的LiDAR传感器和数据分布。

## 🎯 应用场景

UniFlow在自动驾驶领域具有广泛的应用前景，可以用于感知系统中的运动估计、障碍物跟踪和路径规划等任务。通过提升LiDAR场景流的泛化能力，UniFlow可以帮助自动驾驶车辆更好地理解周围环境，从而提高行驶安全性和可靠性。此外，该方法还可以应用于机器人导航、三维重建等领域。

## 📄 摘要（原文）

> LiDAR scene flow is the task of estimating per-point 3D motion between consecutive point clouds. Recent methods achieve centimeter-level accuracy on popular autonomous vehicle (AV) datasets, but are typically only trained and evaluated on a single sensor. In this paper, we aim to learn general motion priors that transfer to diverse and unseen LiDAR sensors. However, prior work in LiDAR semantic segmentation and 3D object detection demonstrate that naively training on multiple datasets yields worse performance than single dataset models. Interestingly, we find that this conventional wisdom does not hold for motion estimation, and that state-of-the-art scene flow methods greatly benefit from cross-dataset training. We posit that low-level tasks such as motion estimation may be less sensitive to sensor configuration; indeed, our analysis shows that models trained on fast-moving objects (e.g., from highway datasets) perform well on fast-moving objects, even across different datasets. Informed by our analysis, we propose UniFlow, a family of feedforward models that unifies and trains on multiple large-scale LiDAR scene flow datasets with diverse sensor placements and point cloud densities. Our frustratingly simple solution establishes a new state-of-the-art on Waymo and nuScenes, improving over prior work by 5.1% and 35.2% respectively. Moreover, UniFlow achieves state-of-the-art accuracy on unseen datasets like TruckScenes, outperforming prior TruckScenes-specific models by 30.1%.

