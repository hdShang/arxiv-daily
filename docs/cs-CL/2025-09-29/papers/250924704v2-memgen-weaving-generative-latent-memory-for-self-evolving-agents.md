---
layout: default
title: "MemGen: Weaving Generative Latent Memory for Self-Evolving Agents"
---

# MemGen: Weaving Generative Latent Memory for Self-Evolving Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24704" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24704v2</a>
  <a href="https://arxiv.org/pdf/2509.24704.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24704v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24704v2', 'MemGen: Weaving Generative Latent Memory for Self-Evolving Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guibin Zhang, Muxin Fu, Shuicheng Yan

**分类**: cs.CL

**发布日期**: 2025-09-29 (更新: 2025-10-12)

---

## 💡 一句话要点

**MemGen：为自进化Agent构建生成式潜在记忆，提升推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `生成式记忆` `自进化Agent` `LLM Agent` `认知模型` `潜在记忆`

## 📋 核心要点

1. 现有Agent记忆方法，如参数记忆和检索记忆，无法捕捉人类认知中推理与记忆的流畅交织。
2. MemGen通过记忆触发器和记忆编织器，构建动态生成式潜在记忆，实现Agent推理过程中的记忆增强。
3. 实验表明，MemGen在多个基准测试中显著优于现有记忆系统，并涌现出类似人类的记忆能力。

## 📝 摘要（中文）

本文提出了一种名为MemGen的动态生成式记忆框架，旨在赋予Agent类似人类的认知能力。与现有参数记忆和检索记忆的范式不同，MemGen通过一个记忆触发器来监控Agent的推理状态，决定是否显式调用记忆；同时，利用一个记忆编织器，将Agent的当前状态作为刺激，构建一个潜在的token序列作为机器原生的记忆，从而丰富其推理过程。这种方式使得Agent能够在推理过程中回忆和增强潜在记忆，形成记忆和认知紧密交织的循环。在八个基准测试上的大量实验表明，MemGen超越了领先的外部记忆系统，例如ExpeL和AWM，最高提升达38.22%，超过GRPO高达13.44%，并表现出强大的跨领域泛化能力。更重要的是，研究发现，在没有显式监督的情况下，MemGen自发地进化出类似人类的记忆能力，包括计划记忆、程序记忆和工作记忆，这表明其朝着更自然形式的机器认知发展。

## 🔬 方法详解

**问题定义**：现有基于LLM的Agent记忆方法主要分为两类：参数记忆通过调整模型参数来记忆，但缺乏灵活性；检索记忆将经验存储在外部数据库中，但无法实现推理和记忆的紧密结合。这两种方法都难以模拟人类认知中记忆与推理的动态交互过程。

**核心思路**：MemGen的核心思路是构建一种生成式的潜在记忆，Agent可以根据当前状态动态地生成和利用这些记忆。通过将Agent的推理状态作为刺激，生成潜在的token序列，并将这些token序列融入到后续的推理过程中，从而实现记忆和推理的紧密交织。

**技术框架**：MemGen框架包含两个主要模块：记忆触发器（Memory Trigger）和记忆编织器（Memory Weaver）。记忆触发器负责监控Agent的推理状态，判断是否需要调用记忆。如果需要调用记忆，记忆编织器则将Agent的当前状态作为输入，生成一段潜在的token序列，作为Agent的记忆。生成的记忆会被添加到Agent的输入中，从而影响Agent的后续推理过程。

**关键创新**：MemGen的关键创新在于其生成式的记忆构建方式。与传统的检索式记忆不同，MemGen的记忆是动态生成的，可以根据Agent的当前状态进行调整。此外，MemGen的记忆是潜在的token序列，可以直接融入到Agent的推理过程中，实现记忆和推理的无缝衔接。

**关键设计**：记忆触发器可以使用一个简单的分类器来判断是否需要调用记忆。记忆编织器可以使用一个Transformer模型，将Agent的当前状态作为输入，生成一段潜在的token序列。损失函数可以采用标准的语言模型损失函数，目标是最大化生成token序列的概率。具体的网络结构和参数设置需要根据具体的应用场景进行调整。

## 📊 实验亮点

MemGen在八个基准测试中取得了显著的性能提升。例如，在与ExpeL和AWM等领先的外部记忆系统相比，MemGen的性能提升高达38.22%。此外，MemGen还表现出强大的跨领域泛化能力，可以在不同的任务中取得良好的效果。更重要的是，研究发现，在没有显式监督的情况下，MemGen自发地进化出类似人类的记忆能力。

## 🎯 应用场景

MemGen具有广泛的应用前景，例如可以应用于智能对话系统、智能助手、游戏AI等领域。通过赋予Agent更强的记忆能力，可以使其更好地理解用户的意图，做出更合理的决策，并提供更个性化的服务。此外，MemGen还可以用于研究人类认知，例如可以用来模拟人类的记忆过程，从而更好地理解人类的思维方式。

## 📄 摘要（原文）

> Agent memory shapes how Large Language Model (LLM)-powered agents, akin to the human brain, progressively refine themselves through environment interactions. Existing paradigms remain constrained: parametric memory forcibly adjusts model parameters, and retrieval-based memory externalizes experience into structured databases, yet neither captures the fluid interweaving of reasoning and memory that underlies human cognition. To address this gap, we propose MemGen, a dynamic generative memory framework that equips agents with a human-esque cognitive faculty. It consists of a \textit{memory trigger}, which monitors the agent's reasoning state to decide explicit memory invocation, and a \textit{memory weaver}, which takes the agent's current state as stimulus to construct a latent token sequence as machine-native memory to enrich its reasoning. In this way, MemGen enables agents to recall and augment latent memory throughout reasoning, producing a tightly interwoven cycle of memory and cognition. Extensive experiments across eight benchmarks show that MemGen surpasses leading external memory systems such as ExpeL and AWM by up to $38.22\%$, exceeds GRPO by up to $13.44\%$, and exhibits strong cross-domain generalization ability. More importantly, we find that without explicit supervision, MemGen spontaneously evolves distinct human-like memory faculties, including planning memory, procedural memory, and working memory, suggesting an emergent trajectory toward more naturalistic forms of machine cognition.

