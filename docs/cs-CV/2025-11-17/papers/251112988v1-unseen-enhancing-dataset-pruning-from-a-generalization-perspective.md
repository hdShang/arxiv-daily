---
layout: default
title: UNSEEN: Enhancing Dataset Pruning from a Generalization Perspective
---

# UNSEEN: Enhancing Dataset Pruning from a Generalization Perspective

**arXiv**: [2511.12988v1](https://arxiv.org/abs/2511.12988) | [PDF](https://arxiv.org/pdf/2511.12988.pdf)

**作者**: Furui Xu, Shaobo Wang, Jiajun Zhang, Chenghao Sun, Haixiang Tang, Linfeng Zhang

---

## 💡 一句话要点

**提出UNSEEN框架从泛化视角增强数据集剪枝，提升核心集性能**

**关键词**: `数据集剪枝` `泛化评分` `核心集优化` `多步选择` `模型训练效率`

## 📋 核心要点

1. 数据集剪枝中样本评分密集化，降低选择区分度，影响核心集构建
2. 基于未训练模型评分样本，并扩展至多步增量选择优化核心集质量
3. 在CIFAR和ImageNet上显著优于SOTA方法，ImageNet-1K剪枝30%无损性能

## 📄 摘要（原文）

> The growing scale of datasets in deep learning has introduced significant computational challenges. Dataset pruning addresses this challenge by constructing a compact but informative coreset from the full dataset with comparable performance. Previous approaches typically establish scoring metrics based on specific criteria to identify representative samples. However, these methods predominantly rely on sample scores obtained from the model's performance during the training (i.e., fitting) phase. As scoring models achieve near-optimal performance on training data, such fitting-centric approaches induce a dense distribution of sample scores within a narrow numerical range. This concentration reduces the distinction between samples and hinders effective selection. To address this challenge, we conduct dataset pruning from the perspective of generalization, i.e., scoring samples based on models not exposed to them during training. We propose a plug-and-play framework, UNSEEN, which can be integrated into existing dataset pruning methods. Additionally, conventional score-based methods are single-step and rely on models trained solely on the complete dataset, providing limited perspective on the importance of samples. To address this limitation, we scale UNSEEN to multi-step scenarios and propose an incremental selection technique through scoring models trained on varying coresets, and optimize the quality of the coreset dynamically. Extensive experiments demonstrate that our method significantly outperforms existing state-of-the-art (SOTA) methods on CIFAR-10, CIFAR-100, and ImageNet-1K. Notably, on ImageNet-1K, UNSEEN achieves lossless performance while reducing training data by 30\%.

