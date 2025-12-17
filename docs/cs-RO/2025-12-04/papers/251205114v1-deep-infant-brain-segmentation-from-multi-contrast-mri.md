---
layout: default
title: Deep infant brain segmentation from multi-contrast MRI
---

# Deep infant brain segmentation from multi-contrast MRI

**arXiv**: [2512.05114v1](https://arxiv.org/abs/2512.05114) | [PDF](https://arxiv.org/pdf/2512.05114.pdf)

**作者**: Malte Hoffmann, Lilla Zöllei, Adrian V. Dalca

---

## 💡 一句话要点

**提出BabySeg框架以解决婴儿脑MRI分割中的方法碎片化问题**

**关键词**: `婴儿脑分割` `多对比MRI` `域随机化` `深度学习框架` `医学图像分析`

## 📋 核心要点

1. 核心问题：婴儿脑MRI分割因发育、成像限制和模态不一致而困难，现有方法碎片化。
2. 方法要点：基于域随机化技术合成训练图像，增强模型对数据集偏移的鲁棒性。
3. 实验或效果：在多种年龄组和输入配置下，单模型实现最先进性能，运行时间短。

## 📄 摘要（原文）

> Segmentation of magnetic resonance images (MRI) facilitates analysis of human brain development by delineating anatomical structures. However, in infants and young children, accurate segmentation is challenging due to development and imaging constraints. Pediatric brain MRI is notoriously difficult to acquire, with inconsistent availability of imaging modalities, substantial non-head anatomy in the field of view, and frequent motion artifacts. This has led to specialized segmentation models that are often limited to specific image types or narrow age groups, or that are fragile for more variable images such as those acquired clinically. We address this method fragmentation with BabySeg, a deep learning brain segmentation framework for infants and young children that supports diverse MRI protocols, including repeat scans and image types unavailable during training. Our approach builds on recent domain randomization techniques, which synthesize training images far beyond realistic bounds to promote dataset shift invariance. We also describe a mechanism that enables models to flexibly pool and interact features from any number of input scans. We demonstrate state-of-the-art performance that matches or exceeds the accuracy of several existing methods for various age cohorts and input configurations using a single model, in a fraction of the runtime required by many existing tools.

