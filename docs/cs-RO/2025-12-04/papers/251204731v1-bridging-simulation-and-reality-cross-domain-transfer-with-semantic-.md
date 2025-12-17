---
layout: default
title: Bridging Simulation and Reality: Cross-Domain Transfer with Semantic 2D Gaussian Splatting
---

# Bridging Simulation and Reality: Cross-Domain Transfer with Semantic 2D Gaussian Splatting

**arXiv**: [2512.04731v1](https://arxiv.org/abs/2512.04731) | [PDF](https://arxiv.org/pdf/2512.04731.pdf)

**作者**: Jian Tang, Pu Pang, Haowen Sun, Chengzhong Ma, Xingyu Chen, Hua Huang, Xuguang Lan

---

## 💡 一句话要点

**提出语义2D高斯泼溅以解决机器人操作中仿真到现实的跨域迁移问题**

**关键词**: `跨域迁移` `语义表示` `高斯泼溅` `机器人操作` `仿真到现实` `域不变特征`

## 📋 核心要点

1. 核心问题：仿真与真实环境间存在显著域差距，影响机器人操作策略的泛化能力
2. 方法要点：利用语义2D高斯泼溅提取对象中心、域不变的空间特征，通过特征级高斯泼溅构建统一3D表示
3. 实验或效果：在ManiSkill仿真环境中评估，结合扩散策略，显著提升现实部署中的任务性能和稳定性

## 📄 摘要（原文）

> Cross-domain transfer in robotic manipulation remains a longstanding challenge due to the significant domain gap between simulated and real-world environments. Existing methods such as domain randomization, adaptation, and sim-real calibration often require extensive tuning or fail to generalize to unseen scenarios. To address this issue, we observe that if domain-invariant features are utilized during policy training in simulation, and the same features can be extracted and provided as the input to policy during real-world deployment, the domain gap can be effectively bridged, leading to significantly improved policy generalization. Accordingly, we propose Semantic 2D Gaussian Splatting (S2GS), a novel representation method that extracts object-centric, domain-invariant spatial features. S2GS constructs multi-view 2D semantic fields and projects them into a unified 3D space via feature-level Gaussian splatting. A semantic filtering mechanism removes irrelevant background content, ensuring clean and consistent inputs for policy learning. To evaluate the effectiveness of S2GS, we adopt Diffusion Policy as the downstream learning algorithm and conduct experiments in the ManiSkill simulation environment, followed by real-world deployment. Results demonstrate that S2GS significantly improves sim-to-real transferability, maintaining high and stable task performance in real-world scenarios.

