---
layout: default
title: "Meta-Policy Reflexion: Reusable Reflective Memory and Rule Admissibility for Resource-Efficient LLM Agent"
---

# Meta-Policy Reflexion: Reusable Reflective Memory and Rule Admissibility for Resource-Efficient LLM Agent

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03990" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03990v2</a>
  <a href="https://arxiv.org/pdf/2509.03990.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03990v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03990v2', 'Meta-Policy Reflexion: Reusable Reflective Memory and Rule Admissibility for Resource-Efficient LLM Agent')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chunlong Wu, Ye Luo, Zhibo Qu, Min Wang

**分类**: cs.AI

**发布日期**: 2025-09-04 (更新: 2025-09-08)

---

## 💡 一句话要点

**提出Meta-Policy Reflexion，提升LLM Agent在复杂任务中的效率与泛化性**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `LLM Agent` `反思学习` `元策略` `知识重用` `规则约束`

## 📋 核心要点

1. 现有LLM Agent在复杂任务中存在重复失败、探索效率低和跨任务泛化能力弱等问题。
2. Meta-Policy Reflexion (MPR) 将LLM反思提炼为可重用的Meta-Policy Memory，通过软解码引导和硬规则约束提升Agent性能。
3. 实验表明，MPR在执行准确性和鲁棒性方面优于现有方法，并能有效提升Agent的稳定性。

## 📝 摘要（中文）

大型语言模型（LLM）Agent在单任务上表现出色，但常出现重复失败、探索效率低和跨任务适应性有限等问题。现有的反思策略（如Reflexion、ReAct）虽然能改善单次行为，但通常产生短暂且特定于任务的轨迹，无法跨任务重用。基于强化学习的方法虽然可以产生可迁移的策略，但需要大量的参数更新和计算。本文提出了Meta-Policy Reflexion（MPR）：一种混合框架，将LLM生成的反思结果整合到结构化的、类似谓词的Meta-Policy Memory（MPM）中，并通过软记忆引导解码和硬规则可采纳性检查（HAC）两种互补机制在推理时应用该记忆。MPR（i）无需模型权重更新即可外部化可重用的纠正知识，（ii）强制执行领域约束以减少不安全或无效的操作，并且（iii）保留了基于语言的反思的适应性。本文形式化了MPM表示，提出了更新和解码算法，并在基于文本的Agent环境中验证了该方法（基于AlfWorld）。实验结果表明，与Reflexion基线相比，执行准确性和鲁棒性得到了持续提高；规则可采纳性进一步提高了稳定性。本文分析了解释这些收益的机制，讨论了可扩展性和失败模式，并概述了多模态和多Agent扩展的未来方向。

## 🔬 方法详解

**问题定义**：现有LLM Agent在复杂任务中表现出重复失败，低效探索，以及有限的跨任务适应性。现有的反思方法（如Reflexion）产生的经验是短暂的，无法跨任务重用。强化学习方法虽然可以学习可迁移的策略，但需要大量的计算资源和参数更新。因此，如何让LLM Agent能够有效地利用历史经验，避免重复犯错，并具备更强的泛化能力是一个关键问题。

**核心思路**：MPR的核心思路是将LLM生成的反思知识提炼并存储到Meta-Policy Memory (MPM) 中，该MPM以结构化的、类似谓词的形式存储知识。在推理阶段，MPR通过两种机制利用MPM：软记忆引导解码和硬规则可采纳性检查(HAC)。软记忆引导解码通过调整LLM的输出概率分布，鼓励Agent选择更符合历史经验的行为。硬规则可采纳性检查则直接禁止Agent选择违反领域约束或已知错误的行为。

**技术框架**：MPR框架主要包含以下几个模块：1) LLM Agent：负责与环境交互，生成动作序列。2) Reflection Module：在Agent执行失败后，利用LLM生成反思，总结失败原因和改进策略。3) Meta-Policy Memory (MPM)：存储从反思中提取的知识，以结构化的形式表示。4) Soft Memory-Guided Decoding：利用MPM中的知识调整LLM的输出概率分布。5) Hard Rule Admissibility Checks (HAC)：根据MPM中的规则，过滤掉不合法的动作。整个流程是：Agent与环境交互 -> 失败后进行反思 -> 反思结果更新MPM -> 下次交互时，利用MPM进行软解码引导和硬规则检查。

**关键创新**：MPR的关键创新在于：1) 提出了Meta-Policy Memory (MPM)，一种结构化的知识表示方法，能够有效地存储和重用LLM生成的反思知识。2) 结合了软记忆引导解码和硬规则可采纳性检查两种机制，既能利用历史经验指导Agent的行为，又能强制执行领域约束，避免Agent犯错。3) 无需模型权重更新即可外部化可重用的纠正知识，降低了计算成本。

**关键设计**：MPM采用类似谓词的结构化表示，例如“如果Agent在X情况下执行了动作Y导致失败，那么下次在X情况下不要执行动作Y”。软记忆引导解码通过调整LLM的输出概率分布来实现，具体方法是根据MPM中知识的相关性，对LLM的输出logits进行加权。硬规则可采纳性检查则直接根据MPM中的规则，过滤掉不合法的动作。具体的参数设置和损失函数在论文中没有详细描述，属于未知信息。

## 📊 实验亮点

实验结果表明，MPR在AlfWorld环境中，与Reflexion基线相比，执行准确性和鲁棒性得到了持续提高。规则可采纳性进一步提高了Agent的稳定性。具体的数据提升幅度在论文中没有明确给出，属于未知信息。但总体而言，实验验证了MPR的有效性。

## 🎯 应用场景

MPR具有广泛的应用前景，可以应用于各种需要智能Agent进行决策的任务中，例如游戏AI、机器人控制、自动化客服等。通过学习和重用历史经验，MPR可以显著提高Agent的效率和鲁棒性，使其能够更好地适应复杂和动态的环境。未来的研究可以将MPR扩展到多模态和多Agent场景，进一步提升其应用价值。

## 📄 摘要（原文）

> Large language model (LLM) agents achieve impressive single-task performance but commonly exhibit repeated failures, inefficient exploration, and limited cross-task adaptability. Existing reflective strategies (e.g., Reflexion, ReAct) improve per-episode behavior but typically produce ephemeral, task-specific traces that are not reused across tasks. Reinforcement-learning based alternatives can produce transferable policies but require substantial parameter updates and compute. In this work we introduce Meta-Policy Reflexion (MPR): a hybrid framework that consolidates LLM-generated reflections into a structured, predicate-like Meta-Policy Memory (MPM) and applies that memory at inference time through two complementary mechanisms soft memory-guided decoding and hard rule admissibility checks(HAC). MPR (i) externalizes reusable corrective knowledge without model weight updates, (ii) enforces domain constraints to reduce unsafe or invalid actions, and (iii) retains the adaptability of language-based reflection. We formalize the MPM representation, present algorithms for update and decoding, and validate the approach in a text-based agent environment following the experimental protocol described in the provided implementation (AlfWorld-based). Empirical results reported in the supplied material indicate consistent gains in execution accuracy and robustness when compared to Reflexion baselines; rule admissibility further improves stability. We analyze mechanisms that explain these gains, discuss scalability and failure modes, and outline future directions for multimodal and multi-agent extensions.

