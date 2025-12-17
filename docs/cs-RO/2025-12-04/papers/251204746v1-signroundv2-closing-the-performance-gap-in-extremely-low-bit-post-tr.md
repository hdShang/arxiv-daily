---
layout: default
title: SignRoundV2: Closing the Performance Gap in Extremely Low-Bit Post-Training Quantization for LLMs
---

# SignRoundV2: Closing the Performance Gap in Extremely Low-Bit Post-Training Quantization for LLMs

**arXiv**: [2512.04746v1](https://arxiv.org/abs/2512.04746) | [PDF](https://arxiv.org/pdf/2512.04746.pdf)

**作者**: Wenhua Cheng, Weiwei Zhang, Heng Guo, Haihao Shen

---

## 💡 一句话要点

**提出SignRoundV2框架以解决大语言模型极低比特后训练量化中的性能下降问题**

**关键词**: `大语言模型量化` `后训练量化` `极低比特量化` `敏感度度量` `比特分配` `量化尺度搜索`

## 📋 核心要点

1. 核心问题：极低比特量化（如2位和4位）常导致大语言模型性能严重下降
2. 方法要点：结合梯度与量化偏差的快速敏感度度量，指导层间比特分配
3. 实验或效果：在4-5位实现约1%方差，2位保持强性能，接近全精度模型

## 📄 摘要（原文）

> Extreme low-bit quantization is critical for efficiently deploying Large Language Models (LLMs), yet it often leads to severe performance degradation at 2-bits and even 4-bits (e.g., MXFP4). We present SignRoundV2, a post-training quantization framework that is highly effective even without mixed-precision. SignRoundV2 introduces (1) a fast sensitivity metric that combines gradient information with quantization-induced deviations to guide layer-wise bit allocation, and (2) a lightweight pre-tuning search for quantization scales to improve extremely low-bit quantization. These components allow SignRoundV2 to close the gap with full-precision models. Extensive experiments indicate that our method sustains competitive accuracy for LLMs, achieving production-grade performance with about 1 percent variance at 4-5 bits and strong results even at 2 bits. The implementation is available at https://github.com/intel/auto-round.

