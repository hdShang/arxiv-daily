---
layout: default
title: Dual-Stream Diffusion for World-Model Augmented Vision-Language-Action Model
---

# Dual-Stream Diffusion for World-Model Augmented Vision-Language-Action Model

**arXiv**: [2510.27607v1](https://arxiv.org/abs/2510.27607) | [PDF](https://arxiv.org/pdf/2510.27607.pdf)

**作者**: John Won, Kyungmin Lee, Huiwon Jang, Dongyoung Kim, Jinwoo Shin

---

## 💡 一句话要点

**提出双流扩散模型以解决视觉-语言-动作模型中模态冲突问题**

**关键词**: `视觉-语言-动作模型` `世界建模` `扩散模型` `模态解耦` `机器人策略学习`

## 📋 核心要点

1. 核心问题：视觉与动作模态差异导致联合预测困难
2. 方法要点：采用双流扩散架构，独立噪声扰动和解耦流匹配损失
3. 实验效果：在模拟和真实机器人任务中显著提升性能

## 📄 摘要（原文）

> Recently, augmenting Vision-Language-Action models (VLAs) with world modeling
> has shown promise in improving robotic policy learning. However, it remains
> challenging to jointly predict next-state observations and action sequences
> because of the inherent difference between the two modalities. To address this,
> we propose DUal-STream diffusion (DUST), a world-model augmented VLA framework
> that handles the modality conflict and enhances the performance of VLAs across
> diverse tasks. Specifically, we propose a multimodal diffusion transformer
> architecture that explicitly maintains separate modality streams while still
> enabling cross-modal knowledge sharing. In addition, we introduce independent
> noise perturbations for each modality and a decoupled flow-matching loss. This
> design enables the model to learn the joint distribution in a bidirectional
> manner while avoiding the need for a unified latent space. Based on the
> decoupling of modalities during training, we also introduce a joint sampling
> method that supports test-time scaling, where action and vision tokens evolve
> asynchronously at different rates. Through experiments on simulated benchmarks
> such as RoboCasa and GR-1, DUST achieves up to 6% gains over baseline methods,
> while our test-time scaling approach provides an additional 2-5% boost. On
> real-world tasks with the Franka Research 3, DUST improves success rates by
> 13%, confirming its effectiveness beyond simulation. Furthermore, pre-training
> on action-free videos from BridgeV2 yields significant transfer gains on
> RoboCasa, underscoring DUST's potential for large-scale VLA pretraining.

