---
layout: default
title: CNN-Based Framework for Pedestrian Age and Gender Classification Using Far-View Surveillance in Mixed-Traffic Intersections
---

# CNN-Based Framework for Pedestrian Age and Gender Classification Using Far-View Surveillance in Mixed-Traffic Intersections

**arXiv**: [2511.22873v1](https://arxiv.org/abs/2511.22873) | [PDF](https://arxiv.org/pdf/2511.22873.pdf)

**作者**: Shisir Shahriar Arif, Md. Muhtashim Shahrier, Nazmul Haque, Md Asif Raihan, Md. Hadiuzzaman

---

## 💡 一句话要点

**提出基于CNN的远视监控框架，用于混合交通路口行人年龄与性别分类。**

**关键词**: `行人分类` `远视监控` `卷积神经网络` `混合交通` `实时推理` `人口统计`

## 📋 核心要点

1. 核心问题：混合交通路口行人安全监控中，年龄与性别等人口统计信息缺失，影响针对性干预。
2. 方法要点：使用CNN从远视监控视频中基于全身视觉线索，统一分类为六类（成人、青少年、儿童的男女）。
3. 实验或效果：在孟加拉国达卡路口数据上，ResNet50模型达86.19%准确率，轻量CNN达84.15%，支持实时推理。

## 📄 摘要（原文）

> Pedestrian safety remains a pressing concern in congested urban intersections, particularly in low- and middle-income countries where traffic is multimodal, and infrastructure often lacks formal control. Demographic factors like age and gender significantly influence pedestrian vulnerability, yet real-time monitoring systems rarely capture this information. To address this gap, this study proposes a deep learning framework that classifies pedestrian age group and gender from far-view intersection footage using convolutional neural networks (CNNs), without relying on facial recognition or high-resolution imagery. The classification is structured as a unified six-class problem, distinguishing adult, teenager, and child pedestrians for both males and females, based on full-body visual cues. Video data was collected from three high-risk intersections in Dhaka, Bangladesh. Two CNN architectures were implemented: ResNet50, a deep convolutional neural network pretrained on ImageNet, and a custom lightweight CNN optimized for computational efficiency. Eight model variants explored combinations of pooling strategies and optimizers. ResNet50 with Max Pooling and SGD achieved the highest accuracy (86.19%), while the custom CNN performed comparably (84.15%) with fewer parameters and faster training. The model's efficient design enables real-time inference on standard surveillance feeds. For practitioners, this system provides a scalable, cost-effective tool to monitor pedestrian demographics at intersections using existing camera infrastructure. Its outputs can shape intersection design, optimize signal timing, and enable targeted safety interventions for vulnerable groups such as children or the elderly. By offering demographic insights often missing in conventional traffic data, the framework supports more inclusive, data-driven planning in mixed-traffic environments.

