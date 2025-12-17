---
layout: default
title: Revisiting Reconstruction-based AI-generated Image Detection: A Geometric Perspective
---

# Revisiting Reconstruction-based AI-generated Image Detection: A Geometric Perspective

**arXiv**: [2510.25141v1](https://arxiv.org/abs/2510.25141) | [PDF](https://arxiv.org/pdf/2510.25141.pdf)

**作者**: Wan Jiang, Jing Yan, Ruixuan Zhang, Xiaojing Chen, Changtao Miao, Zhe Li, Chenhao Lin, Yunfeng Diao, Richang Hong

---

## 💡 一句话要点

**提出ReGap方法以提升AI生成图像检测的准确性和鲁棒性**

**关键词**: `AI生成图像检测` `重建误差` `几何视角` `动态误差计算` `训练无关方法` `鲁棒性`

## 📋 核心要点

1. 现有重建方法缺乏理论依据，依赖经验启发，导致可解释性和可靠性不足
2. 从几何视角引入Jacobian谱下界，提出动态重建误差计算，通过编辑操作增强误差分离
3. 实验显示ReGap优于基线，对后处理操作鲁棒，并在多样条件下泛化良好

## 📄 摘要（原文）

> The rise of generative Artificial Intelligence (AI) has made detecting
> AI-generated images a critical challenge for ensuring authenticity. Existing
> reconstruction-based methods lack theoretical foundations and on empirical
> heuristics, limiting interpretability and reliability. In this paper, we
> introduce the Jacobian-Spectral Lower Bound for reconstruction error from a
> geometric perspective, showing that real images off the reconstruction manifold
> exhibit a non-trivial error lower bound, while generated images on the manifold
> have near-zero error. Furthermore, we reveal the limitations of existing
> methods that rely on static reconstruction error from a single pass. These
> methods often fail when some real images exhibit lower error than generated
> ones. This counterintuitive behavior reduces detection accuracy and requires
> data-specific threshold tuning, limiting their applicability in real-world
> scenarios. To address these challenges, we propose ReGap, a training-free
> method that computes dynamic reconstruction error by leveraging structured
> editing operations to introduce controlled perturbations. This enables
> measuring error changes before and after editing, improving detection accuracy
> by enhancing error separation. Experimental results show that our method
> outperforms existing baselines, exhibits robustness to common post-processing
> operations and generalizes effectively across diverse conditions.

