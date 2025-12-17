---
layout: default
title: ConsistTalk: Intensity Controllable Temporally Consistent Talking Head Generation with Diffusion Noise Search
---

# ConsistTalk: Intensity Controllable Temporally Consistent Talking Head Generation with Diffusion Noise Search

**arXiv**: [2511.06833v1](https://arxiv.org/abs/2511.06833) | [PDF](https://arxiv.org/pdf/2511.06833.pdf)

**作者**: Zhenjie Liu, Jianzhang Lu, Renjie Lu, Cong Liang, Shangfei Wang

---

## 💡 一句话要点

**提出ConsistTalk框架，通过解耦外观-运动表示和噪声搜索推理，解决说话头生成中的闪烁和身份漂移问题。**

**关键词**: `说话头生成` `扩散模型` `光流引导` `知识蒸馏` `噪声搜索` `音视频同步`

## 📋 核心要点

1. 核心问题：当前方法存在视觉闪烁、身份漂移和音视频同步不佳，源于外观-运动表示纠缠和推理不稳定。
2. 方法要点：引入光流引导时序模块解耦运动特征，音频-强度模型实现帧级强度控制，扩散噪声初始化策略优化推理。
3. 实验或效果：实验显示ConsistTalk在减少闪烁、保持身份和提升时间一致性方面优于先前方法。

## 📄 摘要（原文）

> Recent advancements in video diffusion models have significantly enhanced
> audio-driven portrait animation. However, current methods still suffer from
> flickering, identity drift, and poor audio-visual synchronization. These issues
> primarily stem from entangled appearance-motion representations and unstable
> inference strategies. In this paper, we introduce \textbf{ConsistTalk}, a novel
> intensity-controllable and temporally consistent talking head generation
> framework with diffusion noise search inference. First, we propose \textbf{an
> optical flow-guided temporal module (OFT)} that decouples motion features from
> static appearance by leveraging facial optical flow, thereby reducing visual
> flicker and improving temporal consistency. Second, we present an
> \textbf{Audio-to-Intensity (A2I) model} obtained through multimodal
> teacher-student knowledge distillation. By transforming audio and facial
> velocity features into a frame-wise intensity sequence, the A2I model enables
> joint modeling of audio and visual motion, resulting in more natural dynamics.
> This further enables fine-grained, frame-wise control of motion dynamics while
> maintaining tight audio-visual synchronization. Third, we introduce a
> \textbf{diffusion noise initialization strategy (IC-Init)}. By enforcing
> explicit constraints on background coherence and motion continuity during
> inference-time noise search, we achieve better identity preservation and refine
> motion dynamics compared to the current autoregressive strategy. Extensive
> experiments demonstrate that ConsistTalk significantly outperforms prior
> methods in reducing flicker, preserving identity, and delivering temporally
> stable, high-fidelity talking head videos.

