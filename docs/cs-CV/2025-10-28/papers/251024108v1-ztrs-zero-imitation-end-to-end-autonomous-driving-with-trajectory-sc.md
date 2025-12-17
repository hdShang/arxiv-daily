---
layout: default
title: ZTRS: Zero-Imitation End-to-end Autonomous Driving with Trajectory Scoring
---

# ZTRS: Zero-Imitation End-to-end Autonomous Driving with Trajectory Scoring

**arXiv**: [2510.24108v1](https://arxiv.org/abs/2510.24108) | [PDF](https://arxiv.org/pdf/2510.24108.pdf)

**作者**: Zhenxin Li, Wenhao Yao, Zi Wang, Xinglong Sun, Jingde Chen, Nadine Chang, Maying Shen, Jingyu Song, Zuxuan Wu, Shiyi Lan, Jose M. Alvarez

---

## 💡 一句话要点

**提出ZTRS框架，结合传感器输入与强化学习，实现端到端自动驾驶无需模仿学习。**

**关键词**: `端到端自动驾驶` `离线强化学习` `轨迹评分` `传感器数据处理` `策略优化`

## 📋 核心要点

1. 端到端自动驾驶依赖模仿学习，易受专家演示和协变量偏移限制。
2. ZTRS使用离线强化学习和EPO优化，直接从高维传感器数据学习轨迹。
3. 在Navhard和HUGSIM基准上实现先进性能，超越模仿学习基线。

## 📄 摘要（原文）

> End-to-end autonomous driving maps raw sensor inputs directly into
> ego-vehicle trajectories to avoid cascading errors from perception modules and
> to leverage rich semantic cues. Existing frameworks largely rely on Imitation
> Learning (IL), which can be limited by sub-optimal expert demonstrations and
> covariate shift during deployment. On the other hand, Reinforcement Learning
> (RL) has recently shown potential in scaling up with simulations, but is
> typically confined to low-dimensional symbolic inputs (e.g. 3D objects and
> maps), falling short of full end-to-end learning from raw sensor data. We
> introduce ZTRS (Zero-Imitation End-to-End Autonomous Driving with Trajectory
> Scoring), a framework that combines the strengths of both worlds: sensor inputs
> without losing information and RL training for robust planning. To the best of
> our knowledge, ZTRS is the first framework that eliminates IL entirely by only
> learning from rewards while operating directly on high-dimensional sensor data.
> ZTRS utilizes offline reinforcement learning with our proposed Exhaustive
> Policy Optimization (EPO), a variant of policy gradient tailored for enumerable
> actions and rewards. ZTRS demonstrates strong performance across three
> benchmarks: Navtest (generic real-world open-loop planning), Navhard (open-loop
> planning in challenging real-world and synthetic scenarios), and HUGSIM
> (simulated closed-loop driving). Specifically, ZTRS achieves the
> state-of-the-art result on Navhard and outperforms IL-based baselines on
> HUGSIM. Code will be available at https://github.com/woxihuanjiangguo/ZTRS.

