---
layout: default
title: Terrain Diffusion: A Diffusion-Based Successor to Perlin Noise in Infinite, Real-Time Terrain Generation
---

# Terrain Diffusion: A Diffusion-Based Successor to Perlin Noise in Infinite, Real-Time Terrain Generation

**arXiv**: [2512.08309v1](https://arxiv.org/abs/2512.08309) | [PDF](https://arxiv.org/pdf/2512.08309.pdf)

**作者**: Alexander Goslin

---

## 💡 一句话要点

**提出Terrain Diffusion以解决Perlin噪声在无限实时地形生成中真实性和大规模连贯性不足的问题。**

**关键词**: `无限地形生成` `扩散模型` `实时合成` `拉普拉斯编码` `一致性蒸馏` `开源框架`

## 📋 核心要点

1. 核心问题：Perlin噪声等传统方法在无限地形生成中真实性和大规模连贯性有限。
2. 方法要点：引入InfiniteDiffusion算法，结合分层扩散模型和拉普拉斯编码，实现无缝无限生成。
3. 实验或效果：支持实时合成无边景观，能连贯可控地生成整个行星，开源框架提供恒定内存操作。

## 📄 摘要（原文）

> For decades, procedural worlds have been built on procedural noise functions such as Perlin noise, which are fast and infinite, yet fundamentally limited in realism and large-scale coherence. We introduce Terrain Diffusion, an AI-era successor to Perlin noise that bridges the fidelity of diffusion models with the properties that made procedural noise indispensable: seamless infinite extent, seed-consistency, and constant-time random access. At its core is InfiniteDiffusion, a novel algorithm for infinite generation, enabling seamless, real-time synthesis of boundless landscapes. A hierarchical stack of diffusion models couples planetary context with local detail, while a compact Laplacian encoding stabilizes outputs across Earth-scale dynamic ranges. An open-source infinite-tensor framework supports constant-memory manipulation of unbounded tensors, and few-step consistency distillation enables efficient generation. Together, these components establish diffusion models as a practical foundation for procedural world generation, capable of synthesizing entire planets coherently, controllably, and without limits.

