---
layout: default
title: Saliency-Guided Deep Learning for Bridge Defect Detection in Drone Imagery
---

# Saliency-Guided Deep Learning for Bridge Defect Detection in Drone Imagery

**arXiv**: [2511.14040v1](https://arxiv.org/abs/2511.14040) | [PDF](https://arxiv.org/pdf/2511.14040.pdf)

**作者**: Loucif Hebbache, Dariush Amirkhani, Mohand Saïd Allili, Jean-François Lapointe

---

## 💡 一句话要点

**提出基于显著性的深度学习方法，用于无人机图像中的桥梁缺陷检测**

**关键词**: `桥梁缺陷检测` `显著性检测` `YOLOX` `无人机图像` `异常检测`

## 📋 核心要点

1. 核心问题：桥梁缺陷检测在无人机图像中面临异常物体检测与分类的挑战
2. 方法要点：结合显著性区域提议与YOLOX检测器，对显著区域进行亮度增强
3. 实验或效果：在标准数据集上验证了方法的准确性和计算效率

## 📄 摘要（原文）

> Anomaly object detection and classification are one of the main challenging tasks in computer vision and pattern recognition. In this paper, we propose a new method to automatically detect, localize and classify defects in concrete bridge structures using drone imagery. This framework is constituted of two main stages. The first stage uses saliency for defect region proposals where defects often exhibit local discontinuities in the normal surface patterns with regard to their surrounding. The second stage employs a YOLOX-based deep learning detector that operates on saliency-enhanced images obtained by applying bounding-box level brightness augmentation to salient defect regions. Experimental results on standard datasets confirm the performance of our framework and its suitability in terms of accuracy and computational efficiency, which give a huge potential to be implemented in a self-powered inspection system.

