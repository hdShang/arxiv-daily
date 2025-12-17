---
layout: default
title: Voronoi-Assisted Diffusion for Computing Unsigned Distance Fields from Unoriented Points
---

# Voronoi-Assisted Diffusion for Computing Unsigned Distance Fields from Unoriented Points

**arXiv**: [2510.12524v1](https://arxiv.org/abs/2510.12524) | [PDF](https://arxiv.org/pdf/2510.12524.pdf)

**作者**: Jiayi Kong, Chen Zong, Junkai Deng, Xuhui Chen, Fei Hou, Shiqing Xin, Junhui Hou, Chen Qian, Ying He

---

## 💡 一句话要点

**提出Voronoi辅助扩散方法以从无定向点云计算无符号距离场**

**关键词**: `无符号距离场` `点云处理` `Voronoi图` `扩散方法` `几何计算`

## 📋 核心要点

1. 核心问题：现有神经方法计算无符号距离场时存在数值不稳定、高计算成本和可控性差的问题
2. 方法要点：使用Voronoi几何准则对齐双向法向量，扩散后积分恢复无符号距离场
3. 实验或效果：方法高效稳定，能处理封闭、开放、非流形和非定向几何体

## 📄 摘要（原文）

> Unsigned Distance Fields (UDFs) provide a flexible representation for 3D
> shapes with arbitrary topology, including open and closed surfaces, orientable
> and non-orientable geometries, and non-manifold structures. While recent neural
> approaches have shown promise in learning UDFs, they often suffer from
> numerical instability, high computational cost, and limited controllability. We
> present a lightweight, network-free method, Voronoi-Assisted Diffusion (VAD),
> for computing UDFs directly from unoriented point clouds. Our approach begins
> by assigning bi-directional normals to input points, guided by two
> Voronoi-based geometric criteria encoded in an energy function for optimal
> alignment. The aligned normals are then diffused to form an approximate UDF
> gradient field, which is subsequently integrated to recover the final UDF.
> Experiments demonstrate that VAD robustly handles watertight and open surfaces,
> as well as complex non-manifold and non-orientable geometries, while remaining
> computationally efficient and stable.

