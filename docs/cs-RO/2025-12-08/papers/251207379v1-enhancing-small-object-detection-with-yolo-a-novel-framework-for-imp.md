---
layout: default
title: Enhancing Small Object Detection with YOLO: A Novel Framework for Improved Accuracy and Efficiency
---

# Enhancing Small Object Detection with YOLO: A Novel Framework for Improved Accuracy and Efficiency

**arXiv**: [2512.07379v1](https://arxiv.org/abs/2512.07379) | [PDF](https://arxiv.org/pdf/2512.07379.pdf)

**作者**: Mahila Moghadami, Mohammad Ali Keyvanrad, Melika Sabaghian

---

## 💡 一句话要点

**提出基于YOLO的增强框架，通过裁剪优化与架构改进提升航拍图像中小目标检测的准确率与效率**

**关键词**: `小目标检测` `航拍图像` `YOLO框架` `特征增强` `滑动窗口裁剪` `注意力机制`

## 📋 核心要点

1. 核心问题：航拍图像中小目标检测准确率低，现有方法依赖图像裁剪和网络架构调整
2. 方法要点：改进SW-YOLO的裁剪策略，在骨干网络集成CBAM，并设计新头部以增强特征提取
3. 实验或效果：在VisDrone2019数据集上，mAP .5.5从YOLOv5L的35.5提升至61.2，优于SAHI和CZDet

## 📄 摘要（原文）

> This paper investigates and develops methods for detecting small objects in large-scale aerial images. Current approaches for detecting small objects in aerial images often involve image cropping and modifications to detector network architectures. Techniques such as sliding window cropping and architectural enhancements, including higher-resolution feature maps and attention mechanisms, are commonly employed. Given the growing importance of aerial imagery in various critical and industrial applications, the need for robust frameworks for small object detection becomes imperative. To address this need, we adopted the base SW-YOLO approach to enhance speed and accuracy in small object detection by refining cropping dimensions and overlap in sliding window usage and subsequently enhanced it through architectural modifications. we propose a novel model by modifying the base model architecture, including advanced feature extraction modules in the neck for feature map enhancement, integrating CBAM in the backbone to preserve spatial and channel information, and introducing a new head to boost small object detection accuracy. Finally, we compared our method with SAHI, one of the most powerful frameworks for processing large-scale images, and CZDet, which is also based on image cropping, achieving significant improvements in accuracy. The proposed model achieves significant accuracy gains on the VisDrone2019 dataset, outperforming baseline YOLOv5L detection by a substantial margin. Specifically, the final proposed model elevates the mAP .5.5 accuracy on the VisDrone2019 dataset from the base accuracy of 35.5 achieved by the YOLOv5L detector to 61.2. Notably, the accuracy of CZDet, which is another classic method applied to this dataset, is 58.36. This research demonstrates a significant improvement, achieving an increase in accuracy from 35.5 to 61.2.

