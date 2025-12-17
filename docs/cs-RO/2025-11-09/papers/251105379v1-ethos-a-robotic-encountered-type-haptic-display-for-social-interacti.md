---
layout: default
title: ETHOS: A Robotic Encountered-Type Haptic Display for Social Interaction in Virtual Reality
---

# ETHOS: A Robotic Encountered-Type Haptic Display for Social Interaction in Virtual Reality

**arXiv**: [2511.05379v1](https://arxiv.org/abs/2511.05379) | [PDF](https://arxiv.org/pdf/2511.05379.pdf)

**作者**: Eric Godden, Jacquie Groenewegen, Matthew K. X. J. Pan

---

## 💡 一句话要点

**提出ETHOS动态触觉显示系统，以在虚拟现实中实现自然社交互动。**

**关键词**: `触觉显示` `虚拟现实` `社交互动` `机器人控制` `实时追踪`

## 📋 核心要点

1. 核心问题：虚拟现实中社交互动缺乏真实物理接触，影响沉浸感。
2. 方法要点：集成扭矩控制机器人、可更换道具和实时手部追踪控制策略。
3. 实验或效果：静态定位精度约5毫米，平均接触延迟约29毫秒，验证可行性。

## 📄 摘要（原文）

> We present ETHOS (Encountered-Type Haptics for On-demand Social Interaction),
> a dynamic encountered-type haptic display (ETHD) that enables natural physical
> contact in virtual reality (VR) during social interactions such as handovers,
> fist bumps, and high-fives. The system integrates a torque-controlled robotic
> manipulator with interchangeable passive props (silicone hand replicas and a
> baton), marker-based physical-virtual registration via a ChArUco board, and a
> safety monitor that gates motion based on the user's head and hand pose. We
> introduce two control strategies: (i) a static mode that presents a stationary
> prop aligned with its virtual counterpart, consistent with prior ETHD
> baselines, and (ii) a dynamic mode that continuously updates prop position by
> exponentially blending an initial mid-point trajectory with real-time hand
> tracking, generating a unique contact point for each interaction. Bench tests
> show static colocation accuracy of 5.09 +/- 0.94 mm, while user interactions
> achieved temporal alignment with an average contact latency of 28.53 +/- 31.21
> ms across all interaction and control conditions. These results demonstrate the
> feasibility of recreating socially meaningful haptics in VR. By incorporating
> essential safety and control mechanisms, ETHOS establishes a practical
> foundation for high-fidelity, dynamic interpersonal interactions in virtual
> environments.

