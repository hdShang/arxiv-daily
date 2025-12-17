---
layout: default
title: Learned Image Compression for Earth Observation: Implications for Downstream Segmentation Tasks
---

# Learned Image Compression for Earth Observation: Implications for Downstream Segmentation Tasks

**arXiv**: [2512.01788v1](https://arxiv.org/abs/2512.01788) | [PDF](https://arxiv.org/pdf/2512.01788.pdf)

**作者**: Christian Mollière, Iker Cumplido, Marco Zeulner, Lukas Liesenhoff, Matthias Schubert, Julia Gottfriedsen

---

## 💡 一句话要点

**评估学习型压缩在遥感图像压缩中的性能，对比传统方法对分割任务的影响**

**关键词**: `遥感图像压缩` `学习型压缩` `图像分割` `JPEG 2000` `任务特定优化`

## 📋 核心要点

1. 核心问题：卫星遥感数据增长带来传输存储挑战，需压缩数据同时保留关键信息
2. 方法要点：比较传统JPEG 2000与学习型压缩（离散混合高斯似然）在三个分割任务上的表现
3. 实验或效果：学习型压缩在大规模多通道光学图像上优于JPEG 2000，但在小规模单通道热红外数据上传统方法仍具竞争力

## 📄 摘要（原文）

> The rapid growth of data from satellite-based Earth observation (EO) systems poses significant challenges in data transmission and storage. We evaluate the potential of task-specific learned compression algorithms in this context to reduce data volumes while retaining crucial information. In detail, we compare traditional compression (JPEG 2000) versus a learned compression approach (Discretized Mixed Gaussian Likelihood) on three EO segmentation tasks: Fire, cloud, and building detection. Learned compression notably outperforms JPEG 2000 for large-scale, multi-channel optical imagery in both reconstruction quality (PSNR) and segmentation accuracy. However, traditional codecs remain competitive on smaller, single-channel thermal infrared datasets due to limited data and architectural constraints. Additionally, joint end-to-end optimization of compression and segmentation models does not improve performance over standalone optimization.

