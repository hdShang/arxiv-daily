---
layout: default
title: UnityVideo: Unified Multi-Modal Multi-Task Learning for Enhancing World-Aware Video Generation
---

# UnityVideo: Unified Multi-Modal Multi-Task Learning for Enhancing World-Aware Video Generation

**arXiv**: [2512.07831v1](https://arxiv.org/abs/2512.07831) | [PDF](https://arxiv.org/pdf/2512.07831.pdf)

**作者**: Jiehui Huang, Yuechen Zhang, Xu He, Yuan Gao, Zhi Cen, Bin Xia, Yan Zhou, Xin Tao, Pengfei Wan, Jiaya Jia

---

## 💡 一句话要点

**提出UnityVideo统一多模态多任务学习框架，以增强世界感知视频生成能力。**

**关键词**: `多模态视频生成` `世界感知学习` `统一训练框架` `零样本泛化` `动态噪声` `上下文学习`

## 📋 核心要点

1. 核心问题：现有视频生成模型受限于单模态条件，缺乏跨模态交互和模态多样性，影响世界理解。
2. 方法要点：采用动态噪声统一异构训练范式，结合模态切换器和上下文学习器实现多模态统一处理。
3. 实验或效果：构建大规模数据集，通过联合优化加速收敛，提升零样本泛化能力，改善视频质量和物理一致性。

## 📄 摘要（原文）

> Recent video generation models demonstrate impressive synthesis capabilities but remain limited by single-modality conditioning, constraining their holistic world understanding. This stems from insufficient cross-modal interaction and limited modal diversity for comprehensive world knowledge representation. To address these limitations, we introduce UnityVideo, a unified framework for world-aware video generation that jointly learns across multiple modalities (segmentation masks, human skeletons, DensePose, optical flow, and depth maps) and training paradigms. Our approach features two core components: (1) dynamic noising to unify heterogeneous training paradigms, and (2) a modality switcher with an in-context learner that enables unified processing via modular parameters and contextual learning. We contribute a large-scale unified dataset with 1.3M samples. Through joint optimization, UnityVideo accelerates convergence and significantly enhances zero-shot generalization to unseen data. We demonstrate that UnityVideo achieves superior video quality, consistency, and improved alignment with physical world constraints. Code and data can be found at: https://github.com/dvlab-research/UnityVideo

