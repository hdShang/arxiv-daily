---
layout: default
title: Iterative Self-Incentivization Empowers Large Language Models as Agentic Searchers
---

# Iterative Self-Incentivization Empowers Large Language Models as Agentic Searchers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20128" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20128v1</a>
  <a href="https://arxiv.org/pdf/2505.20128.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20128v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20128v1', 'Iterative Self-Incentivization Empowers Large Language Models as Agentic Searchers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhengliang Shi, Lingyong Yan, Dawei Yin, Suzan Verberne, Maarten de Rijke, Zhaochun Ren

**分类**: cs.CL

**发布日期**: 2025-05-26

**备注**: Working in process

---

## 💡 一句话要点

**提出EXSEARCH框架以解决LLM在复杂任务中的信息检索问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `信息检索` `自激励学习` `多跳查询` `知识密集型任务`

## 📋 核心要点

1. 现有方法在复杂任务中难以有效利用LLM进行信息检索，尤其是多跳查询和无关内容的问题。
2. 本文提出EXSEARCH框架，通过自激励过程使LLM在推理过程中逐步检索有用信息，提升检索能力。
3. 在多个知识密集型基准测试中，EXSEARCH显著超越基线方法，精确匹配得分提高了7.8%。

## 📝 摘要（中文）

大型语言模型（LLMs）已广泛应用于信息检索领域，但在复杂任务中有效获取准确知识仍然面临挑战，尤其是多跳查询的复杂性和检索内容的无关性。为此，本文提出了EXSEARCH，一个自主搜索框架，使LLM能够在推理过程中通过自激励的方式检索有用信息。该框架采用广义期望最大化算法，LLM在每一步生成多个搜索轨迹并为其分配重要性权重，进而通过加权损失函数进行训练，形成自我激励的循环。实验结果表明，EXSEARCH在四个知识密集型基准测试中显著优于基线方法，精确匹配得分提升7.8%。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在复杂任务中的信息检索能力不足，尤其是在多跳查询和检索内容无关性方面的挑战。现有方法未能有效利用LLM的潜力，导致信息检索效率低下。

**核心思路**：EXSEARCH框架通过自激励的方式，使LLM在推理过程中动态决定检索内容，从而逐步提升其信息检索能力。该设计旨在让模型在每一步都能根据当前推理状态进行有效的信息获取。

**技术框架**：EXSEARCH的整体架构包括三个主要模块：思考（决定检索内容）、搜索（触发外部检索器）和记录（提取支持推理的细粒度证据）。框架采用广义期望最大化算法，分为E步和M步。

**关键创新**：最重要的创新在于自激励循环的设计，LLM通过生成的搜索轨迹进行自我学习，这一过程与传统的训练方式有本质区别，能够有效提升模型的检索能力。

**关键设计**：在E步中，LLM生成多个搜索轨迹并为其分配重要性权重；在M步中，使用加权损失函数对模型进行训练。这种设计确保了模型能够从自身生成的数据中不断学习和改进。

## 📊 实验亮点

在四个知识密集型基准测试中，EXSEARCH框架显著优于基线方法，精确匹配得分提升了7.8%。这一结果表明，EXSEARCH在复杂信息检索任务中具有显著的性能优势，验证了其有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括智能搜索引擎、问答系统和知识管理平台等。EXSEARCH框架能够提升信息检索的准确性和效率，具有广泛的实际价值。未来，该方法可以扩展到更多复杂的知识检索场景，推动相关领域的发展。

## 📄 摘要（原文）

> Large language models (LLMs) have been widely integrated into information retrieval to advance traditional techniques. However, effectively enabling LLMs to seek accurate knowledge in complex tasks remains a challenge due to the complexity of multi-hop queries as well as the irrelevant retrieved content. To address these limitations, we propose EXSEARCH, an agentic search framework, where the LLM learns to retrieve useful information as the reasoning unfolds through a self-incentivized process. At each step, the LLM decides what to retrieve (thinking), triggers an external retriever (search), and extracts fine-grained evidence (recording) to support next-step reasoning. To enable LLM with this capability, EXSEARCH adopts a Generalized Expectation-Maximization algorithm. In the E-step, the LLM generates multiple search trajectories and assigns an importance weight to each; the M-step trains the LLM on them with a re-weighted loss function. This creates a self-incentivized loop, where the LLM iteratively learns from its own generated data, progressively improving itself for search. We further theoretically analyze this training process, establishing convergence guarantees. Extensive experiments on four knowledge-intensive benchmarks show that EXSEARCH substantially outperforms baselines, e.g., +7.8% improvement on exact match score. Motivated by these promising results, we introduce EXSEARCH-Zoo, an extension that extends our method to broader scenarios, to facilitate future work.

