---
layout: default
title: NI-Tex: Non-isometric Image-based Garment Texture Generation
---

# NI-Tex: Non-isometric Image-based Garment Texture Generation

**arXiv**: [2511.18765v1](https://arxiv.org/abs/2511.18765) | [PDF](https://arxiv.org/pdf/2511.18765.pdf)

**作者**: Hui Shan, Ming Li, Haitao Yang, Kai Zheng, Sizhe Zheng, Yanwei Fu, Xiangru Huang

---

## 💡 一句话要点

**提出NI-Tex方法以解决非等距图像到3D服装纹理生成的挑战**

**关键词**: `非等距纹理生成` `3D服装设计` `PBR纹理` `图像编辑` `多视图融合`

## 📋 核心要点

1. 核心问题：现有方法需严格拓扑一致或精确变形，限制纹理生成质量与灵活性。
2. 方法要点：构建3D Garment Videos数据集，使用Nano Banana编辑，实现跨拓扑纹理生成。
3. 实验或效果：通过迭代烘焙生成无缝PBR纹理，适用于工业级3D服装设计。

## 📄 摘要（原文）

> Existing industrial 3D garment meshes already cover most real-world clothing geometries, yet their texture diversity remains limited. To acquire more realistic textures, generative methods are often used to extract Physically-based Rendering (PBR) textures and materials from large collections of wild images and project them back onto garment meshes. However, most image-conditioned texture generation approaches require strict topological consistency between the input image and the input 3D mesh, or rely on accurate mesh deformation to match to the image poses, which significantly constrains the texture generation quality and flexibility. To address the challenging problem of non-isometric image-based garment texture generation, we construct 3D Garment Videos, a physically simulated, garment-centric dataset that provides consistent geometry and material supervision across diverse deformations, enabling robust cross-pose texture learning. We further employ Nano Banana for high-quality non-isometric image editing, achieving reliable cross-topology texture generation between non-isometric image-geometry pairs. Finally, we propose an iterative baking method via uncertainty-guided view selection and reweighting that fuses multi-view predictions into seamless, production-ready PBR textures. Through extensive experiments, we demonstrate that our feedforward dual-branch architecture generates versatile and spatially aligned PBR materials suitable for industry-level 3D garment design.

