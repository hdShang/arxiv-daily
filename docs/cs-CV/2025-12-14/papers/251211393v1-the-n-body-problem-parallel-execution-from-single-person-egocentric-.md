---
layout: default
title: The N-Body Problem: Parallel Execution from Single-Person Egocentric Video
---

# The N-Body Problem: Parallel Execution from Single-Person Egocentric Video

**arXiv**: [2512.11393v1](https://arxiv.org/abs/2512.11393) | [PDF](https://arxiv.org/pdf/2512.11393.pdf)

**作者**: Zhifan Zhu, Yifei Huang, Yoichi Sato, Dima Damen

---

## 💡 一句话要点

**提出N-Body问题与结构化提示策略，从单人第一人称视频学习多人并行执行任务**

**关键词**: `第一人称视频理解` `并行任务执行` `视觉语言模型` `物理约束推理` `结构化提示`

## 📋 核心要点

1. 核心问题：如何从单人第一人称视频中学习多人并行执行任务，最大化加速但避免物理冲突
2. 方法要点：使用结构化提示引导视觉语言模型推理3D环境、物体使用和时序依赖，生成可行并行执行方案
3. 实验或效果：在EPIC-Kitchens和HD-EPIC数据集上，N=2时动作覆盖率提升45%，冲突率显著降低

## 📄 摘要（原文）

> Humans can intuitively parallelise complex activities, but can a model learn this from observing a single person? Given one egocentric video, we introduce the N-Body Problem: how N individuals, can hypothetically perform the same set of tasks observed in this video. The goal is to maximise speed-up, but naive assignment of video segments to individuals often violates real-world constraints, leading to physically impossible scenarios like two people using the same object or occupying the same space. To address this, we formalise the N-Body Problem and propose a suite of metrics to evaluate both performance (speed-up, task coverage) and feasibility (spatial collisions, object conflicts and causal constraints). We then introduce a structured prompting strategy that guides a Vision-Language Model (VLM) to reason about the 3D environment, object usage, and temporal dependencies to produce a viable parallel execution. On 100 videos from EPIC-Kitchens and HD-EPIC, our method for N = 2 boosts action coverage by 45% over a baseline prompt for Gemini 2.5 Pro, while simultaneously slashing collision rates, object and causal conflicts by 55%, 45% and 55% respectively.

