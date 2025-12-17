---
layout: default
title: PixelRefer: A Unified Framework for Spatio-Temporal Object Referring with Arbitrary Granularity
---

# PixelRefer: A Unified Framework for Spatio-Temporal Object Referring with Arbitrary Granularity

**arXiv**: [2510.23603v1](https://arxiv.org/abs/2510.23603) | [PDF](https://arxiv.org/pdf/2510.23603.pdf)

**作者**: Yuqian Yuan, Wenqiao Zhang, Xin Li, Shihao Wang, Kehan Li, Wentong Li, Jun Xiao, Lei Zhang, Beng Chin Ooi

---

## 💡 一句话要点

**提出PixelRefer统一框架，实现图像和视频中任意粒度对象的细粒度理解**

**关键词**: `多模态大语言模型` `细粒度对象理解` `区域级视觉推理` `高效计算框架` `指令调优数据集`

## 📋 核心要点

1. 现有MLLMs多关注场景级理解，缺乏对象级细粒度推理能力
2. 引入Scale-Adaptive Object Tokenizer生成对象表示，并设计高效变体PixelRefer-Lite
3. 实验验证在多个基准上领先性能，PixelRefer-Lite在保持精度下显著提升效率

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) have demonstrated strong
> general-purpose capabilities in open-world visual comprehension. However, most
> existing MLLMs primarily focus on holistic, scene-level understanding, often
> overlooking the need for fine-grained, object-centric reasoning. In this paper,
> we present PixelRefer, a unified region-level MLLM framework that enables
> advanced fine-grained understanding over user-specified regions across both
> images and videos. Motivated by the observation that LLM attention
> predominantly focuses on object-level tokens, we propose a Scale-Adaptive
> Object Tokenizer (SAOT) to generate compact and semantically rich object
> representations from free-form regions. Our analysis reveals that global visual
> tokens contribute mainly in early LLM layers, inspiring the design of
> PixelRefer-Lite, an efficient variant that employs an Object-Centric Infusion
> module to pre-fuse global context into object tokens. This yields a lightweight
> Object-Only Framework that substantially reduces computational cost while
> maintaining high semantic fidelity. To facilitate fine-grained instruction
> tuning, we curate PixelRefer-2.2M, a high-quality object-centric instruction
> dataset. Extensive experiments across a range of benchmarks validate that
> PixelRefer achieves leading performance with fewer training samples, while
> PixelRefer-Lite offers competitive accuracy with notable gains in efficiency.

