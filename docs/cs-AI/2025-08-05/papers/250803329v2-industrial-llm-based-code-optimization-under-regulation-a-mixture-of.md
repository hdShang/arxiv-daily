---
layout: default
title: "Industrial LLM-based Code Optimization under Regulation: A Mixture-of-Agents Approach"
---

# Industrial LLM-based Code Optimization under Regulation: A Mixture-of-Agents Approach

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03329" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03329v2</a>
  <a href="https://arxiv.org/pdf/2508.03329.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03329v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03329v2', 'Industrial LLM-based Code Optimization under Regulation: A Mixture-of-Agents Approach')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mari Ashiga, Vardan Voskanyan, Fateme Dinmohammadi, Jingzhi Gong, Paul Brookes, Matthew Truscott, Rafail Giavrimis, Mike Basios, Leslie Kanthan, Wei Jie

**分类**: cs.SE, cs.AI

**发布日期**: 2025-08-05 (更新: 2025-08-06)

**备注**: Submitted to ASE'25 Industry Showcase

---

## 💡 一句话要点

**提出混合代理方法以解决受监管环境下的代码优化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `代码优化` `混合代理` `遗传算法` `受监管环境` `软件性能工程` `开源模型`

## 📋 核心要点

1. 现有的代码优化方法在受监管环境中受到数据隐私和合规性的限制，难以实现高效的代码优化。
2. 本文提出了一种混合代理（MoA）方法，利用多个专门的LLMs合成代码，旨在提高优化效果和效率。
3. 实验结果表明，MoA在开放源代码模型中实现了14.3%至22.2%的成本节约和28.6%至32.2%的优化时间提升，优于传统方法。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）在代码优化方面的进展使得工业平台能够以前所未有的规模和速度自动化软件性能工程。然而，受监管行业的组织面临严格的数据隐私和合规要求，限制了可使用的LLMs，给高质量代码优化带来了挑战。本文提出了一种混合代理（MoA）方法，通过多个专门的LLMs直接合成代码，并与基于遗传算法的系统进行比较。研究表明，MoA在开放源代码模型中表现优异，能够实现14.3%至22.2%的成本节约和28.6%至32.2%的优化时间提升，为在生产环境中平衡合规性与优化性能提供了可行的指导。

## 🔬 方法详解

**问题定义**：本文旨在解决受监管环境下的代码优化问题，现有方法因合规性限制而无法有效利用商业LLMs，导致优化效果不佳。

**核心思路**：提出混合代理（MoA）方法，通过整合多个专门的LLMs来合成代码，克服单一模型的局限性，从而提高优化质量和效率。

**技术框架**：整体架构包括多个LLMs的组合与协同工作，首先对输入代码进行分析，然后通过不同模型生成代码变体，最后选择最佳方案。

**关键创新**：首次将MoA应用于工业代码优化，提供了实证数据，显示在开放源代码模型中显著提升了优化性能。

**关键设计**：在模型选择上，结合了多个开源LLMs，并通过遗传算法优化组合，确保在合规性与性能之间取得平衡。具体参数设置和损失函数设计旨在最大化优化效果。

## 📊 实验亮点

实验结果显示，MoA方法在开放源代码模型中实现了14.3%至22.2%的成本节约和28.6%至32.2%的优化时间提升，相较于传统的遗传算法和单一LLM优化器表现更为优越，生成了超过8700个代码变体，验证了其在工业应用中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括软件开发、云计算和金融科技等受监管行业。通过提供高效的代码优化方案，帮助企业在遵循合规要求的同时提升软件性能，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Recent advancements in Large Language Models (LLMs) for code optimization have enabled industrial platforms to automate software performance engineering at unprecedented scale and speed. Yet, organizations in regulated industries face strict constraints on which LLMs they can use - many cannot utilize commercial models due to data privacy regulations and compliance requirements, creating a significant challenge for achieving high-quality code optimization while maintaining cost-effectiveness. We address this by implementing a Mixture-of-Agents (MoA) approach that directly synthesizes code from multiple specialized LLMs, comparing it against TurinTech AI's vanilla Genetic Algorithm (GA)-based ensemble system and individual LLM optimizers using real-world industrial codebases. Our key contributions include: (1) First MoA application to industrial code optimization using real-world codebases; (2) Empirical evidence that MoA excels with open-source models, achieving 14.3% to 22.2% cost savings and 28.6% to 32.2% faster optimization times for regulated environments; (3) Deployment guidelines demonstrating GA's advantage with commercial models while both ensembles outperform individual LLMs; and (4) Real-world validation across 50 code snippets and seven LLM combinations, generating over 8,700 variants, addresses gaps in industrial LLM ensemble evaluation. This provides actionable guidance for organizations balancing regulatory compliance with optimization performance in production environments.

