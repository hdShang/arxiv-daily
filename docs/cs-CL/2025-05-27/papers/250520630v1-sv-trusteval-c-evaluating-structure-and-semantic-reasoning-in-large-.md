---
layout: default
title: "SV-TrustEval-C: Evaluating Structure and Semantic Reasoning in Large Language Models for Source Code Vulnerability Analysis"
---

# SV-TrustEval-C: Evaluating Structure and Semantic Reasoning in Large Language Models for Source Code Vulnerability Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20630" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20630v1</a>
  <a href="https://arxiv.org/pdf/2505.20630.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20630v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20630v1', 'SV-TrustEval-C: Evaluating Structure and Semantic Reasoning in Large Language Models for Source Code Vulnerability Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yansong Li, Paula Branco, Alexander M. Hoole, Manish Marwah, Hari Manassery Koduvely, Guy-Vincent Jourdan, Stephan Jou

**分类**: cs.SE, cs.CL

**发布日期**: 2025-05-27

**期刊**: 2025 IEEE Symposium on Security and Privacy (SP), 2025, pp. 2791-2809

---

## 💡 一句话要点

**提出SV-TrustEval-C以解决LLM在代码漏洞分析中的评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `代码漏洞分析` `结构推理` `语义推理` `基准评估`

## 📋 核心要点

1. 现有方法在评估LLM的漏洞分析能力时，往往忽视了结构和语义推理的重要性，导致评估结果不够全面。
2. 本文提出SV-TrustEval-C基准，通过结构推理和语义推理两个维度，系统性地评估LLM在C语言代码漏洞分析中的能力。
3. 实验结果显示，当前LLM在理解复杂代码关系方面表现不佳，主要依赖模式匹配而非逻辑推理，表明提升空间巨大。

## 📝 摘要（中文）

随着大型语言模型（LLMs）在理解和生成代码方面的进步，准确评估其在源代码漏洞分析中的可靠性变得愈发重要。尽管已有研究探讨了LLM在漏洞检测和修复等任务中的能力，但往往忽视了结构和语义推理在可信漏洞分析中的重要性。为填补这一空白，本文提出了SV-TrustEval-C基准，旨在通过结构推理和语义推理两个维度评估LLM在C语言代码漏洞分析中的能力。实验结果表明，当前LLM在理解复杂代码关系方面远未达到理想水平，其漏洞分析更多依赖于模式匹配而非稳健的逻辑推理。这些发现强调了SV-TrustEval-C基准的有效性，并指出了提升LLM在实际漏洞分析任务中推理能力和可信度的关键领域。

## 🔬 方法详解

**问题定义**：本文旨在解决现有方法在评估大型语言模型（LLMs）在源代码漏洞分析中的不足，特别是对结构和语义推理的忽视。现有研究多集中于漏洞检测和修复，缺乏对模型推理能力的全面评估。

**核心思路**：SV-TrustEval-C基准通过结构推理和语义推理两个维度，系统评估LLMs在分析C语言代码漏洞时的能力。结构推理关注代码元素之间的关系，而语义推理则考察模型在结构和语义扰动下的逻辑一致性。

**技术框架**：SV-TrustEval-C的整体架构包括数据集构建、评估指标设计和实验验证三个主要模块。数据集涵盖多种代码结构和语义扰动场景，评估指标则用于量化模型的推理能力。

**关键创新**：SV-TrustEval-C的创新之处在于其双维度评估方法，结合结构和语义推理，填补了现有评估方法的空白。这种设计使得评估结果更具可信度和实用性。

**关键设计**：在数据集构建中，设置了多种复杂的数据和控制流场景，以测试模型的推理能力。评估指标包括模型在不同扰动下的逻辑一致性和推理准确性，确保全面评估LLMs的能力。

## 📊 实验亮点

实验结果表明，当前LLMs在复杂代码关系理解方面的表现远未达到预期，主要依赖模式匹配而非逻辑推理。SV-TrustEval-C基准的引入，揭示了LLMs在漏洞分析中的关键短板，为后续研究提供了明确的改进方向。

## 🎯 应用场景

该研究的潜在应用领域包括软件安全、代码审计和自动化漏洞检测等。通过提升LLMs在漏洞分析中的推理能力，能够有效提高代码安全性，减少潜在的安全隐患。未来，该基准有望推动LLMs在实际应用中的可信度和可靠性提升。

## 📄 摘要（原文）

> As Large Language Models (LLMs) evolve in understanding and generating code, accurately evaluating their reliability in analyzing source code vulnerabilities becomes increasingly vital. While studies have examined LLM capabilities in tasks like vulnerability detection and repair, they often overlook the importance of both structure and semantic reasoning crucial for trustworthy vulnerability analysis. To address this gap, we introduce SV-TrustEval-C, a benchmark designed to evaluate LLMs' abilities for vulnerability analysis of code written in the C programming language through two key dimensions: structure reasoning - assessing how models identify relationships between code elements under varying data and control flow complexities; and semantic reasoning - examining their logical consistency in scenarios where code is structurally and semantically perturbed. Our results show that current LLMs are far from satisfactory in understanding complex code relationships and that their vulnerability analyses rely more on pattern matching than on robust logical reasoning. These findings underscore the effectiveness of the SV-TrustEval-C benchmark and highlight critical areas for enhancing the reasoning capabilities and trustworthiness of LLMs in real-world vulnerability analysis tasks. Our initial benchmark dataset is publicly available.

