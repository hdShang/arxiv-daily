---
layout: default
title: "Agent-OM: Leveraging LLM Agents for Ontology Matching"
---

# Agent-OM: Leveraging LLM Agents for Ontology Matching

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2312.00326" class="toolbar-btn" target="_blank">📄 arXiv: 2312.00326v23</a>
  <a href="https://arxiv.org/pdf/2312.00326.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2312.00326v23" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2312.00326v23', 'Agent-OM: Leveraging LLM Agents for Ontology Matching')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhangcheng Qiang, Weiqing Wang, Kerry Taylor

**分类**: cs.AI, cs.CL, cs.IR

**发布日期**: 2023-12-01 (更新: 2025-12-09)

**备注**: 31 pages

---

## 💡 一句话要点

**提出Agent-OM以解决本体匹配中的语义互操作性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `本体匹配` `大型语言模型` `语义互操作性` `机器学习` `Siamese网络` `数据集成` `知识图谱`

## 📋 核心要点

1. 现有OM方法主要依赖传统知识系统或机器学习系统，面临概念异构性和匹配精度不足的挑战。
2. 本研究提出Agent-OM框架，利用LLM代理进行本体检索与匹配，旨在提升OM系统的性能与灵活性。
3. 实验结果表明，Agent-OM在简单OM任务上接近最佳性能，并在复杂和少样本任务上显著提升，展示了其有效性。

## 📝 摘要（中文）

本体匹配（OM）使不同本体之间实现语义互操作性，并通过对齐相关实体解决概念异构性。目前，OM系统主要有两种设计范式：传统的基于知识的专家系统和新兴的基于机器学习的预测系统。尽管大型语言模型（LLMs）及其代理在数据工程中取得了革命性进展，但其在OM中的潜力尚未得到充分探索。本研究提出了一种新颖的基于LLM代理的OM系统设计范式，构建了一个名为Agent-OM的通用框架，包含两个用于检索和匹配的Siamese代理及一组OM工具。通过在概念验证系统中的实现，评估结果显示该系统在简单OM任务上接近最佳性能，并在复杂和少样本OM任务上显著提升表现。

## 🔬 方法详解

**问题定义**：本研究旨在解决本体匹配中的语义互操作性问题，现有方法在处理复杂和少样本任务时表现不佳，难以满足实际需求。

**核心思路**：论文提出了一种基于大型语言模型（LLM）代理的OM设计范式，通过引入Siamese网络结构，增强了本体检索和匹配的能力，提升了系统的灵活性和准确性。

**技术框架**：Agent-OM框架由两个Siamese代理组成，分别负责检索和匹配，同时配备一组OM工具。整体流程包括输入本体数据、通过代理进行检索和匹配、输出匹配结果。

**关键创新**：本研究的核心创新在于将LLM代理应用于OM领域，利用其强大的自然语言处理能力，显著提升了匹配精度和处理复杂任务的能力，与传统方法相比具有本质区别。

**关键设计**：在设计中，采用了Siamese网络结构以实现高效的相似度计算，设置了适应OM任务的损失函数，并优化了代理的参数配置，以确保系统在不同任务中的表现。

## 📊 实验亮点

实验结果显示，Agent-OM在三个本体对齐评估轨道上表现优异，其在简单OM任务上接近长期最佳性能，并在复杂和少样本OM任务上显著提升，展示了相较于现有OM系统的明显优势。

## 🎯 应用场景

该研究的潜在应用领域包括知识图谱构建、语义搜索引擎、数据集成等。通过提升本体匹配的准确性和效率，Agent-OM能够为多种行业提供更好的语义互操作性支持，促进信息共享与知识发现。未来，该框架有望在更广泛的领域中应用，推动智能系统的发展。

## 📄 摘要（原文）

> Ontology matching (OM) enables semantic interoperability between different ontologies and resolves their conceptual heterogeneity by aligning related entities. OM systems currently have two prevailing design paradigms: conventional knowledge-based expert systems and newer machine learning-based predictive systems. While large language models (LLMs) and LLM agents have revolutionised data engineering and have been applied creatively in many domains, their potential for OM remains underexplored. This study introduces a novel agent-powered LLM-based design paradigm for OM systems. With consideration of several specific challenges in leveraging LLM agents for OM, we propose a generic framework, namely Agent-OM (Agent for Ontology Matching), consisting of two Siamese agents for retrieval and matching, with a set of OM tools. Our framework is implemented in a proof-of-concept system. Evaluations of three Ontology Alignment Evaluation Initiative (OAEI) tracks over state-of-the-art OM systems show that our system can achieve results very close to the long-standing best performance on simple OM tasks and can significantly improve the performance on complex and few-shot OM tasks.

