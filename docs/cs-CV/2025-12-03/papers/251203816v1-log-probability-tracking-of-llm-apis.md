---
layout: default
title: Log Probability Tracking of LLM APIs
---

# Log Probability Tracking of LLM APIs

**arXiv**: [2512.03816v1](https://arxiv.org/abs/2512.03816) | [PDF](https://arxiv.org/pdf/2512.03816.pdf)

**作者**: Timothée Chauvin, Erwan Le Merrer, François Taïani, Gilles Tredan

---

## 💡 一句话要点

**提出基于对数概率的统计测试，以低成本连续监控LLM API的模型一致性**

**关键词**: `LLM API监控` `对数概率跟踪` `模型一致性审计` `成本效益分析` `TinyChange基准`

## 📋 核心要点

1. 核心问题：现有LLM API审计方法成本高，难以持续监控模型更新，影响应用可靠性和研究可复现性
2. 方法要点：利用LLM对数概率的非确定性特征，通过单令牌输出的平均对数概率进行简单统计测试
3. 实验或效果：在TinyChange基准上，该方法能检测细粒度微调变化，比现有方法敏感且成本降低1000倍

## 📄 摘要（原文）

> When using an LLM through an API provider, users expect the served model to remain consistent over time, a property crucial for the reliability of downstream applications and the reproducibility of research. Existing audit methods are too costly to apply at regular time intervals to the wide range of available LLM APIs. This means that model updates are left largely unmonitored in practice. In this work, we show that while LLM log probabilities (logprobs) are usually non-deterministic, they can still be used as the basis for cost-effective continuous monitoring of LLM APIs. We apply a simple statistical test based on the average value of each token logprob, requesting only a single token of output. This is enough to detect changes as small as one step of fine-tuning, making this approach more sensitive than existing methods while being 1,000x cheaper. We introduce the TinyChange benchmark as a way to measure the sensitivity of audit methods in the context of small, realistic model changes.

