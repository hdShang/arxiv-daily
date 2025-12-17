---
layout: default
title: Multi-Path Collaborative Reasoning via Reinforcement Learning
---

# Multi-Path Collaborative Reasoning via Reinforcement Learning

**arXiv**: [2512.01485v1](https://arxiv.org/abs/2512.01485) | [PDF](https://arxiv.org/pdf/2512.01485.pdf)

**作者**: Jindi Lv, Yuhao Zhou, Zheng Zhu, Xiaofeng Wang, Guan Huang, Jiancheng Lv

---

## 💡 一句话要点

**提出M3PO强化学习框架，通过多路径协作推理解决链式思维解码的确定性限制。**

**关键词**: `链式思维推理` `强化学习` `多路径协作` `解码优化` `推理增强`

## 📋 核心要点

1. 核心问题：传统链式思维推理在解码时存在内部确定性，限制了替代推理路径的探索。
2. 方法要点：利用并行策略作为多样推理源，通过轻量协作机制整合跨路径交互以优化推理。
3. 实验或效果：在知识和推理密集型基准测试中达到最先进性能，保持可解释性和推理效率。

## 📄 摘要（原文）

> Chain-of-Thought (CoT) reasoning has significantly advanced the problem-solving capabilities of Large Language Models (LLMs), yet conventional CoT often exhibits internal determinism during decoding, limiting exploration of plausible alternatives. Recent methods attempt to address this by generating soft abstract tokens to enable reasoning in a continuous semantic space. However, we find that such approaches remain constrained by the greedy nature of autoregressive decoding, which fundamentally isolates the model from alternative reasoning possibilities. In this work, we propose Multi-Path Perception Policy Optimization (M3PO), a novel reinforcement learning framework that explicitly injects collective insights into the reasoning process. M3PO leverages parallel policy rollouts as naturally diverse reasoning sources and integrates cross-path interactions into policy updates through a lightweight collaborative mechanism. This design allows each trajectory to refine its reasoning with peer feedback, thereby cultivating more reliable multi-step reasoning patterns. Empirical results show that M3PO achieves state-of-the-art performance on both knowledge- and reasoning-intensive benchmarks. Models trained with M3PO maintain interpretability and inference efficiency, underscoring the promise of multi-path collaborative learning for robust reasoning.

