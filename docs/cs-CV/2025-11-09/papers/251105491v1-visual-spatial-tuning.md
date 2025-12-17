---
layout: default
title: Visual Spatial Tuning
---

# Visual Spatial Tuning

**arXiv**: [2511.05491v1](https://arxiv.org/abs/2511.05491) | [PDF](https://arxiv.org/pdf/2511.05491.pdf)

**作者**: Rui Yang, Ziyu Zhu, Yanwei Li, Jingjia Huang, Shen Yan, Siyuan Zhou, Zhe Liu, Xiangtai Li, Shuangye Li, Wenqian Wang, Yi Lin, Hengshuang Zhao

---

## 💡 一句话要点

**提出视觉空间调优框架以增强视觉语言模型的空间能力**

**关键词**: `视觉语言模型` `空间感知` `数据集构建` `渐进式训练` `空间推理` `基准测试`

## 📋 核心要点

1. 核心问题：现有方法增强空间感知需额外编码器，增加开销并损害通用能力。
2. 方法要点：构建大规模数据集VST-P和VST-R，采用渐进式训练提升空间推理。
3. 实验效果：在多个空间基准测试中达到SOTA，如MMSI-Bench 34.8%和VSIBench 61.2%。

## 📄 摘要（原文）

> Capturing spatial relationships from visual inputs is a cornerstone of
> human-like general intelligence. Several previous studies have tried to enhance
> the spatial awareness of Vision-Language Models (VLMs) by adding extra expert
> encoders, which brings extra overhead and usually harms general capabilities.
> To enhance the spatial ability in general architectures, we introduce Visual
> Spatial Tuning (VST), a comprehensive framework to cultivate VLMs with
> human-like visuospatial abilities, from spatial perception to reasoning. We
> first attempt to enhance spatial perception in VLMs by constructing a
> large-scale dataset termed VST-P, which comprises 4.1 million samples spanning
> 19 skills across single views, multiple images, and videos. Then, we present
> VST-R, a curated dataset with 135K samples that instruct models to reason in
> space. In particular, we adopt a progressive training pipeline: supervised
> fine-tuning to build foundational spatial knowledge, followed by reinforcement
> learning to further improve spatial reasoning abilities. Without the
> side-effect to general capabilities, the proposed VST consistently achieves
> state-of-the-art results on several spatial benchmarks, including $34.8\%$ on
> MMSI-Bench and $61.2\%$ on VSIBench. It turns out that the
> Vision-Language-Action models can be significantly enhanced with the proposed
> spatial tuning paradigm, paving the way for more physically grounded AI.

