---
layout: default
title: Rectified SpaAttn: Revisiting Attention Sparsity for Efficient Video Generation
---

# Rectified SpaAttn: Revisiting Attention Sparsity for Efficient Video Generation

**arXiv**: [2511.19835v1](https://arxiv.org/abs/2511.19835) | [PDF](https://arxiv.org/pdf/2511.19835.pdf)

**作者**: Xuewen Liu, Zhikai Li, Jing Zhang, Mengjuan Chen, Qingyi Gu

---

## 💡 一句话要点

**提出Rectified SpaAttn以解决视频生成中注意力稀疏导致的性能下降问题**

**关键词**: `视频生成` `注意力稀疏` `扩散变换器` `计算效率` `Triton优化`

## 📋 核心要点

1. 核心问题：现有注意力稀疏方法因系统偏差导致性能严重下降，包括关键令牌权重放大和非关键令牌忽略
2. 方法要点：引入隐式全注意力参考，通过孤立池化注意力重分配和增益感知池化校正来修正注意力分配
3. 实验或效果：在HunyuanVideo和Wan 2.1上实现最高3.33倍和2.08倍加速，同时保持高生成质量

## 📄 摘要（原文）

> Diffusion Transformers dominate video generation, but the quadratic complexity of attention computation introduces substantial latency. Attention sparsity reduces computational costs by focusing on critical tokens while ignoring non-critical tokens. However, existing methods suffer from severe performance degradation. In this paper, we revisit attention sparsity and reveal that existing methods induce systematic biases in attention allocation: (1) excessive focus on critical tokens amplifies their attention weights; (2) complete neglect of non-critical tokens causes the loss of relevant attention weights. To address these issues, we propose Rectified SpaAttn, which rectifies attention allocation with implicit full attention reference, thereby enhancing the alignment between sparse and full attention maps. Specifically: (1) for critical tokens, we show that their bias is proportional to the sparse attention weights, with the ratio governed by the amplified weights. Accordingly, we propose Isolated-Pooling Attention Reallocation, which calculates accurate rectification factors by reallocating multimodal pooled weights. (2) for non-critical tokens, recovering attention weights from the pooled query-key yields attention gains but also introduces pooling errors. Therefore, we propose Gain-Aware Pooling Rectification, which ensures that the rectified gain consistently surpasses the induced error. Moreover, we customize and integrate the Rectified SpaAttn kernel using Triton, achieving up to 3.33 and 2.08 times speedups on HunyuanVideo and Wan 2.1, respectively, while maintaining high generation quality. We release Rectified SpaAttn as open-source at https://github.com/BienLuky/Rectified-SpaAttn .

