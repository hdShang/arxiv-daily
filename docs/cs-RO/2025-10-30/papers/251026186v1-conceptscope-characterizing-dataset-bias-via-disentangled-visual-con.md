---
layout: default
title: ConceptScope: Characterizing Dataset Bias via Disentangled Visual Concepts
---

# ConceptScope: Characterizing Dataset Bias via Disentangled Visual Concepts

**arXiv**: [2510.26186v1](https://arxiv.org/abs/2510.26186) | [PDF](https://arxiv.org/pdf/2510.26186.pdf)

**作者**: Jinho Choi, Hyesu Lim, Steffen Schneider, Jaegul Choo

---

## 💡 一句话要点

**提出ConceptScope框架，通过解耦视觉概念自动识别和量化数据集偏见。**

**关键词**: `数据集偏见分析` `视觉概念解耦` `稀疏自编码器` `可解释AI` `模型诊断`

## 📋 核心要点

1. 核心问题：数据集偏见普遍存在，但缺乏细粒度标注时难以系统识别。
2. 方法要点：使用稀疏自编码器从视觉基础模型中提取可解释概念，分类为目标、上下文和偏见类型。
3. 实验或效果：验证概念覆盖广，检测已知和未知偏见，支持数据集审计和模型诊断。

## 📄 摘要（原文）

> Dataset bias, where data points are skewed to certain concepts, is ubiquitous
> in machine learning datasets. Yet, systematically identifying these biases is
> challenging without costly, fine-grained attribute annotations. We present
> ConceptScope, a scalable and automated framework for analyzing visual datasets
> by discovering and quantifying human-interpretable concepts using Sparse
> Autoencoders trained on representations from vision foundation models.
> ConceptScope categorizes concepts into target, context, and bias types based on
> their semantic relevance and statistical correlation to class labels, enabling
> class-level dataset characterization, bias identification, and robustness
> evaluation through concept-based subgrouping. We validate that ConceptScope
> captures a wide range of visual concepts, including objects, textures,
> backgrounds, facial attributes, emotions, and actions, through comparisons with
> annotated datasets. Furthermore, we show that concept activations produce
> spatial attributions that align with semantically meaningful image regions.
> ConceptScope reliably detects known biases (e.g., background bias in
> Waterbirds) and uncovers previously unannotated ones (e.g, co-occurring objects
> in ImageNet), offering a practical tool for dataset auditing and model
> diagnostics.

