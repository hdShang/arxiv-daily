---
layout: default
title: Explaining Digital Pathology Models via Clustering Activations
---

# Explaining Digital Pathology Models via Clustering Activations

**arXiv**: [2511.14558v1](https://arxiv.org/abs/2511.14558) | [PDF](https://arxiv.org/pdf/2511.14558.pdf)

**作者**: Adam Bajger, Jan Obdržálek, Vojtěch Kůr, Rudolf Nenutil, Petr Holub, Vít Musil, Tomáš Brázdil

---

## 💡 一句话要点

**提出基于聚类的可解释性方法以增强数字病理模型的全局理解。**

**关键词**: `数字病理学` `模型可解释性` `聚类方法` `卷积神经网络` `前列腺癌检测`

## 📋 核心要点

1. 核心问题：现有方法如GradCAM仅突出单张切片的预测区域，缺乏模型全局行为分析。
2. 方法要点：通过聚类激活来展示模型全局行为，并提供更细粒度的信息。
3. 实验或效果：在前列腺癌检测模型上评估，证明方法实用并提升临床信心。

## 📄 摘要（原文）

> We present a clustering-based explainability technique for digital pathology models based on convolutional neural networks. Unlike commonly used methods based on saliency maps, such as occlusion, GradCAM, or relevance propagation, which highlight regions that contribute the most to the prediction for a single slide, our method shows the global behaviour of the model under consideration, while also providing more fine-grained information. The result clusters can be visualised not only to understand the model, but also to increase confidence in its operation, leading to faster adoption in clinical practice. We also evaluate the performance of our technique on an existing model for detecting prostate cancer, demonstrating its usefulness.

