---
layout: default
title: Who Judges the Judge? LLM Jury-on-Demand: Building Trustworthy LLM Evaluation Systems
---

# Who Judges the Judge? LLM Jury-on-Demand: Building Trustworthy LLM Evaluation Systems

**arXiv**: [2512.01786v1](https://arxiv.org/abs/2512.01786) | [PDF](https://arxiv.org/pdf/2512.01786.pdf)

**作者**: Xiaochuan Li, Ke Wang, Girija Gouda, Shubham Choudhary, Yaqun Wang, Linwei Hu, Joel Vaughan, Freddy Lecue

---

## 💡 一句话要点

**提出LLM Jury-on-Demand框架，以动态学习方式提升高风险领域LLM评估的可扩展性与可靠性。**

**关键词**: `大语言模型评估` `动态陪审团` `可靠性预测` `高风险管理` `可扩展系统`

## 📋 核心要点

1. 核心问题：现有LLM评估方法中，人工评估成本高，单LLM评估有偏见，静态陪审团缺乏适应性。
2. 方法要点：训练可靠性预测器，基于输入特征动态选择最优LLM陪审团，并以可靠性加权聚合评分。
3. 实验或效果：在摘要和RAG基准测试中，动态陪审团系统与人类判断的相关性显著高于基线方法。

## 📄 摘要（原文）

> As Large Language Models (LLMs) become integrated into high-stakes domains, there is a growing need for evaluation methods that are both scalable for real-time deployment and reliable for critical decision-making. While human evaluation is reliable, it is slow and costly. Single LLM judges are biased, and static juries lack adaptability. To overcome these limitations, we propose LLM Jury-on-Demand - a dynamic, learning-based framework for scalable and context-aware evaluation. Our method trains a set of reliability predictors to assess when LLM judges will agree with human experts, leveraging token distributions, embeddings, and structural input features. This enables a fully adaptive evaluation where, for each data point, an optimal jury of the most reliable judges is dynamically selected, and their scores are aggregated using their reliability as weights. Experiments on summarization and RAG benchmarks show that our dynamic jury system achieves significantly higher correlation with human judgment than both single-judge and static-jury baselines. These results highlight the promise of adaptive, learning-based juries for building scalable, more reliable and trustworthy evaluation systems for modern LLMs in high-stakes domains.

