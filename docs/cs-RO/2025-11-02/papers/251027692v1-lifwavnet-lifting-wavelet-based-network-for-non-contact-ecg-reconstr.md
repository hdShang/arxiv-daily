---
layout: default
title: LifWavNet: Lifting Wavelet-based Network for Non-contact ECG Reconstruction from Radar
---

# LifWavNet: Lifting Wavelet-based Network for Non-contact ECG Reconstruction from Radar

**arXiv**: [2510.27692v1](https://arxiv.org/abs/2510.27692) | [PDF](https://arxiv.org/pdf/2510.27692.pdf)

**作者**: Soumitra Kundu, Gargi Panda, Saumik Bhattacharya, Aurobinda Routray, Rajlakshmi Guha

---

## 💡 一句话要点

**提出LifWavNet网络，基于可学习提升小波实现雷达信号到非接触ECG重建。**

**关键词**: `非接触ECG重建` `雷达信号处理` `提升小波网络` `多分辨率分析` `STFT损失函数` `心脏监测`

## 📋 核心要点

1. 核心问题：从雷达信号重建非接触心电图，实现无扰心脏监测。
2. 方法要点：采用多分辨率分析与合成模型，结合可学习提升小波和逆提升单元。
3. 实验效果：在公共数据集上优于现有方法，提升ECG重建和心率变异性估计精度。

## 📄 摘要（原文）

> Non-contact electrocardiogram (ECG) reconstruction from radar signals offers
> a promising approach for unobtrusive cardiac monitoring. We present LifWavNet,
> a lifting wavelet network based on a multi-resolution analysis and synthesis
> (MRAS) model for radar-to-ECG reconstruction. Unlike prior models that use
> fixed wavelet approaches, LifWavNet employs learnable lifting wavelets with
> lifting and inverse lifting units to adaptively capture radar signal features
> and synthesize physiologically meaningful ECG waveforms. To improve
> reconstruction fidelity, we introduce a multi-resolution short-time Fourier
> transform (STFT) loss, that enforces consistency with the ground-truth ECG in
> both temporal and spectral domains. Evaluations on two public datasets
> demonstrate that LifWavNet outperforms state-of-the-art methods in ECG
> reconstruction and downstream vital sign estimation (heart rate and heart rate
> variability). Furthermore, intermediate feature visualization highlights the
> interpretability of multi-resolution decomposition and synthesis in
> radar-to-ECG reconstruction. These results establish LifWavNet as a robust
> framework for radar-based non-contact ECG measurement.

