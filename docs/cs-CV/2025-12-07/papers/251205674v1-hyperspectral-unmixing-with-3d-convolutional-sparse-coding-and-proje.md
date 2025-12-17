---
layout: default
title: Hyperspectral Unmixing with 3D Convolutional Sparse Coding and Projected Simplex Volume Maximization
---

# Hyperspectral Unmixing with 3D Convolutional Sparse Coding and Projected Simplex Volume Maximization

**arXiv**: [2512.05674v1](https://arxiv.org/abs/2512.05674) | [PDF](https://arxiv.org/pdf/2512.05674.pdf)

**作者**: Gargi Panda, Soumitra Kundu, Saumik Bhattacharya, Aurobinda Routray

---

## 💡 一句话要点

**提出基于3D卷积稀疏编码网络与投影单纯形体积最大化的高光谱解混方法**

**关键词**: `高光谱解混` `3D卷积稀疏编码` `算法展开` `自编码器` `投影单纯形体积最大化`

## 📋 核心要点

1. 核心问题：高光谱解混旨在分离像素中的端元并估计其丰度分数。
2. 方法要点：通过算法展开构建3D-CSCNet，结合自编码器框架和PSVM算法初始化端元。
3. 实验或效果：在真实和模拟数据集上验证，3D-CSCNet优于现有方法。

## 📄 摘要（原文）

> Hyperspectral unmixing (HSU) aims to separate each pixel into its constituent endmembers and estimate their corresponding abundance fractions. This work presents an algorithm-unrolling-based network for the HSU task, named the 3D Convolutional Sparse Coding Network (3D-CSCNet), built upon a 3D CSC model. Unlike existing unrolling-based networks, our 3D-CSCNet is designed within the powerful autoencoder (AE) framework. Specifically, to solve the 3D CSC problem, we propose a 3D CSC block (3D-CSCB) derived through deep algorithm unrolling. Given a hyperspectral image (HSI), 3D-CSCNet employs the 3D-CSCB to estimate the abundance matrix. The use of 3D CSC enables joint learning of spectral and spatial relationships in the 3D HSI data cube. The estimated abundance matrix is then passed to the AE decoder to reconstruct the HSI, and the decoder weights are extracted as the endmember matrix. Additionally, we propose a projected simplex volume maximization (PSVM) algorithm for endmember estimation, and the resulting endmembers are used to initialize the decoder weights of 3D-CSCNet. Extensive experiments on three real datasets and one simulated dataset with three different signal-to-noise ratio (SNR) levels demonstrate that our 3D-CSCNet outperforms state-of-the-art methods.

