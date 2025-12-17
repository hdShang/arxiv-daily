---
layout: default
title: Controllable Long-term Motion Generation with Extended Joint Targets
---

# Controllable Long-term Motion Generation with Extended Joint Targets

**arXiv**: [2512.04487v1](https://arxiv.org/abs/2512.04487) | [PDF](https://arxiv.org/pdf/2512.04487.pdf)

**作者**: Eunjong Lee, Eunhee Kim, Sanghoon Hong, Eunho Jung, Jihoon Kim

---

## 💡 一句话要点

**提出COMET框架以解决实时角色动画中长序列运动稳定与精细控制问题**

**关键词**: `角色动画` `长序列运动生成` `实时控制` `Transformer` `条件VAE` `风格迁移`

## 📋 核心要点

1. 核心问题：现有方法在长序列中运动退化且缺乏精细控制，限制交互应用
2. 方法要点：基于Transformer的条件VAE实现实时自回归生成，引入参考引导反馈机制确保稳定性
3. 实验或效果：在复杂运动控制任务中显著优于现有方法，支持实时风格迁移

## 📄 摘要（原文）

> Generating stable and controllable character motion in real-time is a key challenge in computer animation. Existing methods often fail to provide fine-grained control or suffer from motion degradation over long sequences, limiting their use in interactive applications. We propose COMET, an autoregressive framework that runs in real time, enabling versatile character control and robust long-horizon synthesis. Our efficient Transformer-based conditional VAE allows for precise, interactive control over arbitrary user-specified joints for tasks like goal-reaching and in-betweening from a single model. To ensure long-term temporal stability, we introduce a novel reference-guided feedback mechanism that prevents error accumulation. This mechanism also serves as a plug-and-play stylization module, enabling real-time style transfer. Extensive evaluations demonstrate that COMET robustly generates high-quality motion at real-time speeds, significantly outperforming state-of-the-art approaches in complex motion control tasks and confirming its readiness for demanding interactive applications.

