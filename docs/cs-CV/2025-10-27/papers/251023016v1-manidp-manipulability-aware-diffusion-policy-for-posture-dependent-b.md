---
layout: default
title: ManiDP: Manipulability-Aware Diffusion Policy for Posture-Dependent Bimanual Manipulation
---

# ManiDP: Manipulability-Aware Diffusion Policy for Posture-Dependent Bimanual Manipulation

**arXiv**: [2510.23016v1](https://arxiv.org/abs/2510.23016) | [PDF](https://arxiv.org/pdf/2510.23016.pdf)

**作者**: Zhuo Li, Junjia Liu, Dianxi Li, Tao Teng, Miao Li, Sylvain Calinon, Darwin Caldwell, Fei Chen

---

## 💡 一句话要点

**提出ManiDP以解决双手机器人操作中姿势依赖任务特征学习不足的问题**

**关键词**: `双手机器人操作` `扩散策略` `姿势依赖特征` `模仿学习` `黎曼概率模型` `任务兼容性`

## 📋 核心要点

1. 现有方法忽略姿势依赖任务特征，影响双臂配置适应力和速度需求
2. ManiDP提取双手机动性，使用黎曼概率模型编码姿势特征，指导扩散过程生成运动序列
3. 在六项真实任务中，平均成功率提升39.33%，任务兼容性提高0.45

## 📄 摘要（原文）

> Recent work has demonstrated the potential of diffusion models in robot
> bimanual skill learning. However, existing methods ignore the learning of
> posture-dependent task features, which are crucial for adapting dual-arm
> configurations to meet specific force and velocity requirements in dexterous
> bimanual manipulation. To address this limitation, we propose
> Manipulability-Aware Diffusion Policy (ManiDP), a novel imitation learning
> method that not only generates plausible bimanual trajectories, but also
> optimizes dual-arm configurations to better satisfy posture-dependent task
> requirements. ManiDP achieves this by extracting bimanual manipulability from
> expert demonstrations and encoding the encapsulated posture features using
> Riemannian-based probabilistic models. These encoded posture features are then
> incorporated into a conditional diffusion process to guide the generation of
> task-compatible bimanual motion sequences. We evaluate ManiDP on six real-world
> bimanual tasks, where the experimental results demonstrate a 39.33$\%$ increase
> in average manipulation success rate and a 0.45 improvement in task
> compatibility compared to baseline methods. This work highlights the importance
> of integrating posture-relevant robotic priors into bimanual skill diffusion to
> enable human-like adaptability and dexterity.

