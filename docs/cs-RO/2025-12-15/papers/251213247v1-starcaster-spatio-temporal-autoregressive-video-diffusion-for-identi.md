---
layout: default
title: STARCaster: Spatio-Temporal AutoRegressive Video Diffusion for Identity- and View-Aware Talking Portraits
---

# STARCaster: Spatio-Temporal AutoRegressive Video Diffusion for Identity- and View-Aware Talking Portraits

**arXiv**: [2512.13247v1](https://arxiv.org/abs/2512.13247) | [PDF](https://arxiv.org/pdf/2512.13247.pdf)

**作者**: Foivos Paraperas Papantoniou, Stathis Galanakis, Rolandos Alexandros Potamias, Bernhard Kainz, Stefanos Zafeiriou

---

## 💡 一句话要点

**提出STARCaster以解决身份感知和自由视角的说话肖像视频生成问题**

**关键词**: `说话肖像动画` `视频扩散模型` `身份感知` `自由视角合成` `音频-视觉同步` `自回归训练`

## 📋 核心要点

1. 核心问题：现有2D语音驱动视频模型依赖参考导致运动多样性有限，3D感知动画基于预训练生成器导致重建不完美和身份漂移
2. 方法要点：采用软身份约束和隐式3D感知，通过组合方法从身份感知运动建模到音频-视觉同步再到新视角动画
3. 实验或效果：在多个基准测试中超越先前方法，有效泛化到不同任务和身份

## 📄 摘要（原文）

> This paper presents STARCaster, an identity-aware spatio-temporal video diffusion model that addresses both speech-driven portrait animation and free-viewpoint talking portrait synthesis, given an identity embedding or reference image, within a unified framework. Existing 2D speech-to-video diffusion models depend heavily on reference guidance, leading to limited motion diversity. At the same time, 3D-aware animation typically relies on inversion through pre-trained tri-plane generators, which often leads to imperfect reconstructions and identity drift. We rethink reference- and geometry-based paradigms in two ways. First, we deviate from strict reference conditioning at pre-training by introducing softer identity constraints. Second, we address 3D awareness implicitly within the 2D video domain by leveraging the inherent multi-view nature of video data. STARCaster adopts a compositional approach progressing from ID-aware motion modeling, to audio-visual synchronization via lip reading-based supervision, and finally to novel view animation through temporal-to-spatial adaptation. To overcome the scarcity of 4D audio-visual data, we propose a decoupled learning approach in which view consistency and temporal coherence are trained independently. A self-forcing training scheme enables the model to learn from longer temporal contexts than those generated at inference, mitigating the overly static animations common in existing autoregressive approaches. Comprehensive evaluations demonstrate that STARCaster generalizes effectively across tasks and identities, consistently surpassing prior approaches in different benchmarks.

