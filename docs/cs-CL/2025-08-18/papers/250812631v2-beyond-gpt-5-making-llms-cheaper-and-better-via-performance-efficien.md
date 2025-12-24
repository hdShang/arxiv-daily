---
layout: default
title: "Beyond GPT-5: Making LLMs Cheaper and Better via Performance-Efficiency Optimized Routing"
---

# Beyond GPT-5: Making LLMs Cheaper and Better via Performance-Efficiency Optimized Routing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.12631" class="toolbar-btn" target="_blank">📄 arXiv: 2508.12631v2</a>
  <a href="https://arxiv.org/pdf/2508.12631.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.12631v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.12631v2', 'Beyond GPT-5: Making LLMs Cheaper and Better via Performance-Efficiency Optimized Routing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yiqun Zhang, Hao Li, Jianhao Chen, Hangfan Zhang, Peng Ye, Lei Bai, Shuyue Hu

**分类**: cs.CL

**发布日期**: 2025-08-18 (更新: 2025-10-22)

**备注**: This work has been accepted to DAI 2025

**DOI**: [10.1145/3772429.3772445](https://doi.org/10.1145/3772429.3772445)

**🔗 代码/项目**: [GITHUB](https://github.com/ZhangYiqun018/AvengersPro)

---

## 💡 一句话要点

**提出Avengers-Pro以优化大语言模型的性能与效率**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `性能优化` `效率提升` `动态路由` `模型集成` `机器学习`

## 📋 核心要点

1. 现有的大语言模型在性能与效率之间的权衡存在不足，难以满足实际应用需求。
2. Avengers-Pro通过动态路由机制，将查询分配给不同效率和容量的模型，从而优化性能与成本。
3. 在多个基准测试中，Avengers-Pro的表现超越了现有最强模型，并在成本上实现了显著降低。

## 📝 摘要（中文）

在大型语言模型（LLM）发展中，平衡性能与效率是一个核心挑战。GPT-5通过测试时路由动态分配查询到高效或高容量模型来应对这一问题。本研究提出了Avengers-Pro，一个测试时路由框架，集成了不同容量和效率的LLM，提供了统一的性能-效率权衡解决方案。Avengers-Pro对输入查询进行嵌入和聚类，然后根据性能-效率评分将每个查询路由到最合适的模型。在6个具有挑战性的基准测试和8个领先模型（包括GPT-5-medium、Gemini-2.5-pro和Claude-opus-4.1）上，Avengers-Pro实现了最先进的结果：通过调整性能-效率权衡参数，其平均准确率比最强单一模型（GPT-5-medium）提高了7%。此外，它在降低27%成本的情况下可以匹配最强单一模型的平均准确率，并在降低63%成本的情况下达到约90%的性能。最后，它实现了帕累托前沿，在所有单一模型中，对于任何给定成本始终提供最高准确率，对于任何给定准确率始终提供最低成本。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型在推理阶段性能与效率之间的权衡问题。现有方法通常无法在不同应用场景中灵活调整，导致资源浪费和性能不足。

**核心思路**：论文提出的Avengers-Pro框架通过动态路由机制，根据输入查询的特征将其分配给最合适的模型，从而实现性能与效率的最佳平衡。这样的设计使得模型能够根据实际需求灵活调整，避免了单一模型的局限性。

**技术框架**：Avengers-Pro的整体架构包括查询嵌入、聚类和路由三个主要模块。首先，对输入查询进行嵌入处理，然后通过聚类算法将相似查询分组，最后根据性能-效率评分将每个查询路由到最适合的模型。

**关键创新**：Avengers-Pro的主要创新在于其动态路由机制，能够在推理过程中实时评估查询的性能-效率需求，并选择最优模型。这一机制与传统的静态模型选择方法有本质区别，后者无法适应多变的查询特征。

**关键设计**：在设计中，Avengers-Pro引入了性能-效率评分机制，该机制基于模型的历史表现和当前查询特征进行动态评估。此外，聚类算法的选择和参数设置也经过精心设计，以确保路由的准确性和效率。

## 📊 实验亮点

在实验中，Avengers-Pro在6个基准测试上表现优异，平均准确率比最强单一模型（GPT-5-medium）提高了7%。此外，在降低27%成本的情况下，其准确率与最强模型持平，并在降低63%成本的情况下达到约90%的性能，展示了其在性能与成本之间的优越平衡。

## 🎯 应用场景

Avengers-Pro框架在多个领域具有广泛的应用潜力，包括自然语言处理、对话系统和智能助手等。通过优化性能与成本的平衡，该框架能够为企业和研究机构提供更高效的模型选择方案，从而提升实际应用的效果和经济性。未来，该技术可能会推动更多智能应用的发展，促进大语言模型的普及与应用。

## 📄 摘要（原文）

> Balancing performance and efficiency is a central challenge in large language model (LLM) advancement. GPT-5 addresses this with test-time routing, dynamically assigning queries to either an efficient or a high-capacity model during inference. In this work, we present Avengers-Pro, a test-time routing framework that ensembles LLMs of varying capacities and efficiencies, providing a unified solution for all performance-efficiency tradeoffs. The Avengers-Pro embeds and clusters incoming queries, then routes each to the most suitable model based on a performance-efficiency score. Across 6 challenging benchmarks and 8 leading models -- including GPT-5-medium, Gemini-2.5-pro, and Claude-opus-4.1 -- Avengers-Pro achieves state-of-the-art results: by varying a performance-efficiency trade-off parameter, it can surpass the strongest single model (GPT-5-medium) by +7% in average accuracy. Moreover, it can match the average accuracy of the strongest single model at 27% lower cost, and reach ~90% of that performance at 63% lower cost. Last but not least, it achieves a Pareto frontier, consistently yielding the highest accuracy for any given cost, and the lowest cost for any given accuracy, among all single models. Code is available at https://github.com/ZhangYiqun018/AvengersPro.

