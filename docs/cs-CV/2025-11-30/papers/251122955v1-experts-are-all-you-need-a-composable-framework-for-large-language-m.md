---
layout: default
title: Experts are all you need: A Composable Framework for Large Language Model Inference
---

# Experts are all you need: A Composable Framework for Large Language Model Inference

**arXiv**: [2511.22955v1](https://arxiv.org/abs/2511.22955) | [PDF](https://arxiv.org/pdf/2511.22955.pdf)

**作者**: Shrihari Sridharan, Sourjya Roy, Anand Raghunathan, Kaushik Roy

---

## 💡 一句话要点

**提出Comp-LLM可组合推理框架，通过子查询依赖图实现专家协作，提升大语言模型效率与准确性。**

**关键词**: `大语言模型推理` `混合专家模型` `可组合框架` `子查询依赖图` `并行处理` `准确性提升`

## 📋 核心要点

1. 核心问题：大语言模型计算负担重，混合专家模型需联合预训练且不支持多步推理，多智能体框架延迟高。
2. 方法要点：Comp-LLM包含子查询生成器、查询执行器和响应聚合器，构建依赖图以并行处理子查询。
3. 实验或效果：在多个基准测试中，Comp-LLM提升准确性达11.01%，模型大小减少1.67x–3.56x，延迟改善1.1x–1.7x。

## 📄 摘要（原文）

> Large Language Models (LLMs) have achieved state-of-the-art accuracies in a variety of natural language processing (NLP) tasks. However, this success comes at the cost of increased model sizes which leads to additional computational burden. Mixture of Experts (MoEs) overcome this bottleneck by decoupling model capacity from computation by only activating a subset of parameters or "experts". However, these models require joint pretraining of these experts along with the router and do not model multi-step reasoning. In contrast, multi-agent frameworks improve reasoning by decomposing complex problems into modular subtasks. However, these frameworks rely on sequential "plan--act--observe" loops, which introduce significant latency. Our work, Comp-LLM, addresses these challenges by introducing a composable inference framework that enables cross-expert collaboration via an explicit sub-query dependency graph. Comp-LLM consists of three components: (1) A Sub-query Generator that decomposes an input query, assigns each sub-query to an appropriate expert using embedding similarity, and constructs a dependency graph; (2) A Query Executor that processes nodes in the graph and identifies opportunities for parallelism based on dependencies and resource constraints; and (3) A Response Aggregator that synthesizes intermediate expert responses into a coherent final answer. Across several benchmarks, Comp-LLM achieves up to 11.01% accuracy improvement over monolithic LLMs of similar size, while offering 1.67x--3.56x reduction in model size with no significant degradation relative to the largest model in its family. Additionally, Comp-LLM provides 1.1x--1.7x latency improvement compared to sequential sub-query processing.

