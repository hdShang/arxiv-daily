---
layout: default
title: Graph VQ-Transformer (GVT): Fast and Accurate Molecular Generation via High-Fidelity Discrete Latents
---

# Graph VQ-Transformer (GVT): Fast and Accurate Molecular Generation via High-Fidelity Discrete Latents

**arXiv**: [2512.02667v1](https://arxiv.org/abs/2512.02667) | [PDF](https://arxiv.org/pdf/2512.02667.pdf)

**作者**: Haozhuo Zheng, Cheng Wang, Yang Liu

---

## 💡 一句话要点

**提出Graph VQ-Transformer以高效准确生成分子，通过高保真离散潜在序列解决扩散模型计算量大和自回归模型误差传播问题。**

**关键词**: `分子生成` `图神经网络` `离散潜在空间` `自回归Transformer` `向量量化变分自编码器`

## 📋 核心要点

1. 核心问题：分子生成中扩散模型计算量大，自回归模型易误差传播，需兼顾准确性与效率。
2. 方法要点：结合Graph VQ-VAE和自回归Transformer，将分子图压缩为高保真离散序列进行序列建模。
3. 实验或效果：在ZINC250k等基准上达到SOTA或竞争性能，关键指标优于扩散模型，效率高。

## 📄 摘要（原文）

> The de novo generation of molecules with desirable properties is a critical challenge, where diffusion models are computationally intensive and autoregressive models struggle with error propagation. In this work, we introduce the Graph VQ-Transformer (GVT), a two-stage generative framework that achieves both high accuracy and efficiency. The core of our approach is a novel Graph Vector Quantized Variational Autoencoder (VQ-VAE) that compresses molecular graphs into high-fidelity discrete latent sequences. By synergistically combining a Graph Transformer with canonical Reverse Cuthill-McKee (RCM) node ordering and Rotary Positional Embeddings (RoPE), our VQ-VAE achieves near-perfect reconstruction rates. An autoregressive Transformer is then trained on these discrete latents, effectively converting graph generation into a well-structured sequence modeling problem. Crucially, this mapping of complex graphs to high-fidelity discrete sequences bridges molecular design with the powerful paradigm of large-scale sequence modeling, unlocking potential synergies with Large Language Models (LLMs). Extensive experiments show that GVT achieves state-of-the-art or highly competitive performance across major benchmarks like ZINC250k, MOSES, and GuacaMol, and notably outperforms leading diffusion models on key distribution similarity metrics such as FCD and KL Divergence. With its superior performance, efficiency, and architectural novelty, GVT not only presents a compelling alternative to diffusion models but also establishes a strong new baseline for the field, paving the way for future research in discrete latent-space molecular generation.

