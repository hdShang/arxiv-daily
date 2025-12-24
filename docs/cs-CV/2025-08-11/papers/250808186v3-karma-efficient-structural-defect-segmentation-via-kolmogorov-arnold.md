---
layout: default
title: "KARMA: Efficient Structural Defect Segmentation via Kolmogorov-Arnold Representation Learning"
---

# KARMA: Efficient Structural Defect Segmentation via Kolmogorov-Arnold Representation Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08186" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08186v3</a>
  <a href="https://arxiv.org/pdf/2508.08186.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08186v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08186v3', 'KARMA: Efficient Structural Defect Segmentation via Kolmogorov-Arnold Representation Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Md Meftahul Ferdaus, Mahdi Abdelguerfi, Elias Ioup, Steven Sloan, Kendall N. Niles, Ken Pathak

**分类**: cs.CV

**发布日期**: 2025-08-11 (更新: 2025-11-06)

**备注**: This work has been submitted to the IEEE for possible publication

**🔗 代码/项目**: [GITHUB](https://github.com/faeyelab/karma)

---

## 💡 一句话要点

**提出KARMA以解决基础设施结构缺陷语义分割问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `语义分割` `结构缺陷` `深度学习` `实时检测` `基础设施监测` `Kolmogorov-Arnold` `低秩分解` `不平衡类别`

## 📋 核心要点

1. 现有深度学习方法在基础设施结构缺陷的语义分割中面临缺陷外观多样性、成像条件恶劣和类别不平衡等挑战。
2. KARMA通过一维函数组合建模复杂缺陷模式，采用低秩分解和优化特征金字塔结构，显著提高了参数效率。
3. 实验结果显示，KARMA在多个基准数据集上实现了优于现有方法的性能，同时参数量大幅减少，适合实时应用。

## 📝 摘要（中文）

基础设施结构缺陷的语义分割因缺陷外观多样、成像条件恶劣及类别不平衡而面临挑战。现有深度学习方法虽然有效，但通常需要数百万参数，难以应用于实时检测系统。本文提出KARMA（Kolmogorov-Arnold Representation Mapping Architecture），一种高效的语义分割框架，通过一维函数组合建模复杂缺陷模式，而非传统卷积。KARMA的三项技术创新包括：1）利用低秩分解的Tiny Kolmogorov-Arnold Network（TiKAN）模块进行特征变换；2）采用可分离卷积的优化特征金字塔结构进行多尺度缺陷分析；3）静态-动态原型机制增强不平衡类别的特征表示。大量实验表明，KARMA在基准基础设施检测数据集上实现了与最先进方法相当或更优的平均IoU性能，同时参数量显著减少（0.959M对比31.04M，减少97%）。KARMA以0.264 GFLOPS的计算量运行，保持适合实时部署的推理速度，能够实现实用的自动化基础设施检测系统而不影响准确性。

## 🔬 方法详解

**问题定义**：本文旨在解决基础设施结构缺陷的语义分割问题，现有方法由于参数量庞大和对不平衡类别的处理不足，难以应用于实时检测场景。

**核心思路**：KARMA通过引入Kolmogorov-Arnold表示学习，采用一维函数组合来建模复杂的缺陷模式，从而提高了模型的参数效率和推理速度。

**技术框架**：KARMA的整体架构包括三个主要模块：Tiny Kolmogorov-Arnold Network（TiKAN）模块用于特征变换，优化的特征金字塔结构用于多尺度分析，以及静态-动态原型机制用于增强特征表示。

**关键创新**：KARMA的核心创新在于其低秩分解的TiKAN模块和静态-动态原型机制，这些设计使得模型在参数效率和处理不平衡类别方面优于传统卷积神经网络。

**关键设计**：KARMA的参数设置经过精心设计，使用了可分离卷积和特征金字塔结构，损失函数则针对不平衡类别进行了优化，确保了模型在不同场景下的鲁棒性和准确性。

## 📊 实验亮点

KARMA在基准基础设施检测数据集上实现了显著的性能提升，平均IoU表现与最先进方法相当，同时参数量从31.04M减少至0.959M，减少幅度达97%。其推理速度为0.264 GFLOPS，适合实时部署，展示了优越的实用性。

## 🎯 应用场景

KARMA的研究成果在基础设施检测、城市安全监控及灾后评估等领域具有广泛的应用潜力。其高效的语义分割能力能够支持实时监测和自动化检测系统，提升基础设施维护的效率和安全性，具有重要的实际价值和社会影响。

## 📄 摘要（原文）

> Semantic segmentation of structural defects in civil infrastructure remains challenging due to variable defect appearances, harsh imaging conditions, and significant class imbalance. Current deep learning methods, despite their effectiveness, typically require millions of parameters, rendering them impractical for real-time inspection systems. We introduce KARMA (Kolmogorov-Arnold Representation Mapping Architecture), a highly efficient semantic segmentation framework that models complex defect patterns through compositions of one-dimensional functions rather than conventional convolutions. KARMA features three technical innovations: (1) a parameter-efficient Tiny Kolmogorov-Arnold Network (TiKAN) module leveraging low-rank factorization for KAN-based feature transformation; (2) an optimized feature pyramid structure with separable convolutions for multi-scale defect analysis; and (3) a static-dynamic prototype mechanism that enhances feature representation for imbalanced classes. Extensive experiments on benchmark infrastructure inspection datasets demonstrate that KARMA achieves competitive or superior mean IoU performance compared to state-of-the-art approaches, while using significantly fewer parameters (0.959M vs. 31.04M, a 97% reduction). Operating at 0.264 GFLOPS, KARMA maintains inference speeds suitable for real-time deployment, enabling practical automated infrastructure inspection systems without compromising accuracy. The source code can be accessed at the following URL: https://github.com/faeyelab/karma.

