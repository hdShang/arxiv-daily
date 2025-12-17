---
layout: default
title: Thor: Towards Human-Level Whole-Body Reactions for Intense Contact-Rich Environments
---

# Thor: Towards Human-Level Whole-Body Reactions for Intense Contact-Rich Environments

**arXiv**: [2510.26280v1](https://arxiv.org/abs/2510.26280) | [PDF](https://arxiv.org/pdf/2510.26280.pdf)

**作者**: Gangyang Li, Qing Shi, Youhao Hu, Jincheng Hu, Zhongyuan Wang, Xinlong Wang, Shaqi Luo

---

## 💡 一句话要点

**提出Thor框架以解决人形机器人在密集接触环境中的全身反应问题**

**关键词**: `人形机器人` `强化学习` `力自适应控制` `全身反应` `接触丰富环境`

## 📋 核心要点

1. 核心问题：人形机器人在密集接触环境中难以生成类人自适应反应，影响稳定性。
2. 方法要点：设计力自适应躯干倾斜奖励函数，并采用解耦强化学习架构控制身体各部分。
3. 实验或效果：在Unitree G1上实现高拉力性能，如后拉167.7N，比基线提升68.9%。

## 📄 摘要（原文）

> Humanoids hold great potential for service, industrial, and rescue
> applications, in which robots must sustain whole-body stability while
> performing intense, contact-rich interactions with the environment. However,
> enabling humanoids to generate human-like, adaptive responses under such
> conditions remains a major challenge. To address this, we propose Thor, a
> humanoid framework for human-level whole-body reactions in contact-rich
> environments. Based on the robot's force analysis, we design a force-adaptive
> torso-tilt (FAT2) reward function to encourage humanoids to exhibit human-like
> responses during force-interaction tasks. To mitigate the high-dimensional
> challenges of humanoid control, Thor introduces a reinforcement learning
> architecture that decouples the upper body, waist, and lower body. Each
> component shares global observations of the whole body and jointly updates its
> parameters. Finally, we deploy Thor on the Unitree G1, and it substantially
> outperforms baselines in force-interaction tasks. Specifically, the robot
> achieves a peak pulling force of 167.7 N (approximately 48% of the G1's body
> weight) when moving backward and 145.5 N when moving forward, representing
> improvements of 68.9% and 74.7%, respectively, compared with the
> best-performing baseline. Moreover, Thor is capable of pulling a loaded rack
> (130 N) and opening a fire door with one hand (60 N). These results highlight
> Thor's effectiveness in enhancing humanoid force-interaction capabilities.

