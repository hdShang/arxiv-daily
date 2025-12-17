---
layout: default
title: GaTector+: A Unified Head-free Framework for Gaze Object and Gaze Following Prediction
---

# GaTector+: A Unified Head-free Framework for Gaze Object and Gaze Following Prediction

**arXiv**: [2510.25301v1](https://arxiv.org/abs/2510.25301) | [PDF](https://arxiv.org/pdf/2510.25301.pdf)

**作者**: Yang Jin, Guangyu Guo, Binglu Wang

---

## 💡 一句话要点

**提出GaTector+统一框架，解决注视对象检测与注视跟随任务中依赖头部先验知识的问题。**

**关键词**: `注视对象检测` `注视跟随` `统一框架` `头部检测` `注意力机制` `评估指标`

## 📋 核心要点

1. 核心问题：现有方法依赖头部先验知识，需辅助网络提取头部位置，限制系统联合优化与实际应用。
2. 方法要点：使用扩展特定-通用-特定特征提取器，结合头部检测分支和基于头部的注意力机制，消除推理时对头部先验的依赖。
3. 实验效果：在多个基准数据集上验证模型在注视对象检测和注视跟随任务中的有效性。

## 📄 摘要（原文）

> Gaze object detection and gaze following are fundamental tasks for
> interpreting human gaze behavior or intent. However, most previous methods
> usually solve these two tasks separately, and their prediction of gaze objects
> and gaze following typically depend on head-related prior knowledge during both
> the training phase and real-world deployment. This dependency necessitates an
> auxiliary network to extract head location, thus precluding joint optimization
> across the entire system and constraining the practical applicability. To this
> end, we propose GaTector+, a unified framework for gaze object detection and
> gaze following, which eliminates the dependence on the head-related priors
> during inference. Specifically, GaTector+ uses an expanded
> specific-general-specific feature extractor that leverages a shared backbone,
> which extracts general features for gaze following and object detection using
> the shared backbone while using specific blocks before and after the shared
> backbone to better consider the specificity of each sub-task. To obtain
> head-related knowledge without prior information, we first embed a head
> detection branch to predict the head of each person. Then, before regressing
> the gaze point, a head-based attention mechanism is proposed to fuse the sense
> feature and gaze feature with the help of head location. Since the
> suboptimization of the gaze point heatmap leads to the performance bottleneck,
> we propose an attention supervision mechanism to accelerate the learning of the
> gaze heatmap. Finally, we propose a novel evaluation metric, mean Similarity
> over Candidates (mSoC), for gaze object detection, which is more sensitive to
> variations between bounding boxes. The experimental results on multiple
> benchmark datasets demonstrate the effectiveness of our model in both gaze
> object detection and gaze following tasks.

