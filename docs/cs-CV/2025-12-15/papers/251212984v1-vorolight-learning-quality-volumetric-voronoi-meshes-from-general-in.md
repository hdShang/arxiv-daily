---
layout: default
title: VoroLight: Learning Quality Volumetric Voronoi Meshes from General Inputs
---

# VoroLight: Learning Quality Volumetric Voronoi Meshes from General Inputs

**arXiv**: [2512.12984v1](https://arxiv.org/abs/2512.12984) | [PDF](https://arxiv.org/pdf/2512.12984.pdf)

**作者**: Jiayin Lu, Ying Jiang, Yin Yang, Chenfanfu Jiang

---

## 💡 一句话要点

**提出VoroLight框架，基于可微Voronoi网格化从多样输入重建高质量三维形状。**

**关键词**: `三维形状重建` `可微Voronoi网格化` `体网格优化` `多样输入处理` `拓扑一致性`

## 📋 核心要点

1. 核心问题：从图像、隐式场、点云和网格等多样输入生成平滑、水密且拓扑一致的体网格。
2. 方法要点：采用三阶段流程，包括可微Voronoi初始化、多边形面球训练优化表面质量和体优化。
3. 实验或效果：直接生成高质量表面和体网格，支持多种输入类型，提升重建精度和拓扑一致性。

## 📄 摘要（原文）

> We present VoroLight, a differentiable framework for 3D shape reconstruction based on Voronoi meshing. Our approach generates smooth, watertight surfaces and topologically consistent volumetric meshes directly from diverse inputs, including images, implicit shape level-set fields, point clouds and meshes. VoroLight operates in three stages: it first initializes a surface using a differentiable Voronoi formulation, then refines surface quality through a polygon-face sphere training stage, and finally reuses the differentiable Voronoi formulation for volumetric optimization with additional interior generator points. Project page: https://jiayinlu19960224.github.io/vorolight/

