---
layout: default
title: [De|Re]constructing VLMs' Reasoning in Counting
---

# [De\|Re]constructing VLMs' Reasoning in Counting

**arXiv**: [2510.19555v1](https://arxiv.org/abs/2510.19555) | [PDF](https://arxiv.org/pdf/2510.19555.pdf)

**作者**: Simone Alghisi, Gabriel Roccabruna, Massimo Rizzoli, Seyed Mahed Mousavi, Giuseppe Riccardi

---

## 💡 一句话要点

**通过输出层微调提升视觉语言模型在计数任务中的推理能力**

**关键词**: `视觉语言模型` `计数任务` `推理能力` `层分析` `输出层微调` `对象检测`

## 📋 核心要点

1. 核心问题：视觉语言模型在计数任务中易受对象数量、空间排列和干扰物影响
2. 方法要点：分析模型层表示，发现错误源于最后一层映射问题
3. 实验或效果：仅微调输出层可使准确率提升高达21%，并在真实数据集验证

## 📄 摘要（原文）

> Vision-Language Models (VLMs) have recently gained attention due to their
> competitive performance on multiple downstream tasks, achieved by following
> user-input instructions. However, VLMs still exhibit several limitations in
> visual reasoning, such as difficulties in identifying relations (e.g., spatial,
> temporal, and among objects), understanding temporal sequences (e.g., frames),
> and counting objects. In this work, we go beyond score-level benchmark
> evaluations of VLMs by investigating the underlying causes of their failures
> and proposing a targeted approach to improve their reasoning capabilities. We
> study the reasoning skills of seven state-of-the-art VLMs in the counting task
> under controlled experimental conditions. Our experiments show that VLMs are
> highly sensitive to the number and type of objects, their spatial arrangement,
> and the co-occurrence of distractors. A layer-wise analysis reveals that errors
> are due to incorrect mapping of the last-layer representation into the output
> space. Our targeted training shows that fine-tuning just the output layer
> improves accuracy by up to 21%. We corroborate these findings by achieving
> consistent improvements on real-world datasets.

