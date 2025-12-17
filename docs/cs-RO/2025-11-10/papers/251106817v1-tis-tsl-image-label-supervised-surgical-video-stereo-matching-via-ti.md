---
layout: default
title: TiS-TSL: Image-Label Supervised Surgical Video Stereo Matching via Time-Switchable Teacher-Student Learning
---

# TiS-TSL: Image-Label Supervised Surgical Video Stereo Matching via Time-Switchable Teacher-Student Learning

**arXiv**: [2511.06817v1](https://arxiv.org/abs/2511.06817) | [PDF](https://arxiv.org/pdf/2511.06817.pdf)

**作者**: Rui Wang, Ying Zhou, Hao Wang, Wenwei Zhang, Qiang Li, Zhiwei Wang

---

## 💡 一句话要点

**提出时间可切换师生学习框架以解决微创手术视频立体匹配中的时空不一致问题**

**关键词**: `立体匹配` `师生学习` `微创手术` `时空一致性` `伪标签过滤` `视频预测`

## 📋 核心要点

1. 核心问题：微创手术中密集视差监督稀缺，现有方法缺乏时空一致性，导致预测不稳定和闪烁伪影
2. 方法要点：采用统一模型支持图像和视频预测模式，通过双向时空一致性过滤伪标签并增强时间连贯性
3. 实验效果：在两个公开数据集上，TEPE和EPE指标分别提升至少2.11%和4.54%，优于现有图像级方法

## 📄 摘要（原文）

> Stereo matching in minimally invasive surgery (MIS) is essential for
> next-generation navigation and augmented reality. Yet, dense disparity
> supervision is nearly impossible due to anatomical constraints, typically
> limiting annotations to only a few image-level labels acquired before the
> endoscope enters deep body cavities. Teacher-Student Learning (TSL) offers a
> promising solution by leveraging a teacher trained on sparse labels to generate
> pseudo labels and associated confidence maps from abundant unlabeled surgical
> videos. However, existing TSL methods are confined to image-level supervision,
> providing only spatial confidence and lacking temporal consistency estimation.
> This absence of spatio-temporal reliability results in unstable disparity
> predictions and severe flickering artifacts across video frames. To overcome
> these challenges, we propose TiS-TSL, a novel time-switchable teacher-student
> learning framework for video stereo matching under minimal supervision. At its
> core is a unified model that operates in three distinct modes: Image-Prediction
> (IP), Forward Video-Prediction (FVP), and Backward Video-Prediction (BVP),
> enabling flexible temporal modeling within a single architecture. Enabled by
> this unified model, TiS-TSL adopts a two-stage learning strategy. The
> Image-to-Video (I2V) stage transfers sparse image-level knowledge to initialize
> temporal modeling. The subsequent Video-to-Video (V2V) stage refines temporal
> disparity predictions by comparing forward and backward predictions to
> calculate bidirectional spatio-temporal consistency. This consistency
> identifies unreliable regions across frames, filters noisy video-level pseudo
> labels, and enforces temporal coherence. Experimental results on two public
> datasets demonstrate that TiS-TSL exceeds other image-based state-of-the-arts
> by improving TEPE and EPE by at least 2.11% and 4.54%, respectively..

