---
layout: default
title: TED-4DGS: Temporally Activated and Embedding-based Deformation for 4DGS Compression
---

# TED-4DGS: Temporally Activated and Embedding-based Deformation for 4DGS Compression

**arXiv**: [2512.05446v1](https://arxiv.org/abs/2512.05446) | [PDF](https://arxiv.org/pdf/2512.05446.pdf)

**作者**: Cheng-Yuan Ho, He-Bi Yang, Jui-Chiu Chiang, Yu-Lun Liu, Wen-Hsiao Peng

---

## 💡 一句话要点

**提出TED-4DGS以优化动态3D高斯溅射表示的率失真压缩**

**关键词**: `动态3D高斯溅射` `率失真优化压缩` `时间激活变形` `嵌入查询` `稀疏锚点表示` `隐式神经表示`

## 📋 核心要点

1. 核心问题：动态3D高斯溅射表示缺乏紧凑变形方案与率失真优化压缩策略。
2. 方法要点：基于稀疏锚点表示，结合时间激活参数和嵌入查询共享变形库实现变形控制。
3. 实验或效果：在多个真实数据集上实现先进的率失真性能，支持压缩框架。

## 📄 摘要（原文）

> Building on the success of 3D Gaussian Splatting (3DGS) in static 3D scene representation, its extension to dynamic scenes, commonly referred to as 4DGS or dynamic 3DGS, has attracted increasing attention. However, designing more compact and efficient deformation schemes together with rate-distortion-optimized compression strategies for dynamic 3DGS representations remains an underexplored area. Prior methods either rely on space-time 4DGS with overspecified, short-lived Gaussian primitives or on canonical 3DGS with deformation that lacks explicit temporal control. To address this, we present TED-4DGS, a temporally activated and embedding-based deformation scheme for rate-distortion-optimized 4DGS compression that unifies the strengths of both families. TED-4DGS is built on a sparse anchor-based 3DGS representation. Each canonical anchor is assigned learnable temporal-activation parameters to specify its appearance and disappearance transitions over time, while a lightweight per-anchor temporal embedding queries a shared deformation bank to produce anchor-specific deformation. For rate-distortion compression, we incorporate an implicit neural representation (INR)-based hyperprior to model anchor attribute distributions, along with a channel-wise autoregressive model to capture intra-anchor correlations. With these novel elements, our scheme achieves state-of-the-art rate-distortion performance on several real-world datasets. To the best of our knowledge, this work represents one of the first attempts to pursue a rate-distortion-optimized compression framework for dynamic 3DGS representations.

