---
layout: default
title: GUI-Rise: Structured Reasoning and History Summarization for GUI Navigation
---

# GUI-Rise: Structured Reasoning and History Summarization for GUI Navigation

**arXiv**: [2510.27210v1](https://arxiv.org/abs/2510.27210) | [PDF](https://arxiv.org/pdf/2510.27210.pdf)

**作者**: Tao Liu, Chongyu Wang, Rongjie Li, Yingchen Yu, Xuming He, Bai Song

---

## 💡 一句话要点

**提出GUI-Rise框架以增强GUI导航的跨域泛化和历史利用**

**关键词**: `GUI导航` `结构化推理` `历史摘要` `强化学习` `跨域泛化`

## 📋 核心要点

1. 当前MLLM GUI导航方法在跨域泛化和历史利用方面存在局限
2. 框架整合结构化推理、动作预测和历史摘要，通过CoT分析和GRPO训练
3. 在标准基准上实现SOTA结果，尤其在域外场景表现优异

## 📄 摘要（原文）

> While Multimodal Large Language Models (MLLMs) have advanced GUI navigation
> agents, current approaches face limitations in cross-domain generalization and
> effective history utilization. We present a reasoning-enhanced framework that
> systematically integrates structured reasoning, action prediction, and history
> summarization. The structured reasoning component generates coherent
> Chain-of-Thought analyses combining progress estimation and decision reasoning,
> which inform both immediate action predictions and compact history summaries
> for future steps. Based on this framework, we train a GUI agent,
> \textbf{GUI-Rise}, through supervised fine-tuning on pseudo-labeled
> trajectories and reinforcement learning with Group Relative Policy Optimization
> (GRPO). This framework employs specialized rewards, including a history-aware
> objective, directly linking summary quality to subsequent action performance.
> Comprehensive evaluations on standard benchmarks demonstrate state-of-the-art
> results under identical training data conditions, with particularly strong
> performance in out-of-domain scenarios. These findings validate our framework's
> ability to maintain robust reasoning and generalization across diverse GUI
> navigation tasks. Code is available at https://leon022.github.io/GUI-Rise.

