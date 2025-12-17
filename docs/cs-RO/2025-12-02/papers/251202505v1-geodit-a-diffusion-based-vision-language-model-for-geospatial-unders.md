---
layout: default
title: GeoDiT: A Diffusion-based Vision-Language Model for Geospatial Understanding
---

# GeoDiT: A Diffusion-based Vision-Language Model for Geospatial Understanding

**arXiv**: [2512.02505v1](https://arxiv.org/abs/2512.02505) | [PDF](https://arxiv.org/pdf/2512.02505.pdf)

**作者**: Jiaqi Liu, Ronghao Fu, Haoran Liu, Lang Sun, Bo Yang

---

## 💡 一句话要点

**提出GeoDiT，一种基于扩散的视觉语言模型，以并行细化过程解决地理空间理解中的序列生成问题。**

**关键词**: `地理空间理解` `扩散模型` `视觉语言模型` `并行生成` `结构化输出`

## 📋 核心要点

1. 核心问题：自回归模型在地理空间理解中因序列生成与数据并行性不匹配，导致输出结构化和连贯性差。
2. 方法要点：采用扩散模型框架，将地理空间生成重构为并行细化过程，实现从粗到细的整体合成。
3. 实验或效果：在图像描述、视觉定位和多目标检测等基准测试中达到新最优性能，验证了模型与数据结构的对齐优势。

## 📄 摘要（原文）

> Autoregressive models are structurally misaligned with the inherently parallel nature of geospatial understanding, forcing a rigid sequential narrative onto scenes and fundamentally hindering the generation of structured and coherent outputs. We challenge this paradigm by reframing geospatial generation as a parallel refinement process, enabling a holistic, coarse-to-fine synthesis that resolves all semantic elements simultaneously. To operationalize this, we introduce GeoDiT, the first diffusion-based vision-language model tailored for the geospatial domain. Extensive experiments demonstrate that GeoDiT establishes a new state-of-the-art on benchmarks requiring structured, object-centric outputs. It achieves significant gains in image captioning, visual grounding, and multi-object detection, precisely the tasks where autoregressive models falter. Our work validates that aligning the generative process with the data's intrinsic structure is key to unlocking superior performance in complex geospatial analysis.

