---
layout: default
title: "Self-GIVE: Associative Thinking from Limited Structured Knowledge for Enhanced Large Language Model Reasoning"
---

# Self-GIVE: Associative Thinking from Limited Structured Knowledge for Enhanced Large Language Model Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.15062" class="toolbar-btn" target="_blank">📄 arXiv: 2505.15062v3</a>
  <a href="https://arxiv.org/pdf/2505.15062.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.15062v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.15062v3', 'Self-GIVE: Associative Thinking from Limited Structured Knowledge for Enhanced Large Language Model Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiashu He, Jinxuan Fan, Bowen Jiang, Ignacio Houine, Dan Roth, Alejandro Ribeiro

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-21 (更新: 2025-10-03)

---

## 💡 一句话要点

**提出Self-GIVE以解决大语言模型推理中的关联思维问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `关联思维` `强化学习` `知识图谱` `生物医学问答` `推理能力` `信息提取`

## 📋 核心要点

1. 现有方法在处理复杂科学问题时，常常面临知识检索不足和推理效率低下的挑战。
2. 本文提出Self-GIVE，通过强化学习实现自动化的关联思维，提升大语言模型的推理能力。
3. 实验结果表明，Self-GIVE显著提高了Qwen2.5模型在生物医学问答任务中的表现，减少了token使用。

## 📝 摘要（中文）

在面对复杂问题时，人类常常通过将问题与已有知识关联来推导合理答案。大语言模型（LLMs）在处理科学问题时也需要这种关联思维，尤其是在检索知识不足以直接回答问题时。Graph Inspired Veracity Extrapolation (GIVE)通过知识图谱来推断结构化知识，但其效率和通用性受到限制。本文提出Self-GIVE，一个基于强化学习的框架，通过自动化关联思维来增强LLMs。Self-GIVE提取结构化信息和实体集，帮助模型与查询概念建立联系。经过在135节点的UMLS知识图谱上微调，Self-GIVE显著提升了Qwen2.5 3B和7B模型在生物医学问答任务中的表现，特别是7B模型在某些任务中超越了GPT3.5 turbo，同时减少了90%以上的token使用。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在科学推理中缺乏有效关联思维的问题。现有的GIVE方法在知识推断时需要构建和修剪大量假设三元组，导致效率低下和通用性不足。

**核心思路**：Self-GIVE通过强化学习框架，自动提取结构化信息和实体集，帮助模型与查询概念建立更有效的联系，从而实现更高效的推理。

**技术框架**：Self-GIVE的整体架构包括信息提取模块、关联思维模块和推理模块。信息提取模块负责从知识图谱中获取相关信息，关联思维模块通过强化学习优化模型的推理过程，推理模块则生成最终答案。

**关键创新**：Self-GIVE的主要创新在于将自动化的关联思维引入到大语言模型中，克服了GIVE方法在知识推断时的高开销和复杂性，使得小型模型也能有效应用。

**关键设计**：在参数设置上，Self-GIVE使用了135节点的UMLS知识图谱，并通过特定的损失函数优化模型的推理能力，确保在减少token使用的同时提升推理准确性。

## 📊 实验亮点

实验结果显示，Self-GIVE在Qwen2.5 3B和7B模型上分别提升了28.5%至71.4%和78.6%至90.5%的性能，尤其是7B模型在某些任务中超越了GPT3.5 turbo，同时token使用减少超过90%。

## 🎯 应用场景

Self-GIVE的研究成果在生物医学问答、科学研究和知识检索等领域具有广泛的应用潜力。通过提升大语言模型的推理能力，该方法能够帮助研究人员更有效地获取和利用知识，推动科学发现和技术进步。

## 📄 摘要（原文）

> When addressing complex questions that require new information, people often associate the question with existing knowledge to derive a sensible answer. For instance, when evaluating whether melatonin aids insomnia, one might associate "hormones helping mental disorders" with "melatonin being a hormone and insomnia a mental disorder" to complete the reasoning. Large Language Models (LLMs) also require such associative thinking, particularly in resolving scientific inquiries when retrieved knowledge is insufficient and does not directly answer the question. Graph Inspired Veracity Extrapolation (GIVE) addresses this by using a knowledge graph (KG) to extrapolate structured knowledge. However, it involves the construction and pruning of many hypothetical triplets, which limits efficiency and generalizability. We propose Self-GIVE, a retrieve-RL framework that enhances LLMs with automatic associative thinking through reinforcement learning. Self-GIVE extracts structured information and entity sets to assist the model in linking to the queried concepts. We address GIVE's key limitations: (1) extensive LLM calls and token overhead for knowledge extrapolation, (2) difficulty in deploying on smaller LLMs (3B or 7B) due to complex instructions, and (3) inaccurate knowledge from LLM pruning. Specifically, after fine-tuning using self-GIVE with a 135 node UMLS KG, it improves the performance of the Qwen2.5 3B and 7B models by up to $\textbf{28.5%$\rightarrow$71.4%}$ and $\textbf{78.6$\rightarrow$90.5%}$ in samples $\textbf{unseen}$ in challenging biomedical QA tasks. In particular, Self-GIVE allows the 7B model to match or outperform GPT3.5 turbo with GIVE, while cutting token usage by over 90%. Self-GIVE enhances the scalable integration of structured retrieval and reasoning with associative thinking.

