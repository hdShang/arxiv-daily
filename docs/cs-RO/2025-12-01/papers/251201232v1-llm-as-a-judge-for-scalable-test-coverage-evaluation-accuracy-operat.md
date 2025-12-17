---
layout: default
title: LLM-as-a-Judge for Scalable Test Coverage Evaluation: Accuracy, Operational Reliability, and Cost
---

# LLM-as-a-Judge for Scalable Test Coverage Evaluation: Accuracy, Operational Reliability, and Cost

**arXiv**: [2512.01232v1](https://arxiv.org/abs/2512.01232) | [PDF](https://arxiv.org/pdf/2512.01232.pdf)

**作者**: Donghao Huang, Shila Chew, Anna Dutkiewicz, Zhaoxia Wang

---

## 💡 一句话要点

**提出LLM-as-a-Judge框架，以可扩展方式评估Gherkin验收测试的覆盖度。**

**关键词**: `测试覆盖度评估` `LLM评估框架` `Gherkin验收测试` `操作可靠性` `成本分析` `模型比较`

## 📋 核心要点

1. 核心问题：大规模软件测试覆盖度评估在QA流程中仍是瓶颈。
2. 方法要点：基于评分准则的框架，使用LLM生成结构化JSON输出评估测试。
3. 实验或效果：在20种模型配置上分析准确性、操作可靠性和成本，发现小模型可优于大模型。

## 📄 摘要（原文）

> Assessing software test coverage at scale remains a bottleneck in QA pipelines. We present LLM-as-a-Judge (LAJ), a production-ready, rubric-driven framework for evaluating Gherkin acceptance tests with structured JSON outputs. Across 20 model configurations (GPT-4, GPT-5 with varying reasoning effort, and open-weight models) on 100 expert-annotated scripts over 5 runs (500 evaluations), we provide the first comprehensive analysis spanning accuracy, operational reliability, and cost. We introduce the Evaluation Completion Rate (ECR@1) to quantify first-attempt success, revealing reliability from 85.4% to 100.0% with material cost implications via retries. Results show that smaller models can outperform larger ones: GPT-4o Mini attains the best accuracy (6.07 MAAE), high reliability (96.6% ECR@1), and low cost ($1.01 per 1K), yielding a 78x cost reduction vs. GPT-5 (high reasoning) while improving accuracy. Reasoning effort is model-family dependent: GPT-5 benefits from increased reasoning (with predictable accuracy-cost tradeoffs), whereas open-weight models degrade across all dimensions as reasoning increases. Overall, cost spans 175x ($0.45-$78.96 per 1K). We release the dataset, framework, and code to support reproducibility and deployment.

