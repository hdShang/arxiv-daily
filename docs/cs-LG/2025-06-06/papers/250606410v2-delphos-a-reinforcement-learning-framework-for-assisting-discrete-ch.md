---
layout: default
title: "Delphos: A reinforcement learning framework for assisting discrete choice model specification"
---

# Delphos: A reinforcement learning framework for assisting discrete choice model specification

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06410" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06410v2</a>
  <a href="https://arxiv.org/pdf/2506.06410.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06410v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06410v2', 'Delphos: A reinforcement learning framework for assisting discrete choice model specification')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gabriel Nova, Stephane Hess, Sander van Cranenburgh

**分类**: econ.GN, cs.LG

**发布日期**: 2025-06-06 (更新: 2025-07-25)

**备注**: 13 pages, 7 figures

---

## 💡 一句话要点

**提出Delphos框架以优化离散选择模型的规范过程**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `离散选择模型` `强化学习` `深度Q网络` `模型规范` `序列决策` `马尔可夫决策过程` `自适应探索` `Pareto前沿`

## 📋 核心要点

1. 现有方法将模型规范视为静态优化问题，缺乏动态适应性，难以有效探索复杂的建模空间。
2. Delphos框架将模型规范问题转化为序列决策问题，通过强化学习方法自适应选择建模动作，优化模型候选。
3. 实验结果表明，Delphos能够高效探索大规模建模空间，识别平衡模型拟合与行为合理性的Pareto前沿候选模型。

## 📝 摘要（中文）

我们介绍了Delphos，一个深度强化学习框架，用于辅助离散选择模型的规范过程。与传统方法将模型规范视为静态优化问题不同，Delphos将这一挑战框架化为一个序列决策问题，形式化为马尔可夫决策过程。在这一设置中，代理通过选择一系列建模动作（如选择变量、适应通用和特定替代品的偏好参数、应用非线性变换和包括协变量的交互作用）来学习指定表现良好的模型候选，并与建模环境互动，后者估计每个候选模型并返回奖励信号。Delphos使用深度Q网络，根据建模结果（如对数似然）和行为预期（如参数符号）接收延迟奖励，并在动作序列中分配奖励，以学习哪些建模决策能导致表现良好的候选模型。我们在模拟和实证数据集上评估了Delphos，结果表明代理能够自适应地探索策略，识别表现良好的模型，且无需先前的领域知识。

## 🔬 方法详解

**问题定义**：本论文旨在解决离散选择模型规范过程中的动态适应性不足问题。现有方法通常将模型规范视为静态优化，难以有效应对复杂的建模空间。

**核心思路**：Delphos框架通过将模型规范视为序列决策问题，利用深度强化学习方法，使代理能够自适应地选择建模动作，从而优化模型候选。

**技术框架**：Delphos的整体架构包括一个代理、建模环境和深度Q网络。代理通过选择变量、调整偏好参数等动作与建模环境互动，环境则根据模型表现返回奖励信号。

**关键创新**：Delphos的创新在于将模型规范问题转化为马尔可夫决策过程，允许代理在动态环境中学习，从而有效探索建模空间，识别高性能模型候选。

**关键设计**：Delphos使用深度Q网络接收延迟奖励，奖励信号基于模型的对数似然和参数符号，设计了适应性的奖励分配机制，以引导代理学习最佳建模决策。具体参数设置和网络结构细节在论文中进行了详细描述。

## 📊 实验亮点

实验结果显示，Delphos在模拟和实证数据集上表现优异，能够有效识别高性能模型候选，且在探索过程中无需先前的领域知识。代理能够集中搜索于高奖励区域，成功定义出平衡模型拟合与行为合理性的Pareto前沿。

## 🎯 应用场景

Delphos框架具有广泛的应用潜力，尤其在经济学、市场研究和社会科学等领域的模型规范中，可以帮助研究人员更高效地构建和优化离散选择模型，提升模型的预测能力和解释性。未来，该框架可能推动更复杂决策过程的建模与分析。

## 📄 摘要（原文）

> We introduce Delphos, a deep reinforcement learning framework for assisting the discrete choice model specification process. Unlike traditional approaches that treat model specification as a static optimisation problem, Delphos represents a paradigm shift: it frames this specification challenge as a sequential decision-making problem, formalised as a Markov Decision Process. In this setting, an agent learns to specify well-performing model candidates by choosing a sequence of modelling actions - such as selecting variables, accommodating both generic and alternative-specific taste parameters, applying non-linear transformations, and including interactions with covariates - and interacting with a modelling environment that estimates each candidate and returns a reward signal. Specifically, Delphos uses a Deep Q-Network that receives delayed rewards based on modelling outcomes (e.g., log-likelihood) and behavioural expectations (e.g., parameter signs), and distributes rewards across the sequence of actions to learn which modelling decisions lead to well-performing candidates. We evaluate Delphos on both simulated and empirical datasets, varying the size of the modelling space and the reward function. To assess the agent's performance in navigating the model space, we analyse the learning curve, the distribution of Q-values, occupancy metrics, and Pareto fronts. Our results show that the agent learns to adaptively explore strategies to identify well-performing models across search spaces, even without prior domain knowledge. It efficiently explores large modelling spaces, concentrates its search in high-reward regions, and suggests candidates that define Pareto frontiers balancing model fit and behavioural plausibility. These findings highlight the potential of this novel adaptive, learning-based framework to assist in the model specification process.

