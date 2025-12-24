---
layout: default
title: "ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs"
---

# ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04696" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04696v1</a>
  <a href="https://arxiv.org/pdf/2509.04696.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04696v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04696v1', 'ODKE+: Ontology-Guided Open-Domain Knowledge Extraction with LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Samira Khorshidi, Azadeh Nikfarjam, Suprita Shankar, Yisi Sang, Yash Govind, Hyun Jang, Ali Kasgari, Alexis McClimans, Mohamed Soliman, Vishnu Konda, Ahmed Fakhry, Xiaoguang Qi

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-04

---

## 💡 一句话要点

**ODKE+：利用LLM和本体指导的开放域知识抽取系统，实现大规模高精度知识图谱构建。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `知识图谱` `开放域知识抽取` `大型语言模型` `本体指导` `信息抽取`

## 📋 核心要点

1. 现有知识图谱维护成本高昂，难以保证新鲜度和完整性，阻碍了其在AI应用中的广泛应用。
2. ODKE+系统结合模式规则和本体指导的LLM提示，构建可扩展的知识抽取流水线，提升抽取精度和效率。
3. 实验结果表明，ODKE+显著提高了知识图谱的覆盖率，并降低了更新延迟，验证了其有效性。

## 📝 摘要（中文）

知识图谱(KGs)是许多人工智能应用的基础，但维护其新鲜度和完整性仍然代价高昂。我们提出了ODKE+，一个生产级别的系统，可以自动从网络来源提取和摄取数百万条高精度的开放域事实。ODKE+将模块化组件组合成一个可扩展的流水线：(1)抽取启动器检测缺失或过时的事实，(2)证据检索器收集支持文档，(3)混合知识抽取器应用基于模式的规则和本体指导的提示来使用大型语言模型(LLM)，(4)轻量级Grounder使用第二个LLM验证提取的事实，(5)校对器对候选事实进行排序和规范化以进行摄取。ODKE+动态生成针对每种实体类型量身定制的本体片段，以使抽取与模式约束对齐，从而实现跨195个谓词的可扩展、类型一致的事实抽取。该系统支持批量和流模式，处理超过900万个维基百科页面，并摄取1900万条高置信度的事实，精度为98.8%。ODKE+显著提高了对传统方法的覆盖率，实现了与第三方KG高达48%的重叠，并将更新延迟平均减少了50天。我们的部署表明，基于本体结构和验证工作流程的LLM抽取可以提供可信赖的、生产规模的知识摄取，具有广泛的实际应用。

## 🔬 方法详解

**问题定义**：论文旨在解决开放域知识图谱构建中，现有方法抽取精度低、覆盖率不足、更新滞后等问题。传统方法依赖人工标注或简单的模式匹配，难以应对复杂多变的Web数据，且维护成本高昂。

**核心思路**：论文的核心思路是结合大型语言模型（LLMs）的强大语义理解能力和本体的结构化知识，构建一个自动化、高精度、可扩展的知识抽取系统。通过本体指导LLM进行知识抽取，并利用验证模块过滤错误信息，从而提高抽取质量。

**技术框架**：ODKE+系统包含以下主要模块：(1) **抽取启动器**：检测知识图谱中缺失或过时的信息，触发新的抽取任务。(2) **证据检索器**：从Web文档中检索与目标实体相关的证据。(3) **混合知识抽取器**：结合基于模式的规则和本体指导的LLM提示，从证据中抽取候选事实。(4) **Grounder**：使用LLM验证抽取的事实，过滤错误信息。(5) **校对器**：对候选事实进行排序和规范化，选择置信度高的事实加入知识图谱。

**关键创新**：ODKE+的关键创新在于：(1) **本体指导的LLM提示**：动态生成针对每种实体类型的本体片段，引导LLM进行类型一致的事实抽取，提高抽取精度。(2) **混合知识抽取方法**：结合模式规则和LLM，充分利用现有知识和LLM的语义理解能力。(3) **轻量级Grounder**：使用LLM进行事实验证，有效过滤错误信息。

**关键设计**：ODKE+的关键设计包括：(1) 动态生成的本体片段，用于指导LLM进行知识抽取。(2) 用于事实验证的LLM Grounder，其具体prompt设计未知。(3) 混合知识抽取器中，模式规则和LLM的融合方式未知。(4) 校对器中，对候选事实进行排序和规范化的具体算法未知。

## 📊 实验亮点

ODKE+系统在实际部署中表现出色，处理了超过900万个维基百科页面，并成功摄取了1900万条高置信度的事实，精度高达98.8%。与传统方法相比，ODKE+显著提高了知识图谱的覆盖率，实现了与第三方知识图谱高达48%的重叠，并将更新延迟平均减少了50天。

## 🎯 应用场景

ODKE+可应用于自动构建和维护大规模知识图谱，为搜索引擎、问答系统、推荐系统等提供高质量的知识支撑。该系统能够显著降低知识图谱的构建成本，提高知识图谱的覆盖率和时效性，从而提升各种AI应用的性能和用户体验。未来，ODKE+有望应用于更广泛的领域，如智能客服、金融风控、医疗诊断等。

## 📄 摘要（原文）

> Knowledge graphs (KGs) are foundational to many AI applications, but maintaining their freshness and completeness remains costly. We present ODKE+, a production-grade system that automatically extracts and ingests millions of open-domain facts from web sources with high precision. ODKE+ combines modular components into a scalable pipeline: (1) the Extraction Initiator detects missing or stale facts, (2) the Evidence Retriever collects supporting documents, (3) hybrid Knowledge Extractors apply both pattern-based rules and ontology-guided prompting for large language models (LLMs), (4) a lightweight Grounder validates extracted facts using a second LLM, and (5) the Corroborator ranks and normalizes candidate facts for ingestion. ODKE+ dynamically generates ontology snippets tailored to each entity type to align extractions with schema constraints, enabling scalable, type-consistent fact extraction across 195 predicates. The system supports batch and streaming modes, processing over 9 million Wikipedia pages and ingesting 19 million high-confidence facts with 98.8% precision. ODKE+ significantly improves coverage over traditional methods, achieving up to 48% overlap with third-party KGs and reducing update lag by 50 days on average. Our deployment demonstrates that LLM-based extraction, grounded in ontological structure and verification workflows, can deliver trustworthiness, production-scale knowledge ingestion with broad real-world applicability. A recording of the system demonstration is included with the submission and is also available at https://youtu.be/UcnE3_GsTWs.

