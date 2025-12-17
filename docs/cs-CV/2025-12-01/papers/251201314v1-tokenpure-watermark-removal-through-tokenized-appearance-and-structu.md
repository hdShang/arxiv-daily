---
layout: default
title: TokenPure: Watermark Removal through Tokenized Appearance and Structural Guidance
---

# TokenPure: Watermark Removal through Tokenized Appearance and Structural Guidance

**arXiv**: [2512.01314v1](https://arxiv.org/abs/2512.01314) | [PDF](https://arxiv.org/pdf/2512.01314.pdf)

**作者**: Pei Yang, Yepeng Liu, Kelly Peng, Yuan Gao, Yiren Song

---

## 💡 一句话要点

**提出TokenPure框架，基于扩散Transformer实现高效水印去除，平衡破坏与一致性。**

**关键词**: `水印去除` `扩散Transformer` `条件生成` `视觉token` `结构token` `图像重建`

## 📋 核心要点

1. 核心问题：数字水印去除需平衡彻底破坏水印与保持内容一致性。
2. 方法要点：将水印图像分解为视觉和结构token，通过条件生成合成无水印图像。
3. 实验效果：在感知质量和一致性上优于现有基线，实现高保真重建。

## 📄 摘要（原文）

> In the digital economy era, digital watermarking serves as a critical basis for ownership proof of massive replicable content, including AI-generated and other virtual assets. Designing robust watermarks capable of withstanding various attacks and processing operations is even more paramount. We introduce TokenPure, a novel Diffusion Transformer-based framework designed for effective and consistent watermark removal. TokenPure solves the trade-off between thorough watermark destruction and content consistency by leveraging token-based conditional reconstruction. It reframes the task as conditional generation, entirely bypassing the initial watermark-carrying noise. We achieve this by decomposing the watermarked image into two complementary token sets: visual tokens for texture and structural tokens for geometry. These tokens jointly condition the diffusion process, enabling the framework to synthesize watermark-free images with fine-grained consistency and structural integrity. Comprehensive experiments show that TokenPure achieves state-of-the-art watermark removal and reconstruction fidelity, substantially outperforming existing baselines in both perceptual quality and consistency.

