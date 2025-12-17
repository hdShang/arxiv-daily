---
layout: default
title: LyTimeT: Towards Robust and Interpretable State-Variable Discovery
---

# LyTimeT: Towards Robust and Interpretable State-Variable Discovery

**arXiv**: [2510.19716v1](https://arxiv.org/abs/2510.19716) | [PDF](https://arxiv.org/pdf/2510.19716.pdf)

**作者**: Kuai Yu, Crystal Su, Xiang Liu, Judah Goldfeder, Mingyuan Shao, Hod Lipson

---

## 💡 一句话要点

**提出LyTimeT框架以从高维视频中提取鲁棒且可解释的动态系统状态变量**

**关键词**: `动态系统建模` `视频预测` `可解释AI` `时空注意力` `稳定性正则化`

## 📋 核心要点

1. 核心问题：高维视频中动态变量提取受背景运动、遮挡和纹理变化等干扰因素影响
2. 方法要点：采用两阶段框架，结合时空注意力编码和Lyapunov稳定性正则化
3. 实验或效果：在合成和真实系统上验证，实现高精度预测和鲁棒性，优于基线方法

## 📄 摘要（原文）

> Extracting the true dynamical variables of a system from high-dimensional
> video is challenging due to distracting visual factors such as background
> motion, occlusions, and texture changes. We propose LyTimeT, a two-phase
> framework for interpretable variable extraction that learns robust and stable
> latent representations of dynamical systems. In Phase 1, LyTimeT employs a
> spatio-temporal TimeSformer-based autoencoder that uses global attention to
> focus on dynamically relevant regions while suppressing nuisance variation,
> enabling distraction-robust latent state learning and accurate long-horizon
> video prediction. In Phase 2, we probe the learned latent space, select the
> most physically meaningful dimensions using linear correlation analysis, and
> refine the transition dynamics with a Lyapunov-based stability regularizer to
> enforce contraction and reduce error accumulation during roll-outs. Experiments
> on five synthetic benchmarks and four real-world dynamical systems, including
> chaotic phenomena, show that LyTimeT achieves mutual information and intrinsic
> dimension estimates closest to ground truth, remains invariant under background
> perturbations, and delivers the lowest analytical mean squared error among
> CNN-based (TIDE) and transformer-only baselines. Our results demonstrate that
> combining spatio-temporal attention with stability constraints yields
> predictive models that are not only accurate but also physically interpretable.

