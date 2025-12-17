---
layout: default
title: MfNeuPAN: Proactive End-to-End Navigation in Dynamic Environments via Direct Multi-Frame Point Constraints
---

# MfNeuPAN: Proactive End-to-End Navigation in Dynamic Environments via Direct Multi-Frame Point Constraints

**arXiv**: [2511.17013v1](https://arxiv.org/abs/2511.17013) | [PDF](https://arxiv.org/pdf/2511.17013.pdf)

**作者**: Yiwen Ying, Hanjing Ye, Senzi Luo, Luyao Liu, Yu Zhan, Li He, Hong Zhang

---

## 💡 一句话要点

**提出多帧点约束框架以解决动态环境中机器人导航的实时避障问题**

**关键词**: `机器人导航` `动态环境避障` `多帧预测` `端到端学习` `主动规划`

## 📋 核心要点

1. 核心问题：传统方法假设静态环境，学习型方法依赖单帧观测，难以适应高度动态场景。
2. 方法要点：利用多帧点约束，包括预测模块生成未来帧，实现主动端到端导航。
3. 实验或效果：仿真和真实实验验证了在未知动态环境中导航的鲁棒性和效率提升。

## 📄 摘要（原文）

> Obstacle avoidance in complex and dynamic environments is a critical challenge for real-time robot navigation. Model-based and learning-based methods often fail in highly dynamic scenarios because traditional methods assume a static environment and cannot adapt to real-time changes, while learning-based methods rely on single-frame observations for motion constraint estimation, limiting their adaptability. To overcome these limitations, this paper proposes a novel framework that leverages multi-frame point constraints, including current and future frames predicted by a dedicated module, to enable proactive end-to-end navigation. By incorporating a prediction module that forecasts the future path of moving obstacles based on multi-frame observations, our method allows the robot to proactively anticipate and avoid potential dangers. This proactive planning capability significantly enhances navigation robustness and efficiency in unknown dynamic environments. Simulations and real-world experiments validate the effectiveness of our approach.

