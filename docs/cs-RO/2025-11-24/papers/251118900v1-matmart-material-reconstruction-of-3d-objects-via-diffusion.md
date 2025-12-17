---
layout: default
title: MatMart: Material Reconstruction of 3D Objects via Diffusion
---

# MatMart: Material Reconstruction of 3D Objects via Diffusion

**arXiv**: [2511.18900v1](https://arxiv.org/abs/2511.18900) | [PDF](https://arxiv.org/pdf/2511.18900.pdf)

**作者**: Xiuchao Wu, Pengfei Zhu, Jiangjing Lyu, Xinguo Liu, Jie Guo, Yanwen Guo, Weiwei Xu, Chengfei Lyu

---

## 💡 一句话要点

**提出MatMart框架，通过扩散模型实现3D物体的材料重建。**

**关键词**: `材料重建` `扩散模型` `3D物体` `视图-材料交叉注意力` `渐进推理`

## 📋 核心要点

1. 核心问题：从输入图像中估计和生成3D物体的物理材料。
2. 方法要点：采用两阶段重建，结合视图-材料交叉注意力和渐进推理。
3. 实验或效果：在材料重建中优于现有方法，具有高保真度和灵活性。

## 📄 摘要（原文）

> Applying diffusion models to physically-based material estimation and generation has recently gained prominence. In this paper, we propose \ttt, a novel material reconstruction framework for 3D objects, offering the following advantages. First, \ttt\ adopts a two-stage reconstruction, starting with accurate material prediction from inputs and followed by prior-guided material generation for unobserved views, yielding high-fidelity results. Second, by utilizing progressive inference alongside the proposed view-material cross-attention (VMCA), \ttt\ enables reconstruction from an arbitrary number of input images, demonstrating strong scalability and flexibility. Finally, \ttt\ achieves both material prediction and generation capabilities through end-to-end optimization of a single diffusion model, without relying on additional pre-trained models, thereby exhibiting enhanced stability across various types of objects. Extensive experiments demonstrate that \ttt\ achieves superior performance in material reconstruction compared to existing methods.

