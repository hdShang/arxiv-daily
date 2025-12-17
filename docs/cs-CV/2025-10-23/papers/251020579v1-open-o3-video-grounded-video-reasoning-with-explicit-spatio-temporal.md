---
layout: default
title: Open-o3 Video: Grounded Video Reasoning with Explicit Spatio-Temporal Evidence
---

# Open-o3 Video: Grounded Video Reasoning with Explicit Spatio-Temporal Evidence

**arXiv**: [2510.20579v1](https://arxiv.org/abs/2510.20579) | [PDF](https://arxiv.org/pdf/2510.20579.pdf)

**作者**: Jiahao Meng, Xiangtai Li, Haochen Wang, Yue Tan, Tao Zhang, Lingdong Kong, Yunhai Tong, Anran Wang, Zhiyang Teng, Yujing Wang, Zhuochen Wang

---

## 💡 一句话要点

**提出Open-o3 Video框架，通过显式时空证据解决视频推理中的时空定位问题。**

**关键词**: `视频推理` `时空证据` `强化学习` `数据集构建` `基准测试` `置信度验证`

## 📋 核心要点

1. 核心问题：视频推理模型缺乏时空证据指示，难以追踪动态场景中的关键证据。
2. 方法要点：构建高质量数据集并采用冷启动强化学习策略，结合多奖励函数优化答案准确性和时空对齐。
3. 实验或效果：在V-STAR基准上实现SOTA，mAM和mLGM显著提升，并在多个视频理解基准上表现一致改进。

## 📄 摘要（原文）

> Most video reasoning models only generate textual reasoning traces without
> indicating when and where key evidence appears. Recent models such as OpenAI-o3
> have sparked wide interest in evidence-centered reasoning for images, yet
> extending this ability to videos is more challenging, as it requires joint
> temporal tracking and spatial localization across dynamic scenes. We introduce
> Open-o3 Video, a non-agent framework that integrates explicit spatio-temporal
> evidence into video reasoning, and carefully collect training data and design
> training strategies to address the aforementioned challenges. The model
> highlights key timestamps, objects, and bounding boxes alongside its answers,
> allowing reasoning to be grounded in concrete visual observations. To enable
> this functionality, we first curate and build two high-quality datasets,
> STGR-CoT-30k for SFT and STGR-RL-36k for RL, with carefully constructed
> temporal and spatial annotations, since most existing datasets offer either
> temporal spans for videos or spatial boxes on images, lacking unified
> spatio-temporal supervision and reasoning traces. Then, we adopt a cold-start
> reinforcement learning strategy with multiple specially designed rewards that
> jointly encourage answer accuracy, temporal alignment, and spatial precision.
> On V-STAR benchmark, Open-o3 Video achieves state-of-the-art performance,
> raising mAM by 14.4% and mLGM by 24.2% on the Qwen2.5-VL baseline. Consistent
> improvements are also observed on a broad range of video understanding
> benchmarks, including VideoMME, WorldSense, VideoMMMU, and TVGBench. Beyond
> accuracy, the reasoning traces produced by Open-o3 Video also provide valuable
> signals for test-time scaling, enabling confidence-aware verification and
> improving answer reliability.

