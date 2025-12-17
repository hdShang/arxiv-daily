---
layout: default
title: Automated Discovery of Laser Dicing Processes with Bayesian Optimization for Semiconductor Manufacturing
---

# Automated Discovery of Laser Dicing Processes with Bayesian Optimization for Semiconductor Manufacturing

**arXiv**: [2511.23141v1](https://arxiv.org/abs/2511.23141) | [PDF](https://arxiv.org/pdf/2511.23141.pdf)

**作者**: David Leeftink, Roman Doll, Heleen Visserman, Marco Post, Faysal Boughorbel, Max Hinne, Marcel van Gerven

---

## 💡 一句话要点

**提出基于贝叶斯优化的自动化激光切割工艺发现方法，用于半导体制造**

**关键词**: `贝叶斯优化` `激光切割` `半导体制造` `自动化工艺发现` `多目标优化`

## 📋 核心要点

1. 核心问题：半导体晶圆激光切割工艺需专家数周调整，以平衡速度、质量和材料完整性。
2. 方法要点：采用高维多目标贝叶斯优化与两级保真度策略，减少破坏性强度评估成本。
3. 实验或效果：在硅晶圆上自动发现可行配置，匹配或超越专家基准，支持专家优化提升速度。

## 📄 摘要（原文）

> Laser dicing of semiconductor wafers is a critical step in microelectronic manufacturing, where multiple sequential laser passes precisely separate individual dies from the wafer. Adapting this complex sequential process to new wafer materials typically requires weeks of expert effort to balance process speed, separation quality, and material integrity. We present the first automated discovery of production-ready laser dicing processes on an industrial LASER1205 dicing system. We formulate the problem as a high-dimensional, constrained multi-objective Bayesian optimization task, and introduce a sequential two-level fidelity strategy to minimize expensive destructive die-strength evaluations. On bare silicon and product wafers, our method autonomously delivers feasible configurations that match or exceed expert baselines in production speed, die strength, and structural integrity, using only technician-level operation. Post-hoc validation of different weight configurations of the utility functions reveals that multiple feasible solutions with qualitatively different trade-offs can be obtained from the final surrogate model. Expert-refinement of the discovered process can further improve production speed while preserving die strength and structural integrity, surpassing purely manual or automated methods.

