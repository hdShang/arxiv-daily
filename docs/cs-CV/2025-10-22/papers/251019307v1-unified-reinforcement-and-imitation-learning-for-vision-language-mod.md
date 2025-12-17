---
layout: default
title: Unified Reinforcement and Imitation Learning for Vision-Language Models
---

# Unified Reinforcement and Imitation Learning for Vision-Language Models

**arXiv**: [2510.19307v1](https://arxiv.org/abs/2510.19307) | [PDF](https://arxiv.org/pdf/2510.19307.pdf)

**作者**: Byung-Kwan Lee, Ryo Hachiuma, Yong Man Ro, Yu-Chiang Frank Wang, Yueh-Hua Wu

---

## 💡 一句话要点

**提出统一强化与模仿学习算法，以高效训练轻量级视觉语言模型。**

**关键词**: `视觉语言模型` `强化学习` `模仿学习` `模型蒸馏` `轻量级模型` `对抗训练`

## 📋 核心要点

1. 视觉语言模型规模大，在资源受限环境中不实用。
2. 结合强化学习和对抗模仿学习，提升学生模型生成能力。
3. 实验显示，RIL在多个基准上缩小与先进模型的性能差距。

## 📄 摘要（原文）

> Vision-Language Models (VLMs) have achieved remarkable progress, yet their
> large scale often renders them impractical for resource-constrained
> environments. This paper introduces Unified Reinforcement and Imitation
> Learning (RIL), a novel and efficient training algorithm designed to create
> powerful, lightweight VLMs. RIL distinctively combines the strengths of
> reinforcement learning with adversarial imitation learning. This enables
> smaller student VLMs not only to mimic the sophisticated text generation of
> large teacher models but also to systematically improve their generative
> capabilities through reinforcement signals. Key to our imitation framework is
> an LLM-based discriminator that adeptly distinguishes between student and
> teacher outputs, complemented by guidance from multiple large teacher VLMs to
> ensure diverse learning. This unified learning strategy, leveraging both
> reinforcement and imitation, empowers student models to achieve significant
> performance gains, making them competitive with leading closed-source VLMs.
> Extensive experiments on diverse vision-language benchmarks demonstrate that
> RIL significantly narrows the performance gap with state-of-the-art open- and
> closed-source VLMs and, in several instances, surpasses them.

