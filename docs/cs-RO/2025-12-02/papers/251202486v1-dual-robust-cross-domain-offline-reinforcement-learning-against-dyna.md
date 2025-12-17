---
layout: default
title: Dual-Robust Cross-Domain Offline Reinforcement Learning Against Dynamics Shifts
---

# Dual-Robust Cross-Domain Offline Reinforcement Learning Against Dynamics Shifts

**arXiv**: [2512.02486v1](https://arxiv.org/abs/2512.02486) | [PDF](https://arxiv.org/pdf/2512.02486.pdf)

**作者**: Zhongjian Qiao, Rui Yang, Jiafei Lyu, Xiu Li, Zhongxiang Dai, Zhuoran Yang, Siyang Gao, Shuang Qiu

---

## 💡 一句话要点

**提出DROCO算法以增强跨域离线强化学习在训练和测试时对动态偏移的双重鲁棒性。**

**关键词**: `跨域离线强化学习` `动态偏移鲁棒性` `鲁棒Bellman算子` `双重鲁棒算法` `离线策略优化`

## 📋 核心要点

1. 核心问题：跨域离线强化学习现有方法主要关注训练时鲁棒性，忽略测试时动态扰动导致的策略脆弱性。
2. 方法要点：引入鲁棒跨域Bellman算子，结合动态值惩罚和Huber损失，确保双重鲁棒性。
3. 实验或效果：在多种动态偏移场景下，DROCO优于基线方法，展现出增强的鲁棒性。

## 📄 摘要（原文）

> Single-domain offline reinforcement learning (RL) often suffers from limited data coverage, while cross-domain offline RL handles this issue by leveraging additional data from other domains with dynamics shifts. However, existing studies primarily focus on train-time robustness (handling dynamics shifts from training data), neglecting the test-time robustness against dynamics perturbations when deployed in practical scenarios. In this paper, we investigate dual (both train-time and test-time) robustness against dynamics shifts in cross-domain offline RL. We first empirically show that the policy trained with cross-domain offline RL exhibits fragility under dynamics perturbations during evaluation, particularly when target domain data is limited. To address this, we introduce a novel robust cross-domain Bellman (RCB) operator, which enhances test-time robustness against dynamics perturbations while staying conservative to the out-of-distribution dynamics transitions, thus guaranteeing the train-time robustness. To further counteract potential value overestimation or underestimation caused by the RCB operator, we introduce two techniques, the dynamic value penalty and the Huber loss, into our framework, resulting in the practical \textbf{D}ual-\textbf{RO}bust \textbf{C}ross-domain \textbf{O}ffline RL (DROCO) algorithm. Extensive empirical results across various dynamics shift scenarios show that DROCO outperforms strong baselines and exhibits enhanced robustness to dynamics perturbations.

