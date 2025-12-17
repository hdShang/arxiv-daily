---
layout: default
title: Beyond Real Weights: Hypercomplex Representations for Stable Quantization
---

# Beyond Real Weights: Hypercomplex Representations for Stable Quantization

**arXiv**: [2512.08524v1](https://arxiv.org/abs/2512.08524) | [PDF](https://arxiv.org/pdf/2512.08524.pdf)

**作者**: Jawad Ibn Ahad, Maisha Rahman, Amrijit Biswas, Muhammad Rafsan Kabir, Robin Krambroeckers, Sifat Momen, Nabeel Mohammed, Shafin Rahman

---

## 💡 一句话要点

**提出渐进式重参数化策略，通过PHM层压缩多模态语言模型以提升效率。**

**关键词**: `多模态语言模型` `模型压缩` `渐进式重参数化` `参数化超复数乘法` `知识蒸馏` `推理加速`

## 📋 核心要点

1. 多模态语言模型参数庞大，部署困难，需高效压缩方法。
2. 渐进替换密集前馈网络为PHM层，结合残差插值和轻量损失保持功能。
3. 在多个视觉语言模型上验证，保持性能同时显著减少参数和推理延迟。

## 📄 摘要（原文）

> Multimodal language models (MLLMs) require large parameter capacity to align high-dimensional visual features with linguistic representations, making them computationally heavy and difficult to deploy efficiently. We introduce a progressive reparameterization strategy that compresses these models by gradually replacing dense feed-forward network blocks with compact Parameterized Hypercomplex Multiplication (PHM) layers. A residual interpolation schedule, together with lightweight reconstruction and knowledge distillation losses, ensures that the PHM modules inherit the functional behavior of their dense counterparts during training. This transition yields substantial parameter and FLOP reductions while preserving strong multimodal alignment, enabling faster inference without degrading output quality. We evaluate the approach on multiple vision-language models (VLMs). Our method maintains performance comparable to the base models while delivering significant reductions in model size and inference latency. Progressive PHM substitution thus offers an architecture-compatible path toward more efficient multimodal reasoning and complements existing low-bit quantization techniques.

