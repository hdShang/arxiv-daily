---
layout: default
title: Evaluating Latent Generative Paradigms for High-Fidelity 3D Shape Completion from a Single Depth Image
---

# Evaluating Latent Generative Paradigms for High-Fidelity 3D Shape Completion from a Single Depth Image

**arXiv**: [2511.11074v1](https://arxiv.org/abs/2511.11074) | [PDF](https://arxiv.org/pdf/2511.11074.pdf)

**作者**: Matthias Humt, Ulrich Hillenbrand, Rudolph Triebel

---

## 💡 一句话要点

**比较扩散与自回归模型，实现单深度图像高保真3D形状补全**

**关键词**: `3D形状补全` `生成模型比较` `深度图像` `扩散模型` `自回归变换器` `潜在空间`

## 📋 核心要点

1. 核心问题：生成模型在3D数据任务中缺乏共识，部分条件信息如单深度图像未充分评估。
2. 方法要点：适配扩散模型和自回归变换器，用于生成形状建模与补全任务。
3. 实验效果：扩散模型在连续潜在空间表现最优，自回归模型在离散空间可匹敌。

## 📄 摘要（原文）

> While generative models have seen significant adoption across a wide range of data modalities, including 3D data, a consensus on which model is best suited for which task has yet to be reached. Further, conditional information such as text and images to steer the generation process are frequently employed, whereas others, like partial 3D data, have not been thoroughly evaluated. In this work, we compare two of the most promising generative models--Denoising Diffusion Probabilistic Models and Autoregressive Causal Transformers--which we adapt for the tasks of generative shape modeling and completion. We conduct a thorough quantitative evaluation and comparison of both tasks, including a baseline discriminative model and an extensive ablation study. Our results show that (1) the diffusion model with continuous latents outperforms both the discriminative model and the autoregressive approach and delivers state-of-the-art performance on multi-modal shape completion from a single, noisy depth image under realistic conditions and (2) when compared on the same discrete latent space, the autoregressive model can match or exceed diffusion performance on these tasks.

