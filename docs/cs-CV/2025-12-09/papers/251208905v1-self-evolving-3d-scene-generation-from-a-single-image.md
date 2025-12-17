---
layout: default
title: Self-Evolving 3D Scene Generation from a Single Image
---

# Self-Evolving 3D Scene Generation from a Single Image

**arXiv**: [2512.08905v1](https://arxiv.org/abs/2512.08905) | [PDF](https://arxiv.org/pdf/2512.08905.pdf)

**作者**: Kaizhi Zheng, Yue Fan, Jing Gu, Zishuo Xu, Xuehai He, Xin Eric Wang

---

## 💡 一句话要点

**提出EvoScene框架，通过自演化方法从单图像生成高质量3D场景**

**关键词**: `单图像3D生成` `自演化框架` `几何推理` `视觉知识` `迭代优化` `3D场景重建`

## 📋 核心要点

1. 核心问题：单图像生成3D场景存在几何不稳定和纹理不一致的挑战
2. 方法要点：结合3D生成模型的几何推理和视频生成模型的视觉知识，迭代优化
3. 实验或效果：在多样场景中实现几何稳定、视图一致纹理和未见过区域补全

## 📄 摘要（原文）

> Generating high-quality, textured 3D scenes from a single image remains a fundamental challenge in vision and graphics. Recent image-to-3D generators recover reasonable geometry from single views, but their object-centric training limits generalization to complex, large-scale scenes with faithful structure and texture. We present EvoScene, a self-evolving, training-free framework that progressively reconstructs complete 3D scenes from single images. The key idea is combining the complementary strengths of existing models: geometric reasoning from 3D generation models and visual knowledge from video generation models. Through three iterative stages--Spatial Prior Initialization, Visual-guided 3D Scene Mesh Generation, and Spatial-guided Novel View Generation--EvoScene alternates between 2D and 3D domains, gradually improving both structure and appearance. Experiments on diverse scenes demonstrate that EvoScene achieves superior geometric stability, view-consistent textures, and unseen-region completion compared to strong baselines, producing ready-to-use 3D meshes for practical applications.

