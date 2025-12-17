---
layout: default
title: Particulate: Feed-Forward 3D Object Articulation
---

# Particulate: Feed-Forward 3D Object Articulation

**arXiv**: [2512.11798v1](https://arxiv.org/abs/2512.11798) | [PDF](https://arxiv.org/pdf/2512.11798.pdf)

**作者**: Ruining Li, Yuxin Yao, Chuanxia Zheng, Christian Rupprecht, Joan Lasenby, Shangzhe Wu, Andrea Vedaldi

---

## 💡 一句话要点

**提出Particulate前馈方法，从单静态3D网格直接推断日常物体的完整铰接结构。**

**关键词**: `3D铰接估计` `前馈网络` `Transformer架构` `点云处理` `运动学推断` `单图像到3D`

## 📋 核心要点

1. 核心问题：从单静态3D网格自动推断物体的铰接结构，包括部件、运动学和约束。
2. 方法要点：使用Part Articulation Transformer处理点云，前馈预测多关节属性，无需逐对象优化。
3. 实验或效果：在公共数据集上训练，推理速度快，优于现有方法，支持AI生成资产。

## 📄 摘要（原文）

> We present Particulate, a feed-forward approach that, given a single static 3D mesh of an everyday object, directly infers all attributes of the underlying articulated structure, including its 3D parts, kinematic structure, and motion constraints. At its core is a transformer network, Part Articulation Transformer, which processes a point cloud of the input mesh using a flexible and scalable architecture to predict all the aforementioned attributes with native multi-joint support. We train the network end-to-end on a diverse collection of articulated 3D assets from public datasets. During inference, Particulate lifts the network's feed-forward prediction to the input mesh, yielding a fully articulated 3D model in seconds, much faster than prior approaches that require per-object optimization. Particulate can also accurately infer the articulated structure of AI-generated 3D assets, enabling full-fledged extraction of articulated 3D objects from a single (real or synthetic) image when combined with an off-the-shelf image-to-3D generator. We further introduce a new challenging benchmark for 3D articulation estimation curated from high-quality public 3D assets, and redesign the evaluation protocol to be more consistent with human preferences. Quantitative and qualitative results show that Particulate significantly outperforms state-of-the-art approaches.

