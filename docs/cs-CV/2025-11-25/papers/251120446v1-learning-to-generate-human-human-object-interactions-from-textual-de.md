---
layout: default
title: Learning to Generate Human-Human-Object Interactions from Textual Descriptions
---

# Learning to Generate Human-Human-Object Interactions from Textual Descriptions

**arXiv**: [2511.20446v1](https://arxiv.org/abs/2511.20446) | [PDF](https://arxiv.org/pdf/2511.20446.pdf)

**作者**: Jeonghyeon Na, Sangwon Baik, Inhee Lee, Junyoung Lee, Hanbyul Joo

---

## 💡 一句话要点

**提出基于文本生成多人-物体交互的统一框架，以解决复杂场景行为建模问题。**

**关键词**: `多人-物体交互` `文本到动作生成` `扩散模型` `合成数据集` `多人类运动生成`

## 📋 核心要点

1. 核心问题：建模两人共享物体交互的关联，称为HHOI，缺乏专用数据集。
2. 方法要点：利用扩散模型训练文本到HOI和HHI模型，并整合为统一生成框架。
3. 实验或效果：生成逼真HHOI，优于单人类方法，并扩展至多人类交互。

## 📄 摘要（原文）

> The way humans interact with each other, including interpersonal distances, spatial configuration, and motion, varies significantly across different situations. To enable machines to understand such complex, context-dependent behaviors, it is essential to model multiple people in relation to the surrounding scene context. In this paper, we present a novel research problem to model the correlations between two people engaged in a shared interaction involving an object. We refer to this formulation as Human-Human-Object Interactions (HHOIs). To overcome the lack of dedicated datasets for HHOIs, we present a newly captured HHOIs dataset and a method to synthesize HHOI data by leveraging image generative models. As an intermediary, we obtain individual human-object interaction (HOIs) and human-human interaction (HHIs) from the HHOIs, and with these data, we train an text-to-HOI and text-to-HHI model using score-based diffusion model. Finally, we present a unified generative framework that integrates the two individual model, capable of synthesizing complete HHOIs in a single advanced sampling process. Our method extends HHOI generation to multi-human settings, enabling interactions involving more than two individuals. Experimental results show that our method generates realistic HHOIs conditioned on textual descriptions, outperforming previous approaches that focus only on single-human HOIs. Furthermore, we introduce multi-human motion generation involving objects as an application of our framework.

