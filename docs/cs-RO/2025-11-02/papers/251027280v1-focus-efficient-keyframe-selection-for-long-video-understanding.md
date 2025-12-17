---
layout: default
title: FOCUS: Efficient Keyframe Selection for Long Video Understanding
---

# FOCUS: Efficient Keyframe Selection for Long Video Understanding

**arXiv**: [2510.27280v1](https://arxiv.org/abs/2510.27280) | [PDF](https://arxiv.org/pdf/2510.27280.pdf)

**作者**: Zirui Zhu, Hailun Xu, Yang Luo, Yong Liu, Kanchan Sarkar, Zhenheng Yang, Yang You

---

## 💡 一句话要点

**提出FOCUS方法以解决长视频理解中关键帧选择的高效性问题**

**关键词**: `长视频理解` `关键帧选择` `多臂老虎机` `训练无关方法` `视觉令牌优化`

## 📋 核心要点

1. 核心问题：长视频处理中视觉令牌过多，现有方法可能遗漏关键信息且依赖预过滤
2. 方法要点：将关键帧选择建模为组合纯探索问题，使用置信上界进行两阶段探索与利用
3. 实验或效果：在长视频问答基准上，处理少于2%帧时准确率显著提升，如LongVideoBench上达11.9%增益

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) represent images and video frames as
> visual tokens. Scaling from single images to hour-long videos, however,
> inflates the token budget far beyond practical limits. Popular pipelines
> therefore either uniformly subsample or apply keyframe selection with
> retrieval-style scoring using smaller vision-language models. However, these
> keyframe selection methods still rely on pre-filtering before selection to
> reduce the inference cost and can miss the most informative moments.
>   We propose FOCUS, Frame-Optimistic Confidence Upper-bound Selection, a
> training-free, model-agnostic keyframe selection module that selects
> query-relevant frames under a strict token budget. FOCUS formulates keyframe
> selection as a combinatorial pure-exploration (CPE) problem in multi-armed
> bandits: it treats short temporal clips as arms, and uses empirical means and
> Bernstein confidence radius to identify informative regions while preserving
> exploration of uncertain areas. The resulting two-stage
> exploration-exploitation procedure reduces from a sequential policy with
> theoretical guarantees, first identifying high-value temporal regions, then
> selecting top-scoring frames within each region On two long-video
> question-answering benchmarks, FOCUS delivers substantial accuracy improvements
> while processing less than 2% of video frames. For videos longer than 20
> minutes, it achieves an 11.9% gain in accuracy on LongVideoBench, demonstrating
> its effectiveness as a keyframe selection method and providing a simple and
> general solution for scalable long-video understanding with MLLMs.

