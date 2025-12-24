---
layout: default
title: MA-RAG: Multi-Agent Retrieval-Augmented Generation via Collaborative Chain-of-Thought Reasoning
---

# MA-RAG: Multi-Agent Retrieval-Augmented Generation via Collaborative Chain-of-Thought Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20096" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20096v2</a>
  <a href="https://arxiv.org/pdf/2505.20096.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20096v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20096v2', 'MA-RAG: Multi-Agent Retrieval-Augmented Generation via Collaborative Chain-of-Thought Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Thang Nguyen, Peter Chin, Yu-Wing Tai

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-26 (更新: 2025-10-11)

---

## 💡 一句话要点

**提出MA-RAG框架以解决复杂信息检索中的推理挑战**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多智能体系统` `增强检索生成` `链式思维` `问答系统` `模块化推理` `信息检索` `医疗问答`

## 📋 核心要点

1. 现有的RAG方法通常依赖于端到端微调或孤立组件的增强，难以有效处理复杂信息检索中的推理挑战。
2. MA-RAG通过协调多个专门的智能体，分解任务为多个子任务，采用链式思维提示来实现协作推理。
3. 实验结果表明，MA-RAG在多跳问答基准上表现优异，甚至小型模型也能超越大型独立LLM，展示了其强大的性能提升。

## 📝 摘要（中文）

我们提出了MA-RAG，一个多智能体框架，用于增强检索生成（RAG），旨在解决复杂信息检索任务中的固有模糊性和推理挑战。与传统的RAG方法不同，MA-RAG协调了一组专门的AI智能体，包括规划者、步骤定义者、提取器和问答智能体，每个智能体负责RAG流程的不同阶段。通过将任务分解为查询消歧、证据提取和答案合成等子任务，并通过链式思维提示使智能体能够交流中间推理，MA-RAG逐步优化检索和合成，同时保持模块化可解释性。在多跳和模糊问答基准测试中，MA-RAG显著超越了独立的LLM和现有的RAG方法，展示了其在各个模型规模上的优越性。

## 🔬 方法详解

**问题定义**：本论文旨在解决复杂信息检索任务中的模糊性和推理挑战。现有方法往往无法有效处理多跳推理和信息整合，导致答案准确性不足。

**核心思路**：MA-RAG的核心思路是通过多个专门的智能体协作来分解任务，每个智能体负责特定的子任务，从而提高整体推理能力和答案质量。

**技术框架**：MA-RAG框架包括四个主要模块：规划者负责任务规划，步骤定义者明确每个步骤，提取器从文档中提取证据，问答智能体合成最终答案。智能体之间通过链式思维提示进行沟通，逐步优化检索和合成过程。

**关键创新**：MA-RAG的创新在于其模块化的多智能体协作机制，能够在推理过程中提供可解释的中间步骤，与传统的端到端方法形成鲜明对比。

**关键设计**：在设计中，规划者和提取器智能体被认为是多跳推理的关键，且高容量模型在问答智能体中尤为重要，以有效合成答案。

## 📊 实验亮点

实验结果显示，MA-RAG在多个多跳问答基准上显著优于现有的RAG方法和独立的LLM，尤其是小型LLaMA3-8B模型在引入MA-RAG后超越了更大规模的独立LLM。此外，LLaMA3-70B和GPT-4o-mini在多跳数据集上创造了新的最优结果，验证了该方法的有效性。

## 🎯 应用场景

MA-RAG框架具有广泛的应用潜力，尤其在复杂的问答系统、医疗问答和其他需要高准确性的信息检索领域。其模块化设计使得在特定领域的适应性和可解释性得以增强，未来可为智能助手和信息检索系统提供更可靠的支持。

## 📄 摘要（原文）

> We present MA-RAG, a Multi-Agent framework for Retrieval-Augmented Generation (RAG) that addresses the inherent ambiguities and reasoning challenges in complex information-seeking tasks. Unlike conventional RAG methods that rely on end-to-end fine-tuning or isolated component enhancements, MA-RAG orchestrates a collaborative set of specialized AI agents: Planner, Step Definer, Extractor, and QA Agents, each responsible for a distinct stage of the RAG pipeline. By decomposing tasks into subtasks such as query disambiguation, evidence extraction, and answer synthesis, and enabling agents to communicate intermediate reasoning via chain-of-thought prompting, MA-RAG progressively refines retrieval and synthesis while maintaining modular interpretability. Extensive experiments on multi-hop and ambiguous QA benchmarks, including NQ, HotpotQA, 2WikimQA, and TriviaQA, demonstrate that MA-RAG significantly outperforms standalone LLMs and existing RAG methods across all model scales. Notably, even a small LLaMA3-8B model equipped with MA-RAG surpasses larger standalone LLMs, while larger variants (LLaMA3-70B and GPT-4o-mini) set new state-of-the-art results on challenging multi-hop datasets. Ablation studies reveal that both the planner and extractor agents are critical for multi-hop reasoning, and that high-capacity models are especially important for the QA agent to synthesize answers effectively. Beyond general-domain QA, MA-RAG generalizes to specialized domains such as medical QA, achieving competitive performance against domain-specific models without any domain-specific fine-tuning. Our results highlight the effectiveness of collaborative, modular reasoning in retrieval-augmented systems: MA-RAG not only improves answer accuracy and robustness but also provides interpretable intermediate reasoning steps, establishing a new paradigm for efficient and reliable multi-agent RAG.

