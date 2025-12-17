---
layout: default
title: Unsupervised Image Classification with Adaptive Nearest Neighbor Selection and Cluster Ensembles
---

# Unsupervised Image Classification with Adaptive Nearest Neighbor Selection and Cluster Ensembles

**arXiv**: [2511.16213v1](https://arxiv.org/abs/2511.16213) | [PDF](https://arxiv.org/pdf/2511.16213.pdf)

**作者**: Melih Baydar, Emre Akbas

---

## 💡 一句话要点

**提出ICCE方法，通过自适应近邻选择和聚类集成提升无监督图像分类性能**

**关键词**: `无监督图像分类` `聚类集成` `自适应近邻选择` `多聚类头` `伪标签训练`

## 📋 核心要点

1. 核心问题：无监督图像分类需将未标注图像分组为语义类别，现有方法多忽略表示学习
2. 方法要点：使用多聚类头训练，结合自适应近邻选择和聚类集成生成共识聚类
3. 实验或效果：在CIFAR10、CIFAR100和ImageNet等基准上达到SOTA，ImageNet准确率超70%

## 📄 摘要（原文）

> Unsupervised image classification, or image clustering, aims to group unlabeled images into semantically meaningful categories. Early methods integrated representation learning and clustering within an iterative framework. However, the rise of foundational models have recently shifted focus solely to clustering, bypassing the representation learning step. In this work, we build upon a recent multi-head clustering approach by introducing adaptive nearest neighbor selection and cluster ensembling strategies to improve clustering performance. Our method, "Image Clustering through Cluster Ensembles" (ICCE), begins with a clustering stage, where we train multiple clustering heads on a frozen backbone, producing diverse image clusterings. We then employ a cluster ensembling technique to consolidate these potentially conflicting results into a unified consensus clustering. Finally, we train an image classifier using the consensus clustering result as pseudo-labels. ICCE achieves state-of-the-art performance on ten image classification benchmarks, achieving 99.3% accuracy on CIFAR10, 89% on CIFAR100, and 70.4% on ImageNet datasets, narrowing the performance gap with supervised methods. To the best of our knowledge, ICCE is the first fully unsupervised image classification method to exceed 70% accuracy on ImageNet.

