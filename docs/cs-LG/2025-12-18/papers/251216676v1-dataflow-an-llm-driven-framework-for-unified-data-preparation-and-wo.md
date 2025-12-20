---
layout: default
title: DataFlow: An LLM-Driven Framework for Unified Data Preparation and Workflow Automation in the Era of Data-Centric AI
---

# DataFlow: An LLM-Driven Framework for Unified Data Preparation and Workflow Automation in the Era of Data-Centric AI

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16676" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16676v1</a>
  <a href="https://arxiv.org/pdf/2512.16676.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16676v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16676v1', 'DataFlow: An LLM-Driven Framework for Unified Data Preparation and Workflow Automation in the Era of Data-Centric AI')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hao Liang, Xiaochen Ma, Zhou Liu, Zhen Hao Wong, Zhengyang Zhao, Zimo Meng, Runming He, Chengyu Shen, Qifeng Cai, Zhaoyang Han, Meiyi Qiang, Yalin Feng, Tianyi Bai, Zewei Pan, Ziyi Guo, Yizhen Jiang, Jingwen Deng, Qijie You, Peichao Lai, Tianyu Guo, Chi Hsu Tsai, Hengyi Feng, Rui Hu, Wenkai Yu, Junbo Niu, Bohan Zeng, Ruichuan An, Lu Ma, Jihao Huang, Yaowei Zheng, Conghui He, Linpeng Tang, Bin Cui, Weinan E, Wentao Zhang

**分类**: cs.LG, cs.CL

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**DataFlow：一个LLM驱动的统一数据准备与工作流自动化框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `数据准备` `大语言模型` `工作流自动化` `LLM Agent` `数据中心AI`

## 📋 核心要点

1. 现有数据准备流程依赖临时脚本和松散的工作流，缺乏抽象，难以复现，且对模型在环数据生成支持有限。
2. DataFlow通过系统级抽象实现模块化、可重用和可组合的数据转换，并提供PyTorch风格的pipeline构建API。
3. 实验表明，DataFlow在多个任务上超越人工数据集和特定基线，并能提升下游LLM性能，例如Text-to-SQL准确率提升3%。

## 📝 摘要（中文）

为了应对大语言模型（LLM）对高质量数据日益增长的需求，本文提出了DataFlow，一个统一且可扩展的LLM驱动的数据准备框架。DataFlow采用系统级抽象，实现了模块化、可重用和可组合的数据转换，并提供了一个类似PyTorch的pipeline构建API，用于构建可调试和优化的数据流。该框架包含近200个可重用算子和六个领域通用的pipeline，涵盖文本、数学推理、代码、Text-to-SQL、agentic RAG和大规模知识抽取。为了进一步提高可用性，我们引入了DataFlow-Agent，它通过算子合成、pipeline规划和迭代验证，自动将自然语言规范转换为可执行的pipeline。在六个代表性用例中，DataFlow始终提高了下游LLM的性能。我们的数学、代码和文本pipeline优于人工数据集和专门的合成基线，在Text-to-SQL中实现了高达+3%的执行准确率（超过SynSQL），在代码基准测试中平均提高了+7%，在MATH、GSM8K和AIME上提高了1-3个点。此外，DataFlow生成的统一的1万样本数据集使基础模型能够超越在100万Infinity-Instruct数据上训练的同类模型。这些结果表明，DataFlow为可靠、可重复和可扩展的LLM数据准备提供了一个实用且高性能的基础，并为未来的数据中心AI开发奠定了系统级基础。

## 🔬 方法详解

**问题定义**：论文旨在解决大规模语言模型（LLM）训练中高质量数据准备的难题。现有方法通常依赖于临时脚本和非结构化的工作流程，导致数据准备过程难以复现、扩展性和优化性差，并且缺乏对模型在环数据生成流程的有效支持。

