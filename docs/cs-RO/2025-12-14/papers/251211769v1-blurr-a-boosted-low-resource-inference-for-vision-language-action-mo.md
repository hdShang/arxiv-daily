---
layout: default
title: BLURR: A Boosted Low-Resource Inference for Vision-Language-Action Models
---

# BLURR: A Boosted Low-Resource Inference for Vision-Language-Action Models

**arXiv**: [2512.11769v1](https://arxiv.org/abs/2512.11769) | [PDF](https://arxiv.org/pdf/2512.11769.pdf)

**作者**: Xiaoyu Ma, Zhengqing Yuan, Zheyuan Zhang, Kaiwen Shi, Lichao Sun, Yanfang Ye

---

## 💡 一句话要点

**提出BLURR轻量推理包装器，以在有限计算资源下加速视觉-语言-动作模型部署。**

**关键词**: `视觉-语言-动作模型` `轻量推理` `键值缓存` `混合精度` `机器人控制` `Web部署`

## 📋 核心要点

1. 核心问题：VLA模型推理栈过重，难以在普通GPU上实现响应式Web演示或高频机器人控制。
2. 方法要点：通过指令前缀键值缓存、混合精度执行和单步展开调度，无需重训练即可加速现有VLA控制器。
3. 实验或效果：在SimplerEnv评估中保持任务成功率，显著降低FLOPs和延迟，并构建交互式Web演示。

## 📄 摘要（原文）

> Vision-language-action (VLA) models enable impressive zero shot manipulation, but their inference stacks are often too heavy for responsive web demos or high frequency robot control on commodity GPUs. We present BLURR, a lightweight inference wrapper that can be plugged into existing VLA controllers without retraining or changing model checkpoints. Instantiated on the pi-zero VLA controller, BLURR keeps the original observation interfaces and accelerates control by combining an instruction prefix key value cache, mixed precision execution, and a single step rollout schedule that reduces per step computation. In our SimplerEnv based evaluation, BLURR maintains task success rates comparable to the original controller while significantly lowering effective FLOPs and wall clock latency. We also build an interactive web demo that allows users to switch between controllers and toggle inference options in real time while watching manipulation episodes. This highlights BLURR as a practical approach for deploying modern VLA policies under tight compute budgets.

