---
layout: default
title: Sharp Monocular View Synthesis in Less Than a Second
---

# Sharp Monocular View Synthesis in Less Than a Second

**arXiv**: [2512.10685v1](https://arxiv.org/abs/2512.10685) | [PDF](https://arxiv.org/pdf/2512.10685.pdf)

**作者**: Lars Mescheder, Wei Dong, Shiwei Li, Xuyang Bai, Marcel Santos, Peiyun Hu, Bruno Lecouat, Mingmin Zhen, Amaël Delaunoy, Tian Fang, Yanghai Tsin, Stephan R. Richter, Vladlen Koltun

---

## 💡 一句话要点

**提出SHARP方法，通过单张图像实现快速逼真视图合成**

**关键词**: `单图像视图合成` `3D高斯表示` `快速渲染` `零样本泛化` `度量相机移动`

## 📋 核心要点

1. 核心问题：从单张图像生成高质量、逼真的新视图，需兼顾速度与精度。
2. 方法要点：使用神经网络前馈预测3D高斯表示参数，支持度量相机移动。
3. 实验或效果：在多个数据集上实现零样本泛化，显著降低LPIPS和DISTS指标，合成时间减少三个数量级。

## 📄 摘要（原文）

> We present SHARP, an approach to photorealistic view synthesis from a single image. Given a single photograph, SHARP regresses the parameters of a 3D Gaussian representation of the depicted scene. This is done in less than a second on a standard GPU via a single feedforward pass through a neural network. The 3D Gaussian representation produced by SHARP can then be rendered in real time, yielding high-resolution photorealistic images for nearby views. The representation is metric, with absolute scale, supporting metric camera movements. Experimental results demonstrate that SHARP delivers robust zero-shot generalization across datasets. It sets a new state of the art on multiple datasets, reducing LPIPS by 25-34% and DISTS by 21-43% versus the best prior model, while lowering the synthesis time by three orders of magnitude. Code and weights are provided at https://github.com/apple/ml-sharp

