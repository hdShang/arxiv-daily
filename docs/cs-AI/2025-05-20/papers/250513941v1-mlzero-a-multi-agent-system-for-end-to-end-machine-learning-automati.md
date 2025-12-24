---
layout: default
title: MLZero: A Multi-Agent System for End-to-end Machine Learning Automation
---

# MLZero: A Multi-Agent System for End-to-end Machine Learning Automation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13941" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13941v1</a>
  <a href="https://arxiv.org/pdf/2505.13941.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13941v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13941v1', 'MLZero: A Multi-Agent System for End-to-end Machine Learning Automation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haoyang Fang, Boran Han, Nick Erickson, Xiyuan Zhang, Su Zhou, Anirudh Dagar, Jiani Zhang, Ali Caner Turkmen, Cuixiong Hu, Huzefa Rangwala, Ying Nian Wu, Bernie Wang, George Karypis

**分类**: cs.MA, cs.AI, cs.CL, cs.LG

**发布日期**: 2025-05-20

---

## 💡 一句话要点

**提出MLZero以实现多模态数据的端到端机器学习自动化**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态数据` `机器学习自动化` `大型语言模型` `认知感知` `代码生成` `语义记忆` `情景记忆` `AutoML`

## 📋 核心要点

1. 现有AutoML系统在多模态数据处理上仍需大量手动配置和专家输入，限制了其自动化程度。
2. MLZero通过多代理框架和大型语言模型，实现了多模态数据的端到端自动化，减少了人类干预。
3. 在MLE-Bench Lite和多模态AutoML代理基准测试中，MLZero的成功率和解决方案质量显著优于竞争对手。

## 📝 摘要（中文）

现有的自动机器学习（AutoML）系统在机器学习的自动化方面取得了进展，但在处理多模态数据时仍需大量手动配置和专家输入。本文介绍了MLZero，这是一种新颖的多代理框架，利用大型语言模型（LLMs）实现多样数据模态的端到端机器学习自动化，且人类干预最小。首先，采用认知感知模块，将原始多模态输入转化为感知上下文，有效指导后续工作流程。为了解决LLMs的关键限制，如生成虚假代码和过时的API知识，我们通过语义和情景记忆增强了迭代代码生成过程。MLZero在MLE-Bench Lite上表现优异，成功率和解决方案质量均超越所有竞争者，获得六枚金牌。此外，在包含25个更具挑战性的多模态任务的多模态AutoML代理基准测试中，MLZero以0.92的成功率（+263.6%）和平均排名2.28大幅超越竞争方法。即使使用紧凑的8B LLM，MLZero也表现出色，超越了现有解决方案的全尺寸系统。

## 🔬 方法详解

**问题定义**：现有的AutoML系统在处理多模态数据时，仍需大量手动配置和专家输入，导致自动化程度不足，效率低下。

**核心思路**：MLZero通过引入多代理框架和大型语言模型，旨在实现多模态数据的端到端自动化，减少人类干预，并提高处理效率。

**技术框架**：MLZero的整体架构包括认知感知模块、迭代代码生成模块和记忆增强模块。认知感知模块将原始输入转化为感知上下文，指导后续工作流程。

**关键创新**：MLZero的主要创新在于结合了语义和情景记忆，增强了代码生成过程的准确性，解决了LLMs的虚假代码生成和过时API知识问题。

**关键设计**：在设计中，MLZero采用了紧凑的8B LLM，确保在保持高效性的同时，能够在多模态任务中表现出色。

## 📊 实验亮点

MLZero在MLE-Bench Lite上表现优异，成功率和解决方案质量均超越所有竞争者，获得六枚金牌。在多模态AutoML代理基准测试中，成功率达到0.92，提升幅度为263.6%，平均排名为2.28，展现了其卓越的性能。

## 🎯 应用场景

MLZero的研究成果在多个领域具有广泛的应用潜力，包括医疗影像分析、智能交通系统和多模态人机交互等。通过实现机器学习的自动化，MLZero可以显著降低对专家知识的依赖，提高数据处理的效率和准确性，推动相关领域的发展。

## 📄 摘要（原文）

> Existing AutoML systems have advanced the automation of machine learning (ML); however, they still require substantial manual configuration and expert input, particularly when handling multimodal data. We introduce MLZero, a novel multi-agent framework powered by Large Language Models (LLMs) that enables end-to-end ML automation across diverse data modalities with minimal human intervention. A cognitive perception module is first employed, transforming raw multimodal inputs into perceptual context that effectively guides the subsequent workflow. To address key limitations of LLMs, such as hallucinated code generation and outdated API knowledge, we enhance the iterative code generation process with semantic and episodic memory. MLZero demonstrates superior performance on MLE-Bench Lite, outperforming all competitors in both success rate and solution quality, securing six gold medals. Additionally, when evaluated on our Multimodal AutoML Agent Benchmark, which includes 25 more challenging tasks spanning diverse data modalities, MLZero outperforms the competing methods by a large margin with a success rate of 0.92 (+263.6\%) and an average rank of 2.28. Our approach maintains its robust effectiveness even with a compact 8B LLM, outperforming full-size systems from existing solutions.

