---
layout: default
title: "MAGIC-MASK: Multi-Agent Guided Inter-Agent Collaboration with Mask-Based Explainability for Reinforcement Learning"
---

# MAGIC-MASK: Multi-Agent Guided Inter-Agent Collaboration with Mask-Based Explainability for Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.00274" class="toolbar-btn" target="_blank">📄 arXiv: 2510.00274v1</a>
  <a href="https://arxiv.org/pdf/2510.00274.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00274v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.00274v1', 'MAGIC-MASK: Multi-Agent Guided Inter-Agent Collaboration with Mask-Based Explainability for Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Maisha Maliha, Dean Hougen

**分类**: cs.AI, cs.LG, cs.MA

**发布日期**: 2025-09-30

**备注**: 16 pages, 3 figures

---

## 💡 一句话要点

**MAGIC-MASK：基于掩码可解释性的多智能体强化学习协作框架**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多智能体强化学习` `可解释性` `掩码学习` `智能体协作` `近端策略优化`

## 📋 核心要点

1. 现有深度强化学习解释性方法计算成本高昂，探索覆盖不足，且难以适应多智能体环境。
2. MAGIC-MASK通过智能体间协作，共享掩码状态信息和经验，实现显著性引导的掩码操作和奖励信息共享。
3. 实验表明，MAGIC-MASK在保真度、学习效率和策略鲁棒性方面优于现有方法，并提供可解释的解释。

## 📝 摘要（中文）

深度强化学习智能体的决策过程理解是部署于安全关键和多智能体环境中的关键挑战。现有解释性方法（如StateMask）在识别关键状态方面有所进展，但仍受限于计算成本、探索覆盖率以及缺乏对多智能体环境的适应性。为克服这些限制，我们提出了MAGIC-MASK，一个基于数学的框架，将基于扰动的解释扩展到多智能体强化学习。该方法集成了近端策略优化、自适应epsilon-greedy探索和轻量级智能体间协作，以共享掩码状态信息和经验。这种协作使每个智能体能够执行显著性引导的掩码操作，并与同伴共享基于奖励的见解，从而减少关键状态发现所需的时间，提高解释保真度，并实现更快、更稳健的学习。该方法的核心创新在于通过统一的数学形式（基于轨迹扰动、奖励保真度分析和Kullback-Leibler散度正则化）将可解释性从单智能体推广到多智能体系统。该框架产生基于概率建模和多智能体马尔可夫决策过程的局部、可解释的解释。我们在单智能体和多智能体基准测试（包括多智能体高速公路驾驶环境和Google Research Football）上验证了该框架，表明MAGIC-MASK在保真度、学习效率和策略鲁棒性方面始终优于最先进的基线，同时提供可解释和可转移的解释。

## 🔬 方法详解

**问题定义**：现有深度强化学习方法在多智能体环境下的可解释性不足，难以理解智能体的决策过程，尤其是在安全关键场景下。StateMask等方法计算成本高，探索范围有限，且缺乏对多智能体协作的有效支持。因此，如何高效、准确地解释多智能体强化学习模型的决策过程是一个关键问题。

**核心思路**：MAGIC-MASK的核心思路是通过智能体之间的协作来提高可解释性和学习效率。每个智能体通过学习一个掩码来识别关键状态，并将这些信息与其他智能体共享。这种协作使得智能体能够更快地发现关键状态，并提高解释的保真度。此外，该方法还利用奖励信息来指导智能体间的协作，从而提高学习效率和策略鲁棒性。

**技术框架**：MAGIC-MASK框架主要包含以下几个模块：1) 基于近端策略优化（PPO）的强化学习算法；2) 自适应epsilon-greedy探索策略，用于平衡探索和利用；3) 轻量级的智能体间协作机制，用于共享掩码状态信息和经验；4) 基于轨迹扰动和奖励保真度分析的可解释性模块，用于生成局部、可解释的解释。整体流程是，每个智能体首先独立学习策略，然后通过协作机制共享信息，并利用可解释性模块生成解释。

**关键创新**：MAGIC-MASK的关键创新在于将可解释性从单智能体系统推广到多智能体系统。它通过统一的数学形式，将轨迹扰动、奖励保真度分析和Kullback-Leibler散度正则化结合起来，从而实现对多智能体决策过程的解释。与现有方法相比，MAGIC-MASK能够更有效地利用智能体间的协作，提高解释的保真度和学习效率。

**关键设计**：在epsilon-greedy探索中，epsilon的值会根据学习进度自适应调整。掩码的设计采用可学习的参数，并通过损失函数来优化，损失函数包括奖励保真度损失和KL散度正则化项。奖励保真度损失用于确保掩码能够保留对奖励影响最大的状态特征，KL散度正则化项用于约束掩码的复杂性，避免过拟合。

## 📊 实验亮点

MAGIC-MASK在多智能体高速公路驾驶环境和Google Research Football等基准测试中表现出色，在保真度、学习效率和策略鲁棒性方面均优于现有方法。例如，在多智能体高速公路驾驶环境中，MAGIC-MASK能够更快地学习到安全驾驶策略，并提供对车辆决策行为的清晰解释。实验结果表明，MAGIC-MASK能够有效地提高多智能体强化学习系统的性能和可解释性。

## 🎯 应用场景

MAGIC-MASK可应用于自动驾驶、机器人协作、博弈游戏等领域。在自动驾驶中，可以解释车辆的决策行为，提高安全性。在机器人协作中，可以帮助理解机器人之间的交互，优化协作策略。在博弈游戏中，可以分析对手的行为模式，制定更有效的策略。该研究有助于提高人工智能系统的透明度和可信度，促进其在实际场景中的应用。

## 📄 摘要（原文）

> Understanding the decision-making process of Deep Reinforcement Learning agents remains a key challenge for deploying these systems in safety-critical and multi-agent environments. While prior explainability methods like StateMask, have advanced the identification of critical states, they remain limited by computational cost, exploration coverage, and lack of adaptation to multi-agent settings. To overcome these limitations, we propose a mathematically grounded framework, MAGIC-MASK (Multi-Agent Guided Inter-agent Collaboration with Mask-Based Explainability for Reinforcement Learning), that extends perturbation-based explanation to Multi-Agent Reinforcement Learning. Our method integrates Proximal Policy Optimization, adaptive epsilon-greedy exploration, and lightweight inter-agent collaboration to share masked state information and peer experience. This collaboration enables each agent to perform saliency-guided masking and share reward-based insights with peers, reducing the time required for critical state discovery, improving explanation fidelity, and leading to faster and more robust learning. The core novelty of our approach lies in generalizing explainability from single-agent to multi-agent systems through a unified mathematical formalism built on trajectory perturbation, reward fidelity analysis, and Kullback-Leibler divergence regularization. This framework yields localized, interpretable explanations grounded in probabilistic modeling and multi-agent Markov decision processes. We validate our framework on both single-agent and multi-agent benchmarks, including a multi-agent highway driving environment and Google Research Football, demonstrating that MAGIC-MASK consistently outperforms state-of-the-art baselines in fidelity, learning efficiency, and policy robustness while offering interpretable and transferable explanations.

