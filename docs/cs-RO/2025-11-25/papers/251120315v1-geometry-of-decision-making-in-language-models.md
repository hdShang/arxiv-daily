---
layout: default
title: Geometry of Decision Making in Language Models
---

# Geometry of Decision Making in Language Models

**arXiv**: [2511.20315v1](https://arxiv.org/abs/2511.20315) | [PDF](https://arxiv.org/pdf/2511.20315.pdf)

**作者**: Abhinav Joshi, Divyanshu Bhatt, Ashutosh Modi

---

## 💡 一句话要点

**研究语言模型内在维度几何以揭示多选问答决策过程**

**关键词**: `语言模型` `内在维度` `多选问答` `表示几何` `决策过程`

## 📋 核心要点

1. 核心问题：语言模型内部决策过程不透明，影响可解释性。
2. 方法要点：使用内在维度分析隐藏表示，聚焦多选问答场景。
3. 实验或效果：28个模型显示ID模式：早期低维、中期扩展、后期压缩。

## 📄 摘要（原文）

> Large Language Models (LLMs) show strong generalization across diverse tasks, yet the internal decision-making processes behind their predictions remain opaque. In this work, we study the geometry of hidden representations in LLMs through the lens of \textit{intrinsic dimension} (ID), focusing specifically on decision-making dynamics in a multiple-choice question answering (MCQA) setting. We perform a large-scale study, with 28 open-weight transformer models and estimate ID across layers using multiple estimators, while also quantifying per-layer performance on MCQA tasks. Our findings reveal a consistent ID pattern across models: early layers operate on low-dimensional manifolds, middle layers expand this space, and later layers compress it again, converging to decision-relevant representations. Together, these results suggest LLMs implicitly learn to project linguistic inputs onto structured, low-dimensional manifolds aligned with task-specific decisions, providing new geometric insights into how generalization and reasoning emerge in language models.

