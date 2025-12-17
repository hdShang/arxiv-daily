---
layout: default
title: Object-Centric 3D Gaussian Splatting for Strawberry Plant Reconstruction and Phenotyping
---

# Object-Centric 3D Gaussian Splatting for Strawberry Plant Reconstruction and Phenotyping

**arXiv**: [2511.02207v1](https://arxiv.org/abs/2511.02207) | [PDF](https://arxiv.org/pdf/2511.02207.pdf)

**作者**: Jiajia Li, Keyi Zhu, Qianwen Zhang, Dong Chen, Qi Sun, Zhaojian Li

---

## 💡 一句话要点

**提出对象中心3D高斯泼溅框架，用于草莓植株重建与表型分析**

**关键词**: `3D高斯泼溅` `植物表型分析` `对象中心重建` `SAM-2分割` `DBSCAN聚类` `PCA分析`

## 📋 核心要点

1. 传统植物表型方法耗时费力且具破坏性，3DGS重建常含背景噪声
2. 结合SAM-2分割与alpha通道掩码，实现无背景高精度植株重建
3. 实验显示方法在准确性和效率上优于传统，支持自动性状估计

## 📄 摘要（原文）

> Strawberries are among the most economically significant fruits in the United
> States, generating over $2 billion in annual farm-gate sales and accounting for
> approximately 13% of the total fruit production value. Plant phenotyping plays
> a vital role in selecting superior cultivars by characterizing plant traits
> such as morphology, canopy structure, and growth dynamics. However, traditional
> plant phenotyping methods are time-consuming, labor-intensive, and often
> destructive. Recently, neural rendering techniques, notably Neural Radiance
> Fields (NeRF) and 3D Gaussian Splatting (3DGS), have emerged as powerful
> frameworks for high-fidelity 3D reconstruction. By capturing a sequence of
> multi-view images or videos around a target plant, these methods enable
> non-destructive reconstruction of complex plant architectures. Despite their
> promise, most current applications of 3DGS in agricultural domains reconstruct
> the entire scene, including background elements, which introduces noise,
> increases computational costs, and complicates downstream trait analysis. To
> address this limitation, we propose a novel object-centric 3D reconstruction
> framework incorporating a preprocessing pipeline that leverages the Segment
> Anything Model v2 (SAM-2) and alpha channel background masking to achieve clean
> strawberry plant reconstructions. This approach produces more accurate
> geometric representations while substantially reducing computational time. With
> a background-free reconstruction, our algorithm can automatically estimate
> important plant traits, such as plant height and canopy width, using DBSCAN
> clustering and Principal Component Analysis (PCA). Experimental results show
> that our method outperforms conventional pipelines in both accuracy and
> efficiency, offering a scalable and non-destructive solution for strawberry
> plant phenotyping.

