---
layout: default
title: From Forecasting to Planning: Policy World Model for Collaborative State-Action Prediction
---

# From Forecasting to Planning: Policy World Model for Collaborative State-Action Prediction

**arXiv**: [2510.19654v1](https://arxiv.org/abs/2510.19654) | [PDF](https://arxiv.org/pdf/2510.19654.pdf)

**作者**: Zhida Zhao, Talas Fu, Yifan Wang, Lijun Wang, Huchuan Lu

---

## 💡 一句话要点

**提出策略世界模型以统一世界建模与轨迹规划，提升自动驾驶性能**

**关键词**: `自动驾驶世界模型` `轨迹规划` `状态-动作预测` `视频预测` `动态增强机制` `协作预测`

## 📋 核心要点

1. 核心问题：现有驾驶世界模型多用于仿真，与轨迹规划脱节，协同机制未充分探索。
2. 方法要点：集成世界建模与规划，通过无动作未来状态预测和协作状态-动作预测。
3. 实验或效果：仅用前摄像头输入，性能匹配或超越依赖多视图多模态的先进方法。

## 📄 摘要（原文）

> Despite remarkable progress in driving world models, their potential for
> autonomous systems remains largely untapped: the world models are mostly
> learned for world simulation and decoupled from trajectory planning. While
> recent efforts aim to unify world modeling and planning in a single framework,
> the synergistic facilitation mechanism of world modeling for planning still
> requires further exploration. In this work, we introduce a new driving paradigm
> named Policy World Model (PWM), which not only integrates world modeling and
> trajectory planning within a unified architecture, but is also able to benefit
> planning using the learned world knowledge through the proposed action-free
> future state forecasting scheme. Through collaborative state-action prediction,
> PWM can mimic the human-like anticipatory perception, yielding more reliable
> planning performance. To facilitate the efficiency of video forecasting, we
> further introduce a dynamically enhanced parallel token generation mechanism,
> equipped with a context-guided tokenizer and an adaptive dynamic focal loss.
> Despite utilizing only front camera input, our method matches or exceeds
> state-of-the-art approaches that rely on multi-view and multi-modal inputs.
> Code and model weights will be released at
> https://github.com/6550Zhao/Policy-World-Model.

