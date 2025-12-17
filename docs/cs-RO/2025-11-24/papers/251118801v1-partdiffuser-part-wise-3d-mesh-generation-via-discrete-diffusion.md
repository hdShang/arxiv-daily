---
layout: default
title: PartDiffuser: Part-wise 3D Mesh Generation via Discrete Diffusion
---

# PartDiffuser: Part-wise 3D Mesh Generation via Discrete Diffusion

**arXiv**: [2511.18801v1](https://arxiv.org/abs/2511.18801) | [PDF](https://arxiv.org/pdf/2511.18801.pdf)

**作者**: Yichen Yang, Hong Li, Haodong Zhu, Linin Yang, Guojun Lei, Sheng Xu, Baochang Zhang

---

## 💡 一句话要点

**提出PartDiffuser以解决3D网格生成中全局结构与局部细节的平衡问题**

**关键词**: `3D网格生成` `离散扩散` `半自回归框架` `语义分割` `点云条件生成`

## 📋 核心要点

1. 现有自回归方法难以平衡全局结构一致性与高保真局部细节，易产生误差累积
2. 采用半自回归扩散框架，部分间自回归确保拓扑，部分内并行扩散重建细节
3. 实验显示在生成细节丰富的3D网格方面显著优于SOTA模型，适合实际应用

## 📄 摘要（原文）

> Existing autoregressive (AR) methods for generating artist-designed meshes struggle to balance global structural consistency with high-fidelity local details, and are susceptible to error accumulation. To address this, we propose PartDiffuser, a novel semi-autoregressive diffusion framework for point-cloud-to-mesh generation. The method first performs semantic segmentation on the mesh and then operates in a "part-wise" manner: it employs autoregression between parts to ensure global topology, while utilizing a parallel discrete diffusion process within each semantic part to precisely reconstruct high-frequency geometric features. PartDiffuser is based on the DiT architecture and introduces a part-aware cross-attention mechanism, using point clouds as hierarchical geometric conditioning to dynamically control the generation process, thereby effectively decoupling the global and local generation tasks. Experiments demonstrate that this method significantly outperforms state-of-the-art (SOTA) models in generating 3D meshes with rich detail, exhibiting exceptional detail representation suitable for real-world applications.

