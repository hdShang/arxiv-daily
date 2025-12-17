---
layout: default
title: NormalView: sensor-agnostic tree species classification from backpack and aerial lidar data using geometric projections
---

# NormalView: sensor-agnostic tree species classification from backpack and aerial lidar data using geometric projections

**arXiv**: [2512.05610v1](https://arxiv.org/abs/2512.05610) | [PDF](https://arxiv.org/pdf/2512.05610.pdf)

**作者**: Juho Korkeala, Jesse Muhojoki, Josef Taher, Klaara Salolahti, Matti Hyyppä, Antero Kukko, Juha Hyyppä

---

## 💡 一句话要点

**提出NormalView方法，基于几何投影实现传感器无关的背包和航空激光雷达数据树种分类**

**关键词**: `点云分类` `几何投影` `传感器无关` `激光雷达` `树种识别` `深度学习`

## 📋 核心要点

1. 核心问题：从点云数据中分类树种，需处理不同传感器（如移动和航空激光扫描）的数据差异。
2. 方法要点：将局部几何信息（法向量估计）嵌入二维投影，作为YOLOv11图像分类网络的输入。
3. 实验或效果：在MLS数据上总体准确率达95.5%，ALS数据上达91.8%，多光谱强度信息提升性能。

## 📄 摘要（原文）

> Laser scanning has proven to be an invaluable tool in assessing the decomposition of forest environments. Mobile laser scanning (MLS) has shown to be highly promising for extremely accurate, tree level inventory. In this study, we present NormalView, a sensor-agnostic projection-based deep learning method for classifying tree species from point cloud data. NormalView embeds local geometric information into two-dimensional projections, in the form of normal vector estimates, and uses the projections as inputs to an image classification network, YOLOv11. In addition, we inspected the effect of multispectral radiometric intensity information on classification performance. We trained and tested our model on high-density MLS data (7 species, ~5000 pts/m^2), as well as high-density airborne laser scanning (ALS) data (9 species, >1000 pts/m^2). On the MLS data, NormalView achieves an overall accuracy (macro-average accuracy) of 95.5 % (94.8 %), and 91.8 % (79.1 %) on the ALS data. We found that having intensity information from multiple scanners provides benefits in tree species classification, and the best model on the multispectral ALS dataset was a model using intensity information from all three channels of the multispectral ALS. This study demonstrates that projection-based methods, when enhanced with geometric information and coupled with state-of-the-art image classification backbones, can achieve exceptional results. Crucially, these methods are sensor-agnostic, relying only on geometric information. Additionally, we publically release the MLS dataset used in the study.

