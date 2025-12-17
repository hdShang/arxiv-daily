---
layout: default
title: AUVIC: Adversarial Unlearning of Visual Concepts for Multi-modal Large Language Models
---

# AUVIC: Adversarial Unlearning of Visual Concepts for Multi-modal Large Language Models

**arXiv**: [2511.11299v1](https://arxiv.org/abs/2511.11299) | [PDF](https://arxiv.org/pdf/2511.11299.pdf)

**作者**: Haokun Chen, Jianing Li, Yao Zhang, Jinhe Bi, Yan Xia, Jindong Gu, Volker Tresp

---

## 💡 一句话要点

**提出AUVIC框架以解决多模态大模型中视觉概念精确遗忘问题**

**关键词**: `多模态大模型` `视觉概念遗忘` `对抗扰动` `数据隐私` `机器遗忘` `基准评估`

## 📋 核心要点

1. 核心问题：多模态大模型数据隐私问题，需实现视觉概念遗忘而不影响相关实体。
2. 方法要点：采用对抗扰动技术，精确隔离目标概念，避免副作用。
3. 实验或效果：在VCUBench基准上，实现高目标遗忘率，性能退化最小。

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) achieve impressive performance once optimized on massive datasets. Such datasets often contain sensitive or copyrighted content, raising significant data privacy concerns. Regulatory frameworks mandating the 'right to be forgotten' drive the need for machine unlearning. This technique allows for the removal of target data without resource-consuming retraining. However, while well-studied for text, visual concept unlearning in MLLMs remains underexplored. A primary challenge is precisely removing a target visual concept without disrupting model performance on related entities. To address this, we introduce AUVIC, a novel visual concept unlearning framework for MLLMs. AUVIC applies adversarial perturbations to enable precise forgetting. This approach effectively isolates the target concept while avoiding unintended effects on similar entities. To evaluate our method, we construct VCUBench. It is the first benchmark designed to assess visual concept unlearning in group contexts. Experimental results demonstrate that AUVIC achieves state-of-the-art target forgetting rates while incurs minimal performance degradation on non-target concepts.

