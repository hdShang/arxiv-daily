---
layout: default
title: ParaBlock: Communication-Computation Parallel Block Coordinate Federated Learning for Large Language Models
---

# ParaBlock: Communication-Computation Parallel Block Coordinate Federated Learning for Large Language Models

**arXiv**: [2511.19959v1](https://arxiv.org/abs/2511.19959) | [PDF](https://arxiv.org/pdf/2511.19959.pdf)

**作者**: Yujia Wang, Yuanpu Cao, Jinghui Chen

---

## 💡 一句话要点

**提出ParaBlock以解决大语言模型联邦学习中的通信延迟问题**

**关键词**: `联邦学习` `大语言模型` `块坐标下降` `通信效率` `并行计算`

## 📋 核心要点

1. 核心问题：大语言模型联邦学习中，单个块参数多，通信延迟高，资源受限客户端负担重
2. 方法要点：建立通信与计算并行线程，提升通信效率，理论收敛率与标准方法相同
3. 实验或效果：在指令跟随和数学推理任务上验证，保持性能同时显著提高通信效率

## 📄 摘要（原文）

> Federated learning (FL) has been extensively studied as a privacy-preserving training paradigm. Recently, federated block coordinate descent scheme has become a popular option in training large-scale models, as it allows clients to train only a subset of the model locally instead of the entire model. However, in the era of large language models (LLMs), even a single block can contain a significant number of parameters, posing substantial communication latency, particularly for resource-constrained clients. To address this challenge in federated training/fine-tuning LLMs, we propose ParaBlock, a novel approach that establishes two parallel threads for communication and computation to enhance communication efficiency. We theoretically prove that the proposed ParaBlock achieves the same convergence rate as the standard federated block coordinate descent methods. Empirical evaluations on fine-tuning LLMs on general instruction following and mathematical reasoning confirm that ParaBlock not only maintains strong performance but also significantly improves communication efficiency.

