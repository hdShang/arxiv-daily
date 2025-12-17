---
layout: default
title: SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference
---

# SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference

**arXiv**: [2510.17777v1](https://arxiv.org/abs/2510.17777) | [PDF](https://arxiv.org/pdf/2510.17777.pdf)

**作者**: Samir Khaki, Junxian Guo, Jiaming Tang, Shang Yang, Yukang Chen, Konstantinos N. Plataniotis, Yao Lu, Song Han, Zhijian Liu

---

## 💡 一句话要点

**提出SparseVILA以解决视觉语言模型推理效率问题**

**关键词**: `视觉语言模型` `推理加速` `令牌剪枝` `多模态推理` `长视频分析`

## 📋 核心要点

1. 视觉令牌数量增长导致VLM推理延迟增加
2. 在预填充阶段剪枝冗余令牌，解码阶段检索查询相关令牌
3. 实现端到端加速2.6倍，同时提升文档理解和推理任务准确率

## 📄 摘要（原文）

> Vision Language Models (VLMs) have rapidly advanced in integrating visual and
> textual reasoning, powering applications across high-resolution image
> understanding, long-video analysis, and multi-turn conversation. However, their
> scalability remains limited by the growing number of visual tokens that
> dominate inference latency. We present SparseVILA, a new paradigm for efficient
> VLM inference that decouples visual sparsity across the prefilling and decoding
> stages. SparseVILA distributes sparsity across stages by pruning redundant
> visual tokens during prefill and retrieving only query-relevant tokens during
> decoding. This decoupled design matches leading prefill pruning methods while
> preserving multi-turn fidelity by retaining most of the visual cache so that
> query-aware tokens can be retrieved at each conversation round. Built on an
> AWQ-optimized inference pipeline, SparseVILA achieves up to 4.0 times faster
> prefilling, 2.5 times faster decoding, and an overall 2.6 times end-to-end
> speedup on long-context video tasks -- while improving accuracy on
> document-understanding and reasoning tasks. By decoupling query-agnostic
> pruning and query-aware retrieval, SparseVILA establishes a new direction for
> efficient multimodal inference, offering a training-free, architecture-agnostic
> framework for accelerating large VLMs without sacrificing capability.

