---
layout: default
title: Unmasking Facial DeepFakes: A Robust Multiview Detection Framework for Natural Images
---

# Unmasking Facial DeepFakes: A Robust Multiview Detection Framework for Natural Images

**arXiv**: [2510.15576v1](https://arxiv.org/abs/2510.15576) | [PDF](https://arxiv.org/pdf/2510.15576.pdf)

**作者**: Sami Belguesmia, Mohand Saïd Allili, Assia Hamadene

---

## 💡 一句话要点

**提出多视图架构以增强自然图像中DeepFake检测的鲁棒性**

**关键词**: `DeepFake检测` `多视图架构` `面部特征分析` `姿态鲁棒性` `图像伪造识别`

## 📋 核心要点

1. 核心问题：现有DeepFake检测方法难以应对姿态变化、遮挡和真实世界中的伪影
2. 方法要点：集成全局、中观和局部视图编码器，分析边界、纹理和面部区域失真
3. 实验或效果：在挑战性数据集上表现优于传统单视图方法，适应多种姿态和光照条件

## 📄 摘要（原文）

> DeepFake technology has advanced significantly in recent years, enabling the
> creation of highly realistic synthetic face images. Existing DeepFake detection
> methods often struggle with pose variations, occlusions, and artifacts that are
> difficult to detect in real-world conditions. To address these challenges, we
> propose a multi-view architecture that enhances DeepFake detection by analyzing
> facial features at multiple levels. Our approach integrates three specialized
> encoders, a global view encoder for detecting boundary inconsistencies, a
> middle view encoder for analyzing texture and color alignment, and a local view
> encoder for capturing distortions in expressive facial regions such as the
> eyes, nose, and mouth, where DeepFake artifacts frequently occur. Additionally,
> we incorporate a face orientation encoder, trained to classify face poses,
> ensuring robust detection across various viewing angles. By fusing features
> from these encoders, our model achieves superior performance in detecting
> manipulated images, even under challenging pose and lighting
> conditions.Experimental results on challenging datasets demonstrate the
> effectiveness of our method, outperforming conventional single-view approaches

