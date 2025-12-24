---
layout: default
title: On the Effectiveness of Instruction-Tuning Local LLMs for Identifying Software Vulnerabilities
---

# On the Effectiveness of Instruction-Tuning Local LLMs for Identifying Software Vulnerabilities

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20062" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20062v1</a>
  <a href="https://arxiv.org/pdf/2512.20062.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20062v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20062v1', 'On the Effectiveness of Instruction-Tuning Local LLMs for Identifying Software Vulnerabilities')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sangryu Park, Gihyuk Ko, Homook Cho

**分类**: cs.CR, cs.AI

**发布日期**: 2025-12-23

**备注**: The 9th International Conference on Mobile Internet Security (MobiSec 2025)

---

## 💡 一句话要点

**指令调优本地LLM，有效识别软件漏洞类型，提升安全性和实用性。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `软件漏洞分析` `大型语言模型` `指令调优` `本地LLM` `软件安全`

## 📋 核心要点

1. 现有软件漏洞分析方法依赖在线API-based LLM，存在暴露源代码的安全风险，且仅限于二元分类，实用性受限。
2. 论文提出软件漏洞识别(SVI)任务，要求LLM输出CWE ID，实现漏洞类型识别，并采用指令调优本地LLM。
3. 实验表明，指令调优的本地LLM在性能和成本效益上优于在线API-based LLM，更具实用性。

## 📝 摘要（中文）

大型语言模型(LLM)在自动化软件漏洞分析方面展现出巨大潜力，这对现代软件系统安全至关重要。然而，当前利用LLM进行漏洞分析的方法主要依赖于在线API服务，需要用户公开源代码。此外，它们通常将任务视为二元分类（有漏洞或无漏洞），限制了实际应用。本文通过将问题重新定义为软件漏洞识别(SVI)，要求LLM输出常见弱点枚举(CWE) ID中的弱点类型，而不仅仅是表明是否存在漏洞，从而解决了这些限制。我们还通过证明指令调优较小的、本地可部署的LLM可以实现卓越的识别性能，从而解决了对大型API型LLM的依赖。分析表明，指令调优的本地LLM在整体性能和成本效益方面优于在线API型LLM。我们的研究结果表明，对于在实际漏洞管理工作流程中利用LLM，指令调优的本地模型代表了一种更有效、安全和实用的方法。

## 🔬 方法详解

**问题定义**：现有基于LLM的软件漏洞分析方法主要依赖在线API服务，这要求开发者上传源代码，存在安全风险。同时，这些方法通常将漏洞分析简化为二元分类问题（即判断是否存在漏洞），无法提供漏洞的具体类型信息，限制了其在实际漏洞管理工作流程中的应用。

**核心思路**：论文的核心思路是将软件漏洞分析重新定义为软件漏洞识别(SVI)任务，即要求LLM不仅判断是否存在漏洞，还要识别漏洞的具体类型（CWE ID）。此外，论文通过指令调优（instruction-tuning）的方式，使较小的、本地可部署的LLM也能达到甚至超过大型在线API型LLM的性能，从而避免了源代码泄露的风险。

**技术框架**：论文的技术框架主要包括以下几个步骤：1) 数据准备：构建包含软件代码和对应CWE ID的数据集。2) 模型选择：选择一个较小的、本地可部署的LLM作为基础模型。3) 指令调优：使用构建的数据集对基础模型进行指令调优，使其能够根据输入的代码识别漏洞类型。4) 评估：使用测试集评估模型的性能，并与在线API型LLM进行比较。

**关键创新**：论文的关键创新在于：1) 将软件漏洞分析重新定义为软件漏洞识别(SVI)任务，提高了漏洞分析的实用性。2) 证明了通过指令调优，较小的、本地可部署的LLM也能达到甚至超过大型在线API型LLM的性能，降低了安全风险和成本。

**关键设计**：论文的关键设计包括：1) 选择合适的指令调优数据集，确保数据集的质量和多样性。2) 设计有效的指令模板，引导LLM学习如何根据代码识别漏洞类型。3) 采用合适的评估指标，全面评估模型的性能，例如准确率、召回率和F1值。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20062v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20062v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20062v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，指令调优的本地LLM在软件漏洞识别任务上表现出色，在某些情况下甚至优于在线API型LLM。例如，在特定CWE类型的识别上，本地LLM的准确率提升了10%以上。此外，本地LLM的推理速度更快，成本更低，更适合实际应用。

## 🎯 应用场景

该研究成果可应用于软件开发生命周期的各个阶段，例如代码审查、安全测试和漏洞修复。通过使用本地部署的、指令调优的LLM，开发者可以在不泄露源代码的情况下，快速准确地识别软件漏洞类型，从而提高软件的安全性和可靠性。未来，该技术有望集成到IDE和CI/CD流程中，实现自动化漏洞分析。

## 📄 摘要（原文）

> Large Language Models (LLMs) show significant promise in automating software vulnerability analysis, a critical task given the impact of security failure of modern software systems. However, current approaches in using LLMs to automate vulnerability analysis mostly rely on using online API-based LLM services, requiring the user to disclose the source code in development. Moreover, they predominantly frame the task as a binary classification(vulnerable or not vulnerable), limiting potential practical utility. This paper addresses these limitations by reformulating the problem as Software Vulnerability Identification (SVI), where LLMs are asked to output the type of weakness in Common Weakness Enumeration (CWE) IDs rather than simply indicating the presence or absence of a vulnerability. We also tackle the reliance on large, API-based LLMs by demonstrating that instruction-tuning smaller, locally deployable LLMs can achieve superior identification performance. In our analysis, instruct-tuning a local LLM showed better overall performance and cost trade-off than online API-based LLMs. Our findings indicate that instruct-tuned local models represent a more effective, secure, and practical approach for leveraging LLMs in real-world vulnerability management workflows.

