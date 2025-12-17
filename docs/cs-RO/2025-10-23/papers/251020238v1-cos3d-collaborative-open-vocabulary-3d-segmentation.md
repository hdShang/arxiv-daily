---
layout: default
title: COS3D: Collaborative Open-Vocabulary 3D Segmentation
---

# COS3D: Collaborative Open-Vocabulary 3D Segmentation

**arXiv**: [2510.20238v1](https://arxiv.org/abs/2510.20238) | [PDF](https://arxiv.org/pdf/2510.20238.pdf)

**作者**: Runsong Zhu, Ka-Hei Hui, Zhengzhe Liu, Qianyi Wu, Weiliang Tang, Shi Qiu, Pheng-Ann Heng, Chi-Wing Fu

---

## 💡 一句话要点

**提出COS3D协作框架以解决开放词汇3D分割中的语言与分割融合问题**

**关键词**: `开放词汇3D分割` `协作场` `实例场` `语言场` `两阶段训练` `自适应提示优化`

## 📋 核心要点

1. 核心问题：现有方法依赖单一语言场或预计算分割，导致分割质量差和误差累积。
2. 方法要点：引入协作场概念，结合实例场和语言场，通过特征映射和两阶段训练优化。
3. 实验或效果：在多个基准测试中表现领先，支持图像分割、层次分割和机器人应用。

## 📄 摘要（原文）

> Open-vocabulary 3D segmentation is a fundamental yet challenging task,
> requiring a mutual understanding of both segmentation and language. However,
> existing Gaussian-splatting-based methods rely either on a single 3D language
> field, leading to inferior segmentation, or on pre-computed class-agnostic
> segmentations, suffering from error accumulation. To address these limitations,
> we present COS3D, a new collaborative prompt-segmentation framework that
> contributes to effectively integrating complementary language and segmentation
> cues throughout its entire pipeline. We first introduce the new concept of
> collaborative field, comprising an instance field and a language field, as the
> cornerstone for collaboration. During training, to effectively construct the
> collaborative field, our key idea is to capture the intrinsic relationship
> between the instance field and language field, through a novel
> instance-to-language feature mapping and designing an efficient two-stage
> training strategy. During inference, to bridge distinct characteristics of the
> two fields, we further design an adaptive language-to-instance prompt
> refinement, promoting high-quality prompt-segmentation inference. Extensive
> experiments not only demonstrate COS3D's leading performance over existing
> methods on two widely-used benchmarks but also show its high potential to
> various applications,~\ie, novel image-based 3D segmentation, hierarchical
> segmentation, and robotics. The code is publicly available at
> \href{https://github.com/Runsong123/COS3D}{https://github.com/Runsong123/COS3D}.

