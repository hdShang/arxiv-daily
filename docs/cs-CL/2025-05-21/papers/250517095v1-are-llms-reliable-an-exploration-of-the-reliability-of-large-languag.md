---
layout: default
title: Are LLMs reliable? An exploration of the reliability of large language models in clinical note generation
---

# Are LLMs reliable? An exploration of the reliability of large language models in clinical note generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.17095" class="toolbar-btn" target="_blank">📄 arXiv: 2505.17095v1</a>
  <a href="https://arxiv.org/pdf/2505.17095.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.17095v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.17095v1', 'Are LLMs reliable? An exploration of the reliability of large language models in clinical note generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kristine Ann M. Carandang, Jasper Meynard P. Araña, Ethan Robert A. Casin, Christopher P. Monterola, Daniel Stanley Y. Tan, Jesus Felix B. Valenzuela, Christian M. Alis

**分类**: cs.CL

**发布日期**: 2025-05-21

**DOI**: [10.18653/v1/2025.acl-industry.99](https://doi.org/10.18653/v1/2025.acl-industry.99)

---

## 💡 一句话要点

**评估大型语言模型在临床笔记生成中的可靠性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `临床笔记生成` `数据隐私` `语义一致性` `医疗文档自动化` `模型评估` `人工智能在医疗中的应用`

## 📋 核心要点

1. 现有的临床笔记生成系统面临LLMs响应的自然变异性，影响医疗服务提供者的信任和使用。
2. 本研究通过评估多种LLMs在生成临床笔记时的一致性和准确性，旨在增强医疗服务提供者对这些工具的信心。
3. 实验结果显示，所有评估的LLMs在语义一致性上表现稳定，Meta的Llama 70B模型在可靠性上表现最佳。

## 📝 摘要（中文）

由于医疗服务提供者在准确文档记录和保护患者数据隐私方面的法律和伦理责任，大型语言模型（LLMs）在临床笔记生成（CNG）中的自然变异性给实际应用带来了挑战。本文评估了来自Anthropic、Meta、Mistral和OpenAI的12个开源和专有LLMs在CNG中的可靠性，重点分析其生成的笔记在一致性、语义一致性和语义相似性方面的表现。结果表明，所有模型家族的LLMs在语义上保持一致，且大多数生成的笔记接近专家的记录。Meta的Llama 70B模型表现最为可靠，建议在CNG中本地部署这些相对较小的开源模型，以确保数据隐私合规并提高医疗服务提供者的文档效率。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在临床笔记生成中的可靠性问题，现有方法在生成一致性和准确性方面存在挑战。

**核心思路**：通过对12个不同的LLMs进行评估，分析其在生成临床笔记时的一致性、语义一致性和语义相似性，以增强医疗服务提供者的信任。

**技术框架**：研究设计包括对各模型在相同提示下生成多次笔记的实验，比较其生成结果的稳定性和准确性。主要模块包括模型选择、生成笔记、结果评估和数据分析。

**关键创新**：本研究的创新点在于系统性地评估多种LLMs在临床笔记生成中的表现，提供了对比分析和实证数据，填补了该领域的研究空白。

**关键设计**：在实验中，使用了多种评估指标，如一致性率、语义一致性和语义相似性，确保了评估结果的全面性和准确性。

## 📊 实验亮点

实验结果显示，所有评估的LLMs在语义一致性上表现稳定，Meta的Llama 70B模型的可靠性最高，生成的笔记与专家记录的相似度显著提高。这些发现为临床笔记生成提供了实证支持，建议使用较小的开源模型以确保数据隐私合规。

## 🎯 应用场景

该研究的潜在应用领域包括医疗文档自动化、电子健康记录系统的集成以及临床决策支持工具的开发。通过提高LLMs在临床笔记生成中的可靠性，可以有效提升医疗服务提供者的工作效率，确保患者数据的隐私和安全。

## 📄 摘要（原文）

> Due to the legal and ethical responsibilities of healthcare providers (HCPs) for accurate documentation and protection of patient data privacy, the natural variability in the responses of large language models (LLMs) presents challenges for incorporating clinical note generation (CNG) systems, driven by LLMs, into real-world clinical processes. The complexity is further amplified by the detailed nature of texts in CNG. To enhance the confidence of HCPs in tools powered by LLMs, this study evaluates the reliability of 12 open-weight and proprietary LLMs from Anthropic, Meta, Mistral, and OpenAI in CNG in terms of their ability to generate notes that are string equivalent (consistency rate), have the same meaning (semantic consistency) and are correct (semantic similarity), across several iterations using the same prompt. The results show that (1) LLMs from all model families are stable, such that their responses are semantically consistent despite being written in various ways, and (2) most of the LLMs generated notes close to the corresponding notes made by experts. Overall, Meta's Llama 70B was the most reliable, followed by Mistral's Small model. With these findings, we recommend the local deployment of these relatively smaller open-weight models for CNG to ensure compliance with data privacy regulations, as well as to improve the efficiency of HCPs in clinical documentation.

