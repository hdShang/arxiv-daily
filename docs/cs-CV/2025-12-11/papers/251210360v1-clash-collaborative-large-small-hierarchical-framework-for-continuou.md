---
layout: default
title: CLASH: Collaborative Large-Small Hierarchical Framework for Continuous Vision-and-Language Navigation
---

# CLASH: Collaborative Large-Small Hierarchical Framework for Continuous Vision-and-Language Navigation

**arXiv**: [2512.10360v1](https://arxiv.org/abs/2512.10360) | [PDF](https://arxiv.org/pdf/2512.10360.pdf)

**作者**: Liuyi Wang, Zongtao He, Jinlong Li, Xiaoyan Qi, Mengxian Hu, Chenpeng Yao, Chengju Liu, Qijun Chen

---

## 💡 一句话要点

**提出CLASH框架以解决视觉语言导航中大型模型与小型模型协作问题**

**关键词**: `视觉语言导航` `模型协作` `不确定性融合` `全景视觉提示` `链式思维推理` `实时部署`

## 📋 核心要点

1. 核心问题：视觉语言导航中大型模型推理能力强但任务性能不足，小型模型任务表现好但泛化有限。
2. 方法要点：结合反应式小型模型规划器与反思式大型模型推理器，通过不确定性感知协作机制自适应融合决策。
3. 实验或效果：在VLN-CE排行榜上取得最佳结果，真实世界实验验证了鲁棒性和有效性。

## 📄 摘要（原文）

> Vision-and-Language Navigation (VLN) requires robots to follow natural language instructions and navigate complex environments without prior maps. While recent vision-language large models demonstrate strong reasoning abilities, they often underperform task-specific panoramic small models in VLN tasks. To address this, we propose CLASH (Collaborative Large-Small Hierarchy), a VLN-CE framework that integrates a reactive small-model planner (RSMP) with a reflective large-model reasoner (RLMR). RSMP adopts a causal-learning-based dual-branch architecture to enhance generalization, while RLMR leverages panoramic visual prompting with chain-of-thought reasoning to support interpretable spatial understanding and navigation. We further introduce an uncertainty-aware collaboration mechanism (UCM) that adaptively fuses decisions from both models. For obstacle avoidance, in simulation, we replace the rule-based controller with a fully learnable point-goal policy, and in real-world deployment, we design a LiDAR-based clustering module for generating navigable waypoints and pair it with an online SLAM-based local controller. CLASH achieves state-of-the-art (SoTA) results (ranking 1-st) on the VLN-CE leaderboard, significantly improving SR and SPL on the test-unseen set over the previous SoTA methods. Real-world experiments demonstrate CLASH's strong robustness, validating its effectiveness in both simulation and deployment scenarios.

