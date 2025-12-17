---
layout: default
title: Perfect Prediction or Plenty of Proposals? What Matters Most in Planning for Autonomous Driving
---

# Perfect Prediction or Plenty of Proposals? What Matters Most in Planning for Autonomous Driving

**arXiv**: [2510.15505v1](https://arxiv.org/abs/2510.15505) | [PDF](https://arxiv.org/pdf/2510.15505.pdf)

**作者**: Aron Distelzweig, Faris Janjoš, Oliver Scheel, Sirish Reddy Varra, Raghu Rajan, Joschka Boedecker

---

## 💡 一句话要点

**提出以高质量提案生成为核心的集成预测与规划方法，提升自动驾驶在交互场景中的性能**

**关键词**: `自动驾驶规划` `集成预测与规划` `提案生成` `交互场景` `模仿学习` `基准测试`

## 📋 核心要点

1. 核心问题：集成预测与规划方法中，预测信息未充分改善规划性能，尤其在交互场景。
2. 方法要点：基于PDM增强提案生成，强调多样、真实且高质量的提案，预测主要用于碰撞检查。
3. 实验或效果：在交互和分布外场景中，该方法显著优于现有方法，达到新SOTA。

## 📄 摘要（原文）

> Traditionally, prediction and planning in autonomous driving (AD) have been
> treated as separate, sequential modules. Recently, there has been a growing
> shift towards tighter integration of these components, known as Integrated
> Prediction and Planning (IPP), with the aim of enabling more informed and
> adaptive decision-making. However, it remains unclear to what extent this
> integration actually improves planning performance. In this work, we
> investigate the role of prediction in IPP approaches, drawing on the widely
> adopted Val14 benchmark, which encompasses more common driving scenarios with
> relatively low interaction complexity, and the interPlan benchmark, which
> includes highly interactive and out-of-distribution driving situations. Our
> analysis reveals that even access to perfect future predictions does not lead
> to better planning outcomes, indicating that current IPP methods often fail to
> fully exploit future behavior information. Instead, we focus on high-quality
> proposal generation, while using predictions primarily for collision checks. We
> find that many imitation learning-based planners struggle to generate realistic
> and plausible proposals, performing worse than PDM - a simple lane-following
> approach. Motivated by this observation, we build on PDM with an enhanced
> proposal generation method, shifting the emphasis towards producing diverse but
> realistic and high-quality proposals. This proposal-centric approach
> significantly outperforms existing methods, especially in out-of-distribution
> and highly interactive settings, where it sets new state-of-the-art results.

