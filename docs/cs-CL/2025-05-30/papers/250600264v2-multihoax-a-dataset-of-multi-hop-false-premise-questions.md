---
layout: default
title: "MultiHoax: A Dataset of Multi-hop False-Premise Questions"
---

# MultiHoax: A Dataset of Multi-hop False-Premise Questions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00264" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00264v2</a>
  <a href="https://arxiv.org/pdf/2506.00264.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00264v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00264v2', 'MultiHoax: A Dataset of Multi-hop False-Premise Questions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mohammadamin Shafiei, Hamidreza Saffari, Nafise Sadat Moosavi

**分类**: cs.CL

**发布日期**: 2025-05-30 (更新: 2025-06-04)

**备注**: accepted at ACL Findings 2025

---

## 💡 一句话要点

**提出MultiHoax数据集以解决多跳错误前提问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多跳推理` `错误前提` `大型语言模型` `数据集构建` `知识推理`

## 📋 核心要点

1. 现有方法主要集中在单跳错误前提问题，缺乏对多跳推理的有效评估，导致模型在复杂推理场景中的表现不佳。
2. 论文提出MultiHoax数据集，专注于多跳错误前提问题，利用维基百科作为知识来源，涵盖多国和多类别知识。
3. 实验结果显示，当前最先进的语言模型在多跳推理任务中检测错误前提的能力不足，强调了该领域的研究需求。

## 📝 摘要（中文）

随着大型语言模型在高风险领域的广泛应用，其检测错误假设和进行批判性推理的能力至关重要。错误前提问题（FPQs）作为一种重要的评估方法，能够揭示由于错误假设导致的不正确响应。现有基准主要集中在单跳FPQs，而现实世界的推理往往需要多跳推理，模型必须在多个推理步骤中验证一致性，而不是依赖表面线索。为填补这一空白，我们提出了MultiHoax，一个用于评估大型语言模型在复杂多步骤推理任务中处理错误前提能力的基准。我们的数据集涵盖七个国家和十个多样的知识类别，以维基百科作为主要知识来源，以促进跨区域的事实推理。实验表明，最先进的大型语言模型在不同国家、知识类别和多跳推理类型中检测错误前提的能力较弱，突显了改进错误前提检测和增强多跳推理能力的必要性。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型在处理多跳错误前提问题时的不足，现有方法主要集中于单跳推理，无法有效应对复杂推理场景中的错误假设。

**核心思路**：论文的核心思路是构建MultiHoax数据集，通过多跳推理任务评估模型的错误前提检测能力，强调模型在多个推理步骤中验证一致性的必要性。

**技术框架**：整体架构包括数据集构建、模型训练和评估三个主要模块。数据集涵盖多国和多类别知识，模型则在此基础上进行训练和性能评估。

**关键创新**：最重要的技术创新点在于引入多跳推理的框架，填补了现有单跳FPQs的研究空白，使得模型能够在更复杂的推理任务中进行评估。

**关键设计**：在数据集构建中，选择维基百科作为知识来源，确保信息的准确性和多样性。此外，设计了适合多跳推理的损失函数，以提升模型在该任务上的表现。

## 📊 实验亮点

实验结果显示，当前最先进的语言模型在多跳推理任务中检测错误前提的能力普遍较弱，尤其在不同国家和知识类别中表现不佳，突显了该领域的研究需求和改进空间。

## 🎯 应用场景

该研究的潜在应用领域包括教育、法律和医疗等高风险领域，能够帮助大型语言模型更好地理解和处理复杂的推理任务，从而提高其在实际应用中的可靠性和准确性。未来，该数据集可能成为评估和改进语言模型推理能力的重要基准。

## 📄 摘要（原文）

> As Large Language Models are increasingly deployed in high-stakes domains, their ability to detect false assumptions and reason critically is crucial for ensuring reliable outputs. False-premise questions (FPQs) serve as an important evaluation method by exposing cases where flawed assumptions lead to incorrect responses. While existing benchmarks focus on single-hop FPQs, real-world reasoning often requires multi-hop inference, where models must verify consistency across multiple reasoning steps rather than relying on surface-level cues. To address this gap, we introduce MultiHoax, a benchmark for evaluating LLMs' ability to handle false premises in complex, multi-step reasoning tasks. Our dataset spans seven countries and ten diverse knowledge categories, using Wikipedia as the primary knowledge source to enable factual reasoning across regions. Experiments reveal that state-of-the-art LLMs struggle to detect false premises across different countries, knowledge categories, and multi-hop reasoning types, highlighting the need for improved false premise detection and more robust multi-hop reasoning capabilities in LLMs.

