---
layout: default
title: CymbaDiff: Structured Spatial Diffusion for Sketch-based 3D Semantic Urban Scene Generation
---

# CymbaDiff: Structured Spatial Diffusion for Sketch-based 3D Semantic Urban Scene Generation

**arXiv**: [2510.13245v1](https://arxiv.org/abs/2510.13245) | [PDF](https://arxiv.org/pdf/2510.13245.pdf)

**作者**: Li Liang, Bo Miao, Xinyu Wang, Naveed Akhtar, Jordan Vice, Ajmal Mian

---

## 💡 一句话要点

**提出CymbaDiff以增强户外3D语义场景生成的空间一致性**

**关键词**: `3D场景生成` `语义分割` `扩散模型` `空间一致性` `户外场景` `草图生成`

## 📋 核心要点

1. 核心问题：户外3D语义场景生成缺乏公开、标注良好的数据集。
2. 方法要点：CymbaDiff引入结构化空间排序，捕捉圆柱连续性和垂直层次。
3. 实验或效果：在SketchSem3D基准上实现优越语义一致性和空间真实性。

## 📄 摘要（原文）

> Outdoor 3D semantic scene generation produces realistic and semantically rich
> environments for applications such as urban simulation and autonomous driving.
> However, advances in this direction are constrained by the absence of publicly
> available, well-annotated datasets. We introduce SketchSem3D, the first
> large-scale benchmark for generating 3D outdoor semantic scenes from abstract
> freehand sketches and pseudo-labeled annotations of satellite images.
> SketchSem3D includes two subsets, Sketch-based SemanticKITTI and Sketch-based
> KITTI-360 (containing LiDAR voxels along with their corresponding sketches and
> annotated satellite images), to enable standardized, rigorous, and diverse
> evaluations. We also propose Cylinder Mamba Diffusion (CymbaDiff) that
> significantly enhances spatial coherence in outdoor 3D scene generation.
> CymbaDiff imposes structured spatial ordering, explicitly captures cylindrical
> continuity and vertical hierarchy, and preserves both physical neighborhood
> relationships and global context within the generated scenes. Extensive
> experiments on SketchSem3D demonstrate that CymbaDiff achieves superior
> semantic consistency, spatial realism, and cross-dataset generalization. The
> code and dataset will be available at
> https://github.com/Lillian-research-hub/CymbaDiff

