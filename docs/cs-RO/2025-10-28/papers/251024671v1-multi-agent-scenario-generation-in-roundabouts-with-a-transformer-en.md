---
layout: default
title: Multi-Agent Scenario Generation in Roundabouts with a Transformer-enhanced Conditional Variational Autoencoder
---

# Multi-Agent Scenario Generation in Roundabouts with a Transformer-enhanced Conditional Variational Autoencoder

**arXiv**: [2510.24671v1](https://arxiv.org/abs/2510.24671) | [PDF](https://arxiv.org/pdf/2510.24671.pdf)

**作者**: Li Li, Tobias Brinkmann, Till Temmen, Markus Eisenbarth, Jakob Andert

---

## 💡 一句话要点

**提出Transformer增强的条件变分自编码器以生成环岛多智能体交通场景**

**关键词**: `条件变分自编码器` `Transformer模型` `多智能体交互` `交通场景生成` `环岛仿真` `智能驾驶验证`

## 📋 核心要点

1. 智能驾驶功能测试面临高成本和低效率问题，需高效虚拟场景生成方法
2. 采用CVAE-T模型，结合Transformer处理环岛高动态和复杂布局场景
3. 模型能准确重构和生成多样真实场景，并通过KPI评估交互行为

## 📄 摘要（原文）

> With the increasing integration of intelligent driving functions into
> serial-produced vehicles, ensuring their functionality and robustness poses
> greater challenges. Compared to traditional road testing, scenario-based
> virtual testing offers significant advantages in terms of time and cost
> efficiency, reproducibility, and exploration of edge cases. We propose a
> Transformer-enhanced Conditional Variational Autoencoder (CVAE-T) model for
> generating multi-agent traffic scenarios in roundabouts, which are
> characterized by high vehicle dynamics and complex layouts, yet remain
> relatively underexplored in current research. The results show that the
> proposed model can accurately reconstruct original scenarios and generate
> realistic, diverse synthetic scenarios. Besides, two Key-Performance-Indicators
> (KPIs) are employed to evaluate the interactive behavior in the generated
> scenarios. Analysis of the latent space reveals partial disentanglement, with
> several latent dimensions exhibiting distinct and interpretable effects on
> scenario attributes such as vehicle entry timing, exit timing, and velocity
> profiles. The results demonstrate the model's capability to generate scenarios
> for the validation of intelligent driving functions involving multi-agent
> interactions, as well as to augment data for their development and iterative
> improvement.

