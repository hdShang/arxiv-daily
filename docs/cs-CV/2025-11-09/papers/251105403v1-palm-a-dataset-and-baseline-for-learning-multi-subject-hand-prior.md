---
layout: default
title: PALM: A Dataset and Baseline for Learning Multi-subject Hand Prior
---

# PALM: A Dataset and Baseline for Learning Multi-subject Hand Prior

**arXiv**: [2511.05403v1](https://arxiv.org/abs/2511.05403) | [PDF](https://arxiv.org/pdf/2511.05403.pdf)

**作者**: Zicong Fan, Edoardo Remelli, David Dimond, Fadime Sener, Liuhao Ge, Bugra Tekin, Cem Keskin, Shreyas Hampali

---

## 💡 一句话要点

**提出PALM数据集和PALM-Net基线，以解决多主体手部建模中数据不足和个性化挑战**

**关键词**: `手部建模` `多主体数据集` `逆渲染` `虚拟人个性化` `几何先验` `多视图图像`

## 📋 核心要点

1. 核心问题：缺乏高质量多主体手部数据集，限制手部几何、外观和关节建模进展
2. 方法要点：构建大规模PALM数据集，结合物理逆渲染学习多主体手部先验
3. 实验或效果：PALM-Net实现单图像手部虚拟人个性化，支持真实感和可重光照

## 📄 摘要（原文）

> The ability to grasp objects, signal with gestures, and share emotion through
> touch all stem from the unique capabilities of human hands. Yet creating
> high-quality personalized hand avatars from images remains challenging due to
> complex geometry, appearance, and articulation, particularly under
> unconstrained lighting and limited views. Progress has also been limited by the
> lack of datasets that jointly provide accurate 3D geometry, high-resolution
> multiview imagery, and a diverse population of subjects. To address this, we
> present PALM, a large-scale dataset comprising 13k high-quality hand scans from
> 263 subjects and 90k multi-view images, capturing rich variation in skin tone,
> age, and geometry. To show its utility, we present a baseline PALM-Net, a
> multi-subject prior over hand geometry and material properties learned via
> physically based inverse rendering, enabling realistic, relightable
> single-image hand avatar personalization. PALM's scale and diversity make it a
> valuable real-world resource for hand modeling and related research.

