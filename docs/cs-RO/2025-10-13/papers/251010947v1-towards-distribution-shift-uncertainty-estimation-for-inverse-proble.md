---
layout: default
title: Towards Distribution-Shift Uncertainty Estimation for Inverse Problems with Generative Priors
---

# Towards Distribution-Shift Uncertainty Estimation for Inverse Problems with Generative Priors

**arXiv**: [2510.10947v1](https://arxiv.org/abs/2510.10947) | [PDF](https://arxiv.org/pdf/2510.10947.pdf)

**作者**: Namhoon Kim, Sara Fridovich-Keil

---

## 💡 一句话要点

**提出基于重构稳定性的分布偏移不确定性指标，用于生成先验逆问题**

**关键词**: `逆问题` `生成先验` `分布偏移检测` `不确定性估计` `重构稳定性` `计算成像`

## 📋 核心要点

1. 生成先逆问题中，测试图像分布偏移易致幻觉，现有方法需校准或非统计估计
2. 利用重构稳定性作为代理指标，无需训练分布知识或重训练，检测分布偏移
3. 在MNIST断层重建实验中，OOD数字重构变异性高，验证指标有效性

## 📄 摘要（原文）

> Generative models have shown strong potential as data-driven priors for
> solving inverse problems such as reconstructing medical images from
> undersampled measurements. While these priors improve reconstruction quality
> with fewer measurements, they risk hallucinating features when test images lie
> outside the training distribution. Existing uncertainty quantification methods
> in this setting (i) require an in-distribution calibration dataset, which may
> not be available, (ii) provide heuristic rather than statistical estimates, or
> (iii) quantify uncertainty from model capacity or limited measurements rather
> than distribution shift. We propose an instance-level, calibration-free
> uncertainty indicator that is sensitive to distribution shift, requires no
> knowledge of the training distribution, and incurs no retraining cost. Our key
> hypothesis is that reconstructions of in-distribution images remain stable
> under random measurement variations, while reconstructions of
> out-of-distribution (OOD) images exhibit greater instability. We use this
> stability as a proxy for detecting distribution shift. Our proposed OOD
> indicator is efficiently computable for any computational imaging inverse
> problem; we demonstrate it on tomographic reconstruction of MNIST digits, where
> a learned proximal network trained only on digit "0" is evaluated on all ten
> digits. Reconstructions of OOD digits show higher variability and
> correspondingly higher reconstruction error, validating this indicator. These
> results suggest a deployment strategy that pairs generative priors with
> lightweight guardrails, enabling aggressive measurement reduction for
> in-distribution cases while automatically warning when priors are applied out
> of distribution.

