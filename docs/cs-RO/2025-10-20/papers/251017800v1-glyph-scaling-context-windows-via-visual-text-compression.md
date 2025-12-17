---
layout: default
title: Glyph: Scaling Context Windows via Visual-Text Compression
---

# Glyph: Scaling Context Windows via Visual-Text Compression

**arXiv**: [2510.17800v1](https://arxiv.org/abs/2510.17800) | [PDF](https://arxiv.org/pdf/2510.17800.pdf)

**作者**: Jiale Cheng, Yusen Liu, Xinyu Zhang, Yulin Fei, Wenyi Hong, Ruiliang Lyu, Weihan Wang, Zhe Su, Xiaotao Gu, Xiao Liu, Yushi Bai, Jie Tang, Hongning Wang, Minlie Huang

---

## 💡 一句话要点

**提出Glyph框架，通过视觉-文本压缩扩展上下文窗口以降低计算成本。**

**关键词**: `长上下文建模` `视觉-文本压缩` `视觉语言模型` `遗传搜索优化` `文档理解`

## 📋 核心要点

1. 核心问题：长上下文LLMs计算和内存成本高，限制百万级token任务实用性。
2. 方法要点：将长文本渲染为图像，使用视觉语言模型处理，实现语义保留压缩。
3. 实验效果：实现3-4倍token压缩，准确率可比Qwen3-8B，提升推理和训练速度。

## 📄 摘要（原文）

> Large language models (LLMs) increasingly rely on long-context modeling for
> tasks such as document understanding, code analysis, and multi-step reasoning.
> However, scaling context windows to the million-token level brings prohibitive
> computational and memory costs, limiting the practicality of long-context LLMs.
> In this work, we take a different perspective-visual context scaling-to tackle
> this challenge. Instead of extending token-based sequences, we propose Glyph, a
> framework that renders long texts into images and processes them with
> vision-language models (VLMs). This approach substantially compresses textual
> input while preserving semantic information, and we further design an
> LLM-driven genetic search to identify optimal visual rendering configurations
> for balancing accuracy and compression. Through extensive experiments, we
> demonstrate that our method achieves 3-4x token compression while maintaining
> accuracy comparable to leading LLMs such as Qwen3-8B on various long-context
> benchmarks. This compression also leads to around 4x faster prefilling and
> decoding, and approximately 2x faster SFT training. Furthermore, under extreme
> compression, a 128K-context VLM could scale to handle 1M-token-level text
> tasks. In addition, the rendered text data benefits real-world multimodal
> tasks, such as document understanding. Our code and model are released at
> https://github.com/thu-coai/Glyph.

