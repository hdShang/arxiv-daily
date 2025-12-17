---
layout: default
title: Sparse Autoencoders are Topic Models
---

# Sparse Autoencoders are Topic Models

**arXiv**: [2511.16309v1](https://arxiv.org/abs/2511.16309) | [PDF](https://arxiv.org/pdf/2511.16309.pdf)

**作者**: Leander Girrbach, Zeynep Akata

---

## 💡 一句话要点

**提出SAE-TM框架，将稀疏自编码器视为主题模型，用于跨模态大规模主题分析。**

**关键词**: `稀疏自编码器` `主题建模` `嵌入分析` `跨模态分析` `最大后验估计`

## 📋 核心要点

1. 核心问题：稀疏自编码器在嵌入分析中的角色与实用价值存在争议。
2. 方法要点：将LDA扩展至嵌入空间，推导SAE目标为最大后验估计器。
3. 实验或效果：SAE-TM在文本和图像数据集上生成更连贯且多样的主题。

## 📄 摘要（原文）

> Sparse autoencoders (SAEs) are used to analyze embeddings, but their role and practical value are debated. We propose a new perspective on SAEs by demonstrating that they can be naturally understood as topic models. We extend Latent Dirichlet Allocation to embedding spaces and derive the SAE objective as a maximum a posteriori estimator under this model. This view implies SAE features are thematic components rather than steerable directions. Based on this, we introduce SAE-TM, a topic modeling framework that: (1) trains an SAE to learn reusable topic atoms, (2) interprets them as word distributions on downstream data, and (3) merges them into any number of topics without retraining. SAE-TM yields more coherent topics than strong baselines on text and image datasets while maintaining diversity. Finally, we analyze thematic structure in image datasets and trace topic changes over time in Japanese woodblock prints. Our work positions SAEs as effective tools for large-scale thematic analysis across modalities. Code and data will be released upon publication.

