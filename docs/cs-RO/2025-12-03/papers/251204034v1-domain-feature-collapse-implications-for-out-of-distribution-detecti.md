---
layout: default
title: Domain Feature Collapse: Implications for Out-of-Distribution Detection and Solutions
---

# Domain Feature Collapse: Implications for Out-of-Distribution Detection and Solutions

**arXiv**: [2512.04034v1](https://arxiv.org/abs/2512.04034) | [PDF](https://arxiv.org/pdf/2512.04034.pdf)

**作者**: Hong Yang, Devroop Kar, Qi Yu, Alex Ororbia, Travis Desell

---

## 💡 一句话要点

**提出域特征坍缩理论以解释单域训练下OOD检测失败，并通过域过滤解决**

**关键词**: `域特征坍缩` `OOD检测` `信息瓶颈` `单域训练` `域过滤` `迁移学习`

## 📋 核心要点

1. 核心问题：单域数据集训练导致模型丢弃域特征，引发OOD检测灾难性失败
2. 方法要点：基于信息论证明域特征坍缩，提出域过滤保留域信息以提升检测
3. 实验或效果：构建Domain Bench基准，验证域过滤有效降低失败率，如MNIST上FPR@95达53%

## 📄 摘要（原文）

> Why do state-of-the-art OOD detection methods exhibit catastrophic failure when models are trained on single-domain datasets? We provide the first theoretical explanation for this phenomenon through the lens of information theory. We prove that supervised learning on single-domain data inevitably produces domain feature collapse -- representations where I(x_d; z) = 0, meaning domain-specific information is completely discarded. This is a fundamental consequence of information bottleneck optimization: models trained on single domains (e.g., medical images) learn to rely solely on class-specific features while discarding domain features, leading to catastrophic failure when detecting out-of-domain samples (e.g., achieving only 53% FPR@95 on MNIST). We extend our analysis using Fano's inequality to quantify partial collapse in practical scenarios. To validate our theory, we introduce Domain Bench, a benchmark of single-domain datasets, and demonstrate that preserving I(x_d; z) > 0 through domain filtering (using pretrained representations) resolves the failure mode. While domain filtering itself is conceptually straightforward, its effectiveness provides strong empirical evidence for our information-theoretic framework. Our work explains a puzzling empirical phenomenon, reveals fundamental limitations of supervised learning in narrow domains, and has broader implications for transfer learning and when to fine-tune versus freeze pretrained models.

