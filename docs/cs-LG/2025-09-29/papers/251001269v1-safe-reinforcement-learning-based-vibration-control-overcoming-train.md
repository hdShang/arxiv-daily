---
layout: default
title: "Safe Reinforcement Learning-Based Vibration Control: Overcoming Training Risks with LQR Guidance"
---

# Safe Reinforcement Learning-Based Vibration Control: Overcoming Training Risks with LQR Guidance

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.01269" class="toolbar-btn" target="_blank">📄 arXiv: 2510.01269v1</a>
  <a href="https://arxiv.org/pdf/2510.01269.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.01269v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.01269v1', 'Safe Reinforcement Learning-Based Vibration Control: Overcoming Training Risks with LQR Guidance')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rohan Vitthal Thorat, Juhi Singh, Rajdip Nayek

**分类**: cs.LG, eess.SY, stat.ML

**发布日期**: 2025-09-29

**备注**: Paper accepted for presentation at ICCMS 2025. The submission includes 10 pages and 6 figures

---

## 💡 一句话要点

**提出基于LQR引导的安全强化学习振动控制，解决训练过程中的安全风险。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `振动控制` `安全强化学习` `线性二次调节器` `混合控制` `无模型控制` `结构控制`

## 📋 核心要点

1. 传统振动控制依赖精确系统模型，系统辨识繁琐；直接在真实系统上训练RL控制器存在安全风险。
2. 提出混合控制框架，利用基于随机模型的LQR控制器引导RL控制器，降低训练过程中的探索风险。
3. 实验验证了该方法在振动控制中的有效性，解决了RL训练安全问题，无需精确系统模型。

## 📝 摘要（中文）

外部激励引起的结构振动会带来显著风险，包括人员安全隐患、结构损坏和维护成本增加。传统的基于模型的控制策略，如线性二次调节器（LQR），能有效抑制振动，但依赖于精确的系统模型，需要繁琐的系统辨识。强化学习（RL）方法无需显式结构模型，仅从观测到的结构行为中学习策略，从而避免了系统辨识。然而，为了使RL控制器真正实现无模型，必须在实际物理系统上进行训练，这可能因RL控制器缺乏先验知识而导致随机控制力，从而损害结构。为降低此风险，我们提出使用LQR控制器引导RL控制器。即使基于完全不正确的模型的LQR控制器也优于无控制状态。受此启发，我们引入了一种集成LQR和RL控制器的混合控制框架。该框架中的LQR策略从随机选择的模型及其参数中导出，无需了解真实或近似的结构模型，从而保持了整体框架的无模型特性，并最大限度地降低了原生RL实现中固有的探索风险。据我们所知，这是第一个解决基于RL的振动控制的关键训练安全挑战并提供验证解决方案的研究。

## 🔬 方法详解

**问题定义**：论文旨在解决基于强化学习的振动控制在实际物理系统训练中存在的安全风险问题。传统的基于模型的控制方法（如LQR）虽然有效，但需要精确的系统模型，而系统辨识过程非常耗时。直接在真实系统上训练强化学习控制器，由于其初始策略的随机性，可能对结构造成损害。

**核心思路**：论文的核心思路是利用一个基于随机模型的LQR控制器来引导强化学习控制器的训练过程。即使LQR控制器基于不准确的模型，也能提供一定的控制效果，从而限制强化学习控制器在探索阶段的随机行为，降低对结构的潜在损害。这种混合控制策略旨在实现安全且无模型的振动控制。

**技术框架**：该混合控制框架包含两个主要组成部分：一个基于随机模型的LQR控制器和一个强化学习控制器。LQR控制器根据一个随机选择的模型参数生成控制策略，用于在训练初期提供基本的振动抑制。强化学习控制器则通过与环境的交互不断学习和优化控制策略。在训练过程中，LQR控制器起到安全保障的作用，限制强化学习控制器的探索范围。最终，强化学习控制器将逐渐接管控制任务，实现更优的性能。

**关键创新**：该论文的关键创新在于提出了使用LQR控制器引导强化学习控制器训练的混合控制框架，从而解决了强化学习在实际物理系统训练中存在的安全风险问题。这种方法无需精确的系统模型，同时保证了训练过程的安全性。这是首次针对RL振动控制训练安全挑战提出的解决方案。

**关键设计**：LQR控制器的模型参数是随机选择的，无需进行系统辨识。强化学习控制器的具体算法（例如，Q-learning, SARSA, Actor-Critic）未在论文信息中明确提及，但可以选择合适的算法进行训练。关键在于LQR控制器提供的初始控制策略能够限制强化学习控制器的探索范围，避免其产生过大的控制力。

## 📊 实验亮点

论文提出了一种基于LQR引导的强化学习振动控制方法，解决了RL训练安全问题。即使LQR控制器基于不准确的模型，也能有效引导RL控制器的训练，避免对结构造成损害。该方法无需精确的系统模型，降低了系统辨识的成本和复杂性。具体性能数据和对比基线未在摘要中提及，但强调了该方法解决了RL振动控制的关键训练安全挑战。

## 🎯 应用场景

该研究成果可应用于各种需要振动控制的工程领域，例如桥梁、建筑物、飞行器和精密仪器等。通过该方法，可以在无需精确系统模型的情况下，安全地训练强化学习控制器，实现高效的振动抑制，降低结构损坏风险和维护成本。该方法为智能结构控制提供了一种新的思路，具有广阔的应用前景。

## 📄 摘要（原文）

> Structural vibrations induced by external excitations pose significant risks, including safety hazards for occupants, structural damage, and increased maintenance costs. While conventional model-based control strategies, such as Linear Quadratic Regulator (LQR), effectively mitigate vibrations, their reliance on accurate system models necessitates tedious system identification. This tedious system identification process can be avoided by using a model-free Reinforcement learning (RL) method. RL controllers derive their policies solely from observed structural behaviour, eliminating the requirement for an explicit structural model. For an RL controller to be truly model-free, its training must occur on the actual physical system rather than in simulation. However, during this training phase, the RL controller lacks prior knowledge and it exerts control force on the structure randomly, which can potentially harm the structure. To mitigate this risk, we propose guiding the RL controller using a Linear Quadratic Regulator (LQR) controller. While LQR control typically relies on an accurate structural model for optimal performance, our observations indicate that even an LQR controller based on an entirely incorrect model outperforms the uncontrolled scenario. Motivated by this finding, we introduce a hybrid control framework that integrates both LQR and RL controllers. In this approach, the LQR policy is derived from a randomly selected model and its parameters. As this LQR policy does not require knowledge of the true or an approximate structural model the overall framework remains model-free. This hybrid approach eliminates dependency on explicit system models while minimizing exploration risks inherent in naive RL implementations. As per our knowledge, this is the first study to address the critical training safety challenge of RL-based vibration control and provide a validated solution.

