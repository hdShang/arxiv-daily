---
layout: default
title: "Agnostics: Learning to Code in Any Programming Language via Reinforcement with a Universal Learning Environment"
---

# Agnostics: Learning to Code in Any Programming Language via Reinforcement with a Universal Learning Environment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04865" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04865v1</a>
  <a href="https://arxiv.org/pdf/2508.04865.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04865v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04865v1', 'Agnostics: Learning to Code in Any Programming Language via Reinforcement with a Universal Learning Environment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aleksander Boruch-Gruszecki, Yangtian Zi, Zixuan Wu, Tejas Oberoi, Carolyn Jane Anderson, Joydeep Biswas, Arjun Guha

**分类**: cs.LG, cs.PL

**发布日期**: 2025-08-06

**备注**: 18 pages, 19 figures. For artifacts, see https://agnostics.abgru.me

---

## 💡 一句话要点

**提出Agnostics以解决低资源编程语言的后训练问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `低资源编程语言` `后训练` `强化学习` `语言无关` `模型性能提升`

## 📋 核心要点

1. 现有大型语言模型在低资源编程语言上表现不佳，缺乏足够的训练数据和后训练基础设施。
2. Agnostics通过语言无关的后训练管道，利用外部可观察行为评估代码，简化了多语言支持的工程需求。
3. 在五种低资源语言上，Agnostics显著提升了模型性能，达到了新的状态-of-the-art结果。

## 📝 摘要（中文）

大型语言模型（LLMs）在高资源语言（如Python和JavaScript）上表现优异，但在低资源语言上却面临挑战。除了预训练数据的短缺，后训练过程也成为瓶颈。本文提出Agnostics，一个语言无关的后训练管道，通过仅依据代码的外部可观察行为来评估代码，从而消除每种语言的工程需求。具体而言，Agnostics利用LLM将现有单元测试数据集重写为I/O格式，提供简短配置以指导编译和运行目标语言，并在稳健的代码执行环境中应用可验证奖励的强化学习。该方法在五种低资源语言上取得了显著提升，推动了模型性能的进步。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在低资源编程语言上的后训练瓶颈，现有方法需要为每种语言构建新的数据集和测试框架，效率低下。

**核心思路**：Agnostics的核心思路是通过外部可观察行为来评估代码，避免了每种语言的特定工程需求，从而实现语言无关的后训练。

**技术框架**：Agnostics的整体架构包括三个主要模块：首先，使用LLM将现有的单元测试数据集转换为I/O格式；其次，提供简短的配置文件以指导如何编译和运行目标语言；最后，在稳健的代码执行环境中应用可验证奖励的强化学习。

**关键创新**：Agnostics的最大创新在于其语言无关的后训练管道，能够通过单一验证器测试任何语言的解决方案，与现有方法相比，显著降低了工程复杂性。

**关键设计**：在设计中，Agnostics使用了简短的YAML配置文件来指导训练过程，确保了灵活性和可扩展性，同时在强化学习中采用了可验证奖励机制，以提高模型的学习效率。

## 📊 实验亮点

在五种低资源语言（Lua、Julia、R、OCaml和Fortran）上，Agnostics显著提升了Qwen-3 4B模型的性能，使其与其他16B-70B开源模型相媲美。此外，对于≤16B参数模型，Agnostics在MultiPL-E和新引入的多语言版本LiveCodeBench上设定了新的state-of-the-art通过率。

## 🎯 应用场景

Agnostics的研究成果具有广泛的应用潜力，特别是在科学和工程领域中，能够支持多种低资源编程语言的开发和测试。通过简化后训练过程，该方法可以加速新语言的模型适应，促进跨语言编程的研究与实践。

## 📄 摘要（原文）

> Large language models (LLMs) already excel at writing code in high-resource languages such as Python and JavaScript, yet stumble on low-resource languages that remain essential to science and engineering. Besides the obvious shortage of pre-training data, post-training itself is a bottleneck: every new language seems to require new datasets, test harnesses, and reinforcement-learning (RL) infrastructure.
>   We introduce Agnostics, a language-agnostic post-training pipeline that eliminates this per-language engineering. The key idea is to judge code solely by its externally observable behavior, so a single verifier can test solutions written in any language. Concretely, we (i) use an LLM to rewrite existing unit-test datasets into an I/O format, (ii) supply a short configuration that tells the verifier how to compile and run a target language, and (iii) apply reinforcement learning with verifiable rewards (RLVR) in a robust code execution environment.
>   Applied to five low-resource languages--Lua, Julia, R, OCaml, and Fortran--Agnostics (1) improves Qwen-3 4B to performance that rivals other 16B-70B open-weight models; (2) scales cleanly to larger and diverse model families (Qwen-3 8B, DeepSeek Coder 6.7B Instruct, Phi 4 Mini); and (3) for ${\le} 16$B parameter models, sets new state-of-the-art pass@1 results on MultiPL-E and a new multi-language version LiveCodeBench that we introduce.
>   We will release the language-agnostic training datasets (Ag-MBPP-X, Ag-Codeforces-X, Ag-LiveCodeBench-X), training code, and ready-to-use configurations, making RL post-training in any programming language as simple as editing a short YAML file.

