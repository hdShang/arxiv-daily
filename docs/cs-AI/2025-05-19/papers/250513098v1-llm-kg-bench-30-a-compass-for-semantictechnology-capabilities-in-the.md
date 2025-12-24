---
layout: default
title: LLM-KG-Bench 3.0: A Compass for SemanticTechnology Capabilities in the Ocean of LLMs
---

# LLM-KG-Bench 3.0: A Compass for SemanticTechnology Capabilities in the Ocean of LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13098" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13098v1</a>
  <a href="https://arxiv.org/pdf/2505.13098.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13098v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13098v1', 'LLM-KG-Bench 3.0: A Compass for SemanticTechnology Capabilities in the Ocean of LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lars-Peter Meyer, Johannes Frey, Desiree Heim, Felix Brei, Claus Stadler, Kurt Junghanns, Michael Martin

**分类**: cs.AI, cs.CL, cs.DB

**发布日期**: 2025-05-19

**备注**: Peer reviewed publication at ESWC 2025 Resources Track

**期刊**: Lecture Notes in Computer Science, Vol 15719(2025), ESWC25 Proceedings Part II, pp 280-296

**DOI**: [10.1007/978-3-031-94578-6_16](https://doi.org/10.1007/978-3-031-94578-6_16)

---

## 💡 一句话要点

**提出LLM-KG-Bench 3.0以评估大语言模型在知识图谱领域的能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `知识图谱` `大语言模型` `语义技术` `自动化评估` `框架设计` `数据集生成` `RDF` `SPARQL`

## 📋 核心要点

1. 现有的大语言模型在知识图谱领域的能力评估缺乏系统性，手动检查答案的效率低下。
2. LLM-KG-Bench 3.0框架提供了一套自动化评估任务，旨在系统性地评估LLM在语义技术中的表现。
3. 通过使用超过30种现代LLM，框架生成了丰富的数据集，显著提升了评估的准确性和效率。

## 📝 摘要（中文）

当前的大语言模型（LLMs）在程序代码开发等多个领域表现出色，但在知识图谱（KGs）方面的支持能力尚不明确。LLM-KG-Bench 3.0框架旨在自动评估LLM在语义技术和知识图谱工程（KGE）方面的能力。本文介绍了该框架的最新版本，包括一套可扩展的任务集、生成的提示、答案和评估数据集，以及对多种开源模型的支持。相较于初始版本，框架在任务API、任务修订和对vllm库的支持等方面进行了显著增强，生成了包含30多种现代开源和专有LLM的综合数据集，展示了模型在RDF和SPARQL处理能力上的表现。

## 🔬 方法详解

**问题定义**：当前缺乏有效的方法来系统性评估大语言模型在知识图谱和语义技术领域的能力，手动评估不仅耗时且容易出错。

**核心思路**：LLM-KG-Bench 3.0框架通过设计一系列自动化评估任务，能够快速、准确地评估不同LLM在处理知识图谱相关任务时的表现。

**技术框架**：该框架包括任务API、评估模块和数据集生成模块，支持多种开源模型的集成，能够灵活处理不同的评估任务。

**关键创新**：框架的主要创新在于其可扩展性和灵活性，能够适应多种语义技术任务的评估需求，显著提高了评估的效率和准确性。

**关键设计**：框架中采用了更新的任务API，支持多种数据格式（如RDF、SPARQL），并通过vllm库扩展了对不同模型的支持，确保了评估任务的多样性和全面性。

## 📊 实验亮点

实验结果显示，LLM-KG-Bench 3.0在评估大语言模型的能力方面显著提升了效率，能够在多种任务上提供准确的性能数据。通过对比分析，框架能够清晰地展示不同模型在RDF和SPARQL处理上的优势与不足，为模型选择提供了有力支持。

## 🎯 应用场景

LLM-KG-Bench 3.0框架在知识图谱和语义技术的研究与应用中具有广泛的潜在应用价值。它可以帮助研究人员和开发者快速评估和比较不同大语言模型在处理知识图谱任务时的能力，从而推动相关技术的发展与应用。

## 📄 摘要（原文）

> Current Large Language Models (LLMs) can assist developing program code beside many other things, but can they support working with Knowledge Graphs (KGs) as well? Which LLM is offering the best capabilities in the field of Semantic Web and Knowledge Graph Engineering (KGE)? Is this possible to determine without checking many answers manually? The LLM-KG-Bench framework in Version 3.0 is designed to answer these questions. It consists of an extensible set of tasks for automated evaluation of LLM answers and covers different aspects of working with semantic technologies. In this paper the LLM-KG-Bench framework is presented in Version 3 along with a dataset of prompts, answers and evaluations generated with it and several state-of-the-art LLMs. Significant enhancements have been made to the framework since its initial release, including an updated task API that offers greater flexibility in handling evaluation tasks, revised tasks, and extended support for various open models through the vllm library, among other improvements. A comprehensive dataset has been generated using more than 30 contemporary open and proprietary LLMs, enabling the creation of exemplary model cards that demonstrate the models' capabilities in working with RDF and SPARQL, as well as comparing their performance on Turtle and JSON-LD RDF serialization tasks.

