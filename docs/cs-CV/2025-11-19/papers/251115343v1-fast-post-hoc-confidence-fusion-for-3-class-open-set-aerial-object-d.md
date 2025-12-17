---
layout: default
title: Fast Post-Hoc Confidence Fusion for 3-Class Open-Set Aerial Object Detection
---

# Fast Post-Hoc Confidence Fusion for 3-Class Open-Set Aerial Object Detection

**arXiv**: [2511.15343v1](https://arxiv.org/abs/2511.15343) | [PDF](https://arxiv.org/pdf/2511.15343.pdf)

**作者**: Spyridon Loukovitis, Vasileios Karampinis, Athanasios Voulodimos

---

## 💡 一句话要点

**提出轻量级后处理框架，实现无人机导航中的三类别开放集目标检测**

**关键词**: `开放集检测` `无人机导航` `后处理框架` `置信度融合` `三类别分类` `多层感知机`

## 📋 核心要点

1. 核心问题：开放集检测需同时处理已知和未知对象，现有方法依赖单一阈值，灵活性不足。
2. 方法要点：使用多层感知机融合多置信度估计，实现ID、OOD和背景的三类别分类。
3. 实验效果：在AUROC上平均提升2.7%，开放集mAP保持或改进，闭集mAP最高提升9点。

## 📄 摘要（原文）

> Developing reliable UAV navigation systems requires robust air-to-air object detectors capable of distinguishing between objects seen during training and previously unseen objects. While many methods address closed-set detection and achieve high-confidence recognition of in-domain (ID) targets, they generally do not tackle open-set detection, which requires simultaneous handling of both ID and out-of-distribution (OOD) objects. Existing open-set approaches typically rely on a single uncertainty score with thresholding, limiting flexibility and often conflating OOD objects with background clutter. In contrast, we propose a lightweight, model-agnostic post-processing framework that explicitly separates background from unknown objects while preserving the base detector's performance. Our approach extends open-set detection beyond binary ID/OOD classification to real-time three-way classification among ID targets, OOD objects, and background. To this end, we employ a fusion scheme that aggregates multiple confidence estimates and per-detection features using a compact multilayer perceptron (MLP). Incorporating different logit variants into the MLP consistently enhances performance across both binary and three-class classification without compromising throughput. Extensive ablation and comparative experiments confirm that our method surpasses threshold-based baselines in two-class classification by an average of 2.7% AUROC, while retaining or improving open-set mAP. Furthermore, our study uniquely enables robust three-class classification, a critical capability for safe UAV navigation, where OOD objects must be actively avoided and background regions safely ignored. Comparative analysis highlights that our method surpasses competitive techniques in AUROC across datasets, while improving closed-set mAP by up to 9 points, an 18% relative gain.

