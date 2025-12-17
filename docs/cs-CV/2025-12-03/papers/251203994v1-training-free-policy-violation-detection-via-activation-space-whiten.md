---
layout: default
title: Training-Free Policy Violation Detection via Activation-Space Whitening in LLMs
---

# Training-Free Policy Violation Detection via Activation-Space Whitening in LLMs

**arXiv**: [2512.03994v1](https://arxiv.org/abs/2512.03994) | [PDF](https://arxiv.org/pdf/2512.03994.pdf)

**作者**: Oren Rachmil, Roy Betser, Itay Gershon, Omer Hofman, Nitay Yakoby, Yuval Meron, Idan Yankelev, Asaf Shabtai, Yuval Elovici, Roman Vainshtein

---

## 💡 一句话要点

**提出基于激活空间白化的免训练策略违规检测方法，以解决组织内部LLM部署中的政策合规问题。**

**关键词**: `策略违规检测` `激活空间白化` `分布外检测` `免训练方法` `LLM对齐` `组织政策合规`

## 📋 核心要点

1. 核心问题：组织部署LLM时需检测内部政策违规，现有方法如安全护栏或微调存在延迟高、可解释性差等局限。
2. 方法要点：将策略违规检测视为分布外检测问题，通过线性变换对隐藏激活进行去相关和标准化，使用欧几里得范数作为合规分数。
3. 实验或效果：在挑战性政策基准上取得最优结果，超越现有护栏和微调推理模型，提供轻量级、易部署的解决方案。

## 📄 摘要（原文）

> Aligning proprietary large language models (LLMs) with internal organizational policies has become an urgent priority as organizations increasingly deploy LLMs in sensitive domains such as legal support, finance, and medical services. Beyond generic safety filters, enterprises require reliable mechanisms to detect policy violations within their regulatory and operational frameworks, where breaches can trigger legal and reputational risks. Existing content moderation frameworks, such as guardrails, remain largely confined to the safety domain and lack the robustness to capture nuanced organizational policies. LLM-as-a-judge and fine-tuning approaches, though flexible, introduce significant latency and lack interpretability. To address these limitations, we propose a training-free and efficient method that treats policy violation detection as an out-of-distribution (OOD) detection problem. Inspired by whitening techniques, we apply a linear transformation to decorrelate the model's hidden activations and standardize them to zero mean and unit variance, yielding near-identity covariance matrix. In this transformed space, we use the Euclidean norm as a compliance score to detect policy violations. The method requires only the policy text and a small number of illustrative samples, which makes it light-weight and easily deployable. On a challenging policy benchmark, our approach achieves state-of-the-art results, surpassing both existing guardrails and fine-tuned reasoning models. This work provides organizations with a practical and statistically grounded framework for policy-aware oversight of LLMs, advancing the broader goal of deployable AI governance. Code is available at: https://tinyurl.com/policy-violation-detection

