---
layout: default
title: Seeing the Unseen: Mask-Driven Positional Encoding and Strip-Convolution Context Modeling for Cross-View Object Geo-Localization
---

# Seeing the Unseen: Mask-Driven Positional Encoding and Strip-Convolution Context Modeling for Cross-View Object Geo-Localization

**arXiv**: [2510.20247v1](https://arxiv.org/abs/2510.20247) | [PDF](https://arxiv.org/pdf/2510.20247.pdf)

**作者**: Shuhan Hu, Yiru Li, Yuanyuan Li, Yingying Zhu

---

## 💡 一句话要点

**提出掩码位置编码和条带卷积以提升跨视角物体地理定位性能**

**关键词**: `跨视角物体地理定位` `掩码位置编码` `条带卷积` `上下文建模` `卫星图像分析` `端到端框架`

## 📋 核心要点

1. 现有方法依赖关键点位置编码，忽略物体形状，导致对标注偏移敏感和跨视角匹配能力有限
2. 引入掩码位置编码捕获空间坐标和物体轮廓，设计条带卷积提取长程上下文特征增强区分度
3. 在CVOGL和VIGOR-Building数据集上实验，定位精度提升3.39%，达到先进水平

## 📄 摘要（原文）

> Cross-view object geo-localization enables high-precision object localization
> through cross-view matching, with critical applications in autonomous driving,
> urban management, and disaster response. However, existing methods rely on
> keypoint-based positional encoding, which captures only 2D coordinates while
> neglecting object shape information, resulting in sensitivity to annotation
> shifts and limited cross-view matching capability. To address these
> limitations, we propose a mask-based positional encoding scheme that leverages
> segmentation masks to capture both spatial coordinates and object silhouettes,
> thereby upgrading the model from "location-aware" to "object-aware."
> Furthermore, to tackle the challenge of large-span objects (e.g., elongated
> buildings) in satellite imagery, we design a context enhancement module. This
> module employs horizontal and vertical strip convolutional kernels to extract
> long-range contextual features, enhancing feature discrimination among
> strip-like objects. Integrating MPE and CEM, we present EDGeo, an end-to-end
> framework for robust cross-view object geo-localization. Extensive experiments
> on two public datasets (CVOGL and VIGOR-Building) demonstrate that our method
> achieves state-of-the-art performance, with a 3.39% improvement in localization
> accuracy under challenging ground-to-satellite scenarios. This work provides a
> robust positional encoding paradigm and a contextual modeling framework for
> advancing cross-view geo-localization research.

