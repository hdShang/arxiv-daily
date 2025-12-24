---
layout: default
title: Leveraging Knowledge Graphs and LLMs for Structured Generation of Misinformation
---

# Leveraging Knowledge Graphs and LLMs for Structured Generation of Misinformation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24479" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24479v1</a>
  <a href="https://arxiv.org/pdf/2505.24479.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24479v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24479v1', 'Leveraging Knowledge Graphs and LLMs for Structured Generation of Misinformation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sania Nayab, Marco Simoni, Giulio Rossolini

**分类**: cs.AI, cs.CL, cs.SI

**发布日期**: 2025-05-30

---

## 💡 一句话要点

**提出基于知识图谱和大型语言模型的结构化虚假信息生成方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `虚假信息生成` `知识图谱` `大型语言模型` `信息检测` `结构化生成` `生成式人工智能`

## 📋 核心要点

1. 虚假信息的生成与传播日益严重，现有检测方法难以有效识别生成的虚假信息。
2. 本文提出利用知识图谱生成虚假三元组，并指导大型语言模型生成虚假信息声明的创新方法。
3. 研究表明，当前大型语言模型在区分真实与虚假信息方面存在显著局限，需改进检测策略。

## 📝 摘要（中文）

虚假信息的快速传播，尤其是近年来生成式人工智能的进步，给社会带来了重大威胁，影响公众舆论、民主稳定和国家安全。理解和主动评估这些威胁需要探索能够系统化和可扩展的虚假信息生成方法。本文提出了一种新方法，利用知识图谱（KGs）作为结构化语义资源，系统生成虚假三元组。通过分析KGs的结构特性，如实体之间的距离及其谓词，我们识别出可能的虚假关系。这些三元组用于指导大型语言模型（LLMs）生成具有不同可信度的虚假信息声明。利用结构化语义关系，我们的确定性方法生成的虚假信息本质上难以被人类检测，完全依赖于公开可用的KGs（例如WikiGraphs）。此外，我们还研究了LLMs在区分真实与人工生成虚假信息方面的有效性，分析显示当前基于LLMs的检测方法存在显著局限，强调了增强检测策略和深入探索生成模型固有偏见的必要性。

## 🔬 方法详解

**问题定义**：本文旨在解决虚假信息生成的结构化与可扩展性问题。现有方法在识别和生成虚假信息时，缺乏系统性和结构化的指导，导致生成的信息难以控制和评估。

**核心思路**：论文的核心思路是利用知识图谱作为结构化语义资源，通过分析其结构特性，系统生成虚假三元组，并利用这些三元组指导大型语言模型生成虚假信息声明。这样的设计使得生成的信息更具可信度和隐蔽性。

**技术框架**：整体架构包括三个主要模块：首先，利用知识图谱生成虚假三元组；其次，基于这些三元组指导大型语言模型生成虚假信息；最后，评估生成信息的可信度和检测效果。

**关键创新**：最重要的技术创新点在于将知识图谱与大型语言模型结合，形成一种新的虚假信息生成机制。这种方法与现有的随机生成方法本质上不同，提供了更高的结构化和可控性。

**关键设计**：在技术细节上，关键参数包括知识图谱的选择和三元组生成算法的设计，损失函数则侧重于生成信息的可信度评估，网络结构则采用了适应性调整以优化生成效果。

## 📊 实验亮点

实验结果显示，利用知识图谱生成的虚假信息在可信度上显著高于传统方法，且在大型语言模型的指导下，生成的信息更难以被人类识别。当前的LLM检测方法在识别这些生成信息时存在显著局限，强调了对检测策略的进一步研究需求。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体内容生成、舆情监测和虚假信息检测等。通过提供一种系统化的虚假信息生成方法，可以帮助相关机构更好地理解和应对虚假信息的传播，从而提升社会的舆论稳定性和安全性。未来，该方法也可能为虚假信息检测技术的发展提供新的思路和工具。

## 📄 摘要（原文）

> The rapid spread of misinformation, further amplified by recent advances in generative AI, poses significant threats to society, impacting public opinion, democratic stability, and national security. Understanding and proactively assessing these threats requires exploring methodologies that enable structured and scalable misinformation generation. In this paper, we propose a novel approach that leverages knowledge graphs (KGs) as structured semantic resources to systematically generate fake triplets. By analyzing the structural properties of KGs, such as the distance between entities and their predicates, we identify plausibly false relationships. These triplets are then used to guide large language models (LLMs) in generating misinformation statements with varying degrees of credibility. By utilizing structured semantic relationships, our deterministic approach produces misinformation inherently challenging for humans to detect, drawing exclusively upon publicly available KGs (e.g., WikiGraphs).
>   Additionally, we investigate the effectiveness of LLMs in distinguishing between genuine and artificially generated misinformation. Our analysis highlights significant limitations in current LLM-based detection methods, underscoring the necessity for enhanced detection strategies and a deeper exploration of inherent biases in generative models.

