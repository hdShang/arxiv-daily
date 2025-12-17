---
layout: default
title: Accelerating Wireless Distributed Learning via Hybrid Split and Federated Learning Optimization
---

# Accelerating Wireless Distributed Learning via Hybrid Split and Federated Learning Optimization

**arXiv**: [2511.19851v1](https://arxiv.org/abs/2511.19851) | [PDF](https://arxiv.org/pdf/2511.19851.pdf)

**作者**: Kun Guo, Xuefei Li, Xijun Wang, Howard H. Yang, Wei Feng, Tony Q. S. Quek

---

## 💡 一句话要点

**提出混合分割与联邦学习优化方法以加速无线分布式学习**

**关键词**: `无线分布式学习` `混合学习优化` `延迟最小化` `块坐标下降` `联邦学习` `分割学习`

## 📋 核心要点

1. 核心问题：学习模式选择和批大小如何影响无线分布式学习性能与延迟
2. 方法要点：使用块坐标下降和舍入算法联合优化学习模式、批大小及资源分配
3. 实验或效果：实验显示该方法显著加速收敛至目标精度，优于现有方法

## 📄 摘要（原文）

> Federated learning (FL) and split learning (SL) are two effective distributed learning paradigms in wireless networks, enabling collaborative model training across mobile devices without sharing raw data. While FL supports low-latency parallel training, it may converge to less accurate model. In contrast, SL achieves higher accuracy through sequential training but suffers from increased delay. To leverage the advantages of both, hybrid split and federated learning (HSFL) allows some devices to operate in FL mode and others in SL mode. This paper aims to accelerate HSFL by addressing three key questions: 1) How does learning mode selection affect overall learning performance? 2) How does it interact with batch size? 3) How can these hyperparameters be jointly optimized alongside communication and computational resources to reduce overall learning delay? We first analyze convergence, revealing the interplay between learning mode and batch size. Next, we formulate a delay minimization problem and propose a two-stage solution: a block coordinate descent method for a relaxed problem to obtain a locally optimal solution, followed by a rounding algorithm to recover integer batch sizes with near-optimal performance. Experimental results demonstrate that our approach significantly accelerates convergence to the target accuracy compared to existing methods.

