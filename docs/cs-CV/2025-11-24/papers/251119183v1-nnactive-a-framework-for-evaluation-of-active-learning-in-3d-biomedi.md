---
layout: default
title: nnActive: A Framework for Evaluation of Active Learning in 3D Biomedical Segmentation
---

# nnActive: A Framework for Evaluation of Active Learning in 3D Biomedical Segmentation

**arXiv**: [2511.19183v1](https://arxiv.org/abs/2511.19183) | [PDF](https://arxiv.org/pdf/2511.19183.pdf)

**作者**: Carsten T. Lüth, Jeremias Traub, Kim-Celine Kahl, Till J. Bungert, Lukas Klein, Lars Krämer, Paul F. Jaeger, Fabian Isensee, Klaus Maier-Hein

---

## 💡 一句话要点

**提出nnActive框架以解决3D生物医学分割中主动学习评估的缺陷**

**关键词**: `主动学习` `3D生物医学分割` `nnU-Net扩展` `标注效率` `随机采样策略` `开源框架`

## 📋 核心要点

1. 核心问题：3D生物医学分割依赖昂贵标注，主动学习评估存在四个常见缺陷，如数据集限制和基线不当。
2. 方法要点：nnActive扩展nnU-Net，使用部分标注和3D补丁查询，改进随机采样策略和效率指标。
3. 实验或效果：在四个数据集上，主动学习优于标准随机采样，但未可靠超越改进的随机采样。

## 📄 摘要（原文）

> Semantic segmentation is crucial for various biomedical applications, yet its reliance on large annotated datasets presents a bottleneck due to the high cost and specialized expertise required for manual labeling. Active Learning (AL) aims to mitigate this challenge by querying only the most informative samples, thereby reducing annotation effort. However, in the domain of 3D biomedical imaging, there is no consensus on whether AL consistently outperforms Random sampling. Four evaluation pitfalls hinder the current methodological assessment. These are (1) restriction to too few datasets and annotation budgets, (2) using 2D models on 3D images without partial annotations, (3) Random baseline not being adapted to the task, and (4) measuring annotation cost only in voxels. In this work, we introduce nnActive, an open-source AL framework that overcomes these pitfalls by (1) means of a large scale study spanning four biomedical imaging datasets and three label regimes, (2) extending nnU-Net by using partial annotations for training with 3D patch-based query selection, (3) proposing Foreground Aware Random sampling strategies tackling the foreground-background class imbalance of medical images and (4) propose the foreground efficiency metric, which captures the low annotation cost of background-regions. We reveal the following findings: (A) while all AL methods outperform standard Random sampling, none reliably surpasses an improved Foreground Aware Random sampling; (B) benefits of AL depend on task specific parameters; (C) Predictive Entropy is overall the best performing AL method, but likely requires the most annotation effort; (D) AL performance can be improved with more compute intensive design choices. As a holistic, open-source framework, nnActive can serve as a catalyst for research and application of AL in 3D biomedical imaging. Code is at: https://github.com/MIC-DKFZ/nnActive

