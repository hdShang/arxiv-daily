---
layout: default
title: "ReVeal: Self-Evolving Code Agents via Reliable Self-Verification"
---

# ReVeal: Self-Evolving Code Agents via Reliable Self-Verification

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11442" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11442v2</a>
  <a href="https://arxiv.org/pdf/2506.11442.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11442v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11442v2', 'ReVeal: Self-Evolving Code Agents via Reliable Self-Verification')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yiyang Jin, Kunzhao Xu, Hang Li, Xueting Han, Yanmin Zhou, Cheng Li, Jing Bai

**分类**: cs.SE, cs.LG

**发布日期**: 2025-06-13 (更新: 2025-10-21)

---

## 💡 一句话要点

**提出ReVeal以解决自我验证不可靠的问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `自我验证` `代码生成` `多轮推理` `工具评估` `深度学习` `AI代理` `自动化编程`

## 📋 核心要点

1. 现有的强化学习方法依赖结果奖励，未能有效优化自我验证，导致验证不可靠和测试时扩展性不足。
2. 本文提出ReVeal框架，通过显式优化自我验证，结构化长时间推理为生成-验证回合，促进代码和测试的共同演化。
3. 实验结果显示，ReVeal在LiveCodeBench上实现了超过20轮的代码演化，显著提高了Pass@k，展示了更强的探索能力。

## 📝 摘要（中文）

强化学习与可验证奖励（RLVR）提升了大型语言模型的推理能力。然而，现有方法仅依赖结果奖励，未能显式优化验证或利用现实环境中的可靠信号，导致自我验证不可靠且测试时扩展性有限。为此，本文通过显式优化自我验证，提出了ReVeal，一个多轮强化学习框架，通过自我验证和基于工具的评估来演化代码生成。ReVeal将长时间推理结构化为迭代生成-验证回合，并结合TAPO进行回合级信用分配，促进代码与测试生成的共同演化。在推理阶段，增强的自我验证使模型能够利用自构建的测试和工具反馈，在LiveCodeBench上连续演化代码超过20轮，尽管训练仅基于三轮。这显著提高了Pass@k，表明探索能力增强，扩展了基础模型的推理边界。这些发现突显了ReVeal作为可扩展的RL训练和测试时扩展范式的潜力，为更强大和自主的AI代理铺平了道路。

## 🔬 方法详解

**问题定义**：本文旨在解决现有强化学习方法在自我验证方面的不可靠性，导致测试时扩展性不足的问题。现有方法仅依赖结果奖励，缺乏对验证过程的优化。

**核心思路**：ReVeal框架通过显式优化自我验证，将其作为深度测试时扩展的可靠驱动因素。通过将长时间推理结构化为迭代生成和验证的回合，增强了模型的推理能力。

**技术框架**：ReVeal的整体架构包括多个模块：生成模块负责代码生成，验证模块负责自我验证，TAPO用于回合级信用分配。整个过程通过多轮迭代进行，形成一个闭环反馈机制。

**关键创新**：ReVeal的主要创新在于将自我验证显式优化，并将其与生成过程结合，形成生成-验证的迭代回合。这与现有方法的单一结果奖励机制形成了本质区别。

**关键设计**：在设计中，采用了特定的损失函数来平衡生成和验证的权重，同时在网络结构上引入了模块化设计，以便于扩展和优化。

## 📊 实验亮点

实验结果表明，ReVeal在LiveCodeBench上实现了超过20轮的代码演化，尽管训练仅基于三轮，Pass@k显著提高，表明模型的探索能力增强，推理边界得到了扩展。

## 🎯 应用场景

ReVeal框架在代码生成和测试生成领域具有广泛的应用潜力，尤其适用于需要高可靠性和自适应能力的自动化编程任务。未来，该方法可扩展到更复杂的AI代理系统中，提升其自主学习和推理能力。

## 📄 摘要（原文）

> Reinforcement learning with verifiable rewards (RLVR) has advanced the reasoning capabilities of large language models. However, existing methods rely solely on outcome rewards, without explicitly optimizing verification or leveraging reliable signals from realistic environments, leading to unreliable self-verification and limited test-time scaling. To address this, we widen the verification-generation asymmetry by explicitly optimizing self-verification, making it a reliable driver of deeper test-time scaling. We introduce ReVeal, a multi-turn reinforcement learning framework that evolves code generation through self-verification and tool-based evaluation. ReVeal structures long-horizon reasoning as iterative generation-verification turns and incorporates TAPO for turn-level credit assignment, fostering the co-evolution of code and test generation. At inference, this strengthened self-verification enables the model to use self-constructed tests and tool feedback to continuously evolve code for 20+ turns on LiveCodeBench despite training on only three. It also significantly improves Pass@k, indicating stronger exploration that expands the reasoning boundaries of the base model. These findings highlight the promise of ReVeal as a scalable paradigm for RL training and test-time scaling, paving the way for more robust and autonomous AI agents.

