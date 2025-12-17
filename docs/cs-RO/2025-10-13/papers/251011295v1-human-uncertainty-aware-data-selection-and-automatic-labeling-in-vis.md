---
layout: default
title: Human Uncertainty-Aware Data Selection and Automatic Labeling in Visual Question Answering
---

# Human Uncertainty-Aware Data Selection and Automatic Labeling in Visual Question Answering

**arXiv**: [2510.11295v1](https://arxiv.org/abs/2510.11295) | [PDF](https://arxiv.org/pdf/2510.11295.pdf)

**作者**: Jian Lan, Zhicheng Liu, Udo Schlegel, Raoyuan Zhao, Yihong Liu, Hinrich Schütze, Michael A. Hedderich, Thomas Seidl

---

## 💡 一句话要点

**提出HaDola框架以利用人类不确定性优化视觉问答模型训练**

**关键词**: `视觉问答` `人类不确定性` `数据选择` `自动标注` `模型校准` `监督微调`

## 📋 核心要点

1. 核心问题：人类不确定性影响监督微调，高不确定性样本可能降低模型性能。
2. 方法要点：HaDola通过四阶段迭代选择数据并自动标注，减少对昂贵标注的依赖。
3. 实验或效果：在VQAv2和VizWiz数据集上，HaDola以更少数据匹配或超越先进基线。

## 📄 摘要（原文）

> Large vision-language models (VLMs) achieve strong performance in Visual
> Question Answering but still rely heavily on supervised fine-tuning (SFT) with
> massive labeled datasets, which is costly due to human annotations. Crucially,
> real-world datasets often exhibit human uncertainty (HU) -- variation in human
> confidence across annotations -- but standard SFT simply optimizes toward the
> most frequent label, disregarding HU distributions. This leaves two open
> questions: How does HU affect SFT, and how can HU be effectively leveraged in
> training? In this work, we first conduct a systematic evaluation of VLMs across
> varying HU levels. We have two key findings: (i) surprisingly, high-HU samples
> contribute little or even degrade model performance, and (ii) naively training
> on the full dataset yields under-calibrated models that fail to capture HU
> distributions. Motivated by these findings, we introduce HaDola, a human
> uncertainty-aware data selection and automatic labeling framework. HaDola
> operates in four stages -- discriminate, self-annotate, error trigger, and
> training -- to iteratively identify harmful samples, prioritize informative
> ones, and bootstrap from a small seed set (5\% of data). Our approach
> substantially reduces reliance on costly HU annotations and makes VLMs more
> accurate and better calibrated. Extensive experiments on VQAv2 and VizWiz
> datasets demonstrate that HaDola consistently matches or outperforms
> state-of-the-art baselines with less training data. Our work highlights the
> importance of explicitly modeling HU in SFT, suggesting that better utilization
> of HU is more effective than merely scaling up dataset size.

