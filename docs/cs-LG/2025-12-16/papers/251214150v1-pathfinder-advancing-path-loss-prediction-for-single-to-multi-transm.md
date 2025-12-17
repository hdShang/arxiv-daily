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

**提出PathFinder架构，通过主动环境建模和注意力机制解决单到多发射器场景下的路径损耗预测问题。**

🎯 **匹配领域**: **强化学习**

**关键词**: `路径损耗预测` `主动环境建模` `多发射器场景` `解耦特征编码` `掩码引导注意力` `分布偏移` `5G网络优化` `深度学习`

## 📋 核心要点

1. 现有方法被动建模环境，忽视发射器和关键特征，导致预测不准确。
2. PathFinder通过解耦编码和掩码引导注意力，主动建模建筑物和发射器，提升多场景适应性。
3. 实验显示PathFinder在S2MT-RPP基准上显著优于现有方法，尤其在多发射器测试中表现突出。

## 📝 摘要（中文）

无线电路径损耗预测（RPP）对于优化5G网络和实现物联网、智慧城市等应用至关重要。然而，当前基于深度学习的RPP方法存在三个主要问题：缺乏主动环境建模，难以处理现实中的多发射器场景，以及在分布偏移下泛化能力差，特别是当训练和测试环境在建筑密度或发射器配置上不同时。本文提出了PathFinder，一种新颖的架构，通过解耦特征编码主动建模建筑物和发射器，并集成掩码引导的低秩注意力机制，独立关注接收器和建筑区域。此外，还引入了面向发射器的混合策略进行鲁棒训练，并创建了一个新的基准——单到多发射器RPP（S2MT-RPP），专门用于评估外推性能（在单发射器训练后进行多发射器测试）。实验结果表明，PathFinder在性能上显著优于现有最先进方法，尤其是在具有挑战性的多发射器场景中。我们的代码和项目网站可在https://emorzz1g.github.io/PathFinder/获取。

## 🔬 方法详解

PathFinder的整体框架基于深度神经网络，核心创新点包括解耦特征编码，将建筑物和发射器信息分离处理，以及掩码引导的低秩注意力机制，该机制独立聚焦于接收器和建筑区域，避免信息混淆。与现有方法的主要区别在于主动环境建模，而非被动依赖数据，同时通过面向发射器的混合策略增强训练鲁棒性，专门针对单到多发射器场景设计，解决了分布偏移问题。

## 📊 实验亮点

PathFinder在单到多发射器RPP基准测试中表现优异，相比现有方法，在多发射器场景下的预测精度显著提升，验证了其在外推任务中的强大泛化能力。

## 🎯 应用场景

该研究可应用于5G网络优化、物联网部署和智慧城市建设，通过准确预测路径损耗，帮助规划基站布局、提升信号覆盖和网络效率，支持大规模无线通信系统的智能管理。

## 📄 摘要（原文）

> Radio path loss prediction (RPP) is critical for optimizing 5G networks and enabling IoT, smart city, and similar applications. However, current deep learning-based RPP methods lack proactive environmental modeling, struggle with realistic multi-transmitter scenarios, and generalize poorly under distribution shifts, particularly when training/testing environments differ in building density or transmitter configurations. This paper identifies three key issues: (1) passive environmental modeling that overlooks transmitters and key environmental features; (2) overemphasis on single-transmitter scenarios despite real-world multi-transmitter prevalence; (3) excessive focus on in-distribution performance while neglecting distribution shift challenges. To address these, we propose PathFinder, a novel architecture that actively models buildings and transmitters via disentangled feature encoding and integrates Mask-Guided Low-rank Attention to independently focus on receiver and building regions. We also introduce a Transmitter-Oriented Mixup strategy for robust training and a new benchmark, single-to-multi-transmitter RPP (S2MT-RPP), tailored to evaluate extrapolation performance (multi-transmitter testing after single-transmitter training). Experimental results show PathFinder outperforms state-of-the-art methods significantly, especially in challenging multi-transmitter scenarios. Our code and project site are available at: https://emorzz1g.github.io/PathFinder/.

