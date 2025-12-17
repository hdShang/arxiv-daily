---
layout: default
title: StreetView-Waste: A Multi-Task Dataset for Urban Waste Management
---

# StreetView-Waste: A Multi-Task Dataset for Urban Waste Management

**arXiv**: [2511.16440v1](https://arxiv.org/abs/2511.16440) | [PDF](https://arxiv.org/pdf/2511.16440.pdf)

**作者**: Diogo J. Paulo, João Martins, Hugo Proença, João C. Neves

---

## 💡 一句话要点

**提出StreetView-Waste数据集以解决城市垃圾管理中的多任务视觉感知问题**

**关键词**: `垃圾容器检测` `目标跟踪` `语义分割` `城市视觉数据集` `几何先验` `启发式方法`

## 📋 核心要点

1. 核心问题：现有垃圾检测数据集缺乏对溢出容器跟踪和动态场景的标注，限制实际应用。
2. 方法要点：提供多任务数据集，并引入启发式跟踪和几何先验框架提升性能。
3. 实验或效果：启发式方法减少计数误差79.6%，几何策略提升分割mAP@0.5 27%。

## 📄 摘要（原文）

> Urban waste management remains a critical challenge for the development of smart cities. Despite the growing number of litter detection datasets, the problem of monitoring overflowing waste containers, particularly from images captured by garbage trucks, has received little attention. While existing datasets are valuable, they often lack annotations for specific container tracking or are captured in static, decontextualized environments, limiting their utility for real-world logistics. To address this gap, we present StreetView-Waste, a comprehensive dataset of urban scenes featuring litter and waste containers. The dataset supports three key evaluation tasks: (1) waste container detection, (2) waste container tracking, and (3) waste overflow segmentation. Alongside the dataset, we provide baselines for each task by benchmarking state-of-the-art models in object detection, tracking, and segmentation. Additionally, we enhance baseline performance by proposing two complementary strategies: a heuristic-based method for improved waste container tracking and a model-agnostic framework that leverages geometric priors to refine litter segmentation. Our experimental results show that while fine-tuned object detectors achieve reasonable performance in detecting waste containers, baseline tracking methods struggle to accurately estimate their number; however, our proposed heuristics reduce the mean absolute counting error by 79.6%. Similarly, while segmenting amorphous litter is challenging, our geometry-aware strategy improves segmentation mAP@0.5 by 27% on lightweight models, demonstrating the value of multimodal inputs for this task. Ultimately, StreetView-Waste provides a challenging benchmark to encourage research into real-world perception systems for urban waste management.

