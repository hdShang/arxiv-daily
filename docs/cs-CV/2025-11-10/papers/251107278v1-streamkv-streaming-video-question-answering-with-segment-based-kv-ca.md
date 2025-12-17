---
layout: default
title: StreamKV: Streaming Video Question-Answering with Segment-based KV Cache Retrieval and Compression
---

# StreamKV: Streaming Video Question-Answering with Segment-based KV Cache Retrieval and Compression

**arXiv**: [2511.07278v1](https://arxiv.org/abs/2511.07278) | [PDF](https://arxiv.org/pdf/2511.07278.pdf)

**作者**: Yilong Chen, Xiang Bai, Zhibin Wang, Chengyu Bai, Yuhan Dai, Ming Lu, Shanghang Zhang

---

## 💡 一句话要点

**提出StreamKV框架，通过语义分割与KV缓存优化提升长视频问答效率与准确性**

**关键词**: `视频大模型` `KV缓存检索` `语义分割` `长视频问答` `内存效率优化`

## 📋 核心要点

1. 核心问题：现有视频大模型处理长视频时KV缓存检索与压缩不足，影响效率与准确性。
2. 方法要点：动态分割视频为语义段，计算摘要向量并引入指导提示进行KV缓存压缩与检索。
3. 实验效果：在StreamingVQA基准上显著优于现有在线视频大模型，提升准确率与计算效率。

## 📄 摘要（原文）

> Video Large Language Models (Video-LLMs) have demonstrated significant
> potential in the areas of video captioning, search, and summarization. However,
> current Video-LLMs still face challenges with long real-world videos. Recent
> methods have introduced a retrieval mechanism that retrieves query-relevant KV
> caches for question answering, enhancing the efficiency and accuracy of long
> real-world videos. However, the compression and retrieval of KV caches are
> still not fully explored. In this paper, we propose \textbf{StreamKV}, a
> training-free framework that seamlessly equips Video-LLMs with advanced KV
> cache retrieval and compression. Compared to previous methods that used uniform
> partitioning, StreamKV dynamically partitions video streams into semantic
> segments, which better preserves semantic information. For KV cache retrieval,
> StreamKV calculates a summary vector for each segment to retain segment-level
> information essential for retrieval. For KV cache compression, StreamKV
> introduces a guidance prompt designed to capture the key semantic elements
> within each segment, ensuring only the most informative KV caches are retained
> for answering questions. Moreover, StreamKV unifies KV cache retrieval and
> compression within a single module, performing both in a layer-adaptive manner,
> thereby further improving the effectiveness of streaming video question
> answering. Extensive experiments on public StreamingVQA benchmarks demonstrate
> that StreamKV significantly outperforms existing Online Video-LLMs, achieving
> superior accuracy while substantially improving both memory efficiency and
> computational latency. The code has been released at
> https://github.com/sou1p0wer/StreamKV.

