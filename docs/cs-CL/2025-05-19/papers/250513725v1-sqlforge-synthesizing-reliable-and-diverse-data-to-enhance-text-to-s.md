---
layout: default
title: "SQLForge: Synthesizing Reliable and Diverse Data to Enhance Text-to-SQL Reasoning in LLMs"
---

# SQLForge: Synthesizing Reliable and Diverse Data to Enhance Text-to-SQL Reasoning in LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13725" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13725v1</a>
  <a href="https://arxiv.org/pdf/2505.13725.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13725v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13725v1', 'SQLForge: Synthesizing Reliable and Diverse Data to Enhance Text-to-SQL Reasoning in LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yu Guo, Dong Jin, Shenghao Ye, Shuangwu Chen, Jian Yang, Xiaobin Tan

**分类**: cs.CL

**发布日期**: 2025-05-19

**备注**: 12 pages, 7 figures, accepted to ACL Findings 2025

**期刊**: SQLForge: Synthesizing Reliable and Diverse Data to Enhance Text-to-SQL Reasoning in LLMs (Guo et al., Findings 2025)

**DOI**: [10.18653/v1/2025.findings-acl.443](https://doi.org/10.18653/v1/2025.findings-acl.443)

---

## 💡 一句话要点

**提出SQLForge以增强LLM的文本到SQL推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本到SQL推理` `大型语言模型` `数据合成` `模型微调` `SQL模板`

## 📋 核心要点

1. 现有的文本到SQL推理方法在开源模型与闭源模型之间存在显著的性能差距，影响了实际应用效果。
2. SQLForge通过合成可靠和多样化的数据，利用SQL语法约束和反向翻译来提升数据的逻辑性和多样性。
3. SQLForge-LM在Spider和BIRD基准测试中表现出色，分别达到了85.7%和59.8%的EX准确率，显著提升了开源模型的性能。

## 📝 摘要（中文）

大型语言模型（LLMs）在文本到SQL推理任务中展现了显著潜力，但开源模型与闭源模型之间仍存在较大性能差距。本文提出SQLForge，一种新颖的方法，通过合成可靠且多样化的数据来增强LLM的文本到SQL推理能力。我们通过SQL语法约束和SQL到问题的反向翻译提高数据的可靠性，确保数据在结构和语义层面的逻辑性。同时，我们提出了SQL模板丰富和迭代数据领域探索机制，以提升数据的多样性。在增强数据的基础上，我们对多种不同架构和参数规模的开源模型进行了微调，形成了一系列被称为SQLForge-LM的模型。SQLForge-LM在广泛认可的Spider和BIRD基准测试中达到了开源模型的最先进性能，具体而言，在Spider Dev上实现了85.7%的EX准确率，在BIRD Dev上实现了59.8%的EX准确率，显著缩小了与闭源方法的性能差距。

## 🔬 方法详解

**问题定义**：本文旨在解决开源大型语言模型在文本到SQL推理任务中性能不足的问题，特别是与闭源模型相比的显著差距。现有方法在数据的可靠性和多样性方面存在不足，导致推理效果不佳。

**核心思路**：SQLForge的核心思路是通过合成高质量的训练数据来提升模型的推理能力。具体而言，通过引入SQL语法约束和SQL到问题的反向翻译，确保生成数据在逻辑和语义上的一致性，同时通过丰富SQL模板和迭代探索数据领域来增加数据的多样性。

**技术框架**：SQLForge的整体架构包括数据合成模块、数据增强模块和模型微调模块。数据合成模块负责生成符合SQL语法的数据，数据增强模块则通过多样化的模板和领域探索来扩展数据集，最后通过微调模块对不同架构的开源模型进行训练。

**关键创新**：SQLForge的主要创新在于结合了SQL语法约束和反向翻译技术，确保生成数据的逻辑性，同时通过模板丰富和领域探索机制显著提升数据的多样性。这种方法与传统的单一数据生成方式有本质区别。

**关键设计**：在关键设计上，SQLForge采用了多种SQL模板，并通过迭代方式探索不同的数据领域，以确保生成数据的多样性和覆盖面。此外，模型微调过程中采用了适应性学习率和多种损失函数，以优化模型性能。

## 📊 实验亮点

SQLForge-LM在Spider Dev和BIRD Dev基准测试中分别达到了85.7%和59.8%的EX准确率，显著优于现有开源模型，缩小了与闭源方法的性能差距。这一结果表明，SQLForge在提升文本到SQL推理能力方面具有显著的效果和实用价值。

## 🎯 应用场景

SQLForge的研究成果在数据库查询生成、智能问答系统和数据分析等领域具有广泛的应用潜力。通过提升文本到SQL推理的准确性和可靠性，该方法可以帮助开发更智能的数据库交互工具，进而推动数据驱动决策的效率和准确性。未来，SQLForge的理念和方法也可能扩展到其他自然语言处理任务中，促进更广泛的AI应用。

## 📄 摘要（原文）

> Large Language models (LLMs) have demonstrated significant potential in text-to-SQL reasoning tasks, yet a substantial performance gap persists between existing open-source models and their closed-source counterparts. In this paper, we introduce SQLForge, a novel approach for synthesizing reliable and diverse data to enhance text-to-SQL reasoning in LLMs. We improve data reliability through SQL syntax constraints and SQL-to-question reverse translation, ensuring data logic at both structural and semantic levels. We also propose an SQL template enrichment and iterative data domain exploration mechanism to boost data diversity. Building on the augmented data, we fine-tune a variety of open-source models with different architectures and parameter sizes, resulting in a family of models termed SQLForge-LM. SQLForge-LM achieves the state-of-the-art performance on the widely recognized Spider and BIRD benchmarks among the open-source models. Specifically, SQLForge-LM achieves EX accuracy of 85.7% on Spider Dev and 59.8% on BIRD Dev, significantly narrowing the performance gap with closed-source methods.

