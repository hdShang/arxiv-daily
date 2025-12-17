---
layout: default
title: Fusion of Heterogeneous Pathology Foundation Models for Whole Slide Image Analysis
---

# Fusion of Heterogeneous Pathology Foundation Models for Whole Slide Image Analysis

**arXiv**: [2510.27237v1](https://arxiv.org/abs/2510.27237) | [PDF](https://arxiv.org/pdf/2510.27237.pdf)

**作者**: Zhidong Yang, Xiuhui Shi, Wei Ba, Zhigang Song, Haijing Luan, Taiyuan Hu, Senlin Lin, Jiguang Wang, Shaohua Kevin Zhou, Rui Yan

---

## 💡 一句话要点

**提出FuseCPath框架以融合异构病理基础模型，提升全切片图像分析性能**

**关键词**: `全切片图像分析` `病理基础模型融合` `多视图聚类` `补丁级特征` `切片级特征` `癌症数据集`

## 📋 核心要点

1. 核心问题：病理基础模型因训练数据和架构差异导致特征异质性，影响下游任务性能。
2. 方法要点：采用多视图聚类筛选判别性补丁，并设计补丁级和切片级融合策略。
3. 实验或效果：在TCGA多癌症数据集上验证，FuseCPath达到最先进性能。

## 📄 摘要（原文）

> Whole slide image (WSI) analysis has emerged as an increasingly essential
> technique in computational pathology. Recent advances in the pathological
> foundation models (FMs) have demonstrated significant advantages in deriving
> meaningful patch-level or slide-level feature representations from WSIs.
> However, current pathological FMs have exhibited substantial heterogeneity
> caused by diverse private training datasets and different network
> architectures. This heterogeneity introduces performance variability when we
> utilize the extracted features from different FMs in the downstream tasks. To
> fully explore the advantage of multiple FMs effectively, in this work, we
> propose a novel framework for the fusion of heterogeneous pathological FMs,
> called FuseCPath, yielding a model with a superior ensemble performance. The
> main contributions of our framework can be summarized as follows: (i) To
> guarantee the representativeness of the training patches, we propose a
> multi-view clustering-based method to filter out the discriminative patches via
> multiple FMs' embeddings. (ii) To effectively fuse the heterogeneous
> patch-level FMs, we devise a cluster-level re-embedding strategy to online
> capture patch-level local features. (iii) To effectively fuse the heterogeneous
> slide-level FMs, we devise a collaborative distillation strategy to explore the
> connections between slide-level FMs. Extensive experiments conducted on lung
> cancer, bladder cancer, and colorectal cancer datasets from The Cancer Genome
> Atlas (TCGA) have demonstrated that the proposed FuseCPath achieves
> state-of-the-art performance across multiple tasks on these public datasets.

