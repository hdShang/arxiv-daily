---
layout: default
title: Imitation Learning Policy based on Multi-Step Consistent Integration Shortcut Model
---

# Imitation Learning Policy based on Multi-Step Consistent Integration Shortcut Model

**arXiv**: [2510.19356v1](https://arxiv.org/abs/2510.19356) | [PDF](https://arxiv.org/pdf/2510.19356.pdf)

**作者**: Yu Fang, Xinyu Wang, Xuehe Zhang, Wanli Xue, Mingwei Zhang, Shengyong Chen, Jie Zhao

---

## 💡 一句话要点

**提出多步一致集成捷径模型以平衡机器人模仿学习的推理速度与性能**

**关键词**: `机器人模仿学习` `流匹配方法` `多步一致性损失` `自适应梯度分配` `一步推理优化`

## 📋 核心要点

1. 核心问题：流匹配方法在机器人模仿学习中推理时间高，现有蒸馏和一致性方法性能不足。
2. 方法要点：扩展多步一致性损失，分割一步损失为多步，并采用自适应梯度分配稳定优化。
3. 实验或效果：在模拟基准和真实环境任务中验证算法有效性，提升一步推理性能。

## 📄 摘要（原文）

> The wide application of flow-matching methods has greatly promoted the
> development of robot imitation learning. However, these methods all face the
> problem of high inference time. To address this issue, researchers have
> proposed distillation methods and consistency methods, but the performance of
> these methods still struggles to compete with that of the original diffusion
> models and flow-matching models. In this article, we propose a one-step
> shortcut method with multi-step integration for robot imitation learning. To
> balance the inference speed and performance, we extend the multi-step
> consistency loss on the basis of the shortcut model, split the one-step loss
> into multi-step losses, and improve the performance of one-step inference.
> Secondly, to solve the problem of unstable optimization of the multi-step loss
> and the original flow-matching loss, we propose an adaptive gradient allocation
> method to enhance the stability of the learning process. Finally, we evaluate
> the proposed method in two simulation benchmarks and five real-world
> environment tasks. The experimental results verify the effectiveness of the
> proposed algorithm.

