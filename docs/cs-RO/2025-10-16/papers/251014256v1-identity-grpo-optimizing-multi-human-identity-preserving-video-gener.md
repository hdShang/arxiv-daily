---
layout: default
title: Identity-GRPO: Optimizing Multi-Human Identity-preserving Video Generation via Reinforcement Learning
---

# Identity-GRPO: Optimizing Multi-Human Identity-preserving Video Generation via Reinforcement Learning

**arXiv**: [2510.14256v1](https://arxiv.org/abs/2510.14256) | [PDF](https://arxiv.org/pdf/2510.14256.pdf)

**作者**: Xiangyu Meng, Zixian Zhang, Zhenghao Zhang, Junchao Liao, Long Qin, Weizhi Wang

---

## 💡 一句话要点

**提出Identity-GRPO以优化多人类身份保持的视频生成**

**关键词**: `视频生成` `身份保持` `强化学习` `多人类一致性` `奖励模型`

## 📋 核心要点

1. 核心问题：现有方法在动态交互中难以保持多人类身份一致性
2. 方法要点：构建视频奖励模型，并采用GRPO变体优化生成策略
3. 实验或效果：在人类一致性指标上比基线方法提升高达18.9%

## 📄 摘要（原文）

> While advanced methods like VACE and Phantom have advanced video generation
> for specific subjects in diverse scenarios, they struggle with multi-human
> identity preservation in dynamic interactions, where consistent identities
> across multiple characters are critical. To address this, we propose
> Identity-GRPO, a human feedback-driven optimization pipeline for refining
> multi-human identity-preserving video generation. First, we construct a video
> reward model trained on a large-scale preference dataset containing
> human-annotated and synthetic distortion data, with pairwise annotations
> focused on maintaining human consistency throughout the video. We then employ a
> GRPO variant tailored for multi-human consistency, which greatly enhances both
> VACE and Phantom. Through extensive ablation studies, we evaluate the impact of
> annotation quality and design choices on policy optimization. Experiments show
> that Identity-GRPO achieves up to 18.9% improvement in human consistency
> metrics over baseline methods, offering actionable insights for aligning
> reinforcement learning with personalized video generation.

