---
layout: default
title: SteeringTTA: Guiding Diffusion Trajectories for Robust Test-Time-Adaptation
---

# SteeringTTA: Guiding Diffusion Trajectories for Robust Test-Time-Adaptation

**arXiv**: [2510.14634v1](https://arxiv.org/abs/2510.14634) | [PDF](https://arxiv.org/pdf/2510.14634.pdf)

**作者**: Jihyun Yu, Yoojin Oh, Wonho Bae, Mingyu Kim, Junhyug Noh

---

## 💡 一句话要点

**提出SteeringTTA以通过引导扩散轨迹提升测试时适应在分布偏移下的鲁棒性**

**关键词**: `测试时适应` `扩散模型` `分布偏移` `伪标签` `Feynman-Kac引导` `图像分类`

## 📋 核心要点

1. 核心问题：基于梯度的扩散TTA方法探索受限，影响跨失真类型的泛化能力。
2. 方法要点：采用Feynman-Kac引导，结合伪标签奖励和多粒子轨迹平衡探索与置信度。
3. 实验或效果：在ImageNet-C上无需模型更新或源数据，性能优于基线。

## 📄 摘要（原文）

> Test-time adaptation (TTA) aims to correct performance degradation of deep
> models under distribution shifts by updating models or inputs using unlabeled
> test data. Input-only diffusion-based TTA methods improve robustness for
> classification to corruptions but rely on gradient guidance, limiting
> exploration and generalization across distortion types. We propose SteeringTTA,
> an inference-only framework that adapts Feynman-Kac steering to guide
> diffusion-based input adaptation for classification with rewards driven by
> pseudo-label. SteeringTTA maintains multiple particle trajectories, steered by
> a combination of cumulative top-K probabilities and an entropy schedule, to
> balance exploration and confidence. On ImageNet-C, SteeringTTA consistently
> outperforms the baseline without any model updates or source data.

