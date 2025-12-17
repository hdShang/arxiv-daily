---
layout: default
title: Ensembling Pruned Attention Heads For Uncertainty-Aware Efficient Transformers
---

# Ensembling Pruned Attention Heads For Uncertainty-Aware Efficient Transformers

**arXiv**: [2510.18358v1](https://arxiv.org/abs/2510.18358) | [PDF](https://arxiv.org/pdf/2510.18358.pdf)

**作者**: Firas Gabetni, Giuseppe Curci, Andrea Pilzer, Subhankar Roy, Elisa Ricci, Gianni Franchi

---

## 💡 一句话要点

**提出Hydra Ensembles以高效实现不确定性量化，适用于安全关键场景。**

**关键词**: `不确定性量化` `注意力头剪枝` `高效集成` `Transformer模型` `零样本分类`

## 📋 核心要点

1. 核心问题：深度集成方法计算和内存成本高，难以扩展到大型模型。
2. 方法要点：通过剪枝注意力头创建多样成员，并使用分组全连接层合并。
3. 实验或效果：在图像和文本分类任务中，性能匹配或超越Deep Ensembles，推理速度接近单网络。

## 📄 摘要（原文）

> Uncertainty quantification (UQ) is essential for deploying deep neural
> networks in safety-critical settings. Although methods like Deep Ensembles
> achieve strong UQ performance, their high computational and memory costs hinder
> scalability to large models. We introduce Hydra Ensembles, an efficient
> transformer-based ensemble that prunes attention heads to create diverse
> members and merges them via a new multi-head attention with grouped
> fully-connected layers. This yields a compact model with inference speed close
> to a single network, matching or surpassing Deep Ensembles in UQ performance
> without retraining from scratch. We also provide an in-depth analysis of
> pruning, showing that naive approaches can harm calibration, whereas Hydra
> Ensembles preserves robust uncertainty. Experiments on image and text
> classification tasks, with various architectures, show consistent gains over
> Deep Ensembles. Remarkably, in zero-shot classification on ImageNet-1k, our
> approach surpasses state of the art methods, even without requiring additional
> training.

