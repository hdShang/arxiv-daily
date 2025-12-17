---
layout: default
title: Solving LLM Repetition Problem in Production: A Comprehensive Study of Multiple Solutions
---

# Solving LLM Repetition Problem in Production: A Comprehensive Study of Multiple Solutions

**arXiv**: [2512.04419v1](https://arxiv.org/abs/2512.04419) | [PDF](https://arxiv.org/pdf/2512.04419.pdf)

**作者**: Weiwei Wang, Weijie Zou, Jiyong Min

---

## 💡 一句话要点

**提出多种解决方案以解决生产环境中大语言模型重复生成问题**

**关键词**: `大语言模型` `重复生成问题` `波束搜索` `直接偏好优化` `生产部署` `代码解释任务`

## 📋 核心要点

1. 核心问题：大语言模型在批处理代码解释任务中产生重复内容，导致性能下降和系统停滞
2. 方法要点：基于马尔可夫模型分析根源，评估波束搜索、惩罚参数和直接偏好优化三种解决方案
3. 实验或效果：实验验证波束搜索的early_stopping参数是关键，提供生产就绪的解决方案

## 📄 摘要（原文）

> The repetition problem, where Large Language Models (LLMs) continuously generate repetitive content without proper termination, poses a critical challenge in production deployments, causing severe performance degradation and system stalling. This paper presents a comprehensive investigation and multiple practical solutions for the repetition problem encountered in real-world batch code interpretation tasks.
>   We identify three distinct repetition patterns: (1) business rule generation repetition, (2) method call relationship analysis repetition, and (3) PlantUML diagram syntax generation repetition. Through rigorous theoretical analysis based on Markov models, we establish that the root cause lies in greedy decoding's inability to escape repetitive loops, exacerbated by self-reinforcement effects.
>   Our comprehensive experimental evaluation demonstrates three viable solutions: (1) Beam Search decoding with early_stopping=True serves as a universal post-hoc mechanism that effectively resolves all three repetition patterns; (2) presence_penalty hyperparameter provides an effective solution specifically for BadCase 1; and (3) Direct Preference Optimization (DPO) fine-tuning offers a universal model-level solution for all three BadCases.
>   The primary value of this work lies in combining first-hand production experience with extensive experimental validation. Our main contributions include systematic theoretical analysis of repetition mechanisms, comprehensive evaluation of multiple solutions with task-specific applicability mapping, identification of early_stopping as the critical parameter for Beam Search effectiveness, and practical production-ready solutions validated in real deployment environments.

