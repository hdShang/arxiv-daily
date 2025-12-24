---
layout: default
title: BASIL: Best-Action Symbolic Interpretable Learning for Evolving Compact RL Policies
---

# BASIL: Best-Action Symbolic Interpretable Learning for Evolving Compact RL Policies

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00328" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00328v3</a>
  <a href="https://arxiv.org/pdf/2506.00328.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00328v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00328v3', 'BASIL: Best-Action Symbolic Interpretable Learning for Evolving Compact RL Policies')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kourosh Shahnazari, Seyed Moein Ayyoubzadeh, Mohammadali Keshtparvar

**分类**: cs.AI

**发布日期**: 2025-05-31 (更新: 2025-06-11)

---

## 💡 一句话要点

**提出BASIL以解决可解释强化学习的挑战**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `可解释强化学习` `符号学习` `进化算法` `质量多样性优化` `自动决策系统`

## 📋 核心要点

1. 现有深度强化学习方法生成的策略往往不透明，难以进行验证和人类监督，限制了其在安全关键领域的应用。
2. BASIL通过在线进化搜索与质量多样性优化，生成符号化的基于规则的可解释策略，确保策略的透明性和复杂性可控。
3. 在三个基准任务中，BASIL合成的可解释控制器在表现上与深度强化学习基线相当，展示了其有效性和实用性。

## 📝 摘要（中文）

可解释的强化学习是安全关键应用中自主决策系统部署的一项重大挑战。现代深度强化学习方法虽然强大，但往往生成不透明的策略，妨碍验证、降低透明度并阻碍人类监督。为此，本文提出BASIL（最佳行动符号可解释学习），通过在线进化搜索与质量多样性优化，系统性地生成符号化的基于规则的策略。BASIL将策略表示为状态变量上的有序符号谓词列表，确保完全可解释性和可处理的策略复杂性。通过使用质量多样性归档，该方法鼓励顶尖解决方案之间的行为和结构多样性，同时复杂度感知的适应性促进了紧凑表示的合成。实验证明，BASIL在CartPole-v1、MountainCar-v0和Acrobot-v1三个基准任务中，始终合成出与深度强化学习基线相当的可解释控制器。

## 🔬 方法详解

**问题定义**：本文旨在解决可解释强化学习中的不透明策略问题，现有方法在安全关键应用中难以验证和监督。

**核心思路**：BASIL通过在线进化搜索生成符号化的规则基础策略，确保策略的可解释性和复杂性可控，促进多样性与紧凑表示的合成。

**技术框架**：BASIL的整体架构包括质量多样性归档、复杂度感知适应性和在线学习模块，支持对策略的动态生成与优化。

**关键创新**：BASIL的主要创新在于结合了符号表达能力、进化多样性和在线学习，形成统一的策略合成框架，与传统深度强化学习方法本质上不同。

**关键设计**：在设计中，BASIL使用确切的规则数量约束和适应性机制，以平衡透明性与表达能力，同时优化复杂度感知的适应性适应性函数。

## 📊 实验亮点

在三个基准任务（CartPole-v1、MountainCar-v0和Acrobot-v1）中，BASIL合成的可解释控制器在性能上与深度强化学习基线相当，展示了其在策略透明性和复杂性控制方面的优势。实验结果表明，BASIL能够有效生成紧凑且可解释的策略，提升了可解释强化学习的实用性。

## 🎯 应用场景

BASIL的研究成果在安全关键领域具有广泛的应用潜力，如自动驾驶、医疗决策和工业自动化等。通过提供可解释的决策支持，BASIL能够增强人类对自动化系统的信任，促进其在复杂环境中的应用。未来，BASIL的框架可能会被进一步扩展，以适应更多的动态和复杂的决策场景。

## 📄 摘要（原文）

> The quest for interpretable reinforcement learning is a grand challenge for the deployment of autonomous decision-making systems in safety-critical applications. Modern deep reinforcement learning approaches, while powerful, tend to produce opaque policies that compromise verification, reduce transparency, and impede human oversight. To address this, we introduce BASIL (Best-Action Symbolic Interpretable Learning), a systematic approach for generating symbolic, rule-based policies via online evolutionary search with quality-diversity (QD) optimization. BASIL represents policies as ordered lists of symbolic predicates over state variables, ensuring full interpretability and tractable policy complexity. By using a QD archive, the methodology in the proposed study encourages behavioral and structural diversity between top-performing solutions, while a complexity-aware fitness encourages the synthesis of compact representations. The evolutionary system supports the use of exact constraints for rule count and system adaptability for balancing transparency with expressiveness. Empirical comparisons with three benchmark tasks CartPole-v1, MountainCar-v0, and Acrobot-v1 show that BASIL consistently synthesizes interpretable controllers with compact representations comparable to deep reinforcement learning baselines. Herein, this article introduces a new interpretable policy synthesis method that combines symbolic expressiveness, evolutionary diversity, and online learning through a unifying framework.

