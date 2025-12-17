---
layout: default
title: RoboGPT-R1: Enhancing Robot Planning with Reinforcement Learning
---

# RoboGPT-R1: Enhancing Robot Planning with Reinforcement Learning

**arXiv**: [2510.14828v1](https://arxiv.org/abs/2510.14828) | [PDF](https://arxiv.org/pdf/2510.14828.pdf)

**作者**: Jinrui Liu, Bingyan Nie, Boyu Li, Yaran Chen, Yuze Wang, Shunsen He, Haoran Li

---

## 💡 一句话要点

**提出RoboGPT-R1两阶段微调框架以增强机器人在长视距操作任务中的规划能力**

**关键词**: `机器人规划` `强化学习` `视觉语言模型` `长视距操作` `两阶段微调` `奖励函数设计`

## 📋 核心要点

1. 核心问题：通用视觉语言模型在机器人规划中泛化差且物理理解不足，难以处理复杂长视距任务。
2. 方法要点：采用监督微调获取基础知识，再通过强化学习提升视觉空间理解和推理能力。
3. 实验或效果：在EmbodiedBench基准上，显著超越GPT-4o-mini和其他模型，提升超过20%。

## 📄 摘要（原文）

> Improving the reasoning capabilities of embodied agents is crucial for robots
> to complete complex human instructions in long-view manipulation tasks
> successfully. Despite the success of large language models and vision language
> models based on Supervised Fine-Tuning (SFT) in planning tasks, they continue
> facing challenges in performing long-horizon manipulation tasks in complex
> real-world environments, owing to their restricted common sense and reasoning
> capabilities. Considering that aligning general-purpose vision language models
> to robotic planning tasks via supervised fine-tuning suffers from poor
> generalization and insufficient physical understanding, we propose RoboGPT-R1,
> a two-stage fine-tuning framework for embodied planning. In this framework,
> supervised training acquires foundational knowledge through expert sequences,
> followed by RL to address the model's shortcomings in visual-spatial
> understanding and reasoning. To achieve physical understanding and action
> sequence consistency in multi-step reasoning tasks, we design a rule-based
> reward function that simultaneously considers long-horizon performance and
> action constraint in the environment. The reasoning model, trained on
> Qwen2.5-VL-3B, significantly outperforms the larger-scale model, GPT-4o-mini,
> by 21.33% and surpasses other work trained on Qwen2.5-VL-7B by 20.33% on the
> EmbodiedBench benchmark.

