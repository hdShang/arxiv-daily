---
layout: default
title: TARFVAE: Efficient One-Step Generative Time Series Forecasting via TARFLOW based VAE
---

# TARFVAE: Efficient One-Step Generative Time Series Forecasting via TARFLOW based VAE

**arXiv**: [2511.22853v1](https://arxiv.org/abs/2511.22853) | [PDF](https://arxiv.org/pdf/2511.22853.pdf)

**作者**: Jiawen Wei, Lan Jiang, Pengbo Wei, Ziwen Ye, Teng Song, Chen Chen, Guangrui Ma

---

## 💡 一句话要点

**提出TARFVAE框架，结合TARFLOW与VAE实现高效一步生成式时间序列预测。**

**关键词**: `时间序列预测` `生成式模型` `变分自编码器` `自回归流` `一步生成` `高效预测`

## 📋 核心要点

1. 针对现有生成式方法预测效率低、长时预测实验不足的问题，提出TARFVAE框架。
2. 核心方法为在VAE中集成TARFLOW模块，打破高斯假设，提升潜在空间信息量，实现一步快速生成。
3. 实验表明，TARFVAE在基准数据集上超越现有方法，保持高效预测速度，验证其有效性。

## 📄 摘要（原文）

> Time series data is ubiquitous, with forecasting applications spanning from finance to healthcare. Beyond popular deterministic methods, generative models are gaining attention due to advancements in areas like image synthesis and video generation, as well as their inherent ability to provide probabilistic predictions. However, existing generative approaches mostly involve recurrent generative operations or repeated denoising steps, making the prediction laborious, particularly for long-term forecasting. Most of them only conduct experiments for relatively short-term forecasting, with limited comparison to deterministic methods in long-term forecasting, leaving their practical advantages unclear. This paper presents TARFVAE, a novel generative framework that combines the Transformer-based autoregressive flow (TARFLOW) and variational autoencoder (VAE) for efficient one-step generative time series forecasting. Inspired by the rethinking that complex architectures for extracting time series representations might not be necessary, we add a flow module, TARFLOW, to VAE to promote spontaneous learning of latent variables that benefit predictions. TARFLOW enhances VAE's posterior estimation by breaking the Gaussian assumption, thereby enabling a more informative latent space. TARFVAE uses only the forward process of TARFLOW, avoiding autoregressive inverse operations and thus ensuring fast generation. During generation, it samples from the prior latent space and directly generates full-horizon forecasts via the VAE decoder. With simple MLP modules, TARFVAE achieves superior performance over state-of-the-art deterministic and generative models across different forecast horizons on benchmark datasets while maintaining efficient prediction speed, demonstrating its effectiveness as an efficient and powerful solution for generative time series forecasting.

