---
layout: default
title: Circle of Willis Centerline Graphs: A Dataset and Baseline Algorithm
---

# Circle of Willis Centerline Graphs: A Dataset and Baseline Algorithm

**arXiv**: [2510.13720v1](https://arxiv.org/abs/2510.13720) | [PDF](https://arxiv.org/pdf/2510.13720.pdf)

**作者**: Fabio Musio, Norman Juchler, Kaiyuan Yang, Suprosanna Shit, Chinmay Prabhakar, Bjoern Menze, Sven Hirsch

---

## 💡 一句话要点

**提出基于U-Net和A*算法的基线方法，用于从脑动脉图像中提取中心线图，以解决复杂几何下的可靠中心线提取问题。**

**关键词**: `中心线提取` `骨架化算法` `脑动脉图像` `图连接` `特征鲁棒性`

## 📋 核心要点

1. 核心问题：传统骨架化方法难以从复杂几何的Willis环中提取可靠中心线，且公开数据集稀缺。
2. 方法要点：使用细化骨架化算法从TopCoW数据集提取中心线图，结合U-Net骨架化和A*图连接。
3. 实验或效果：在测试集上，图拓扑重建F1=1，节点距离误差低于一像素，特征误差低于5%。

## 📄 摘要（原文）

> The Circle of Willis (CoW) is a critical network of arteries in the brain,
> often implicated in cerebrovascular pathologies. Voxel-level segmentation is an
> important first step toward an automated CoW assessment, but a full
> quantitative analysis requires centerline representations. However,
> conventional skeletonization techniques often struggle to extract reliable
> centerlines due to the CoW's complex geometry, and publicly available
> centerline datasets remain scarce. To address these challenges, we used a
> thinning-based skeletonization algorithm to extract and curate centerline
> graphs and morphometric features from the TopCoW dataset, which includes 200
> stroke patients, each imaged with MRA and CTA. The curated graphs were used to
> develop a baseline algorithm for centerline and feature extraction, combining
> U-Net-based skeletonization with A* graph connection. Performance was evaluated
> on a held-out test set, focusing on anatomical accuracy and feature robustness.
> Further, we used the extracted features to predict the frequency of fetal PCA
> variants, confirm theoretical bifurcation optimality relations, and detect
> subtle modality differences. The baseline algorithm consistently reconstructed
> graph topology with high accuracy (F1 = 1), and the average Euclidean node
> distance between reference and predicted graphs was below one voxel. Features
> such as segment radius, length, and bifurcation ratios showed strong
> robustness, with median relative errors below 5% and Pearson correlations above
> 0.95. Our results demonstrate the utility of learning-based skeletonization
> combined with graph connection for anatomically plausible centerline
> extraction. We emphasize the importance of going beyond simple voxel-based
> measures by evaluating anatomical accuracy and feature robustness. The dataset
> and baseline algorithm have been released to support further method development
> and clinical research.

