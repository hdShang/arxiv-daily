---
layout: default
title: MeanFlow Transformers with Representation Autoencoders
---

# MeanFlow Transformers with Representation Autoencoders

**arXiv**: [2511.13019v1](https://arxiv.org/abs/2511.13019) | [PDF](https://arxiv.org/pdf/2511.13019.pdf)

**作者**: Zheyuan Hu, Chieh-Hsin Lai, Ge Wu, Yuki Mitsufuji, Stefano Ermon

---

## 💡 一句话要点

**提出基于表示自编码器的MeanFlow方法，以高效稳定训练和采样，用于图像生成。**

**关键词**: `图像生成` `表示自编码器` `MeanFlow` `蒸馏训练` `高效采样`

## 📋 核心要点

1. 核心问题：MeanFlow训练计算量大、不稳定，且依赖复杂超参数指导。
2. 方法要点：在表示自编码器潜在空间训练，采用一致性中训练和两阶段蒸馏方案。
3. 实验效果：在ImageNet 256上1步FID达2.03，降低采样GFLOPS 38%和训练成本83%。

## 📄 摘要（原文）

> MeanFlow (MF) is a diffusion-motivated generative model that enables efficient few-step generation by learning long jumps directly from noise to data. In practice, it is often used as a latent MF by leveraging the pre-trained Stable Diffusion variational autoencoder (SD-VAE) for high-dimensional data modeling. However, MF training remains computationally demanding and is often unstable. During inference, the SD-VAE decoder dominates the generation cost, and MF depends on complex guidance hyperparameters for class-conditional generation. In this work, we develop an efficient training and sampling scheme for MF in the latent space of a Representation Autoencoder (RAE), where a pre-trained vision encoder (e.g., DINO) provides semantically rich latents paired with a lightweight decoder. We observe that naive MF training in the RAE latent space suffers from severe gradient explosion. To stabilize and accelerate training, we adopt Consistency Mid-Training for trajectory-aware initialization and use a two-stage scheme: distillation from a pre-trained flow matching teacher to speed convergence and reduce variance, followed by an optional bootstrapping stage with a one-point velocity estimator to further reduce deviation from the oracle mean flow. This design removes the need for guidance, simplifies training configurations, and reduces computation in both training and sampling. Empirically, our method achieves a 1-step FID of 2.03, outperforming vanilla MF's 3.43, while reducing sampling GFLOPS by 38% and total training cost by 83% on ImageNet 256. We further scale our approach to ImageNet 512, achieving a competitive 1-step FID of 3.23 with the lowest GFLOPS among all baselines. Code is available at https://github.com/sony/mf-rae.

