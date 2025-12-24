---
layout: default
title: "Dynamic Context Tuning for Retrieval-Augmented Generation: Enhancing Multi-Turn Planning and Tool Adaptation"
---

# Dynamic Context Tuning for Retrieval-Augmented Generation: Enhancing Multi-Turn Planning and Tool Adaptation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11092" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11092v2</a>
  <a href="https://arxiv.org/pdf/2506.11092.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11092v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11092v2', 'Dynamic Context Tuning for Retrieval-Augmented Generation: Enhancing Multi-Turn Planning and Tool Adaptation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jubin Abhishek Soni, Amit Anand, Rajesh Kumar Pandey, Aniket Abhishek Soni

**分类**: cs.CL, cs.AI, cs.HC

**发布日期**: 2025-06-05 (更新: 2025-07-19)

**备注**: We are withdrawing the submission in order to thoroughly revise the work

---

## 💡 一句话要点

**提出动态上下文调优以解决多轮对话和工具适应问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `动态上下文调优` `检索增强生成` `多轮对话` `工具适应` `大型语言模型` `医疗助手` `智能家居`

## 📋 核心要点

1. 现有的RAG系统通常只能处理静态的单轮交互，无法适应用户意图和工具环境的动态变化。
2. 本文提出动态上下文调优（DCT）框架，通过集成上下文缓存和动态工具选择，支持多轮对话。
3. 实验结果显示，DCT在计划准确性上提高了14%，幻觉减少了37%，且成本显著低于GPT-4。

## 📝 摘要（中文）

检索增强生成（RAG）显著提升了大型语言模型（LLMs）的能力，通过将其输出与外部工具和知识源结合。然而，现有的RAG系统通常局限于静态的单轮交互，无法适应医疗和智能家居等动态领域。本文提出了一种轻量级框架——动态上下文调优（DCT），支持多轮对话和不断变化的工具环境，无需重新训练。DCT集成了基于注意力的上下文缓存、基于LoRA的检索和高效的上下文压缩。实验结果表明，DCT在计划准确性上提高了14%，并减少了37%的幻觉，同时以显著更低的成本匹配GPT-4的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决现有RAG系统在动态领域（如医疗和智能家居）中无法适应用户意图和工具环境变化的问题。现有方法通常局限于静态单轮交互，无法有效处理多轮对话和工具适应性。

**核心思路**：提出动态上下文调优（DCT）框架，通过集成注意力机制的上下文缓存和基于LoRA的动态工具选择，支持多轮对话而无需重新训练。

**技术框架**：DCT框架主要包括三个模块：1) 上下文缓存，跟踪相关的历史信息；2) 动态工具选择，基于LoRA技术选择领域特定工具；3) 上下文压缩，确保输入在LLM的上下文限制内。

**关键创新**：DCT的核心创新在于其动态适应能力，能够在不重新训练的情况下，支持多轮对话和新工具的引入，这与现有方法的静态特性形成鲜明对比。

**关键设计**：DCT采用了基于注意力的上下文缓存机制，能够有效存储和检索历史信息，同时通过LoRA技术实现高效的工具选择，确保系统在动态环境中的灵活性和适应性。

## 📊 实验亮点

实验结果表明，DCT在计划准确性上提高了14%，幻觉减少了37%。与GPT-4相比，DCT在性能上相当，但成本显著降低，展示了其在实际应用中的优势。

## 🎯 应用场景

该研究的潜在应用领域包括医疗助手、智能家居管理和客户服务等动态环境。DCT框架的灵活性和适应性使其能够在不断变化的用户需求和工具环境中提供高效的支持，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Retrieval-Augmented Generation (RAG) has significantly advanced large language models (LLMs) by grounding their outputs in external tools and knowledge sources. However, existing RAG systems are typically constrained to static, single-turn interactions with fixed toolsets, making them ill-suited for dynamic domains such as healthcare and smart homes, where user intent, available tools, and contextual factors evolve over time. We present Dynamic Context Tuning (DCT), a lightweight framework that extends RAG to support multi-turn dialogue and evolving tool environments without requiring retraining. DCT integrates an attention-based context cache to track relevant past information, LoRA-based retrieval to dynamically select domain-specific tools, and efficient context compression to maintain inputs within LLM context limits. Experiments on both synthetic and real-world benchmarks show that DCT improves plan accuracy by 14% and reduces hallucinations by 37%, while matching GPT-4 performance at significantly lower cost. Furthermore, DCT generalizes to previously unseen tools, enabling scalable and adaptable AI assistants across a wide range of dynamic environments.

