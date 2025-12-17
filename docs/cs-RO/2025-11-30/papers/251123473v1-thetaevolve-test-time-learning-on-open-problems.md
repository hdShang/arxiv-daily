---
layout: default
title: ThetaEvolve: Test-time Learning on Open Problems
---

# ThetaEvolve: Test-time Learning on Open Problems

**arXiv**: [2511.23473v1](https://arxiv.org/abs/2511.23473) | [PDF](https://arxiv.org/pdf/2511.23473.pdf)

**作者**: Yiping Wang, Shao-Rong Su, Zhiyuan Zeng, Eva Xu, Liliang Ren, Xinyu Yang, Zeyi Huang, Xuehai He, Luyao Ma, Baolin Peng, Hao Cheng, Pengcheng He, Weizhu Chen, Shuohang Wang, Simon Shaolei Du, Yelong Shen

---

## 💡 一句话要点

**提出ThetaEvolve框架，通过测试时学习改进开放优化问题**

**关键词**: `测试时学习` `开放优化问题` `强化学习` `大语言模型` `程序演化` `开源框架`

## 📋 核心要点

1. 核心问题：现有系统如AlphaEvolve依赖前沿大模型且无法内部化演化策略，限制了可扩展性和学习能力。
2. 方法要点：ThetaEvolve简化并扩展AlphaEvolve，结合上下文学习和强化学习，支持单一大模型、程序数据库和批量采样。
3. 实验或效果：在开放问题如圆包装和自相关不等式上，ThetaEvolve使开源模型达到新最优界，且测试时强化学习优于纯推理基线。

## 📄 摘要（原文）

> Recent advances in large language models (LLMs) have enabled breakthroughs in mathematical discovery, exemplified by AlphaEvolve, a closed-source system that evolves programs to improve bounds on open problems. However, it relies on ensembles of frontier LLMs to achieve new bounds and is a pure inference system that models cannot internalize the evolving strategies. We introduce ThetaEvolve, an open-source framework that simplifies and extends AlphaEvolve to efficiently scale both in-context learning and Reinforcement Learning (RL) at test time, allowing models to continually learn from their experiences in improving open optimization problems. ThetaEvolve features a single LLM, a large program database for enhanced exploration, batch sampling for higher throughput, lazy penalties to discourage stagnant outputs, and optional reward shaping for stable training signals, etc. ThetaEvolve is the first evolving framework that enable a small open-source model, like DeepSeek-R1-0528-Qwen3-8B, to achieve new best-known bounds on open problems (circle packing and first auto-correlation inequality) mentioned in AlphaEvolve. Besides, across two models and four open tasks, we find that ThetaEvolve with RL at test-time consistently outperforms inference-only baselines, and the model indeed learns evolving capabilities, as the RL-trained checkpoints demonstrate faster progress and better final performance on both trained target task and other unseen tasks. We release our code publicly: https://github.com/ypwang61/ThetaEvolve

