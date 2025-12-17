---
layout: default
title: Leveraging Compression to Construct Transferable Bitrate Ladders
---

# Leveraging Compression to Construct Transferable Bitrate Ladders

**arXiv**: [2512.12952v1](https://arxiv.org/abs/2512.12952) | [PDF](https://arxiv.org/pdf/2512.12952.pdf)

**作者**: Krishna Srikar Durbha, Hassene Tmar, Ping-Hao Wu, Ioannis Katsavounidis, Alan C. Bovik

---

## 💡 一句话要点

**提出基于压缩分析的机器学习方法，以构建可转移的比特率阶梯，提升视频编码效率。**

**关键词**: `视频编码` `比特率阶梯` `机器学习` `VMAF预测` `压缩分析` `质量评估`

## 📋 核心要点

1. 核心问题：传统比特率阶梯构建计算开销大，需高效替代方案。
2. 方法要点：通过分析压缩过程和源视频感知测量，预测压缩视频的VMAF分数。
3. 实验或效果：在大规模视频集上评估，优于现有方法，并探索不同编码设置下的性能。

## 📄 摘要（原文）

> Over the past few years, per-title and per-shot video encoding techniques have demonstrated significant gains as compared to conventional techniques such as constant CRF encoding and the fixed bitrate ladder. These techniques have demonstrated that constructing content-gnostic per-shot bitrate ladders can provide significant bitrate gains and improved Quality of Experience (QoE) for viewers under various network conditions. However, constructing a convex hull for every video incurs a significant computational overhead. Recently, machine learning-based bitrate ladder construction techniques have emerged as a substitute for convex hull construction. These methods operate by extracting features from source videos to train machine learning (ML) models to construct content-adaptive bitrate ladders. Here, we present a new ML-based bitrate ladder construction technique that accurately predicts the VMAF scores of compressed videos, by analyzing the compression procedure and by making perceptually relevant measurements on the source videos prior to compression. We evaluate the performance of our proposed framework against leading prior methods on a large corpus of videos. Since training ML models on every encoder setting is time-consuming, we also investigate how per-shot bitrate ladders perform under different encoding settings. We evaluate the performance of all models against the fixed bitrate ladder and the best possible convex hull constructed using exhaustive encoding with Bjontegaard-delta metrics.

