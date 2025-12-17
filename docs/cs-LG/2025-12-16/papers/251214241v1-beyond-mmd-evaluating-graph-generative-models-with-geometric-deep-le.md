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

**提出RGM方法以解决图生成模型评估中MMD指标的局限性问题**

**关键词**: `图生成模型` `几何深度学习` `模型评估` `最大均值差异` `图结构特性` `图分类` `网络科学` `生物信息学`

## 📋 核心要点

1. 现有图生成模型评估主要依赖最大均值差异，但该指标在捕捉图结构特性方面存在不足，导致评估不全面。
2. 论文提出RGM方法，利用几何深度学习模型在定制数据集上训练，以更准确地评估生成图的分布和结构特性。
3. 实验表明，GRAN和EDGE模型在生成真实图时存在结构特征保留的局限，同时验证了MMD作为评估指标的不充分性。

## 📝 摘要（中文）

图生成是网络科学和生物信息学等领域的核心任务，图生成模型通过学习真实世界图的分布来生成相似的新样本，如基于变分自编码器、循环神经网络和扩散模型的方法。然而，现有评估过程主要依赖最大均值差异作为度量生成图集合属性分布的指标，存在明显局限。本文提出了一种名为RGM的新方法，用于评估图生成模型，克服了MMD的不足。作为方法实践，我们全面评估了两种先进图生成模型：图循环注意力网络和高效度引导图生成模型，通过几何深度学习模型在合成与真实图数据集上训练进行性能比较。研究发现，虽然两种模型能生成具有特定拓扑属性的图，但在保持区分不同图域的结构特征方面存在显著局限，同时揭示了MMD作为评估指标的不充分性，为未来研究提供了替代方案。

## 🔬 方法详解

论文的核心方法是RGM，整体框架基于几何深度学习模型，该模型在包含合成和真实图的定制数据集上训练，专门用于图分类任务。关键技术创新点在于将图生成模型的评估问题转化为图表示学习问题，通过训练模型来区分不同图域的结构特征，从而更全面地评估生成图的分布。与现有方法的主要区别在于，RGM不依赖单一统计指标如MMD，而是利用深度学习模型捕捉图的复杂结构模式，提供更细粒度的评估视角。

## 📊 实验亮点

实验结果显示，GRAN和EDGE模型在生成图时能复现某些拓扑属性，但在保持区分不同图域的结构特征方面表现不佳，同时证实了MMD作为评估指标的局限性，为未来研究提供了基于几何深度学习的替代评估框架。

## 🎯 应用场景

该研究可应用于网络科学、生物信息学等领域，通过改进图生成模型的评估，有助于开发更高质量的合成图，用于网络模拟、药物发现和社交网络分析等实际任务，提升模型在实际场景中的可靠性和泛化能力。

## 📄 摘要（原文）

> Graph generation is a crucial task in many fields, including network science and bioinformatics, as it enables the creation of synthetic graphs that mimic the properties of real-world networks for various applications. Graph Generative Models (GGMs) have emerged as a promising solution to this problem, leveraging deep learning techniques to learn the underlying distribution of real-world graphs and generate new samples that closely resemble them. Examples include approaches based on Variational Auto-Encoders, Recurrent Neural Networks, and more recently, diffusion-based models. However, the main limitation often lies in the evaluation process, which typically relies on Maximum Mean Discrepancy (MMD) as a metric to assess the distribution of graph properties in the generated ensemble. This paper introduces a novel methodology for evaluating GGMs that overcomes the limitations of MMD, which we call RGM (Representation-aware Graph-generation Model evaluation). As a practical demonstration of our methodology, we present a comprehensive evaluation of two state-of-the-art Graph Generative Models: Graph Recurrent Attention Networks (GRAN) and Efficient and Degree-guided graph GEnerative model (EDGE). We investigate their performance in generating realistic graphs and compare them using a Geometric Deep Learning model trained on a custom dataset of synthetic and real-world graphs, specifically designed for graph classification tasks. Our findings reveal that while both models can generate graphs with certain topological properties, they exhibit significant limitations in preserving the structural characteristics that distinguish different graph domains. We also highlight the inadequacy of Maximum Mean Discrepancy as an evaluation metric for GGMs and suggest alternative approaches for future research.

