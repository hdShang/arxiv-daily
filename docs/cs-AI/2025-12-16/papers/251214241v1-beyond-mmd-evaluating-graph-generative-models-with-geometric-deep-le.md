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

🎯 **匹配领域**: **强化学习**

**关键词**: `图生成模型评估` `几何深度学习` `图表示学习` `最大均值差异` `图分类任务` `图神经网络` `结构特征分析` `合成图生成`

## 📋 核心要点

1. 现有图生成模型评估主要依赖MMD指标，但该指标无法充分捕捉图的结构特征差异，导致评估结果不全面。
2. 论文提出RGM方法，利用几何深度学习模型学习图表示，通过分类任务评估生成图与真实图在结构特征上的相似性。
3. 实验显示GRAN和EDGE模型在生成图时存在结构特征保留不足的问题，RGM方法能更准确地揭示这些局限性。

## 📝 摘要（中文）

图生成是网络科学和生物信息学等领域的核心任务，图生成模型（GGMs）通过深度学习技术学习真实世界图的分布并生成相似样本。然而，现有评估方法主要依赖最大均值差异（MMD）来评估生成图集合的属性分布，存在明显局限性。本文提出了一种名为RGM（Representation-aware Graph-generation Model evaluation）的新方法，用于评估GGMs并克服MMD的不足。作为方法演示，我们全面评估了两种最先进的图生成模型：图循环注意力网络（GRAN）和高效度引导图生成模型（EDGE）。通过使用在合成和真实图数据集上训练的几何深度学习模型，我们研究了它们在生成真实图方面的性能。结果表明，虽然两种模型都能生成具有某些拓扑属性的图，但在保持区分不同图域的结构特征方面存在显著局限性。我们还强调了MMD作为GGMs评估指标的不足，并为未来研究提出了替代方法。

## 🔬 方法详解

**问题定义**：论文要解决图生成模型（GGMs）评估中现有方法依赖最大均值差异（MMD）指标的局限性问题。MMD主要基于图属性分布进行统计比较，但无法充分评估生成图在结构特征上的真实性，导致评估结果可能不准确或不全面。

**核心思路**：论文提出RGM（Representation-aware Graph-generation Model evaluation）方法，核心思想是利用几何深度学习模型学习图的表示，通过图分类任务来评估生成图与真实图在结构特征上的相似性。这种方法旨在捕捉图的高阶结构信息，弥补MMD仅关注低阶统计属性的不足。

**技术框架**：整体架构包括数据准备、模型训练和评估三个阶段。首先，构建包含合成图和真实图的自定义数据集，用于图分类任务。然后，训练一个几何深度学习模型（如基于图神经网络的分类器）来学习图的表示。最后，使用该模型对生成图进行分类，通过分类性能（如准确率）来评估GGMs的生成质量，并与MMD指标进行对比。

**关键创新**：最重要的技术创新是引入基于几何深度学习的表示学习来评估图生成模型，这超越了传统基于统计距离的MMD方法。本质区别在于，RGM关注图的结构特征和领域区分能力，而MMD仅依赖于预定义的图属性分布，可能导致评估偏差。

**关键设计**：关键设计包括使用自定义数据集混合合成和真实图，以确保评估的泛化性；选择几何深度学习模型（如图神经网络）进行图表示学习，以捕捉拓扑结构；通过分类任务设置，将生成图输入训练好的分类器，评估其与真实图的相似度；具体参数和损失函数依赖于所选几何深度学习模型，论文中未详细说明，但强调模型需针对图分类任务优化。

## 📊 实验亮点

实验对GRAN和EDGE两种先进图生成模型进行了全面评估。使用RGM方法结合几何深度学习模型，结果显示，虽然两种模型能生成具有某些拓扑属性（如度分布）的图，但在保持结构特征（如图域区分能力）方面存在显著局限性。具体而言，生成图在分类任务中的性能较低，表明其结构真实性不足。与MMD指标相比，RGM能更准确地揭示这些不足，突显了MMD作为评估指标的 inadequacy。实验未提供具体性能数据，但强调了RGM在评估中的优势。

## 🎯 应用场景

该研究在图生成模型评估领域具有重要应用价值，可广泛应用于网络科学、生物信息学、社交网络分析和药物发现等领域。通过提供更准确的评估方法，RGM能帮助研究人员优化图生成模型，生成更真实的合成图，用于数据增强、隐私保护或模拟实验。未来，该方法可能推动图生成技术的发展，并促进跨领域应用中的图数据合成与评估标准化。

## 📄 摘要（原文）

> Graph generation is a crucial task in many fields, including network science and bioinformatics, as it enables the creation of synthetic graphs that mimic the properties of real-world networks for various applications. Graph Generative Models (GGMs) have emerged as a promising solution to this problem, leveraging deep learning techniques to learn the underlying distribution of real-world graphs and generate new samples that closely resemble them. Examples include approaches based on Variational Auto-Encoders, Recurrent Neural Networks, and more recently, diffusion-based models. However, the main limitation often lies in the evaluation process, which typically relies on Maximum Mean Discrepancy (MMD) as a metric to assess the distribution of graph properties in the generated ensemble. This paper introduces a novel methodology for evaluating GGMs that overcomes the limitations of MMD, which we call RGM (Representation-aware Graph-generation Model evaluation). As a practical demonstration of our methodology, we present a comprehensive evaluation of two state-of-the-art Graph Generative Models: Graph Recurrent Attention Networks (GRAN) and Efficient and Degree-guided graph GEnerative model (EDGE). We investigate their performance in generating realistic graphs and compare them using a Geometric Deep Learning model trained on a custom dataset of synthetic and real-world graphs, specifically designed for graph classification tasks. Our findings reveal that while both models can generate graphs with certain topological properties, they exhibit significant limitations in preserving the structural characteristics that distinguish different graph domains. We also highlight the inadequacy of Maximum Mean Discrepancy as an evaluation metric for GGMs and suggest alternative approaches for future research.

