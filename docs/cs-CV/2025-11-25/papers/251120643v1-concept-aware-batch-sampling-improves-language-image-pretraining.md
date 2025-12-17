---
layout: default
title: Concept-Aware Batch Sampling Improves Language-Image Pretraining
---

# Concept-Aware Batch Sampling Improves Language-Image Pretraining

**arXiv**: [2511.20643v1](https://arxiv.org/abs/2511.20643) | [PDF](https://arxiv.org/pdf/2511.20643.pdf)

**作者**: Adhiraj Ghosh, Vishaal Udandarao, Thao Nguyen, Matteo Farina, Mehdi Cherti, Jenia Jitsev, Sewoong Oh, Elisa Ricci, Ludwig Schmidt, Matthias Bethge

---

## 💡 一句话要点

**提出概念感知批采样以改进语言-图像预训练**

**关键词**: `语言-图像预训练` `概念感知采样` `数据筛选` `在线学习` `CLIP模型` `多模态学习`

## 📋 核心要点

1. 核心问题：现有数据筛选方法离线且概念无关，易引入数据偏见。
2. 方法要点：基于DataConcept数据集，开发在线概念感知批采样框架CABS。
3. 实验或效果：在28个基准测试中显著提升CLIP/SigLIP模型性能。

## 📄 摘要（原文）

> What data should a vision-language model be trained on? To answer this question, many data curation efforts center on the quality of a dataset. However, most of these existing methods are (i) offline, i.e. they produce a static dataset from a set of predetermined filtering criteria, and (ii) concept-agnostic, i.e. they use model-based filters which induce additional data biases. In this work, we go beyond such offline, concept-agnostic methods and advocate for more flexible, task-adaptive online concept-based curation. Our first contribution is DataConcept, a collection of 128M web-crawled image-text pairs annotated with fine-grained details about their concept composition. Building on DataConcept, we introduce Concept-Aware Batch Sampling (CABS), a simple yet effective batch sampling framework that flexibly constructs batches on-the-fly based on specific target distributions. We propose two variants: (i) Diversity Maximization (CABS-DM) to curate batches with a broad coverage of available concepts, and (ii) Frequency Maximization (CABS-FM) to curate batches with high object multiplicity. Through extensive evaluations across 28 benchmarks, we demonstrate that our CABS method significantly benefits CLIP/SigLIP model classes and yields highly performant models. Overall, CABS represents a strong open-source alternative to proprietary online data curation algorithms, enabling practitioners to define custom concept distributions that optimize for specific downstream tasks.

