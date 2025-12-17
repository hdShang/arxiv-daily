---
layout: default
title: VoMP: Predicting Volumetric Mechanical Property Fields
---

# VoMP: Predicting Volumetric Mechanical Property Fields

**arXiv**: [2510.22975v1](https://arxiv.org/abs/2510.22975) | [PDF](https://arxiv.org/pdf/2510.22975.pdf)

**作者**: Rishit Dagli, Donglai Xiang, Vismay Modi, Charles Loop, Clement Fuji Tsang, Anka He Chen, Anita Hu, Gavriel State, David I. W. Levin, Maria Shugrina

---

## 💡 一句话要点

**提出VoMP方法以预测3D物体的体积力学属性，替代手工设计。**

**关键词**: `体积力学属性预测` `3D物体表示` `几何Transformer` `材料潜码学习` `多视图特征聚合`

## 📋 核心要点

1. 物理模拟依赖空间变化的力学属性，传统方法需手工设计，效率低。
2. VoMP使用前馈网络聚合多视图特征，通过几何Transformer预测体素材料潜码。
3. 实验显示VoMP在准确性和速度上远超现有方法，基于真实数据集保证材料有效性。

## 📄 摘要（原文）

> Physical simulation relies on spatially-varying mechanical properties, often
> laboriously hand-crafted. VoMP is a feed-forward method trained to predict
> Young's modulus ($E$), Poisson's ratio ($\nu$), and density ($\rho$) throughout
> the volume of 3D objects, in any representation that can be rendered and
> voxelized. VoMP aggregates per-voxel multi-view features and passes them to our
> trained Geometry Transformer to predict per-voxel material latent codes. These
> latents reside on a manifold of physically plausible materials, which we learn
> from a real-world dataset, guaranteeing the validity of decoded per-voxel
> materials. To obtain object-level training data, we propose an annotation
> pipeline combining knowledge from segmented 3D datasets, material databases,
> and a vision-language model, along with a new benchmark. Experiments show that
> VoMP estimates accurate volumetric properties, far outperforming prior art in
> accuracy and speed.

