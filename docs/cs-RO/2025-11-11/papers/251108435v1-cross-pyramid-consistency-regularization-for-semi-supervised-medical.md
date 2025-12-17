---
layout: default
title: Cross-pyramid consistency regularization for semi-supervised medical image segmentation
---

# Cross-pyramid consistency regularization for semi-supervised medical image segmentation

**arXiv**: [2511.08435v1](https://arxiv.org/abs/2511.08435) | [PDF](https://arxiv.org/pdf/2511.08435.pdf)

**作者**: Matus Bojko, Maros Kollar, Marek Jakab, Wanda Benesova

---

## 💡 一句话要点

**提出跨金字塔一致性正则化以提升半监督医学图像分割性能**

**关键词**: `半监督学习` `医学图像分割` `一致性正则化` `金字塔网络` `知识蒸馏`

## 📋 核心要点

1. 核心问题：半监督学习在医学图像分割中如何有效利用未标记数据
2. 方法要点：设计双分支金字塔网络，结合跨解码器金字塔预测一致性正则化
3. 实验或效果：在公共数据集上优于五种自监督方法，与最新方法性能相当

## 📄 摘要（原文）

> Semi-supervised learning (SSL) enables training of powerful models with the assumption of limited, carefully labelled data and a large amount of unlabeled data to support the learning. In this paper, we propose a hybrid consistency learning approach to effectively exploit unlabeled data for semi-supervised medical image segmentation by leveraging Cross-Pyramid Consistency Regularization (CPCR) between two decoders. First, we design a hybrid Dual Branch Pyramid Network (DBPNet), consisting of an encoder and two decoders that differ slightly, each producing a pyramid of perturbed auxiliary predictions across multiple resolution scales. Second, we present a learning strategy for this network named CPCR that combines existing consistency learning and uncertainty minimization approaches on the main output predictions of decoders with our novel regularization term. More specifically, in this term, we extend the soft-labeling setting to pyramid predictions across decoders to support knowledge distillation in deep hierarchical features. Experimental results show that DBPNet with CPCR outperforms five state-of-the-art self-supervised learning methods and has comparable performance with recent ones on a public benchmark dataset.

