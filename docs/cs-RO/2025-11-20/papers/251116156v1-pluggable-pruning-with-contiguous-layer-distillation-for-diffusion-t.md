---
layout: default
title: Pluggable Pruning with Contiguous Layer Distillation for Diffusion Transformers
---

# Pluggable Pruning with Contiguous Layer Distillation for Diffusion Transformers

**arXiv**: [2511.16156v1](https://arxiv.org/abs/2511.16156) | [PDF](https://arxiv.org/pdf/2511.16156.pdf)

**作者**: Jian Ma, Qirong Peng, Xujie Zhu, Peixing Xie, Chen Chen, Haonan Lu

---

## 💡 一句话要点

**提出可插拔剪枝与连续层蒸馏方法，以压缩扩散变换器参数并保持图像生成质量。**

**关键词**: `扩散变换器` `结构化剪枝` `知识蒸馏` `图像生成` `模型压缩` `资源优化`

## 📋 核心要点

1. 扩散变换器参数量大，计算成本高，阻碍资源受限部署。
2. 通过线性探测和相似度趋势分析识别冗余层，结合交替蒸馏实现深度和宽度剪枝。
3. 实验显示参数减少50%，关键指标退化小于3%，代码开源。

## 📄 摘要（原文）

> Diffusion Transformers (DiTs) have shown exceptional performance in image generation, yet their large parameter counts incur high computational costs, impeding deployment in resource-constrained settings. To address this, we propose Pluggable Pruning with Contiguous Layer Distillation (PPCL), a flexible structured pruning framework specifically designed for DiT architectures. First, we identify redundant layer intervals through a linear probing mechanism combined with the first-order differential trend analysis of similarity metrics. Subsequently, we propose a plug-and-play teacher-student alternating distillation scheme tailored to integrate depth-wise and width-wise pruning within a single training phase. This distillation framework enables flexible knowledge transfer across diverse pruning ratios, eliminating the need for per-configuration retraining. Extensive experiments on multiple Multi-Modal Diffusion Transformer architecture models demonstrate that PPCL achieves a 50\% reduction in parameter count compared to the full model, with less than 3\% degradation in key objective metrics. Notably, our method maintains high-quality image generation capabilities while achieving higher compression ratios, rendering it well-suited for resource-constrained environments. The open-source code, checkpoints for PPCL can be found at the following link: https://github.com/OPPO-Mente-Lab/Qwen-Image-Pruning.

