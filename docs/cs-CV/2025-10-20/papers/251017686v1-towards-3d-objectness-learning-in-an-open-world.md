---
layout: default
title: Towards 3D Objectness Learning in an Open World
---

# Towards 3D Objectness Learning in an Open World

**arXiv**: [2510.17686v1](https://arxiv.org/abs/2510.17686) | [PDF](https://arxiv.org/pdf/2510.17686.pdf)

**作者**: Taichi Liu, Zhenyu Wang, Ruofeng Liu, Guang Wang, Desheng Zhang

---

## 💡 一句话要点

**提出OP3Det以解决开放世界3D物体检测问题**

**关键词**: `3D物体检测` `开放世界学习` `跨模态融合` `零样本检测` `类别无关检测`

## 📋 核心要点

1. 核心问题：传统3D检测器在开放世界中泛化不足，难以检测未见物体。
2. 方法要点：融合2D语义先验和3D几何先验，实现类别无关的物体提议。
3. 实验或效果：在AR指标上超越现有方法达16.0%，泛化性能显著提升。

## 📄 摘要（原文）

> Recent advancements in 3D object detection and novel category detection have
> made significant progress, yet research on learning generalized 3D objectness
> remains insufficient. In this paper, we delve into learning open-world 3D
> objectness, which focuses on detecting all objects in a 3D scene, including
> novel objects unseen during training. Traditional closed-set 3D detectors
> struggle to generalize to open-world scenarios, while directly incorporating 3D
> open-vocabulary models for open-world ability struggles with vocabulary
> expansion and semantic overlap. To achieve generalized 3D object discovery, We
> propose OP3Det, a class-agnostic Open-World Prompt-free 3D Detector to detect
> any objects within 3D scenes without relying on hand-crafted text prompts. We
> introduce the strong generalization and zero-shot capabilities of 2D foundation
> models, utilizing both 2D semantic priors and 3D geometric priors for
> class-agnostic proposals to broaden 3D object discovery. Then, by integrating
> complementary information from point cloud and RGB image in the cross-modal
> mixture of experts, OP3Det dynamically routes uni-modal and multi-modal
> features to learn generalized 3D objectness. Extensive experiments demonstrate
> the extraordinary performance of OP3Det, which significantly surpasses existing
> open-world 3D detectors by up to 16.0% in AR and achieves a 13.5% improvement
> compared to closed-world 3D detectors.

