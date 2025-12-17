---
layout: default
title: Model-Based Diffusion Sampling for Predictive Control in Offline Decision Making
---

# Model-Based Diffusion Sampling for Predictive Control in Offline Decision Making

**arXiv**: [2512.08280v1](https://arxiv.org/abs/2512.08280) | [PDF](https://arxiv.org/pdf/2512.08280.pdf)

**作者**: Haldun Balim, Na Li, Yilun Du

---

## 💡 一句话要点

**提出基于模型的扩散采样框架MPDiffuser，以解决离线决策中轨迹动态不可行的问题。**

**关键词**: `离线决策` `扩散模型` `模型预测控制` `轨迹生成` `机器人控制`

## 📋 核心要点

1. 离线决策需从固定数据集合成可靠行为，但现有生成方法常产生动态不可行轨迹。
2. MPDiffuser结合规划器、动力学模型和排序器，通过交替扩散采样优化轨迹的任务对齐与可行性。
3. 在D4RL和DSRL基准上表现优于现有方法，并初步扩展到视觉控制与真实机器人部署。

## 📄 摘要（原文）

> Offline decision-making requires synthesizing reliable behaviors from fixed datasets without further interaction, yet existing generative approaches often yield trajectories that are dynamically infeasible. We propose Model Predictive Diffuser (MPDiffuser), a compositional model-based diffusion framework consisting of: (i) a planner that generates diverse, task-aligned trajectories; (ii) a dynamics model that enforces consistency with the underlying system dynamics; and (iii) a ranker module that selects behaviors aligned with the task objectives. MPDiffuser employs an alternating diffusion sampling scheme, where planner and dynamics updates are interleaved to progressively refine trajectories for both task alignment and feasibility during the sampling process. We also provide a theoretical rationale for this procedure, showing how it balances fidelity to data priors with dynamics consistency. Empirically, the compositional design improves sample efficiency, as it leverages even low-quality data for dynamics learning and adapts seamlessly to novel dynamics. We evaluate MPDiffuser on both unconstrained (D4RL) and constrained (DSRL) offline decision-making benchmarks, demonstrating consistent gains over existing approaches. Furthermore, we present a preliminary study extending MPDiffuser to vision-based control tasks, showing its potential to scale to high-dimensional sensory inputs. Finally, we deploy our method on a real quadrupedal robot, showcasing its practicality for real-world control.

