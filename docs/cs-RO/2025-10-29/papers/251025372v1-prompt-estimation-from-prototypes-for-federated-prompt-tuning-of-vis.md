---
layout: default
title: Prompt Estimation from Prototypes for Federated Prompt Tuning of Vision Transformers
---

# Prompt Estimation from Prototypes for Federated Prompt Tuning of Vision Transformers

**arXiv**: [2510.25372v1](https://arxiv.org/abs/2510.25372) | [PDF](https://arxiv.org/pdf/2510.25372.pdf)

**作者**: M Yashwanth, Sharannya Ghosh, Aditay Tripathi, Anirban Chakraborty

---

## 💡 一句话要点

**提出PEP-FedPT框架以解决联邦学习中视觉Transformer提示调优的泛化与个性化平衡问题**

**关键词**: `联邦学习` `视觉Transformer` `提示调优` `参数高效微调` `数据异构性` `个性化学习`

## 📋 核心要点

1. 核心问题：联邦学习中全局提示调优泛化差，个性化调优易过拟合且缺乏泛化能力
2. 方法要点：引入类上下文混合提示，结合全局共享提示和类特定提示，实现每样本个性化
3. 实验或效果：在多个数据集上超越现有方法，适应数据异构场景，提升效率和泛化性

## 📄 摘要（原文）

> Visual Prompt Tuning (VPT) of pre-trained Vision Transformers (ViTs) has
> proven highly effective as a parameter-efficient fine-tuning technique for
> adapting large models to downstream tasks with limited data. Its parameter
> efficiency makes it particularly suitable for Federated Learning (FL), where
> both communication and computation budgets are often constrained. However,
> global prompt tuning struggles to generalize across heterogeneous clients,
> while personalized tuning overfits to local data and lacks generalization. We
> propose PEP-FedPT (Prompt Estimation from Prototypes for Federated Prompt
> Tuning), a unified framework designed to achieve both generalization and
> personalization in federated prompt tuning of ViTs. Within this framework, we
> introduce the novel Class-Contextualized Mixed Prompt (CCMP) - based on
> class-specific prompts maintained alongside a globally shared prompt. For each
> input, CCMP adaptively combines class-specific prompts using weights derived
> from global class prototypes and client class priors. This approach enables
> per-sample prompt personalization without storing client-dependent trainable
> parameters. The prompts are collaboratively optimized via traditional federated
> averaging technique on the same. Comprehensive evaluations on CIFAR-100,
> TinyImageNet, DomainNet, and iNaturalist datasets demonstrate that PEP-FedPT
> consistently surpasses the state-of-the-art baselines under diverse data
> heterogeneity scenarios, establishing a strong foundation for efficient and
> generalizable federated prompt tuning of Vision Transformers.

