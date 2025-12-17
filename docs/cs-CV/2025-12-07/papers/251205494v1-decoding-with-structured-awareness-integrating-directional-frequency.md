---
layout: default
title: Decoding with Structured Awareness: Integrating Directional, Frequency-Spatial, and Structural Attention for Medical Image Segmentation
---

# Decoding with Structured Awareness: Integrating Directional, Frequency-Spatial, and Structural Attention for Medical Image Segmentation

**arXiv**: [2512.05494v1](https://arxiv.org/abs/2512.05494) | [PDF](https://arxiv.org/pdf/2512.05494.pdf)

**作者**: Fan Zhang, Zhiwei Gu, Hua Wang

---

## 💡 一句话要点

**提出集成方向、频空和结构注意力的解码器框架，以解决医学图像分割中边缘细节和空间连续性建模问题。**

**关键词**: `医学图像分割` `注意力机制` `频空融合` `结构建模` `解码器优化`

## 📋 核心要点

1. 针对Transformer解码器在边缘细节、局部纹理和空间连续性建模方面的局限性。
2. 核心模块包括方向引导的ACFA、频空融合的TFFA和结构感知的SMMM，增强全局依赖和局部信息保留。
3. 实验表明在肿瘤分割和器官边界提取等任务中提升分割精度和模型泛化能力。

## 📄 摘要（原文）

> To address the limitations of Transformer decoders in capturing edge details, recognizing local textures and modeling spatial continuity, this paper proposes a novel decoder framework specifically designed for medical image segmentation, comprising three core modules. First, the Adaptive Cross-Fusion Attention (ACFA) module integrates channel feature enhancement with spatial attention mechanisms and introduces learnable guidance in three directions (planar, horizontal, and vertical) to enhance responsiveness to key regions and structural orientations. Second, the Triple Feature Fusion Attention (TFFA) module fuses features from Spatial, Fourier and Wavelet domains, achieving joint frequency-spatial representation that strengthens global dependency and structural modeling while preserving local information such as edges and textures, making it particularly effective in complex and blurred boundary scenarios. Finally, the Structural-aware Multi-scale Masking Module (SMMM) optimizes the skip connections between encoder and decoder by leveraging multi-scale context and structural saliency filtering, effectively reducing feature redundancy and improving semantic interaction quality. Working synergistically, these modules not only address the shortcomings of traditional decoders but also significantly enhance performance in high-precision tasks such as tumor segmentation and organ boundary extraction, improving both segmentation accuracy and model generalization. Experimental results demonstrate that this framework provides an efficient and practical solution for medical image segmentation.

