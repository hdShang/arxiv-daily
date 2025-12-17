---
layout: default
title: Mofasa: A Step Change in Metal-Organic Framework Generation
---

# Mofasa: A Step Change in Metal-Organic Framework Generation

**arXiv**: [2512.01756v1](https://arxiv.org/abs/2512.01756) | [PDF](https://arxiv.org/pdf/2512.01756.pdf)

**作者**: Vaidotas Simkus, Anders Christensen, Steven Bennett, Ian Johnson, Mark Neumann, James Gin, Jonathan Godwin, Benjamin Rhodes

---

## 💡 一句话要点

**提出Mofasa全原子潜在扩散模型，用于高性能生成金属有机框架材料。**

**关键词**: `金属有机框架生成` `潜在扩散模型` `全原子建模` `材料发现` `晶体结构采样`

## 📋 核心要点

1. 核心问题：金属有机框架材料生成缺乏高性能生成模型，限制了其理性设计与发现。
2. 方法要点：采用全原子潜在扩散模型，联合采样位置、原子类型和晶格向量，避免手工组装算法。
3. 实验或效果：模型能生成多达500原子的系统，性能达到先进水平，并发布MofasaDB数据库和网络界面。

## 📄 摘要（原文）

> Mofasa is an all-atom latent diffusion model with state-of-the-art performance for generating Metal-Organic Frameworks (MOFs). These are highly porous crystalline materials used to harvest water from desert air, capture carbon dioxide, store toxic gases and catalyse chemical reactions. In recognition of their value, the development of MOFs recently received a Nobel Prize in Chemistry.
>   In many ways, MOFs are well-suited for exploiting generative models in chemistry: they are rationally-designable materials with a large combinatorial design space and strong structure-property couplings. And yet, to date, a high performance generative model has been lacking. To fill this gap, we introduce Mofasa, a general-purpose latent diffusion model that jointly samples positions, atom-types and lattice vectors for systems as large as 500 atoms. Mofasa avoids handcrafted assembly algorithms common in the literature, unlocking the simultaneous discovery of metal nodes, linkers and topologies.
>   To help the scientific community build on our work, we release MofasaDB, an annotated library of hundreds of thousands of sampled MOF structures, along with a user-friendly web interface for search and discovery: https://mofux.ai/ .

