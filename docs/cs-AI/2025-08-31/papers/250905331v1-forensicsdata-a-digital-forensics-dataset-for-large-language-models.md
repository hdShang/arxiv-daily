---
layout: default
title: "ForensicsData: A Digital Forensics Dataset for Large Language Models"
---

# ForensicsData: A Digital Forensics Dataset for Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05331" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05331v1</a>
  <a href="https://arxiv.org/pdf/2509.05331.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05331v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05331v1', 'ForensicsData: A Digital Forensics Dataset for Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Youssef Chakir, Iyad Lahsen-Cherif

**分类**: cs.CR, cs.AI, cs.CL

**发布日期**: 2025-08-31

**备注**: Accepted to WiMob 2025 (21st International Conference on Wireless and Mobile Computing, Networking and Communications), Marrakesh, Morocco, Oct 20-22, 2025. 6 pages, 5 figures, 5 tables. IEEEtran conference format

---

## 💡 一句话要点

**提出ForensicsData以解决数字取证数据集匮乏问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `数字取证` `恶意软件分析` `数据集构建` `大型语言模型` `问答系统` `网络安全` `研究工具`

## 📋 核心要点

1. 现有数字取证领域缺乏足够的真实数据集，导致研究和工具开发受限。
2. 本文提出ForensicsData数据集，通过实际恶意软件分析报告生成问答上下文三元组，填补数据集空白。
3. 实验结果表明，Gemini 2 Flash模型在内容生成与取证术语对齐方面表现最佳，提升了数据集质量。

## 📝 摘要（中文）

随着网络事件的复杂性增加，数字取证调查人员在证据收集和分析方面面临重大挑战。尽管现实数据集对于支持研究和工具开发至关重要，但由于伦理、法律和隐私问题，公共资源仍然有限。为了解决这一空白，本文介绍了ForensicsData，这是一个来自实际恶意软件分析报告的广泛问答上下文数据集，包含超过5000个问答三元组。该数据集采用独特的工作流程创建，提取结构化数据，利用大型语言模型将其转化为问答格式，并通过专门的评估过程确认其质量。经过评估，Gemini 2 Flash模型在生成内容与取证术语的对齐方面表现最佳。ForensicsData旨在通过支持可重复实验和促进研究社区的合作来推动数字取证的发展。

## 🔬 方法详解

**问题定义**：本文旨在解决数字取证领域中缺乏真实、可用数据集的问题。现有方法在证据收集和分析中面临伦理和法律限制，导致公共资源匮乏。

**核心思路**：通过从实际的恶意软件分析报告中提取信息，构建一个包含问答上下文的丰富数据集，以支持数字取证的研究和工具开发。利用大型语言模型将结构化数据转化为问答格式，确保数据的相关性和准确性。

**技术框架**：整体流程包括数据提取、格式转换和质量评估三个主要模块。首先，从真实的恶意软件分析报告中提取结构化数据；然后，使用大型语言模型将其转化为问答格式；最后，通过专门的评估流程确认数据集的质量。

**关键创新**：ForensicsData数据集的创新之处在于其基于真实案例构建的问答三元组，填补了数字取证领域的数据空白，并通过大型语言模型提升了数据的专业性和实用性。

**关键设计**：在数据生成过程中，采用了特定的参数设置和评估标准，以确保生成内容的质量和准确性。特别是Gemini 2 Flash模型在对齐取证术语方面表现优异，成为数据集构建的关键工具。

## 📊 实验亮点

实验结果显示，Gemini 2 Flash模型在生成内容与取证术语对齐方面表现最佳，显著提升了数据集的质量。具体而言，该模型在问答生成任务中相较于其他模型表现出更高的准确性和一致性，验证了其在数字取证领域的应用价值。

## 🎯 应用场景

ForensicsData数据集具有广泛的应用潜力，尤其在数字取证、网络安全和恶意软件分析等领域。它可以为研究人员提供真实案例支持，促进新工具和方法的开发，提升数字取证的效率和准确性。未来，该数据集可能成为数字取证领域的重要资源，推动相关研究的深入开展。

## 📄 摘要（原文）

> The growing complexity of cyber incidents presents significant challenges for digital forensic investigators, especially in evidence collection and analysis. Public resources are still limited because of ethical, legal, and privacy concerns, even though realistic datasets are necessary to support research and tool developments. To address this gap, we introduce ForensicsData, an extensive Question-Context-Answer (Q-C-A) dataset sourced from actual malware analysis reports. It consists of more than 5,000 Q-C-A triplets. A unique workflow was used to create the dataset, which extracts structured data, uses large language models (LLMs) to transform it into Q-C-A format, and then uses a specialized evaluation process to confirm its quality. Among the models evaluated, Gemini 2 Flash demonstrated the best performance in aligning generated content with forensic terminology. ForensicsData aims to advance digital forensics by enabling reproducible experiments and fostering collaboration within the research community.

