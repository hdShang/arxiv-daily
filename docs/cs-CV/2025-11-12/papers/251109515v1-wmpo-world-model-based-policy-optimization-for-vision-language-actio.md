---
layout: default
title: WMPO: World Model-based Policy Optimization for Vision-Language-Action Models
---

# WMPO: World Model-based Policy Optimization for Vision-Language-Action Models

**arXiv**: [2511.09515v1](https://arxiv.org/abs/2511.09515) | [PDF](https://arxiv.org/pdf/2511.09515.pdf)

**作者**: Fangqi Zhu, Zhengyang Yan, Zicong Hong, Quanxin Shou, Xiao Ma, Song Guo

---

## 💡 一句话要点

**提出WMPO框架，通过像素预测实现无真实环境交互的视觉-语言-动作模型策略优化**

**关键词**: `视觉-语言-动作模型` `世界模型` `策略优化` `样本效率` `机器人操作`

## 📋 核心要点

1. 核心问题：视觉-语言-动作模型依赖专家演示，难以从失败中学习，强化学习样本效率低
2. 方法要点：基于像素预测的世界模型对齐预训练特征，支持在线策略优化
3. 实验或效果：在仿真和真实机器人中提升样本效率、性能，并展现自校正和泛化能力

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models have shown strong potential for general-purpose robotic manipulation, but their reliance on expert demonstrations limits their ability to learn from failures and perform self-corrections. Reinforcement learning (RL) addresses these through self-improving interactions with the physical environment, but suffers from high sample complexity on real robots. We introduce World-Model-based Policy Optimization (WMPO), a principled framework for on-policy VLA RL without interacting with the real environment. In contrast to widely used latent world models, WMPO focuses on pixel-based predictions that align the "imagined" trajectories with the VLA features pretrained with web-scale images. Crucially, WMPO enables the policy to perform on-policy GRPO that provides stronger performance than the often-used off-policy methods. Extensive experiments in both simulation and real-robot settings demonstrate that WMPO (i) substantially improves sample efficiency, (ii) achieves stronger overall performance, (iii) exhibits emergent behaviors such as self-correction, and (iv) demonstrates robust generalization and lifelong learning capabilities.

