---
layout: default
title: C-NAV: Towards Self-Evolving Continual Object Navigation in Open World
---

# C-NAV: Towards Self-Evolving Continual Object Navigation in Open World

**arXiv**: [2510.20685v1](https://arxiv.org/abs/2510.20685) | [PDF](https://arxiv.org/pdf/2510.20685.pdf)

**作者**: Ming-Ming Yu, Fei Zhu, Wenzhuo Liu, Yirong Yang, Qunbo Wang, Wenjun Wu, Jing Liu

---

## 💡 一句话要点

**提出C-NAV框架以解决开放世界中持续物体导航的灾难性遗忘问题**

**关键词**: `持续学习` `物体导航` `灾难性遗忘` `特征蒸馏` `特征回放` `自适应采样`

## 📋 核心要点

1. 核心问题：现有方法依赖静态轨迹和固定物体类别，无法适应动态开放世界的持续学习需求。
2. 方法要点：集成双路径抗遗忘机制，包括特征蒸馏和特征回放，确保表示与策略一致性。
3. 实验或效果：在多种模型架构上优于现有方法，性能优于全轨迹保留基线，同时降低内存需求。

## 📄 摘要（原文）

> Embodied agents are expected to perform object navigation in dynamic,
> open-world environments. However, existing approaches typically rely on static
> trajectories and a fixed set of object categories during training, overlooking
> the real-world requirement for continual adaptation to evolving scenarios. To
> facilitate related studies, we introduce the continual object navigation
> benchmark, which requires agents to acquire navigation skills for new object
> categories while avoiding catastrophic forgetting of previously learned
> knowledge. To tackle this challenge, we propose C-Nav, a continual visual
> navigation framework that integrates two key innovations: (1) A dual-path
> anti-forgetting mechanism, which comprises feature distillation that aligns
> multi-modal inputs into a consistent representation space to ensure
> representation consistency, and feature replay that retains temporal features
> within the action decoder to ensure policy consistency. (2) An adaptive
> sampling strategy that selects diverse and informative experiences, thereby
> reducing redundancy and minimizing memory overhead. Extensive experiments
> across multiple model architectures demonstrate that C-Nav consistently
> outperforms existing approaches, achieving superior performance even compared
> to baselines with full trajectory retention, while significantly lowering
> memory requirements. The code will be publicly available at
> https://bigtree765.github.io/C-Nav-project.

