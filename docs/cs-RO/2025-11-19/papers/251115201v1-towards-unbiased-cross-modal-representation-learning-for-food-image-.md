---
layout: default
title: Towards Unbiased Cross-Modal Representation Learning for Food Image-to-Recipe Retrieval
---

# Towards Unbiased Cross-Modal Representation Learning for Food Image-to-Recipe Retrieval

**arXiv**: [2511.15201v1](https://arxiv.org/abs/2511.15201) | [PDF](https://arxiv.org/pdf/2511.15201.pdf)

**作者**: Qing Wang, Chong-Wah Ngo, Ee-Peng Lim

---

## 💡 一句话要点

**提出因果干预方法以解决食物图像-食谱检索中的表示学习偏差问题**

**关键词**: `跨模态检索` `表示学习` `因果干预` `食物图像` `食谱检索` `偏差消除`

## 📋 核心要点

1. 核心问题：现有方法将食谱视为图像描述，忽略烹饪和拍摄因素导致的偏差
2. 方法要点：基于因果理论建模偏差，使用后门调整进行干预以消除偏差
3. 实验或效果：在Recipe1M数据集上实现MedR=1，并报告新SOTA检索性能

## 📄 摘要（原文）

> This paper addresses the challenges of learning representations for recipes and food images in the cross-modal retrieval problem. As the relationship between a recipe and its cooked dish is cause-and-effect, treating a recipe as a text source describing the visual appearance of a dish for learning representation, as the existing approaches, will create bias misleading image-and-recipe similarity judgment. Specifically, a food image may not equally capture every detail in a recipe, due to factors such as the cooking process, dish presentation, and image-capturing conditions. The current representation learning tends to capture dominant visual-text alignment while overlooking subtle variations that determine retrieval relevance. In this paper, we model such bias in cross-modal representation learning using causal theory. The causal view of this problem suggests ingredients as one of the confounder sources and a simple backdoor adjustment can alleviate the bias. By causal intervention, we reformulate the conventional model for food-to-recipe retrieval with an additional term to remove the potential bias in similarity judgment. Based on this theory-informed formulation, we empirically prove the oracle performance of retrieval on the Recipe1M dataset to be MedR=1 across the testing data sizes of 1K, 10K, and even 50K. We also propose a plug-and-play neural module, which is essentially a multi-label ingredient classifier for debiasing. New state-of-the-art search performances are reported on the Recipe1M dataset.

