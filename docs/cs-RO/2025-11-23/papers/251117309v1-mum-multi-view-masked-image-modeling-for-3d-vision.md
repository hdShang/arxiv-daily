---
layout: default
title: MuM: Multi-View Masked Image Modeling for 3D Vision
---

# MuM: Multi-View Masked Image Modeling for 3D Vision

**arXiv**: [2511.17309v1](https://arxiv.org/abs/2511.17309) | [PDF](https://arxiv.org/pdf/2511.17309.pdf)

**作者**: David Nordström, Johan Edstedt, Fredrik Kahl, Georg Bökman

---

## 💡 一句话要点

**提出多视图掩码图像建模方法以增强3D视觉特征学习**

**关键词**: `多视图学习` `掩码图像建模` `3D视觉` `自监督学习` `几何推理`

## 📋 核心要点

1. 核心问题：现有自监督学习模型如DINOv3侧重语义理解，缺乏几何推理能力。
2. 方法要点：扩展MAE至多视图，统一掩码并使用轻量解码器与帧间注意力。
3. 实验或效果：在重建、匹配和姿态估计任务中优于DINOv3和CroCo v2。

## 📄 摘要（原文）

> Self-supervised learning on images seeks to extract meaningful visual representations from unlabeled data. When scaled to large datasets, this paradigm has achieved state-of-the-art performance and the resulting trained models such as DINOv3 have seen widespread adoption. However, most prior efforts are optimized for semantic understanding rather than geometric reasoning. One important exception is Cross-View Completion, CroCo, which is a form of masked autoencoding (MAE) tailored for 3D understanding. In this work, we continue on the path proposed by CroCo and focus on learning features tailored for 3D vision. In a nutshell, we extend MAE to arbitrarily many views of the same scene. By uniformly masking all views and employing a lightweight decoder with inter-frame attention, our approach is inherently simpler and more scalable than CroCo. We evaluate the resulting model, MuM, extensively on downstream tasks including feedforward reconstruction, dense image matching and relative pose estimation, finding that it outperforms the state-of-the-art visual encoders DINOv3 and CroCo v2.

