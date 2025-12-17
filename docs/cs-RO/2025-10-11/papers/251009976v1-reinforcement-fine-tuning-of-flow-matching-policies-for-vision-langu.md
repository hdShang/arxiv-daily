---
layout: default
title: Reinforcement Fine-Tuning of Flow-Matching Policies for Vision-Language-Action Models
---

# Reinforcement Fine-Tuning of Flow-Matching Policies for Vision-Language-Action Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.09976" class="toolbar-btn" target="_blank">📄 arXiv: 2510.09976v1</a>
  <a href="https://arxiv.org/pdf/2510.09976.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.09976v1" onclick="toggleFavorite(this, '2510.09976v1', 'Reinforcement Fine-Tuning of Flow-Matching Policies for Vision-Language-Action Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mingyang Lyu, Yinqian Sun, Erliang Lin, Huangrui Li, Ruolin Chen, Feifei Zhao, Yi Zeng

**分类**: cs.LG, cs.RO

**发布日期**: 2025-10-11

---

## 💡 一句话要点

**提出Flow Policy Optimization (FPO)算法，用于强化微调视觉-语言-动作模型的Flow-Matching策略。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作模型` `强化学习` `Flow-Matching` `策略优化` `在线微调`

## 📋 核心要点

1. 现有VLA模型依赖大规模监督数据，性能受限于数据质量和覆盖范围，在线强化学习微调面临重要性采样计算难题。
2. 提出Flow Policy Optimization (FPO)算法，通过重构重要性采样过程，实现Flow-Matching策略的强化微调。
3. 在LIBERO和ALOHA任务上，FPO优于现有基线方法，并在稀疏奖励下表现出稳定的学习能力，验证了算法的有效性。

## 📝 摘要（中文）

视觉-语言-动作(VLA)模型，如OpenVLA、Octo和$π_0$，通过利用大规模演示数据展现了强大的泛化能力，但其性能仍受到监督数据质量和覆盖范围的根本限制。强化学习(RL)为通过在线交互改进和微调VLA模型提供了一条有希望的途径。然而，传统的策略梯度方法在基于Flow-Matching的模型中计算上不可行，因为重要性采样的过程难以处理，需要显式计算策略比率。为了克服这个限制，我们提出了Flow Policy Optimization (FPO)算法，该算法通过利用条件Flow-Matching目标中每个样本的变化来重新构建重要性采样。此外，FPO通过集成结构感知的信用分配以提高梯度效率、裁剪的替代目标以稳定优化、多步潜在探索以鼓励多样化的策略更新以及Q-集成机制以提供稳健的价值估计，实现了$π_0$模型的稳定和可扩展的在线强化微调。我们在LIBERO基准和ALOHA模拟任务上评估了FPO，并与监督、偏好对齐、基于扩散、自回归在线RL和$π_0$-FAST基线进行比较，观察到在稀疏奖励下，相对于模仿先验和强大的替代方案，FPO具有持续的改进和稳定的学习。此外，消融研究和潜在空间动态分析进一步突出了FPO中各个组成部分的贡献，验证了所提出的计算模块的有效性和在线RL期间条件Flow-Matching目标的稳定收敛。

## 🔬 方法详解

**问题定义**：论文旨在解决视觉-语言-动作(VLA)模型在实际应用中，由于监督数据的局限性导致性能瓶颈的问题。现有基于Flow-Matching的VLA模型，如$π_0$，虽然具有良好的泛化能力，但其性能上限受限于训练数据的质量和覆盖范围。利用强化学习进行在线微调是一个有潜力的解决方案，但传统策略梯度方法在Flow-Matching模型中面临重要性采样计算量大的问题，因为需要显式计算策略比率，这使得在线强化学习微调变得不可行。

**核心思路**：论文的核心思路是重新构建重要性采样过程，避免直接计算策略比率。具体而言，FPO算法利用条件Flow-Matching目标中每个样本的变化来近似重要性采样，从而将策略梯度计算转化为对Flow-Matching目标函数的优化。这种方法降低了计算复杂度，使得在线强化学习微调成为可能。此外，FPO还集成了多种技术来提高训练的稳定性和效率。

**技术框架**：FPO算法的整体框架包括以下几个主要模块：
1. **Flow Policy Optimization (FPO) 核心算法**：重新构建重要性采样，实现策略梯度优化。
2. **结构感知的信用分配**：提高梯度效率，加速学习过程。
3. **裁剪的替代目标**：稳定优化过程，防止策略崩溃。
4. **多步潜在探索**：鼓励策略多样性，避免陷入局部最优。
5. **Q-集成机制**：提供稳健的价值估计，提高策略评估的准确性。

**关键创新**：FPO算法最重要的技术创新在于其对重要性采样的重新构建。传统方法需要显式计算策略比率，而FPO通过利用条件Flow-Matching目标中每个样本的变化来近似重要性采样，从而避免了这一计算瓶颈。这种方法使得在Flow-Matching模型上进行在线强化学习微调成为可能，并显著降低了计算复杂度。

**关键设计**：FPO算法的关键设计包括：
1. **条件Flow-Matching目标函数**：利用该目标函数的变化来近似重要性采样。
2. **结构感知的信用分配策略**：根据动作对环境的影响程度分配不同的权重。
3. **裁剪的替代目标函数**：限制策略更新的幅度，防止策略崩溃。
4. **多步潜在探索策略**：在潜在空间中进行多步探索，鼓励策略多样性。
5. **Q-集成网络结构**：使用多个Q网络进行集成，提高价值估计的准确性。

## 📊 实验亮点

实验结果表明，FPO算法在LIBERO和ALOHA任务上均优于现有基线方法，包括监督学习、偏好对齐、基于扩散的模型、自回归在线RL以及$π_0$-FAST。在稀疏奖励环境下，FPO表现出更稳定的学习能力和更高的性能提升，验证了算法的有效性和鲁棒性。消融实验也证明了FPO中各个模块的贡献。

## 🎯 应用场景

该研究成果可应用于机器人控制、自动驾驶、游戏AI等领域。通过强化微调VLA模型，可以提升机器人在复杂环境中的决策能力和泛化性能，使其能够更好地理解人类指令并完成各种任务。未来，该技术有望推动机器人智能化水平的提升，实现更安全、高效的人机协作。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models such as OpenVLA, Octo, and $π_0$ have shown strong generalization by leveraging large-scale demonstrations, yet their performance is still fundamentally constrained by the quality and coverage of supervised data. Reinforcement learning (RL) provides a promising path for improving and fine-tuning VLAs through online interaction. However, conventional policy gradient methods are computationally infeasible in the context of flow-matching based models due to the intractability of the importance sampling process, which requires explicit computation of policy ratios. To overcome this limitation, we propose Flow Policy Optimization (FPO) algorithm, which reformulates importance sampling by leveraging per-sample changes in the conditional flow-matching objective. Furthermore, FPO achieves stable and scalable online reinforcement fine-tuning of the $π_0$ model by integrating structure-aware credit assignment to enhance gradient efficiency, clipped surrogate objectives to stabilize optimization, multi-step latent exploration to encourage diverse policy updates, and a Q-ensemble mechanism to provide robust value estimation. We evaluate FPO on the LIBERO benchmark and the ALOHA simulation task against supervised, preference-aligned, diffusion-based, autoregressive online RL, and $π_0$-FAST baselines, observing consistent improvements over the imitation prior and strong alternatives with stable learning under sparse rewards. In addition, ablation studies and analyses of the latent space dynamics further highlight the contributions of individual components within FPO, validating the effectiveness of the proposed computational modules and the stable convergence of the conditional flow-matching objective during online RL.

