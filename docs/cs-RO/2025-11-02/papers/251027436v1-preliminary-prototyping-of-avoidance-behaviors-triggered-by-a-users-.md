---
layout: default
title: Preliminary Prototyping of Avoidance Behaviors Triggered by a User's Physical Approach to a Robot
---

# Preliminary Prototyping of Avoidance Behaviors Triggered by a User's Physical Approach to a Robot

**arXiv**: [2510.27436v1](https://arxiv.org/abs/2510.27436) | [PDF](https://arxiv.org/pdf/2510.27436.pdf)

**作者**: Tomoko Yonezawa, Hirotake Yamazoe, Atsuo Fujino, Daigo Suhara, Takaya Tamamoto, Yuto Nishiguchi

---

## 💡 一句话要点

**提出基于PAD模型和人际距离的机器人回避行为设计，以处理用户接近时的交互问题。**

**关键词**: `人机交互` `回避行为` `PAD情感模型` `人际距离建模` `机器人控制`

## 📋 核心要点

1. 核心问题：人机交互中用户物理接近时，机器人如何灵活响应类似人类的拒绝或容忍行为。
2. 方法要点：使用PAD模型的支配轴建模不适感累积与衰减，实现容忍和极限回避行为。
3. 实验或效果：在臂式机器人上实现从内部状态到分级运动和回避动作的连贯管道。

## 📄 摘要（原文）

> Human-robot interaction frequently involves physical proximity or contact. In
> human-human settings, people flexibly accept, reject, or tolerate such
> approaches depending on the relationship and context. We explore the design of
> a robot's rejective internal state and corresponding avoidance behaviors, such
> as withdrawing or pushing away, when a person approaches. We model the
> accumulation and decay of discomfort as a function of interpersonal distance,
> and implement tolerance (endurance) and limit-exceeding avoidance driven by the
> Dominance axis of the PAD affect model. The behaviors and their intensities are
> realized on an arm robot. Results illustrate a coherent pipeline from internal
> state parameters to graded endurance motions and, once a limit is crossed, to
> avoidance actions.

