---
layout: default
title: DiCaP: Distribution-Calibrated Pseudo-labeling for Semi-Supervised Multi-Label Learning
---

# DiCaP: Distribution-Calibrated Pseudo-labeling for Semi-Supervised Multi-Label Learning

**arXiv**: [2511.20225v1](https://arxiv.org/abs/2511.20225) | [PDF](https://arxiv.org/pdf/2511.20225.pdf)

**作者**: Bo Han, Zhuoming Li, Xiaoyu Wang, Yaxin Hou, Hui Liu, Junhui Hou, Yuheng Jia

---

## 💡 一句话要点

**提出DiCaP框架以解决半监督多标签学习中伪标签权重分配问题**

**关键词**: `半监督多标签学习` `伪标签校准` `分布校准` `对比学习` `多标签分类`

## 📋 核心要点

1. 核心问题：现有方法对伪标签分配等权重，易放大噪声预测影响性能。
2. 方法要点：基于后验精度估计伪标签权重，并采用双阈值机制区分样本。
3. 实验或效果：在多个基准数据集上性能提升，最高超越SOTA方法4.27%。

## 📄 摘要（原文）

> Semi-supervised multi-label learning (SSMLL) aims to address the challenge of limited labeled data in multi-label learning (MLL) by leveraging unlabeled data to improve the model's performance. While pseudo-labeling has become a dominant strategy in SSMLL, most existing methods assign equal weights to all pseudo-labels regardless of their quality, which can amplify the impact of noisy or uncertain predictions and degrade the overall performance. In this paper, we theoretically verify that the optimal weight for a pseudo-label should reflect its correctness likelihood. Empirically, we observe that on the same dataset, the correctness likelihood distribution of unlabeled data remains stable, even as the number of labeled training samples varies. Building on this insight, we propose Distribution-Calibrated Pseudo-labeling (DiCaP), a correctness-aware framework that estimates posterior precision to calibrate pseudo-label weights. We further introduce a dual-thresholding mechanism to separate confident and ambiguous regions: confident samples are pseudo-labeled and weighted accordingly, while ambiguous ones are explored by unsupervised contrastive learning. Experiments conducted on multiple benchmark datasets verify that our method achieves consistent improvements, surpassing state-of-the-art methods by up to 4.27%.

