---
layout: default
title: DeshadowMamba: Deshadowing as 1D Sequential Similarity
---

# DeshadowMamba: Deshadowing as 1D Sequential Similarity

**arXiv**: [2510.24260v1](https://arxiv.org/abs/2510.24260) | [PDF](https://arxiv.org/pdf/2510.24260.pdf)

**作者**: Zhaotong Yang, Yi Chen, Yanying Li, Shengfeng He, Yangyang Xu, Junyu Dong, Jian Yang, Yong Du

---

## 💡 一句话要点

**提出DeshadowMamba以解决图像阴影去除中的结构扭曲和颜色不一致问题**

**关键词**: `图像阴影去除` `序列建模` `选择性状态空间模型` `对比学习` `颜色恢复`

## 📋 核心要点

1. 核心问题：现有注意力模型在阴影去除中混合无关区域光照线索，导致结构扭曲和颜色不一致
2. 方法要点：引入CrossGate机制和ColorShift正则化，结合Mamba模型实现阴影感知的序列建模
3. 实验或效果：在公共基准测试中达到最先进的视觉质量和强定量性能

## 📄 摘要（原文）

> Recent deep models for image shadow removal often rely on attention-based
> architectures to capture long-range dependencies. However, their fixed
> attention patterns tend to mix illumination cues from irrelevant regions,
> leading to distorted structures and inconsistent colors. In this work, we
> revisit shadow removal from a sequence modeling perspective and explore the use
> of Mamba, a selective state space model that propagates global context through
> directional state transitions. These transitions yield an efficient global
> receptive field while preserving positional continuity. Despite its potential,
> directly applying Mamba to image data is suboptimal, since it lacks awareness
> of shadow-non-shadow semantics and remains susceptible to color interference
> from nearby regions. To address these limitations, we propose CrossGate, a
> directional modulation mechanism that injects shadow-aware similarity into
> Mamba's input gate, allowing selective integration of relevant context along
> transition axes. To further ensure appearance fidelity, we introduce ColorShift
> regularization, a contrastive learning objective driven by global color
> statistics. By synthesizing structured informative negatives, it guides the
> model to suppress color contamination and achieve robust color restoration.
> Together, these components adapt sequence modeling to the structural integrity
> and chromatic consistency required for shadow removal. Extensive experiments on
> public benchmarks demonstrate that DeshadowMamba achieves state-of-the-art
> visual quality and strong quantitative performance.

