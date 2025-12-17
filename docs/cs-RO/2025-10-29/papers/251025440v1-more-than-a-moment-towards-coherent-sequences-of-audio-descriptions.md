---
layout: default
title: More than a Moment: Towards Coherent Sequences of Audio Descriptions
---

# More than a Moment: Towards Coherent Sequences of Audio Descriptions

**arXiv**: [2510.25440v1](https://arxiv.org/abs/2510.25440) | [PDF](https://arxiv.org/pdf/2510.25440.pdf)

**作者**: Eshika Khandelwal, Junyu Xie, Tengda Han, Max Bain, Arsha Nagrani, Andrew Zisserman, Gül Varol, Makarand Tapaswi

---

## 💡 一句话要点

**提出CoherentAD方法以生成连贯的音频描述序列，提升视频无障碍访问。**

**关键词**: `音频描述生成` `序列连贯性` `无障碍技术` `自回归选择` `叙事评估`

## 📋 核心要点

1. 核心问题：自动音频描述方法独立生成描述，导致序列重复且不连贯。
2. 方法要点：训练无关方法，生成候选描述并通过自回归选择构建连贯叙事。
3. 实验或效果：引入StoryRecall指标，方法在叙事理解和减少重复方面优于先前方法。

## 📄 摘要（原文）

> Audio Descriptions (ADs) convey essential on-screen information, allowing
> visually impaired audiences to follow videos. To be effective, ADs must form a
> coherent sequence that helps listeners to visualise the unfolding scene, rather
> than describing isolated moments. However, most automatic methods generate each
> AD independently, often resulting in repetitive, incoherent descriptions. To
> address this, we propose a training-free method, CoherentAD, that first
> generates multiple candidate descriptions for each AD time interval, and then
> performs auto-regressive selection across the sequence to form a coherent and
> informative narrative. To evaluate AD sequences holistically, we introduce a
> sequence-level metric, StoryRecall, which measures how well the predicted ADs
> convey the ground truth narrative, alongside repetition metrics that capture
> the redundancy across consecutive AD outputs. Our method produces coherent AD
> sequences with enhanced narrative understanding, outperforming prior approaches
> that rely on independent generations.

