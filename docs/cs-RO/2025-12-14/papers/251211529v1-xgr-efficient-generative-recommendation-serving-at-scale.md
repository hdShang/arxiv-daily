---
layout: default
title: xGR: Efficient Generative Recommendation Serving at Scale
---

# xGR: Efficient Generative Recommendation Serving at Scale

**arXiv**: [2512.11529v1](https://arxiv.org/abs/2512.11529) | [PDF](https://arxiv.org/pdf/2512.11529.pdf)

**作者**: Qingxiao Sun, Tongxuan Liu, Shen Zhang, Siyu Wu, Peijun Yang, Haotian Liang, Menxin Li, Xiaolong Ma, Zhiwei Liang, Ziyi Ren, Minchao Zhang, Xinyu Liu, Ke Zhang, Depei Qian, Hailong Yang

---

## 💡 一句话要点

**提出xGR以解决高并发下生成式推荐系统低延迟服务问题**

**关键词**: `生成式推荐` `低延迟服务` `KV缓存优化` `排序加速` `流水线并行`

## 📋 核心要点

1. 核心问题：生成式推荐处理长提示、短输出，但解码阶段计算和排序开销大，难以满足高并发低延迟需求。
2. 方法要点：通过阶段化计算和分离KV缓存统一预填充与解码，利用早期排序终止和基于掩码的过滤优化排序，重构流水线实现多级重叠和多流并行。
3. 实验或效果：在真实推荐数据集上，xGR在严格延迟约束下比现有基线至少提升3.49倍吞吐量。

## 📄 摘要（原文）

> Recommendation system delivers substantial economic benefits by providing personalized predictions. Generative recommendation (GR) integrates LLMs to enhance the understanding of long user-item sequences. Despite employing attention-based architectures, GR's workload differs markedly from that of LLM serving. GR typically processes long prompt while producing short, fixed-length outputs, yet the computational cost of each decode phase is especially high due to the large beam width. In addition, since the beam search involves a vast item space, the sorting overhead becomes particularly time-consuming. We propose xGR, a GR-oriented serving system that meets strict low-latency requirements under highconcurrency scenarios. First, xGR unifies the processing of prefill and decode phases through staged computation and separated KV cache. Second, xGR enables early sorting termination and mask-based item filtering with data structure reuse. Third, xGR reconstructs the overall pipeline to exploit multilevel overlap and multi-stream parallelism. Our experiments with real-world recommendation service datasets demonstrate that xGR achieves at least 3.49x throughput compared to the state-of-the-art baseline under strict latency constraints.

