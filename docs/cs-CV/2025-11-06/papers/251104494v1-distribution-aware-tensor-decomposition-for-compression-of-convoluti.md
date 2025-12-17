---
layout: default
title: Distribution-Aware Tensor Decomposition for Compression of Convolutional Neural Networks
---

# Distribution-Aware Tensor Decomposition for Compression of Convolutional Neural Networks

**arXiv**: [2511.04494v1](https://arxiv.org/abs/2511.04494) | [PDF](https://arxiv.org/pdf/2511.04494.pdf)

**作者**: Alper Kalle, Theo Rudkiewicz, Mohamed-Oumar Ouerfelli, Mohamed Tamaazousti

---

## 💡 一句话要点

**提出分布感知张量分解方法以压缩卷积神经网络，无需微调保持高精度**

**关键词**: `神经网络压缩` `张量分解` `数据感知优化` `卷积神经网络` `低秩近似`

## 📋 核心要点

1. 核心问题：神经网络压缩中传统方法使用权重空间各向同性范数，忽略数据分布影响。
2. 方法要点：引入数据感知范数，最小化层输出分布变化，优化Tucker-2和CPD分解。
3. 实验效果：在多个CNN和数据集上验证，无需微调即可实现竞争性精度，且可跨数据集迁移。

## 📄 摘要（原文）

> Neural networks are widely used for image-related tasks but typically demand
> considerable computing power. Once a network has been trained, however, its
> memory- and compute-footprint can be reduced by compression. In this work, we
> focus on compression through tensorization and low-rank representations.
> Whereas classical approaches search for a low-rank approximation by minimizing
> an isotropic norm such as the Frobenius norm in weight-space, we use
> data-informed norms that measure the error in function space. Concretely, we
> minimize the change in the layer's output distribution, which can be expressed
> as $\lVert (W - \widetilde{W}) \Sigma^{1/2}\rVert_F$ where $\Sigma^{1/2}$ is
> the square root of the covariance matrix of the layer's input and $W$,
> $\widetilde{W}$ are the original and compressed weights. We propose new
> alternating least square algorithms for the two most common tensor
> decompositions (Tucker-2 and CPD) that directly optimize the new norm. Unlike
> conventional compression pipelines, which almost always require
> post-compression fine-tuning, our data-informed approach often achieves
> competitive accuracy without any fine-tuning. We further show that the same
> covariance-based norm can be transferred from one dataset to another with only
> a minor accuracy drop, enabling compression even when the original training
> dataset is unavailable. Experiments on several CNN architectures (ResNet-18/50,
> and GoogLeNet) and datasets (ImageNet, FGVC-Aircraft, Cifar10, and Cifar100)
> confirm the advantages of the proposed method.

