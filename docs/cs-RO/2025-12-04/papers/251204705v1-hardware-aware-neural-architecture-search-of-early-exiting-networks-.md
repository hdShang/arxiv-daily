---
layout: default
title: Hardware-aware Neural Architecture Search of Early Exiting Networks on Edge Accelerators
---

# Hardware-aware Neural Architecture Search of Early Exiting Networks on Edge Accelerators

**arXiv**: [2512.04705v1](https://arxiv.org/abs/2512.04705) | [PDF](https://arxiv.org/pdf/2512.04705.pdf)

**作者**: Alaa Zniber, Arne Symons, Ouassim Karrakchou, Marian Verhelst, Mounir Ghogho

---

## 💡 一句话要点

**提出硬件感知神经架构搜索框架，优化边缘加速器上的早期退出网络设计**

**关键词**: `神经架构搜索` `早期退出网络` `边缘计算` `硬件感知优化` `量化感知训练`

## 📋 核心要点

1. 核心问题：边缘部署中，早期退出网络受硬件异构性和量化约束影响，自动优化研究不足
2. 方法要点：集成量化和硬件资源分配，系统搜索网络骨干中的早期退出点位置
3. 实验或效果：在CIFAR-10数据集上，发现架构可减少超50%计算成本，提升边缘环境适应性

## 📄 摘要（原文）

> Advancements in high-performance computing and cloud technologies have enabled the development of increasingly sophisticated Deep Learning (DL) models. However, the growing demand for embedded intelligence at the edge imposes stringent computational and energy constraints, challenging the deployment of these large-scale models. Early Exiting Neural Networks (EENN) have emerged as a promising solution, allowing dynamic termination of inference based on input complexity to enhance efficiency. Despite their potential, EENN performance is highly influenced by the heterogeneity of edge accelerators and the constraints imposed by quantization, affecting accuracy, energy efficiency, and latency. Yet, research on the automatic optimization of EENN design for edge hardware remains limited. To bridge this gap, we propose a hardware-aware Neural Architecture Search (NAS) framework that systematically integrates the effects of quantization and hardware resource allocation to optimize the placement of early exit points within a network backbone. Experimental results on the CIFAR-10 dataset demonstrate that our NAS framework can discover architectures that achieve over a 50\% reduction in computational costs compared to conventional static networks, making them more suitable for deployment in resource-constrained edge environments.