**核心思路**：论文的核心思路是构建一个统一的、可扩展的LLM驱动的数据准备框架DataFlow。该框架通过系统级的抽象，将数据转换过程模块化、可重用和可组合，从而简化数据准备流程，提高效率和可维护性。DataFlow还引入了DataFlow-Agent，利用LLM自动将自然语言描述转化为可执行的数据pipeline。

**技术框架**：DataFlow框架包含以下主要模块：1) 可重用算子库：包含近200个算子，涵盖文本、数学、代码等多个领域；2) PyTorch风格的pipeline构建API：方便用户构建、调试和优化数据流；3) DataFlow-Agent：自动将自然语言规范转换为可执行的pipeline，包括算子合成、pipeline规划和迭代验证等步骤。整体流程是从自然语言需求开始，通过DataFlow-Agent生成pipeline，然后利用算子库和pipeline API执行数据转换，最终得到高质量的数据集。

**关键创新**：DataFlow的关键创新在于：1) 统一的系统级抽象，使得数据准备流程更加模块化和可重用；2) DataFlow-Agent，利用LLM自动生成数据pipeline，降低了数据准备的门槛；3) 框架的可扩展性，方便用户添加新的算子和pipeline，适应不同的数据准备需求。与现有方法相比，DataFlow更加结构化、自动化和可扩展。

**关键设计**：DataFlow-Agent的设计是关键。它利用LLM进行算子合成和pipeline规划，需要解决如何将自然语言需求准确映射到算子和pipeline的问题。迭代验证机制用于确保生成的pipeline的正确性。此外，框架还考虑了数据流的优化，例如算子融合和并行执行，以提高数据准备的效率。具体参数设置和损失函数等细节未在摘要中提及，属于未知信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16676v1/x4.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16676v1/x5.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16676v1/x6.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，DataFlow在多个任务上取得了显著的性能提升。例如，在Text-to-SQL任务中，DataFlow的准确率比SynSQL提高了3%。在代码基准测试中，平均提高了7%。在MATH、GSM8K和AIME等数学推理任务中，提高了1-3个点。此外，DataFlow生成的1万样本数据集使基础模型能够超越在100万Infinity-Instruct数据上训练的同类模型。

## 🎯 应用场景

DataFlow框架可广泛应用于各种需要高质量数据的大语言模型训练场景，例如文本生成、数学推理、代码生成、知识图谱构建等。它能显著降低数据准备的成本和复杂度，提高LLM的性能和可靠性，加速数据中心AI的发展。

## 📄 摘要（原文）

> The rapidly growing demand for high-quality data in Large Language Models (LLMs) has intensified the need for scalable, reliable, and semantically rich data preparation pipelines. However, current practices remain dominated by ad-hoc scripts and loosely specified workflows, which lack principled abstractions, hinder reproducibility, and offer limited support for model-in-the-loop data generation. To address these challenges, we present DataFlow, a unified and extensible LLM-driven data preparation framework. DataFlow is designed with system-level abstractions that enable modular, reusable, and composable data transformations, and provides a PyTorch-style pipeline construction API for building debuggable and optimizable dataflows. The framework consists of nearly 200 reusable operators and six domain-general pipelines spanning text, mathematical reasoning, code, Text-to-SQL, agentic RAG, and large-scale knowledge extraction. To further improve usability, we introduce DataFlow-Agent, which automatically translates natural-language specifications into executable pipelines via operator synthesis, pipeline planning, and iterative verification. Across six representative use cases, DataFlow consistently improves downstream LLM performance. Our math, code, and text pipelines outperform curated human datasets and specialized synthetic baselines, achieving up to +3\% execution accuracy in Text-to-SQL over SynSQL, +7\% average improvements on code benchmarks, and 1--3 point gains on MATH, GSM8K, and AIME. Moreover, a unified 10K-sample dataset produced by DataFlow enables base models to surpass counterparts trained on 1M Infinity-Instruct data. These results demonstrate that DataFlow provides a practical and high-performance substrate for reliable, reproducible, and scalable LLM data preparation, and establishes a system-level foundation for future data-centric AI development.

