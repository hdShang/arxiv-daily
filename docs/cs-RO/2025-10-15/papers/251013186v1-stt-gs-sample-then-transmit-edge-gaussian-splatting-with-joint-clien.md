---
layout: default
title: STT-GS: Sample-Then-Transmit Edge Gaussian Splatting with Joint Client Selection and Power Control
---

# STT-GS: Sample-Then-Transmit Edge Gaussian Splatting with Joint Client Selection and Power Control

**arXiv**: [2510.13186v1](https://arxiv.org/abs/2510.13186) | [PDF](https://arxiv.org/pdf/2510.13186.pdf)

**作者**: Zhen Li, Xibin Jin, Guoliang Li, Shuai Wang, Miaowen Wen, Huseyin Arslan, Derrick Wing Kwan Ng, Chengzhong Xu

---

## 💡 一句话要点

**提出STT-GS策略，通过联合客户端选择与功率控制优化边缘高斯泼溅场景重建质量**

**关键词**: `边缘高斯泼溅` `客户端选择` `功率控制` `样本后传输` `特征域聚类` `PAMM算法`

## 📋 核心要点

1. 核心问题：边缘高斯泼溅中，传统资源管理方法不适用于最大化场景重建质量。
2. 方法要点：采用样本后传输策略，结合特征域聚类和PAMM算法优化资源分配。
3. 实验效果：在真实数据集上显著优于基准，实现低采样比下的准确预测和成本平衡。

## 📄 摘要（原文）

> Edge Gaussian splatting (EGS), which aggregates data from distributed clients
> and trains a global GS model at the edge server, is an emerging paradigm for
> scene reconstruction. Unlike traditional edge resource management methods that
> emphasize communication throughput or general-purpose learning performance, EGS
> explicitly aims to maximize the GS qualities, rendering existing approaches
> inapplicable. To address this problem, this paper formulates a novel
> GS-oriented objective function that distinguishes the heterogeneous view
> contributions of different clients. However, evaluating this function in turn
> requires clients' images, leading to a causality dilemma. To this end, this
> paper further proposes a sample-then-transmit EGS (or STT-GS for short)
> strategy, which first samples a subset of images as pilot data from each client
> for loss prediction. Based on the first-stage evaluation, communication
> resources are then prioritized towards more valuable clients. To achieve
> efficient sampling, a feature-domain clustering (FDC) scheme is proposed to
> select the most representative data and pilot transmission time minimization
> (PTTM) is adopted to reduce the pilot overhead.Subsequently, we develop a joint
> client selection and power control (JCSPC) framework to maximize the
> GS-oriented function under communication resource constraints. Despite the
> nonconvexity of the problem, we propose a low-complexity efficient solution
> based on the penalty alternating majorization minimization (PAMM) algorithm.
> Experiments unveil that the proposed scheme significantly outperforms existing
> benchmarks on real-world datasets. It is found that the GS-oriented objective
> can be accurately predicted with low sampling ratios (e.g.,10%), and our method
> achieves an excellent tradeoff between view contributions and communication
> costs.

