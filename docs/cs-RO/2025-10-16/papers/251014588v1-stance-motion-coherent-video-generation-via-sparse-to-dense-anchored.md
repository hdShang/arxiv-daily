---
layout: default
title: STANCE: Motion Coherent Video Generation Via Sparse-to-Dense Anchored Encoding
---

# STANCE: Motion Coherent Video Generation Via Sparse-to-Dense Anchored Encoding

**arXiv**: [2510.14588v1](https://arxiv.org/abs/2510.14588) | [PDF](https://arxiv.org/pdf/2510.14588.pdf)

**作者**: Zhifei Chen, Tianshuo Xu, Leyi Wu, Luozhou Wang, Dongyu Yan, Zihan You, Wenting Luo, Guo Zhang, Yingcong Chen

---

## 💡 一句话要点

**提出STANCE框架，通过稀疏到稠密锚定编码解决视频生成中运动一致性问题**

**关键词**: `视频生成` `运动一致性` `稀疏到稠密编码` `实例线索` `Dense RoPE` `时间相干性`

## 📋 核心要点

1. 核心问题：视频生成中对象运动不连贯，源于运动提示编码后有效令牌过少和外观-运动优化冲突
2. 方法要点：使用实例线索生成稠密2.5D运动场，并引入Dense RoPE保持运动令牌显著性
3. 实验或效果：结合RGB与辅助图预测，提升时间一致性，无需逐帧轨迹脚本

## 📄 摘要（原文）

> Video generation has recently made striking visual progress, but maintaining
> coherent object motion and interactions remains difficult. We trace two
> practical bottlenecks: (i) human-provided motion hints (e.g., small 2D maps)
> often collapse to too few effective tokens after encoding, weakening guidance;
> and (ii) optimizing for appearance and motion in a single head can favor
> texture over temporal consistency. We present STANCE, an image-to-video
> framework that addresses both issues with two simple components. First, we
> introduce Instance Cues -- a pixel-aligned control signal that turns sparse,
> user-editable hints into a dense 2.5D (camera-relative) motion field by
> averaging per-instance flow and augmenting with monocular depth over the
> instance mask. This reduces depth ambiguity compared to 2D arrow inputs while
> remaining easy to use. Second, we preserve the salience of these cues in token
> space with Dense RoPE, which tags a small set of motion tokens (anchored on the
> first frame) with spatial-addressable rotary embeddings. Paired with joint RGB
> \(+\) auxiliary-map prediction (segmentation or depth), our model anchors
> structure while RGB handles appearance, stabilizing optimization and improving
> temporal coherence without requiring per-frame trajectory scripts.

