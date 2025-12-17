---
layout: default
title: AEBNAS: Strengthening Exit Branches in Early-Exit Networks through Hardware-Aware Neural Architecture Search
---

# AEBNAS: Strengthening Exit Branches in Early-Exit Networks through Hardware-Aware Neural Architecture Search

**arXiv**: [2512.10671v1](https://arxiv.org/abs/2512.10671) | [PDF](https://arxiv.org/pdf/2512.10671.pdf)

**作者**: Oscar Robben, Saeed Khalilian, Nirvana Meratnia

---

## 💡 一句话要点

**提出AEBNAS，通过硬件感知神经架构搜索增强早期退出网络中的退出分支，以优化资源受限设备上的能效与精度。**

**关键词**: `早期退出网络` `神经架构搜索` `硬件感知优化` `能效计算` `自适应阈值` `资源受限设备`

## 📋 核心要点

1. 早期退出网络设计需平衡效率与性能，但手动优化退出分支深度与层类型耗时且困难。
2. 采用硬件感知NAS自动搜索退出分支的最佳深度与层类型，结合自适应阈值调整优化精度与能效。
3. 在CIFAR-10、CIFAR-100和SVHN数据集上验证，相比现有方法，在相同或更低MACs下实现更高精度。

## 📄 摘要（原文）

> Early-exit networks are effective solutions for reducing the overall energy consumption and latency of deep learning models by adjusting computation based on the complexity of input data. By incorporating intermediate exit branches into the architecture, they provide less computation for simpler samples, which is particularly beneficial for resource-constrained devices where energy consumption is crucial. However, designing early-exit networks is a challenging and time-consuming process due to the need to balance efficiency and performance. Recent works have utilized Neural Architecture Search (NAS) to design more efficient early-exit networks, aiming to reduce average latency while improving model accuracy by determining the best positions and number of exit branches in the architecture. Another important factor affecting the efficiency and accuracy of early-exit networks is the depth and types of layers in the exit branches. In this paper, we use hardware-aware NAS to strengthen exit branches, considering both accuracy and efficiency during optimization. Our performance evaluation on the CIFAR-10, CIFAR-100, and SVHN datasets demonstrates that our proposed framework, which considers varying depths and layers for exit branches along with adaptive threshold tuning, designs early-exit networks that achieve higher accuracy with the same or lower average number of MACs compared to the state-of-the-art approaches.

