---
layout: default
title: A Systematic Study of Model Merging Techniques in Large Language Models
---

# A Systematic Study of Model Merging Techniques in Large Language Models

**arXiv**: [2511.21437v1](https://arxiv.org/abs/2511.21437) | [PDF](https://arxiv.org/pdf/2511.21437.pdf)

**作者**: Oğuz Kağan Hitit, Leander Girrbach, Zeynep Akata

---

## 💡 一句话要点

**系统评估模型合并方法，发现Task Arithmetic在大语言模型中表现最佳**

**关键词**: `模型合并` `大语言模型` `Task Arithmetic` `性能评估` `子空间方法`

## 📋 核心要点

1. 核心问题：模型合并技术是否适用于大语言模型，以提升性能而不需额外训练
2. 方法要点：评估六种先进合并方法，包括子空间方法，使用标准基准测试
3. 实验或效果：Task Arithmetic可靠提升性能，其他方法常导致显著性能下降

## 📄 摘要（原文）

> Model merging combines multiple fine-tuned checkpoints into a single model without additional training, offering an attractive approach to reusing models and efficiently improving performance. However, it remains unclear whether the advantages reported for smaller models and classifiers generalize to LLMs. We present a large-scale, systematic evaluation of six state-of-the-art merging methods, including recent subspace methods, across four open-weight LLMs, twelve fine-tuned checkpoints per base model, and sixteen standard LLM benchmarks. Evaluating through standardized benchmarks, we measure both the probability that a merged model outperforms the base model and relative gains over the best individual checkpoint. Our results show that the oldest and simplest method, Task Arithmetic, is the only approach that reliably yields performance gains on LLMs. Other interference-aware and subspace merging methods typically result in significant performance drops. Our findings indicate that current merging techniques do not directly transfer to modern LLMs. This motivates the design of LLM-specific merging algorithms and merging-aware fine-tuning methods. Code will be released upon acceptance of this paper.

