---
layout: default
title: Data-Efficient Learning of Anomalous Diffusion with Wavelet Representations: Enabling Direct Learning from Experimental Trajectories
---

# Data-Efficient Learning of Anomalous Diffusion with Wavelet Representations: Enabling Direct Learning from Experimental Trajectories

**arXiv**: [2512.08510v1](https://arxiv.org/abs/2512.08510) | [PDF](https://arxiv.org/pdf/2512.08510.pdf)

**作者**: Gongyi Wang, Yu Zhang, Zihan Huang

---

## 💡 一句话要点

**提出基于小波表示的数据高效学习方法，以直接从实验轨迹学习异常扩散**

**关键词**: `异常扩散分析` `小波表示` `数据高效学习` `单粒子追踪` `实验轨迹学习` `扩散机制解耦`

## 📋 核心要点

1. 核心问题：机器学习分析异常扩散时，模拟数据与稀缺实验数据不匹配导致性能下降
2. 方法要点：使用六种小波族构建轨迹表示，结合小波模量尺度图以提升数据效率
3. 实验或效果：在模拟和实验轨迹上优于现有方法，用少量实验数据实现更优预测

## 📄 摘要（原文）

> Machine learning (ML) has become a versatile tool for analyzing anomalous diffusion trajectories, yet most existing pipelines are trained on large collections of simulated data. In contrast, experimental trajectories, such as those from single-particle tracking (SPT), are typically scarce and may differ substantially from the idealized models used for simulation, leading to degradation or even breakdown of performance when ML methods are applied to real data. To address this mismatch, we introduce a wavelet-based representation of anomalous diffusion that enables data-efficient learning directly from experimental recordings. This representation is constructed by applying six complementary wavelet families to each trajectory and combining the resulting wavelet modulus scalograms. We first evaluate the wavelet representation on simulated trajectories from the andi-datasets benchmark, where it clearly outperforms both feature-based and trajectory-based methods with as few as 1000 training trajectories and still retains an advantage on large training sets. We then use this representation to learn directly from experimental SPT trajectories of fluorescent beads diffusing in F-actin networks, where the wavelet representation remains superior to existing alternatives for both diffusion-exponent regression and mesh-size classification. In particular, when predicting the diffusion exponents of experimental trajectories, a model trained on 1200 experimental tracks using the wavelet representation achieves significantly lower errors than state-of-the-art deep learning models trained purely on $10^6$ simulated trajectories. We associate this data efficiency with the emergence of distinct scale fingerprints disentangling underlying diffusion mechanisms in the wavelet spectra.

