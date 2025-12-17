---
layout: default
title: LangHOPS: Language Grounded Hierarchical Open-Vocabulary Part Segmentation
---

# LangHOPS: Language Grounded Hierarchical Open-Vocabulary Part Segmentation

**arXiv**: [2510.25263v1](https://arxiv.org/abs/2510.25263) | [PDF](https://arxiv.org/pdf/2510.25263.pdf)

**作者**: Yang Miao, Jan-Nico Zaech, Xi Wang, Fabien Despinoy, Danda Pani Paudel, Luc Van Gool

---

## 💡 一句话要点

**提出LangHOPS框架，基于MLLM实现开放词汇对象-部件实例分割。**

**关键词**: `开放词汇分割` `多模态大语言模型` `对象-部件层次` `实例分割` `零样本学习`

## 📋 核心要点

1. 核心问题：开放词汇对象-部件实例分割，需处理层次化概念。
2. 方法要点：在语言空间构建对象-部件层次，利用MLLM知识推理。
3. 实验效果：在PartImageNet和ADE20K上取得SOTA，提升AP和mIOU。

## 📄 摘要（原文）

> We propose LangHOPS, the first Multimodal Large Language Model (MLLM) based
> framework for open-vocabulary object-part instance segmentation. Given an
> image, LangHOPS can jointly detect and segment hierarchical object and part
> instances from open-vocabulary candidate categories. Unlike prior approaches
> that rely on heuristic or learnable visual grouping, our approach grounds
> object-part hierarchies in language space. It integrates the MLLM into the
> object-part parsing pipeline to leverage its rich knowledge and reasoning
> capabilities, and link multi-granularity concepts within the hierarchies. We
> evaluate LangHOPS across multiple challenging scenarios, including in-domain
> and cross-dataset object-part instance segmentation, and zero-shot semantic
> segmentation. LangHOPS achieves state-of-the-art results, surpassing previous
> methods by 5.5% Average Precision (AP) (in-domain) and 4.8% (cross-dataset) on
> the PartImageNet dataset and by 2.5% mIOU on unseen object parts in ADE20K
> (zero-shot). Ablation studies further validate the effectiveness of the
> language-grounded hierarchy and MLLM driven part query refinement strategy. The
> code will be released here.

