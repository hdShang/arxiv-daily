---
layout: default
title: "Trust, But Verify: A Self-Verification Approach to Reinforcement Learning with Verifiable Rewards"
---

# Trust, But Verify: A Self-Verification Approach to Reinforcement Learning with Verifiable Rewards

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13445" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13445v1</a>
  <a href="https://arxiv.org/pdf/2505.13445.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13445v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13445v1', 'Trust, But Verify: A Self-Verification Approach to Reinforcement Learning with Verifiable Rewards')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaoyuan Liu, Tian Liang, Zhiwei He, Jiahao Xu, Wenxuan Wang, Pinjia He, Zhaopeng Tu, Haitao Mi, Dong Yu

**分类**: cs.AI, cs.CL

**发布日期**: 2025-05-19

**备注**: code available at https://github.com/xyliu-cs/RISE

---

## 💡 一句话要点

**提出RISE框架以解决强化学习中的自我验证问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `自我验证` `可验证奖励` `数学推理` `大型语言模型` `在线学习` `模型训练`

## 📋 核心要点

1. 现有的强化学习方法在自我验证方面存在不足，模型无法有效地验证其输出的正确性。
2. RISE框架通过同时训练模型的问题解决和自我验证能力，利用可验证奖励提供实时反馈。
3. 实验结果显示，RISE在多个数学推理基准上显著提高了解决准确性，并增强了自我验证行为。

## 📝 摘要（中文）

大型语言模型（LLMs）在复杂推理中展现出巨大潜力，而可验证奖励的强化学习（RLVR）是其关键增强策略。然而，现有方法普遍存在“表面自我反思”的问题，模型未能有效验证自身输出。为此，本文提出RISE（通过自我验证强化推理），这是一个新颖的在线强化学习框架，旨在同时提升模型的问题解决能力和自我验证能力。RISE通过结果验证器提供可验证奖励，实时反馈解决方案生成和自我验证任务。在每次迭代中，模型生成解决方案并自我批评，两个轨迹共同促进策略更新。大量实验表明，RISE在数学推理基准上持续提高模型的解决准确性，同时增强自我验证能力。

## 🔬 方法详解

**问题定义**：本文旨在解决现有强化学习方法中模型自我验证能力不足的问题，尤其是“表面自我反思”现象，导致模型无法有效确认其输出的准确性。

**核心思路**：RISE框架的核心思想是通过在线强化学习过程，结合问题解决和自我验证任务的训练，利用可验证奖励提供实时反馈，从而提升模型的整体能力。

**技术框架**：RISE的整体架构包括两个主要模块：解决方案生成模块和自我验证模块。在每次迭代中，模型首先生成解决方案，然后对自身生成的解决方案进行批评，两个过程的结果共同用于更新策略。

**关键创新**：RISE的主要创新在于将自我验证与问题解决能力的训练整合在一个统一的强化学习框架中，显著提升了模型的自我反思能力，与传统方法相比，具有更高的灵活性和有效性。

**关键设计**：在RISE中，关键参数设置包括可验证奖励的设计和损失函数的选择，确保模型在自我验证过程中能够获得有效的反馈。此外，网络结构设计上，模型能够同时处理生成和验证任务，优化整体性能。

## 📊 实验亮点

在多个数学推理基准上，RISE模型的解决准确性显著提高，实验结果表明，相较于基线模型，RISE在自我验证行为上表现出更高的频率和准确性，验证了其有效性和优势。

## 🎯 应用场景

RISE框架具有广泛的应用潜力，特别是在需要高准确性和自我验证能力的复杂推理任务中，如自动化决策系统、智能助手和教育技术等领域。未来，RISE可能推动更智能的自我意识推理系统的发展，提升人工智能在实际应用中的可靠性和有效性。

## 📄 摘要（原文）

> Large Language Models (LLMs) show great promise in complex reasoning, with Reinforcement Learning with Verifiable Rewards (RLVR) being a key enhancement strategy. However, a prevalent issue is ``superficial self-reflection'', where models fail to robustly verify their own outputs. We introduce RISE (Reinforcing Reasoning with Self-Verification), a novel online RL framework designed to tackle this. RISE explicitly and simultaneously trains an LLM to improve both its problem-solving and self-verification abilities within a single, integrated RL process. The core mechanism involves leveraging verifiable rewards from an outcome verifier to provide on-the-fly feedback for both solution generation and self-verification tasks. In each iteration, the model generates solutions, then critiques its own on-policy generated solutions, with both trajectories contributing to the policy update. Extensive experiments on diverse mathematical reasoning benchmarks show that RISE consistently improves model's problem-solving accuracy while concurrently fostering strong self-verification skills. Our analyses highlight the advantages of online verification and the benefits of increased verification compute. Additionally, RISE models exhibit more frequent and accurate self-verification behaviors during reasoning. These advantages reinforce RISE as a flexible and effective path towards developing more robust and self-aware reasoners.

