---
layout: default
title: AXIOM: Learning to Play Games in Minutes with Expanding Object-Centric Models
---

# AXIOM: Learning to Play Games in Minutes with Expanding Object-Centric Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24784" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24784v1</a>
  <a href="https://arxiv.org/pdf/2505.24784.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24784v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24784v1', 'AXIOM: Learning to Play Games in Minutes with Expanding Object-Centric Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Conor Heins, Toon Van de Maele, Alexander Tschantz, Hampus Linander, Dimitrije Markovic, Tommaso Salvatori, Corrado Pezzato, Ozan Catal, Ran Wei, Magnus Koudahl, Marco Perin, Karl Friston, Tim Verbelen, Christopher Buckley

**分类**: cs.AI, cs.LG, stat.ML

**发布日期**: 2025-05-30

**备注**: 10 pages main text, 4 figures, 2 tables; 25 pages supplementary material, 8 figures

---

## 💡 一句话要点

**提出AXIOM以解决深度强化学习的数据效率问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `深度强化学习` `主动推理` `物体中心模型` `数据效率` `游戏AI` `贝叶斯方法` `在线学习`

## 📋 核心要点

1. 现有深度强化学习方法在数据效率上无法与人类学习相提并论，尤其是在物体交互的理解上存在不足。
2. 本文提出AXIOM架构，通过整合物体中心的动态和交互先验知识，提升低数据环境下的学习效率。
3. AXIOM在10,000次交互步骤内成功掌握多种游戏，展现出较少的参数需求和较低的计算成本。

## 📝 摘要（中文）

当前的深度强化学习（DRL）方法在多个领域取得了最先进的性能，但在数据效率方面相较于人类学习仍显不足。主动推理提供了一个将感知信息与先验知识结合的框架，以学习世界模型并量化自身信念和预测的不确定性。然而，主动推理模型通常针对单一任务设计，缺乏DRL方法的领域灵活性。为此，本文提出了一种新架构AXIOM，整合了关于物体中心动态和交互的核心先验知识，以加速低数据环境下的学习。AXIOM在仅需10,000次交互步骤内掌握多种游戏，且参数数量较少，避免了基于梯度优化的计算开销。

## 🔬 方法详解

**问题定义**：本文旨在解决深度强化学习在数据效率和领域灵活性方面的不足，现有方法通常依赖大量数据进行训练，难以快速适应新任务。

**核心思路**：AXIOM通过整合关于物体交互的核心先验知识，构建物体中心的动态模型，从而在低数据环境中加速学习过程。这样的设计使得模型能够在较少的交互中快速掌握任务。

**技术框架**：AXIOM的整体架构包括物体表示、动态建模和在线扩展模块。物体表示将场景视为物体的组合，动态建模则采用分段线性轨迹来捕捉稀疏的物体间交互，在线扩展模块通过从单一事件学习混合模型并进行贝叶斯模型简化来增强模型的泛化能力。

**关键创新**：AXIOM的主要创新在于其将主动推理与深度强化学习相结合，既保持了贝叶斯方法的数据效率和可解释性，又实现了跨任务的泛化能力。这一设计使得AXIOM在处理新任务时表现出色。

**关键设计**：AXIOM的设计中采用了较少的参数设置，避免了复杂的梯度优化过程，利用贝叶斯模型简化技术定期优化模型结构，以提高学习效率和泛化能力。具体的损失函数和网络结构细节在论文中有详细描述。

## 📊 实验亮点

AXIOM在仅10,000次交互步骤内成功掌握多种游戏，相较于传统深度强化学习方法，其参数数量显著减少，并且避免了梯度优化的高计算开销。这一结果表明AXIOM在数据效率和学习速度上具有明显优势。

## 🎯 应用场景

AXIOM的研究成果具有广泛的应用潜力，尤其是在需要快速适应新环境和任务的领域，如机器人控制、游戏AI和智能代理等。其高效的数据利用率和灵活的模型结构使其在实际应用中能够显著降低训练成本，提高响应速度，未来可能推动更多智能系统的开发与应用。

## 📄 摘要（原文）

> Current deep reinforcement learning (DRL) approaches achieve state-of-the-art performance in various domains, but struggle with data efficiency compared to human learning, which leverages core priors about objects and their interactions. Active inference offers a principled framework for integrating sensory information with prior knowledge to learn a world model and quantify the uncertainty of its own beliefs and predictions. However, active inference models are usually crafted for a single task with bespoke knowledge, so they lack the domain flexibility typical of DRL approaches. To bridge this gap, we propose a novel architecture that integrates a minimal yet expressive set of core priors about object-centric dynamics and interactions to accelerate learning in low-data regimes. The resulting approach, which we call AXIOM, combines the usual data efficiency and interpretability of Bayesian approaches with the across-task generalization usually associated with DRL. AXIOM represents scenes as compositions of objects, whose dynamics are modeled as piecewise linear trajectories that capture sparse object-object interactions. The structure of the generative model is expanded online by growing and learning mixture models from single events and periodically refined through Bayesian model reduction to induce generalization. AXIOM masters various games within only 10,000 interaction steps, with both a small number of parameters compared to DRL, and without the computational expense of gradient-based optimization.

