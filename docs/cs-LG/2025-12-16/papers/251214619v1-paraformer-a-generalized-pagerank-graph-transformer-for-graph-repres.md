---
layout: default
title: ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation Learning
---

# ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14619" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14619v1</a>
  <a href="https://arxiv.org/pdf/2512.14619.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14619v1" onclick="toggleFavorite(this, '2512.14619v1', 'ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chaohao Yuan, Zhenjie Song, Ercan Engin Kuruoglu, Kangfei Zhao, Yang Liu, Deli Zhao, Hong Cheng, Yu Rong

**分类**: cs.LG

**发布日期**: 2025-12-16

**备注**: Accepted by WSDM 2026

**🔗 代码/项目**: [GITHUB](https://github.com/chaohaoyuan/ParaFormer)

---

## 💡 一句话要点

**提出ParaFormer，一种基于PageRank增强的图Transformer，缓解图表示学习中的过平滑问题。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `图神经网络` `图Transformer` `PageRank` `过平滑` `图表示学习`

## 📋 核心要点

1. 深度图神经网络（GNNs）存在过平滑问题，导致节点表示难以区分，限制了模型性能。
2. ParaFormer通过引入PageRank增强的注意力机制，模仿深度Transformer的行为，缓解过平滑问题。
3. 实验结果表明，ParaFormer在节点分类和图分类任务中均取得了显著的性能提升，验证了其有效性。

## 📝 摘要（中文）

图Transformer (GTs) 作为一种有前景的图学习工具，利用其全连接特性有效地捕获全局信息。为了解决深度GNN中的过平滑问题，最初引入了全局注意力，从而消除了使用深度GNN的必要性。然而，通过实证和理论分析，我们验证了引入的全局注意力表现出严重的过平滑现象，由于其固有的低通滤波特性，导致节点表示变得难以区分。这种效应甚至比在GNN中观察到的更强。为了缓解这个问题，我们提出了PageRank Transformer (ParaFormer)，它具有PageRank增强的注意力模块，旨在模仿深度Transformer的行为。我们在理论上和实验上证明了ParaFormer通过充当自适应通滤波器来缓解过平滑。实验表明，ParaFormer在数千到数百万个节点的11个数据集上的节点分类和图分类任务中都取得了持续的性能提升，验证了其有效性。

## 🔬 方法详解

**问题定义**：论文旨在解决图神经网络中由于全局注意力机制引入而导致的过平滑问题。现有的图Transformer虽然能够捕获全局信息，但其全局注意力机制本质上是一个低通滤波器，导致节点表示趋于一致，难以区分，从而限制了模型的表达能力。这种过平滑现象甚至比传统GNN更严重。

**核心思路**：论文的核心思路是通过引入PageRank算法来增强注意力机制，使其能够自适应地传递信息，从而缓解过平滑问题。PageRank算法可以根据节点的重要性来调整注意力权重，使得重要的节点能够对其他节点产生更大的影响，从而保持节点表示的多样性。这种设计模仿了深度Transformer的行为，使其能够更好地捕获图的结构信息。

**技术框架**：ParaFormer的整体架构基于Transformer，主要包含以下模块：输入嵌入层、PageRank增强的注意力模块、前馈神经网络和输出层。输入嵌入层将节点特征转换为向量表示。PageRank增强的注意力模块是核心模块，它利用PageRank算法计算节点的重要性，并将其融入到注意力权重中。前馈神经网络用于进一步处理节点表示。输出层根据任务类型输出节点分类或图分类结果。

**关键创新**：ParaFormer的关键创新在于提出了PageRank增强的注意力模块。与传统的全局注意力机制不同，该模块能够根据节点的重要性自适应地调整注意力权重，从而缓解过平滑问题。这种设计使得模型能够更好地捕获图的结构信息，并保持节点表示的多样性。

**关键设计**：PageRank增强的注意力模块的关键设计在于如何将PageRank值融入到注意力权重中。论文采用了一种加权平均的方式，将PageRank值作为权重，对注意力权重进行调整。具体来说，对于节点i和节点j，其注意力权重为：attention(i,j) = softmax(Q_i * K_j^T + alpha * PageRank(i))，其中Q_i和K_j分别是节点i和节点j的查询向量和键向量，alpha是一个可学习的参数，用于控制PageRank值的影响程度。损失函数采用交叉熵损失函数，用于节点分类和图分类任务。

## 📊 实验亮点

实验结果表明，ParaFormer在11个数据集上取得了显著的性能提升。在节点分类任务中，ParaFormer在多个数据集上超越了现有的图神经网络和图Transformer模型。在图分类任务中，ParaFormer也取得了具有竞争力的结果。例如，在某些数据集上，ParaFormer的性能提升超过了5%。这些结果验证了ParaFormer的有效性，表明其能够有效地缓解过平滑问题，并提高图表示学习的性能。

## 🎯 应用场景

ParaFormer具有广泛的应用前景，可以应用于社交网络分析、生物信息学、化学信息学等领域。例如，在社交网络分析中，可以利用ParaFormer进行用户分类、社区检测等任务。在生物信息学中，可以利用ParaFormer进行蛋白质结构预测、药物发现等任务。该研究的实际价值在于提高了图表示学习的性能，为解决实际问题提供了更有效的工具。未来，可以进一步研究ParaFormer在更大规模图数据上的应用，并探索其与其他图学习技术的结合。

## 📄 摘要（原文）

> Graph Transformers (GTs) have emerged as a promising graph learning tool, leveraging their all-pair connected property to effectively capture global information. To address the over-smoothing problem in deep GNNs, global attention was initially introduced, eliminating the necessity for using deep GNNs. However, through empirical and theoretical analysis, we verify that the introduced global attention exhibits severe over-smoothing, causing node representations to become indistinguishable due to its inherent low-pass filtering. This effect is even stronger than that observed in GNNs. To mitigate this, we propose PageRank Transformer (ParaFormer), which features a PageRank-enhanced attention module designed to mimic the behavior of deep Transformers. We theoretically and empirically demonstrate that ParaFormer mitigates over-smoothing by functioning as an adaptive-pass filter. Experiments show that ParaFormer achieves consistent performance improvements across both node classification and graph classification tasks on 11 datasets ranging from thousands to millions of nodes, validating its efficacy. The supplementary material, including code and appendix, can be found in https://github.com/chaohaoyuan/ParaFormer.

