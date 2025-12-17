---
layout: default
title: CoDeQ: End-to-End Joint Model Compression with Dead-Zone Quantizer for High-Sparsity and Low-Precision Networks
---

# CoDeQ: End-to-End Joint Model Compression with Dead-Zone Quantizer for High-Sparsity and Low-Precision Networks

**arXiv**: [2512.12981v1](https://arxiv.org/abs/2512.12981) | [PDF](https://arxiv.org/pdf/2512.12981.pdf)

**作者**: Jonathan Wenshøj, Tong Chen, Bob Pepin, Raghavendra Selvan

---

## 💡 一句话要点

**提出CoDeQ方法，通过可学习死区量化器实现端到端联合剪枝与量化，用于高稀疏低精度网络。**

**关键词**: `模型压缩` `联合剪枝量化` `死区量化器` `端到端优化` `高稀疏网络` `低精度网络`

## 📋 核心要点

1. 现有联合剪枝-量化方法依赖训练循环外的辅助过程，导致工程复杂和次优压缩。
2. CoDeQ利用量化器死区等效于幅度剪枝，通过参数化死区宽度实现端到端可微分优化。
3. 在ImageNet上，CoDeQ将ResNet-18的比特操作降至约5%，同时保持接近全精度准确率。

## 📄 摘要（原文）

> While joint pruning--quantization is theoretically superior to sequential application, current joint methods rely on auxiliary procedures outside the training loop for finding compression parameters. This reliance adds engineering complexity and hyperparameter tuning, while also lacking a direct data-driven gradient signal, which might result in sub-optimal compression. In this paper, we introduce CoDeQ, a simple, fully differentiable method for joint pruning--quantization. Our approach builds on a key observation: the dead-zone of a scalar quantizer is equivalent to magnitude pruning, and can be used to induce sparsity directly within the quantization operator. Concretely, we parameterize the dead-zone width and learn it via backpropagation, alongside the quantization parameters. This design provides explicit control of sparsity, regularized by a single global hyperparameter, while decoupling sparsity selection from bit-width selection. The result is a method for Compression with Dead-zone Quantizer (CoDeQ) that supports both fixed-precision and mixed-precision quantization (controlled by an optional second hyperparameter). It simultaneously determines the sparsity pattern and quantization parameters in a single end-to-end optimization. Consequently, CoDeQ does not require any auxiliary procedures, making the method architecture-agnostic and straightforward to implement. On ImageNet with ResNet-18, CoDeQ reduces bit operations to ~5% while maintaining close to full precision accuracy in both fixed and mixed-precision regimes.

