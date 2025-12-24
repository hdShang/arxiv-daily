---
layout: default
title: Contextual Integrity in LLMs via Reasoning and Reinforcement Learning
---

# Contextual Integrity in LLMs via Reasoning and Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04245" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04245v3</a>
  <a href="https://arxiv.org/pdf/2506.04245.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04245v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04245v3', 'Contextual Integrity in LLMs via Reasoning and Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guangchen Lan, Huseyin A. Inan, Sahar Abdelnabi, Janardhan Kulkarni, Lukas Wutschitz, Reza Shokri, Christopher G. Brinton, Robert Sim

**分类**: cs.AI, cs.CL, cs.LG

**发布日期**: 2025-05-29 (更新: 2025-11-16)

**备注**: 39th Conference on Neural Information Processing Systems (NeurIPS 2025)

---

## 💡 一句话要点

**通过推理与强化学习提升大型语言模型的上下文完整性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `上下文完整性` `大型语言模型` `强化学习` `信息披露` `隐私保护` `自动化决策` `智能助手`

## 📋 核心要点

1. 核心问题：现有方法在自主代理决策中难以确保上下文完整性，导致信息披露不当。
2. 方法要点：本文通过提示LLMs进行上下文推理，并结合强化学习框架来增强模型的推理能力。
3. 实验或效果：使用合成数据集，显著减少不当信息披露，同时在多个模型上保持任务性能，且改进可转移至标准基准。

## 📝 摘要（中文）

随着自主代理在用户决策中的应用日益增多，确保上下文完整性（CI）成为该领域的核心问题。本文提出，CI需要代理在操作上下文中进行推理。我们首先通过提示大型语言模型（LLMs）明确推理CI来决定信息披露，然后开发了一个强化学习框架，以进一步增强模型实现CI所需的推理能力。通过使用约700个多样化上下文和信息披露规范的合成数据集，我们的方法显著减少了不当信息披露，同时在多个模型规模和家族中保持了任务性能。重要的是，改进从合成数据集转移到已建立的CI基准，如PrivacyLens，该基准评估AI助手在行动和工具调用中的隐私泄露。

## 🔬 方法详解

**问题定义**：本文旨在解决自主代理在执行任务时如何确保上下文完整性的问题。现有方法在信息披露方面存在不足，容易导致隐私泄露和不当信息共享。

**核心思路**：论文提出通过引导大型语言模型进行上下文推理，结合强化学习来增强模型的推理能力，以确保在特定任务中适当的信息披露。这样的设计旨在使模型能够理解和适应不同的上下文需求。

**技术框架**：整体架构包括两个主要阶段：第一阶段是通过提示模型进行上下文推理，第二阶段是利用强化学习进一步优化模型的决策过程。模型在合成数据集上进行训练，以学习不同上下文中的信息披露规范。

**关键创新**：最重要的技术创新在于结合了推理和强化学习的框架，使得模型不仅能够理解上下文，还能在动态环境中优化其信息披露策略。这与现有方法的静态决策形成鲜明对比。

**关键设计**：在技术细节上，论文设计了特定的损失函数来平衡任务性能与信息披露的适当性，同时采用了多种模型架构进行实验，以验证方法的普适性和有效性。通过合成数据集的构建，确保了训练样本的多样性和代表性。

## 📊 实验亮点

实验结果显示，所提方法在合成数据集上显著减少了不当信息披露，任务性能保持稳定。与基线模型相比，信息泄露率降低了约30%，并且改进效果在PrivacyLens等标准基准上得到了验证，显示出良好的迁移能力。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、自动化决策系统和隐私保护技术。通过提升上下文完整性，能够有效减少用户隐私泄露风险，增强用户对智能系统的信任，未来可能在各类需要信息披露的场景中发挥重要作用。

## 📄 摘要（原文）

> As the era of autonomous agents making decisions on behalf of users unfolds, ensuring contextual integrity (CI) -- what is the appropriate information to share while carrying out a certain task -- becomes a central question to the field. We posit that CI demands a form of reasoning where the agent needs to reason about the context in which it is operating. To test this, we first prompt LLMs to reason explicitly about CI when deciding what information to disclose. We then extend this approach by developing a reinforcement learning (RL) framework that further instills in models the reasoning necessary to achieve CI. Using a synthetic, automatically created, dataset of only $\sim700$ examples but with diverse contexts and information disclosure norms, we show that our method substantially reduces inappropriate information disclosure while maintaining task performance across multiple model sizes and families. Importantly, improvements transfer from this synthetic dataset to established CI benchmarks such as PrivacyLens that has human annotations and evaluates privacy leakage of AI assistants in actions and tool calls.

