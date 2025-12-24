---
layout: default
title: "FeatBench: Evaluating Coding Agents on Feature Implementation for Vibe Coding"
---

# FeatBench: Evaluating Coding Agents on Feature Implementation for Vibe Coding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22237" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22237v1</a>
  <a href="https://arxiv.org/pdf/2509.22237.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22237v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22237v1', 'FeatBench: Evaluating Coding Agents on Feature Implementation for Vibe Coding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haorui Chen, Chengze Li, Jia Li

**分类**: cs.CL, cs.AI, cs.SE

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**FeatBench：提出用于评估代码智能体在振动编码中特征实现能力的新基准**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `代码生成` `大型语言模型` `振动编码` `特征实现` `评估基准`

## 📋 核心要点

1. 现有代码生成评估基准难以评估智能体在“振动编码”中特征实现的能力，缺乏纯自然语言输入和对真实场景的模拟。
2. FeatBench基准专注于特征实现，采用纯自然语言提示，并设计了严格的数据收集和测试流程，涵盖多种应用领域。
3. 实验表明，现有智能体在FeatBench上的表现仍有很大提升空间，最高成功率仅为29.94%，并观察到“激进实现”的现象。

## 📝 摘要（中文）

大型语言模型（LLMs）的快速发展催生了一种名为“振动编码”的新型软件开发模式，用户通过高级自然语言与编码智能体交互。然而，现有的代码生成评估基准不足以评估智能体的振动编码能力。现有基准存在错位，要么需要代码级别的规范，要么狭隘地关注问题解决，忽略了振动编码范式中特征实现的关键场景。为了解决这一差距，我们提出了FeatBench，这是一个专注于特征实现的振动编码新基准。我们的基准具有以下几个关键特征：1. 纯自然语言提示。任务输入完全由抽象的自然语言描述组成，没有任何代码或结构提示。2. 严格且不断发展的数据收集过程。FeatBench建立在多级过滤管道上，以确保质量，并建立在全自动管道上以发展基准，从而减轻数据污染。3. 综合测试用例。每个任务都包括Fail-to-Pass（F2P）和Pass-to-Pass（P2P）测试，以验证正确性并防止回归。4. 多样化的应用领域。该基准包括来自不同领域的存储库，以确保它反映真实世界的场景。我们在FeatBench上评估了两个最先进的智能体框架和四个领先的LLM。我们的评估表明，振动编码范式中的特征实现是一个重大挑战，最高的成功率仅为29.94%。我们的分析还揭示了一种“激进实现”的趋势，这种策略自相矛盾地导致了关键故障和卓越的软件设计。我们发布FeatBench、我们的自动化收集管道以及所有实验结果，以促进进一步的社区研究。

## 🔬 方法详解

**问题定义**：现有代码生成评估基准无法有效评估编码智能体在“振动编码”范式下的特征实现能力。这些基准通常需要代码级别的规范，或者侧重于解决特定问题，而忽略了从高级自然语言描述到完整功能实现的这一关键过程。现有方法的痛点在于缺乏对真实软件开发流程中特征添加场景的模拟和评估。

**核心思路**：FeatBench的核心思路是构建一个专门用于评估编码智能体特征实现能力的基准。该基准采用纯自然语言描述作为输入，模拟真实世界中开发者接收到的需求，并设计了严格的测试用例来验证智能体生成的代码的正确性和鲁棒性。通过这种方式，FeatBench能够更全面地评估智能体在“振动编码”范式下的表现。

**技术框架**：FeatBench的整体框架包括以下几个主要组成部分：1. 数据收集管道：用于从各种开源项目中收集特征实现任务。2. 多级过滤管道：用于确保数据的质量和避免数据污染。3. 测试用例生成器：用于生成Fail-to-Pass (F2P) 和 Pass-to-Pass (P2P) 测试用例。4. 评估器：用于评估编码智能体生成的代码的正确性和鲁棒性。整个流程是自动化的，可以不断发展和更新基准。

**关键创新**：FeatBench最重要的技术创新点在于其专注于评估编码智能体在“振动编码”范式下的特征实现能力。与现有基准相比，FeatBench采用纯自然语言描述作为输入，更加贴近真实世界的软件开发场景。此外，FeatBench还设计了严格的测试用例，包括Fail-to-Pass (F2P) 和 Pass-to-Pass (P2P) 测试，以确保评估的准确性和可靠性。

**关键设计**：FeatBench的关键设计包括：1. 纯自然语言提示：任务输入仅包含抽象的自然语言描述，没有任何代码或结构提示。2. 多级过滤管道：包括语法检查、语义分析和人工审核，以确保数据的质量。3. Fail-to-Pass (F2P) 测试：验证智能体是否能够修复错误的代码。4. Pass-to-Pass (P2P) 测试：验证智能体是否能够保持代码的正确性，防止回归。5. 多样化的应用领域：包括来自不同领域的存储库，以确保基准的通用性。

## 📊 实验亮点

在FeatBench上的实验结果显示，现有最先进的智能体框架和大型语言模型在特征实现方面仍面临挑战，最高成功率仅为29.94%。研究还发现了一种“激进实现”的现象，即智能体倾向于过度实现需求，这可能导致关键错误，但也可能带来更好的软件设计。这些发现为未来的研究提供了重要的方向。

## 🎯 应用场景

FeatBench的研究成果可应用于提升代码智能体在软件开发中的实用性，尤其是在需求理解和特征实现方面。通过FeatBench的评估，可以促进智能体在“振动编码”范式下的发展，降低软件开发的门槛，提高开发效率。未来，FeatBench可以扩展到更多领域，并与其他代码生成基准结合，形成更全面的评估体系。

## 📄 摘要（原文）

> The rapid advancement of Large Language Models (LLMs) has given rise to a novel software development paradigm known as "vibe coding," where users interact with coding agents through high-level natural language. However, existing evaluation benchmarks for code generation inadequately assess an agent's vibe coding capabilities. Existing benchmarks are misaligned, as they either require code-level specifications or focus narrowly on issue-solving, neglecting the critical scenario of feature implementation within the vibe coding paradiam. To address this gap, we propose FeatBench, a novel benchmark for vibe coding that focuses on feature implementation. Our benchmark is distinguished by several key features: 1. Pure Natural Language Prompts. Task inputs consist solely of abstract natural language descriptions, devoid of any code or structural hints. 2. A Rigorous & Evolving Data Collection Process. FeatBench is built on a multi-level filtering pipeline to ensure quality and a fully automated pipeline to evolve the benchmark, mitigating data contamination. 3. Comprehensive Test Cases. Each task includes Fail-to-Pass (F2P) and Pass-to-Pass (P2P) tests to verify correctness and prevent regressions. 4. Diverse Application Domains. The benchmark includes repositories from diverse domains to ensure it reflects real-world scenarios. We evaluate two state-of-the-art agent frameworks with four leading LLMs on FeatBench. Our evaluation reveals that feature implementation within the vibe coding paradigm is a significant challenge, with the highest success rate of only 29.94%. Our analysis also reveals a tendency for "aggressive implementation," a strategy that paradoxically leads to both critical failures and superior software design. We release FeatBench, our automated collection pipeline, and all experimental results to facilitate further community research.

