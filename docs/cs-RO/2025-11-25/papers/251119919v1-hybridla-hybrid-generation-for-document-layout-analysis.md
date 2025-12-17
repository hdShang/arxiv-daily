---
layout: default
title: HybriDLA: Hybrid Generation for Document Layout Analysis
---

# HybriDLA: Hybrid Generation for Document Layout Analysis

**arXiv**: [2511.19919v1](https://arxiv.org/abs/2511.19919) | [PDF](https://arxiv.org/pdf/2511.19919.pdf)

**作者**: Yufan Chen, Omar Moured, Ruiping Liu, Junwei Zheng, Kunyu Peng, Jiaming Zhang, Rainer Stiefelhagen

---

## 💡 一句话要点

**提出HybriDLA框架以解决现代文档布局分析中元素多样性和复杂性挑战**

**关键词**: `文档布局分析` `生成式模型` `扩散模型` `自回归解码` `多尺度特征融合` `边界框预测`

## 📋 核心要点

1. 传统文档布局分析依赖固定查询，难以处理元素数量和布局多变的现代文档
2. 结合扩散和自回归解码，迭代优化边界框并注入语义上下文，提升预测精度
3. 在DocLayNet和M$^6$Doc基准测试中达到83.5% mAP，实现最先进性能

## 📄 摘要（原文）

> Conventional document layout analysis (DLA) traditionally depends on empirical priors or a fixed set of learnable queries executed in a single forward pass. While sufficient for early-generation documents with a small, predetermined number of regions, this paradigm struggles with contemporary documents, which exhibit diverse element counts and increasingly complex layouts. To address challenges posed by modern documents, we present HybriDLA, a novel generative framework that unifies diffusion and autoregressive decoding within a single layer. The diffusion component iteratively refines bounding-box hypotheses, whereas the autoregressive component injects semantic and contextual awareness, enabling precise region prediction even in highly varied layouts. To further enhance detection quality, we design a multi-scale feature-fusion encoder that captures both fine-grained and high-level visual cues. This architecture elevates performance to 83.5% mean Average Precision (mAP). Extensive experiments on the DocLayNet and M$^6$Doc benchmarks demonstrate that HybriDLA sets a state-of-the-art performance, outperforming previous approaches. All data and models will be made publicly available at https://yufanchen96.github.io/projects/HybriDLA.

