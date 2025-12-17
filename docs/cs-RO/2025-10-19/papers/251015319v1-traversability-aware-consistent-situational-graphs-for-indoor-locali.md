---
layout: default
title: Traversability-aware Consistent Situational Graphs for Indoor Localization and Mapping
---

# Traversability-aware Consistent Situational Graphs for Indoor Localization and Mapping

**arXiv**: [2510.15319v1](https://arxiv.org/abs/2510.15319) | [PDF](https://arxiv.org/pdf/2510.15319.pdf)

**作者**: Jeewon Kim, Minho Oh, Hyun Myung

---

## 💡 一句话要点

**提出可通行性感知房间分割方法，以提升室内定位与建图的语义一致性和计算效率。**

**关键词**: `室内定位` `场景图` `姿态图优化` `房间分割` `可通行性感知`

## 📋 核心要点

1. 核心问题：现有方法在房间分割中易过分割或欠分割，导致定位和建图不准确。
2. 方法要点：结合机器人可通行性信息，实现一致的分割，优化姿态图约束。
3. 实验或效果：在重复遍历数据集上，提高房间重检测频率并减少优化时间。

## 📄 摘要（原文）

> Scene graphs enhance 3D mapping capabilities in robotics by understanding the
> relationships between different spatial elements, such as rooms and objects.
> Recent research extends scene graphs to hierarchical layers, adding and
> leveraging constraints across these levels. This approach is tightly integrated
> with pose-graph optimization, improving both localization and mapping accuracy
> simultaneously. However, when segmenting spatial characteristics, consistently
> recognizing rooms becomes challenging due to variations in viewpoints and
> limited field of view (FOV) of sensors. For example, existing real-time
> approaches often over-segment large rooms into smaller, non-functional spaces
> that are not useful for localization and mapping due to the time-dependent
> method. Conversely, their voxel-based room segmentation method often
> under-segment in complex cases like not fully enclosed 3D space that are
> non-traversable for ground robots or humans, leading to false constraints in
> pose-graph optimization. We propose a traversability-aware room segmentation
> method that considers the interaction between robots and surroundings, with
> consistent feasibility of traversability information. This enhances both the
> semantic coherence and computational efficiency of pose-graph optimization.
> Improved performance is demonstrated through the re-detection frequency of the
> same rooms in a dataset involving repeated traversals of the same space along
> the same path, as well as the optimization time consumption.

