---
layout: default
title: NTK-Guided Implicit Neural Teaching
---

# NTK-Guided Implicit Neural Teaching

**arXiv**: [2511.15487v1](https://arxiv.org/abs/2511.15487) | [PDF](https://arxiv.org/pdf/2511.15487.pdf)

**作者**: Chen Zhang, Wei Zuo, Bingyang Cheng, Yikun Wang, Wei-Bin Kou, Yik Chung WU, Ngai Wong

---

## 💡 一句话要点

**提出NTK引导隐式神经教学以加速隐式神经表示训练**

**关键词**: `隐式神经表示` `神经正切核` `训练加速` `坐标采样` `函数逼近`

## 📋 核心要点

1. 隐式神经表示拟合高分辨率信号时计算成本高昂
2. 利用神经正切核动态选择坐标以最大化全局函数更新
3. 实验显示训练时间减半且保持或提升表示质量

## 📄 摘要（原文）

> Implicit Neural Representations (INRs) parameterize continuous signals via multilayer perceptrons (MLPs), enabling compact, resolution-independent modeling for tasks like image, audio, and 3D reconstruction. However, fitting high-resolution signals demands optimizing over millions of coordinates, incurring prohibitive computational costs. To address it, we propose NTK-Guided Implicit Neural Teaching (NINT), which accelerates training by dynamically selecting coordinates that maximize global functional updates. Leveraging the Neural Tangent Kernel (NTK), NINT scores examples by the norm of their NTK-augmented loss gradients, capturing both fitting errors and heterogeneous leverage (self-influence and cross-coordinate coupling). This dual consideration enables faster convergence compared to existing methods. Through extensive experiments, we demonstrate that NINT significantly reduces training time by nearly half while maintaining or improving representation quality, establishing state-of-the-art acceleration among recent sampling-based strategies.

