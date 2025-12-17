---
layout: default
title: $Δ\mathrm{Energy}$: Optimizing Energy Change During Vision-Language Alignment Improves both OOD Detection and OOD Generalization
---

# $Δ\mathrm{Energy}$: Optimizing Energy Change During Vision-Language Alignment Improves both OOD Detection and OOD Generalization

**arXiv**: [2510.11296v1](https://arxiv.org/abs/2510.11296) | [PDF](https://arxiv.org/pdf/2510.11296.pdf)

**作者**: Lin Zhu, Yifeng Yang, Xinbing Wang, Qinying Gu, Nanyang Ye

---

## 💡 一句话要点

**提出ΔEnergy优化能量变化，提升视觉语言模型的OOD检测与泛化能力**

**关键词**: `视觉语言模型` `分布外检测` `能量优化` `泛化能力` `微调框架` `Hessian一致性`

## 📋 核心要点

1. 核心问题：视觉语言模型在真实任务中面临分布外数据，需改进泛化与检测能力
2. 方法要点：引入ΔEnergy作为OOD分数，通过能量变化优化和EBM框架统一微调
3. 实验或效果：在OOD检测和泛化基准上，AUROC提升10%至25%，优于现有方法

## 📄 摘要（原文）

> Recent approaches for vision-language models (VLMs) have shown remarkable
> success in achieving fast downstream adaptation. When applied to real-world
> downstream tasks, VLMs inevitably encounter both the in-distribution (ID) data
> and out-of-distribution (OOD) data. The OOD datasets often include both
> covariate shifts (e.g., known classes with changes in image styles) and
> semantic shifts (e.g., test-time unseen classes). This highlights the
> importance of improving VLMs' generalization ability to covariate-shifted OOD
> data, while effectively detecting open-set semantic-shifted OOD classes. In
> this paper, inspired by the substantial energy change observed in closed-set
> data when re-aligning vision-language modalities (specifically by directly
> reducing the maximum cosine similarity to a low value), we introduce a novel
> OOD score, named {\Delta}Energy. {\Delta}Energy significantly outperforms the
> vanilla energy-based OOD score and provides a more reliable approach for OOD
> detection. Furthermore, {\Delta}Energy can simultaneously improve OOD
> generalization under covariate shifts, which is achieved by lower-bound
> maximization for {\Delta}Energy (termed EBM). EBM is theoretically proven to
> not only enhance OOD detection but also yields a domain-consistent Hessian,
> which serves as a strong indicator for OOD generalization. Based on this
> finding, we developed a unified fine-tuning framework that allows for improving
> VLMs' robustness in both OOD generalization and OOD detection. Extensive
> experiments on challenging OOD detection and generalization benchmarks
> demonstrate the superiority of our method, outperforming recent approaches by
> 10% to 25% in AUROC.

