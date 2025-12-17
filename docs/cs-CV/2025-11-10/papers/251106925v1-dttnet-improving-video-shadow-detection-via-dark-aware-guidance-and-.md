---
layout: default
title: DTTNet: Improving Video Shadow Detection via Dark-Aware Guidance and Tokenized Temporal Modeling
---

# DTTNet: Improving Video Shadow Detection via Dark-Aware Guidance and Tokenized Temporal Modeling

**arXiv**: [2511.06925v1](https://arxiv.org/abs/2511.06925) | [PDF](https://arxiv.org/pdf/2511.06925.pdf)

**作者**: Zhicheng Li, Kunyang Sun, Rui Yao, Hancheng Zhu, Fuyuan Hu, Jiaqi Zhao, Zhiwen Shao, Yong Zhou

---

## 💡 一句话要点

**提出DTTNet，通过暗感知引导和令牌化时序建模改进视频阴影检测**

**关键词**: `视频阴影检测` `视觉-语言匹配` `暗感知语义` `令牌化时序建模` `实时推理`

## 📋 核心要点

1. 核心问题：视频阴影检测面临阴影-背景模糊和动态阴影变形挑战
2. 方法要点：使用视觉-语言匹配模块和暗感知语义块区分阴影，令牌化时序块高效建模时序
3. 实验或效果：在多个基准数据集上实现最先进精度和实时推理效率

## 📄 摘要（原文）

> Video shadow detection confronts two entwined difficulties: distinguishing
> shadows from complex backgrounds and modeling dynamic shadow deformations under
> varying illumination. To address shadow-background ambiguity, we leverage
> linguistic priors through the proposed Vision-language Match Module (VMM) and a
> Dark-aware Semantic Block (DSB), extracting text-guided features to explicitly
> differentiate shadows from dark objects. Furthermore, we introduce adaptive
> mask reweighting to downweight penumbra regions during training and apply edge
> masks at the final decoder stage for better supervision. For temporal modeling
> of variable shadow shapes, we propose a Tokenized Temporal Block (TTB) that
> decouples spatiotemporal learning. TTB summarizes cross-frame shadow semantics
> into learnable temporal tokens, enabling efficient sequence encoding with
> minimal computation overhead. Comprehensive Experiments on multiple benchmark
> datasets demonstrate state-of-the-art accuracy and real-time inference
> efficiency. Codes are available at https://github.com/city-cheng/DTTNet.

