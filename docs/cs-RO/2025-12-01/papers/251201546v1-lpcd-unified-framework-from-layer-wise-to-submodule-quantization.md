---
layout: default
title: LPCD: Unified Framework from Layer-Wise to Submodule Quantization
---

# LPCD: Unified Framework from Layer-Wise to Submodule Quantization

**arXiv**: [2512.01546v1](https://arxiv.org/abs/2512.01546) | [PDF](https://arxiv.org/pdf/2512.01546.pdf)

**作者**: Yuma Ichikawa, Yudai Fujimoto, Akira Sakai

---

## 💡 一句话要点

**提出LPCD统一框架，通过层间优化与投影实现任意子模块量化，提升后训练量化性能。**

**关键词**: `后训练量化` `子模块量化` `层间量化` `误差传播` `LLM优化` `统一框架`

## 📋 核心要点

1. 现有后训练量化方法多聚焦线性层，难以捕获大子模块行为，导致误差传播或局限特定模块。
2. LPCD扩展层间量化，通过松弛目标优化任意子模块，并投影回层间量化器，统一现有方法。
3. 在多种LLM架构和比特宽度下，LPCD增强层间量化与现有子模块方法，效果一致提升。

## 📄 摘要（原文）

> Post-training quantization (PTQ) aims to preserve model-level behavior; however, most methods focus on individual linear layers. Even recent extensions, such as QEP and LoaQ, which mitigate error propagation or target specific submodules, still rely on layer-wise formulations and fail to capture the behavior of larger submodules. We introduce Layer-Projected Coordinate Descent (LPCD), a unified framework that extends PTQ beyond layers by optimizing relaxed objectives across arbitrary submodules and projecting the solutions with layer-wise quantizers. LPCD generalizes existing methods and provides a principled approach to quantizing complex submodules while maintaining the efficiency and compatibility of layer-wise PTQ pipelines. Across diverse LLM architectures and bit-widths, LPCD-based submodule quantization consistently enhances both layer-wise PTQ methods and existing submodule approaches.

