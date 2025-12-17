---
layout: default
title: Biothreat Benchmark Generation Framework for Evaluating Frontier AI Models II: Benchmark Generation Process
---

# Biothreat Benchmark Generation Framework for Evaluating Frontier AI Models II: Benchmark Generation Process

**arXiv**: [2512.08451v1](https://arxiv.org/abs/2512.08451) | [PDF](https://arxiv.org/pdf/2512.08451.pdf)

**作者**: Gary Ackerman, Zachary Kallenborn, Anna Wetzel, Hayley Peterson, Jenna LaTourette, Olivia Shoemaker, Brandon Behlendorf, Sheriff Almakki, Doug Clifford, Noah Sheinbaum

---

## 💡 一句话要点

**提出细菌生物威胁基准生成框架，用于评估前沿AI模型的生物安全风险**

**关键词**: `生物安全基准` `前沿AI评估` `红队测试` `基准生成框架` `生物威胁分析`

## 📋 核心要点

1. 核心问题：前沿AI模型可能被用于生物恐怖主义，需量化其生物安全风险
2. 方法要点：通过网页提示生成、红队测试和挖掘现有语料库，生成超过7,000个潜在基准
3. 实验或效果：经过去重和诊断性评估，最终筛选出1,010个基准，确保其诊断性、相关性和分析层次对齐

## 📄 摘要（原文）

> The potential for rapidly-evolving frontier artificial intelligence (AI) models, especially large language models (LLMs), to facilitate bioterrorism or access to biological weapons has generated significant policy, academic, and public concern. Both model developers and policymakers seek to quantify and mitigate any risk, with an important element of such efforts being the development of model benchmarks that can assess the biosecurity risk posed by a particular model. This paper, the second in a series of three, describes the second component of a novel Biothreat Benchmark Generation (BBG) framework: the generation of the Bacterial Biothreat Benchmark (B3) dataset. The development process involved three complementary approaches: 1) web-based prompt generation, 2) red teaming, and 3) mining existing benchmark corpora, to generate over 7,000 potential benchmarks linked to the Task-Query Architecture that was developed during the first component of the project. A process of de-duplication, followed by an assessment of uplift diagnosticity, and general quality control measures, reduced the candidates to a set of 1,010 final benchmarks. This procedure ensured that these benchmarks are a) diagnostic in terms of providing uplift; b) directly relevant to biosecurity threats; and c) are aligned with a larger biosecurity architecture permitting nuanced analysis at different levels of analysis.

