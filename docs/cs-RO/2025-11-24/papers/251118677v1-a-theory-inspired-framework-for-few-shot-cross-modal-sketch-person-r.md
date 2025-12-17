---
layout: default
title: A Theory-Inspired Framework for Few-Shot Cross-Modal Sketch Person Re-Identification
---

# A Theory-Inspired Framework for Few-Shot Cross-Modal Sketch Person Re-Identification

**arXiv**: [2511.18677v1](https://arxiv.org/abs/2511.18677) | [PDF](https://arxiv.org/pdf/2511.18677.pdf)

**作者**: Yunpeng Gong, Yongjie Hou, Jiangming Shi, Kim Long Diep, Min Jiang

---

## 💡 一句话要点

**提出KTCAA框架以解决少样本跨模态草图行人重识别问题**

**关键词**: `草图行人重识别` `跨模态学习` `少样本学习` `泛化理论` `元学习` `对齐增强`

## 📋 核心要点

1. 核心问题：草图与RGB图像模态差异大且标注数据少，导致重识别困难。
2. 方法要点：基于泛化理论，设计对齐增强和知识转移催化剂模块提升对齐与鲁棒性。
3. 实验或效果：在多个基准测试中实现最先进性能，尤其在数据稀缺条件下表现突出。

## 📄 摘要（原文）

> Sketch based person re-identification aims to match hand-drawn sketches with RGB surveillance images, but remains challenging due to significant modality gaps and limited annotated data. To address this, we introduce KTCAA, a theoretically grounded framework for few-shot cross-modal generalization. Motivated by generalization theory, we identify two key factors influencing target domain risk: (1) domain discrepancy, which quantifies the alignment difficulty between source and target distributions; and (2) perturbation invariance, which evaluates the model's robustness to modality shifts. Based on these insights, we propose two components: (1) Alignment Augmentation (AA), which applies localized sketch-style transformations to simulate target distributions and facilitate progressive alignment; and (2) Knowledge Transfer Catalyst (KTC), which enhances invariance by introducing worst-case perturbations and enforcing consistency. These modules are jointly optimized under a meta-learning paradigm that transfers alignment knowledge from data-rich RGB domains to sketch-based scenarios. Experiments on multiple benchmarks demonstrate that KTCAA achieves state-of-the-art performance, particularly in data-scarce conditions.

