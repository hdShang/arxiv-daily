---
layout: default
title: CogniSNN: Enabling Neuron-Expandability, Pathway-Reusability, and Dynamic-Configurability with Random Graph Architectures in Spiking Neural Networks
---

# CogniSNN: Enabling Neuron-Expandability, Pathway-Reusability, and Dynamic-Configurability with Random Graph Architectures in Spiking Neural Networks

**arXiv**: [2512.11743v1](https://arxiv.org/abs/2512.11743) | [PDF](https://arxiv.org/pdf/2512.11743.pdf)

**作者**: Yongsheng Huang, Peibo Duan, Yujie Wu, Kai Sun, Zhipeng Liu, Changsheng Zhang, Bin Zhang, Mingkun Xu

---

## 💡 一句话要点

**提出CogniSNN，通过随机图架构实现神经元可扩展性、通路可重用性和动态可配置性，以提升脉冲神经网络性能。**

**关键词**: `脉冲神经网络` `随机图架构` `通路可重用性` `动态增长学习` `神经形态计算`

## 📋 核心要点

1. 问题：主流SNN采用链式架构，忽略大脑随机连接特性，导致性能受限。
2. 方法：引入随机图架构、改进残差机制、自适应池化、KP-LwF和DGL算法。
3. 效果：在神经形态数据集和Tiny-ImageNet上达到或超越先进SNN，增强连续学习和鲁棒性。

## 📄 摘要（原文）

> Spiking neural networks (SNNs), regarded as the third generation of artificial neural networks, are expected to bridge the gap between artificial intelligence and computational neuroscience. However, most mainstream SNN research directly adopts the rigid, chain-like hierarchical architecture of traditional artificial neural networks (ANNs), ignoring key structural characteristics of the brain. Biological neurons are stochastically interconnected, forming complex neural pathways that exhibit Neuron-Expandability, Pathway-Reusability, and Dynamic-Configurability. In this paper, we introduce a new SNN paradigm, named Cognition-aware SNN (CogniSNN), by incorporating Random Graph Architecture (RGA). Furthermore, we address the issues of network degradation and dimensional mismatch in deep pathways by introducing an improved pure spiking residual mechanism alongside an adaptive pooling strategy. Then, we design a Key Pathway-based Learning without Forgetting (KP-LwF) approach, which selectively reuses critical neural pathways while retaining historical knowledge, enabling efficient multi-task transfer. Finally, we propose a Dynamic Growth Learning (DGL) algorithm that allows neurons and synapses to grow dynamically along the internal temporal dimension. Extensive experiments demonstrate that CogniSNN achieves performance comparable to, or even surpassing, current state-of-the-art SNNs on neuromorphic datasets and Tiny-ImageNet. The Pathway-Reusability enhances the network's continuous learning capability across different scenarios, while the dynamic growth algorithm improves robustness against interference and mitigates the fixed-timestep constraints during neuromorphic chip deployment. This work demonstrates the potential of SNNs with random graph structures in advancing brain-inspired intelligence and lays the foundation for their practical application on neuromorphic hardware.

