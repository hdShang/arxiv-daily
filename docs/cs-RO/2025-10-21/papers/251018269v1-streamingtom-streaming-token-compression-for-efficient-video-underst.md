---
layout: default
title: StreamingTOM: Streaming Token Compression for Efficient Video Understanding
---

# StreamingTOM: Streaming Token Compression for Efficient Video Understanding

**arXiv**: [2510.18269v1](https://arxiv.org/abs/2510.18269) | [PDF](https://arxiv.org/pdf/2510.18269.pdf)

**作者**: Xueyi Chen, Keda Tao, Kele Shao, Huan Wang

---

## 💡 一句话要点

**提出StreamingTOM框架以解决流式视频理解中的因果性和累积性效率瓶颈**

**关键词**: `流式视频理解` `令牌压缩` `因果性处理` `键值缓存优化` `训练免费方法`

## 📋 核心要点

1. 核心问题：流式视频模型受因果性限制无法访问未来帧，且令牌累积导致效率下降
2. 方法要点：采用因果时间减少和在线量化内存两阶段，压缩预填充和键值缓存
3. 实验效果：实现15.7倍键值缓存压缩、2倍首令牌时间加速，保持高准确率

## 📄 摘要（原文）

> Unlike offline processing, streaming video vision-language models face two
> fundamental constraints: causality and accumulation. Causality prevents access
> to future frames that offline methods exploit, while accumulation causes tokens
> to grow unbounded, creating efficiency bottlenecks. However, existing
> approaches only regulate post-LLM kv-cache, leaving costly pre-LLM prefill
> unchanged. We introduce StreamingTOM, a training-free, plug-and-play two-stage
> framework that addresses both pre-LLM and post-LLM bottlenecks with predictable
> latency. Causal Temporal Reduction imposes a fixed per-frame budget and selects
> tokens based on adjacent-frame changes and token saliency, drastically reducing
> per-frame prefill cost by processing only a compact subset of visual tokens per
> frame instead of all visual tokens. Online Quantized Memory stores tokens in
> 4-bit format, retrieves relevant groups on demand, and dequantizes them,
> keeping the active kv-cache bounded regardless of stream length. Experiments
> demonstrate our method achieves $15.7\times$ kv-cache compression, $1.2\times$
> lower peak memory and $2\times$ faster TTFT compared to prior SOTA.
> StreamingTOM maintains state-of-the-art accuracy among training-free methods
> with an average of $63.8\%$ on offline benchmarks and $55.8\%/3.7$ on RVS.
> These results highlight the practical benefits of our two-stage approach for
> efficient streaming video understanding with bounded growth.

