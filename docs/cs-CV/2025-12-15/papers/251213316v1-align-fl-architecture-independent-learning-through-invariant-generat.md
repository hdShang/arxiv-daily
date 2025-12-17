---
layout: default
title: ALIGN-FL: Architecture-independent Learning through Invariant Generative component sharing in Federated Learning
---

# ALIGN-FL: Architecture-independent Learning through Invariant Generative component sharing in Federated Learning

**arXiv**: [2512.13316v1](https://arxiv.org/abs/2512.13316) | [PDF](https://arxiv.org/pdf/2512.13316.pdf)

**作者**: Mayank Gulati, Benedikt Groß, Gerhard Wunder

---

## 💡 一句话要点

**提出ALIGN-FL，通过选择性共享生成组件解决联邦学习中高度非独立同分布数据的学习挑战。**

**关键词**: `联邦学习` `非独立同分布数据` `隐私保护生成模型` `异构架构` `差分隐私` `生成组件共享`

## 📋 核心要点

1. 核心问题：联邦学习中数据分布高度非独立同分布，导致模型训练困难。
2. 方法要点：仅共享生成能力，结合差分隐私和Lipschitz正则化，支持异构客户端架构。
3. 实验效果：在MNIST和Fashion-MNIST数据集上验证，有效处理异常值并保持模型效用。

## 📄 摘要（原文）

> We present ALIGN-FL, a novel approach to distributed learning that addresses the challenge of learning from highly disjoint data distributions through selective sharing of generative components. Instead of exchanging full model parameters, our framework enables privacy-preserving learning by transferring only generative capabilities across clients, while the server performs global training using synthetic samples. Through complementary privacy mechanisms: DP-SGD with adaptive clipping and Lipschitz regularized VAE decoders and a stateful architecture supporting heterogeneous clients, we experimentally validate our approach on MNIST and Fashion-MNIST datasets with cross-domain outliers. Our analysis demonstrates that both privacy mechanisms effectively map sensitive outliers to typical data points while maintaining utility in extreme Non-IID scenarios typical of cross-silo collaborations.
>   Index Terms: Client-invariant Learning, Federated Learning (FL), Privacy-preserving Generative Models, Non-Independent and Identically Distributed (Non-IID), Heterogeneous Architectures

