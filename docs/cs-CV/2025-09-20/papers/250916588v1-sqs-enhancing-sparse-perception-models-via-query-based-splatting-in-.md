---
layout: default
title: "SQS: Enhancing Sparse Perception Models via Query-based Splatting in Autonomous Driving"
---

# SQS: Enhancing Sparse Perception Models via Query-based Splatting in Autonomous Driving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16588" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16588v1</a>
  <a href="https://arxiv.org/pdf/2509.16588.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16588v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16588v1', 'SQS: Enhancing Sparse Perception Models via Query-based Splatting in Autonomous Driving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haiming Zhang, Yiyao Zhu, Wending Zhou, Xu Yan, Yingjie Cai, Bingbing Liu, Shuguang Cui, Zhen Li

**分类**: cs.CV, cs.AI, cs.RO

**发布日期**: 2025-09-20

**备注**: NeurIPS 2025 (Spotlight)

---

## 💡 一句话要点

**SQS：基于查询Splatting增强自动驾驶稀疏感知模型**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `稀疏感知模型` `查询Splatting` `预训练` `自动驾驶` `3D感知` `占据预测` `目标检测`

## 📋 核心要点

1. 稀疏感知模型避免了显式的密集BEV或体素构建，但缺乏足够的上下文信息。
2. SQS通过预训练学习细粒度上下文特征，利用自监督Splatting重建多视角图像和深度图。
3. SQS在占据预测和3D目标检测等任务上显著提升性能，优于现有预训练方法。

## 📝 摘要（中文）

本文提出SQS，一种新颖的基于查询的Splatting预训练方法，旨在提升自动驾驶中稀疏感知模型（SPMs）的性能。SQS引入了一个插件模块，在预训练期间从稀疏查询中预测3D高斯表示，利用自监督Splatting通过重建多视角图像和深度图来学习细粒度的上下文特征。在微调阶段，预训练的高斯查询通过查询交互机制无缝集成到下游网络中，从而将预训练查询与特定任务查询显式连接，有效地适应了占据预测和3D目标检测的多样化需求。在自动驾驶基准测试上的大量实验表明，SQS在多个基于查询的3D感知任务（尤其是在占据预测和3D目标检测方面）提供了显著的性能提升，明显优于先前的最先进的预训练方法（即，在占据预测上+1.3 mIoU，在3D检测上+1.0 NDS）。

## 🔬 方法详解

**问题定义**：现有的稀疏感知模型（SPMs）虽然计算效率高，但由于缺乏显式的密集BEV或体素表示，难以捕捉充分的上下文信息，限制了其在复杂自动驾驶场景中的感知能力。尤其是在处理遮挡、光照变化等问题时，性能会显著下降。

**核心思路**：SQS的核心思路是利用基于查询的Splatting进行预训练，学习细粒度的上下文特征。通过从稀疏查询中预测3D高斯表示，并利用自监督Splatting重建多视角图像和深度图，模型能够学习到更丰富的场景信息。这种方法旨在弥补SPMs在上下文感知方面的不足，从而提升其整体性能。

**技术框架**：SQS包含一个插件模块，该模块在预训练阶段从稀疏查询中预测3D高斯表示。该模块接收稀疏查询作为输入，输出一组3D高斯参数，这些参数描述了场景中的几何和外观信息。然后，利用这些高斯参数进行Splatting操作，将3D信息投影到2D图像平面上，并重建多视角图像和深度图。通过最小化重建误差，模型可以学习到更准确的3D场景表示。在微调阶段，预训练的高斯查询通过查询交互机制与下游任务的特定查询进行连接，从而将预训练知识迁移到下游任务中。

**关键创新**：SQS的关键创新在于其基于查询的Splatting预训练方法。与传统的预训练方法不同，SQS直接从稀疏查询中学习3D场景表示，避免了显式的密集表示构建，从而保持了计算效率。此外，SQS利用自监督Splatting进行预训练，无需人工标注，降低了训练成本。

**关键设计**：SQS的关键设计包括：1) 3D高斯表示的参数化方式，例如均值、方差、颜色等；2) 自监督Splatting的损失函数，例如图像重建损失和深度图重建损失；3) 查询交互机制的设计，例如注意力机制或交叉注意力机制，用于将预训练查询与下游任务查询进行融合。

## 📊 实验亮点

SQS在自动驾驶基准测试中取得了显著的性能提升。在占据预测任务上，SQS的mIoU指标提升了1.3%，在3D目标检测任务上，NDS指标提升了1.0%。这些结果表明，SQS能够有效地提升稀疏感知模型的性能，使其在复杂自动驾驶场景中具有更强的感知能力。SQS明显优于先前的最先进的预训练方法。

## 🎯 应用场景

SQS技术可广泛应用于自动驾驶领域的3D感知任务，例如目标检测、语义分割、占据预测等。通过提升稀疏感知模型的性能，可以提高自动驾驶系统的安全性和可靠性，使其能够更好地理解周围环境，并做出更合理的决策。此外，该技术还可以应用于机器人导航、虚拟现实等领域。

## 📄 摘要（原文）

> Sparse Perception Models (SPMs) adopt a query-driven paradigm that forgoes explicit dense BEV or volumetric construction, enabling highly efficient computation and accelerated inference. In this paper, we introduce SQS, a novel query-based splatting pre-training specifically designed to advance SPMs in autonomous driving. SQS introduces a plug-in module that predicts 3D Gaussian representations from sparse queries during pre-training, leveraging self-supervised splatting to learn fine-grained contextual features through the reconstruction of multi-view images and depth maps. During fine-tuning, the pre-trained Gaussian queries are seamlessly integrated into downstream networks via query interaction mechanisms that explicitly connect pre-trained queries with task-specific queries, effectively accommodating the diverse requirements of occupancy prediction and 3D object detection. Extensive experiments on autonomous driving benchmarks demonstrate that SQS delivers considerable performance gains across multiple query-based 3D perception tasks, notably in occupancy prediction and 3D object detection, outperforming prior state-of-the-art pre-training approaches by a significant margin (i.e., +1.3 mIoU on occupancy prediction and +1.0 NDS on 3D detection).

