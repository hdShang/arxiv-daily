---
layout: default
title: MMA: A Momentum Mamba Architecture for Human Activity Recognition with Inertial Sensors
---

# MMA: A Momentum Mamba Architecture for Human Activity Recognition with Inertial Sensors

**arXiv**: [2511.21550v1](https://arxiv.org/abs/2511.21550) | [PDF](https://arxiv.org/pdf/2511.21550.pdf)

**作者**: Thai-Khanh Nguyen, Uyen Vo, Tan M. Nguyen, Thieu N. Vo, Trung-Hieu Le, Cuong Pham

---

## 💡 一句话要点

**提出动量增强状态空间模型以改进惯性传感器人体活动识别**

**关键词**: `人体活动识别` `状态空间模型` `动量机制` `惯性传感器` `长序列建模` `深度学习`

## 📋 核心要点

1. 传统深度模型在长序列建模中存在梯度问题和计算成本高
2. 引入动量机制增强状态空间模型，提升稳定性和长程依赖捕捉
3. 在多个基准测试中实现精度、鲁棒性和收敛速度的显著提升

## 📄 摘要（原文）

> Human activity recognition (HAR) from inertial sensors is essential for ubiquitous computing, mobile health, and ambient intelligence. Conventional deep models such as Convolutional Neural Networks (CNNs), Recurrent Neural Networks (RNNs), and transformers have advanced HAR but remain limited by vanishing or exloding gradients, high computational cost, and difficulty in capturing long-range dependencies. Structured state-space models (SSMs) like Mamba address these challenges with linear complexity and effective temporal modeling, yet they are restricted to first-order dynamics without stable longterm memory mechanisms. We introduce Momentum Mamba, a momentum-augmented SSM that incorporates second-order dynamics to improve stability of information flow across time steps, robustness, and long-sequence modeling. Two extensions further expand its capacity: Complex Momentum Mamba for frequency-selective memory scaling. Experiments on multiple HAR benchmarks demonstrate consistent gains over vanilla Mamba and Transformer baselines in accuracy, robustness, and convergence speed. With only moderate increases in training cost, momentum-augmented SSMs offer a favorable accuracy-efficiency balance, establishing them as a scalable paradigm for HAR and a promising principal framework for broader sequence modeling applications.

