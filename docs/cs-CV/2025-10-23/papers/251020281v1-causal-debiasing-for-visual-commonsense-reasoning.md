---
layout: default
title: Causal Debiasing for Visual Commonsense Reasoning
---

# Causal Debiasing for Visual Commonsense Reasoning

**arXiv**: [2510.20281v1](https://arxiv.org/abs/2510.20281) | [PDF](https://arxiv.org/pdf/2510.20281.pdf)

**作者**: Jiayi Zou, Gengyun Jia, Bing-Kun Bao

---

## 💡 一句话要点

**提出因果去偏方法以解决视觉常识推理中的数据集偏见问题**

**关键词**: `视觉常识推理` `因果去偏` `后门调整` `数据集偏见` `跨模态泛化` `VCR-OOD数据集`

## 📋 核心要点

1. 核心问题：视觉常识推理中存在文本和视觉数据的共现与统计偏见，影响模型泛化。
2. 方法要点：基于因果图分析，采用后门调整方法消除预测捷径，构建答案字典去偏。
3. 实验或效果：在VCR-OOD数据集上验证去偏方法的有效性，提升模型跨模态泛化能力。

## 📄 摘要（原文）

> Visual Commonsense Reasoning (VCR) refers to answering questions and
> providing explanations based on images. While existing methods achieve high
> prediction accuracy, they often overlook bias in datasets and lack debiasing
> strategies. In this paper, our analysis reveals co-occurrence and statistical
> biases in both textual and visual data. We introduce the VCR-OOD datasets,
> comprising VCR-OOD-QA and VCR-OOD-VA subsets, which are designed to evaluate
> the generalization capabilities of models across two modalities. Furthermore,
> we analyze the causal graphs and prediction shortcuts in VCR and adopt a
> backdoor adjustment method to remove bias. Specifically, we create a dictionary
> based on the set of correct answers to eliminate prediction shortcuts.
> Experiments demonstrate the effectiveness of our debiasing method across
> different datasets.

