---
layout: default
title: ManiAgent: An Agentic Framework for General Robotic Manipulation
---

# ManiAgent: An Agentic Framework for General Robotic Manipulation

**arXiv**: [2510.11660v1](https://arxiv.org/abs/2510.11660) | [PDF](https://arxiv.org/pdf/2510.11660.pdf)

**作者**: Yi Yang, Kefan Gu, Yuqing Wen, Hebei Li, Yucheng Zhao, Tiancai Wang, Xudong Liu

---

## 💡 一句话要点

**提出ManiAgent代理框架以解决机器人操作中复杂推理和长时任务规划问题**

**关键词**: `机器人操作` `代理框架` `视觉-语言-动作模型` `任务规划` `多代理系统`

## 📋 核心要点

1. 核心问题：视觉-语言-动作模型在复杂推理和长时任务规划中受限于数据稀缺和模型能力
2. 方法要点：采用多代理架构，通过代理间通信实现环境感知、子任务分解和动作生成
3. 实验或效果：在SimplerEnv基准上成功率86.8%，真实世界拾放任务成功率95.8%

## 📄 摘要（原文）

> While Vision-Language-Action (VLA) models have demonstrated impressive
> capabilities in robotic manipulation, their performance in complex reasoning
> and long-horizon task planning is limited by data scarcity and model capacity.
> To address this, we introduce ManiAgent, an agentic architecture for general
> manipulation tasks that achieves end-to-end output from task descriptions and
> environmental inputs to robotic manipulation actions. In this framework,
> multiple agents involve inter-agent communication to perform environmental
> perception, sub-task decomposition and action generation, enabling efficient
> handling of complex manipulation scenarios. Evaluations show ManiAgent achieves
> an 86.8% success rate on the SimplerEnv benchmark and 95.8% on real-world
> pick-and-place tasks, enabling efficient data collection that yields VLA models
> with performance comparable to those trained on human-annotated datasets.The
> project webpage is available at https://yi-yang929.github.io/ManiAgent/.

