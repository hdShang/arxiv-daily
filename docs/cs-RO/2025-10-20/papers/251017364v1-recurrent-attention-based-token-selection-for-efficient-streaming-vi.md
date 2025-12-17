---
layout: default
title: Recurrent Attention-based Token Selection for Efficient Streaming Video-LLMs
---

# Recurrent Attention-based Token Selection for Efficient Streaming Video-LLMs

**arXiv**: [2510.17364v1](https://arxiv.org/abs/2510.17364) | [PDF](https://arxiv.org/pdf/2510.17364.pdf)

**作者**: Vaggelis Dorovatas, Soroush Seifi, Gunshi Gupta, Rahaf Aljundi

---

## 💡 一句话要点

**提出基于循环注意力的令牌选择方法，以提升流式视频-大语言模型的效率。**

**关键词**: `流式视频处理` `视觉令牌选择` `注意力机制` `视频-大语言模型` `效率优化`

## 📋 核心要点

1. 核心问题：流式场景下，长视频需在线处理，标准Video-LLMs难以实时响应查询。
2. 方法要点：利用LLM注意力选择视觉令牌，结合循环处理和历史令牌，实现轻量级问答。
3. 实验或效果：在流式视频基准上达到SOTA，丢弃95%令牌时性能损失最小。

## 📄 摘要（原文）

> Video Large Language Models (Video-LLMs) excel at understanding videos
> in-context, provided they have full access to the video when answering queries.
> However, these models face challenges in streaming scenarios where hour-long
> videos must be processed online, and questions need timely responses. In this
> work, we propose a training-free approach compatible with standard Video-LLMs,
> leveraging three key concepts: 1) LLM-informed selection of visual tokens to
> identify those that the LLM has attended to and contributed to its
> understanding of each short clip. Our attention-based selection allows us to
> discard up to ~95% of unimportant visual tokens with minimal performance loss;
> 2) Recurrent processing of past selected tokens to generate temporally coherent
> understanding of each processed clip; 3) Caption-based question answering for
> lightweight and accurate responses. Our method achieves state-of-the-art
> performance on streaming video benchmarks, striking a balance between
> efficiency and effectiveness.

