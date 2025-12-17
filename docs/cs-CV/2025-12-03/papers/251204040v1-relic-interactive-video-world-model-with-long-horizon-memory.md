---
layout: default
title: RELIC: Interactive Video World Model with Long-Horizon Memory
---

# RELIC: Interactive Video World Model with Long-Horizon Memory

**arXiv**: [2512.04040v1](https://arxiv.org/abs/2512.04040) | [PDF](https://arxiv.org/pdf/2512.04040.pdf)

**作者**: Yicong Hong, Yiqun Mei, Chongjian Ge, Yiran Xu, Yang Zhou, Sai Bi, Yannick Hold-Geoffroy, Mike Roberts, Matthew Fisher, Eli Shechtman, Kalyan Sunkavalli, Feng Liu, Zhengqi Li, Hao Tan

---

## 💡 一句话要点

**提出RELIC交互式视频世界模型，通过压缩历史记忆和因果蒸馏实现实时长时探索**

**关键词**: `交互式世界模型` `长时记忆` `视频扩散蒸馏` `实时生成` `空间一致性`

## 📋 核心要点

1. 核心问题：现有方法难以同时实现实时长时流、一致空间记忆和精确用户控制
2. 方法要点：使用压缩历史潜在令牌和相机感知记忆结构，结合因果蒸馏训练
3. 实验或效果：在16 FPS下实时生成，展示更准确动作跟随和稳定长时流

## 📄 摘要（原文）

> A truly interactive world model requires three key ingredients: real-time long-horizon streaming, consistent spatial memory, and precise user control. However, most existing approaches address only one of these aspects in isolation, as achieving all three simultaneously is highly challenging-for example, long-term memory mechanisms often degrade real-time performance. In this work, we present RELIC, a unified framework that tackles these three challenges altogether. Given a single image and a text description, RELIC enables memory-aware, long-duration exploration of arbitrary scenes in real time. Built upon recent autoregressive video-diffusion distillation techniques, our model represents long-horizon memory using highly compressed historical latent tokens encoded with both relative actions and absolute camera poses within the KV cache. This compact, camera-aware memory structure supports implicit 3D-consistent content retrieval and enforces long-term coherence with minimal computational overhead. In parallel, we fine-tune a bidirectional teacher video model to generate sequences beyond its original 5-second training horizon, and transform it into a causal student generator using a new memory-efficient self-forcing paradigm that enables full-context distillation over long-duration teacher as well as long student self-rollouts. Implemented as a 14B-parameter model and trained on a curated Unreal Engine-rendered dataset, RELIC achieves real-time generation at 16 FPS while demonstrating more accurate action following, more stable long-horizon streaming, and more robust spatial-memory retrieval compared with prior work. These capabilities establish RELIC as a strong foundation for the next generation of interactive world modeling.

