---
layout: default
title: DRL-Based Injection Molding Process Parameter Optimization for Adaptive and Profitable Production
---

# DRL-Based Injection Molding Process Parameter Optimization for Adaptive and Profitable Production

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.10988" class="toolbar-btn" target="_blank">📄 arXiv: 2505.10988v1</a>
  <a href="https://arxiv.org/pdf/2505.10988.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.10988v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.10988v1', 'DRL-Based Injection Molding Process Parameter Optimization for Adaptive and Profitable Production')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Joon-Young Kim, Jecheon Yu, Heekyu Kim, Seunghwa Ryu

**分类**: cs.AI, eess.SY

**发布日期**: 2025-05-16

**备注**: 50 pages, 10 figures

---

## 💡 一句话要点

**提出基于深度强化学习的注塑工艺参数优化方法以提升生产效益**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `深度强化学习` `注塑工艺` `参数优化` `实时优化` `制造业` `智能决策` `经济性能`

## 📋 核心要点

1. 现有注塑工艺优化方法难以在动态环境中平衡产品质量与盈利能力，面临挑战。
2. 论文提出基于深度强化学习的框架，通过利润函数和代理模型实现实时工艺优化。
3. 实验结果显示，该框架在保持产品质量的同时，最大化利润，并显著提高推理速度。

## 📝 摘要（中文）

塑料注射成型在现代制造中至关重要，但在动态环境和经济条件下优化工艺参数以平衡产品质量和盈利能力仍然是一个持续的挑战。本研究提出了一种新颖的基于深度强化学习（DRL）的实时工艺优化框架，将产品质量和盈利能力整合到控制目标中。开发了一个利润函数，以反映现实制造成本，包括树脂、模具磨损和电力价格的时段变化。构建了代理模型以预测产品质量和周期时间，使得DRL代理能够高效离线训练。实验结果表明，该DRL框架能够动态适应季节性和操作变化，持续保持产品质量并最大化利润。与传统的优化方法相比，DRL模型在经济性能上表现相当，推理速度提高了135倍，适合实时应用。

## 🔬 方法详解

**问题定义**：本论文旨在解决塑料注射成型过程中工艺参数优化的问题，现有方法在动态环境下难以有效平衡产品质量与盈利能力，导致生产效率低下。

**核心思路**：提出了一种基于深度强化学习的框架，通过实时优化工艺参数，整合产品质量和盈利能力作为控制目标，从而实现智能化的生产决策。

**技术框架**：整体架构包括利润函数的构建、代理模型的训练以及基于软演员-评论家（SAC）和近端策略优化（PPO）算法的DRL代理。框架分为离线训练和实时优化两个阶段。

**关键创新**：最重要的创新点在于将利润函数与产品质量预测相结合，形成了一个动态适应的优化框架，显著提升了传统优化方法的实时性和适应性。

**关键设计**：关键参数设置包括利润函数的设计，代理模型的构建，以及使用SAC和PPO算法进行高效训练，确保了模型在不同环境下的稳定性和准确性。

## 📊 实验亮点

实验结果表明，所提出的DRL框架在动态适应性方面表现优异，能够在保持产品质量的同时最大化利润。与传统遗传算法相比，DRL模型在经济性能上表现相当，推理速度提高了135倍，适合实时应用。

## 🎯 应用场景

该研究的潜在应用领域包括现代制造业中的注塑工艺优化，尤其是在需要快速响应市场变化的生产环境中。通过实现智能化的工艺参数调整，该框架能够有效降低生产成本，提高产品质量，具有显著的实际价值和未来影响。

## 📄 摘要（原文）

> Plastic injection molding remains essential to modern manufacturing. However, optimizing process parameters to balance product quality and profitability under dynamic environmental and economic conditions remains a persistent challenge. This study presents a novel deep reinforcement learning (DRL)-based framework for real-time process optimization in injection molding, integrating product quality and profitability into the control objective. A profit function was developed to reflect real-world manufacturing costs, incorporating resin, mold wear, and electricity prices, including time-of-use variations. Surrogate models were constructed to predict product quality and cycle time, enabling efficient offline training of DRL agents using soft actor-critic (SAC) and proximal policy optimization (PPO) algorithms. Experimental results demonstrate that the proposed DRL framework can dynamically adapt to seasonal and operational variations, consistently maintaining product quality while maximizing profit. Compared to traditional optimization methods such as genetic algorithms, the DRL models achieved comparable economic performance with up to 135x faster inference speeds, making them well-suited for real-time applications. The framework's scalability and adaptability highlight its potential as a foundation for intelligent, data-driven decision-making in modern manufacturing environments.

