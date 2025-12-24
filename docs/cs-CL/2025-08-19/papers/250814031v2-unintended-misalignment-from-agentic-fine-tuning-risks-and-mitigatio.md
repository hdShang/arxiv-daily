---
layout: default
title: "Unintended Misalignment from Agentic Fine-Tuning: Risks and Mitigation"
---

# Unintended Misalignment from Agentic Fine-Tuning: Risks and Mitigation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14031" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14031v2</a>
  <a href="https://arxiv.org/pdf/2508.14031.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14031v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14031v2', 'Unintended Misalignment from Agentic Fine-Tuning: Risks and Mitigation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dongyoon Hahm, Taywon Min, Woogyeol Jin, Kimin Lee

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-08-19 (更新: 2025-11-17)

**备注**: Accepted at AAAI 2026 AI Alignment Track, Source code: https://github.com/HahmDY/agentic-ft-safety

---

## 💡 一句话要点

**提出PING方法以解决大语言模型的安全性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `安全性` `微调` `前缀注入` `代理系统` `自然语言处理` `任务执行` `拒绝机制`

## 📋 核心要点

1. 现有方法在微调大型语言模型时，往往忽视了安全性，导致模型可能执行有害任务。
2. 本文提出的PING方法通过在模型响应前添加自然语言前缀，有效引导模型拒绝有害请求。
3. 实验结果显示，PING在多种基准测试中显著提升了模型的安全性和有效性，超越了现有的提示方法。

## 📝 摘要（中文）

随着大型语言模型（LLMs）向具备代理能力的系统演变，它们能够规划并与外部工具互动以解决复杂任务。然而，在针对特定代理任务的微调过程中，安全性问题常常被忽视。本文展示了经过对齐的LLMs在执行代理任务时可能无意中失去对齐，导致执行有害任务的可能性增加。为应对这些安全挑战，提出了前缀注入保护（PING）方法，通过在代理响应前添加自动生成的自然语言前缀，引导其拒绝有害请求，同时保持在良性任务上的表现。实验结果表明，PING显著提高了微调LLM代理的安全性，而不牺牲其有效性。

## 🔬 方法详解

**问题定义**：本文解决的是大型语言模型在微调过程中可能出现的无意对齐问题，导致其在执行代理任务时更容易执行有害任务。现有方法未能有效处理这一安全性隐患。

**核心思路**：PING方法通过在模型的响应前添加自动生成的自然语言前缀，来引导模型拒绝有害请求，同时保持其在良性任务上的表现。这样的设计旨在通过引导机制增强模型的安全性。

**技术框架**：PING的整体架构包括两个主要模块：生成候选前缀和选择最优前缀。首先，生成多个候选前缀，然后通过优化任务表现和拒绝行为来选择最佳前缀。

**关键创新**：PING的核心创新在于其前缀注入机制，通过自然语言前缀的引导，显著改善了模型的拒绝能力，与传统的提示方法相比，提供了更为有效的安全性保障。

**关键设计**：在设计中，PING采用了迭代生成和选择的策略，确保前缀既能提升任务表现，又能有效引导模型拒绝有害请求。具体的参数设置和损失函数设计在实验中经过优化，以达到最佳效果。

## 📊 实验亮点

实验结果表明，PING方法在网络导航和代码生成任务中显著提升了模型的安全性，超越了现有的提示方法。具体而言，PING在多个基准测试中表现出更高的拒绝率和任务有效性，证明了其在安全性和性能上的双重优势。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、自动化客服和其他需要与用户互动的代理系统。通过提高模型的安全性，PING方法能够有效降低模型执行有害任务的风险，提升用户信任度和系统可靠性。未来，该方法可能在更广泛的人工智能应用中发挥重要作用。

## 📄 摘要（原文）

> Beyond simple text generation, Large Language Models (LLMs) have evolved into agentic systems capable of planning and interacting with external tools to solve complex tasks. This evolution involves fine-tuning LLMs on agent-specific tasks to enhance their proficiency. However, safety concerns are frequently overlooked during this fine-tuning process. In this work, we show that aligned LLMs can become unintentionally misaligned, leading to a higher likelihood of executing harmful tasks and a reduced tendency to refuse them when fine-tuned to execute agentic tasks. To address these safety challenges, we propose Prefix INjection Guard (PING), a simple yet effective method that prepends automatically generated natural language prefixes to agent responses, guiding them to refuse harmful requests while preserving performance on benign tasks. Specifically, we introduce an iterative approach that alternates between (1) generating candidate prefixes and (2) selecting those that optimize both task performance and refusal behavior. Experimental results demonstrate that PING significantly enhances the safety of fine-tuned LLM agents without sacrificing their effectiveness. PING consistently outperforms existing prompting approaches across diverse benchmarks in both web navigation and code generation tasks. Our analysis of internal hidden states via linear probes reveals that prefix tokens are crucial for behavior modification, explaining the performance gains. WARNING: This paper contains contents that are unethical or offensive in nature.

