---
layout: default
title: 4DSegStreamer: Streaming 4D Panoptic Segmentation via Dual Threads
---

# 4DSegStreamer: Streaming 4D Panoptic Segmentation via Dual Threads

**arXiv**: [2510.17664v1](https://arxiv.org/abs/2510.17664) | [PDF](https://arxiv.org/pdf/2510.17664.pdf)

**作者**: Ling Liu, Jun Tian, Li Yi

---

## 💡 一句话要点

**提出4DSegStreamer框架，通过双线程系统实现流式4D全景分割，适用于动态环境实时感知。**

**关键词**: `4D全景分割` `流式感知` `双线程系统` `动态环境` `实时预测`

## 📋 核心要点

1. 核心问题：流式4D全景分割在动态环境中需实时细粒度感知，时间预算受限。
2. 方法要点：采用预测线程和推理线程，预测未来动态并补偿运动，确保及时预测。
3. 实验或效果：在HOI4D、SemanticKITTI和nuScenes数据集上验证有效性，尤其在高FPS下鲁棒。

## 📄 摘要（原文）

> 4D panoptic segmentation in a streaming setting is critical for highly
> dynamic environments, such as evacuating dense crowds and autonomous driving in
> complex scenarios, where real-time, fine-grained perception within a
> constrained time budget is essential. In this paper, we introduce
> 4DSegStreamer, a novel framework that employs a Dual-Thread System to
> efficiently process streaming frames. The framework is general and can be
> seamlessly integrated into existing 3D and 4D segmentation methods to enable
> real-time capability. It also demonstrates superior robustness compared to
> existing streaming perception approaches, particularly under high FPS
> conditions. The system consists of a predictive thread and an inference thread.
> The predictive thread leverages historical motion and geometric information to
> extract features and forecast future dynamics. The inference thread ensures
> timely prediction for incoming frames by aligning with the latest memory and
> compensating for ego-motion and dynamic object movements. We evaluate
> 4DSegStreamer on the indoor HOI4D dataset and the outdoor SemanticKITTI and
> nuScenes datasets. Comprehensive experiments demonstrate the effectiveness of
> our approach, particularly in accurately predicting dynamic objects in complex
> scenes.

