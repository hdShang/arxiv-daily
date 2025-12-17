---
layout: default
title: Mitigating Error Accumulation in Co-Speech Motion Generation via Global Rotation Diffusion and Multi-Level Constraints
---

# Mitigating Error Accumulation in Co-Speech Motion Generation via Global Rotation Diffusion and Multi-Level Constraints

**arXiv**: [2511.10076v1](https://arxiv.org/abs/2511.10076) | [PDF](https://arxiv.org/pdf/2511.10076.pdf)

**作者**: Xiangyue Zhang, Jianfang Li, Jianqiang Ren, Jiaxu Zhang

---

## 💡 一句话要点

**提出GlobalDiff框架，通过全局旋转扩散和多级约束解决语音驱动运动生成中的误差累积问题。**

**关键词**: `语音驱动运动生成` `扩散模型` `全局旋转` `多级约束` `误差累积缓解` `运动结构保持`

## 📋 核心要点

1. 核心问题：现有方法基于局部关节旋转，导致层次误差累积，末端执行器运动不稳定。
2. 方法要点：首次在全局关节旋转空间操作扩散模型，引入多级约束增强结构感知。
3. 实验或效果：在标准基准上，性能提升46.0%，生成平滑准确运动。

## 📄 摘要（原文）

> Reliable co-speech motion generation requires precise motion representation and consistent structural priors across all joints. Existing generative methods typically operate on local joint rotations, which are defined hierarchically based on the skeleton structure. This leads to cumulative errors during generation, manifesting as unstable and implausible motions at end-effectors. In this work, we propose GlobalDiff, a diffusion-based framework that operates directly in the space of global joint rotations for the first time, fundamentally decoupling each joint's prediction from upstream dependencies and alleviating hierarchical error accumulation. To compensate for the absence of structural priors in global rotation space, we introduce a multi-level constraint scheme. Specifically, a joint structure constraint introduces virtual anchor points around each joint to better capture fine-grained orientation. A skeleton structure constraint enforces angular consistency across bones to maintain structural integrity. A temporal structure constraint utilizes a multi-scale variational encoder to align the generated motion with ground-truth temporal patterns. These constraints jointly regularize the global diffusion process and reinforce structural awareness. Extensive evaluations on standard co-speech benchmarks show that GlobalDiff generates smooth and accurate motions, improving the performance by 46.0 % compared to the current SOTA under multiple speaker identities.

