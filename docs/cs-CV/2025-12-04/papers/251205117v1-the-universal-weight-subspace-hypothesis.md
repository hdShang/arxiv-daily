---
layout: default
title: The Universal Weight Subspace Hypothesis
---

# The Universal Weight Subspace Hypothesis

**arXiv**: [2512.05117v1](https://arxiv.org/abs/2512.05117) | [PDF](https://arxiv.org/pdf/2512.05117.pdf)

**作者**: Prakhar Kaushik, Shravan Chaudhari, Ankit Vaidya, Rama Chellappa, Alan Yuille

---

## 💡 一句话要点

**提出通用权重子空间假设，揭示跨任务神经网络共享低维参数子空间**

**关键词**: `权重子空间` `谱分析` `多任务学习` `模型合并` `神经网络结构` `计算效率`

## 📋 核心要点

1. 核心问题：探究深度神经网络在不同任务训练后是否具有内在的相似参数结构
2. 方法要点：通过谱分解技术分析超1100个模型的权重矩阵，识别共享的稀疏子空间
3. 实验或效果：发现模型在少数主方向上捕获大部分方差，支持子空间通用性

## 📄 摘要（原文）

> We show that deep neural networks trained across diverse tasks exhibit remarkably similar low-dimensional parametric subspaces. We provide the first large-scale empirical evidence that demonstrates that neural networks systematically converge to shared spectral subspaces regardless of initialization, task, or domain. Through mode-wise spectral analysis of over 1100 models - including 500 Mistral-7B LoRAs, 500 Vision Transformers, and 50 LLaMA-8B models - we identify universal subspaces capturing majority variance in just a few principal directions. By applying spectral decomposition techniques to the weight matrices of various architectures trained on a wide range of tasks and datasets, we identify sparse, joint subspaces that are consistently exploited, within shared architectures across diverse tasks and datasets. Our findings offer new insights into the intrinsic organization of information within deep networks and raise important questions about the possibility of discovering these universal subspaces without the need for extensive data and computational resources. Furthermore, this inherent structure has significant implications for model reusability, multi-task learning, model merging, and the development of training and inference-efficient algorithms, potentially reducing the carbon footprint of large-scale neural models.

