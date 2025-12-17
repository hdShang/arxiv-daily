---
layout: default
title: video-SALMONN S: Streaming Audio-Visual LLMs Beyond Length Limits via Memory
---

# video-SALMONN S: Streaming Audio-Visual LLMs Beyond Length Limits via Memory

**arXiv**: [2510.11129v1](https://arxiv.org/abs/2510.11129) | [PDF](https://arxiv.org/pdf/2510.11129.pdf)

**作者**: Guangzhi Sun, Yixuan Li, Xiaodong Wu, Yudong Yang, Wei Li, Zejun Ma, Chao Zhang

---

## 💡 一句话要点

**提出video-SALMONN S以在固定内存下处理长视频流，实现高质量音频-视觉理解**

**关键词**: `流式音频-视觉大语言模型` `长视频理解` `测试时训练` `记忆模块` `固定内存处理`

## 📋 核心要点

1. 当前视频理解LLM难以处理长视频流，存在内存限制和信息丢失问题
2. 引入测试时训练记忆模块和提示依赖记忆读取器，替代令牌合并以捕获长程依赖
3. 在长视频基准测试中，模型在3小时视频上保持高性能，优于离线与流式基线

## 📄 摘要（原文）

> Continuous, high-frame-rate, high-resolution processing of long video streams
> is critical for future AI agents, yet current video-understanding LLMs struggle
> to scale. Offline, fixed-frame-number methods require the stream length to
> adapt frame rates; streaming methods constrain memory by merging or discarding
> tokens, losing information. We propose video-SALMONN S, a streaming
> audio-visual LLM that, to our knowledge, is the first to process 3-hour videos
> at 1 FPS and 360p resolution under a fixed memory budget. Our model introduces
> (i) a test-time-training (TTT) memory module that continually updates token
> representations to capture long-range dependencies by replacing token merging,
> and (ii) a prompt-dependent memory reader that selectively retrieves
> context-relevant content from fixed-size memory. The TTT module is optimised
> with a Hessian-free conjugate-gradient procedure (TTT_HF) for efficient
> adaptation. On long-video benchmarks (Video-MME, LVBench, VideoEvalPro),
> video-SALMONN S sustains high-quality understanding on multi-hour videos with
> 10k frames and 1M tokens. Our 8B-parameter model achieves 74.2% overall and
> 67.8% on the Video-MME long split, outperforming both offline and streaming
> baselines.

