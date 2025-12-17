---
layout: default
title: Grab-3D: Detecting AI-Generated Videos from 3D Geometric Temporal Consistency
---

# Grab-3D: Detecting AI-Generated Videos from 3D Geometric Temporal Consistency

**arXiv**: [2512.13665v1](https://arxiv.org/abs/2512.13665) | [PDF](https://arxiv.org/pdf/2512.13665.pdf)

**作者**: Wenhan Chen, Sezer Karaoglu, Theo Gevers

---

## 💡 一句话要点

**提出Grab-3D框架，基于3D几何时间一致性检测AI生成视频**

**关键词**: `AI生成视频检测` `3D几何一致性` `Transformer框架` `消失点分析` `跨域泛化`

## 📋 核心要点

1. 核心问题：现有方法对AI生成视频中3D几何模式探索有限，需可靠检测机制
2. 方法要点：使用消失点表示3D几何，设计几何感知Transformer，注入几何位置编码和注意力
3. 实验或效果：在静态场景数据集上验证，显著优于现有检测器，具有跨域泛化能力

## 📄 摘要（原文）

> Recent advances in diffusion-based generation techniques enable AI models to produce highly realistic videos, heightening the need for reliable detection mechanisms. However, existing detection methods provide only limited exploration of the 3D geometric patterns present in generated videos. In this paper, we use vanishing points as an explicit representation of 3D geometry patterns, revealing fundamental discrepancies in geometric consistency between real and AI-generated videos. We introduce Grab-3D, a geometry-aware transformer framework for detecting AI-generated videos based on 3D geometric temporal consistency. To enable reliable evaluation, we construct an AI-generated video dataset of static scenes, allowing stable 3D geometric feature extraction. We propose a geometry-aware transformer equipped with geometric positional encoding, temporal-geometric attention, and an EMA-based geometric classifier head to explicitly inject 3D geometric awareness into temporal modeling. Experiments demonstrate that Grab-3D significantly outperforms state-of-the-art detectors, achieving robust cross-domain generalization to unseen generators.

