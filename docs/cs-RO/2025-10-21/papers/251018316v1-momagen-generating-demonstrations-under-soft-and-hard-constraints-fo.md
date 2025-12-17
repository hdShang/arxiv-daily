---
layout: default
title: MoMaGen: Generating Demonstrations under Soft and Hard Constraints for Multi-Step Bimanual Mobile Manipulation
---

# MoMaGen: Generating Demonstrations under Soft and Hard Constraints for Multi-Step Bimanual Mobile Manipulation

**arXiv**: [2510.18316v1](https://arxiv.org/abs/2510.18316) | [PDF](https://arxiv.org/pdf/2510.18316.pdf)

**作者**: Chengshu Li, Mengdi Xu, Arpit Bahety, Hang Yin, Yunfan Jiang, Huang Huang, Josiah Wong, Sujay Garlanka, Cem Gokmen, Ruohan Zhang, Weiyu Liu, Jiajun Wu, Roberto Martín-Martín, Li Fei-Fei

---

## 💡 一句话要点

**提出MoMaGen框架，在软硬约束下生成多步骤双手机器人移动操作演示数据**

**关键词**: `机器人模仿学习` `双手机器人操作` `移动机器人` `数据生成优化` `约束优化问题`

## 📋 核心要点

1. 核心问题：多步骤双手机器人移动操作中，数据收集成本高，现有方法难以处理基座放置和相机定位挑战
2. 方法要点：将数据生成建模为约束优化问题，强制执行硬约束如可达性，平衡软约束如导航可见性
3. 实验或效果：在四个任务中生成更多样数据集，从单演示训练策略，仅需40真实演示即可部署到物理硬件

## 📄 摘要（原文）

> Imitation learning from large-scale, diverse human demonstrations has proven
> effective for training robots, but collecting such data is costly and
> time-consuming. This challenge is amplified for multi-step bimanual mobile
> manipulation, where humans must teleoperate both a mobile base and two
> high-degree-of-freedom arms. Prior automated data generation frameworks have
> addressed static bimanual manipulation by augmenting a few human demonstrations
> in simulation, but they fall short for mobile settings due to two key
> challenges: (1) determining base placement to ensure reachability, and (2)
> positioning the camera to provide sufficient visibility for visuomotor
> policies. To address these issues, we introduce MoMaGen, which formulates data
> generation as a constrained optimization problem that enforces hard constraints
> (e.g., reachability) while balancing soft constraints (e.g., visibility during
> navigation). This formulation generalizes prior approaches and provides a
> principled foundation for future methods. We evaluate MoMaGen on four
> multi-step bimanual mobile manipulation tasks and show that it generates
> significantly more diverse datasets than existing methods. Leveraging this
> diversity, MoMaGen can train successful imitation learning policies from a
> single source demonstration, and these policies can be fine-tuned with as few
> as 40 real-world demonstrations to achieve deployment on physical robotic
> hardware. More details are available at our project page: momagen.github.io.

