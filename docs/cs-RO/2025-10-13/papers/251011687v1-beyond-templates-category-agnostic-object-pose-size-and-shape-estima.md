---
layout: default
title: Beyond 'Templates': Category-Agnostic Object Pose, Size, and Shape Estimation from a Single View
---

# Beyond 'Templates': Category-Agnostic Object Pose, Size, and Shape Estimation from a Single View

**arXiv**: [2510.11687v1](https://arxiv.org/abs/2510.11687) | [PDF](https://arxiv.org/pdf/2510.11687.pdf)

**作者**: Jinyu Zhang, Haitao Lin, Jiashu Hou, Xiangyang Xue, Yanwei Fu

---

## 💡 一句话要点

**提出类别无关框架，从单视图同时估计物体6D位姿、尺寸和形状，无需模板或CAD模型。**

**关键词**: `6D位姿估计` `类别无关学习` `形状重建` `Transformer模型` `零样本泛化` `实时推理`

## 📋 核心要点

1. 核心问题：从视觉输入估计物体6D位姿、尺寸和形状，现有方法依赖先验或泛化差。
2. 方法要点：融合2D特征与3D点云，使用Transformer和专家混合，并行解码实现实时推理。
3. 实验或效果：在合成数据训练，多基准测试中实现SOTA，零样本泛化强于未知物体。

## 📄 摘要（原文）

> Estimating an object's 6D pose, size, and shape from visual input is a
> fundamental problem in computer vision, with critical applications in robotic
> grasping and manipulation. Existing methods either rely on object-specific
> priors such as CAD models or templates, or suffer from limited generalization
> across categories due to pose-shape entanglement and multi-stage pipelines. In
> this work, we propose a unified, category-agnostic framework that
> simultaneously predicts 6D pose, size, and dense shape from a single RGB-D
> image, without requiring templates, CAD models, or category labels at test
> time. Our model fuses dense 2D features from vision foundation models with
> partial 3D point clouds using a Transformer encoder enhanced by a
> Mixture-of-Experts, and employs parallel decoders for pose-size estimation and
> shape reconstruction, achieving real-time inference at 28 FPS. Trained solely
> on synthetic data from 149 categories in the SOPE dataset, our framework is
> evaluated on four diverse benchmarks SOPE, ROPE, ObjaversePose, and HANDAL,
> spanning over 300 categories. It achieves state-of-the-art accuracy on seen
> categories while demonstrating remarkably strong zero-shot generalization to
> unseen real-world objects, establishing a new standard for open-set 6D
> understanding in robotics and embodied AI.

