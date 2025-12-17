---
layout: default
title: InfoMotion: A Graph-Based Approach to Video Dataset Distillation for Echocardiography
---

# InfoMotion: A Graph-Based Approach to Video Dataset Distillation for Echocardiography

**arXiv**: [2512.09422v1](https://arxiv.org/abs/2512.09422) | [PDF](https://arxiv.org/pdf/2512.09422.pdf)

**作者**: Zhe Li, Hadrien Reynaud, Alberto Gomez, Bernhard Kainz

---

## 💡 一句话要点

**提出基于图的方法InfoMotion，用于超声心动图视频数据集蒸馏以提升效率。**

**关键词**: `视频数据集蒸馏` `超声心动图` `运动特征提取` `图算法` `医疗视频分析`

## 📋 核心要点

1. 核心问题：超声心动图视频数据规模大，存储、计算和模型训练效率面临挑战。
2. 方法要点：提取运动特征捕获时序动态，构建类内图并使用Infomap算法选择代表性样本。
3. 实验或效果：在EchoNet-Dynamic数据集上，仅用25个合成视频实现69.38%的测试准确率。

## 📄 摘要（原文）

> Echocardiography playing a critical role in the diagnosis and monitoring of cardiovascular diseases as a non-invasive real-time assessment of cardiac structure and function. However, the growing scale of echocardiographic video data presents significant challenges in terms of storage, computation, and model training efficiency. Dataset distillation offers a promising solution by synthesizing a compact, informative subset of data that retains the key clinical features of the original dataset. In this work, we propose a novel approach for distilling a compact synthetic echocardiographic video dataset. Our method leverages motion feature extraction to capture temporal dynamics, followed by class-wise graph construction and representative sample selection using the Infomap algorithm. This enables us to select a diverse and informative subset of synthetic videos that preserves the essential characteristics of the original dataset. We evaluate our approach on the EchoNet-Dynamic datasets and achieve a test accuracy of \(69.38\%\) using only \(25\) synthetic videos. These results demonstrate the effectiveness and scalability of our method for medical video dataset distillation.

