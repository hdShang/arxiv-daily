---
layout: default
title: UniComp: Rethinking Video Compression Through Informational Uniqueness
---

# UniComp: Rethinking Video Compression Through Informational Uniqueness

**arXiv**: [2512.03575v1](https://arxiv.org/abs/2512.03575) | [PDF](https://arxiv.org/pdf/2512.03575.pdf)

**作者**: Chao Yuan, Shimin Chen, Minliang Lin, Limeng Qiao, Guanglu Wan, Lin Ma

---

## 💡 一句话要点

**提出UniComp框架，通过信息独特性优化视频压缩，在有限计算预算下最大化信息保真度。**

**关键词**: `视频压缩` `信息独特性` `令牌压缩` `自适应资源分配` `语义帧分组` `空间动态压缩`

## 📋 核心要点

1. 核心问题：视频压缩中如何最小化重建误差，同时受计算预算约束。
2. 方法要点：基于信息独特性设计三个模块，逐步进行语义帧分组、自适应资源分配和细粒度空间压缩。
3. 实验或效果：在有限计算预算下，UniComp优于现有方法，有效保留关键视觉令牌。

## 📄 摘要（原文）

> Distinct from attention-based compression methods, this paper presents an information uniqueness driven video compression framework, termed UniComp, which aims to maximize the information fidelity of video representations under constrained computational budgets. Starting from the information-theoretic perspective, we formulate the vision compression as an optimization problem that minimizes conditional entropy (reconstruction error) between retained and full tokens. To achieve this, we introduce the notion of information uniqueness to measure intrinsic redundancy among tokens to link with reconstruction error. Based on uniqueness, we design three modules-Frame Group Fusion, Token Allocation, and Spatial Dynamic Compression-that progressively perform semantic frame grouping, adaptive resource allocation, and fine-grained spatial compression. Extensive experiments demonstrate that UniComp consistently outperforms existing compression methods in preserving essential visual tokens under limited computational budgets, highlighting the pivotal role of information uniqueness in token compression efficacy.

