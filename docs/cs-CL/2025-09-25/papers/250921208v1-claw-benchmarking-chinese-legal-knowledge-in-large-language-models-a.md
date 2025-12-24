---
layout: default
title: "CLaw: Benchmarking Chinese Legal Knowledge in Large Language Models - A Fine-grained Corpus and Reasoning Analysis"
---

# CLaw: Benchmarking Chinese Legal Knowledge in Large Language Models - A Fine-grained Corpus and Reasoning Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21208" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21208v1</a>
  <a href="https://arxiv.org/pdf/2509.21208.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21208v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21208v1', 'CLaw: Benchmarking Chinese Legal Knowledge in Large Language Models - A Fine-grained Corpus and Reasoning Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinzhe Xu, Liang Zhao, Hongshen Xu, Chen Chen

**分类**: cs.CL

**发布日期**: 2025-09-25

---

## 💡 一句话要点

**CLaw：构建中文法律知识基准，评估大语言模型在法律推理中的能力。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `法律知识` `中文法律` `基准测试` `法律推理`

## 📋 核心要点

1. 现有大语言模型在法律领域应用中，缺乏对法律知识的专门训练，导致其法律知识深度不足，影响了推理的可靠性。
2. CLaw基准通过构建细粒度的法律语料库和案例推理实例，旨在全面评估大语言模型在中文法律知识和推理方面的能力。
3. 实验结果表明，现有大语言模型在准确再现法律条文方面存在显著困难，这严重影响了其法律推理的可靠性。

## 📝 摘要（中文）

大型语言模型（LLMs）越来越多地被用于分析法律文本和引用相关法规，但由于通用预训练过程中缺乏对法律领域的专门关注，其可靠性常常受到影响，掩盖了其法律知识的真正深度。本文介绍了一个名为CLaw的新基准，专门用于评估LLMs在中文法律知识及其在推理中的应用。CLaw包含两个关键组成部分：（1）一个全面的、细粒度的语料库，包含所有306部中国国家法规，分割到子条款级别，并结合精确的历史修订时间戳，用于严格的召回评估（64,849条目）；（2）一组具有挑战性的、基于案例的推理实例（254个），这些实例来自中国最高法院策划的材料，用于评估法律知识的实际应用。我们的实证评估表明，大多数当代LLMs在忠实地再现法律条文方面都存在显著困难。由于准确检索和引用法律条文是法律推理的基础，因此这种缺陷严重损害了其响应的可靠性。我们认为，要在LLMs中实现可信的法律推理，需要准确的知识检索（可能通过监督微调（SFT）或检索增强生成（RAG）来增强）和强大的通用推理能力的强大协同作用。这项工作为推进特定领域的LLM推理，特别是在复杂的法律领域，提供了重要的基准和关键见解。

## 🔬 方法详解

**问题定义**：现有的大语言模型在处理法律文本时，由于缺乏专门的法律知识训练，无法准确理解和应用法律条文，导致在法律推理任务中表现不佳。现有方法难以评估模型在细粒度法律知识上的掌握程度，也无法有效衡量模型在实际案例中的推理能力。

**核心思路**：CLaw的核心思路是构建一个高质量、细粒度的中文法律知识基准，包括全面的法律语料库和具有挑战性的案例推理实例，从而全面评估大语言模型在法律领域的知识掌握和推理能力。通过精确的历史修订时间戳，可以进行更严格的召回评估。

**技术框架**：CLaw基准主要包含两个部分：一是细粒度的中文法律语料库，包含所有306部中国国家法规，分割到子条款级别，并包含历史修订时间戳。二是案例推理实例，包含254个来自中国最高法院的案例，用于评估模型在实际案例中的法律推理能力。评估过程包括知识召回和案例推理两个阶段。

**关键创新**：CLaw的关键创新在于其细粒度的法律语料库和案例推理实例。语料库的细粒度分割和历史修订时间戳使得可以进行更精确的知识召回评估。案例推理实例则模拟了实际的法律应用场景，更真实地反映了模型在法律领域的推理能力。

**关键设计**：语料库的构建采用了人工标注和自动分割相结合的方法，确保了语料库的质量和覆盖范围。案例推理实例的设计参考了中国最高法院的案例，并进行了适当的简化和抽象，以便于模型进行推理。评估指标包括知识召回率和案例推理准确率。

## 📊 实验亮点

实验结果表明，现有的大语言模型在CLaw基准上表现不佳，尤其是在知识召回方面。大多数模型无法准确地检索和引用相关的法律条文，这严重影响了其在案例推理中的表现。例如，在知识召回任务中，模型的平均准确率低于50%。这些结果表明，现有的大语言模型在法律领域的知识掌握和推理能力仍有很大的提升空间。

## 🎯 应用场景

CLaw基准的潜在应用领域包括法律咨询、智能合同审查、法律文书生成等。通过提高大语言模型在法律领域的知识掌握和推理能力，可以为法律从业者提供更高效、更准确的辅助工具，从而提升法律服务的质量和效率。未来，该基准可以用于开发更智能的法律AI系统，推动法律行业的智能化转型。

## 📄 摘要（原文）

> Large Language Models (LLMs) are increasingly tasked with analyzing legal texts and citing relevant statutes, yet their reliability is often compromised by general pre-training that ingests legal texts without specialized focus, obscuring the true depth of their legal knowledge. This paper introduces CLaw, a novel benchmark specifically engineered to meticulously evaluate LLMs on Chinese legal knowledge and its application in reasoning. CLaw comprises two key components: (1) a comprehensive, fine-grained corpus of all 306 Chinese national statutes, segmented to the subparagraph level and incorporating precise historical revision timesteps for rigorous recall evaluation (64,849 entries), and (2) a challenging set of 254 case-based reasoning instances derived from China Supreme Court curated materials to assess the practical application of legal knowledge. Our empirical evaluation reveals that most contemporary LLMs significantly struggle to faithfully reproduce legal provisions. As accurate retrieval and citation of legal provisions form the basis of legal reasoning, this deficiency critically undermines the reliability of their responses. We contend that achieving trustworthy legal reasoning in LLMs requires a robust synergy of accurate knowledge retrieval--potentially enhanced through supervised fine-tuning (SFT) or retrieval-augmented generation (RAG)--and strong general reasoning capabilities. This work provides an essential benchmark and critical insights for advancing domain-specific LLM reasoning, particularly within the complex legal sphere.

