---
layout: default
title: Fast Visuomotor Policy for Robotic Manipulation
---

# Fast Visuomotor Policy for Robotic Manipulation

**arXiv**: [2510.12483v1](https://arxiv.org/abs/2510.12483) | [PDF](https://arxiv.org/pdf/2510.12483.pdf)

**作者**: Jingkai Jia, Tong Yang, Xueyao Chen, Chenhuan Liu, Wenqiang Zhang

---

## 💡 一句话要点

**提出Energy Policy框架，用于高速机器人操作任务，实现高效多模态动作预测。**

**关键词**: `机器人操作` `多模态动作预测` `能量学习` `高效策略` `高频任务`

## 📋 核心要点

1. 核心问题：现有机器人策略在高频任务中计算开销大，难以实现快速多模态动作预测。
2. 方法要点：采用能量分数作为学习目标，引入能量MLP简化架构，单次前向预测多模态动作。
3. 实验或效果：在模拟和真实任务中，性能匹配或超越先进方法，显著降低计算成本。

## 📄 摘要（原文）

> We present a fast and effective policy framework for robotic manipulation,
> named Energy Policy, designed for high-frequency robotic tasks and
> resource-constrained systems. Unlike existing robotic policies, Energy Policy
> natively predicts multimodal actions in a single forward pass, enabling
> high-precision manipulation at high speed. The framework is built upon two core
> components. First, we adopt the energy score as the learning objective to
> facilitate multimodal action modeling. Second, we introduce an energy MLP to
> implement the proposed objective while keeping the architecture simple and
> efficient. We conduct comprehensive experiments in both simulated environments
> and real-world robotic tasks to evaluate the effectiveness of Energy Policy.
> The results show that Energy Policy matches or surpasses the performance of
> state-of-the-art manipulation methods while significantly reducing
> computational overhead. Notably, on the MimicGen benchmark, Energy Policy
> achieves superior performance with at a faster inference compared to existing
> approaches.

