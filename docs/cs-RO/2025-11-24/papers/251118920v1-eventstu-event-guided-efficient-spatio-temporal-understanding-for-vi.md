---
layout: default
title: EventSTU: Event-Guided Efficient Spatio-Temporal Understanding for Video Large Language Models
---

# EventSTU: Event-Guided Efficient Spatio-Temporal Understanding for Video Large Language Models

**arXiv**: [2511.18920v1](https://arxiv.org/abs/2511.18920) | [PDF](https://arxiv.org/pdf/2511.18920.pdf)

**作者**: Wenhao Xu, Xin Dong, Yue Li, Haoyuan Shi, Zhiwei Xiong

---

## 💡 一句话要点

**提出EventSTU框架以解决视频大语言模型推理成本高的问题**

**关键词**: `事件引导视频理解` `高效时空理解` `关键帧采样` `token剪枝` `事件基准` `视频大语言模型`

## 📋 核心要点

1. 核心问题：视频大语言模型在长视频中因token数量多导致推理成本高。
2. 方法要点：利用事件相机特性进行训练无关的粗到细关键帧采样和自适应token剪枝。
3. 实验或效果：实现3.01倍FLOPs减少和3.10倍预填充加速，同时提升性能。

## 📄 摘要（原文）

> Video large language models have demonstrated strong video understanding capabilities but suffer from high inference costs due to the massive number of tokens in long videos. Inspired by event-based vision, we propose an event-guided, training-free framework for efficient spatio-temporal understanding, named EventSTU. In the temporal domain, we design a coarse-to-fine keyframe sampling algorithm that exploits the change-triggered property of event cameras to eliminate redundant frames. In the spatial domain, we design an adaptive token pruning algorithm that leverages the visual saliency of events as a zero-cost prior to guide spatial reduction. From a holistic spatio-temporal perspective, we further integrate question relevance from keyframe sampling to adaptively allocate token pruning budgets. To facilitate evaluation, we construct EventBench, the first event-inclusive, human-annotated multimodal benchmark that covers diverse real-world scenarios. Beyond physical event cameras, EventSTU also supports general video understanding using simulated events. Comprehensive experiments show that EventSTU achieves 3.01x FLOPs reduction and 3.10x prefilling speedup over the strongest baseline while still improving performance.

