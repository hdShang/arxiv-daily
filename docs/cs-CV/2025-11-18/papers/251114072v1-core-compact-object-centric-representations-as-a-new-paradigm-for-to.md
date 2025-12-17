---
layout: default
title: CORE: Compact Object-centric REpresentations as a New Paradigm for Token Merging in LVLMs
---

# CORE: Compact Object-centric REpresentations as a New Paradigm for Token Merging in LVLMs

**arXiv**: [2511.14072v1](https://arxiv.org/abs/2511.14072) | [PDF](https://arxiv.org/pdf/2511.14072.pdf)

**作者**: Jingyu Lei, Gaoang Wang, Der-Horng Lee

---

## 💡 一句话要点

**提出CORE对象中心表示范式，以解决LVLM视觉令牌压缩中的语义缺失问题**

**关键词**: `视觉语言模型` `令牌压缩` `对象中心表示` `语义分割` `高效计算` `基准测试`

## 📋 核心要点

1. LVLM视觉令牌随图像分辨率二次增长，导致计算和内存成本高昂
2. CORE利用分割解码器生成对象掩码，指导令牌合并为紧凑对象中心表示
3. 实验显示CORE在固定和自适应压缩率下均实现SOTA，极端压缩下性能损失极小

## 📄 摘要（原文）

> Large Vision-Language Models (LVLMs) usually suffer from prohibitive computational and memory costs due to the quadratic growth of visual tokens with image resolution. Existing token compression methods, while varied, often lack a high-level semantic understanding, leading to suboptimal merges, information redundancy, or context loss. To address these limitations, we introduce CORE (Compact Object-centric REpresentations), a new paradigm for visual token compression. CORE leverages an efficient segmentation decoder to generate object masks, which serve as a high-level semantic prior to guide the merging of visual tokens into a compact set of object-centric representations. Furthermore, a novel centroid-guided sorting mechanism restores a coherent spatial order to the merged tokens, preserving vital positional information. Extensive experiments show that CORE not only establishes a new state-of-the-art on six authoritative benchmarks for fixed-rate compression, but also achieves dramatic efficiency gains in adaptive-rate settings. Even under extreme compression, after aggressively retaining with only 2.2% of all visual tokens, CORE still maintains 97.4% of baseline performance. Our work demonstrates the superiority of object-centric representations for efficient and effective LVLM processing.

