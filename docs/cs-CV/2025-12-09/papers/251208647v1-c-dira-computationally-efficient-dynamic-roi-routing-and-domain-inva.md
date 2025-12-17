---
layout: default
title: C-DIRA: Computationally Efficient Dynamic ROI Routing and Domain-Invariant Adversarial Learning for Lightweight Driver Behavior Recognition
---

# C-DIRA: Computationally Efficient Dynamic ROI Routing and Domain-Invariant Adversarial Learning for Lightweight Driver Behavior Recognition

**arXiv**: [2512.08647v1](https://arxiv.org/abs/2512.08647) | [PDF](https://arxiv.org/pdf/2512.08647.pdf)

**作者**: Keito Inoshita

---

## 💡 一句话要点

**提出C-DIRA框架，通过动态ROI路由和域不变对抗学习，实现轻量级驾驶员行为识别的高效与泛化。**

**关键词**: `驾驶员行为识别` `轻量级模型` `动态ROI路由` `域不变学习` `对抗学习` `边缘计算`

## 📋 核心要点

1. 核心问题：轻量模型在边缘设备上实时识别驾驶员分心行为时，难以平衡计算效率与细粒度特征提取，且泛化能力不足。
2. 方法要点：结合显著性驱动的Top-K ROI池化和融合分类进行局部特征提取，动态路由仅对高难度样本应用ROI推理，并利用伪域标注和对抗学习学习域不变特征。
3. 实验或效果：在State Farm数据集上，C-DIRA相比先前轻量模型，在保持高准确率的同时显著减少FLOPs和延迟，并在视觉退化及未见域中表现出鲁棒性。

## 📄 摘要（原文）

> Driver distraction behavior recognition using in-vehicle cameras demands real-time inference on edge devices. However, lightweight models often fail to capture fine-grained behavioral cues, resulting in reduced performance on unseen drivers or under varying conditions. ROI-based methods also increase computational cost, making it difficult to balance efficiency and accuracy. This work addresses the need for a lightweight architecture that overcomes these constraints. We propose Computationally efficient Dynamic region of Interest Routing and domain-invariant Adversarial learning for lightweight driver behavior recognition (C-DIRA). The framework combines saliency-driven Top-K ROI pooling and fused classification for local feature extraction and integration. Dynamic ROI routing enables selective computation by applying ROI inference only to high difficulty data samples. Moreover, pseudo-domain labeling and adversarial learning are used to learn domain-invariant features robust to driver and background variation. Experiments on the State Farm Distracted Driver Detection Dataset show that C-DIRA maintains high accuracy with significantly fewer FLOPs and lower latency than prior lightweight models. It also demonstrates robustness under visual degradation such as blur and low-light, and stable performance across unseen domains. These results confirm C-DIRA's effectiveness in achieving compactness, efficiency, and generalization.

