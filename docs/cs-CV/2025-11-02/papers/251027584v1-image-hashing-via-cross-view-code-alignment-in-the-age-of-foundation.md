---
layout: default
title: Image Hashing via Cross-View Code Alignment in the Age of Foundation Models
---

# Image Hashing via Cross-View Code Alignment in the Age of Foundation Models

**arXiv**: [2510.27584v1](https://arxiv.org/abs/2510.27584) | [PDF](https://arxiv.org/pdf/2510.27584.pdf)

**作者**: Ilyass Moummad, Kawtar Zaher, Hervé Goëau, Alexis Joly

---

## 💡 一句话要点

**提出CroVCA方法，通过跨视图代码对齐实现高效图像哈希检索**

**关键词**: `图像哈希` `跨视图对齐` `编码率最大化` `轻量网络` `高效检索` `基础模型`

## 📋 核心要点

1. 核心问题：基础模型嵌入高维，最近邻搜索计算成本高，现有哈希方法复杂且训练慢。
2. 方法要点：使用单一二元交叉熵损失对齐语义视图，编码率最大化防止代码崩溃。
3. 实验或效果：在多个基准上实现SOTA，16位哈希训练仅需数分钟，效率高。

## 📄 摘要（原文）

> Efficient large-scale retrieval requires representations that are both
> compact and discriminative. Foundation models provide powerful visual and
> multimodal embeddings, but nearest neighbor search in these high-dimensional
> spaces is computationally expensive. Hashing offers an efficient alternative by
> enabling fast Hamming distance search with binary codes, yet existing
> approaches often rely on complex pipelines, multi-term objectives, designs
> specialized for a single learning paradigm, and long training times. We
> introduce CroVCA (Cross-View Code Alignment), a simple and unified principle
> for learning binary codes that remain consistent across semantically aligned
> views. A single binary cross-entropy loss enforces alignment, while coding-rate
> maximization serves as an anti-collapse regularizer to promote balanced and
> diverse codes. To implement this, we design HashCoder, a lightweight MLP
> hashing network with a final batch normalization layer to enforce balanced
> codes. HashCoder can be used as a probing head on frozen embeddings or to adapt
> encoders efficiently via LoRA fine-tuning. Across benchmarks, CroVCA achieves
> state-of-the-art results in just 5 training epochs. At 16 bits, it particularly
> well-for instance, unsupervised hashing on COCO completes in under 2 minutes
> and supervised hashing on ImageNet100 in about 3 minutes on a single GPU. These
> results highlight CroVCA's efficiency, adaptability, and broad applicability.

