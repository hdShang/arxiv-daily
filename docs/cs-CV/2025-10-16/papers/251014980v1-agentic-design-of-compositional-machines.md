---
layout: default
title: Agentic Design of Compositional Machines
---

# Agentic Design of Compositional Machines

**arXiv**: [2510.14980v1](https://arxiv.org/abs/2510.14980) | [PDF](https://arxiv.org/pdf/2510.14980.pdf)

**作者**: Wenqian Zhang, Weiyang Liu, Zhen Liu

---

## 💡 一句话要点

**提出BesiegeField测试床和RL微调方法，以提升LLMs在组合机器设计中的能力。**

**关键词**: `组合机器设计` `大型语言模型` `物理模拟` `强化学习微调` `测试床构建`

## 📋 核心要点

1. 核心问题：LLMs能否学习在模拟物理环境中设计组合机器以满足功能需求。
2. 方法要点：引入BesiegeField测试床，支持基于部件的构建、物理模拟和奖励评估。
3. 实验或效果：基准测试LLMs，识别关键能力不足，探索RL微调以改进性能。

## 📄 摘要（原文）

> The design of complex machines stands as both a marker of human intelligence
> and a foundation of engineering practice. Given recent advances in large
> language models (LLMs), we ask whether they, too, can learn to create. We
> approach this question through the lens of compositional machine design: a task
> in which machines are assembled from standardized components to meet functional
> demands like locomotion or manipulation in a simulated physical environment. To
> support this investigation, we introduce BesiegeField, a testbed built on the
> machine-building game Besiege, which enables part-based construction, physical
> simulation and reward-driven evaluation. Using BesiegeField, we benchmark
> state-of-the-art LLMs with agentic workflows and identify key capabilities
> required for success, including spatial reasoning, strategic assembly, and
> instruction-following. As current open-source models fall short, we explore
> reinforcement learning (RL) as a path to improvement: we curate a cold-start
> dataset, conduct RL finetuning experiments, and highlight open challenges at
> the intersection of language, machine design, and physical reasoning.

