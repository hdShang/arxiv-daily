---
layout: default
title: Provably Optimal Reinforcement Learning under Safety Filtering
---

# Provably Optimal Reinforcement Learning under Safety Filtering

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.18082" class="toolbar-btn" target="_blank">📄 arXiv: 2510.18082v1</a>
  <a href="https://arxiv.org/pdf/2510.18082.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.18082v1" onclick="toggleFavorite(this, '2510.18082v1', 'Provably Optimal Reinforcement Learning under Safety Filtering')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Donggeon David Oh, Duy P. Nguyen, Haimin Hu, Jaime F. Fisac

**分类**: cs.LG, cs.RO, eess.SY

**发布日期**: 2025-10-20

**备注**: 17 pages, 3 figures

---

## 💡 一句话要点

**提出安全过滤下的可证明最优强化学习方法，解决安全约束下的性能损失问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `安全强化学习` `安全过滤` `马尔可夫决策过程` `安全性` `最优性` `Safety Gymnasium`

## 📋 核心要点

1. 现有强化学习方法在安全关键场景中应用受限，缺乏正式安全保证，容易出现灾难性故障。
2. 论文提出一种基于安全过滤的强化学习框架，证明了适当的安全过滤不会降低渐近性能。
3. 实验表明，该方法在Safety Gymnasium上实现了零违规，且性能与未过滤的基线相当甚至更好。

## 📝 摘要（中文）

近年来，强化学习（RL）在日益复杂的任务中得到应用，但缺乏正式的安全保证限制了其在安全关键环境中的应用。一种常见的实用方法是用安全过滤器增强RL策略，该过滤器会覆盖不安全的动作，以防止训练和部署期间的失败。然而，安全过滤通常被认为会牺牲性能并阻碍学习过程。本文证明，这种安全-性能权衡并非固有，并且首次证明，使用足够宽松的安全过滤器来强制执行安全性不会降低渐近性能。本文使用安全关键马尔可夫决策过程（SC-MDP）来形式化RL安全性，该过程需要绝对避免灾难性故障状态，而不是高概率避免。此外，本文定义了一个相关的过滤MDP，由于安全过滤器（被认为是环境的一部分），所有动作都会产生安全效果。本文的主要定理表明：（i）在过滤后的MDP中学习是绝对安全的，（ii）标准RL收敛适用于过滤后的MDP，以及（iii）在过滤后的MDP中最佳的任何策略（通过相同的过滤器执行时）实现了与SC-MDP中最佳安全策略相同的渐近回报，从而实现了安全执行和性能优化之间的完全分离。本文在Safety Gymnasium上使用代表性任务和约束验证了该理论，观察到训练期间零违规，并且最终性能匹配或超过了未过滤的基线。这些结果阐明了安全过滤学习中一个长期存在的问题，并为安全RL提供了一个简单、有原则的方案：训练和部署具有最宽松可用安全过滤器的RL策略。

## 🔬 方法详解

**问题定义**：现有强化学习方法在安全关键任务中，由于缺乏安全保证，容易导致灾难性后果。常见的安全过滤方法虽然能保证安全性，但往往会牺牲性能，阻碍学习过程，造成安全性和性能之间的权衡。因此，需要一种既能保证安全性，又能保持甚至提升性能的强化学习方法。

**核心思路**：论文的核心思路是证明，只要安全过滤器足够宽松（即允许尽可能多的安全动作），那么在过滤后的MDP中学习到的最优策略，在原始SC-MDP中也能达到最优性能。这意味着安全性和性能可以解耦，可以先通过安全过滤器保证安全性，再优化性能，而不用担心安全过滤会影响最终性能。

**技术框架**：论文构建了一个安全关键马尔可夫决策过程（SC-MDP）来形式化安全约束，并定义了一个过滤后的MDP，其中所有动作都是安全的，这得益于安全过滤器的作用。整体框架包含以下几个关键部分：1. 定义SC-MDP，明确安全状态和安全约束；2. 设计安全过滤器，将不安全动作过滤掉，只允许安全动作；3. 构建过滤后的MDP，在该MDP中进行强化学习；4. 证明在过滤后的MDP中学习到的最优策略，在原始SC-MDP中也能达到最优性能。

**关键创新**：论文最重要的创新在于证明了安全过滤下的强化学习可以达到最优性能，打破了安全性和性能之间的权衡。以往的研究通常认为安全过滤会牺牲性能，而本文证明了只要安全过滤器足够宽松，就不会出现这种情况。这为安全强化学习提供了一个新的视角和方法。

**关键设计**：论文的关键设计在于安全过滤器的宽松程度。安全过滤器需要足够宽松，以允许尽可能多的安全动作，从而避免过度限制策略的学习。论文并没有给出具体的安全过滤器设计方法，而是强调了其宽松性的重要性。此外，论文还依赖于标准强化学习算法的收敛性，并证明了这些算法在过滤后的MDP中仍然有效。

## 📊 实验亮点

论文在Safety Gymnasium上进行了实验，结果表明，使用安全过滤的强化学习方法在训练过程中实现了零违规，并且最终性能与未过滤的基线相当甚至更好。这验证了论文的理论结果，即安全过滤不会降低渐近性能，甚至可以提高性能。例如，在某些任务中，安全过滤后的策略能够更快地收敛到最优策略。

## 🎯 应用场景

该研究成果可应用于各种安全关键领域，如自动驾驶、机器人控制、医疗决策等。通过使用安全过滤器，可以保证系统在训练和部署过程中不会发生灾难性故障，从而提高系统的安全性和可靠性。该方法还有助于加速强化学习在这些领域的应用，降低开发成本和风险。

## 📄 摘要（原文）

> Recent advances in reinforcement learning (RL) enable its use on increasingly complex tasks, but the lack of formal safety guarantees still limits its application in safety-critical settings. A common practical approach is to augment the RL policy with a safety filter that overrides unsafe actions to prevent failures during both training and deployment. However, safety filtering is often perceived as sacrificing performance and hindering the learning process. We show that this perceived safety-performance tradeoff is not inherent and prove, for the first time, that enforcing safety with a sufficiently permissive safety filter does not degrade asymptotic performance. We formalize RL safety with a safety-critical Markov decision process (SC-MDP), which requires categorical, rather than high-probability, avoidance of catastrophic failure states. Additionally, we define an associated filtered MDP in which all actions result in safe effects, thanks to a safety filter that is considered to be a part of the environment. Our main theorem establishes that (i) learning in the filtered MDP is safe categorically, (ii) standard RL convergence carries over to the filtered MDP, and (iii) any policy that is optimal in the filtered MDP-when executed through the same filter-achieves the same asymptotic return as the best safe policy in the SC-MDP, yielding a complete separation between safety enforcement and performance optimization. We validate the theory on Safety Gymnasium with representative tasks and constraints, observing zero violations during training and final performance matching or exceeding unfiltered baselines. Together, these results shed light on a long-standing question in safety-filtered learning and provide a simple, principled recipe for safe RL: train and deploy RL policies with the most permissive safety filter that is available.

