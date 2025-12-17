---
layout: default
title: Textured Geometry Evaluation: Perceptual 3D Textured Shape Metric via 3D Latent-Geometry Network
---

# Textured Geometry Evaluation: Perceptual 3D Textured Shape Metric via 3D Latent-Geometry Network

**arXiv**: [2512.01380v1](https://arxiv.org/abs/2512.01380) | [PDF](https://arxiv.org/pdf/2512.01380.pdf)

**作者**: Tianyu Luan, Xuelu Feng, Zixin Zhu, Phani Nuney, Sheng Liu, Xuan Gong, David Doermann, Chunming Qiao, Junsong Yuan

---

## 💡 一句话要点

**提出TGE方法以直接评估带纹理3D网格的保真度，避免渲染依赖**

**关键词**: `3D形状评估` `纹理网格` `感知度量` `真实世界失真` `几何与颜色联合`

## 📋 核心要点

1. 核心问题：现有3D形状评估指标如Chamfer Distance与人类感知不一致，基于渲染的方法存在结构覆盖不全和视角敏感问题
2. 方法要点：TGE直接基于3D网格和颜色信息联合计算保真度，无需渲染，使用真实世界失真数据集训练
3. 实验或效果：在真实世界失真数据集上，TGE优于基于渲染和仅几何的方法

## 📄 摘要（原文）

> Textured high-fidelity 3D models are crucial for games, AR/VR, and film, but human-aligned evaluation methods still fall behind despite recent advances in 3D reconstruction and generation. Existing metrics, such as Chamfer Distance, often fail to align with how humans evaluate the fidelity of 3D shapes. Recent learning-based metrics attempt to improve this by relying on rendered images and 2D image quality metrics. However, these approaches face limitations due to incomplete structural coverage and sensitivity to viewpoint choices. Moreover, most methods are trained on synthetic distortions, which differ significantly from real-world distortions, resulting in a domain gap. To address these challenges, we propose a new fidelity evaluation method that is based directly on 3D meshes with texture, without relying on rendering. Our method, named Textured Geometry Evaluation TGE, jointly uses the geometry and color information to calculate the fidelity of the input textured mesh with comparison to a reference colored shape. To train and evaluate our metric, we design a human-annotated dataset with real-world distortions. Experiments show that TGE outperforms rendering-based and geometry-only methods on real-world distortion dataset.

