---
layout: default
title: PoseGAM: Robust Unseen Object Pose Estimation via Geometry-Aware Multi-View Reasoning
---

# PoseGAM: Robust Unseen Object Pose Estimation via Geometry-Aware Multi-View Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.10840" class="toolbar-btn" target="_blank">📄 arXiv: 2512.10840v1</a>
  <a href="https://arxiv.org/pdf/2512.10840.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.10840v1" onclick="toggleFavorite(this, '2512.10840v1', 'PoseGAM: Robust Unseen Object Pose Estimation via Geometry-Aware Multi-View Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jianqi Chen, Biao Zhang, Xiangjun Tang, Peter Wonka

**分类**: cs.CV

**发布日期**: 2025-12-11

**备注**: Project page: https://windvchen.github.io/PoseGAM/

**🔗 代码/项目**: [PROJECT_PAGE](https://windvchen.github.io/PoseGAM/)

---

## 💡 一句话要点

**PoseGAM：基于几何感知多视角推理的鲁棒未知物体姿态估计**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `6D姿态估计` `未知物体` `多视角推理` `几何感知` `点云` `深度学习` `机器人视觉`

## 📋 核心要点

1. 现有方法依赖于查询图像与物体模型或模板图像之间的显式特征对应，这在未知物体姿态估计中面临挑战。
2. PoseGAM通过几何感知多视角推理，直接从查询图像和模板图像预测物体姿态，避免了显式匹配。
3. 实验结果表明，PoseGAM在多个基准测试中取得了SOTA性能，平均AR提升5.1%，最高提升达17.6%。

## 📝 摘要（中文）

本文提出PoseGAM，一种几何感知的多视角框架，用于直接从查询图像和多个模板图像预测物体姿态，无需显式特征匹配，从而解决未知物体的6D姿态估计难题。该方法基于多视角基础模型架构，通过显式的基于点的几何信息和几何表示网络学习的特征来整合物体几何信息。此外，构建了一个包含超过19万个对象的大规模合成数据集，以增强鲁棒性和泛化能力。在多个基准测试上的大量评估表明，PoseGAM达到了最先进的性能，平均AR指标比现有方法提高了5.1%，在单个数据集上实现了高达17.6%的增益，表明其对未知物体具有很强的泛化能力。

## 🔬 方法详解

**问题定义**：论文旨在解决未知物体的6D姿态估计问题。现有方法通常依赖于在查询图像和物体模型或模板图像之间建立显式的特征对应关系，这种方法在处理未知物体时表现不佳，因为缺乏预先存在的模型或模板。因此，如何有效地利用几何信息，实现对未知物体的鲁棒姿态估计是一个关键挑战。

**核心思路**：PoseGAM的核心思路是利用多视角信息和几何感知能力，直接从查询图像和多个模板图像预测物体姿态，而无需显式地建立特征对应关系。通过整合显式的点云几何信息和从几何表示网络学习到的几何特征，模型能够更好地理解物体的三维结构，从而实现更准确的姿态估计。

**技术框架**：PoseGAM的整体框架基于多视角基础模型架构。它包含以下主要模块：1) 特征提取模块，用于从查询图像和模板图像中提取视觉特征；2) 几何表示模块，用于编码物体的几何信息，包括显式的点云表示和学习到的几何特征；3) 多视角推理模块，用于整合来自不同视角的特征和几何信息，预测物体的姿态。

**关键创新**：PoseGAM的关键创新在于其几何感知的多视角推理方法。它通过显式的点云几何信息和从几何表示网络学习到的几何特征，有效地整合了物体的几何信息，从而提高了姿态估计的准确性和鲁棒性。此外，该方法避免了显式的特征匹配，使其能够更好地处理未知物体。

**关键设计**：PoseGAM的关键设计包括：1) 使用点云作为显式的几何表示，直接编码物体的三维结构；2) 设计几何表示网络，学习物体的几何特征，补充点云表示的不足；3) 使用多视角注意力机制，整合来自不同视角的特征和几何信息；4) 构建大规模合成数据集，用于训练和评估模型的泛化能力。

## 📊 实验亮点

PoseGAM在多个基准测试中取得了显著的性能提升。例如，在平均AR指标上，PoseGAM比现有方法提高了5.1%，在单个数据集上实现了高达17.6%的增益。这些结果表明，PoseGAM对未知物体具有很强的泛化能力，并且能够有效地利用几何信息进行姿态估计。

## 🎯 应用场景

PoseGAM在机器人抓取、增强现实、自动驾驶等领域具有广泛的应用前景。它可以帮助机器人更好地理解和操作未知物体，提高增强现实应用的真实感，并为自动驾驶系统提供更准确的环境感知能力。该研究的未来影响在于推动计算机视觉技术在实际场景中的应用，并促进相关领域的发展。

## 📄 摘要（原文）

> 6D object pose estimation, which predicts the transformation of an object relative to the camera, remains challenging for unseen objects. Existing approaches typically rely on explicitly constructing feature correspondences between the query image and either the object model or template images. In this work, we propose PoseGAM, a geometry-aware multi-view framework that directly predicts object pose from a query image and multiple template images, eliminating the need for explicit matching. Built upon recent multi-view-based foundation model architectures, the method integrates object geometry information through two complementary mechanisms: explicit point-based geometry and learned features from geometry representation networks. In addition, we construct a large-scale synthetic dataset containing more than 190k objects under diverse environmental conditions to enhance robustness and generalization. Extensive evaluations across multiple benchmarks demonstrate our state-of-the-art performance, yielding an average AR improvement of 5.1% over prior methods and achieving up to 17.6% gains on individual datasets, indicating strong generalization to unseen objects. Project page: https://windvchen.github.io/PoseGAM/ .

