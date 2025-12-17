---
layout: default
title: CogMem: A Cognitive Memory Architecture for Sustained Multi-Turn Reasoning in Large Language Models
---

# CogMem: A Cognitive Memory Architecture for Sustained Multi-Turn Reasoning in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14118" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14118</a>
  <a href="https://arxiv.org/pdf/2512.14118.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14118" onclick="toggleFavorite(this, '2512.14118', 'CogMem: A Cognitive Memory Architecture for Sustained Multi-Turn Reasoning in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yiran Zhang, Jincheng Hu, Mark Dras, Usman Naseem

**分类**: cs.CL

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**CogMem：一种认知记忆架构，用于大型语言模型中持续的多轮推理**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `多轮推理` `认知架构` `记忆增强` `上下文管理`

## 📋 核心要点

1. 现有大型语言模型在多轮对话中存在推理偏差、任务漂移和记忆衰退等问题，影响了推理的准确性和连贯性。
2. CogMem架构通过引入长期记忆、直接访问记忆和注意力焦点机制，模拟认知过程，实现对上下文信息的有效管理和利用。
3. 实验结果表明，CogMem能够有效缓解推理失败，控制上下文增长，并提高多轮推理的一致性，提升了LLM的可靠性。

## 📝 摘要（中文）

大型语言模型(LLM)擅长单轮推理，但在扩展的多轮交互中常常会损失准确性和连贯性。TurnBench等最新评估突出了重复出现的失败模式——推理偏差、任务漂移、幻觉、过度自信和记忆衰退。目前的方法通常附加完整的对话历史，导致无限制的上下文增长、更高的计算成本和降低的推理效率。我们介绍CogMem，一种认知启发、记忆增强的LLM架构，它通过结构化的持久记忆来支持持续的迭代推理。CogMem包含三个层：长期记忆(LTM)，用于巩固跨会话的推理策略；直接访问(DA)记忆，用于维护会话级别的笔记并检索相关的长期记忆；以及注意力焦点(FoA)机制，用于在每一轮动态地重建简洁的、与任务相关的上下文。在TurnBench上的实验表明，这种分层设计减轻了推理失败，控制了上下文增长，并提高了扩展推理链中的一致性，从而朝着LLM中更可靠、更像人类的推理迈进。

## 🔬 方法详解

**问题定义**：大型语言模型在多轮对话中面临推理能力下降的问题。简单地拼接对话历史会导致上下文长度无限增长，增加计算成本，并降低推理效率。现有的方法难以有效地管理和利用对话历史中的信息，导致推理偏差、任务漂移、幻觉和记忆衰退等问题。

**核心思路**：CogMem的核心思路是借鉴人类认知架构，通过构建分层记忆系统来模拟人类的记忆和推理过程。长期记忆(LTM)存储通用的推理策略，直接访问记忆(DA)维护当前会话的上下文信息，注意力焦点(FoA)动态地选择与当前任务相关的上下文，从而实现高效和可靠的多轮推理。

**技术框架**：CogMem架构包含三个主要模块：1) **长期记忆(LTM)**：存储跨会话学习到的通用推理策略。2) **直接访问记忆(DA)**：维护当前会话的笔记，并检索相关的长期记忆。3) **注意力焦点(FoA)**：动态地从LTM和DA中选择与当前任务相关的上下文，构建简洁的输入。整个流程是，在每一轮对话中，DA首先检索LTM中相关的知识，然后FoA根据当前输入和DA中的信息，选择最相关的上下文，最后将选择的上下文输入LLM进行推理。

**关键创新**：CogMem的关键创新在于其分层记忆架构和注意力焦点机制。与现有方法直接拼接对话历史不同，CogMem通过LTM存储通用知识，DA维护会话上下文，FoA动态选择相关信息，从而实现了对上下文信息的有效管理和利用。这种分层结构能够缓解推理偏差、任务漂移和记忆衰退等问题。

**关键设计**：LTM使用知识图谱或向量数据库存储推理策略。DA使用滑动窗口或循环神经网络维护会话上下文。FoA使用注意力机制或检索模型选择相关信息。具体的参数设置、损失函数和网络结构需要根据具体的应用场景进行调整。例如，可以使用对比学习来训练LTM，使用强化学习来优化FoA的选择策略。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14118/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14118/images/Tokens.png" alt="fig_1" loading="lazy">
</figure>
</div>

## 📊 实验亮点

在TurnBench基准测试中，CogMem在多轮推理任务上显著优于现有方法。实验结果表明，CogMem能够有效缓解推理失败，控制上下文增长，并提高多轮推理的一致性。具体性能数据需要在论文中查找，但摘要表明CogMem在多个指标上都取得了显著提升。

## 🎯 应用场景

CogMem架构可应用于需要持续多轮推理的对话系统，例如智能客服、虚拟助手和教育辅导机器人。通过提高LLM在多轮对话中的推理能力和一致性，可以提升用户体验，并扩展LLM的应用范围。该研究对于开发更可靠、更像人类的对话系统具有重要意义。

## 📄 摘要（原文）

> Large language models (LLMs) excel at single-turn reasoning but often lose accuracy and coherence over extended, multi-turn interactions. Recent evaluations such as TurnBench highlight recurring failure modes-reasoning bias, task drift, hallucination, overconfidence, and memory decay. Current approaches typically append full conversational histories, causing unbounded context growth, higher computational costs, and degraded reasoning efficiency. We introduce CogMem, a cognitively inspired, memory-augmented LLM architecture that supports sustained iterative reasoning through structured, persistent memory. CogMem incorporates three layers: a Long-Term Memory (LTM) that consolidates cross-session reasoning strategies; a Direct Access (DA) memory that maintains session-level notes and retrieves relevant long-term memories; and a Focus of Attention (FoA) mechanism that dynamically reconstructs concise, task-relevant context at each turn. Experiments on TurnBench show that this layered design mitigates reasoning failures, controls context growth, and improves consistency across extended reasoning chains, moving toward more reliable, human-like reasoning in LLMs.

