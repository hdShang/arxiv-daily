---
layout: default
title: Script: Graph-Structured and Query-Conditioned Semantic Token Pruning for Multimodal Large Language Models
---

# Script: Graph-Structured and Query-Conditioned Semantic Token Pruning for Multimodal Large Language Models

**arXiv**: [2512.01949v1](https://arxiv.org/abs/2512.01949) | [PDF](https://arxiv.org/pdf/2512.01949.pdf)

**作者**: Zhongyu Yang, Dannong Xu, Wei Pang, Yingfang Yuan

---

## 💡 一句话要点

**提出Script方法以解决多模态大语言模型中视觉令牌冗余导致的效率问题**

**关键词**: `多模态大语言模型` `令牌剪枝` `图结构剪枝` `查询条件剪枝` `模型效率优化` `视觉理解`

## 📋 核心要点

1. 核心问题：视觉令牌增长导致内存消耗和推理延迟增加，现有剪枝方法忽略查询相关性或受注意力机制限制
2. 方法要点：结合图结构剪枝去除视觉冗余令牌和查询条件语义剪枝保留查询相关信息，无需重训练且可跨模型通用
3. 实验或效果：在14个基准测试中，Script在LLaVA-NeXT-7B上实现最高6.8倍预填充加速和10倍FLOP减少，性能保留96.88%

## 📄 摘要（原文）

> The rapid growth of visual tokens in multimodal large language models (MLLMs) leads to excessive memory consumption and inference latency, especially when handling high-resolution images and videos. Token pruning is a technique used to mitigate this issue by removing redundancy, but existing methods often ignore relevance to the user query or suffer from the limitations of attention mechanisms, reducing their adaptability and effectiveness. To address these challenges, we propose Script, a plug-and-play pruning method that requires no retraining and generalizes across diverse MLLMs. Script comprises two modules: a graph-structured pruning module that removes visually redundant tokens, and a query-conditioned semantic pruning module that preserves query-relevant visual information. Together, they enhance performance on multimodal tasks. Experiments on fourteen benchmarks across image and video understanding tasks show that Script consistently achieves higher model efficiency and predictive accuracy compared to existing pruning methods. On LLaVA-NeXT-7B, it achieves up to 6.8x prefill speedup and 10x FLOP reduction, while retaining 96.88% of the original performance.

