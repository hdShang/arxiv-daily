---
layout: default
title: LiveStar: Live Streaming Assistant for Real-World Online Video Understanding
---

# LiveStar: Live Streaming Assistant for Real-World Online Video Understanding

**arXiv**: [2511.05299v1](https://arxiv.org/abs/2511.05299) | [PDF](https://arxiv.org/pdf/2511.05299.pdf)

**作者**: Zhenyu Yang, Kairui Zhang, Yuhang Hu, Bing Wang, Shengsheng Qian, Bin Wen, Fan Yang, Tingting Gao, Weiming Dong, Changsheng Xu

---

## 💡 一句话要点

**提出LiveStar以解决在线视频理解中实时响应与叙事连贯性问题**

**关键词**: `在线视频理解` `流式解码` `内存压缩` `视频大语言模型` `实时响应`

## 📋 核心要点

1. 现有在线视频大模型难以同时处理连续帧输入并确定最佳响应时机，影响实时性与连贯性
2. 采用自适应流式解码，包括增量视频语言对齐、响应静默解码框架和内存感知加速
3. 在多个基准测试中，语义正确性平均提升19.5%，推理速度提升12.0%

## 📄 摘要（原文）

> Despite significant progress in Video Large Language Models (Video-LLMs) for
> offline video understanding, existing online Video-LLMs typically struggle to
> simultaneously process continuous frame-by-frame inputs and determine optimal
> response timing, often compromising real-time responsiveness and narrative
> coherence. To address these limitations, we introduce LiveStar, a pioneering
> live streaming assistant that achieves always-on proactive responses through
> adaptive streaming decoding. Specifically, LiveStar incorporates: (1) a
> training strategy enabling incremental video-language alignment for
> variable-length video streams, preserving temporal consistency across
> dynamically evolving frame sequences; (2) a response-silence decoding framework
> that determines optimal proactive response timing via a single forward pass
> verification; (3) memory-aware acceleration via peak-end memory compression for
> online inference on 10+ minute videos, combined with streaming key-value cache
> to achieve 1.53x faster inference. We also construct an OmniStar dataset, a
> comprehensive dataset for training and benchmarking that encompasses 15 diverse
> real-world scenarios and 5 evaluation tasks for online video understanding.
> Extensive experiments across three benchmarks demonstrate LiveStar's
> state-of-the-art performance, achieving an average 19.5% improvement in
> semantic correctness with 18.1% reduced timing difference compared to existing
> online Video-LLMs, while improving FPS by 12.0% across all five OmniStar tasks.
> Our model and dataset can be accessed at https://github.com/yzy-bupt/LiveStar.

