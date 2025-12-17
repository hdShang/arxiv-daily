---
layout: default
title: DOS: Distilling Observable Softmaps of Zipfian Prototypes for Self-Supervised Point Representation
---

# DOS: Distilling Observable Softmaps of Zipfian Prototypes for Self-Supervised Point Representation

**arXiv**: [2512.11465v1](https://arxiv.org/abs/2512.11465) | [PDF](https://arxiv.org/pdf/2512.11465.pdf)

**作者**: Mohamed Abdelsamad, Michael Ulrich, Bin Yang, Miao Zhang, Yakov Miron, Abhinav Valada

---

## 💡 一句话要点

**提出DOS框架，通过可观测点软图蒸馏和Zipfian原型解决3D点云自监督学习中的语义不平衡和信息泄露问题。**

**关键词**: `3D点云表示` `自监督学习` `软图蒸馏` `Zipfian原型` `语义分割` `3D目标检测`

## 📋 核心要点

1. 核心问题：3D点云自监督学习面临几何不规则、重建易走捷径和语义分布不平衡的挑战。
2. 方法要点：仅蒸馏可观测点的语义相关性软图，引入Zipfian原型并使用Zipf-Sinkhorn算法强制原型使用的幂律先验。
3. 实验或效果：在多个基准测试中优于当前最先进方法，无需额外数据或标注，验证了可扩展性和有效性。

## 📄 摘要（原文）

> Recent advances in self-supervised learning (SSL) have shown tremendous potential for learning 3D point cloud representations without human annotations. However, SSL for 3D point clouds still faces critical challenges due to irregular geometry, shortcut-prone reconstruction, and unbalanced semantics distribution. In this work, we propose DOS (Distilling Observable Softmaps), a novel SSL framework that self-distills semantic relevance softmaps only at observable (unmasked) points. This strategy prevents information leakage from masked regions and provides richer supervision than discrete token-to-prototype assignments. To address the challenge of unbalanced semantics in an unsupervised setting, we introduce Zipfian prototypes and incorporate them using a modified Sinkhorn-Knopp algorithm, Zipf-Sinkhorn, which enforces a power-law prior over prototype usage and modulates the sharpness of the target softmap during training. DOS outperforms current state-of-the-art methods on semantic segmentation and 3D object detection across multiple benchmarks, including nuScenes, Waymo, SemanticKITTI, ScanNet, and ScanNet200, without relying on extra data or annotations. Our results demonstrate that observable-point softmaps distillation offers a scalable and effective paradigm for learning robust 3D representations.

