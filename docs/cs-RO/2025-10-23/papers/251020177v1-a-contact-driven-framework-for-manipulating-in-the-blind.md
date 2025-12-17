---
layout: default
title: A Contact-Driven Framework for Manipulating in the Blind
---

# A Contact-Driven Framework for Manipulating in the Blind

**arXiv**: [2510.20177v1](https://arxiv.org/abs/2510.20177) | [PDF](https://arxiv.org/pdf/2510.20177.pdf)

**作者**: Muhammad Suhail Saleem, Lai Yuan, Maxim Likhachev

---

## 💡 一句话要点

**提出基于接触反馈与结构先验的盲操作框架，以在视觉受限环境中实现鲁棒机器人操作。**

**关键词**: `机器人操作` `接触反馈` `占用估计` `运动规划` `结构先验` `盲操作`

## 📋 核心要点

1. 核心问题：机器人在视觉不足环境中操作，需依赖接触反馈避免碰撞并完成任务。
2. 方法要点：整合接触检测、占用估计和规划模块，利用结构先验预测未知区域。
3. 实验或效果：在模拟和真实任务中验证，任务完成时间减少达2倍，模块贡献得到确认。

## 📄 摘要（原文）

> Robots often face manipulation tasks in environments where vision is
> inadequate due to clutter, occlusions, or poor lighting--for example, reaching
> a shutoff valve at the back of a sink cabinet or locating a light switch above
> a crowded shelf. In such settings, robots, much like humans, must rely on
> contact feedback to distinguish free from occupied space and navigate around
> obstacles. Many of these environments often exhibit strong structural
> priors--for instance, pipes often span across sink cabinets--that can be
> exploited to anticipate unseen structure and avoid unnecessary collisions. We
> present a theoretically complete and empirically efficient framework for
> manipulation in the blind that integrates contact feedback with structural
> priors to enable robust operation in unknown environments. The framework
> comprises three tightly coupled components: (i) a contact detection and
> localization module that utilizes joint torque sensing with a contact particle
> filter to detect and localize contacts, (ii) an occupancy estimation module
> that uses the history of contact observations to build a partial occupancy map
> of the workspace and extrapolate it into unexplored regions with learned
> predictors, and (iii) a planning module that accounts for the fact that contact
> localization estimates and occupancy predictions can be noisy, computing paths
> that avoid collisions and complete tasks efficiently without eliminating
> feasible solutions. We evaluate the system in simulation and in the real world
> on a UR10e manipulator across two domestic tasks--(i) manipulating a valve
> under a kitchen sink surrounded by pipes and (ii) retrieving a target object
> from a cluttered shelf. Results show that the framework reliably solves these
> tasks, achieving up to a 2x reduction in task completion time compared to
> baselines, with ablations confirming the contribution of each module.

