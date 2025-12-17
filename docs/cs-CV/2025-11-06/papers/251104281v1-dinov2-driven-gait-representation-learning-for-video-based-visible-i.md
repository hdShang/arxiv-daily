---
layout: default
title: DINOv2 Driven Gait Representation Learning for Video-Based Visible-Infrared Person Re-identification
---

# DINOv2 Driven Gait Representation Learning for Video-Based Visible-Infrared Person Re-identification

**arXiv**: [2511.04281v1](https://arxiv.org/abs/2511.04281) | [PDF](https://arxiv.org/pdf/2511.04281.pdf)

**作者**: Yujie Yang, Shuang Li, Jun Ye, Neng Dong, Fan Li, Huafeng Li

---

## 💡 一句话要点

**提出DinoGRL框架，利用DINOv2学习步态特征以解决视频可见光-红外行人重识别问题。**

**关键词**: `行人重识别` `跨模态检索` `步态特征学习` `视频序列分析` `DINOv2应用`

## 📋 核心要点

1. 核心问题：现有方法忽视步态特征，难以建模跨模态视频匹配的时空一致性。
2. 方法要点：结合DINOv2语义先验生成轮廓，并通过双向交互增强步态与外观特征。
3. 实验或效果：在HITSZ-VCM和BUPT数据集上显著优于现有先进方法。

## 📄 摘要（原文）

> Video-based Visible-Infrared person re-identification (VVI-ReID) aims to
> retrieve the same pedestrian across visible and infrared modalities from video
> sequences. Existing methods tend to exploit modality-invariant visual features
> but largely overlook gait features, which are not only modality-invariant but
> also rich in temporal dynamics, thus limiting their ability to model the
> spatiotemporal consistency essential for cross-modal video matching. To address
> these challenges, we propose a DINOv2-Driven Gait Representation Learning
> (DinoGRL) framework that leverages the rich visual priors of DINOv2 to learn
> gait features complementary to appearance cues, facilitating robust
> sequence-level representations for cross-modal retrieval. Specifically, we
> introduce a Semantic-Aware Silhouette and Gait Learning (SASGL) model, which
> generates and enhances silhouette representations with general-purpose semantic
> priors from DINOv2 and jointly optimizes them with the ReID objective to
> achieve semantically enriched and task-adaptive gait feature learning.
> Furthermore, we develop a Progressive Bidirectional Multi-Granularity
> Enhancement (PBMGE) module, which progressively refines feature representations
> by enabling bidirectional interactions between gait and appearance streams
> across multiple spatial granularities, fully leveraging their complementarity
> to enhance global representations with rich local details and produce highly
> discriminative features. Extensive experiments on HITSZ-VCM and BUPT datasets
> demonstrate the superiority of our approach, significantly outperforming
> existing state-of-the-art methods.

