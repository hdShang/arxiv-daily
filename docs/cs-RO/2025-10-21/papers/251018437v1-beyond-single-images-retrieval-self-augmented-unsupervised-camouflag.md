---
layout: default
title: Beyond Single Images: Retrieval Self-Augmented Unsupervised Camouflaged Object Detection
---

# Beyond Single Images: Retrieval Self-Augmented Unsupervised Camouflaged Object Detection

**arXiv**: [2510.18437v1](https://arxiv.org/abs/2510.18437) | [PDF](https://arxiv.org/pdf/2510.18437.pdf)

**作者**: Ji Du, Xin Wang, Fangwei Hao, Mingyang Yu, Chunyuan Chen, Jiesheng Wu, Bin Wang, Jing Xu, Ping Li

---

## 💡 一句话要点

**提出RISE检索自增强范式，利用数据集上下文生成伪标签以解决无监督伪装物体检测问题**

**关键词**: `伪装物体检测` `无监督学习` `检索增强` `伪标签生成` `多视图检索` `原型库构建`

## 📋 核心要点

1. 核心问题：伪装物体检测需从高度相似背景中分割物体，现有方法依赖图像级建模或标注，未充分利用数据集级信息
2. 方法要点：通过聚类-检索策略构建原型库，并采用多视图KNN检索生成鲁棒伪掩码，无需标注
3. 实验或效果：在无监督和提示方法中表现优异，代码已开源

## 📄 摘要（原文）

> At the core of Camouflaged Object Detection (COD) lies segmenting objects
> from their highly similar surroundings. Previous efforts navigate this
> challenge primarily through image-level modeling or annotation-based
> optimization. Despite advancing considerably, this commonplace practice hardly
> taps valuable dataset-level contextual information or relies on laborious
> annotations. In this paper, we propose RISE, a RetrIeval SElf-augmented
> paradigm that exploits the entire training dataset to generate pseudo-labels
> for single images, which could be used to train COD models. RISE begins by
> constructing prototype libraries for environments and camouflaged objects using
> training images (without ground truth), followed by K-Nearest Neighbor (KNN)
> retrieval to generate pseudo-masks for each image based on these libraries. It
> is important to recognize that using only training images without annotations
> exerts a pronounced challenge in crafting high-quality prototype libraries. In
> this light, we introduce a Clustering-then-Retrieval (CR) strategy, where
> coarse masks are first generated through clustering, facilitating subsequent
> histogram-based image filtering and cross-category retrieval to produce
> high-confidence prototypes. In the KNN retrieval stage, to alleviate the effect
> of artifacts in feature maps, we propose Multi-View KNN Retrieval (MVKR), which
> integrates retrieval results from diverse views to produce more robust and
> precise pseudo-masks. Extensive experiments demonstrate that RISE outperforms
> state-of-the-art unsupervised and prompt-based methods. Code is available at
> https://github.com/xiaohainku/RISE.

