---
layout: default
title: End-to-End Motion Capture from Rigid Body Markers with Geodesic Loss
---

# End-to-End Motion Capture from Rigid Body Markers with Geodesic Loss

**arXiv**: [2511.16418v1](https://arxiv.org/abs/2511.16418) | [PDF](https://arxiv.org/pdf/2511.16418.pdf)

**作者**: Hai Lan, Zongyan Li, Jianmin Hu, Jialing Yang, Houde Dai

---

## 💡 一句话要点

**提出基于刚性体标记和测地损失的方法，实现实时高精度运动捕捉**

**关键词**: `运动捕捉` `刚性体标记` `测地损失` `SMPL参数估计` `端到端学习`

## 📋 核心要点

1. 核心问题：传统光学运动捕捉依赖密集标记，存在设置耗时和标记识别模糊问题
2. 方法要点：使用刚性体标记提供6自由度数据，结合测地损失端到端回归SMPL参数
3. 实验或效果：在合成和真实数据上达到先进精度，计算效率比优化方法高一个数量级

## 📄 摘要（原文）

> Marker-based optical motion capture (MoCap), while long regarded as the gold standard for accuracy, faces practical challenges, such as time-consuming preparation and marker identification ambiguity, due to its reliance on dense marker configurations, which fundamentally limit its scalability. To address this, we introduce a novel fundamental unit for MoCap, the Rigid Body Marker (RBM), which provides unambiguous 6-DoF data and drastically simplifies setup. Leveraging this new data modality, we develop a deep-learning-based regression model that directly estimates SMPL parameters under a geodesic loss. This end-to-end approach matches the performance of optimization-based methods while requiring over an order of magnitude less computation. Trained on synthesized data from the AMASS dataset, our end-to-end model achieves state-of-the-art accuracy in body pose estimation. Real-world data captured using a Vicon optical tracking system further demonstrates the practical viability of our approach. Overall, the results show that combining sparse 6-DoF RBM with a manifold-aware geodesic loss yields a practical and high-fidelity solution for real-time MoCap in graphics, virtual reality, and biomechanics.

