---
layout: default
title: Live Avatar: Streaming Real-time Audio-Driven Avatar Generation with Infinite Length
---

# Live Avatar: Streaming Real-time Audio-Driven Avatar Generation with Infinite Length

**arXiv**: [2512.04677v1](https://arxiv.org/abs/2512.04677) | [PDF](https://arxiv.org/pdf/2512.04677.pdf)

**作者**: Yubo Huang, Hailong Guo, Fangtai Wu, Shifeng Zhang, Shijie Huang, Qijun Gan, Lin Liu, Sirui Zhao, Enhong Chen, Jiaming Liu, Steven Hoi

---

## 💡 一句话要点

**提出Live Avatar框架，通过算法-系统协同设计实现实时、高保真、无限长度的音频驱动虚拟人生成。**

**关键词**: `实时虚拟人生成` `扩散模型推理` `流水线并行` `时序一致性` `音频驱动合成` `长视频生成`

## 📋 核心要点

1. 核心问题：现有扩散模型受限于顺序计算和长序列不一致性，难以实时生成音频驱动虚拟人。
2. 方法要点：引入时间步强制流水线并行（TPP）和滚动沉帧机制（RSFM），提升分布式推理效率和时序一致性。
3. 实验或效果：在5个H800 GPU上实现20 FPS端到端生成，首次达到大规模实时高保真虚拟人生成。

## 📄 摘要（原文）

> Existing diffusion-based video generation methods are fundamentally constrained by sequential computation and long-horizon inconsistency, limiting their practical adoption in real-time, streaming audio-driven avatar synthesis. We present Live Avatar, an algorithm-system co-designed framework that enables efficient, high-fidelity, and infinite-length avatar generation using a 14-billion-parameter diffusion model. Our approach introduces Timestep-forcing Pipeline Parallelism (TPP), a distributed inference paradigm that pipelines denoising steps across multiple GPUs, effectively breaking the autoregressive bottleneck and ensuring stable, low-latency real-time streaming. To further enhance temporal consistency and mitigate identity drift and color artifacts, we propose the Rolling Sink Frame Mechanism (RSFM), which maintains sequence fidelity by dynamically recalibrating appearance using a cached reference image. Additionally, we leverage Self-Forcing Distribution Matching Distillation to facilitate causal, streamable adaptation of large-scale models without sacrificing visual quality. Live Avatar demonstrates state-of-the-art performance, reaching 20 FPS end-to-end generation on 5 H800 GPUs, and, to the best of our knowledge, is the first to achieve practical, real-time, high-fidelity avatar generation at this scale. Our work establishes a new paradigm for deploying advanced diffusion models in industrial long-form video synthesis applications.

