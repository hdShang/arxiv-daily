---
layout: default
title: Autoregressive Image Generation Needs Only a Few Lines of Cached Tokens
---

# Autoregressive Image Generation Needs Only a Few Lines of Cached Tokens

**arXiv**: [2512.04857v1](https://arxiv.org/abs/2512.04857) | [PDF](https://arxiv.org/pdf/2512.04857.pdf)

**作者**: Ziran Qin, Youru Lv, Mingbao Lin, Zeren Zhang, Chanfan Gan, Tieyuan Chen, Weiyao Lin

---

## 💡 一句话要点

**提出LineAR以解决自回归图像生成中的内存瓶颈问题**

**关键词**: `自回归图像生成` `键值缓存压缩` `内存优化` `吞吐量加速` `训练无关方法` `视觉注意力`

## 📋 核心要点

1. 自回归图像生成因需缓存所有先前生成的视觉令牌而面临严重内存瓶颈，导致高存储需求和低吞吐量。
2. LineAR是一种无需训练的渐进键值缓存压缩方法，通过行级管理和2D视图，基于行间注意力逐步淘汰对后续行生成无害的低信息令牌。
3. 实验在六个自回归图像生成模型上验证了其有效性，实现了内存节省和吞吐量加速，同时保持或提升生成质量。

## 📄 摘要（原文）

> Autoregressive (AR) visual generation has emerged as a powerful paradigm for image and multimodal synthesis, owing to its scalability and generality. However, existing AR image generation suffers from severe memory bottlenecks due to the need to cache all previously generated visual tokens during decoding, leading to both high storage requirements and low throughput. In this paper, we introduce \textbf{LineAR}, a novel, training-free progressive key-value (KV) cache compression pipeline for autoregressive image generation. By fully exploiting the intrinsic characteristics of visual attention, LineAR manages the cache at the line level using a 2D view, preserving the visual dependency regions while progressively evicting less-informative tokens that are harmless for subsequent line generation, guided by inter-line attention. LineAR enables efficient autoregressive (AR) image generation by utilizing only a few lines of cache, achieving both memory savings and throughput speedup, while maintaining or even improving generation quality. Extensive experiments across six autoregressive image generation models, including class-conditional and text-to-image generation, validate its effectiveness and generality. LineAR improves ImageNet FID from 2.77 to 2.68 and COCO FID from 23.85 to 22.86 on LlamaGen-XL and Janus-Pro-1B, while retaining only 1/6 KV cache. It also improves DPG on Lumina-mGPT-768 with just 1/8 KV cache. Additionally, LineAR achieves significant memory and throughput gains, including up to 67.61% memory reduction and 7.57x speedup on LlamaGen-XL, and 39.66% memory reduction and 5.62x speedup on Janus-Pro-7B.

