---
layout: default
title: Prompt Fairness: Sub-group Disparities in LLMs
---

# Prompt Fairness: Sub-group Disparities in LLMs

**arXiv**: [2511.19956v1](https://arxiv.org/abs/2511.19956) | [PDF](https://arxiv.org/pdf/2511.19956.pdf)

**作者**: Meiyu Zhong, Noel Teku, Ravi Tandon

---

## 💡 一句话要点

**提出信息论指标与干预策略以缓解大语言模型提示公平性问题**

**关键词**: `大语言模型` `提示公平性` `信息论指标` `子群偏差` `模型干预` `响应稳定性`

## 📋 核心要点

1. 核心问题：大语言模型对相同问题不同提示风格响应不一致，导致子群间公平性差异
2. 方法要点：使用子群敏感性和跨群一致性指标量化偏差，并应用多数投票和提示中性化干预
3. 实验效果：干预后跨群分歧值从最高0.28降至0.22以下，输出稳定性提升

## 📄 摘要（原文）

> Large Language Models (LLMs), though shown to be effective in many applications, can vary significantly in their response quality. In this paper, we investigate this problem of prompt fairness: specifically, the phrasing of a prompt by different users/styles, despite the same question being asked in principle, may elicit different responses from an LLM. To quantify this disparity, we propose to use information-theoretic metrics that can capture two dimensions of bias: subgroup sensitivity, the variability of responses within a subgroup and cross group consistency, the variability of responses across subgroups. Our analysis reveals that certain subgroups exhibit both higher internal variability and greater divergence from others. Our empirical analysis reveals that certain demographic sub groups experience both higher internal variability and greater divergence from others, indicating structural inequities in model behavior. To mitigate these disparities, we propose practical interventions, including majority voting across multiple generations and prompt neutralization, which together improve response stability and enhance fairness across user populations. In the experiments, we observe clear prompt sensitivity disparities across demographic subgroups: before mitigation, cross-group divergence values reach 0.28 and typically fall in the from 0.14 to 0.22 range. After applying our neutralization and multi generation strategy, these divergences consistently decrease, with the largest gap reduced to 0.22 and many distances falling to 0.17 or below, indicating more stable and consistent outputs across subgroups.

