---
layout: default
title: "Bridging AI and Carbon Capture: A Dataset for LLMs in Ionic Liquids and CBE Research"
---

# Bridging AI and Carbon Capture: A Dataset for LLMs in Ionic Liquids and CBE Research

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.06964" class="toolbar-btn" target="_blank">📄 arXiv: 2505.06964v2</a>
  <a href="https://arxiv.org/pdf/2505.06964.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.06964v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.06964v2', 'Bridging AI and Carbon Capture: A Dataset for LLMs in Ionic Liquids and CBE Research')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gaurab Sarkar, Sougata Saha

**分类**: cs.AI

**发布日期**: 2025-05-11 (更新: 2025-05-17)

---

## 💡 一句话要点

**提出针对离子液体的LLM评估数据集以促进碳捕集研究**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `离子液体` `碳捕集` `数据集` `化学与生物工程` `推理能力` `环境科学`

## 📋 核心要点

1. 现有的LLMs在化学与生物工程领域的应用尚未得到充分评估，缺乏有效的基准测试。
2. 本文提出了一个包含5920个示例的专家策划数据集，旨在评估LLMs在离子液体领域的推理能力。
3. 实验结果显示，虽然小型通用LLMs对离子液体有基本了解，但在高级推理能力上存在明显不足。

## 📝 摘要（中文）

大型语言模型（LLMs）在各领域的知识和推理任务中表现出色，但在化学与生物工程（CBE）等专业领域的有效性尚未得到充分探索。为此，本文提供了一个全面的实证分析，重点关注离子液体（ILs）在碳捕集中的应用，开发并发布了一个包含5920个示例的专家策划数据集，以评估LLMs在该领域的推理能力。通过对三种参数少于100亿的开源LLMs进行评估，发现小型通用LLMs对ILs的基本知识有所了解，但缺乏高级应用所需的专业推理能力。基于这些结果，讨论了增强LLMs在碳捕集研究中实用性的策略。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在化学与生物工程领域，尤其是离子液体碳捕集应用中的推理能力不足的问题。现有方法缺乏针对特定领域的评估基准，导致LLMs在专业知识和推理能力上的评估不够全面。

**核心思路**：通过构建一个包含多样化难度和领域特定知识的数据集，来系统性地评估LLMs在离子液体研究中的推理能力。该数据集的设计旨在平衡语言复杂性与专业知识，以便更好地反映LLMs的实际应用能力。

**技术框架**：整体架构包括数据集的构建、LLMs的选择与评估、以及结果分析三个主要阶段。数据集由专家策划，涵盖不同难度的示例，以确保评估的全面性和有效性。

**关键创新**：本文的主要创新在于首次针对离子液体领域构建了专门的数据集，并通过实证分析揭示了LLMs在该领域的推理能力与不足之处。这一方法与现有的通用评估方法有本质区别，强调了领域特定知识的重要性。

**关键设计**：数据集包含5920个示例，设计时考虑了语言复杂性和领域知识的平衡。评估过程中选择了三种参数少于100亿的开源LLMs，确保结果的可比性和实用性。

## 📊 实验亮点

实验结果表明，小型通用LLMs在离子液体知识方面表现出基本理解，但在高级推理能力上存在显著不足。通过使用新构建的数据集，评估结果为未来LLMs在碳捕集研究中的应用提供了重要的改进方向。

## 🎯 应用场景

该研究的潜在应用领域包括化学与生物工程、环境科学以及人工智能与机器学习的交叉研究。通过提升LLMs在碳捕集研究中的推理能力，能够促进离子液体的应用开发，进而推动全球碳中和目标的实现。

## 📄 摘要（原文）

> Large Language Models (LLMs) have demonstrated exceptional performance in general knowledge and reasoning tasks across various domains. However, their effectiveness in specialized scientific fields like Chemical and Biological Engineering (CBE) remains underexplored. Addressing this gap requires robust evaluation benchmarks that assess both knowledge and reasoning capabilities in these niche areas, which are currently lacking. To bridge this divide, we present a comprehensive empirical analysis of LLM reasoning capabilities in CBE, with a focus on Ionic Liquids (ILs) for carbon sequestration - an emerging solution for mitigating global warming. We develop and release an expert - curated dataset of 5,920 examples designed to benchmark LLMs' reasoning in this domain. The dataset incorporates varying levels of difficulty, balancing linguistic complexity and domain-specific knowledge. Using this dataset, we evaluate three open-source LLMs with fewer than 10 billion parameters. Our findings reveal that while smaller general-purpose LLMs exhibit basic knowledge of ILs, they lack the specialized reasoning skills necessary for advanced applications. Building on these results, we discuss strategies to enhance the utility of LLMs for carbon capture research, particularly using ILs. Given the significant carbon footprint of LLMs, aligning their development with IL research presents a unique opportunity to foster mutual progress in both fields and advance global efforts toward achieving carbon neutrality by 2050.

