---
layout: default
title: Automated Pollen Recognition in Optical and Holographic Microscopy Images
---

# Automated Pollen Recognition in Optical and Holographic Microscopy Images

**arXiv**: [2512.08589v1](https://arxiv.org/abs/2512.08589) | [PDF](https://arxiv.org/pdf/2512.08589.pdf)

**作者**: Swarn Singh Warshaneyan, Maksims Ivanovs, Blaž Cugmas, Inese Bērziņa, Laura Goldberga, Mindaugas Tamosiunas, Roberts Kadiķis

---

## 💡 一句话要点

**提出基于深度学习的自动化花粉识别方法，应用于光学与全息显微镜图像，提升兽医细胞学检测效率。**

**关键词**: `花粉识别` `深度学习` `光学显微镜` `全息显微镜` `目标检测` `图像分类`

## 📋 核心要点

1. 核心问题：自动化花粉检测与分类在光学和全息显微镜图像中性能差异大，全息图像初始准确率低。
2. 方法要点：使用YOLOv8s进行目标检测和MobileNetV3L进行分类，通过自动标注和边界框扩大扩展数据集。
3. 实验或效果：光学图像检测mAP50达91.3%，分类准确率97%；全息图像经优化后检测mAP50从2.49%提升至13.3%，分类准确率从42%提升至54%。

## 📄 摘要（原文）

> This study explores the application of deep learning to improve and automate pollen grain detection and classification in both optical and holographic microscopy images, with a particular focus on veterinary cytology use cases. We used YOLOv8s for object detection and MobileNetV3L for the classification task, evaluating their performance across imaging modalities. The models achieved 91.3% mAP50 for detection and 97% overall accuracy for classification on optical images, whereas the initial performance on greyscale holographic images was substantially lower. We addressed the performance gap issue through dataset expansion using automated labeling and bounding box area enlargement. These techniques, applied to holographic images, improved detection performance from 2.49% to 13.3% mAP50 and classification performance from 42% to 54%. Our work demonstrates that, at least for image classification tasks, it is possible to pair deep learning techniques with cost-effective lensless digital holographic microscopy devices.

