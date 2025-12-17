---
layout: default
title: Backdoor Unlearning by Linear Task Decomposition
---

# Backdoor Unlearning by Linear Task Decomposition

**arXiv**: [2510.14845v1](https://arxiv.org/abs/2510.14845) | [PDF](https://arxiv.org/pdf/2510.14845.pdf)

**作者**: Amel Abdelraheem, Alessandro Favero, Gerome Bovet, Pascal Frossard

---

## 💡 一句话要点

**提出线性任务分解方法以移除基础模型中的后门攻击**

**关键词**: `后门移除` `基础模型安全` `线性任务分解` `权重空间分析` `CLIP模型` `对抗攻击防御`

## 📋 核心要点

1. 基础模型易受后门攻击，现有方法需高成本微调且影响其他任务性能
2. 发现后门在权重空间中与良性任务解耦，可隔离并擦除其影响
3. 实验显示方法近乎完美移除后门，平均保持96%清洁准确率

## 📄 摘要（原文）

> Foundation models have revolutionized computer vision by enabling broad
> generalization across diverse tasks. Yet, they remain highly susceptible to
> adversarial perturbations and targeted backdoor attacks. Mitigating such
> vulnerabilities remains an open challenge, especially given that the
> large-scale nature of the models prohibits retraining to ensure safety.
> Existing backdoor removal approaches rely on costly fine-tuning to override the
> harmful behavior, and can often degrade performance on other unrelated tasks.
> This raises the question of whether backdoors can be removed without
> compromising the general capabilities of the models. In this work, we address
> this question and study how backdoors are encoded in the model weight space,
> finding that they are disentangled from other benign tasks. Specifically, this
> separation enables the isolation and erasure of the backdoor's influence on the
> model with minimal impact on clean performance. Building on this insight, we
> introduce a simple unlearning method that leverages such disentanglement.
> Through extensive experiments with CLIP-based models and common adversarial
> triggers, we show that, given the knowledge of the attack, our method achieves
> approximately perfect unlearning, while retaining, on average, 96% of clean
> accuracy. Additionally, we demonstrate that even when the attack and its
> presence are unknown, our method successfully unlearns backdoors by proper
> estimation using reverse-engineered triggers. Overall, our method consistently
> yields better unlearning and clean accuracy tradeoffs when compared to present
> state-of-the-art defenses.

