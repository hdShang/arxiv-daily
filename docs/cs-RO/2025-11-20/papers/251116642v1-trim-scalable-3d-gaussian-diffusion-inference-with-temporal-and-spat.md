---
layout: default
title: TRIM: Scalable 3D Gaussian Diffusion Inference with Temporal and Spatial Trimming
---

# TRIM: Scalable 3D Gaussian Diffusion Inference with Temporal and Spatial Trimming

**arXiv**: [2511.16642v1](https://arxiv.org/abs/2511.16642) | [PDF](https://arxiv.org/pdf/2511.16642.pdf)

**作者**: Zeyuan Yin, Xiaoming Liu

---

## 💡 一句话要点

**提出TRIM方法以加速3D高斯扩散模型推理，通过时空修剪提升效率与质量**

**关键词**: `3D高斯扩散模型` `推理加速` `轨迹缩减` `实例掩码去噪` `后训练优化` `可扩展生成`

## 📋 核心要点

1. 核心问题：3D高斯扩散模型因高斯基元数量庞大，导致去噪和后处理耗时，推理缓慢且可扩展性差
2. 方法要点：结合轨迹缩减和实例掩码去噪，使用轻量选择器评估潜在基元，并修剪冗余背景区域
3. 实验或效果：广泛实验表明TRIM显著提升3D生成的效率与质量，支持推理时缩放

## 📄 摘要（原文）

> Recent advances in 3D Gaussian diffusion models suffer from time-intensive denoising and post-denoising processing due to the massive number of Gaussian primitives, resulting in slow generation and limited scalability along sampling trajectories. To improve the efficiency of 3D diffusion models, we propose $\textbf{TRIM}$ ($\textbf{T}$rajectory $\textbf{R}$eduction and $\textbf{I}$nstance $\textbf{M}$ask denoising), a post-training approach that incorporates both temporal and spatial trimming strategies, to accelerate inference without compromising output quality while supporting the inference-time scaling for Gaussian diffusion models. Instead of scaling denoising trajectories in a costly end-to-end manner, we develop a lightweight selector model to evaluate latent Gaussian primitives derived from multiple sampled noises, enabling early trajectory reduction by selecting candidates with high-quality potential. Furthermore, we introduce instance mask denoising to prune learnable Gaussian primitives by filtering out redundant background regions, reducing inference computation at each denoising step. Extensive experiments and analysis demonstrate that TRIM significantly improves both the efficiency and quality of 3D generation. Source code is available at $\href{https://github.com/zeyuanyin/TRIM}{link}$.

