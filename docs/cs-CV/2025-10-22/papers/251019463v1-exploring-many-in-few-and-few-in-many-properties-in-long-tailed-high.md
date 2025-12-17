---
layout: default
title: Exploring "Many in Few" and "Few in Many" Properties in Long-Tailed, Highly-Imbalanced IC Defect Classification
---

# Exploring "Many in Few" and "Few in Many" Properties in Long-Tailed, Highly-Imbalanced IC Defect Classification

**arXiv**: [2510.19463v1](https://arxiv.org/abs/2510.19463) | [PDF](https://arxiv.org/pdf/2510.19463.pdf)

**作者**: Hao-Chiang Shao, Chun-Hao Chang, Yu-Hsien Lin, Chia-Wen Lin, Shao-Yun Fang, Yan-Hsiu Liu

---

## 💡 一句话要点

**提出ReCAME-Net以解决IC缺陷分类中高度不平衡数据的挑战**

**关键词**: `IC缺陷分类` `高度不平衡数据` `多专家分类器` `区域通道注意力` `度量学习` `知识蒸馏`

## 📋 核心要点

1. 核心问题：真实IC缺陷数据高度不平衡，类内多样性和类间相似性导致分类困难
2. 方法要点：采用多专家分类器框架，集成区域通道注意力、度量学习损失和知识蒸馏
3. 实验或效果：在IC-Defect-14数据集上优于现有方法，并在公共数据集上保持竞争力

## 📄 摘要（原文）

> Despite significant advancements in deep classification techniques and in-lab
> automatic optical inspection models for long-tailed or highly imbalanced data,
> applying these approaches to real-world IC defect classification tasks remains
> challenging. This difficulty stems from two primary factors. First, real-world
> conditions, such as the high yield-rate requirements in the IC industry, result
> in data distributions that are far more skewed than those found in general
> public imbalanced datasets. Consequently, classifiers designed for open
> imbalanced datasets often fail to perform effectively in real-world scenarios.
> Second, real-world samples exhibit a mix of class-specific attributes and
> class-agnostic, domain-related features. This complexity adds significant
> difficulty to the classification process, particularly for highly imbalanced
> datasets. To address these challenges, this paper introduces the IC-Defect-14
> dataset, a large, highly imbalanced IC defect image dataset sourced from AOI
> systems deployed in real-world IC production lines. This dataset is
> characterized by its unique "intra-class clusters" property, which presents two
> major challenges: large intra-class diversity and high inter-class similarity.
> These characteristics, rarely found simultaneously in existing public datasets,
> significantly degrade the performance of current state-of-the-art classifiers
> for highly imbalanced data. To tackle this challenge, we propose ReCAME-Net,
> which follows a multi-expert classifier framework and integrates a regional
> channel attention module, metric learning losses, a hard category mining
> strategy, and a knowledge distillation procedure. Extensive experimental
> evaluations demonstrate that ReCAME-Net outperforms previous state-of-the-art
> models on the IC-Defect-14 dataset while maintaining comparable performance and
> competitiveness on general public datasets.

