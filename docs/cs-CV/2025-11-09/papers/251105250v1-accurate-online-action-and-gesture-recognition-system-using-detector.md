---
layout: default
title: Accurate online action and gesture recognition system using detectors and Deep SPD Siamese Networks
---

# Accurate online action and gesture recognition system using detectors and Deep SPD Siamese Networks

**arXiv**: [2511.05250v1](https://arxiv.org/abs/2511.05250) | [PDF](https://arxiv.org/pdf/2511.05250.pdf)

**作者**: Mohamed Sanim Akremi, Rim Slama, Hedi Tabia

---

## 💡 一句话要点

**提出基于检测器和深度SPD孪生网络的在线动作识别系统，以处理未分割骨架序列流。**

**关键词**: `在线动作识别` `骨架序列` `SPD矩阵` `孪生网络` `手势识别` `身体动作识别`

## 📋 核心要点

1. 核心问题：在线连续动作识别在未分割骨架序列中难以实时检测和分类。
2. 方法要点：使用SPD矩阵表示骨架数据，结合孪生网络学习语义相似性进行检测和分类。
3. 实验或效果：在手势和身体动作基准测试中，多数情况下优于现有先进方法。

## 📄 摘要（原文）

> Online continuous motion recognition is a hot topic of research since it is
> more practical in real life application cases. Recently, Skeleton-based
> approaches have become increasingly popular, demonstrating the power of using
> such 3D temporal data. However, most of these works have focused on
> segment-based recognition and are not suitable for the online scenarios. In
> this paper, we propose an online recognition system for skeleton sequence
> streaming composed from two main components: a detector and a classifier, which
> use a Semi-Positive Definite (SPD) matrix representation and a Siamese network.
> The powerful statistical representations for the skeletal data given by the SPD
> matrices and the learning of their semantic similarity by the Siamese network
> enable the detector to predict time intervals of the motions throughout an
> unsegmented sequence. In addition, they ensure the classifier capability to
> recognize the motion in each predicted interval. The proposed detector is
> flexible and able to identify the kinetic state continuously. We conduct
> extensive experiments on both hand gesture and body action recognition
> benchmarks to prove the accuracy of our online recognition system which in most
> cases outperforms state-of-the-art performances.

