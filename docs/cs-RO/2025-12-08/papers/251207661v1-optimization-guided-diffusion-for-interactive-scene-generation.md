---
layout: default
title: Optimization-Guided Diffusion for Interactive Scene Generation
---

# Optimization-Guided Diffusion for Interactive Scene Generation

**arXiv**: [2512.07661v1](https://arxiv.org/abs/2512.07661) | [PDF](https://arxiv.org/pdf/2512.07661.pdf)

**作者**: Shiaho Li, Naisheng Ye, Tianyu Li, Kashyap Chitta, Tuo An, Peng Su, Boyang Wang, Haiou Liu, Chen Lv, Hongyang Li

---

## 💡 一句话要点

**提出OMEGA框架，通过优化引导扩散生成物理合理且行为一致的自动驾驶场景**

**关键词**: `自动驾驶场景生成` `扩散模型` `优化引导采样` `物理约束` `行为一致性` `对抗场景生成`

## 📋 核心要点

1. 问题：现有数据驱动场景生成模型缺乏可控性，常违反物理或社会约束，影响评估自动驾驶车辆的安全性。
2. 方法：OMEGA在扩散采样中引入优化引导，通过约束优化重锚反向扩散步骤，确保轨迹的物理合理性和行为一致性。
3. 效果：在nuPlan和Waymo数据集上，OMEGA显著提升场景有效性和可控性，并生成更多安全关键对抗场景。

## 📄 摘要（原文）

> Realistic and diverse multi-agent driving scenes are crucial for evaluating autonomous vehicles, but safety-critical events which are essential for this task are rare and underrepresented in driving datasets. Data-driven scene generation offers a low-cost alternative by synthesizing complex traffic behaviors from existing driving logs. However, existing models often lack controllability or yield samples that violate physical or social constraints, limiting their usability. We present OMEGA, an optimization-guided, training-free framework that enforces structural consistency and interaction awareness during diffusion-based sampling from a scene generation model. OMEGA re-anchors each reverse diffusion step via constrained optimization, steering the generation towards physically plausible and behaviorally coherent trajectories. Building on this framework, we formulate ego-attacker interactions as a game-theoretic optimization in the distribution space, approximating Nash equilibria to generate realistic, safety-critical adversarial scenarios. Experiments on nuPlan and Waymo show that OMEGA improves generation realism, consistency, and controllability, increasing the ratio of physically and behaviorally valid scenes from 32.35% to 72.27% for free exploration capabilities, and from 11% to 80% for controllability-focused generation. Our approach can also generate $5\times$ more near-collision frames with a time-to-collision under three seconds while maintaining the overall scene realism.

