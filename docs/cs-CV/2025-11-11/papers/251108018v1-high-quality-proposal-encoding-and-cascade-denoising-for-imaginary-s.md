---
layout: default
title: High-Quality Proposal Encoding and Cascade Denoising for Imaginary Supervised Object Detection
---

# High-Quality Proposal Encoding and Cascade Denoising for Imaginary Supervised Object Detection

**arXiv**: [2511.08018v1](https://arxiv.org/abs/2511.08018) | [PDF](https://arxiv.org/pdf/2511.08018.pdf)

**作者**: Zhiyuan Chen, Yuelin Guo, Zitong Huang, Haoyu He, Renhao Lu, Weizhe Zhang

---

## 💡 一句话要点

**提出Cascade HQP-DETR以解决虚构监督目标检测中的数据质量、收敛慢和噪声过拟合问题**

**关键词**: `虚构监督目标检测` `查询初始化` `级联去噪` `合成数据生成` `DETR架构`

## 📋 核心要点

1. 核心问题：合成数据质量差、DETR收敛慢、伪标签噪声导致过拟合
2. 方法要点：高质量数据生成、基于SAM的查询初始化、级联去噪训练
3. 实验或效果：仅训练12epochs，在PASCAL VOC上达到61.04% mAP@0.5

## 📄 摘要（原文）

> Object detection models demand large-scale annotated datasets, which are costly and labor-intensive to create. This motivated Imaginary Supervised Object Detection (ISOD), where models train on synthetic images and test on real images. However, existing methods face three limitations: (1) synthetic datasets suffer from simplistic prompts, poor image quality, and weak supervision; (2) DETR-based detectors, due to their random query initialization, struggle with slow convergence and overfitting to synthetic patterns, hindering real-world generalization; (3) uniform denoising pressure promotes model overfitting to pseudo-label noise. We propose Cascade HQP-DETR to address these limitations. First, we introduce a high-quality data pipeline using LLaMA-3, Flux, and Grounding DINO to generate the FluxVOC and FluxCOCO datasets, advancing ISOD from weak to full supervision. Second, our High-Quality Proposal guided query encoding initializes object queries with image-specific priors from SAM-generated proposals and RoI-pooled features, accelerating convergence while steering the model to learn transferable features instead of overfitting to synthetic patterns. Third, our cascade denoising algorithm dynamically adjusts training weights through progressively increasing IoU thresholds across decoder layers, guiding the model to learn robust boundaries from reliable visual cues rather than overfitting to noisy labels. Trained for just 12 epochs solely on FluxVOC, Cascade HQP-DETR achieves a SOTA 61.04\% mAP@0.5 on PASCAL VOC 2007, outperforming strong baselines, with its competitive real-data performance confirming the architecture's universal applicability.

