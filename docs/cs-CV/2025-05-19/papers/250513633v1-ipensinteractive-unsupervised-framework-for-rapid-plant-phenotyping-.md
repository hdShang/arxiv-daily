---
layout: default
title: "IPENS:Interactive Unsupervised Framework for Rapid Plant Phenotyping Extraction via NeRF-SAM2 Fusion"
---

# IPENS:Interactive Unsupervised Framework for Rapid Plant Phenotyping Extraction via NeRF-SAM2 Fusion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13633" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13633v1</a>
  <a href="https://arxiv.org/pdf/2505.13633.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13633v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13633v1', 'IPENS:Interactive Unsupervised Framework for Rapid Plant Phenotyping Extraction via NeRF-SAM2 Fusion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wentao Song, He Huang, Youqiang Sun, Fang Qu, Jiaqi Zhang, Longhui Fang, Yuwei Hao, Chenyang Peng

**分类**: cs.CV

**发布日期**: 2025-05-19

---

## 💡 一句话要点

**提出IPENS以解决植物表型提取中的无监督多目标分割问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `植物表型` `无监督学习` `多目标分割` `点云提取` `智能育种` `计算机视觉` `深度学习`

## 📋 核心要点

1. 现有植物表型提取方法依赖于大量手动标注数据，面对自遮挡物体时效果不佳，限制了其应用。
2. IPENS通过结合SAM2分割的2D掩膜和辐射场信息，实现了无监督的多目标点云提取，解决了多目标分割挑战。
3. 在水稻和小麦数据集上，IPENS分别实现了63.72%和89.68%的分割准确率，展现出优越的表型估计性能。

## 📝 摘要（中文）

先进的植物表型技术在特征改良和智能育种中至关重要。现有方法依赖于大量高精度的手动标注数据，面对自遮挡的谷物级物体时，无监督方法往往效果不佳。本研究提出IPENS，一种交互式无监督多目标点云提取方法，利用SAM2（Segment Anything Model 2）分割的2D掩膜提升至3D空间进行目标点云提取。实验结果表明，IPENS在水稻数据集上实现了63.72%的谷物级分割准确率（mIoU），并展现出强大的表型估计能力。该方法无需标注数据，通过简单的单轮交互在3分钟内快速提取多个目标的谷物级点云，具有显著的智能育种效率提升潜力。

## 🔬 方法详解

**问题定义**：本研究旨在解决植物表型提取中的无监督多目标分割问题。现有方法在处理自遮挡的谷物级物体时，往往依赖于大量手动标注数据，导致效率低下和适用性差。

**核心思路**：IPENS的核心思路是利用SAM2分割的2D掩膜和辐射场信息，将其提升至3D空间进行点云提取。通过设计多目标协同优化策略，解决了单次交互下的多目标分割挑战。

**技术框架**：IPENS的整体架构包括数据输入、2D掩膜生成、3D点云提升和多目标协同优化四个主要模块。首先，通过SAM2生成2D掩膜，然后利用辐射场信息将其提升至3D，最后进行多目标优化以实现精确分割。

**关键创新**：IPENS的主要创新在于结合了无监督学习与交互式分割，能够在无需标注数据的情况下，实现快速且高效的多目标点云提取。这一方法在处理自遮挡物体时表现出色，显著提升了分割准确率。

**关键设计**：在设计中，IPENS采用了特定的损失函数以优化多目标分割效果，并通过调节网络结构参数来提升模型的适应性和准确性。

## 📊 实验亮点

实验结果显示，IPENS在水稻数据集上实现了63.72%的分割准确率（mIoU），在小麦数据集上进一步提升至89.68%。此外，表型估计性能也非常出色，水稻的谷物体积预测R2达到0.7697，小麦的穗体积预测R2更是高达0.9956，显示出显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括农业科学、植物育种和生态监测等。IPENS提供了一种非侵入式的高质量表型提取解决方案，能够加速植物育种过程，提高作物改良的效率和精度，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Advanced plant phenotyping technologies play a crucial role in targeted trait improvement and accelerating intelligent breeding. Due to the species diversity of plants, existing methods heavily rely on large-scale high-precision manually annotated data. For self-occluded objects at the grain level, unsupervised methods often prove ineffective. This study proposes IPENS, an interactive unsupervised multi-target point cloud extraction method. The method utilizes radiance field information to lift 2D masks, which are segmented by SAM2 (Segment Anything Model 2), into 3D space for target point cloud extraction. A multi-target collaborative optimization strategy is designed to effectively resolve the single-interaction multi-target segmentation challenge. Experimental validation demonstrates that IPENS achieves a grain-level segmentation accuracy (mIoU) of 63.72% on a rice dataset, with strong phenotypic estimation capabilities: grain volume prediction yields R2 = 0.7697 (RMSE = 0.0025), leaf surface area R2 = 0.84 (RMSE = 18.93), and leaf length and width predictions achieve R2 = 0.97 and 0.87 (RMSE = 1.49 and 0.21). On a wheat dataset,IPENS further improves segmentation accuracy to 89.68% (mIoU), with equally outstanding phenotypic estimation performance: spike volume prediction achieves R2 = 0.9956 (RMSE = 0.0055), leaf surface area R2 = 1.00 (RMSE = 0.67), and leaf length and width predictions reach R2 = 0.99 and 0.92 (RMSE = 0.23 and 0.15). This method provides a non-invasive, high-quality phenotyping extraction solution for rice and wheat. Without requiring annotated data, it rapidly extracts grain-level point clouds within 3 minutes through simple single-round interactions on images for multiple targets, demonstrating significant potential to accelerate intelligent breeding efficiency.

