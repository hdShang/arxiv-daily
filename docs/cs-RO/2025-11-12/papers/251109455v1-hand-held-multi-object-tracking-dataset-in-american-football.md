---
layout: default
title: Hand Held Multi-Object Tracking Dataset in American Football
---

# Hand Held Multi-Object Tracking Dataset in American Football

**arXiv**: [2511.09455v1](https://arxiv.org/abs/2511.09455) | [PDF](https://arxiv.org/pdf/2511.09455.pdf)

**作者**: Rintaro Otsubo, Kanta Sawafuji, Hideo Saito

---

## 💡 一句话要点

**提出首个美式足球多目标跟踪数据集，解决高密度场景下玩家跟踪难题**

**关键词**: `多目标跟踪` `美式足球数据集` `玩家检测` `重识别模型` `高密度场景` `微调优化`

## 📋 核心要点

1. 核心问题：美式足球中玩家频繁遮挡和接触，缺乏标准化数据集，难以公平比较跟踪方法
2. 方法要点：构建专用检测与跟踪数据集，集成微调检测器和重识别模型提升跟踪系统
3. 实验或效果：在拥挤场景中实现准确跟踪，微调模型优于预训练模型，跟踪精度显著提高

## 📄 摘要（原文）

> Multi-Object Tracking (MOT) plays a critical role in analyzing player behavior from videos, enabling performance evaluation. Current MOT methods are often evaluated using publicly available datasets. However, most of these focus on everyday scenarios such as pedestrian tracking or are tailored to specific sports, including soccer and basketball. Despite the inherent challenges of tracking players in American football, such as frequent occlusion and physical contact, no standardized dataset has been publicly available, making fair comparisons between methods difficult. To address this gap, we constructed the first dedicated detection and tracking dataset for the American football players and conducted a comparative evaluation of various detection and tracking methods. Our results demonstrate that accurate detection and tracking can be achieved even in crowded scenarios. Fine-tuning detection models improved performance over pre-trained models. Furthermore, when these fine-tuned detectors and re-identification models were integrated into tracking systems, we observed notable improvements in tracking accuracy compared to existing approaches. This work thus enables robust detection and tracking of American football players in challenging, high-density scenarios previously underserved by conventional methods.

