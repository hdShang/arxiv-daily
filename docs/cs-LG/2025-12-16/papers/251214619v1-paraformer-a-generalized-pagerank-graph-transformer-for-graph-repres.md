---
layout: default
title: ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation Learning
---

# ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation Learning

**arXiv**: [2512.14619v1](https://arxiv.org/abs/2512.14619) | [PDF](https://arxiv.org/pdf/2512.14619.pdf)

**作者**: Chaohao Yuan, Zhenjie Song, Ercan Engin Kuruoglu, Kangfei Zhao, Yang Liu, Deli Zhao, Hong Cheng, Yu Rong

**分类**: cs.LG

**发布日期**: 2025-12-16

**备注**: Accepted by WSDM 2026

**🔗 代码/项目**: [GITHUB](https://github.com/chaohaoyuan/ParaFormer)

---

## 💡 一句话要点

**提出PageRank Transformer（ParaFormer）以解决图Transformer中全局注意力导致的过平滑问题，提升图表示学习性能。**

**关键词**: `图Transformer` `过平滑问题` `PageRank算法` `自适应滤波` `图表示学习` `节点分类` `图分类` `全局注意力`

## 📋 核心要点

1. 现有图Transformer的全局注意力机制存在严重过平滑问题，导致节点表示趋同，影响图学习性能。
2. 提出PageRank Transformer（ParaFormer），通过PageRank增强的注意力模块模拟深度Transformer，实现自适应滤波以缓解过平滑。
3. 在11个数据集上，ParaFormer在节点分类和图分类任务中均表现出性能提升，验证了其有效性和泛化能力。

## 📝 摘要（中文）

图Transformer（GTs）作为一种有前景的图学习工具，利用其全连接特性有效捕获全局信息。为应对深度图神经网络（GNNs）中的过平滑问题，全局注意力被引入，从而无需依赖深度GNNs。然而，通过实证和理论分析，我们发现全局注意力本身表现出严重的过平滑现象，由于其固有的低通滤波特性，导致节点表示变得难以区分，这种效应甚至比GNNs中观察到的更强。为缓解此问题，我们提出PageRank Transformer（ParaFormer），其核心是一个PageRank增强的注意力模块，旨在模拟深度Transformer的行为。我们从理论和实证上证明，ParaFormer通过充当自适应通滤波器来减轻过平滑。实验表明，ParaFormer在11个数据集（节点数从数千到数百万）的节点分类和图分类任务中均取得一致的性能提升，验证了其有效性。补充材料（包括代码和附录）可在https://github.com/chaohaoyuan/ParaFormer找到。

## 🔬 方法详解

ParaFormer的整体框架基于图Transformer，核心创新在于引入PageRank增强的注意力模块。该模块通过整合PageRank算法来调整注意力权重，使其能够自适应地过滤信息，从而模拟深度Transformer的行为，避免全局注意力固有的低通滤波效应。与现有方法的主要区别在于，传统图Transformer的全局注意力易导致过平滑，而ParaFormer通过PageRank机制实现自适应通滤波，有效平衡局部和全局信息，提升表示学习的区分度。

## 📊 实验亮点

ParaFormer在11个数据集（节点数从数千到数百万）上均取得性能提升，在节点分类和图分类任务中表现一致优于基线方法，验证了其缓解过平滑的有效性和泛化能力。

## 🎯 应用场景

该研究可应用于社交网络分析、推荐系统、生物信息学和知识图谱等领域，通过提升图表示学习的准确性和鲁棒性，支持节点分类、图分类等任务，具有广泛的工业和研究价值。

## 📄 摘要（原文）

> Graph Transformers (GTs) have emerged as a promising graph learning tool, leveraging their all-pair connected property to effectively capture global information. To address the over-smoothing problem in deep GNNs, global attention was initially introduced, eliminating the necessity for using deep GNNs. However, through empirical and theoretical analysis, we verify that the introduced global attention exhibits severe over-smoothing, causing node representations to become indistinguishable due to its inherent low-pass filtering. This effect is even stronger than that observed in GNNs. To mitigate this, we propose PageRank Transformer (ParaFormer), which features a PageRank-enhanced attention module designed to mimic the behavior of deep Transformers. We theoretically and empirically demonstrate that ParaFormer mitigates over-smoothing by functioning as an adaptive-pass filter. Experiments show that ParaFormer achieves consistent performance improvements across both node classification and graph classification tasks on 11 datasets ranging from thousands to millions of nodes, validating its efficacy. The supplementary material, including code and appendix, can be found in https://github.com/chaohaoyuan/ParaFormer.

