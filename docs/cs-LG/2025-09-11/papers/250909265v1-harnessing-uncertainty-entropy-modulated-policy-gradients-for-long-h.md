---
layout: default
title: "Harnessing Uncertainty: Entropy-Modulated Policy Gradients for Long-Horizon LLM Agents"
---

# Harnessing Uncertainty: Entropy-Modulated Policy Gradients for Long-Horizon LLM Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09265" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09265v1</a>
  <a href="https://arxiv.org/pdf/2509.09265.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09265v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09265v1', 'Harnessing Uncertainty: Entropy-Modulated Policy Gradients for Long-Horizon LLM Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiawei Wang, Jiacai Liu, Yuqian Fu, Yingru Li, Xintao Wang, Yuan Lin, Yu Yue, Lin Zhang, Yang Wang, Ke Wang

**分类**: cs.LG, cs.CL

**发布日期**: 2025-09-11

**备注**: ICLR 2026 Under review

---

## 💡 一句话要点

**提出熵调制策略梯度(EMPG)以提升LLM Agent在长时任务中的表现**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `LLM Agent` `长时任务` `策略梯度` `熵调制` `强化学习` `不确定性` `信用分配`

## 📋 核心要点

1. 长时任务中，LLM Agent面临稀疏奖励带来的信用分配难题，现有方法依赖密集奖励信号，但效果有限。
2. EMPG通过熵调制策略梯度，根据每一步的不确定性重新校准学习信号，稳定探索并优化学习过程。
3. 在WebShop、ALFWorld和Deep Search等任务上，EMPG显著优于现有策略梯度方法，提升Agent性能。

## 📝 摘要（中文）

基于大型语言模型(LLM)的Agent在长时任务中面临着一个重大挑战：稀疏的、基于结果的奖励使得难以将功劳分配给中间步骤。以往的方法主要集中于创建密集的奖励信号来指导学习，例如通过逆强化学习等传统强化学习技术，或者使用过程奖励模型进行逐步反馈。本文发现LLM学习动态的一个根本问题：策略梯度的幅度与熵固有地耦合在一起，导致对确信的正确行为进行低效的小更新，并可能使不确定的行为进行不稳定的大更新。为了解决这个问题，我们提出了熵调制策略梯度(EMPG)，这是一个基于逐步不确定性和最终任务结果重新校准学习信号的框架。EMPG放大了对确信的正确行为的更新，惩罚了确信的错误，并减弱了来自不确定步骤的更新，以稳定探索。我们进一步引入了一个未来清晰度奖励项，鼓励Agent找到更可预测的解决方案路径。通过在三个具有挑战性的Agent任务WebShop、ALFWorld和Deep Search上的综合实验，我们证明了EMPG实现了显著的性能提升，并显著优于强大的策略梯度基线。

## 🔬 方法详解

**问题定义**：论文旨在解决长时任务中，基于LLM的Agent由于稀疏奖励而难以进行有效学习的问题。现有方法，如逆强化学习和过程奖励模型，试图通过生成密集的奖励信号来指导学习，但这些方法往往复杂且难以泛化。更根本的问题在于，LLM策略梯度的幅度与策略的熵值耦合，导致对确定性高的正确行为更新过小，而对不确定行为的更新可能不稳定，从而影响学习效率和稳定性。

**核心思路**：论文的核心思路是解耦策略梯度和熵之间的关系，通过熵调制来重新校准学习信号。具体来说，对于确定性高的正确行为，放大其梯度更新；对于确定性高的错误行为，惩罚其梯度更新；对于不确定性高的行为，减弱其梯度更新。此外，引入未来清晰度奖励，鼓励Agent选择更易预测的路径，从而提高学习效率。

**技术框架**：EMPG框架主要包含以下几个部分：1) LLM Agent与环境交互，生成轨迹数据；2) 计算每一步动作的熵值，作为不确定性的度量；3) 根据熵值和最终奖励，计算熵调制后的策略梯度；4) 使用熵调制后的策略梯度更新LLM Agent的策略；5) 计算未来清晰度奖励，并将其加入到总奖励中。整个流程通过不断迭代，优化Agent的策略，使其能够更好地完成长时任务。

**关键创新**：EMPG最重要的创新点在于提出了熵调制策略梯度，它能够根据每一步的不确定性动态调整学习信号的强度。与传统的策略梯度方法相比，EMPG能够更有效地利用数据，提高学习效率和稳定性。此外，未来清晰度奖励也是一个重要的创新，它能够引导Agent选择更易于学习的路径。

**关键设计**：EMPG的关键设计包括：1) 熵的计算方式，论文中使用的是标准的策略熵；2) 熵调制函数的选择，论文中使用了线性函数，但也可以尝试其他非线性函数；3) 未来清晰度奖励的计算方式，论文中使用的是基于模型预测的奖励，也可以尝试其他基于规则或学习的奖励；4) 各种超参数的设置，如熵调制系数、未来清晰度奖励系数等，这些超参数需要根据具体任务进行调整。

## 📊 实验亮点

实验结果表明，EMPG在WebShop、ALFWorld和Deep Search三个具有挑战性的Agent任务上均取得了显著的性能提升。例如，在WebShop任务上，EMPG的成功率比基线方法提高了超过20%。这些结果证明了EMPG的有效性和泛化能力，表明其能够显著提升LLM Agent在长时任务中的表现。

## 🎯 应用场景

EMPG具有广泛的应用前景，可以应用于各种需要长时规划和决策的任务中，例如机器人导航、游戏AI、自动驾驶、任务型对话系统等。通过提高Agent在复杂环境中的学习效率和稳定性，EMPG可以帮助开发更智能、更可靠的AI系统，从而提升生产效率，改善用户体验。

## 📄 摘要（原文）

> In long-horizon tasks, recent agents based on Large Language Models (LLMs) face a significant challenge that sparse, outcome-based rewards make it difficult to assign credit to intermediate steps. Previous methods mainly focus on creating dense reward signals to guide learning, either through traditional reinforcement learning techniques like inverse reinforcement learning or by using Process Reward Models for step-by-step feedback. In this paper, we identify a fundamental problem in the learning dynamics of LLMs: the magnitude of policy gradients is inherently coupled with the entropy, which leads to inefficient small updates for confident correct actions and potentially destabilizes large updates for uncertain ones. To resolve this, we propose Entropy-Modulated Policy Gradients (EMPG), a framework that re-calibrates the learning signal based on step-wise uncertainty and the final task outcome. EMPG amplifies updates for confident correct actions, penalizes confident errors, and attenuates updates from uncertain steps to stabilize exploration. We further introduce a bonus term for future clarity that encourages agents to find more predictable solution paths. Through comprehensive experiments on three challenging agent tasks, WebShop, ALFWorld, and Deep Search, we demonstrate that EMPG achieves substantial performance gains and significantly outperforms strong policy gradient baselines. Project page is at https://empgseed-seed.github.io/

