---
layout: default
title: Densemarks: Learning Canonical Embeddings for Human Heads Images via Point Tracks
---

# Densemarks: Learning Canonical Embeddings for Human Heads Images via Point Tracks

**arXiv**: [2511.02830v1](https://arxiv.org/abs/2511.02830) | [PDF](https://arxiv.org/pdf/2511.02830.pdf)

**作者**: Dmitrii Pozdeev, Alexey Artemov, Ananta R. Bhattarai, Artem Sevastopolsky

---

## 💡 一句话要点

**提出DenseMarks学习头部图像的规范嵌入，实现高质量密集对应**

**关键词**: `密集对应学习` `头部图像分析` `规范嵌入` `对比损失` `多任务学习` `3D嵌入预测`

## 📋 核心要点

1. 核心问题：如何从2D头部图像中学习密集对应，以处理姿态变化和覆盖整个头部。
2. 方法要点：使用Vision Transformer预测像素级3D嵌入，通过对比损失和多任务学习训练。
3. 实验或效果：在几何感知点匹配和单目头部跟踪中达到先进水平，代码将公开。

## 📄 摘要（原文）

> We propose DenseMarks - a new learned representation for human heads,
> enabling high-quality dense correspondences of human head images. For a 2D
> image of a human head, a Vision Transformer network predicts a 3D embedding for
> each pixel, which corresponds to a location in a 3D canonical unit cube. In
> order to train our network, we collect a dataset of pairwise point matches,
> estimated by a state-of-the-art point tracker over a collection of diverse
> in-the-wild talking heads videos, and guide the mapping via a contrastive loss,
> encouraging matched points to have close embeddings. We further employ
> multi-task learning with face landmarks and segmentation constraints, as well
> as imposing spatial continuity of embeddings through latent cube features,
> which results in an interpretable and queryable canonical space. The
> representation can be used for finding common semantic parts, face/head
> tracking, and stereo reconstruction. Due to the strong supervision, our method
> is robust to pose variations and covers the entire head, including hair.
> Additionally, the canonical space bottleneck makes sure the obtained
> representations are consistent across diverse poses and individuals. We
> demonstrate state-of-the-art results in geometry-aware point matching and
> monocular head tracking with 3D Morphable Models. The code and the model
> checkpoint will be made available to the public.

