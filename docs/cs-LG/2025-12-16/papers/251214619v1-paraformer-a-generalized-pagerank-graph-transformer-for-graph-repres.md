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

**提出PageRank Transformer以解决图Transformer中的过度平滑问题**

🎯 **匹配领域**: **视觉里程计**

**关键词**: `图Transformer` `过度平滑` `PageRank` `自适应滤波` `图表示学习` `节点分类` `图分类` `全局注意力`

## 📋 核心要点

1. 现有图Transformer的全局注意力机制存在严重过度平滑问题，导致节点表示难以区分，影响模型性能。
2. 提出PageRank Transformer，通过PageRank增强的注意力模块模拟深度Transformer行为，实现自适应滤波以缓解过度平滑。
3. 在11个数据集上的实验显示，ParaFormer在节点和图分类任务中均取得一致性能提升，验证其有效性。

## 📝 摘要（中文）

图Transformer（GTs）作为一种有前景的图学习工具，利用其全连接特性有效捕获全局信息。为解决深度图神经网络（GNNs）中的过度平滑问题，全局注意力机制被引入，消除了使用深度GNNs的必要性。然而，通过实证和理论分析，我们发现引入的全局注意力表现出严重的过度平滑，由于其固有的低通滤波特性，导致节点表示变得难以区分，这种效应甚至比GNNs中观察到的更强。为缓解此问题，我们提出了PageRank Transformer（ParaFormer），其特点是包含一个PageRank增强的注意力模块，旨在模拟深度Transformer的行为。我们从理论和实证上证明，ParaFormer通过充当自适应通滤波器来减轻过度平滑。实验表明，ParaFormer在从数千到数百万节点的11个数据集上的节点分类和图分类任务中均实现了持续的性能提升，验证了其有效性。补充材料，包括代码和附录，可在https://github.com/chaohaoyuan/ParaFormer找到。

## 🔬 方法详解

ParaFormer的整体框架基于图Transformer，核心创新在于引入PageRank增强的注意力模块。该模块通过整合PageRank算法来调整注意力权重，使其能够自适应地过滤信息，从而模拟深度Transformer的层次化特征提取过程。与现有方法的主要区别在于，传统图Transformer的全局注意力是低通滤波器，导致过度平滑；而ParaFormer通过PageRank机制实现自适应通滤波，有效平衡局部和全局信息，减少表示退化。

## 📊 实验亮点

ParaFormer在11个数据集上均表现出色，包括节点分类和图分类任务，性能提升一致，特别是在大规模图数据上验证了其缓解过度平滑的有效性，证明了自适应滤波策略的优越性。

## 🎯 应用场景

该研究可应用于社交网络分析、生物信息学、推荐系统等需要处理大规模图数据的领域，通过提升图表示学习的准确性和鲁棒性，支持节点分类、图分类等任务，具有广泛的实际价值。

## 📄 摘要（原文）

> Graph Transformers (GTs) have emerged as a promising graph learning tool, leveraging their all-pair connected property to effectively capture global information. To address the over-smoothing problem in deep GNNs, global attention was initially introduced, eliminating the necessity for using deep GNNs. However, through empirical and theoretical analysis, we verify that the introduced global attention exhibits severe over-smoothing, causing node representations to become indistinguishable due to its inherent low-pass filtering. This effect is even stronger than that observed in GNNs. To mitigate this, we propose PageRank Transformer (ParaFormer), which features a PageRank-enhanced attention module designed to mimic the behavior of deep Transformers. We theoretically and empirically demonstrate that ParaFormer mitigates over-smoothing by functioning as an adaptive-pass filter. Experiments show that ParaFormer achieves consistent performance improvements across both node classification and graph classification tasks on 11 datasets ranging from thousands to millions of nodes, validating its efficacy. The supplementary material, including code and appendix, can be found in https://github.com/chaohaoyuan/ParaFormer.

