---
layout: default
title: COVLM-RL: Critical Object-Oriented Reasoning for Autonomous Driving Using VLM-Guided Reinforcement Learning
---

# COVLM-RL: Critical Object-Oriented Reasoning for Autonomous Driving Using VLM-Guided Reinforcement Learning

**arXiv**: [2512.09349v1](https://arxiv.org/abs/2512.09349) | [PDF](https://arxiv.org/pdf/2512.09349.pdf)

**作者**: Lin Li, Yuxin Cai, Jianwu Fang, Jianru Xue, Chen Lv

---

## 💡 一句话要点

**提出COVLM-RL框架，通过VLM引导的强化学习解决自动驾驶的泛化与可解释性问题。**

**关键词**: `自动驾驶` `视觉语言模型` `强化学习` `关键对象推理` `可解释性` `泛化能力`

## 📋 核心要点

1. 核心问题：端到端自动驾驶框架在泛化、训练效率和可解释性方面存在不足。
2. 方法要点：结合关键对象推理与VLM引导的强化学习，使用CoT提示生成语义决策先验。
3. 实验或效果：在CARLA模拟器中，训练环境成功率提升30%，未见环境提升50%。

## 📄 摘要（原文）

> End-to-end autonomous driving frameworks face persistent challenges in generalization, training efficiency, and interpretability. While recent methods leverage Vision-Language Models (VLMs) through supervised learning on large-scale datasets to improve reasoning, they often lack robustness in novel scenarios. Conversely, reinforcement learning (RL)-based approaches enhance adaptability but remain data-inefficient and lack transparent decision-making. % contribution To address these limitations, we propose COVLM-RL, a novel end-to-end driving framework that integrates Critical Object-oriented (CO) reasoning with VLM-guided RL. Specifically, we design a Chain-of-Thought (CoT) prompting strategy that enables the VLM to reason over critical traffic elements and generate high-level semantic decisions, effectively transforming multi-view visual inputs into structured semantic decision priors. These priors reduce the input dimensionality and inject task-relevant knowledge into the RL loop, accelerating training and improving policy interpretability. However, bridging high-level semantic guidance with continuous low-level control remains non-trivial. To this end, we introduce a consistency loss that encourages alignment between the VLM's semantic plans and the RL agent's control outputs, enhancing interpretability and training stability. Experiments conducted in the CARLA simulator demonstrate that COVLM-RL significantly improves the success rate by 30\% in trained driving environments and by 50\% in previously unseen environments, highlighting its strong generalization capability.

