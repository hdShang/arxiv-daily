---
layout: default
title: "Log-Augmented Generation: Scaling Test-Time Reasoning with Reusable Computation"
---

# Log-Augmented Generation: Scaling Test-Time Reasoning with Reusable Computation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14398" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14398v1</a>
  <a href="https://arxiv.org/pdf/2505.14398.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14398v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14398v1', 'Log-Augmented Generation: Scaling Test-Time Reasoning with Reusable Computation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Peter Baile Chen, Yi Zhang, Dan Roth, Samuel Madden, Jacob Andreas, Michael Cafarella

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-05-20

**备注**: Data and code are available at https://peterbaile.github.io/lag/

---

## 💡 一句话要点

**提出日志增强生成框架以提升模型推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `日志增强生成` `推理能力` `大型语言模型` `知识重用` `KV缓存` `智能助手` `自动化客服`

## 📋 核心要点

1. 现有的大型语言模型在推理能力上存在不足，无法有效利用过去的经验进行学习和适应新任务。
2. 本文提出的日志增强生成（LAG）框架，通过重用先前计算和推理，提升模型在新任务中的表现。
3. 实验结果显示，LAG在知识和推理密集型数据集上显著超越了不使用日志的标准系统，提升效果明显。

## 📝 摘要（中文）

尽管人类能够自然地从过去的经验中学习并适应，但大型语言模型（LLMs）及其代理模型在保留先前任务的推理并将其应用于未来上下文方面存在困难。为了解决这一局限性，本文提出了一种新颖的框架——日志增强生成（LAG），该框架在测试时直接重用过去日志中的计算和推理，从而增强模型从先前任务中学习的能力，并在新任务中表现更好，同时保持系统的高效性和可扩展性。具体而言，我们的系统使用键值（KV）缓存表示任务日志，编码先前任务的完整推理上下文，同时仅存储选定子集的KV缓存。当新任务出现时，LAG从相关日志中检索KV值以增强生成。我们的研究表明，该方法显著优于不利用日志的标准代理系统，以及基于反思和KV缓存技术的现有解决方案。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在测试时无法有效利用先前任务推理的问题。现有方法往往依赖反思机制或知识提取，导致效率低下和准确性不足。

**核心思路**：LAG框架通过直接重用先前任务的计算和推理，避免了额外的知识提取步骤，从而提高了模型的学习能力和推理效率。

**技术框架**：LAG系统的整体架构包括任务日志的KV缓存表示、相关日志的KV值检索和生成增强三个主要模块。系统在新任务出现时，通过检索相关日志中的KV值来增强生成过程。

**关键创新**：LAG的核心创新在于直接重用先前的推理和计算，而不是依赖反思机制或额外的知识提取步骤。这一设计使得模型在处理新任务时更加高效和准确。

**关键设计**：在技术细节方面，LAG使用了选择性存储的KV缓存，仅存储与任务相关的子集，确保了系统的高效性。同时，设计了适应性强的检索机制，以便在新任务中快速获取相关信息。

## 📊 实验亮点

实验结果表明，LAG在知识和推理密集型数据集上显著优于不使用日志的标准代理系统，提升幅度达到XX%。与现有基于反思和KV缓存的技术相比，LAG在准确性和效率上均有显著改善，展示了其在实际应用中的巨大潜力。

## 🎯 应用场景

该研究的潜在应用场景包括智能助手、自动化客服、教育辅导等领域，能够帮助系统更好地理解用户需求并提供个性化服务。未来，LAG框架有望在多种复杂任务中实现更高效的推理和决策支持，推动人工智能的进一步发展。

## 📄 摘要（原文）

> While humans naturally learn and adapt from past experiences, large language models (LLMs) and their agentic counterparts struggle to retain reasoning from previous tasks and apply them in future contexts. To address this limitation, we propose a novel framework, log-augmented generation (LAG) that directly reuses prior computation and reasoning from past logs at test time to enhance model's ability to learn from previous tasks and perform better on new, unseen challenges, all while keeping the system efficient and scalable. Specifically, our system represents task logs using key-value (KV) caches, encoding the full reasoning context of prior tasks while storing KV caches for only a selected subset of tokens. When a new task arises, LAG retrieves the KV values from relevant logs to augment generation. Our approach differs from reflection-based memory mechanisms by directly reusing prior reasoning and computations without requiring additional steps for knowledge extraction or distillation. Our method also goes beyond existing KV caching techniques, which primarily target efficiency gains rather than improving accuracy. Experiments on knowledge- and reasoning-intensive datasets demonstrate that our method significantly outperforms standard agentic systems that do not utilize logs, as well as existing solutions based on reflection and KV cache techniques.

