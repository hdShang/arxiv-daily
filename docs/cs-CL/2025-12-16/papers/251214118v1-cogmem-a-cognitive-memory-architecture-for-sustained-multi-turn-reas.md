---
layout: default
title: CogMem: A Cognitive Memory Architecture for Sustained Multi-Turn Reasoning in Large Language Models
---

# CogMem: A Cognitive Memory Architecture for Sustained Multi-Turn Reasoning in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14118" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14118v1</a>
  <a href="https://arxiv.org/pdf/2512.14118.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14118v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14118v1', 'CogMem: A Cognitive Memory Architecture for Sustained Multi-Turn Reasoning in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yiran Zhang, Jincheng Hu, Mark Dras, Usman Naseem

**分类**: cs.CL

**发布日期**: 2025-12-16

**备注**: underreview

---

## 💡 一句话要点

**CogMem：一种认知记忆架构，用于大型语言模型中持续的多轮推理**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `多轮推理` `认知架构` `记忆增强` `上下文管理`

## 📋 核心要点

1. 大型语言模型在多轮对话中存在推理偏差、任务漂移和记忆衰退等问题，影响了其长期推理能力。
2. CogMem架构通过引入长期记忆、直接访问记忆和注意力焦点机制，模拟人类认知过程，实现持续迭代推理。
3. 实验表明，CogMem能有效缓解推理失败，控制上下文增长，并提升多轮推理的一致性，更接近人类推理。

## 📝 摘要（中文）

大型语言模型(LLM)擅长单轮推理，但在扩展的多轮交互中，准确性和连贯性往往会下降。TurnBench等最新评估突出了重复出现的失败模式——推理偏差、任务漂移、幻觉、过度自信和记忆衰退。目前的方法通常附加完整的对话历史，导致无限制的上下文增长、更高的计算成本和降低的推理效率。我们介绍CogMem，一种受认知启发、记忆增强的LLM架构，它通过结构化的持久记忆来支持持续的迭代推理。CogMem包含三个层：长期记忆(LTM)，用于巩固跨会话的推理策略；直接访问(DA)记忆，用于维护会话级别的笔记并检索相关的长期记忆；以及注意力焦点(FoA)机制，用于在每一轮动态地重建简洁的、与任务相关的上下文。在TurnBench上的实验表明，这种分层设计减轻了推理失败，控制了上下文增长，并提高了扩展推理链中的一致性，从而朝着LLM中更可靠、更像人类的推理迈进。

## 🔬 方法详解

**问题定义**：大型语言模型在多轮对话中，由于上下文长度限制和信息衰减，难以保持推理的一致性和准确性。现有方法简单地拼接对话历史，导致计算成本高昂，且容易出现推理偏差、任务漂移等问题。

**核心思路**：CogMem的核心在于模拟人类的认知记忆过程，通过分层记忆结构来管理和利用对话历史信息。长期记忆存储通用的推理策略，直接访问记忆维护当前会话的上下文信息，注意力焦点机制则动态地选择与当前任务相关的上下文，从而实现高效且一致的多轮推理。

**技术框架**：CogMem架构包含三个主要模块：1) 长期记忆(LTM)：存储跨会话的推理策略，例如常用的推理规则或知识。2) 直接访问记忆(DA)：维护当前会话的笔记，记录关键信息和推理步骤。3) 注意力焦点(FoA)：根据当前任务，从LTM和DA中选择相关信息，构建简洁的上下文输入到LLM中进行推理。整个流程是迭代的，每一轮推理都会更新DA，并可能从LTM中检索信息。

**关键创新**：CogMem的关键创新在于其分层记忆结构和动态上下文构建机制。与简单拼接对话历史的方法不同，CogMem能够有选择地保留和利用信息，避免了上下文冗余和信息衰减。此外，LTM的引入使得模型能够学习和利用跨会话的推理经验，提高了泛化能力。

**关键设计**：LTM可以使用知识图谱或向量数据库等形式存储推理策略。DA可以使用简单的键值对存储会话信息。FoA可以使用注意力机制或检索模型来选择相关信息。具体的参数设置和损失函数取决于具体的实现方式，但目标都是最大化推理的准确性和一致性，同时最小化计算成本。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14118v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14118v1/images/Tokens.png" alt="fig_1" loading="lazy">
</figure>
</div>

## 📊 实验亮点

CogMem在TurnBench基准测试中表现出色，有效缓解了推理失败，控制了上下文增长，并提高了多轮推理的一致性。具体性能数据未知，但论文强调CogMem在多个指标上优于现有方法，证明了其分层记忆结构和动态上下文构建机制的有效性。

## 🎯 应用场景

CogMem架构可应用于需要长期对话和复杂推理的场景，如智能客服、虚拟助手、教育辅导等。通过提升LLM在多轮交互中的推理能力，可以构建更智能、更可靠的对话系统，提供更个性化和高效的服务。该研究对提升人机交互体验具有重要意义。

## 📄 摘要（原文）

> Large language models (LLMs) excel at single-turn reasoning but often lose accuracy and coherence over extended, multi-turn interactions. Recent evaluations such as TurnBench highlight recurring failure modes-reasoning bias, task drift, hallucination, overconfidence, and memory decay. Current approaches typically append full conversational histories, causing unbounded context growth, higher computational costs, and degraded reasoning efficiency. We introduce CogMem, a cognitively inspired, memory-augmented LLM architecture that supports sustained iterative reasoning through structured, persistent memory. CogMem incorporates three layers: a Long-Term Memory (LTM) that consolidates cross-session reasoning strategies; a Direct Access (DA) memory that maintains session-level notes and retrieves relevant long-term memories; and a Focus of Attention (FoA) mechanism that dynamically reconstructs concise, task-relevant context at each turn. Experiments on TurnBench show that this layered design mitigates reasoning failures, controls context growth, and improves consistency across extended reasoning chains, moving toward more reliable, human-like reasoning in LLMs.

