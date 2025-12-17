---
layout: default
title: IDEAL-M3D: Instance Diversity-Enriched Active Learning for Monocular 3D Detection
---

# IDEAL-M3D: Instance Diversity-Enriched Active Learning for Monocular 3D Detection

**arXiv**: [2511.19301v1](https://arxiv.org/abs/2511.19301) | [PDF](https://arxiv.org/pdf/2511.19301.pdf)

**作者**: Johannes Meier, Florian Günther, Riccardo Marin, Oussema Dhaouadi, Jacques Kaiser, Daniel Cremers

---

## 💡 一句话要点

**提出IDEAL-M3D以解决单目3D检测中主动学习的实例多样性和标注效率问题**

**关键词**: `单目3D检测` `主动学习` `实例多样性` `标注效率` `深度估计` `KITTI数据集`

## 📋 核心要点

1. 核心问题：现有主动学习方法选择整张图像，效率低，且偏向深度模糊的远距离物体
2. 方法要点：采用实例级管道，通过异构骨干网络和任务无关特征增强多样性
3. 实验或效果：在KITTI数据集上，仅用60%标注达到相似或更高AP3D，节省资源

## 📄 摘要（原文）

> Monocular 3D detection relies on just a single camera and is therefore easy to deploy. Yet, achieving reliable 3D understanding from monocular images requires substantial annotation, and 3D labels are especially costly. To maximize performance under constrained labeling budgets, it is essential to prioritize annotating samples expected to deliver the largest performance gains. This prioritization is the focus of active learning. Curiously, we observed two significant limitations in active learning algorithms for 3D monocular object detection. First, previous approaches select entire images, which is inefficient, as non-informative instances contained in the same image also need to be labeled. Secondly, existing methods rely on uncertainty-based selection, which in monocular 3D object detection creates a bias toward depth ambiguity. Consequently, distant objects are selected, while nearby objects are overlooked.
>   To address these limitations, we propose IDEAL-M3D, the first instance-level pipeline for monocular 3D detection. For the first time, we demonstrate that an explicitly diverse, fast-to-train ensemble improves diversity-driven active learning for monocular 3D. We induce diversity with heterogeneous backbones and task-agnostic features, loss weight perturbation, and time-dependent bagging. IDEAL-M3D shows superior performance and significant resource savings: with just 60% of the annotations, we achieve similar or better AP3D on KITTI validation and test set results compared to training the same detector on the whole dataset.

