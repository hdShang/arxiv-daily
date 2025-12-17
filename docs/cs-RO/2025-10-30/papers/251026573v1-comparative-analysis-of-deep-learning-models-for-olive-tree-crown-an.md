---
layout: default
title: Comparative Analysis of Deep Learning Models for Olive Tree Crown and Shadow Segmentation Towards Biovolume Estimation
---

# Comparative Analysis of Deep Learning Models for Olive Tree Crown and Shadow Segmentation Towards Biovolume Estimation

**arXiv**: [2510.26573v1](https://arxiv.org/abs/2510.26573) | [PDF](https://arxiv.org/pdf/2510.26573.pdf)

**作者**: Wondimagegn Abebe Demissie, Stefano Roccella, Rudy Rossetto, Antonio Minnocci, Andrea Vannini, Luca Sebastiani

---

## 💡 一句话要点

**比较U-Net、YOLOv11m-seg和Mask R-CNN用于橄榄树冠和阴影分割以估计生物体积**

**关键词**: `深度学习分割` `橄榄树生物体积估计` `UAV图像分析` `Mask R-CNN` `YOLOv11m-seg` `U-Net`

## 📋 核心要点

1. 核心问题：橄榄树生物体积估计对精准农业至关重要，尤其在气候压力下的地中海地区。
2. 方法要点：使用UAV图像，比较三种深度学习模型分割树冠和阴影，结合太阳几何估计生物体积。
3. 实验或效果：Mask R-CNN准确率最高，YOLOv11m-seg速度最快，生物体积估计范围4-24立方米。

## 📄 摘要（原文）

> Olive tree biovolume estimation is a key task in precision agriculture,
> supporting yield prediction and resource management, especially in
> Mediterranean regions severely impacted by climate-induced stress. This study
> presents a comparative analysis of three deep learning models U-Net,
> YOLOv11m-seg, and Mask RCNN for segmenting olive tree crowns and their shadows
> in ultra-high resolution UAV imagery. The UAV dataset, acquired over
> Vicopisano, Italy, includes manually annotated crown and shadow masks. Building
> on these annotations, the methodology emphasizes spatial feature extraction and
> robust segmentation; per-tree biovolume is then estimated by combining crown
> projected area with shadow-derived height using solar geometry. In testing,
> Mask R-CNN achieved the best overall accuracy (F1 = 0.86; mIoU = 0.72), while
> YOLOv11m-seg provided the fastest throughput (0.12 second per image). The
> estimated biovolumes spanned from approximately 4 to 24 cubic meters,
> reflecting clear structural differences among trees. These results indicate
> Mask R-CNN is preferable when biovolume accuracy is paramount, whereas
> YOLOv11m-seg suits large-area deployments where speed is critical; U-Net
> remains a lightweight, high-sensitivity option. The framework enables accurate,
> scalable orchard monitoring and can be further strengthened with DEM or DSM
> integration and field calibration for operational decision support.

