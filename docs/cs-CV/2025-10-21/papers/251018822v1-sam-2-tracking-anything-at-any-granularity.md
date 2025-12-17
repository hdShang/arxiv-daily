---
layout: default
title: SAM 2++: Tracking Anything at Any Granularity
---

# SAM 2++: Tracking Anything at Any Granularity

**arXiv**: [2510.18822v1](https://arxiv.org/abs/2510.18822) | [PDF](https://arxiv.org/pdf/2510.18822.pdf)

**作者**: Jiaming Zhang, Cheng Liang, Yichun Yang, Chenkai Zeng, Yutao Cui, Xinwen Zhang, Xin Zhou, Kai Ma, Gangshan Wu, Limin Wang

---

## 💡 一句话要点

**提出SAM 2++统一模型以解决视频跟踪中不同粒度任务的分割问题**

**关键词**: `视频跟踪` `统一模型` `任务自适应内存` `多粒度跟踪` `数据引擎`

## 📋 核心要点

1. 核心问题：现有跟踪器针对单一任务设计，缺乏泛化性，导致模型冗余。
2. 方法要点：设计任务特定提示和统一解码器，引入任务自适应内存机制。
3. 实验或效果：在多个基准测试中实现新SOTA，验证统一跟踪框架的鲁棒性。

## 📄 摘要（原文）

> Video tracking aims at finding the specific target in subsequent frames given
> its initial state. Due to the varying granularity of target states across
> different tasks, most existing trackers are tailored to a single task and
> heavily rely on custom-designed modules within the individual task, which
> limits their generalization and leads to redundancy in both model design and
> parameters. To unify video tracking tasks, we present SAM 2++, a unified model
> towards tracking at any granularity, including masks, boxes, and points. First,
> to extend target granularity, we design task-specific prompts to encode various
> task inputs into general prompt embeddings, and a unified decoder to unify
> diverse task results into a unified form pre-output. Next, to satisfy memory
> matching, the core operation of tracking, we introduce a task-adaptive memory
> mechanism that unifies memory across different granularities. Finally, we
> introduce a customized data engine to support tracking training at any
> granularity, producing a large and diverse video tracking dataset with rich
> annotations at three granularities, termed Tracking-Any-Granularity, which
> represents a comprehensive resource for training and benchmarking on unified
> tracking. Comprehensive experiments on multiple benchmarks confirm that SAM 2++
> sets a new state of the art across diverse tracking tasks at different
> granularities, establishing a unified and robust tracking framework.

