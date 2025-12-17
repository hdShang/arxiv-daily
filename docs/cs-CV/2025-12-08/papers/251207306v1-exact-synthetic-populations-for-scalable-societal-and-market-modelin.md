---
layout: default
title: Exact Synthetic Populations for Scalable Societal and Market Modeling
---

# Exact Synthetic Populations for Scalable Societal and Market Modeling

**arXiv**: [2512.07306v1](https://arxiv.org/abs/2512.07306) | [PDF](https://arxiv.org/pdf/2512.07306.pdf)

**作者**: Thierry Petit, Arnault Pachot

---

## 💡 一句话要点

**提出基于约束编程的合成人口生成框架，以精确控制人口统计特征并支持社会与市场建模。**

**关键词**: `合成人口生成` `约束编程` `人口统计建模` `社会行为模拟` `市场场景分析`

## 📋 核心要点

1. 核心问题：传统方法依赖样本推断分布，难以确保个体一致性和精确统计匹配。
2. 方法要点：直接编码聚合统计和结构关系，无需微观数据，实现高精度合成人口生成。
3. 实验或效果：在官方人口数据上验证，并分析分布偏差对下游分析的影响。

## 📄 摘要（原文）

> We introduce a constraint-programming framework for generating synthetic populations that reproduce target statistics with high precision while enforcing full individual consistency. Unlike data-driven approaches that infer distributions from samples, our method directly encodes aggregated statistics and structural relations, enabling exact control of demographic profiles without requiring any microdata. We validate the approach on official demographic sources and study the impact of distributional deviations on downstream analyses. This work is conducted within the Pollitics project developed by Emotia, where synthetic populations can be queried through large language models to model societal behaviors, explore market and policy scenarios, and provide reproducible decision-grade insights without personal data.

