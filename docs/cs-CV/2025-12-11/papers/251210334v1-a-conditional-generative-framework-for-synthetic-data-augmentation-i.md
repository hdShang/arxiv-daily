---
layout: default
title: A Conditional Generative Framework for Synthetic Data Augmentation in Segmenting Thin and Elongated Structures in Biological Images
---

# A Conditional Generative Framework for Synthetic Data Augmentation in Segmenting Thin and Elongated Structures in Biological Images

**arXiv**: [2512.10334v1](https://arxiv.org/abs/2512.10334) | [PDF](https://arxiv.org/pdf/2512.10334.pdf)

**作者**: Yi Liu, Yichi Zhang

---

## 💡 一句话要点

**提出基于Pix2Pix的条件生成框架，以解决生物图像中细长结构分割的数据标注难题。**

**关键词**: `细长结构分割` `条件生成对抗网络` `合成数据增强` `生物图像分析` `结构感知损失`

## 📋 核心要点

1. 核心问题：细长丝状结构（如微管）在生物图像中分割时，高质量像素级标注数据获取困难，因密集分布和几何特性导致人工标注耗时费力。
2. 方法要点：基于Pix2Pix架构的条件生成框架，从二值掩码生成逼真的显微镜图像，并引入丝状结构感知损失以提升生成图像的结构相似性。
3. 实验或效果：实验验证了方法的有效性，优于未使用合成数据训练的现有模型，但具体性能指标未知。

## 📄 摘要（原文）

> Thin and elongated filamentous structures, such as microtubules and actin filaments, often play important roles in biological systems. Segmenting these filaments in biological images is a fundamental step for quantitative analysis. Recent advances in deep learning have significantly improved the performance of filament segmentation. However, there is a big challenge in acquiring high quality pixel-level annotated dataset for filamentous structures, as the dense distribution and geometric properties of filaments making manual annotation extremely laborious and time-consuming. To address the data shortage problem, we propose a conditional generative framework based on the Pix2Pix architecture to generate realistic filaments in microscopy images from binary masks. We also propose a filament-aware structural loss to improve the structure similarity when generating synthetic images. Our experiments have demonstrated the effectiveness of our approach and outperformed existing model trained without synthetic data.

