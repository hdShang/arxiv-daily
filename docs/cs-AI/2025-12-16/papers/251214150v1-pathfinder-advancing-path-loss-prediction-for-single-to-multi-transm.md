---
layout: default
title: PathFinder: Advancing Path Loss Prediction for Single-to-Multi-Transmitter Scenario
---

# PathFinder: Advancing Path Loss Prediction for Single-to-Multi-Transmitter Scenario

**arXiv**: [2512.14150v1](https://arxiv.org/abs/2512.14150) | [PDF](https://arxiv.org/pdf/2512.14150.pdf)

**作者**: Zhijie Zhong, Zhiwen Yu, Pengyu Li, Jianming Lv, C. L. Philip Chen, Min Chen

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-16

**备注**: 34 pages, 14 figures, 4 tables. Under review

**🔗 代码/项目**: [PROJECT_PAGE](https://emorzz1g.github.io/PathFinder/)

---

## 💡 一句话要点

**提出PathFinder架构，通过主动环境建模和注意力机制解决单发射器到多发射器场景下的路径损耗预测问题。**

**关键词**: `路径损耗预测` `多发射器场景` `主动环境建模` `注意力机制` `分布偏移` `5G网络优化` `深度学习`

## 📋 核心要点

1. 现有方法被动建模环境，忽视发射器和关键特征，导致预测不准确。
2. PathFinder通过解耦编码和掩码引导注意力主动建模环境，提升多发射器场景适应性。
3. 在S2MT-RPP基准上，PathFinder显著优于现有方法，尤其在多发射器测试中表现突出。

## 📝 摘要（中文）

无线电路径损耗预测（RPP）对于优化5G网络和实现物联网、智慧城市等应用至关重要。然而，当前基于深度学习的RPP方法存在三个主要问题：缺乏主动环境建模、难以处理真实多发射器场景、在分布偏移下泛化能力差。本文提出PathFinder架构，通过解耦特征编码主动建模建筑物和发射器，并集成掩码引导低秩注意力机制独立关注接收器和建筑物区域。此外，引入面向发射器的混合策略进行鲁棒训练，并创建单到多发射器RPP（S2MT-RPP）基准来评估外推性能。实验结果表明，PathFinder在挑战性多发射器场景中显著优于现有方法。代码和项目网站已公开。

## 🔬 方法详解

PathFinder整体框架基于深度神经网络，核心创新包括解耦特征编码和掩码引导低秩注意力机制。解耦编码主动分离建筑物和发射器特征，增强环境建模能力；注意力机制独立处理接收器和建筑物区域，优化信息聚焦。与现有方法相比，PathFinder强调主动建模而非被动学习，并引入面向发射器的混合策略提升鲁棒性，专门针对单到多发射器场景设计，解决了分布偏移挑战。

## 📊 实验亮点

PathFinder在单到多发射器RPP基准测试中表现优异，相比现有方法显著提升预测精度，特别是在多发射器场景下，验证了其主动建模和注意力机制的有效性。

## 🎯 应用场景

该研究可应用于5G网络优化、物联网部署和智慧城市建设，通过精准路径损耗预测提升无线通信效率，支持多发射器环境下的网络规划和资源分配，具有实际工程价值。

## 📄 摘要（原文）

> Radio path loss prediction (RPP) is critical for optimizing 5G networks and enabling IoT, smart city, and similar applications. However, current deep learning-based RPP methods lack proactive environmental modeling, struggle with realistic multi-transmitter scenarios, and generalize poorly under distribution shifts, particularly when training/testing environments differ in building density or transmitter configurations. This paper identifies three key issues: (1) passive environmental modeling that overlooks transmitters and key environmental features; (2) overemphasis on single-transmitter scenarios despite real-world multi-transmitter prevalence; (3) excessive focus on in-distribution performance while neglecting distribution shift challenges. To address these, we propose PathFinder, a novel architecture that actively models buildings and transmitters via disentangled feature encoding and integrates Mask-Guided Low-rank Attention to independently focus on receiver and building regions. We also introduce a Transmitter-Oriented Mixup strategy for robust training and a new benchmark, single-to-multi-transmitter RPP (S2MT-RPP), tailored to evaluate extrapolation performance (multi-transmitter testing after single-transmitter training). Experimental results show PathFinder outperforms state-of-the-art methods significantly, especially in challenging multi-transmitter scenarios. Our code and project site are available at: https://emorzz1g.github.io/PathFinder/.

