---
layout: default
title: MedInsightBench: Evaluating Medical Analytics Agents Through Multi-Step Insight Discovery in Multimodal Medical Data
---

# MedInsightBench: Evaluating Medical Analytics Agents Through Multi-Step Insight Discovery in Multimodal Medical Data

**arXiv**: [2512.13297v1](https://arxiv.org/abs/2512.13297) | [PDF](https://arxiv.org/pdf/2512.13297.pdf)

**作者**: Zhenghao Zhu, Chuxue Cao, Sirui Han, Yuanfeng Song, Xing Chen, Caleb Chen Cao, Yike Guo

---

## 💡 一句话要点

**提出MedInsightBench基准与MedInsightAgent框架，以评估和改进多模态模型在医疗数据分析中的洞察发现能力。**

**关键词**: `医疗数据分析` `多模态基准` `自动化代理框架` `深度洞察发现` `医疗图像理解`

## 📋 核心要点

1. 核心问题：缺乏高质量数据集评估多模态模型在复杂医疗数据中的深度洞察能力。
2. 方法要点：构建包含332个医疗案例的基准，并设计三模块自动化代理框架进行多步分析。
3. 实验或效果：现有模型表现有限，MedInsightAgent能提升通用模型在医疗洞察发现中的性能。

## 📄 摘要（原文）

> In medical data analysis, extracting deep insights from complex, multi-modal datasets is essential for improving patient care, increasing diagnostic accuracy, and optimizing healthcare operations. However, there is currently a lack of high-quality datasets specifically designed to evaluate the ability of large multi-modal models (LMMs) to discover medical insights. In this paper, we introduce MedInsightBench, the first benchmark that comprises 332 carefully curated medical cases, each annotated with thoughtfully designed insights. This benchmark is intended to evaluate the ability of LMMs and agent frameworks to analyze multi-modal medical image data, including posing relevant questions, interpreting complex findings, and synthesizing actionable insights and recommendations. Our analysis indicates that existing LMMs exhibit limited performance on MedInsightBench, which is primarily attributed to their challenges in extracting multi-step, deep insights and the absence of medical expertise. Therefore, we propose MedInsightAgent, an automated agent framework for medical data analysis, composed of three modules: Visual Root Finder, Analytical Insight Agent, and Follow-up Question Composer. Experiments on MedInsightBench highlight pervasive challenges and demonstrate that MedInsightAgent can improve the performance of general LMMs in medical data insight discovery.

