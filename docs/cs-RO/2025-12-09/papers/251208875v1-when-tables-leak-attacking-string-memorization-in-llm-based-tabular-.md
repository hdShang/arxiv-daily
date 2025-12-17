---
layout: default
title: When Tables Leak: Attacking String Memorization in LLM-Based Tabular Data Generation
---

# When Tables Leak: Attacking String Memorization in LLM-Based Tabular Data Generation

**arXiv**: [2512.08875v1](https://arxiv.org/abs/2512.08875) | [PDF](https://arxiv.org/pdf/2512.08875.pdf)

**作者**: Joshua Ward, Bochao Gu, Chi-Hua Wang, Guang Cheng

---

## 💡 一句话要点

**提出LevAtt攻击揭示LLM表格生成中数字字符串记忆泄露隐私风险，并提出防御方法。**

**关键词**: `表格数据生成` `隐私泄露` `成员推理攻击` `大语言模型` `数字字符串记忆`

## 📋 核心要点

1. 核心问题：LLM表格生成方法易泄露训练数据中数字字符串记忆，导致隐私风险。
2. 方法要点：设计LevAtt无盒成员推理攻击，仅基于生成数据分析数字序列泄露。
3. 实验或效果：攻击在多种模型和数据集上暴露显著泄露，并提出扰动采样防御降低风险。

## 📄 摘要（原文）

> Large Language Models (LLMs) have recently demonstrated remarkable performance in generating high-quality tabular synthetic data. In practice, two primary approaches have emerged for adapting LLMs to tabular data generation: (i) fine-tuning smaller models directly on tabular datasets, and (ii) prompting larger models with examples provided in context. In this work, we show that popular implementations from both regimes exhibit a tendency to compromise privacy by reproducing memorized patterns of numeric digits from their training data. To systematically analyze this risk, we introduce a simple No-box Membership Inference Attack (MIA) called LevAtt that assumes adversarial access to only the generated synthetic data and targets the string sequences of numeric digits in synthetic observations. Using this approach, our attack exposes substantial privacy leakage across a wide range of models and datasets, and in some cases, is even a perfect membership classifier on state-of-the-art models. Our findings highlight a unique privacy vulnerability of LLM-based synthetic data generation and the need for effective defenses. To this end, we propose two methods, including a novel sampling strategy that strategically perturbs digits during generation. Our evaluation demonstrates that this approach can defeat these attacks with minimal loss of fidelity and utility of the synthetic data.

