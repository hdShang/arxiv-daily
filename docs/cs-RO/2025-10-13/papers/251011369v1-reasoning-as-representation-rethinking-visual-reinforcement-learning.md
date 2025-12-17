---
layout: default
title: Reasoning as Representation: Rethinking Visual Reinforcement Learning in Image Quality Assessment
---

# Reasoning as Representation: Rethinking Visual Reinforcement Learning in Image Quality Assessment

**arXiv**: [2510.11369v1](https://arxiv.org/abs/2510.11369) | [PDF](https://arxiv.org/pdf/2510.11369.pdf)

**作者**: Shijie Zhao, Xuanyu Zhang, Weiqi Li, Junlin Li, Li Zhang, Tianfan Xue, Jian Zhang

---

## 💡 一句话要点

**提出RALI算法，通过对比学习对齐图像与文本表示，提升图像质量评估的泛化与效率。**

**关键词**: `图像质量评估` `强化学习` `对比学习` `多模态表示对齐` `模型泛化` `推理效率优化`

## 📋 核心要点

1. 基于推理的IQA模型泛化强但机制不明，且推理能耗高限制部署。
2. RL训练使MLLMs将冗余视觉表示转为紧凑文本表示，驱动泛化。
3. RALI无需推理过程，参数与时间减少95%，泛化性能媲美推理模型。

## 📄 摘要（原文）

> Reasoning-based image quality assessment (IQA) models trained through
> reinforcement learning (RL) exhibit exceptional generalization, yet the
> underlying mechanisms and critical factors driving this capability remain
> underexplored in current research. Moreover, despite their superior
> performance, these models incur inference energy usage and latency orders of
> magnitude higher than their earlier counterparts, restricting their deployment
> in specific scenarios. Through extensive experiments, this paper verifies and
> elaborates that through RL training, MLLMs leverage their reasoning capability
> to convert redundant visual representations into compact, cross-domain aligned
> text representations. This conversion is precisely the source of the
> generalization exhibited by these reasoning-based IQA models. Building on this
> fundamental insight, we propose a novel algorithm, RALI, which employs
> contrastive learning to directly align images with these generalizable text
> representations learned by RL. This approach eliminates the reliance on
> reasoning processes and even obviates the need to load an LLM. For the quality
> scoring task, this framework achieves generalization performance comparable to
> reasoning-based models while requiring less than 5% of their model parameters
> and inference time.

