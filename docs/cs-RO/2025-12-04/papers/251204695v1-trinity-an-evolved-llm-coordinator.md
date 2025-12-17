---
layout: default
title: TRINITY: An Evolved LLM Coordinator
---

# TRINITY: An Evolved LLM Coordinator

**arXiv**: [2512.04695v1](https://arxiv.org/abs/2512.04695) | [PDF](https://arxiv.org/pdf/2512.04695.pdf)

**作者**: Jinglue Xu, Qi Sun, Peter Schwendeman, Stefan Nielsen, Edoardo Cetin, Yujin Tang

---

## 💡 一句话要点

**提出轻量级协调器Trinity，通过进化策略优化多LLM协作以解决模型融合难题。**

**关键词**: `大语言模型协调` `进化策略优化` `多模型协作` `轻量级架构` `任务分配`

## 📋 核心要点

1. 核心问题：权重融合受限于架构不匹配和封闭API，难以有效结合多样基础模型。
2. 方法要点：采用约0.6B参数紧凑模型和约10K参数轻量头，通过进化策略分配Thinker、Worker、Verifier角色。
3. 实验效果：在编码、数学、推理等任务上超越现有方法，LiveCodeBench得分86.2%，泛化能力强。

## 📄 摘要（原文）

> Combining diverse foundation models is promising, but weight-merging is limited by mismatched architectures and closed APIs. Trinity addresses this with a lightweight coordinator that orchestrates collaboration among large language models (LLMs). The coordinator, comprising a compact language model (approximately $0.6$B parameters) and a lightweight head (approximately $10$K parameters), is optimized with an evolutionary strategy for efficient and adaptive delegation. Trinity processes queries over multiple turns, where at each turn the coordinator assigns one of three roles (Thinker, Worker, or Verifier) to a selected LLM, effectively offloading complex skill acquisition from the coordinator itself. Experiments show that Trinity consistently outperforms individual models and existing methods across coding, math, reasoning, and domain knowledge tasks, and generalizes robustly to out-of-distribution tasks. On standard benchmarks, Trinity achieves state-of-the-art results, including a score of 86.2% on LiveCodeBench. Theoretical and empirical analyses identify two main factors behind this performance: (1) the coordinator's hidden-state representations provide rich contextualization of inputs, and (2) under high dimensionality and strict budget constraints, the separable Covariance Matrix Adaptation Evolution Strategy offers advantages over reinforcement learning, imitation learning, and random search by exploiting potential block-epsilon-separability.

