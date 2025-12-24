---
layout: default
title: Hyperbolic Dataset Distillation
---

# Hyperbolic Dataset Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24623" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24623v2</a>
  <a href="https://arxiv.org/pdf/2505.24623.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24623v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24623v2', 'Hyperbolic Dataset Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenyuan Li, Guang Li, Keisuke Maeda, Takahiro Ogawa, Miki Haseyama

**分类**: cs.LG, cs.AI, cs.CV

**发布日期**: 2025-05-30 (更新: 2025-10-17)

**备注**: Accepted to NeurIPS 2025

**🔗 代码/项目**: [GITHUB](https://github.com/Guang000/HDD)

---

## 💡 一句话要点

**提出超曲面数据集蒸馏方法以解决大规模数据集挑战**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `数据集蒸馏` `超曲面空间` `深度学习` `模型压缩` `分布匹配`

## 📋 核心要点

1. 现有的数据集蒸馏方法在处理复杂数据分布时，往往忽视了数据之间的几何和层次关系，导致性能下降。
2. 本文提出的HDD方法利用超曲面空间的特性，通过优化合成数据与原始数据的质心之间的超曲面距离，增强了层次结构的建模能力。
3. 实验结果表明，HDD方法在保持模型性能的同时，仅需20%的蒸馏核心集即可实现显著的训练稳定性提升。

## 📝 摘要（中文）

为了解决深度学习中大规模数据集带来的计算和存储挑战，数据集蒸馏被提出以合成一个紧凑的数据集，替代原始数据集，同时保持相当的模型性能。与需要昂贵的双层优化的优化方法不同，分布匹配方法通过对齐合成数据和原始数据的分布来提高效率，从而消除了嵌套优化。现有的分布匹配方法局限于欧几里得空间，忽视了复杂的几何和层次关系。为此，本文提出了一种新颖的超曲面数据集蒸馏方法HDD，利用负曲率的超曲面空间自然建模层次和树状结构。HDD将特征嵌入到洛伦兹超曲面空间，通过优化合成数据和原始数据的质心之间的超曲面距离，显式地将层次结构整合到蒸馏过程中。

## 🔬 方法详解

**问题定义**：本文旨在解决现有数据集蒸馏方法在处理复杂数据分布时的不足，尤其是对数据之间几何和层次关系的忽视。现有方法多依赖于双层优化，计算成本高，效率低下。

**核心思路**：HDD方法通过引入超曲面空间，利用其负曲率特性来建模层次结构，优化合成数据与原始数据的质心之间的超曲面距离，从而在蒸馏过程中显式整合层次信息。

**技术框架**：HDD的整体架构包括特征提取模块、超曲面嵌入模块和距离优化模块。特征提取模块使用浅层网络提取数据特征，随后将这些特征嵌入到洛伦兹超曲面空间中，最后通过优化质心之间的超曲面距离来实现数据蒸馏。

**关键创新**：HDD是首个将超曲面空间引入数据集蒸馏过程的方法，显著区别于传统的欧几里得空间方法，能够更好地捕捉数据的层次结构和几何特性。

**关键设计**：在HDD中，损失函数设计为质心之间的超曲面距离，网络结构采用浅层网络以降低计算复杂度，同时在超曲面空间中进行数据剪枝，仅需20%的蒸馏核心集即可保持模型性能。

## 📊 实验亮点

实验结果显示，HDD方法在仅使用20%的蒸馏核心集的情况下，仍能保持模型性能，并显著提高训练的稳定性。这一结果相较于传统方法，展示了HDD在数据集蒸馏中的高效性和创新性。

## 🎯 应用场景

该研究的潜在应用领域包括计算机视觉、自然语言处理和其他需要处理大规模数据集的深度学习任务。通过有效的蒸馏方法，HDD可以帮助研究人员和工程师在资源受限的环境中训练高性能模型，提升模型的训练效率和稳定性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> To address the computational and storage challenges posed by large-scale datasets in deep learning, dataset distillation has been proposed to synthesize a compact dataset that replaces the original while maintaining comparable model performance. Unlike optimization-based approaches that require costly bi-level optimization, distribution matching (DM) methods improve efficiency by aligning the distributions of synthetic and original data, thereby eliminating nested optimization. DM achieves high computational efficiency and has emerged as a promising solution. However, existing DM methods, constrained to Euclidean space, treat data as independent and identically distributed points, overlooking complex geometric and hierarchical relationships. To overcome this limitation, we propose a novel hyperbolic dataset distillation method, termed HDD. Hyperbolic space, characterized by negative curvature and exponential volume growth with distance, naturally models hierarchical and tree-like structures. HDD embeds features extracted by a shallow network into the Lorentz hyperbolic space, where the discrepancy between synthetic and original data is measured by the hyperbolic (geodesic) distance between their centroids. By optimizing this distance, the hierarchical structure is explicitly integrated into the distillation process, guiding synthetic samples to gravitate towards the root-centric regions of the original data distribution while preserving their underlying geometric characteristics. Furthermore, we find that pruning in hyperbolic space requires only 20% of the distilled core set to retain model performance, while significantly improving training stability. To the best of our knowledge, this is the first work to incorporate the hyperbolic space into the dataset distillation process. The code is available at https://github.com/Guang000/HDD.

