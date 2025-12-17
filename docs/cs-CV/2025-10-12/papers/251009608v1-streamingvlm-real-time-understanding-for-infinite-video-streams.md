---
layout: default
title: StreamingVLM: Real-Time Understanding for Infinite Video Streams
---

# StreamingVLM: Real-Time Understanding for Infinite Video Streams

**arXiv**: [2510.09608v1](https://arxiv.org/abs/2510.09608) | [PDF](https://arxiv.org/pdf/2510.09608.pdf)

**作者**: Ruyi Xu, Guangxuan Xiao, Yukang Chen, Liuning He, Kelly Peng, Yao Lu, Song Han

---

## 💡 一句话要点

**提出StreamingVLM以解决无限视频流实时理解中的延迟与内存问题**

**关键词**: `无限视频流理解` `实时视觉语言模型` `KV缓存优化` `监督微调策略` `长视频基准评估`

## 📋 核心要点

1. 核心问题：处理无限视频流时，全注意力机制导致二次计算成本和长视频性能下降。
2. 方法要点：通过复用注意力sink状态、短窗口视觉令牌和长窗口文本令牌，维持紧凑KV缓存。
3. 实验效果：在Inf-Streams-Eval基准上，以66.18%胜率优于GPT-4O mini，实时性能达8 FPS。

## 📄 摘要（原文）

> Vision-language models (VLMs) could power real-time assistants and autonomous
> agents, but they face a critical challenge: understanding near-infinite video
> streams without escalating latency and memory usage. Processing entire videos
> with full attention leads to quadratic computational costs and poor performance
> on long videos. Meanwhile, simple sliding window methods are also flawed, as
> they either break coherence or suffer from high latency due to redundant
> recomputation. In this paper, we introduce StreamingVLM, a model designed for
> real-time, stable understanding of infinite visual input. Our approach is a
> unified framework that aligns training with streaming inference. During
> inference, we maintain a compact KV cache by reusing states of attention sinks,
> a short window of recent vision tokens, and a long window of recent text
> tokens. This streaming ability is instilled via a simple supervised fine-tuning
> (SFT) strategy that applies full attention on short, overlapped video chunks,
> which effectively mimics the inference-time attention pattern without training
> on prohibitively long contexts. For evaluation, we build Inf-Streams-Eval, a
> new benchmark with videos averaging over two hours that requires dense,
> per-second alignment between frames and text. On Inf-Streams-Eval, StreamingVLM
> achieves a 66.18% win rate against GPT-4O mini and maintains stable, real-time
> performance at up to 8 FPS on a single NVIDIA H100. Notably, our SFT strategy
> also enhances general VQA abilities without any VQA-specific fine-tuning,
> improving performance on LongVideoBench by +4.30 and OVOBench Realtime by
> +5.96. Code is available at https://github.com/mit-han-lab/streaming-vlm.

