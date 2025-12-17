---
layout: default
title: Quanvolutional Neural Networks for Spectrum Peak-Finding
---

# Quanvolutional Neural Networks for Spectrum Peak-Finding

**arXiv**: [2512.13125v1](https://arxiv.org/abs/2512.13125) | [PDF](https://arxiv.org/pdf/2512.13125.pdf)

**作者**: Lukas Bischof, Rudolf M. Füchslin, Kurt Stockinger, Pavel Sulimov

---

## 💡 一句话要点

**提出量子卷积神经网络用于光谱峰值查找，在合成NMR数据集上优于经典CNN。**

**关键词**: `量子卷积神经网络` `光谱分析` `峰值查找` `NMR光谱` `量子机器学习`

## 📋 核心要点

1. 核心问题：光谱（如NMR）峰值查找与定位是复杂分子分析中的挑战性任务。
2. 方法要点：设计可解释的量子卷积神经网络架构，直接与经典CNN对比。
3. 实验或效果：在困难光谱上，F1分数提升11%，峰值位置估计平均绝对误差降低30%。

## 📄 摘要（原文）

> The analysis of spectra, such as Nuclear Magnetic Resonance (NMR) spectra, for the comprehensive characterization of peaks is a challenging task for both experts and machines, especially with complex molecules. This process, also known as deconvolution, involves identifying and quantifying the peaks in the spectrum. Machine learning techniques have shown promising results in automating this process. With the advent of quantum computing, there is potential to further enhance these techniques. In this work, inspired by the success of classical Convolutional Neural Networks (CNNs), we explore the use of Quanvolutional Neural Networks (QuanvNNs) for the multi-task peak finding problem, involving both peak counting and position estimation. We implement a simple and interpretable QuanvNN architecture that can be directly compared to its classical CNN counterpart, and evaluate its performance on a synthetic NMR-inspired dataset. Our results demonstrate that QuanvNNs outperform classical CNNs on challenging spectra, achieving an 11\% improvement in F1 score and a 30\% reduction in mean absolute error for peak position estimation. Additionally, QuanvNNs appear to exhibit better convergence stability for harder problems.

