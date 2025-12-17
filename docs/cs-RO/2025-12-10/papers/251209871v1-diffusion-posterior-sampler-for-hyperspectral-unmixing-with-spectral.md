---
layout: default
title: Diffusion Posterior Sampler for Hyperspectral Unmixing with Spectral Variability Modeling
---

# Diffusion Posterior Sampler for Hyperspectral Unmixing with Spectral Variability Modeling

**arXiv**: [2512.09871v1](https://arxiv.org/abs/2512.09871) | [PDF](https://arxiv.org/pdf/2512.09871.pdf)

**作者**: Yimin Zhu, Lincoln Linlin Xu

---

## 💡 一句话要点

**提出DPS4Un扩散后验采样器，用于高光谱解混与光谱变异性建模**

**关键词**: `高光谱解混` `扩散模型` `光谱变异性` `贝叶斯框架` `超像素分割`

## 📋 核心要点

1. 核心问题：线性光谱混合模型中的光谱先验分布与光谱变异性建模挑战
2. 方法要点：利用预训练条件扩散模型作为后验采样器，结合超像素构建端元束训练先验
3. 实验或效果：在三个真实基准数据集上优于现有高光谱解混方法

## 📄 摘要（原文）

> Linear spectral mixture models (LMM) provide a concise form to disentangle the constituent materials (endmembers) and their corresponding proportions (abundance) in a single pixel. The critical challenges are how to model the spectral prior distribution and spectral variability. Prior knowledge and spectral variability can be rigorously modeled under the Bayesian framework, where posterior estimation of Abundance is derived by combining observed data with endmember prior distribution. Considering the key challenges and the advantages of the Bayesian framework, a novel method using a diffusion posterior sampler for semiblind unmixing, denoted as DPS4Un, is proposed to deal with these challenges with the following features: (1) we view the pretrained conditional spectrum diffusion model as a posterior sampler, which can combine the learned endmember prior with observation to get the refined abundance distribution. (2) Instead of using the existing spectral library as prior, which may raise bias, we establish the image-based endmember bundles within superpixels, which are used to train the endmember prior learner with diffusion model. Superpixels make sure the sub-scene is more homogeneous. (3) Instead of using the image-level data consistency constraint, the superpixel-based data fidelity term is proposed. (4) The endmember is initialized as Gaussian noise for each superpixel region, DPS4Un iteratively updates the abundance and endmember, contributing to spectral variability modeling. The experimental results on three real-world benchmark datasets demonstrate that DPS4Un outperforms the state-of-the-art hyperspectral unmixing methods.

