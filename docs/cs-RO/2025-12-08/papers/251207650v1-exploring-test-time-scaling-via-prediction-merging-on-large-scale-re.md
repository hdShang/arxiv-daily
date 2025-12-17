---
layout: default
title: Exploring Test-time Scaling via Prediction Merging on Large-Scale Recommendation
---

# Exploring Test-time Scaling via Prediction Merging on Large-Scale Recommendation

**arXiv**: [2512.07650v1](https://arxiv.org/abs/2512.07650) | [PDF](https://arxiv.org/pdf/2512.07650.pdf)

**作者**: Fuyuan Lyu, Zhentai Chen, Jingyan Jiang, Lingjie Li, Xing Tang, Xiuqiang He, Xue Liu

---

## 💡 一句话要点

**提出测试时缩放方法，通过预测合并提升大规模推荐系统效率**

**关键词**: `测试时缩放` `预测合并` `大规模推荐系统` `模型异质性` `计算效率` `在线推理`

## 📋 核心要点

1. 核心问题：如何在测试时高效利用计算资源，替代传统训练时参数缩放，以提升推荐系统性能
2. 方法要点：利用模型架构异质性或同构初始化随机性生成多样化预测，并通过合并增强输出
3. 实验或效果：在三个基准测试中评估八种模型，证明方法有效且优于参数缩放，支持在线并行加速

## 📄 摘要（原文）

> Inspired by the success of language models (LM), scaling up deep learning recommendation systems (DLRS) has become a recent trend in the community. All previous methods tend to scale up the model parameters during training time. However, how to efficiently utilize and scale up computational resources during test time remains underexplored, which can prove to be a scaling-efficient approach and bring orthogonal improvements in LM domains. The key point in applying test-time scaling to DLRS lies in effectively generating diverse yet meaningful outputs for the same instance. We propose two ways: One is to explore the heterogeneity of different model architectures. The other is to utilize the randomness of model initialization under a homogeneous architecture. The evaluation is conducted across eight models, including both classic and SOTA models, on three benchmarks. Sufficient evidence proves the effectiveness of both solutions. We further prove that under the same inference budget, test-time scaling can outperform parameter scaling. Our test-time scaling can also be seamlessly accelerated with the increase in parallel servers when deployed online, without affecting the inference time on the user side. Code is available.

