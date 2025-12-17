---
layout: default
title: ContextDrag: Precise Drag-Based Image Editing via Context-Preserving Token Injection and Position-Consistent Attention
---

# ContextDrag: Precise Drag-Based Image Editing via Context-Preserving Token Injection and Position-Consistent Attention

**arXiv**: [2512.08477v1](https://arxiv.org/abs/2512.08477) | [PDF](https://arxiv.org/pdf/2512.08477.pdf)

**作者**: Huiguo He, Pengyu Yan, Ziqi Yi, Weizhi Zhong, Zheng Liu, Yejun Tang, Huan Yang, Kun Gai, Guanbin Li, Lianwen Jin

---

## 💡 一句话要点

**提出ContextDrag，通过上下文保留令牌注入和位置一致注意力实现精确拖拽式图像编辑**

**关键词**: `拖拽式图像编辑` `上下文建模` `令牌注入` `注意力机制` `图像保真度`

## 📋 核心要点

1. 核心问题：现有拖拽式编辑方法未能充分利用参考图像的上下文信息，导致编辑连贯性和保真度不足
2. 方法要点：引入上下文保留令牌注入（CTI）和位置一致注意力（PCA），无需微调即可保留细粒度细节
3. 实验或效果：在DragBench-SR和DragBench-DR上超越所有现有SOTA方法，代码将公开

## 📄 摘要（原文）

> Drag-based image editing aims to modify visual content followed by user-specified drag operations. Despite existing methods having made notable progress, they still fail to fully exploit the contextual information in the reference image, including fine-grained texture details, leading to edits with limited coherence and fidelity. To address this challenge, we introduce ContextDrag, a new paradigm for drag-based editing that leverages the strong contextual modeling capability of editing models, such as FLUX-Kontext. By incorporating VAE-encoded features from the reference image, ContextDrag can leverage rich contextual cues and preserve fine-grained details, without the need for finetuning or inversion. Specifically, ContextDrag introduced a novel Context-preserving Token Injection (CTI) that injects noise-free reference features into their correct destination locations via a Latent-space Reverse Mapping (LRM) algorithm. This strategy enables precise drag control while preserving consistency in both semantics and texture details. Second, ContextDrag adopts a novel Position-Consistent Attention (PCA), which positional re-encodes the reference tokens and applies overlap-aware masking to eliminate interference from irrelevant reference features. Extensive experiments on DragBench-SR and DragBench-DR demonstrate that our approach surpasses all existing SOTA methods. Code will be publicly available.

