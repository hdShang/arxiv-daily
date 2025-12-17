---
layout: default
title: Ponimator: Unfolding Interactive Pose for Versatile Human-human Interaction Animation
---

# Ponimator: Unfolding Interactive Pose for Versatile Human-human Interaction Animation

**arXiv**: [2510.14976v1](https://arxiv.org/abs/2510.14976) | [PDF](https://arxiv.org/pdf/2510.14976.pdf)

**作者**: Shaowei Liu, Chuan Guo, Bing Zhou, Jian Wang

---

## 💡 一句话要点

**提出Ponimator框架，基于近距交互姿态实现多样化人-人交互动画**

**关键词**: `人-人交互动画` `条件扩散模型` `姿态先验` `运动生成` `文本到交互合成`

## 📋 核心要点

1. 核心问题：如何从近距人-人交互姿态推断和生成动态交互动画
2. 方法要点：使用两个条件扩散模型，分别处理时空先验生成运动和姿态
3. 实验效果：在多个数据集验证框架通用性、有效性和鲁棒性

## 📄 摘要（原文）

> Close-proximity human-human interactive poses convey rich contextual
> information about interaction dynamics. Given such poses, humans can
> intuitively infer the context and anticipate possible past and future dynamics,
> drawing on strong priors of human behavior. Inspired by this observation, we
> propose Ponimator, a simple framework anchored on proximal interactive poses
> for versatile interaction animation. Our training data consists of
> close-contact two-person poses and their surrounding temporal context from
> motion-capture interaction datasets. Leveraging interactive pose priors,
> Ponimator employs two conditional diffusion models: (1) a pose animator that
> uses the temporal prior to generate dynamic motion sequences from interactive
> poses, and (2) a pose generator that applies the spatial prior to synthesize
> interactive poses from a single pose, text, or both when interactive poses are
> unavailable. Collectively, Ponimator supports diverse tasks, including
> image-based interaction animation, reaction animation, and text-to-interaction
> synthesis, facilitating the transfer of interaction knowledge from high-quality
> mocap data to open-world scenarios. Empirical experiments across diverse
> datasets and applications demonstrate the universality of the pose prior and
> the effectiveness and robustness of our framework.

