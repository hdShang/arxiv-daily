---
layout: default
title: CausalProfiler: Generating Synthetic Benchmarks for Rigorous and Transparent Evaluation of Causal Machine Learning
---

# CausalProfiler: Generating Synthetic Benchmarks for Rigorous and Transparent Evaluation of Causal Machine Learning

**arXiv**: [2511.22842v1](https://arxiv.org/abs/2511.22842) | [PDF](https://arxiv.org/pdf/2511.22842.pdf)

**作者**: Panayiotis Panayiotou, Audrey Poinsot, Alessandro Leite, Nicolas Chesneau, Marc Schoenauer, Özgür Şimşek

---

## 💡 一句话要点

**提出CausalProfiler以生成合成基准，用于因果机器学习的严谨透明评估**

**关键词**: `因果机器学习` `基准生成` `合成数据` `评估方法` `因果推理`

## 📋 核心要点

1. 现有因果机器学习评估依赖有限数据集，导致结论脆弱且不可泛化
2. CausalProfiler基于明确设计选择随机采样因果模型、数据和查询，生成合成基准
3. 实验评估多种先进方法，展示其在识别和非识别机制下的分析能力

## 📄 摘要（原文）

> Causal machine learning (Causal ML) aims to answer "what if" questions using machine learning algorithms, making it a promising tool for high-stakes decision-making. Yet, empirical evaluation practices in Causal ML remain limited. Existing benchmarks often rely on a handful of hand-crafted or semi-synthetic datasets, leading to brittle, non-generalizable conclusions. To bridge this gap, we introduce CausalProfiler, a synthetic benchmark generator for Causal ML methods. Based on a set of explicit design choices about the class of causal models, queries, and data considered, the CausalProfiler randomly samples causal models, data, queries, and ground truths constituting the synthetic causal benchmarks. In this way, Causal ML methods can be rigorously and transparently evaluated under a variety of conditions. This work offers the first random generator of synthetic causal benchmarks with coverage guarantees and transparent assumptions operating on the three levels of causal reasoning: observation, intervention, and counterfactual. We demonstrate its utility by evaluating several state-of-the-art methods under diverse conditions and assumptions, both in and out of the identification regime, illustrating the types of analyses and insights the CausalProfiler enables.

