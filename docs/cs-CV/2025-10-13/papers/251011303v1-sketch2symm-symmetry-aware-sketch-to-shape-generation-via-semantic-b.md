---
layout: default
title: sketch2symm: Symmetry-aware sketch-to-shape generation via semantic bridging
---

# sketch2symm: Symmetry-aware sketch-to-shape generation via semantic bridging

**arXiv**: [2510.11303v1](https://arxiv.org/abs/2510.11303) | [PDF](https://arxiv.org/pdf/2510.11303.pdf)

**作者**: Yan Zhou, Mingji Li, Xiantao Zeng, Jie Lin, Yuexia Zhou

---

## 💡 一句话要点

**提出Sketch2Symm方法，通过语义桥接和对称约束从草图生成几何一致的3D形状**

**关键词**: `草图到3D重建` `语义桥接` `对称约束` `几何一致性` `生成方法`

## 📋 核心要点

1. 核心问题：草图输入抽象稀疏，缺乏足够语义和几何信息，导致3D重建困难。
2. 方法要点：采用两阶段生成，先通过草图到图像翻译进行语义桥接，再引入对称约束作为几何先验。
3. 实验效果：在主流数据集上，Chamfer距离、Earth Mover距离和F-Score指标优于现有方法。

## 📄 摘要（原文）

> Sketch-based 3D reconstruction remains a challenging task due to the abstract
> and sparse nature of sketch inputs, which often lack sufficient semantic and
> geometric information. To address this, we propose Sketch2Symm, a two-stage
> generation method that produces geometrically consistent 3D shapes from
> sketches. Our approach introduces semantic bridging via sketch-to-image
> translation to enrich sparse sketch representations, and incorporates symmetry
> constraints as geometric priors to leverage the structural regularity commonly
> found in everyday objects. Experiments on mainstream sketch datasets
> demonstrate that our method achieves superior performance compared to existing
> sketch-based reconstruction methods in terms of Chamfer Distance, Earth Mover's
> Distance, and F-Score, verifying the effectiveness of the proposed semantic
> bridging and symmetry-aware design.

