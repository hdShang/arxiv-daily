---
layout: default
title: Anatomica: Localized Control over Geometric and Topological Properties for Anatomical Diffusion Models
---

# Anatomica: Localized Control over Geometric and Topological Properties for Anatomical Diffusion Models

**arXiv**: [2511.20587v1](https://arxiv.org/abs/2511.20587) | [PDF](https://arxiv.org/pdf/2511.20587.pdf)

**作者**: Karim Kadry, Abdallah Abdelwahed, Shoaib Goraya, Ajay Manicka, Naravich Chutisilp, Farhad Nezami, Elazer Edelman

---

## 💡 一句话要点

**提出Anatomica框架，在推理时控制解剖体素图的几何与拓扑属性**

**关键词**: `解剖体素图生成` `几何拓扑控制` `潜在扩散模型` `持久同调` `可微优化`

## 📋 核心要点

1. 核心问题：如何在生成多类解剖体素图时实现局部几何和拓扑控制
2. 方法要点：使用控制域提取子结构，通过可微惩罚函数和持久同调施加约束
3. 实验或效果：应用于潜在扩散模型，灵活控制解剖属性，支持合成数据集设计

## 📄 摘要（原文）

> We present Anatomica: an inference-time framework for generating multi-class anatomical voxel maps with localized geo-topological control. During generation, we use cuboidal control domains of varying dimensionality, location, and shape to slice out relevant substructures. These local substructures are used to compute differentiable penalty functions that steer the sample towards target constraints. We control geometric features such as size, shape, and position through voxel-wise moments, while topological features such as connected components, loops, and voids are enforced through persistent homology. Lastly, we implement Anatomica for latent diffusion models, where neural field decoders partially extract substructures, enabling the efficient control of anatomical properties. Anatomica applies flexibly across diverse anatomical systems, composing constraints to control complex structures over arbitrary dimensions and coordinate systems, thereby enabling the rational design of synthetic datasets for virtual trials or machine learning workflows.

