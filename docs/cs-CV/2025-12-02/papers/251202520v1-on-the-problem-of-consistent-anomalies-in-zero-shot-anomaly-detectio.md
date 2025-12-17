---
layout: default
title: On the Problem of Consistent Anomalies in Zero-Shot Anomaly Detection
---

# On the Problem of Consistent Anomalies in Zero-Shot Anomaly Detection

**arXiv**: [2512.02520v1](https://arxiv.org/abs/2512.02520) | [PDF](https://arxiv.org/pdf/2512.02520.pdf)

**作者**: Tai Le-Gia

---

## 💡 一句话要点

**提出CoDeGraph框架以解决零样本异常检测中的一致异常问题**

**关键词**: `零样本异常检测` `一致异常` `图神经网络` `医学影像分析` `视觉Transformer`

## 📋 核心要点

1. 核心问题：一致异常导致基于距离的方法系统性偏差，影响零样本异常分类与分割。
2. 方法要点：基于相似性缩放和邻居耗尽现象，构建多阶段图框架CoDeGraph过滤一致异常。
3. 实验或效果：扩展至3D医学影像，实现无训练样本的零样本异常检测，并桥接批处理和文本方法。

## 📄 摘要（原文）

> Zero-shot anomaly classification and segmentation (AC/AS) aim to detect anomalous samples and regions without any training data, a capability increasingly crucial in industrial inspection and medical imaging. This dissertation aims to investigate the core challenges of zero-shot AC/AS and presents principled solutions rooted in theory and algorithmic design.
>   We first formalize the problem of consistent anomalies, a failure mode in which recurring similar anomalies systematically bias distance-based methods. By analyzing the statistical and geometric behavior of patch representations from pre-trained Vision Transformers, we identify two key phenomena - similarity scaling and neighbor-burnout - that describe how relationships among normal patches change with and without consistent anomalies in settings characterized by highly similar objects.
>   We then introduce CoDeGraph, a graph-based framework for filtering consistent anomalies built on the similarity scaling and neighbor-burnout phenomena. Through multi-stage graph construction, community detection, and structured refinement, CoDeGraph effectively suppresses the influence of consistent anomalies.
>   Next, we extend this framework to 3D medical imaging by proposing a training-free, computationally efficient volumetric tokenization strategy for MRI data. This enables a genuinely zero-shot 3D anomaly detection pipeline and shows that volumetric anomaly segmentation is achievable without any 3D training samples.
>   Finally, we bridge batch-based and text-based zero-shot methods by demonstrating that CoDeGraph-derived pseudo-masks can supervise prompt-driven vision-language models. Together, this dissertation provides theoretical understanding and practical solutions for the zero-shot AC/AS problem.

