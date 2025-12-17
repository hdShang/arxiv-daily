---
layout: default
title: Failure Prediction at Runtime for Generative Robot Policies
---

# Failure Prediction at Runtime for Generative Robot Policies

**arXiv**: [2510.09459v1](https://arxiv.org/abs/2510.09459) | [PDF](https://arxiv.org/pdf/2510.09459.pdf)

**作者**: Ralf Römer, Adrian Kobras, Luca Worbis, Angela P. Schoellig

---

## 💡 一句话要点

**提出FIPER框架以预测生成式机器人策略的运行时失败**

**关键词**: `失败预测` `生成式模仿学习` `保形预测` `动作不确定性` `机器人安全`

## 📋 核心要点

1. 核心问题：生成式模仿学习在未知环境或动作误差下易导致任务失败，需早期预测
2. 方法要点：通过OOD检测和动作块熵评估失败指标，并利用保形预测校准阈值
3. 实验或效果：在多种仿真和真实环境中，FIPER比现有方法更准确、更早预测失败

## 📄 摘要（原文）

> Imitation learning (IL) with generative models, such as diffusion and flow
> matching, has enabled robots to perform complex, long-horizon tasks. However,
> distribution shifts from unseen environments or compounding action errors can
> still cause unpredictable and unsafe behavior, leading to task failure. Early
> failure prediction during runtime is therefore essential for deploying robots
> in human-centered and safety-critical environments. We propose FIPER, a general
> framework for Failure Prediction at Runtime for generative IL policies that
> does not require failure data. FIPER identifies two key indicators of impending
> failure: (i) out-of-distribution (OOD) observations detected via random network
> distillation in the policy's embedding space, and (ii) high uncertainty in
> generated actions measured by a novel action-chunk entropy score. Both failure
> prediction scores are calibrated using a small set of successful rollouts via
> conformal prediction. A failure alarm is triggered when both indicators,
> aggregated over short time windows, exceed their thresholds. We evaluate FIPER
> across five simulation and real-world environments involving diverse failure
> modes. Our results demonstrate that FIPER better distinguishes actual failures
> from benign OOD situations and predicts failures more accurately and earlier
> than existing methods. We thus consider this work an important step towards
> more interpretable and safer generative robot policies. Code, data and videos
> are available at https://tum-lsy.github.io/fiper_website.

