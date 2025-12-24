---
layout: default
title: "AutoRule: Reasoning Chain-of-thought Extracted Rule-based Rewards Improve Preference Learning"
---

# AutoRule: Reasoning Chain-of-thought Extracted Rule-based Rewards Improve Preference Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15651" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15651v1</a>
  <a href="https://arxiv.org/pdf/2506.15651.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15651v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15651v1', 'AutoRule: Reasoning Chain-of-thought Extracted Rule-based Rewards Improve Preference Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tevin Wang, Chenyan Xiong

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-06-18

**🔗 代码/项目**: [GITHUB](https://github.com/cxcscmu/AutoRule)

---

## 💡 一句话要点

**提出AutoRule以自动化提取规则改善偏好学习**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `规则提取` `强化学习` `人类反馈` `自动化` `偏好学习` `语言模型`

## 📋 核心要点

1. 现有的基于规则的奖励方法依赖手动规则工程，效率低且难以扩展。
2. AutoRule通过自动提取用户偏好中的规则，形成基于规则的奖励，简化了这一过程。
3. 实验结果显示，使用AutoRule训练的模型在多个评估指标上显著优于基线模型，提升效果明显。

## 📝 摘要（中文）

基于规则的奖励为从人类反馈中改进强化学习（RLHF）提供了一种有前景的策略，但现有方法通常依赖于手动规则工程。我们提出了AutoRule，这是一种完全自动化的方法，用于从偏好反馈中提取规则并将其制定为基于规则的奖励。AutoRule提取过程分为三个阶段：利用推理模型解释用户偏好，从这些解释的推理链中识别候选规则，并将其合成统一的规则集。通过最终的规则集，我们使用语言模型验证器计算每个输出满足的规则比例，并将该指标作为辅助奖励与学习的奖励模型一起用于策略优化。使用AutoRule训练Llama-3-8B模型在AlpacaEval2.0上实现了28.6%的相对提升，并在MT-Bench子集的第二轮表现上获得了6.1%的相对增益。我们的分析确认提取的规则与数据集偏好高度一致。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有基于规则的奖励方法依赖手动规则工程的问题，这导致了效率低下和难以扩展的局限性。

**核心思路**：论文提出的AutoRule方法通过自动化提取用户偏好中的规则，形成基于规则的奖励，从而提高强化学习的效率和效果。

**技术框架**：AutoRule的提取过程分为三个主要阶段：首先，利用推理模型解释用户的偏好；其次，从这些解释的推理链中识别候选规则；最后，将候选规则合成一个统一的规则集。

**关键创新**：AutoRule的最大创新在于其完全自动化的规则提取过程，显著减少了对人工干预的依赖，提升了规则的生成效率和准确性。

**关键设计**：在技术细节上，AutoRule使用语言模型验证器来计算每个输出满足的规则比例，并将其作为辅助奖励与学习的奖励模型结合使用，以优化策略。

## 📊 实验亮点

实验结果显示，使用AutoRule训练的Llama-3-8B模型在AlpacaEval2.0上实现了28.6%的相对提升，并在MT-Bench子集的第二轮表现上获得了6.1%的相对增益，显著优于基线模型GRPO。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和人机交互等，能够有效提升模型在复杂任务中的表现。未来，AutoRule可能会在更多领域中推广，促进自动化规则生成技术的发展。

## 📄 摘要（原文）

> Rule-based rewards offer a promising strategy for improving reinforcement learning from human feedback (RLHF), but current approaches often rely on manual rule engineering. We present AutoRule, a fully automated method for extracting rules from preference feedback and formulating them into rule-based rewards. AutoRule extraction operates in three stages: it leverages a reasoning model to interpret user preferences, identifies candidate rules from the reasoning chain of these interpretations, and synthesizes them into a unified rule set. Leveraging the finalized rule set, we employ language-model verifiers to compute the fraction of rules satisfied by each output, using this metric as an auxiliary reward alongside the learned reward model during policy optimization. Training a Llama-3-8B model with AutoRule results in a 28.6\% relative improvement in length-controlled win rate on AlpacaEval2.0, and a 6.1\% relative gain in second-turn performance on a held-out MT-Bench subset, compared to a GRPO baseline trained with the same learned reward model but without the rule-based auxiliary reward. Our analysis confirms that the extracted rules exhibit good agreement with dataset preference. We find that AutoRule demonstrates reduced reward hacking compared to a learned reward model when run over two episodes. Finally, our case study suggests that the extracted rules capture unique qualities valued in different datasets. The extracted rules are provided in the appendix, and the code is open-sourced at https://github.com/cxcscmu/AutoRule.

