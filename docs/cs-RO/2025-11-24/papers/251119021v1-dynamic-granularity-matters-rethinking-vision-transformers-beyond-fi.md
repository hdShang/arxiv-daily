---
layout: default
title: Dynamic Granularity Matters: Rethinking Vision Transformers Beyond Fixed Patch Splitting
---

# Dynamic Granularity Matters: Rethinking Vision Transformers Beyond Fixed Patch Splitting

**arXiv**: [2511.19021v1](https://arxiv.org/abs/2511.19021) | [PDF](https://arxiv.org/pdf/2511.19021.pdf)

**作者**: Qiyang Yu, Yu Fang, Tianrui Li, Xuemei Cao, Yan Chen, Jianghao Li, Fan Min

---

## 💡 一句话要点

**提出Grc-ViT以动态调整视觉粒度，提升Vision Transformers的细粒度识别与计算效率**

**关键词**: `视觉Transformer` `动态粒度调整` `细粒度识别` `计算效率优化` `注意力机制` `图像复杂度评估`

## 📋 核心要点

1. Vision Transformers在捕捉全局依赖时，难以高效表示细粒度局部细节，且现有多尺度方法依赖固定补丁大小并引入冗余计算
2. Grc-ViT通过粗粒度评估模块分析图像复杂度，并利用细粒度精炼模块动态调整补丁和窗口大小，优化注意力计算
3. 实验表明，Grc-ViT在准确性和计算效率间实现优越平衡，增强细粒度判别能力

## 📄 摘要（原文）

> Vision Transformers (ViTs) have demonstrated strong capabilities in capturing global dependencies but often struggle to efficiently represent fine-grained local details. Existing multi-scale approaches alleviate this issue by integrating hierarchical or hybrid features; however, they rely on fixed patch sizes and introduce redundant computation. To address these limitations, we propose Granularity-driven Vision Transformer (Grc-ViT), a dynamic coarse-to-fine framework that adaptively adjusts visual granularity based on image complexity. It comprises two key stages: (1) Coarse Granularity Evaluation module, which assesses visual complexity using edge density, entropy, and frequency-domain cues to estimate suitable patch and window sizes; (2) Fine-grained Refinement module, which refines attention computation according to the selected granularity, enabling efficient and precise feature learning. Two learnable parameters, α and \b{eta}, are optimized end-to-end to balance global reasoning and local perception. Comprehensive evaluations demonstrate that Grc-ViT enhances fine-grained discrimination while achieving a superior trade-off between accuracy and computational efficiency.

