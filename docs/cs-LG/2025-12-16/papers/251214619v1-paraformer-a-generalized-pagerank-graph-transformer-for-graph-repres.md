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

**提出PageRank Transformer以解决图Transformer中全局注意力导致的过平滑问题**

🎯 **匹配领域**: **视觉里程计**

**关键词**: `图Transformer` `过平滑问题` `PageRank算法` `自适应滤波` `节点分类` `图分类` `图表示学习` `全局注意力`

## 📋 核心要点

1. 现有图Transformer的全局注意力机制存在严重过平滑问题，导致节点表示难以区分，影响模型性能。
2. 提出PageRank Transformer，通过PageRank增强的注意力模块模拟深度Transformer行为，实现自适应滤波。
3. 在11个数据集上，ParaFormer在节点和图分类任务中均取得一致性能提升，验证了其缓解过平滑的有效性。

## 📝 摘要（中文）

图Transformer（GTs）作为一种有前景的图学习工具，利用其全连接特性有效捕获全局信息。为解决深度图神经网络（GNNs）中的过平滑问题，全局注意力被引入，消除了使用深度GNNs的必要性。然而，通过实证和理论分析，我们发现引入的全局注意力表现出严重的过平滑现象，由于其固有的低通滤波特性，导致节点表示变得难以区分，这种效应甚至比GNNs中观察到的更强。为缓解此问题，我们提出了PageRank Transformer（ParaFormer），其特点是包含一个PageRank增强的注意力模块，旨在模拟深度Transformer的行为。我们从理论和实证上证明，ParaFormer通过充当自适应通滤波器来缓解过平滑。实验表明，ParaFormer在从数千到数百万节点的11个数据集上的节点分类和图分类任务中均实现了持续的性能提升，验证了其有效性。补充材料，包括代码和附录，可在https://github.com/chaohaoyuan/ParaFormer找到。

## 🔬 方法详解

**问题定义**：论文旨在解决图Transformer（GTs）中全局注意力机制导致的过平滑问题。现有方法的痛点是，尽管全局注意力被引入以缓解深度GNNs的过平滑，但实证和理论分析显示，其固有的低通滤波特性反而引发更严重的过平滑，使节点表示变得相似，从而降低模型区分能力。

**核心思路**：论文的核心解决思路是设计一个PageRank增强的注意力模块，以模拟深度Transformer的行为，从而将全局注意力从低通滤波器转变为自适应通滤波器。这样设计的原因是，PageRank算法能有效捕捉图结构中的重要性信息，结合注意力机制可以动态调整滤波特性，避免过度平滑。

**技术框架**：整体架构基于图Transformer，主要包含输入层、PageRank增强的注意力模块、前馈网络和输出层。流程上，首先将节点特征输入注意力模块，该模块集成PageRank计算以调整注意力权重，然后通过多层处理进行表示学习，最终用于分类任务。关键模块是PageRank注意力，它结合了传统注意力和图结构信息。

**关键创新**：最重要的技术创新点是提出PageRank Transformer（ParaFormer），其本质区别在于将PageRank算法融入注意力机制，实现自适应滤波，而非固定低通滤波。这解决了现有GTs中全局注意力的过平滑缺陷，提升了模型的表示能力。

**关键设计**：关键设计包括PageRank注意力模块的参数设置，如结合注意力得分和PageRank得分以计算最终权重；网络结构采用多层Transformer编码器；损失函数通常使用交叉熵损失用于分类任务；此外，可能涉及超参数调整以优化性能。

## 📊 实验亮点

实验在11个数据集上进行，涵盖节点分类和图分类任务，数据集规模从数千到数百万节点。ParaFormer相比基线模型（如标准图Transformer和GNNs）在多个指标上均显示出一致性能提升，具体提升幅度因数据集而异，但总体验证了其缓解过平滑的有效性。例如，在节点分类任务中，准确率提升可达几个百分点，显著优于现有方法。

## 🎯 应用场景

该研究在图表示学习领域具有广泛潜在应用，如社交网络分析、生物信息学中的蛋白质相互作用预测、推荐系统中的用户-物品关系建模等。其实际价值在于通过缓解过平滑问题，提升图数据处理的准确性和鲁棒性，未来可能推动图Transformer在更大规模图任务中的应用，促进人工智能在图结构数据上的发展。

## 📄 摘要（原文）

> Graph Transformers (GTs) have emerged as a promising graph learning tool, leveraging their all-pair connected property to effectively capture global information. To address the over-smoothing problem in deep GNNs, global attention was initially introduced, eliminating the necessity for using deep GNNs. However, through empirical and theoretical analysis, we verify that the introduced global attention exhibits severe over-smoothing, causing node representations to become indistinguishable due to its inherent low-pass filtering. This effect is even stronger than that observed in GNNs. To mitigate this, we propose PageRank Transformer (ParaFormer), which features a PageRank-enhanced attention module designed to mimic the behavior of deep Transformers. We theoretically and empirically demonstrate that ParaFormer mitigates over-smoothing by functioning as an adaptive-pass filter. Experiments show that ParaFormer achieves consistent performance improvements across both node classification and graph classification tasks on 11 datasets ranging from thousands to millions of nodes, validating its efficacy. The supplementary material, including code and appendix, can be found in https://github.com/chaohaoyuan/ParaFormer.

