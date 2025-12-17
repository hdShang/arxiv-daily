---
layout: default
title: FANoise: Singular Value-Adaptive Noise Modulation for Robust Multimodal Representation Learning
---

# FANoise: Singular Value-Adaptive Noise Modulation for Robust Multimodal Representation Learning

**arXiv**: [2511.20997v1](https://arxiv.org/abs/2511.20997) | [PDF](https://arxiv.org/pdf/2511.20997.pdf)

**作者**: Jiaoyang Li, Jun Fang, Tianhao Gao, Xiaohui Zhang, Zhiyuan Liu, Chao Liu, Pengzhang Liu, Qixia Jiang

---

## 💡 一句话要点

**提出FANoise特征自适应噪声注入策略以增强多模态表示学习的鲁棒性**

**关键词**: `多模态表示学习` `噪声注入` `对比学习` `特征自适应` `鲁棒性增强`

## 📋 核心要点

1. 核心问题：现有噪声注入方法多为启发式或静态，忽略训练中特征分布的动态变化
2. 方法要点：基于对比学习动态，利用奇异值自适应调制噪声，平衡噪声利弊
3. 实验或效果：在多种基础VLM模型上，FANoise一致提升多模态任务性能

## 📄 摘要（原文）

> Representation learning is fundamental to modern machine learning, powering applications such as text retrieval and multimodal understanding. However, learning robust and generalizable representations remains challenging. While prior work has demonstrated that active noise injection, a form of data augmentation, can enhance encoding performance, most existing methods rely on heuristic or static noise, overlooking the dynamic nature of feature distributions during training. In this work, we systematically study the role of noise in representation learning from both gradient-based and feature distribution perspectives, using InfoNCE loss as a representative example. Focusing on multimodal representation learning, we propose FANoise, a novel feature-adaptive noise injection strategy. By leveraging the dynamics of contrastive learning, FANoise effectively mitigates the negative impacts of noise while preserving its benefits. Under this theoretically grounded framework, comprehensive experiments demonstrate that FANoise consistently improves overall performance on multimodal tasks across various base VLM models.

