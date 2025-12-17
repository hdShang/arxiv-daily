---
layout: default
title: DriveCritic: Towards Context-Aware, Human-Aligned Evaluation for Autonomous Driving with Vision-Language Models
---

# DriveCritic: Towards Context-Aware, Human-Aligned Evaluation for Autonomous Driving with Vision-Language Models

**arXiv**: [2510.13108v1](https://arxiv.org/abs/2510.13108) | [PDF](https://arxiv.org/pdf/2510.13108.pdf)

**作者**: Jingyu Song, Zhenxin Li, Shiyi Lan, Xinglong Sun, Nadine Chang, Maying Shen, Joshua Chen, Katherine A. Skinner, Jose M. Alvarez

---

## 💡 一句话要点

**提出DriveCritic框架，通过视觉语言模型实现上下文感知的自动驾驶评估，以对齐人类偏好。**

**关键词**: `自动驾驶评估` `视觉语言模型` `上下文感知` `人类偏好对齐` `强化学习微调`

## 📋 核心要点

1. 核心问题：现有自动驾驶评估指标缺乏上下文感知，难以在复杂场景中匹配人类判断。
2. 方法要点：构建DriveCritic数据集和基于VLM的评估模型，采用两阶段监督与强化学习进行微调。
3. 实验或效果：DriveCritic在匹配人类偏好和上下文感知方面显著优于现有指标和基线。

## 📄 摘要（原文）

> Benchmarking autonomous driving planners to align with human judgment remains
> a critical challenge, as state-of-the-art metrics like the Extended Predictive
> Driver Model Score (EPDMS) lack context awareness in nuanced scenarios. To
> address this, we introduce DriveCritic, a novel framework featuring two key
> contributions: the DriveCritic dataset, a curated collection of challenging
> scenarios where context is critical for correct judgment and annotated with
> pairwise human preferences, and the DriveCritic model, a Vision-Language Model
> (VLM) based evaluator. Fine-tuned using a two-stage supervised and
> reinforcement learning pipeline, the DriveCritic model learns to adjudicate
> between trajectory pairs by integrating visual and symbolic context.
> Experiments show DriveCritic significantly outperforms existing metrics and
> baselines in matching human preferences and demonstrates strong context
> awareness. Overall, our work provides a more reliable, human-aligned foundation
> to evaluating autonomous driving systems.

