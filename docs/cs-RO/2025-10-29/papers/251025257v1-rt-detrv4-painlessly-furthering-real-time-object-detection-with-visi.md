---
layout: default
title: RT-DETRv4: Painlessly Furthering Real-Time Object Detection with Vision Foundation Models
---

# RT-DETRv4: Painlessly Furthering Real-Time Object Detection with Vision Foundation Models

**arXiv**: [2510.25257v1](https://arxiv.org/abs/2510.25257) | [PDF](https://arxiv.org/pdf/2510.25257.pdf)

**作者**: Zijun Liao, Yian Zhao, Xin Shan, Yu Yan, Chang Liu, Lei Lu, Xiangyang Ji, Jie Chen

---

## 💡 一句话要点

**提出基于视觉基础模型的蒸馏框架，提升轻量实时目标检测性能**

**关键词**: `实时目标检测` `视觉基础模型` `知识蒸馏` `轻量网络` `语义转移`

## 📋 核心要点

1. 轻量检测器特征表示弱，阻碍性能提升与部署
2. 引入深度语义注入模块和梯度引导自适应调制策略
3. 在COCO数据集上实现高精度与高帧率，AP达49.7-57.0

## 📄 摘要（原文）

> Real-time object detection has achieved substantial progress through
> meticulously designed architectures and optimization strategies. However, the
> pursuit of high-speed inference via lightweight network designs often leads to
> degraded feature representation, which hinders further performance improvements
> and practical on-device deployment. In this paper, we propose a cost-effective
> and highly adaptable distillation framework that harnesses the rapidly evolving
> capabilities of Vision Foundation Models (VFMs) to enhance lightweight object
> detectors. Given the significant architectural and learning objective
> disparities between VFMs and resource-constrained detectors, achieving stable
> and task-aligned semantic transfer is challenging. To address this, on one
> hand, we introduce a Deep Semantic Injector (DSI) module that facilitates the
> integration of high-level representations from VFMs into the deep layers of the
> detector. On the other hand, we devise a Gradient-guided Adaptive Modulation
> (GAM) strategy, which dynamically adjusts the intensity of semantic transfer
> based on gradient norm ratios. Without increasing deployment and inference
> overhead, our approach painlessly delivers striking and consistent performance
> gains across diverse DETR-based models, underscoring its practical utility for
> real-time detection. Our new model family, RT-DETRv4, achieves state-of-the-art
> results on COCO, attaining AP scores of 49.7/53.5/55.4/57.0 at corresponding
> speeds of 273/169/124/78 FPS.

