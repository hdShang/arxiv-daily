---
layout: default
title: "Legal$Δ$: Enhancing Legal Reasoning in LLMs via Reinforcement Learning with Chain-of-Thought Guided Information Gain"
---

# Legal$Δ$: Enhancing Legal Reasoning in LLMs via Reinforcement Learning with Chain-of-Thought Guided Information Gain

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.12281" class="toolbar-btn" target="_blank">📄 arXiv: 2508.12281v2</a>
  <a href="https://arxiv.org/pdf/2508.12281.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.12281v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.12281v2', 'Legal$Δ$: Enhancing Legal Reasoning in LLMs via Reinforcement Learning with Chain-of-Thought Guided Information Gain')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xin Dai, Buqiang Xu, Zhenghao Liu, Yukun Yan, Huiyuan Xie, Xiaoyuan Yi, Shuo Wang, Ge Yu

**分类**: cs.CL

**发布日期**: 2025-08-17 (更新: 2025-08-19)

**🔗 代码/项目**: [GITHUB](https://github.com/NEUIR/LegalDelta)

---

## 💡 一句话要点

**提出Legal$Δ$以解决法律推理模型的可靠性与可解释性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `法律推理` `强化学习` `链式思维` `信息增益` `大型语言模型` `可解释性` `深度学习`

## 📋 核心要点

1. 现有法律LLMs在复杂法律场景中缺乏可靠的推理能力，常常只给出直接答案，导致可解释性不足。
2. 本文提出的Legal$Δ$框架通过强化学习和链式思维引导的信息增益，提升法律推理的质量和深度。
3. 实验结果显示，Legal$Δ$在法律推理任务中超越了多个基线模型，提升了准确性和可解释性。

## 📝 摘要（中文）

法律人工智能（LegalAI）在自动化司法决策方面取得了显著进展，但现有的法律大型语言模型（LLMs）在生成可靠和可解释的推理过程中仍然面临挑战。它们往往快速给出答案，而缺乏明确的多步骤推理，这限制了在复杂法律场景中的有效性。为了解决这一问题，本文提出了Legal$Δ$，一个通过链式思维引导的信息增益来增强法律推理的强化学习框架。Legal$Δ$在训练过程中采用双模式输入设置，最大化直接答案与推理增强模式之间的信息增益，从而鼓励模型获取有意义的推理模式。实验结果表明，Legal$Δ$在多个法律推理任务中超越了强基线，在准确性和可解释性上均表现优异。

## 🔬 方法详解

**问题定义**：现有的法律大型语言模型在复杂的法律推理任务中，往往缺乏可靠性和可解释性，导致生成的答案缺乏多步骤推理的支持，限制了其在实际应用中的有效性。

**核心思路**：本文提出的Legal$Δ$框架通过强化学习结合链式思维引导的信息增益，旨在提升模型的推理能力，使其能够生成更为深刻和可靠的法律判断。

**技术框架**：Legal$Δ$采用双模式输入设置，包括直接答案模式和推理增强模式。在训练过程中，模型通过最大化这两种模式之间的信息增益，逐步提炼出有效的推理模式。框架分为两个阶段：首先从强大的大型推理模型DeepSeek-R1中提炼潜在推理能力，其次通过差异比较和多维奖励机制来优化推理质量。

**关键创新**：Legal$Δ$的主要创新在于其双模式输入和信息增益最大化策略，这与传统的单一答案生成方法有本质区别。通过引导模型关注推理过程而非仅仅答案，提升了法律推理的深度和可靠性。

**关键设计**：在设计上，Legal$Δ$采用了多维奖励机制，评估推理的结构一致性和法律领域的特异性。此外，模型的损失函数设计考虑了推理的质量与信息增益之间的平衡，确保生成的推理过程既有深度又具备可解释性。

## 📊 实验亮点

实验结果表明，Legal$Δ$在多个法律推理任务中表现优异，准确性和可解释性均显著高于强基线模型，具体提升幅度达到XX%（具体数据待补充）。该模型在不依赖标注偏好数据的情况下，持续生成更为稳健和可信的法律判断。

## 🎯 应用场景

该研究的潜在应用领域包括法律咨询、智能合约审查和司法判决辅助等。通过提升法律推理的可靠性与可解释性，Legal$Δ$能够为法律从业者提供更为精准的决策支持，进而推动法律人工智能的实际应用和发展。

## 📄 摘要（原文）

> Legal Artificial Intelligence (LegalAI) has achieved notable advances in automating judicial decision-making with the support of Large Language Models (LLMs). However, existing legal LLMs still struggle to generate reliable and interpretable reasoning processes. They often default to fast-thinking behavior by producing direct answers without explicit multi-step reasoning, limiting their effectiveness in complex legal scenarios that demand rigorous justification. To address this challenge, we propose Legal$Δ$, a reinforcement learning framework designed to enhance legal reasoning through chain-of-thought guided information gain. During training, Legal$Δ$ employs a dual-mode input setup-comprising direct answer and reasoning-augmented modes-and maximizes the information gain between them. This encourages the model to acquire meaningful reasoning patterns rather than generating superficial or redundant explanations. Legal$Δ$ follows a two-stage approach: (1) distilling latent reasoning capabilities from a powerful Large Reasoning Model (LRM), DeepSeek-R1, and (2) refining reasoning quality via differential comparisons, combined with a multidimensional reward mechanism that assesses both structural coherence and legal-domain specificity. Experimental results on multiple legal reasoning tasks demonstrate that Legal$Δ$ outperforms strong baselines in both accuracy and interpretability. It consistently produces more robust and trustworthy legal judgments without relying on labeled preference data. All code and data will be released at https://github.com/NEUIR/LegalDelta.

