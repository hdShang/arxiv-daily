---
layout: default
title: Generalizing Shape-from-Template to Topological Changes
---

# Generalizing Shape-from-Template to Topological Changes

**arXiv**: [2511.03459v1](https://arxiv.org/abs/2511.03459) | [PDF](https://arxiv.org/pdf/2511.03459.pdf)

**作者**: Kevin Manogue, Tomasz M Schang, Dilara Kuş, Jonas Müller, Stefan Zachow, Agniva Sengupta

---

## 💡 一句话要点

**提出拓扑变化感知的SfT方法，以处理变形中的拓扑变化问题。**

**关键词**: `形状从模板` `拓扑变化` `表面重建` `能量最小化` `图像对应`

## 📋 核心要点

1. 核心问题：传统SfT方法在物体变形伴随拓扑变化时失效。
2. 方法要点：基于经典SfT初始化，迭代分区模板以最小化能量函数。
3. 实验效果：在合成和真实数据上优于基线，捕捉撕裂和切割事件。

## 📄 摘要（原文）

> Reconstructing the surfaces of deformable objects from correspondences
> between a 3D template and a 2D image is well studied under Shape-from-Template
> (SfT) methods; however, existing approaches break down when topological changes
> accompany the deformation. We propose a principled extension of SfT that
> enables reconstruction in the presence of such changes. Our approach is
> initialized with a classical SfT solution and iteratively adapts the template
> by partitioning its spatial domain so as to minimize an energy functional that
> jointly encodes physical plausibility and reprojection consistency. We
> demonstrate that the method robustly captures a wide range of practically
> relevant topological events including tears and cuts on bounded 2D surfaces,
> thereby establishing the first general framework for topological-change-aware
> SfT. Experiments on both synthetic and real data confirm that our approach
> consistently outperforms baseline methods.

