---
layout: default
title: Object Detection as an Optional Basis: A Graph Matching Network for Cross-View UAV Localization
---

# Object Detection as an Optional Basis: A Graph Matching Network for Cross-View UAV Localization

**arXiv**: [2511.02489v1](https://arxiv.org/abs/2511.02489) | [PDF](https://arxiv.org/pdf/2511.02489.pdf)

**作者**: Tao Liu, Kan Ren, Qian Chen

---

## 💡 一句话要点

**提出基于对象检测和图神经网络的跨视角无人机定位方法，以解决GNSS缺失区域的图像匹配问题。**

**关键词**: `无人机定位` `跨视角匹配` `对象检测` `图神经网络` `图像检索` `异构图像`

## 📋 核心要点

1. 核心问题：在GNSS缺失区域，无人机视觉定位面临跨视角、跨时相和异构图像匹配的挑战。
2. 方法要点：利用对象检测提取显著实例，结合图神经网络推理节点关系，实现精细匹配。
3. 实验或效果：在公开和真实数据集上验证，有效处理异构外观差异，泛化能力强。

## 📄 摘要（原文）

> With the rapid growth of the low-altitude economy, UAVs have become crucial
> for measurement and tracking in patrol systems. However, in GNSS-denied areas,
> satellite-based localization methods are prone to failure. This paper presents
> a cross-view UAV localization framework that performs map matching via object
> detection, aimed at effectively addressing cross-temporal, cross-view,
> heterogeneous aerial image matching. In typical pipelines, UAV visual
> localization is formulated as an image-retrieval problem: features are
> extracted to build a localization map, and the pose of a query image is
> estimated by matching it to a reference database with known poses. Because
> publicly available UAV localization datasets are limited, many approaches
> recast localization as a classification task and rely on scene labels in these
> datasets to ensure accuracy. Other methods seek to reduce cross-domain
> differences using polar-coordinate reprojection, perspective transformations,
> or generative adversarial networks; however, they can suffer from misalignment,
> content loss, and limited realism. In contrast, we leverage modern object
> detection to accurately extract salient instances from UAV and satellite
> images, and integrate a graph neural network to reason about inter-image and
> intra-image node relationships. Using a fine-grained, graph-based
> node-similarity metric, our method achieves strong retrieval and localization
> performance. Extensive experiments on public and real-world datasets show that
> our approach handles heterogeneous appearance differences effectively and
> generalizes well, making it applicable to scenarios with larger modality gaps,
> such as infrared-visible image matching. Our dataset will be publicly available
> at the following URL: https://github.com/liutao23/ODGNNLoc.git.

