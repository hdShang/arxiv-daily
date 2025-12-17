---
layout: default
title: Generalizing WiFi Gesture Recognition via Large-Model-Aware Semantic Distillation and Alignment
---

# Generalizing WiFi Gesture Recognition via Large-Model-Aware Semantic Distillation and Alignment

**arXiv**: [2510.13390v1](https://arxiv.org/abs/2510.13390) | [PDF](https://arxiv.org/pdf/2510.13390.pdf)

**作者**: Feng-Qi Cui, Yu-Tong Guo, Tianyue Zheng, Jinyang Huang

---

## 💡 一句话要点

**提出GLSDA框架以增强WiFi手势识别的泛化能力和语义表达。**

**关键词**: `WiFi手势识别` `语义蒸馏` `跨模态对齐` `模型压缩` `RF传感` `泛化学习`

## 📋 核心要点

1. WiFi手势识别泛化差，因CSI域敏感且缺乏高级语义抽象。
2. 利用大模型语义先验，设计双路径编码和多尺度语义对齐机制。
3. 在Widar3.0基准上，跨域识别性能优，模型轻量化且延迟低。

## 📄 摘要（原文）

> WiFi-based gesture recognition has emerged as a promising RF sensing paradigm
> for enabling non-contact and privacy-preserving human-computer interaction in
> AIoT environments. However, existing methods often suffer from limited
> generalization and semantic expressiveness due to the domain-sensitive nature
> of Channel State Information and the lack of high-level gesture abstraction. To
> address these challenges, we propose a novel generalization framework, termed
> Large-Model-Aware Semantic Distillation and Alignment (GLSDA), which leverages
> the semantic prior of pre-trained large foundation models to enhance gesture
> representation learning in both in-domain and cross-domain scenarios.
> Specifically, we first design a dual-path CSI encoding pipeline that captures
> geometric and dynamic gesture patterns via CSI-Ratio phase sequences and
> Doppler spectrograms. These representations are then fed into a Multiscale
> Semantic Encoder, which learns robust temporal embeddings and aligns them with
> gesture semantics through cross-modal attention mechanisms. To further enhance
> category discrimination, we introduce a Semantic-Aware Soft Supervision scheme
> that encodes inter-class correlations and reduces label ambiguity, especially
> for semantically similar gestures. Finally, we develop a Robust
> Dual-Distillation strategy to compress the aligned model into a lightweight
> student network, jointly distilling intermediate features and semantic-informed
> soft labels from the teacher model. Extensive experiments on the Widar3.0
> benchmark show that GLSDA consistently outperforms state-of-the-art methods in
> both in-domain and cross-domain gesture recognition tasks, while significantly
> reducing model size and inference latency. Our method offers a scalable and
> deployable solution for generalized RF-based gesture interfaces in real-world
> AIoT applications.

