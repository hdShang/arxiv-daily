---
layout: default
title: "Learning to Recover: Dynamic Reward Shaping with Wheel-Leg Coordination for Fallen Robots"
---

# Learning to Recover: Dynamic Reward Shaping with Wheel-Leg Coordination for Fallen Robots

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05516" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05516v2</a>
  <a href="https://arxiv.org/pdf/2506.05516.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05516v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05516v2', 'Learning to Recover: Dynamic Reward Shaping with Wheel-Leg Coordination for Fallen Robots')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Boyuan Deng, Luca Rossini, Jin Wang, Weijie Wang, Dimitrios Kanoulas, Nikolaos Tsagarakis

**分类**: cs.RO, cs.AI, cs.LG

**发布日期**: 2025-06-05 (更新: 2025-10-08)

**🔗 代码/项目**: [PROJECT_PAGE](https://boyuandeng.github.io/L2R-WheelLegCoordination/)

---

## 💡 一句话要点

**提出动态奖励塑形方法以解决机器人跌倒恢复问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `轮腿机器人` `动态奖励塑形` `课程学习` `恢复策略` `自适应控制`

## 📋 核心要点

1. 现有方法依赖于预先规划的动作和简化模型，难以应对复杂的跌倒恢复场景，导致恢复策略的鲁棒性不足。
2. 本文提出了一种学习框架，结合动态奖励塑形与课程学习，旨在动态调整恢复策略的探索与姿态优化。
3. 在两个四足平台上的实验结果显示，恢复成功率高达99.1%和97.8%，且关节扭矩消耗显著降低，验证了方法的有效性。

## 📝 摘要（中文）

适应性恢复跌倒事件是轮腿机器人实际应用中的关键技能，这类机器人结合了腿的灵活性与轮子的速度以实现快速恢复。然而，传统方法依赖于预先规划的恢复动作、简化的动力学或稀疏奖励，往往无法产生稳健的恢复策略。本文提出了一种基于学习的框架，集成了基于情节的动态奖励塑形和课程学习，动态平衡多样恢复动作的探索与精确姿态的优化。采用不对称的演员-评论家架构，通过利用仿真中的特权信息加速训练，同时注入噪声的观察增强了对不确定性的鲁棒性。实验表明，协同的轮腿协调减少了15.8%和26.2%的关节扭矩消耗，并通过能量转移机制改善了稳定性。在两个不同的四足平台上进行的广泛评估显示，恢复成功率高达99.1%和97.8%，且无需特定平台的调优。

## 🔬 方法详解

**问题定义**：本文旨在解决轮腿机器人在跌倒后恢复的挑战，现有方法往往依赖于预设的恢复动作，缺乏灵活性和适应性。

**核心思路**：通过引入动态奖励塑形与课程学习，论文的核心思路是动态平衡恢复动作的探索与姿态的精细调整，以提高恢复策略的有效性和鲁棒性。

**技术框架**：整体架构包括动态奖励塑形模块、课程学习模块和不对称的演员-评论家网络。动态奖励塑形根据恢复过程中的表现调整奖励，而课程学习则逐步增加任务难度以促进学习。

**关键创新**：最重要的创新在于将动态奖励塑形与课程学习结合，形成了一种新的训练策略，显著提升了机器人在复杂环境中的恢复能力。

**关键设计**：在网络结构上，采用不对称的演员-评论家架构，并在训练过程中注入噪声以增强对环境不确定性的鲁棒性。同时，设计了特定的损失函数以优化恢复策略。

## 📊 实验亮点

实验结果显示，采用该方法的机器人在两个四足平台上的恢复成功率分别达到99.1%和97.8%，相比于传统方法，关节扭矩消耗减少了15.8%和26.2%，显著提升了能效和稳定性。

## 🎯 应用场景

该研究的潜在应用领域包括服务机器人、救援机器人以及工业自动化等场景，能够显著提升机器人在复杂环境中的自适应能力和恢复效率。未来，该方法有望推动轮腿机器人在实际应用中的广泛部署，提升其操作的安全性和可靠性。

## 📄 摘要（原文）

> Adaptive recovery from fall incidents are essential skills for the practical deployment of wheeled-legged robots, which uniquely combine the agility of legs with the speed of wheels for rapid recovery. However, traditional methods relying on preplanned recovery motions, simplified dynamics or sparse rewards often fail to produce robust recovery policies. This paper presents a learning-based framework integrating Episode-based Dynamic Reward Shaping and curriculum learning, which dynamically balances exploration of diverse recovery maneuvers with precise posture refinement. An asymmetric actor-critic architecture accelerates training by leveraging privileged information in simulation, while noise-injected observations enhance robustness against uncertainties. We further demonstrate that synergistic wheel-leg coordination reduces joint torque consumption by 15.8% and 26.2% and improves stabilization through energy transfer mechanisms. Extensive evaluations on two distinct quadruped platforms achieve recovery success rates up to 99.1% and 97.8% without platform-specific tuning. The supplementary material is available at https://boyuandeng.github.io/L2R-WheelLegCoordination/

