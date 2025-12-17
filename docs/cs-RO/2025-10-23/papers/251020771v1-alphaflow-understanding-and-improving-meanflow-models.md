---
layout: default
title: AlphaFlow: Understanding and Improving MeanFlow Models
---

# AlphaFlow: Understanding and Improving MeanFlow Models

**arXiv**: [2510.20771v1](https://arxiv.org/abs/2510.20771) | [PDF](https://arxiv.org/pdf/2510.20771.pdf)

**作者**: Huijie Zhang, Aliaksandr Siarohin, Willi Menapace, Michael Vasilkovsky, Sergey Tulyakov, Qing Qu, Ivan Skorokhodov

---

## 💡 一句话要点

**提出α-Flow以解决MeanFlow优化冲突，提升少步生成模型性能**

**关键词**: `少步生成建模` `流匹配` `优化冲突` `课程学习` `图像生成`

## 📋 核心要点

1. MeanFlow目标分解为轨迹流匹配和一致性，梯度分析显示负相关导致优化冲突
2. 引入α-Flow统一多种目标，采用课程策略平滑过渡以解耦冲突目标
3. 在ImageNet-1K 256x256上，α-Flow-XL/2+模型使用DiT骨干取得SOTA FID分数

## 📄 摘要（原文）

> MeanFlow has recently emerged as a powerful framework for few-step generative
> modeling trained from scratch, but its success is not yet fully understood. In
> this work, we show that the MeanFlow objective naturally decomposes into two
> parts: trajectory flow matching and trajectory consistency. Through gradient
> analysis, we find that these terms are strongly negatively correlated, causing
> optimization conflict and slow convergence. Motivated by these insights, we
> introduce $\alpha$-Flow, a broad family of objectives that unifies trajectory
> flow matching, Shortcut Model, and MeanFlow under one formulation. By adopting
> a curriculum strategy that smoothly anneals from trajectory flow matching to
> MeanFlow, $\alpha$-Flow disentangles the conflicting objectives, and achieves
> better convergence. When trained from scratch on class-conditional ImageNet-1K
> 256x256 with vanilla DiT backbones, $\alpha$-Flow consistently outperforms
> MeanFlow across scales and settings. Our largest $\alpha$-Flow-XL/2+ model
> achieves new state-of-the-art results using vanilla DiT backbones, with FID
> scores of 2.58 (1-NFE) and 2.15 (2-NFE).

