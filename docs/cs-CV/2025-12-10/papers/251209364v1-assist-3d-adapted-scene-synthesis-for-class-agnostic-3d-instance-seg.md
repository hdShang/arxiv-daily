---
layout: default
title: ASSIST-3D: Adapted Scene Synthesis for Class-Agnostic 3D Instance Segmentation
---

# ASSIST-3D: Adapted Scene Synthesis for Class-Agnostic 3D Instance Segmentation

**arXiv**: [2512.09364v1](https://arxiv.org/abs/2512.09364) | [PDF](https://arxiv.org/pdf/2512.09364.pdf)

**作者**: Shengchao Zhou, Jiehong Lin, Jiahui Liu, Shizhen Zhao, Chirui Chang, Xiaojuan Qi

---

## 💡 一句话要点

**提出ASSIST-3D以合成多样化场景数据，增强类无关3D实例分割的泛化能力**

**关键词**: `3D实例分割` `场景合成` `数据增强` `类无关学习` `点云处理` `泛化能力`

## 📋 核心要点

1. 核心问题：类无关3D实例分割因标注数据稀缺或噪声而泛化困难，现有合成方法难以兼顾几何多样性、上下文复杂性和布局合理性。
2. 方法要点：ASSIST-3D通过异构对象选择、LLM引导的布局生成和多视图点云构建，合成高质量训练数据。
3. 实验或效果：在ScanNetV2等基准测试中，使用ASSIST-3D数据训练的模型显著优于现有方法，验证了其有效性。

## 📄 摘要（原文）

> Class-agnostic 3D instance segmentation tackles the challenging task of segmenting all object instances, including previously unseen ones, without semantic class reliance. Current methods struggle with generalization due to the scarce annotated 3D scene data or noisy 2D segmentations. While synthetic data generation offers a promising solution, existing 3D scene synthesis methods fail to simultaneously satisfy geometry diversity, context complexity, and layout reasonability, each essential for this task. To address these needs, we propose an Adapted 3D Scene Synthesis pipeline for class-agnostic 3D Instance SegmenTation, termed as ASSIST-3D, to synthesize proper data for model generalization enhancement. Specifically, ASSIST-3D features three key innovations, including 1) Heterogeneous Object Selection from extensive 3D CAD asset collections, incorporating randomness in object sampling to maximize geometric and contextual diversity; 2) Scene Layout Generation through LLM-guided spatial reasoning combined with depth-first search for reasonable object placements; and 3) Realistic Point Cloud Construction via multi-view RGB-D image rendering and fusion from the synthetic scenes, closely mimicking real-world sensor data acquisition. Experiments on ScanNetV2, ScanNet++, and S3DIS benchmarks demonstrate that models trained with ASSIST-3D-generated data significantly outperform existing methods. Further comparisons underscore the superiority of our purpose-built pipeline over existing 3D scene synthesis approaches.

