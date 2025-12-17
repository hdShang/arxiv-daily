---
layout: default
title: Beyond MMD: Evaluating Graph Generative Models with Geometric Deep Learning
---

# Beyond MMD: Evaluating Graph Generative Models with Geometric Deep Learning

**arXiv**: [2512.14241v1](https://arxiv.org/abs/2512.14241) | [PDF](https://arxiv.org/pdf/2512.14241.pdf)

**作者**: Salvatore Romano, Marco Grassia, Giuseppe Mangioni

**分类**: cs.LG, cs.AI, physics.soc-ph

**发布日期**: 2025-12-16

**备注**: 16 pages, 4 figures

---

## 💡 一句话要点

**提出RGM方法以解决图生成模型评估中MMD的局限性，基于几何深度学习进行更准确评估。**

🎯 **匹配领域**: **强化学习**

**关键词**: `图生成模型评估` `几何深度学习` `最大均值差异` `图神经网络` `图分类任务` `表示学习` `拓扑性质分析` `合成图生成`

## 📋 核心要点

1. 核心问题：现有图生成模型评估过度依赖最大均值差异（MMD），无法准确捕捉图的结构特性差异，导致评估不全面。
2. 方法要点：提出RGM方法，基于几何深度学习模型训练自定义数据集，通过图分类任务评估生成图的表示质量，超越MMD的局限性。
3. 实验或效果：评估GRAN和EDGE模型，发现它们在生成图时能保留某些拓扑性质，但在结构特征保持上存在不足，验证了MMD的缺陷。

## 📝 摘要（中文）

图生成是网络科学和生物信息学等领域的核心任务，图生成模型（GGMs）利用深度学习技术学习真实世界图的分布并生成相似样本，如基于变分自编码器、循环神经网络和扩散模型的方法。然而，现有评估过程主要依赖最大均值差异（MMD）作为度量，存在局限性。本文提出一种名为RGM（表示感知图生成模型评估）的新方法，克服了MMD的不足。作为方法演示，我们全面评估了两种先进图生成模型：图循环注意力网络（GRAN）和高效度引导图生成模型（EDGE），通过几何深度学习模型在自定义合成与真实图数据集上进行分类任务分析。研究发现，尽管两种模型能生成具有特定拓扑性质的图，但在保持区分不同图域的结构特征方面存在显著限制，同时强调了MMD作为评估度量的不足，并为未来研究提出了替代方案。

## 🔬 方法详解

论文核心方法是RGM（表示感知图生成模型评估），整体框架包括：首先，构建一个包含合成和真实图的自定义数据集，专门用于图分类任务；其次，训练一个几何深度学习模型（如基于图神经网络的分类器）来学习图的表示；然后，使用该模型评估图生成模型（如GRAN和EDGE）生成的图，通过分类性能或表示相似性来量化生成图与真实图的差异。关键技术创新点在于将评估从传统的MMD度量转向基于几何深度学习的表示分析，这能更细致地捕捉图的结构和域特性。与现有方法的主要区别是，RGM不依赖单一统计度量，而是利用深度学习模型进行端到端评估，从而提供更全面和准确的性能分析。

## 📊 实验亮点

实验显示，GRAN和EDGE在生成图时能模拟某些拓扑属性（如度分布），但在保持图域特有结构特征（如社区结构或全局连通性）方面表现不佳；RGM方法通过几何深度学习模型揭示了这些局限性，并证明MMD作为评估度量不足以捕捉复杂图特性，为未来研究提供了更准确的评估基准。

## 🎯 应用场景

该研究可应用于网络科学、生物信息学、社交网络分析和药物发现等领域，通过改进图生成模型的评估，帮助生成更逼真的合成图，用于模拟、数据增强和算法测试，提升实际应用的可靠性和效率。

## 📄 摘要（原文）

> Graph generation is a crucial task in many fields, including network science and bioinformatics, as it enables the creation of synthetic graphs that mimic the properties of real-world networks for various applications. Graph Generative Models (GGMs) have emerged as a promising solution to this problem, leveraging deep learning techniques to learn the underlying distribution of real-world graphs and generate new samples that closely resemble them. Examples include approaches based on Variational Auto-Encoders, Recurrent Neural Networks, and more recently, diffusion-based models. However, the main limitation often lies in the evaluation process, which typically relies on Maximum Mean Discrepancy (MMD) as a metric to assess the distribution of graph properties in the generated ensemble. This paper introduces a novel methodology for evaluating GGMs that overcomes the limitations of MMD, which we call RGM (Representation-aware Graph-generation Model evaluation). As a practical demonstration of our methodology, we present a comprehensive evaluation of two state-of-the-art Graph Generative Models: Graph Recurrent Attention Networks (GRAN) and Efficient and Degree-guided graph GEnerative model (EDGE). We investigate their performance in generating realistic graphs and compare them using a Geometric Deep Learning model trained on a custom dataset of synthetic and real-world graphs, specifically designed for graph classification tasks. Our findings reveal that while both models can generate graphs with certain topological properties, they exhibit significant limitations in preserving the structural characteristics that distinguish different graph domains. We also highlight the inadequacy of Maximum Mean Discrepancy as an evaluation metric for GGMs and suggest alternative approaches for future research.

