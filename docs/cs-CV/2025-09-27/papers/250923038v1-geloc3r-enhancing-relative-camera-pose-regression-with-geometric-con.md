---
layout: default
title: "GeLoc3r: Enhancing Relative Camera Pose Regression with Geometric Consistency Regularization"
---

# GeLoc3r: Enhancing Relative Camera Pose Regression with Geometric Consistency Regularization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23038" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23038v1</a>
  <a href="https://arxiv.org/pdf/2509.23038.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23038v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23038v1', 'GeLoc3r: Enhancing Relative Camera Pose Regression with Geometric Consistency Regularization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jingxing Li, Yongjae Lee, Deliang Fan

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-27

---

## 💡 一句话要点

**GeLoc3r：通过几何一致性正则化增强相对相机位姿回归**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `相对相机位姿估计` `几何一致性正则化` `深度学习` `位姿回归` `三维重建`

## 📋 核心要点

1. 现有ReLoc3R方法虽然速度快精度高，但内部表示存在几何不一致性，限制了其精度上限。
2. GeLoc3r通过几何一致性正则化（GCR）训练回归网络，使其在推理时无需几何计算即可产生几何一致的位姿。
3. 实验表明，GeLoc3r在多个数据集上显著优于ReLoc3R，在CO3Dv2上AUC@5°提升了16%。

## 📝 摘要（中文）

ReLoc3R在快速推理（25ms）和回归精度方面取得了突破性进展，但分析表明其内部表示存在细微的几何不一致性，阻碍了其达到基于对应关系的方法（如MASt3R，每个pair需要300ms）的精度上限。本文提出了GeLoc3r，一种新颖的相对相机位姿估计方法，通过几何一致性正则化（GCR）增强位姿回归方法。GeLoc3r通过训练回归网络以产生几何一致的位姿，而无需推理时的几何计算，从而克服了速度-精度困境。在训练期间，GeLoc3r利用ground-truth深度生成密集的3D-2D对应关系，使用FusionTransformer对它们进行加权，学习对应关系的重要性，并通过加权RANSAC计算几何一致的位姿。这创建了一个一致性损失，将几何知识转移到回归网络中。与需要在推理时进行回归和几何求解的FAR方法不同，GeLoc3r仅在测试时使用增强的回归头，保持了ReLoc3R的快速速度，并接近了MASt3R的高精度。在具有挑战性的基准测试中，GeLoc3r始终优于ReLoc3R，取得了显著的改进，包括在CO3Dv2数据集上AUC@5°从34.85%提高到40.45%（相对改进16%），在RealEstate10K上从66.70%提高到68.66%，在MegaDepth1500上从49.60%提高到50.45%。通过在训练期间教授几何一致性而不是在推理时强制执行，GeLoc3r代表了神经网络学习相机几何的新范式，实现了回归的速度和对应方法的几何理解。

## 🔬 方法详解

**问题定义**：论文旨在解决相对相机位姿估计问题。现有ReLoc3R方法虽然速度快，但由于内部几何不一致性，精度受限。基于对应关系的方法（如MASt3R）精度高，但计算成本高昂，推理速度慢。因此，如何在保证速度的同时提高相对相机位姿估计的精度是一个挑战。

**核心思路**：论文的核心思路是在训练阶段引入几何一致性正则化（GCR），将几何知识融入到回归网络中。通过学习ground-truth深度信息，生成3D-2D对应关系，并利用这些对应关系计算几何一致的位姿，从而指导回归网络的训练。这样，在推理阶段，只需使用训练好的回归网络即可获得高精度且几何一致的位姿估计，避免了耗时的几何计算。

**技术框架**：GeLoc3r的整体框架包括以下几个主要模块：1) 3D-2D对应关系生成模块：利用ground-truth深度信息生成密集的3D-2D对应关系。2) FusionTransformer模块：学习每个对应关系的重要性权重。3) 加权RANSAC模块：利用加权的3D-2D对应关系计算几何一致的位姿。4) 一致性损失计算模块：计算回归网络预测的位姿与几何一致位姿之间的损失，用于指导网络训练。在推理阶段，仅使用训练好的回归网络进行位姿估计。

**关键创新**：GeLoc3r的关键创新在于提出了几何一致性正则化（GCR）方法，将几何知识融入到回归网络的训练过程中。与传统的先回归后几何求解的方法（如FAR）不同，GeLoc3r在训练阶段学习几何一致性，而在推理阶段仅使用回归网络，从而实现了速度和精度的平衡。这种“训练时学习几何，推理时直接应用”的思路是与现有方法的本质区别。

**关键设计**：在3D-2D对应关系生成方面，使用了ground-truth深度信息，保证了对应关系的准确性。FusionTransformer的设计允许网络学习不同对应关系的重要性，从而更好地利用几何信息。一致性损失函数的设计至关重要，需要平衡回归损失和几何一致性损失之间的权重。RANSAC算法的参数设置（如迭代次数、内点阈值）也会影响最终的位姿估计精度。

## 📊 实验亮点

GeLoc3r在多个具有挑战性的数据集上取得了显著的性能提升。在CO3Dv2数据集上，GeLoc3r的AUC@5°达到了40.45%，相比ReLoc3R的34.85%有显著提升（相对提升16%）。在RealEstate10K和MegaDepth1500数据集上，GeLoc3r也分别取得了68.66%和50.45%的AUC@5°，均优于ReLoc3R。这些结果表明GeLoc3r能够有效地学习几何一致性，并提高相对相机位姿估计的精度。

## 🎯 应用场景

GeLoc3r在机器人导航、增强现实、三维重建等领域具有广泛的应用前景。高精度且快速的相对相机位姿估计对于构建精确的地图、实现鲁棒的定位以及增强用户体验至关重要。该研究成果有望推动这些领域的发展，并为相关应用提供更可靠的技术支持。

## 📄 摘要（原文）

> Prior ReLoc3R achieves breakthrough performance with fast 25ms inference and state-of-the-art regression accuracy, yet our analysis reveals subtle geometric inconsistencies in its internal representations that prevent reaching the precision ceiling of correspondence-based methods like MASt3R (which require 300ms per pair). In this work, we present GeLoc3r, a novel approach to relative camera pose estimation that enhances pose regression methods through Geometric Consistency Regularization (GCR). GeLoc3r overcomes the speed-accuracy dilemma by training regression networks to produce geometrically consistent poses without inference-time geometric computation. During training, GeLoc3r leverages ground-truth depth to generate dense 3D-2D correspondences, weights them using a FusionTransformer that learns correspondence importance, and computes geometrically-consistent poses via weighted RANSAC. This creates a consistency loss that transfers geometric knowledge into the regression network. Unlike FAR method which requires both regression and geometric solving at inference, GeLoc3r only uses the enhanced regression head at test time, maintaining ReLoc3R's fast speed and approaching MASt3R's high accuracy. On challenging benchmarks, GeLoc3r consistently outperforms ReLoc3R, achieving significant improvements including 40.45% vs. 34.85% AUC@5° on the CO3Dv2 dataset (16% relative improvement), 68.66% vs. 66.70% AUC@5° on RealEstate10K, and 50.45% vs. 49.60% on MegaDepth1500. By teaching geometric consistency during training rather than enforcing it at inference, GeLoc3r represents a paradigm shift in how neural networks learn camera geometry, achieving both the speed of regression and the geometric understanding of correspondence methods.

