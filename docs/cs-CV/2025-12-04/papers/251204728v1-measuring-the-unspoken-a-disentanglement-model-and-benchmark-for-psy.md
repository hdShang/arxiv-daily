---
layout: default
title: Measuring the Unspoken: A Disentanglement Model and Benchmark for Psychological Analysis in the Wild
---

# Measuring the Unspoken: A Disentanglement Model and Benchmark for Psychological Analysis in the Wild

**arXiv**: [2512.04728v1](https://arxiv.org/abs/2512.04728) | [PDF](https://arxiv.org/pdf/2512.04728.pdf)

**作者**: Yigui Feng, Qinglin Wang, Haotian Mo, Yang Liu, Ke Liu, Gencheng Liu, Xinhai Chen, Siqi Shen, Songzhu Mei, Jie Liu

---

## 💡 一句话要点

**提出MIND模型和PRISM基准，解决野外对话中视觉-语言模型的表达-情感歧义和评估难题。**

**关键词**: `视觉-语言模型` `心理分析` `解耦学习` `微表情检测` `评估基准` `野外对话`

## 📋 核心要点

1. 核心问题：现有视觉-语言模型在野外对话中无法处理表达-情感歧义，且缺乏可验证的评估指标。
2. 方法要点：引入MIND模型，通过状态判断模块抑制歧义唇部特征，实现视觉解耦；构建ConvoInsight-DB数据集和PRISM评估框架。
3. 实验或效果：在PRISM基准上，MIND显著优于基线，微表情检测提升86.95%，消融研究确认状态判断模块是关键。

## 📄 摘要（原文）

> Generative psychological analysis of in-the-wild conversations faces two fundamental challenges: (1) existing Vision-Language Models (VLMs) fail to resolve Articulatory-Affective Ambiguity, where visual patterns of speech mimic emotional expressions; and (2) progress is stifled by a lack of verifiable evaluation metrics capable of assessing visual grounding and reasoning depth. We propose a complete ecosystem to address these twin challenges. First, we introduce Multilevel Insight Network for Disentanglement(MIND), a novel hierarchical visual encoder that introduces a Status Judgment module to algorithmically suppress ambiguous lip features based on their temporal feature variance, achieving explicit visual disentanglement. Second, we construct ConvoInsight-DB, a new large-scale dataset with expert annotations for micro-expressions and deep psychological inference. Third, Third, we designed the Mental Reasoning Insight Rating Metric (PRISM), an automated dimensional framework that uses expert-guided LLM to measure the multidimensional performance of large mental vision models. On our PRISM benchmark, MIND significantly outperforms all baselines, achieving a +86.95% gain in micro-expression detection over prior SOTA. Ablation studies confirm that our Status Judgment disentanglement module is the most critical component for this performance leap. Our code has been opened.

