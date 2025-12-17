---
layout: default
title: Explainable Graph Representation Learning via Graph Pattern Analysis
---

# Explainable Graph Representation Learning via Graph Pattern Analysis

**arXiv**: [2512.04530v1](https://arxiv.org/abs/2512.04530) | [PDF](https://arxiv.org/pdf/2512.04530.pdf)

**作者**: Xudong Wang, Ziheng Sun, Chris Ding, Jicong Fan

---

## 💡 一句话要点

**提出PXGL-GNN框架，通过图模式分析实现可解释的图表示学习**

**关键词**: `可解释人工智能` `图表示学习` `图模式分析` `图神经网络` `子结构采样`

## 📋 核心要点

1. 核心问题：探究图表示中捕获的具体信息，聚焦表示级可解释性
2. 方法要点：采样图子结构，学习模式表示并加权组合以解释贡献
3. 实验或效果：在监督和无监督任务中验证有效性，提供理论分析

## 📄 摘要（原文）

> Explainable artificial intelligence (XAI) is an important area in the AI community, and interpretability is crucial for building robust and trustworthy AI models. While previous work has explored model-level and instance-level explainable graph learning, there has been limited investigation into explainable graph representation learning. In this paper, we focus on representation-level explainable graph learning and ask a fundamental question: What specific information about a graph is captured in graph representations? Our approach is inspired by graph kernels, which evaluate graph similarities by counting substructures within specific graph patterns. Although the pattern counting vector can serve as an explainable representation, it has limitations such as ignoring node features and being high-dimensional. To address these limitations, we introduce a framework (PXGL-GNN) for learning and explaining graph representations through graph pattern analysis. We start by sampling graph substructures of various patterns. Then, we learn the representations of these patterns and combine them using a weighted sum, where the weights indicate the importance of each graph pattern's contribution. We also provide theoretical analyses of our methods, including robustness and generalization. In our experiments, we show how to learn and explain graph representations for real-world data using pattern analysis. Additionally, we compare our method against multiple baselines in both supervised and unsupervised learning tasks to demonstrate its effectiveness.

