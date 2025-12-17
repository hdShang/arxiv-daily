---
layout: default
title: MemFlow: Flowing Adaptive Memory for Consistent and Efficient Long Video Narratives
---

# MemFlow: Flowing Adaptive Memory for Consistent and Efficient Long Video Narratives

**arXiv**: [2512.14699v1](https://arxiv.org/abs/2512.14699) | [PDF](https://arxiv.org/pdf/2512.14699.pdf)

**作者**: Sihui Ji, Xi Chen, Shuai Yang, Xin Tao, Pengfei Wan, Hengshuang Zhao

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: Project Page: https://sihuiji.github.io/MemFlow.github.io/

---

## 💡 一句话要点

**提出MemFlow方法，通过动态检索相关历史帧和激活相关token，解决流式视频生成中的长上下文一致性挑战。**

**关键词**: `流式视频生成` `长上下文一致性` `自适应记忆` `动态检索` `注意力机制` `KV缓存` `多模态AI` `视频叙事`

## 📋 核心要点

1. 现有方法使用固定策略压缩历史帧，难以适应不同视频块对历史线索的差异化需求，导致长上下文一致性不足。
2. MemFlow在生成前动态检索与文本提示最相关的历史帧更新内存，生成时仅激活相关token，实现自适应记忆管理。
3. 实验表明，MemFlow显著提升长视频叙事一致性，计算开销极小（速度仅降7.9%），兼容现有流式生成模型。

## 📝 摘要（中文）

流式视频生成的核心挑战在于维持长上下文中的内容一致性，这对内存设计提出了高要求。现有解决方案大多通过预定义策略压缩历史帧来维护内存，但不同待生成的视频块应参考不同的历史线索，固定策略难以满足这一需求。本文提出MemFlow来解决此问题。具体而言，在生成即将到来的视频块之前，我们通过检索与该块文本提示最相关的历史帧来动态更新内存库。这一设计使得即使未来帧中出现新事件或场景切换，也能保持叙事连贯性。此外，在生成过程中，我们仅激活内存库中与每个查询最相关的token，这有效保证了生成效率。通过这种方式，MemFlow在实现出色的长上下文一致性的同时，计算负担可忽略不计（与无内存基线相比速度仅降低7.9%），并保持与任何具有KV缓存的流式视频生成模型的兼容性。

## 🔬 方法详解

MemFlow的整体框架基于流式视频生成模型，核心创新在于引入自适应记忆流机制。方法包括两个关键步骤：首先，在生成每个视频块前，根据当前文本提示从历史帧中动态检索最相关的内容，更新内存库，确保记忆与生成需求对齐；其次，在注意力层中，仅激活内存库中与查询最相关的token，减少计算冗余。与现有方法的主要区别在于，MemFlow摒弃了固定压缩策略，采用动态检索和选择性激活，实现了更灵活高效的长上下文管理。

## 📊 实验亮点

MemFlow在长上下文一致性方面表现突出，同时计算负担极低，与无内存基线相比速度仅降低7.9%，并保持与现有流式视频生成模型的兼容性，验证了其高效性和实用性。

## 🎯 应用场景

该研究可应用于长视频自动生成、影视制作辅助、游戏场景动态渲染等领域，提升叙事连贯性和效率，为多模态AI在创意产业中的实际部署提供技术支持。

## 📄 摘要（原文）

> The core challenge for streaming video generation is maintaining the content consistency in long context, which poses high requirement for the memory design. Most existing solutions maintain the memory by compressing historical frames with predefined strategies. However, different to-generate video chunks should refer to different historical cues, which is hard to satisfy with fixed strategies. In this work, we propose MemFlow to address this problem. Specifically, before generating the coming chunk, we dynamically update the memory bank by retrieving the most relevant historical frames with the text prompt of this chunk. This design enables narrative coherence even if new event happens or scenario switches in future frames. In addition, during generation, we only activate the most relevant tokens in the memory bank for each query in the attention layers, which effectively guarantees the generation efficiency. In this way, MemFlow achieves outstanding long-context consistency with negligible computation burden (7.9% speed reduction compared with the memory-free baseline) and keeps the compatibility with any streaming video generation model with KV cache.

