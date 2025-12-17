---
layout: default
title: Learning to Expand Images for Efficient Visual Autoregressive Modeling
---

# Learning to Expand Images for Efficient Visual Autoregressive Modeling

**arXiv**: [2511.15499v1](https://arxiv.org/abs/2511.15499) | [PDF](https://arxiv.org/pdf/2511.15499.pdf)

**作者**: Ruiqing Yang, Kaixin Zhang, Zheng Zhang, Shan You, Tao Huang

---

## 💡 一句话要点

**提出扩展自回归表示以解决视觉生成效率问题**

**关键词**: `视觉自回归建模` `图像生成` `高效解码` `螺旋展开` `长度自适应策略`

## 📋 核心要点

1. 现有视觉自回归模型存在解码效率低或多尺度表示复杂的问题
2. 引入螺旋展开和长度自适应解码，模拟人类视觉中心向外感知
3. 在ImageNet上实现保真度与效率的先进权衡

## 📄 摘要（原文）

> Autoregressive models have recently shown great promise in visual generation by leveraging discrete token sequences akin to language modeling. However, existing approaches often suffer from inefficiency, either due to token-by-token decoding or the complexity of multi-scale representations. In this work, we introduce Expanding Autoregressive Representation (EAR), a novel generation paradigm that emulates the human visual system's center-outward perception pattern. EAR unfolds image tokens in a spiral order from the center and progressively expands outward, preserving spatial continuity and enabling efficient parallel decoding. To further enhance flexibility and speed, we propose a length-adaptive decoding strategy that dynamically adjusts the number of tokens predicted at each step. This biologically inspired design not only reduces computational cost but also improves generation quality by aligning the generation order with perceptual relevance. Extensive experiments on ImageNet demonstrate that EAR achieves state-of-the-art trade-offs between fidelity and efficiency on single-scale autoregressive models, setting a new direction for scalable and cognitively aligned autoregressive image generation.

