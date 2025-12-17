---
layout: default
title: NaTex: Seamless Texture Generation as Latent Color Diffusion
---

# NaTex: Seamless Texture Generation as Latent Color Diffusion

**arXiv**: [2511.16317v1](https://arxiv.org/abs/2511.16317) | [PDF](https://arxiv.org/pdf/2511.16317.pdf)

**作者**: Zeqiang Lai, Yunfei Zhao, Zibo Zhao, Xin Yang, Xin Huang, Jingwei Huang, Xiangyu Yue, Chunchao Guo

---

## 💡 一句话要点

**提出NaTex框架以解决3D纹理生成中的对齐与一致性问题**

**关键词**: `3D纹理生成` `潜在颜色扩散` `几何感知VAE` `多控制扩散变换器` `纹理对齐` `下游应用`

## 📋 核心要点

1. 核心问题：传统方法依赖2D多视图扩散，存在遮挡、对齐和颜色一致性问题
2. 方法要点：采用潜在颜色扩散，结合几何感知VAE和多控制DiT，直接预测3D空间颜色
3. 实验或效果：在纹理对齐和一致性上显著优于先前方法，并支持多种下游应用

## 📄 摘要（原文）

> We present NaTex, a native texture generation framework that predicts texture color directly in 3D space. In contrast to previous approaches that rely on baking 2D multi-view images synthesized by geometry-conditioned Multi-View Diffusion models (MVDs), NaTex avoids several inherent limitations of the MVD pipeline. These include difficulties in handling occluded regions that require inpainting, achieving precise mesh-texture alignment along boundaries, and maintaining cross-view consistency and coherence in both content and color intensity. NaTex features a novel paradigm that addresses the aforementioned issues by viewing texture as a dense color point cloud. Driven by this idea, we propose latent color diffusion, which comprises a geometry-awared color point cloud VAE and a multi-control diffusion transformer (DiT), entirely trained from scratch using 3D data, for texture reconstruction and generation. To enable precise alignment, we introduce native geometry control that conditions the DiT on direct 3D spatial information via positional embeddings and geometry latents. We co-design the VAE-DiT architecture, where the geometry latents are extracted via a dedicated geometry branch tightly coupled with the color VAE, providing fine-grained surface guidance that maintains strong correspondence with the texture. With these designs, NaTex demonstrates strong performance, significantly outperforming previous methods in texture coherence and alignment. Moreover, NaTex also exhibits strong generalization capabilities, either training-free or with simple tuning, for various downstream applications, e.g., material generation, texture refinement, and part segmentation and texturing.

