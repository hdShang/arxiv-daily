---
layout: default
title: Pole-Image: A Self-Supervised Pole-Anchored Descriptor for Long-Term LiDAR Localization and Map Maintenance
---

# Pole-Image: A Self-Supervised Pole-Anchored Descriptor for Long-Term LiDAR Localization and Map Maintenance

**arXiv**: [2510.17237v1](https://arxiv.org/abs/2510.17237) | [PDF](https://arxiv.org/pdf/2510.17237.pdf)

**作者**: Wuhao Xie, Kanji Tanaka

---

## 💡 一句话要点

**提出Pole-Image方法以解决长期LiDAR定位与地图维护中的地标描述问题**

**关键词**: `LiDAR定位` `自监督学习` `地标描述` `对比学习` `地图维护` `杆状锚点`

## 📋 核心要点

1. 核心问题：传统地标方法在可检测性与独特性间存在权衡，难以稳定识别独特签名
2. 方法要点：使用杆状地标作为锚点，生成2D极坐标图像编码相对几何，应用对比学习训练描述符
3. 实验或效果：描述符克服感知混淆，实现鲁棒定位；高精度编码支持高灵敏度变化检测，促进地图维护

## 📄 摘要（原文）

> Long-term autonomy for mobile robots requires both robust self-localization
> and reliable map maintenance. Conventional landmark-based methods face a
> fundamental trade-off between landmarks with high detectability but low
> distinctiveness (e.g., poles) and those with high distinctiveness but difficult
> stable detection (e.g., local point cloud structures). This work addresses the
> challenge of descriptively identifying a unique "signature" (local point cloud)
> by leveraging a detectable, high-precision "anchor" (like a pole). To solve
> this, we propose a novel canonical representation, "Pole-Image," as a hybrid
> method that uses poles as anchors to generate signatures from the surrounding
> 3D structure. Pole-Image represents a pole-like landmark and its surrounding
> environment, detected from a LiDAR point cloud, as a 2D polar coordinate image
> with the pole itself as the origin. This representation leverages the pole's
> nature as a high-precision reference point, explicitly encoding the "relative
> geometry" between the stable pole and the variable surrounding point cloud. The
> key advantage of pole landmarks is that "detection" is extremely easy. This
> ease of detection allows the robot to easily track the same pole, enabling the
> automatic and large-scale collection of diverse observational data (positive
> pairs). This data acquisition feasibility makes "Contrastive Learning (CL)"
> applicable. By applying CL, the model learns a viewpoint-invariant and highly
> discriminative descriptor. The contributions are twofold: 1) The descriptor
> overcomes perceptual aliasing, enabling robust self-localization. 2) The
> high-precision encoding enables high-sensitivity change detection, contributing
> to map maintenance.

