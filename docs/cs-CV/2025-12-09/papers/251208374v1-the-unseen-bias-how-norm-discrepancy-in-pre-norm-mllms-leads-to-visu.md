---
layout: default
title: The Unseen Bias: How Norm Discrepancy in Pre-Norm MLLMs Leads to Visual Information Loss
---

# The Unseen Bias: How Norm Discrepancy in Pre-Norm MLLMs Leads to Visual Information Loss

**arXiv**: [2512.08374v1](https://arxiv.org/abs/2512.08374) | [PDF](https://arxiv.org/pdf/2512.08374.pdf)

**作者**: Bozhou Li, Xinda Xue, Sihan Yang, Yang Shi, Xinlong Chen, Yushuo Guan, Yuanxing Zhang, Wentao Zhang

---

## 💡 一句话要点

**提出在视觉投影器后插入LayerNorm层以解决MLLMs中视觉与文本令牌范数差异导致的跨模态融合问题**

**关键词**: `多模态大语言模型` `范数差异` `跨模态融合` `LayerNorm` `视觉信息损失` `不对称更新动态`

## 📋 核心要点

1. 核心问题：Pre-Norm架构导致视觉令牌高范数与文本令牌低范数差异，引发不对称更新动态，损害跨模态特征融合
2. 方法要点：在视觉投影器后添加单个LayerNorm层，强制对齐视觉与文本令牌范数，实现简单有效
3. 实验或效果：在LLaVA-1.5架构上验证，多模态和纯文本基准（如MMLU）性能显著提升

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs), which couple pre-trained vision encoders and language models, have shown remarkable capabilities. However, their reliance on the ubiquitous Pre-Norm architecture introduces a subtle yet critical flaw: a severe norm disparity between the high-norm visual tokens and the low-norm text tokens. In this work, we present a formal theoretical analysis demonstrating that this imbalance is not a static issue. Instead, it induces an ``asymmetric update dynamic,'' where high-norm visual tokens exhibit a ``representational inertia,'' causing them to transform semantically much slower than their textual counterparts. This fundamentally impairs effective cross-modal feature fusion. Our empirical validation across a range of mainstream MLLMs confirms that this theoretical dynamic -- the persistence of norm disparity and the resulting asymmetric update rates -- is a prevalent phenomenon. Based on this insight, we propose a remarkably simple yet effective solution: inserting a single, carefully initialized LayerNorm layer after the visual projector to enforce norm alignment. Experiments conducted on the LLaVA-1.5 architecture show that this intervention yields significant performance gains not only on a wide suite of multimodal benchmarks but also, notably, on text-only evaluations such as MMLU, suggesting that resolving the architectural imbalance leads to a more holistically capable model.

