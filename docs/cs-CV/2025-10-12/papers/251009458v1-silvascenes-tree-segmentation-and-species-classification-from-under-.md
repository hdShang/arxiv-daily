---
layout: default
title: SilvaScenes: Tree Segmentation and Species Classification from Under-Canopy Images in Natural Forests
---

# SilvaScenes: Tree Segmentation and Species Classification from Under-Canopy Images in Natural Forests

**arXiv**: [2510.09458v1](https://arxiv.org/abs/2510.09458) | [PDF](https://arxiv.org/pdf/2510.09458.pdf)

**作者**: David-Alexandre Duclos, William Guimont-Martin, Gabriel Jeanson, Arthur Larochelle-Tremblay, Théo Defosse, Frédéric Moore, Philippe Nolet, François Pomerleau, Philippe Giguère

---

## 💡 一句话要点

**提出SilvaScenes数据集以解决自然林冠下树木分割与物种分类的感知挑战**

**关键词**: `实例分割` `树木物种分类` `森林机器人感知` `数据集构建` `深度学习基准测试`

## 📋 核心要点

1. 核心问题：自然森林中遮挡、光照变化和植被密集导致机器人感知困难，现有数据集不足
2. 方法要点：收集加拿大魁北克五生物气候域图像，标注24种1476棵树，用于实例分割
3. 实验或效果：树分割mAP达67.65%，物种分类mAP仅35.69%，显示分类挑战大

## 📄 摘要（原文）

> Interest in robotics for forest management is growing, but perception in
> complex, natural environments remains a significant hurdle. Conditions such as
> heavy occlusion, variable lighting, and dense vegetation pose challenges to
> automated systems, which are essential for precision forestry, biodiversity
> monitoring, and the automation of forestry equipment. These tasks rely on
> advanced perceptual capabilities, such as detection and fine-grained species
> classification of individual trees. Yet, existing datasets are inadequate to
> develop such perception systems, as they often focus on urban settings or a
> limited number of species. To address this, we present SilvaScenes, a new
> dataset for instance segmentation of tree species from under-canopy images.
> Collected across five bioclimatic domains in Quebec, Canada, SilvaScenes
> features 1476 trees from 24 species with annotations from forestry experts. We
> demonstrate the relevance and challenging nature of our dataset by benchmarking
> modern deep learning approaches for instance segmentation. Our results show
> that, while tree segmentation is easy, with a top mean average precision (mAP)
> of 67.65%, species classification remains a significant challenge with an mAP
> of only 35.69%. Our dataset and source code will be available at
> https://github.com/norlab-ulaval/SilvaScenes.

