---
layout: default
title: Performative Policy Gradient: Optimality in Performative Reinforcement Learning
---

# Performative Policy Gradient: Optimality in Performative Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20576" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20576v1</a>
  <a href="https://arxiv.org/pdf/2512.20576.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20576v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20576v1', 'Performative Policy Gradient: Optimality in Performative Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Debabrota Basu, Udvas Das, Brahim Driss, Uddalak Mukherjee

**分类**: cs.LG, cs.AI, math.OC

**发布日期**: 2025-12-23

---

## 💡 一句话要点

**提出PePG算法，解决强化学习中策略执行带来的环境动态变化问题，实现策略的执行最优性。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `执行性强化学习` `策略梯度` `环境动态` `策略优化` `最优性` `性能差异引理` `后部署机器学习`

## 📋 核心要点

1. 传统强化学习忽略了策略执行对环境动态的影响，导致算法在实际部署中性能下降。
2. 论文提出Performative Policy Gradient (PePG) 算法，通过考虑策略执行带来的环境变化，优化策略。
3. 实验结果表明，PePG 在标准执行性强化学习环境中优于传统策略梯度算法和其他旨在实现稳定性的执行性RL算法。

## 📝 摘要（中文）

后部署的机器学习算法通常会影响它们所作用的环境，从而改变标准强化学习（RL）方法忽略的底层动态。虽然在执行性设置中设计最优算法最近已在监督学习中得到研究，但RL对应方法仍未得到充分探索。在本文中，我们证明了RL中性能差异引理和策略梯度定理的执行性对应物，并进一步介绍了执行性策略梯度算法（PePG）。PePG是第一个旨在解决RL中执行性问题的策略梯度算法。在softmax参数化下，无论是否进行熵正则化，我们都证明PePG收敛到执行性最优策略，即在自身引起的分布变化下保持最优的策略。因此，PePG显著扩展了先前在执行性RL中的工作，这些工作实现了执行性稳定性，但没有实现最优性。此外，我们对标准执行性RL环境的实证分析验证了PePG优于标准策略梯度算法和现有旨在实现稳定性的执行性RL算法。

## 🔬 方法详解

**问题定义**：论文旨在解决强化学习中，智能体策略的执行会对环境产生影响，进而改变环境动态，导致传统强化学习算法训练出的策略不再是最优的问题。现有方法通常忽略这种环境变化，或者只关注策略的稳定性，而无法保证策略的执行最优性。

**核心思路**：论文的核心思路是，将策略执行对环境的影响纳入强化学习的优化过程中。通过对性能差异引理和策略梯度定理进行扩展，使其能够反映策略执行带来的环境变化，从而指导策略的优化。PePG算法旨在找到一种策略，该策略在由自身引起的分布变化下仍然是最优的。

**技术框架**：PePG算法基于策略梯度方法，其整体框架与传统的策略梯度算法类似，包括以下几个主要步骤：1) 收集经验数据：智能体与环境交互，收集状态、动作、奖励等数据。2) 估计策略梯度：利用收集到的数据，估计策略梯度，该梯度反映了策略对环境的影响。3) 更新策略：根据估计的策略梯度，更新策略参数。PePG的关键在于策略梯度的估计方式，它考虑了策略执行带来的环境变化。

**关键创新**：PePG算法最重要的技术创新点在于，它首次在策略梯度算法中考虑了策略执行对环境的影响，并证明了在softmax参数化下，PePG算法能够收敛到执行性最优策略。与现有方法的本质区别在于，PePG算法不仅关注策略的稳定性，更关注策略的执行最优性。

**关键设计**：PePG算法的关键设计包括：1) 对性能差异引理和策略梯度定理进行扩展，使其能够反映策略执行带来的环境变化。2) 使用softmax参数化策略，并证明了在该参数化下，PePG算法能够收敛到执行性最优策略。3) 可以选择是否使用熵正则化，以提高策略的探索能力和稳定性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20576v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20576v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20576v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，在标准执行性强化学习环境中，PePG算法优于传统的策略梯度算法和其他旨在实现稳定性的执行性RL算法。具体来说，PePG算法能够更快地收敛到最优策略，并且在环境发生变化时，能够更好地保持策略的性能。这验证了PePG算法在解决执行性强化学习问题上的有效性。

## 🎯 应用场景

该研究成果可应用于机器人、自动驾驶、推荐系统等领域，在这些领域中，智能体的行为会对环境产生显著影响。通过使用PePG算法，可以训练出更适应环境变化、性能更优的策略，提高智能体在实际应用中的表现。例如，在推荐系统中，PePG可以用于优化推荐策略，使其能够适应用户兴趣的变化，从而提高推荐的准确性和用户满意度。

## 📄 摘要（原文）

> Post-deployment machine learning algorithms often influence the environments they act in, and thus shift the underlying dynamics that the standard reinforcement learning (RL) methods ignore. While designing optimal algorithms in this performative setting has recently been studied in supervised learning, the RL counterpart remains under-explored. In this paper, we prove the performative counterparts of the performance difference lemma and the policy gradient theorem in RL, and further introduce the Performative Policy Gradient algorithm (PePG). PePG is the first policy gradient algorithm designed to account for performativity in RL. Under softmax parametrisation, and also with and without entropy regularisation, we prove that PePG converges to performatively optimal policies, i.e. policies that remain optimal under the distribution shifts induced by themselves. Thus, PePG significantly extends the prior works in Performative RL that achieves performative stability but not optimality. Furthermore, our empirical analysis on standard performative RL environments validate that PePG outperforms standard policy gradient algorithms and the existing performative RL algorithms aiming for stability.

