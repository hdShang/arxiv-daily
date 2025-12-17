---
layout: default
title: Evaluating Video Models as Simulators of Multi-Person Pedestrian Trajectories
---

# Evaluating Video Models as Simulators of Multi-Person Pedestrian Trajectories

**arXiv**: [2510.20182v1](https://arxiv.org/abs/2510.20182) | [PDF](https://arxiv.org/pdf/2510.20182.pdf)

**作者**: Aaron Appelle, Jerome P. Lynch

---

## 💡 一句话要点

**提出评估协议以验证视频模型作为多行人轨迹模拟器的能力**

**关键词**: `视频生成模型` `多行人轨迹` `评估协议` `鸟瞰图重建` `文本到视频` `图像到视频`

## 📋 核心要点

1. 核心问题：现有视频生成模型在多智能体交互动态方面的合理性未经验证
2. 方法要点：开发文本到视频和图像到视频的评估协议，包括轨迹重建方法
3. 实验或效果：分析显示模型学习到有效先验，但存在合并和消失等失败模式

## 📄 摘要（原文）

> Large-scale video generation models have demonstrated high visual realism in
> diverse contexts, spurring interest in their potential as general-purpose world
> simulators. Existing benchmarks focus on individual subjects rather than scenes
> with multiple interacting people. However, the plausibility of multi-agent
> dynamics in generated videos remains unverified. We propose a rigorous
> evaluation protocol to benchmark text-to-video (T2V) and image-to-video (I2V)
> models as implicit simulators of pedestrian dynamics. For I2V, we leverage
> start frames from established datasets to enable comparison with a ground truth
> video dataset. For T2V, we develop a prompt suite to explore diverse pedestrian
> densities and interactions. A key component is a method to reconstruct 2D
> bird's-eye view trajectories from pixel-space without known camera parameters.
> Our analysis reveals that leading models have learned surprisingly effective
> priors for plausible multi-agent behavior. However, failure modes like merging
> and disappearing people highlight areas for future improvement.

