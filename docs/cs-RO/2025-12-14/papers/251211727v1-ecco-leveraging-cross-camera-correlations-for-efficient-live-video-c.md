---
layout: default
title: ECCO: Leveraging Cross-Camera Correlations for Efficient Live Video Continuous Learning
---

# ECCO: Leveraging Cross-Camera Correlations for Efficient Live Video Continuous Learning

**arXiv**: [2512.11727v1](https://arxiv.org/abs/2512.11727) | [PDF](https://arxiv.org/pdf/2512.11727.pdf)

**作者**: Yuze He, Ferdi Kossmann, Srinivasan Seshan, Peter Steenkiste

---

## 💡 一句话要点

**提出ECCO框架，利用跨摄像头相关性实现高效视频连续学习**

**关键词**: `视频分析` `连续学习` `摄像头分组` `资源优化` `动态重训练`

## 📋 核心要点

1. 核心问题：单摄像头独立重训练模型导致计算和通信成本高，难以扩展
2. 方法要点：动态分组摄像头共享模型，优化GPU分配和传输控制
3. 实验或效果：在相同资源下提升重训练精度6.7%-18.1%，或支持3.3倍并发摄像头

## 📄 摘要（原文）

> Recent advances in video analytics address real-time data drift by continuously retraining specialized, lightweight DNN models for individual cameras. However, the current practice of retraining a separate model for each camera suffers from high compute and communication costs, making it unscalable. We present ECCO, a new video analytics framework designed for resource-efficient continuous learning. The key insight is that the data drift, which necessitates model retraining, often shows temporal and spatial correlations across nearby cameras. By identifying cameras that experience similar drift and retraining a shared model for them, ECCO can substantially reduce the associated compute and communication costs. Specifically, ECCO introduces: (i) a lightweight grouping algorithm that dynamically forms and updates camera groups; (ii) a GPU allocator that dynamically assigns GPU resources across different groups to improve retraining accuracy and ensure fairness; and (iii) a transmission controller at each camera that configures frame sampling and coordinates bandwidth sharing with other cameras based on its assigned GPU resources. We conducted extensive evaluations on three distinctive datasets for two vision tasks. Compared to leading baselines, ECCO improves retraining accuracy by 6.7%-18.1% using the same compute and communication resources, or supports 3.3 times more concurrent cameras at the same accuracy.

