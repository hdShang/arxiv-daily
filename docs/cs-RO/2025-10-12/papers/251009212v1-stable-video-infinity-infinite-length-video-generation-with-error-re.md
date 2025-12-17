---
layout: default
title: Stable Video Infinity: Infinite-Length Video Generation with Error Recycling
---

# Stable Video Infinity: Infinite-Length Video Generation with Error Recycling

**arXiv**: [2510.09212v1](https://arxiv.org/abs/2510.09212) | [PDF](https://arxiv.org/pdf/2510.09212.pdf)

**作者**: Wuyang Li, Wentao Pan, Po-Chien Luan, Yang Gao, Alexandre Alahi

---

## 💡 一句话要点

**提出Stable Video Infinity，通过错误回收微调实现无限长度视频生成**

**关键词**: `无限视频生成` `错误回收微调` `扩散变换器` `自回归学习` `流匹配` `条件生成`

## 📋 核心要点

1. 核心问题：训练假设与自回归生成间的误差累积和假设差距，导致场景重复和运动单调。
2. 方法要点：采用错误回收微调，将自生成错误作为监督提示，促进模型主动识别和纠正错误。
3. 实验或效果：在三个基准测试中验证其多功能性和先进性能，支持从秒级到无限时长视频生成。

## 📄 摘要（原文）

> We propose Stable Video Infinity (SVI) that is able to generate
> infinite-length videos with high temporal consistency, plausible scene
> transitions, and controllable streaming storylines. While existing long-video
> methods attempt to mitigate accumulated errors via handcrafted anti-drifting
> (e.g., modified noise scheduler, frame anchoring), they remain limited to
> single-prompt extrapolation, producing homogeneous scenes with repetitive
> motions. We identify that the fundamental challenge extends beyond error
> accumulation to a critical discrepancy between the training assumption (seeing
> clean data) and the test-time autoregressive reality (conditioning on
> self-generated, error-prone outputs). To bridge this hypothesis gap, SVI
> incorporates Error-Recycling Fine-Tuning, a new type of efficient training that
> recycles the Diffusion Transformer (DiT)'s self-generated errors into
> supervisory prompts, thereby encouraging DiT to actively identify and correct
> its own errors. This is achieved by injecting, collecting, and banking errors
> through closed-loop recycling, autoregressively learning from error-injected
> feedback. Specifically, we (i) inject historical errors made by DiT to
> intervene on clean inputs, simulating error-accumulated trajectories in flow
> matching; (ii) efficiently approximate predictions with one-step bidirectional
> integration and calculate errors with residuals; (iii) dynamically bank errors
> into replay memory across discretized timesteps, which are resampled for new
> input. SVI is able to scale videos from seconds to infinite durations with no
> additional inference cost, while remaining compatible with diverse conditions
> (e.g., audio, skeleton, and text streams). We evaluate SVI on three benchmarks,
> including consistent, creative, and conditional settings, thoroughly verifying
> its versatility and state-of-the-art role.

