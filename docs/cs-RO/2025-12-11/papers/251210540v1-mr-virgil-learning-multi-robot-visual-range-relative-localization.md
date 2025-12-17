---
layout: default
title: Mr. Virgil: Learning Multi-robot Visual-range Relative Localization
---

# Mr. Virgil: Learning Multi-robot Visual-range Relative Localization

**arXiv**: [2512.10540v1](https://arxiv.org/abs/2512.10540) | [PDF](https://arxiv.org/pdf/2512.10540.pdf)

**作者**: Si Wang, Zhehan Li, Jiadong Lu, Rong Xiong, Yanjun Cao, Yue Wang

---

## 💡 一句话要点

**提出Mr. Virgil框架，通过图神经网络与可微分位姿图优化解决多机器人视觉-超宽带融合定位中的匹配问题。**

**关键词**: `多机器人定位` `视觉-超宽带融合` `图神经网络` `位姿图优化` `数据关联` `不确定性估计`

## 📋 核心要点

1. 核心问题：多机器人相对定位中，视觉检测与超宽带测距的匹配依赖硬件或调优算法，易产生错误匹配。
2. 方法要点：采用图神经网络进行数据关联，结合可微分位姿图优化后端，提供鲁棒匹配、初始位置预测和不确定性估计。
3. 实验或效果：在模拟和真实场景中，包括遮挡条件，相比传统方法展现出稳定性和准确性提升。

## 📄 摘要（原文）

> Ultra-wideband (UWB)-vision fusion localization has achieved extensive applications in the domain of multi-agent relative localization. The challenging matching problem between robots and visual detection renders existing methods highly dependent on identity-encoded hardware or delicate tuning algorithms. Overconfident yet erroneous matches may bring about irreversible damage to the localization system. To address this issue, we introduce Mr. Virgil, an end-to-end learning multi-robot visual-range relative localization framework, consisting of a graph neural network for data association between UWB rangings and visual detections, and a differentiable pose graph optimization (PGO) back-end. The graph-based front-end supplies robust matching results, accurate initial position predictions, and credible uncertainty estimates, which are subsequently integrated into the PGO back-end to elevate the accuracy of the final pose estimation. Additionally, a decentralized system is implemented for real-world applications. Experiments spanning varying robot numbers, simulation and real-world, occlusion and non-occlusion conditions showcase the stability and exactitude under various scenes compared to conventional methods. Our code is available at: https://github.com/HiOnes/Mr-Virgil.

