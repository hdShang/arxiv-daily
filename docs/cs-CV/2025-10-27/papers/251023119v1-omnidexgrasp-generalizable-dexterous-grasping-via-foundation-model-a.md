---
layout: default
title: OmniDexGrasp: Generalizable Dexterous Grasping via Foundation Model and Force Feedback
---

# OmniDexGrasp: Generalizable Dexterous Grasping via Foundation Model and Force Feedback

**arXiv**: [2510.23119v1](https://arxiv.org/abs/2510.23119) | [PDF](https://arxiv.org/pdf/2510.23119.pdf)

**作者**: Yi-Lin Wei, Zhexi Luo, Yuhao Lin, Mu Lin, Zhizhao Liang, Shuoyu Chen, Wei-Shi Zheng

---

## 💡 一句话要点

**提出OmniDexGrasp框架，结合基础模型与力反馈实现通用灵巧抓取**

**关键词**: `灵巧抓取` `基础模型` `力反馈控制` `机器人泛化` `动作转移`

## 📋 核心要点

1. 核心问题：现有方法因语义灵巧抓取数据集有限，难以泛化到多样物体或任务
2. 方法要点：集成基础模型生成人类抓取图像，并转换演示为机器人可执行动作
3. 实验或效果：仿真与真实机器人实验验证其在多样提示、任务和灵巧手上的有效性

## 📄 摘要（原文）

> Enabling robots to dexterously grasp and manipulate objects based on human
> commands is a promising direction in robotics. However, existing approaches are
> challenging to generalize across diverse objects or tasks due to the limited
> scale of semantic dexterous grasp datasets. Foundation models offer a new way
> to enhance generalization, yet directly leveraging them to generate feasible
> robotic actions remains challenging due to the gap between abstract model
> knowledge and physical robot execution. To address these challenges, we propose
> OmniDexGrasp, a generalizable framework that achieves omni-capabilities in user
> prompting, dexterous embodiment, and grasping tasks by combining foundation
> models with the transfer and control strategies. OmniDexGrasp integrates three
> key modules: (i) foundation models are used to enhance generalization by
> generating human grasp images supporting omni-capability of user prompt and
> task; (ii) a human-image-to-robot-action transfer strategy converts human
> demonstrations into executable robot actions, enabling omni dexterous
> embodiment; (iii) force-aware adaptive grasp strategy ensures robust and stable
> grasp execution. Experiments in simulation and on real robots validate the
> effectiveness of OmniDexGrasp on diverse user prompts, grasp task and dexterous
> hands, and further results show its extensibility to dexterous manipulation
> tasks.

