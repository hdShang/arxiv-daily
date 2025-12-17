---
layout: default
title: PhysHSI: Towards a Real-World Generalizable and Natural Humanoid-Scene Interaction System
---

# PhysHSI: Towards a Real-World Generalizable and Natural Humanoid-Scene Interaction System

**arXiv**: [2510.11072v1](https://arxiv.org/abs/2510.11072) | [PDF](https://arxiv.org/pdf/2510.11072.pdf)

**作者**: Huayi Wang, Wentao Zhang, Runyi Yu, Tao Huang, Junli Ren, Feiyu Jia, Zirui Wang, Xiaojie Niu, Xiao Chen, Jiahe Chen, Qifeng Chen, Jingbo Wang, Jiangmiao Pang

---

## 💡 一句话要点

**提出PhysHSI系统，实现人形机器人在真实世界中通用且自然的场景交互。**

**关键词**: `人形机器人交互` `对抗运动先验` `场景感知` `模拟到真实部署` `多模态定位`

## 📋 核心要点

1. 核心问题：人形机器人需在真实环境中执行交互任务，但现有方法难以统一泛化运动和鲁棒感知。
2. 方法要点：采用模拟对抗运动先验学习，结合LiDAR与相机粗到精定位，提升交互自然性和鲁棒性。
3. 实验或效果：在模拟和真实世界验证四种交互任务，成功率高、泛化强、运动自然。

## 📄 摘要（原文）

> Deploying humanoid robots to interact with real-world environments--such as
> carrying objects or sitting on chairs--requires generalizable, lifelike motions
> and robust scene perception. Although prior approaches have advanced each
> capability individually, combining them in a unified system is still an ongoing
> challenge. In this work, we present a physical-world humanoid-scene interaction
> system, PhysHSI, that enables humanoids to autonomously perform diverse
> interaction tasks while maintaining natural and lifelike behaviors. PhysHSI
> comprises a simulation training pipeline and a real-world deployment system. In
> simulation, we adopt adversarial motion prior-based policy learning to imitate
> natural humanoid-scene interaction data across diverse scenarios, achieving
> both generalization and lifelike behaviors. For real-world deployment, we
> introduce a coarse-to-fine object localization module that combines LiDAR and
> camera inputs to provide continuous and robust scene perception. We validate
> PhysHSI on four representative interactive tasks--box carrying, sitting, lying,
> and standing up--in both simulation and real-world settings, demonstrating
> consistently high success rates, strong generalization across diverse task
> goals, and natural motion patterns.

