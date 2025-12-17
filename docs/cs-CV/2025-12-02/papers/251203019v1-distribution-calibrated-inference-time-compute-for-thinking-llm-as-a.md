---
layout: default
title: Distribution-Calibrated Inference time compute for Thinking LLM-as-a-Judge
---

# Distribution-Calibrated Inference time compute for Thinking LLM-as-a-Judge

**arXiv**: [2512.03019v1](https://arxiv.org/abs/2512.03019) | [PDF](https://arxiv.org/pdf/2512.03019.pdf)

**作者**: Hamid Dadkhahi, Firas Trabelsi, Parker Riley, Juraj Juraska, Mehdi Mirzazadeh

---

## 💡 一句话要点

**提出分布校准的推理时计算聚合方法，以提升大语言模型作为评判者的可靠性**

**关键词**: `大语言模型评判` `推理时计算` `分布校准` `成对偏好评估` `Bradley-Terry模型` `噪声聚合`

## 📋 核心要点

1. 核心问题：大语言模型作为成对偏好评判者时，单样本噪声大且常见聚合规则在允许平局时不一致
2. 方法要点：基于Bradley-Terry-Davidson模型，利用极性（非平局边际）和决断性（非平局率）校准评分分布
3. 实验或效果：在多个基准测试中降低MAE、提高成对准确率，匹配或超越人类评判者共识

## 📄 摘要（原文）

> Thinking Large Language Models (LLMs) used as judges for pairwise preferences remain noisy at the single-sample level, and common aggregation rules (majority vote, soft self-consistency, or instruction-based self-aggregation) are inconsistent when ties are allowed. We study inference-time compute (ITC) for evaluators that generate n independent thinking-rating samples per item, and propose a principled, distribution-calibrated aggregation scheme. Our method models three-way preferences with a Bradley-Terry-Davidson formulation on rating counts, leveraging both polarity (margin among non-ties) and decisiveness (non-tie rate) to distinguish narrow margins from strong consensus. Across various evaluation benchmarks, our approach consistently reduces MAE and increases pairwise accuracy versus standard baselines, and when evaluated against human-consensus meta-labels, matches or exceeds individual human raters. These results show that carefully allocating ITC and aggregating with distribution-aware methods turns noisy individual model judgments into reliable ratings for evaluation.

