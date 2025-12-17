---
layout: default
title: Robust and Generalizable GNN Fine-Tuning via Uncertainty-aware Adapter Learning
---

# Robust and Generalizable GNN Fine-Tuning via Uncertainty-aware Adapter Learning

**arXiv**: [2511.18859v1](https://arxiv.org/abs/2511.18859) | [PDF](https://arxiv.org/pdf/2511.18859.pdf)

**作者**: Bo Jiang, Weijun Zhao, Beibei Wang, Xiao Wang, Jin Tang

---

## 💡 一句话要点

**提出不确定性感知适配器以增强图神经网络在噪声数据下的鲁棒性和泛化能力**

**关键词**: `图神经网络微调` `不确定性学习` `适配器模块` `噪声鲁棒性` `高斯概率模型` `泛化能力`

## 📋 核心要点

1. 图数据在微调中易受噪声影响，现有适配器方法鲁棒性和泛化性不足
2. 引入高斯概率适配器，通过方差变化自动吸收噪声，提升模型适应性
3. 多基准实验验证方法在噪声图数据下的有效性、鲁棒性和高泛化能力

## 📄 摘要（原文）

> Recently, fine-tuning large-scale pre-trained GNNs has yielded remarkable attention in adapting pre-trained GNN models for downstream graph learning tasks. One representative fine-tuning method is to exploit adapter (termed AdapterGNN) which aims to 'augment' the pre-trained model by inserting a lightweight module to make the 'augmented' model better adapt to the downstream tasks. However, graph data may contain various types of noise in downstream tasks, such as noisy edges and ambiguous node attributes. Existing AdapterGNNs are often prone to graph noise and exhibit limited generalizability. How to enhance the robustness and generalization ability of GNNs' fine tuning remains an open problem. In this paper, we show that the above problem can be well addressed by integrating uncertainty learning into the GNN adapter. We propose the Uncertainty-aware Adapter (UAdapterGNN) that fortifies pre-trained GNN models against noisy graph data in the fine-tuning process. Specifically, in contrast to regular AdapterGNN, our UAdapterGNN exploits Gaussian probabilistic adapter to augment the pre-trained GNN model. In this way, when the graph contains various noises,our method can automatically absorb the effects of changes in the variances of the Gaussian distribution, thereby significantly enhancing the model's robustness. Also, UAdapterGNN can further improve the generalization ability of the model on the downstream tasks. Extensive experiments on several benchmarks demonstrate the effectiveness, robustness and high generalization ability of the proposed UAdapterGNN method.

