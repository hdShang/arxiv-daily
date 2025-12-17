---
layout: default
title: VideoSSM: Autoregressive Long Video Generation with Hybrid State-Space Memory
---

# VideoSSM: Autoregressive Long Video Generation with Hybrid State-Space Memory

**arXiv**: [2512.04519v1](https://arxiv.org/abs/2512.04519) | [PDF](https://arxiv.org/pdf/2512.04519.pdf)

**作者**: Yifei Yu, Xiaoshan Wu, Xinting Hu, Tao Hu, Yangtian Sun, Xiaoyang Lyu, Bo Wang, Lin Ma, Yuewen Ma, Zhongrui Wang, Xiaojuan Qi

---

## 💡 一句话要点

**提出VideoSSM，结合自回归扩散与混合状态空间记忆，以解决长视频生成中的累积误差和一致性挑战。**

**关键词**: `长视频生成` `自回归扩散` `状态空间模型` `混合记忆` `时间一致性` `交互控制`

## 📋 核心要点

1. 核心问题：自回归长视频生成面临累积误差、运动漂移和内容重复，导致分钟级一致性差。
2. 方法要点：采用混合状态空间记忆，全局SSM存储场景动态，局部上下文窗口提供运动细节，确保线性时间扩展。
3. 实验或效果：在长短范围基准测试中，实现最佳时间一致性和运动稳定性，支持交互式提示控制。

## 📄 摘要（原文）

> Autoregressive (AR) diffusion enables streaming, interactive long-video generation by producing frames causally, yet maintaining coherence over minute-scale horizons remains challenging due to accumulated errors, motion drift, and content repetition. We approach this problem from a memory perspective, treating video synthesis as a recurrent dynamical process that requires coordinated short- and long-term context. We propose VideoSSM, a Long Video Model that unifies AR diffusion with a hybrid state-space memory. The state-space model (SSM) serves as an evolving global memory of scene dynamics across the entire sequence, while a context window provides local memory for motion cues and fine details. This hybrid design preserves global consistency without frozen, repetitive patterns, supports prompt-adaptive interaction, and scales in linear time with sequence length. Experiments on short- and long-range benchmarks demonstrate state-of-the-art temporal consistency and motion stability among autoregressive video generator especially at minute-scale horizons, enabling content diversity and interactive prompt-based control, thereby establishing a scalable, memory-aware framework for long video generation.

