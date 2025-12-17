---
layout: default
title: Infinity and Beyond: Compositional Alignment in VAR and Diffusion T2I Models
---

# Infinity and Beyond: Compositional Alignment in VAR and Diffusion T2I Models

**arXiv**: [2512.11542v1](https://arxiv.org/abs/2512.11542) | [PDF](https://arxiv.org/pdf/2512.11542.pdf)

**作者**: Hossein Shahabadi, Niki Sepasian, Arash Marioriyad, Ali Sharifi-Zarchi, Mahdieh Soleymani Baghshah

---

## 💡 一句话要点

**评估VAR与扩散T2I模型在组合对齐上的性能，Infinity-8B表现最佳**

**关键词**: `文本到图像模型` `组合对齐` `VAR模型` `扩散模型` `基准测试` `性能评估`

## 📋 核心要点

1. 核心问题：文本到图像模型在对象、属性和空间关系的组合对齐上仍面临挑战
2. 方法要点：系统比较六种T2I模型，包括VAR和扩散架构，使用T2I-CompBench++和GenEval基准
3. 实验或效果：Infinity-8B在组合对齐上整体最强，Infinity-2B在效率-性能权衡中表现优异

## 📄 摘要（原文）

> Achieving compositional alignment between textual descriptions and generated images - covering objects, attributes, and spatial relationships - remains a core challenge for modern text-to-image (T2I) models. Although diffusion-based architectures have been widely studied, the compositional behavior of emerging Visual Autoregressive (VAR) models is still largely unexamined. We benchmark six diverse T2I systems - SDXL, PixArt-$α$, Flux-Dev, Flux-Schnell, Infinity-2B, and Infinity-8B - across the full T2I-CompBench++ and GenEval suites, evaluating alignment in color and attribute binding, spatial relations, numeracy, and complex multi-object prompts. Across both benchmarks, Infinity-8B achieves the strongest overall compositional alignment, while Infinity-2B also matches or exceeds larger diffusion models in several categories, highlighting favorable efficiency-performance trade-offs. In contrast, SDXL and PixArt-$α$ show persistent weaknesses in attribute-sensitive and spatial tasks. These results provide the first systematic comparison of VAR and diffusion approaches to compositional alignment and establish unified baselines for the future development of the T2I model.

