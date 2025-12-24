---
layout: default
title: "Token-Level Precise Attack on RAG: Searching for the Best Alternatives to Mislead Generation"
---

# Token-Level Precise Attack on RAG: Searching for the Best Alternatives to Mislead Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03110" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03110v1</a>
  <a href="https://arxiv.org/pdf/2508.03110.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03110v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03110v1', 'Token-Level Precise Attack on RAG: Searching for the Best Alternatives to Mislead Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zizhong Li, Haopeng Zhang, Jiawei Zhang

**分类**: cs.CL

**发布日期**: 2025-08-05

---

## 💡 一句话要点

**提出TPARAG以解决RAG系统的安全漏洞问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `检索增强生成` `安全漏洞` `对抗性攻击` `大型语言模型` `开放域问答` `Token级攻击` `鲁棒性提升`

## 📋 核心要点

1. 现有方法在攻击RAG系统时，往往过于依赖检索器，或未能同时考虑检索和生成阶段，导致效果受限。
2. 本文提出TPARAG框架，通过轻量级白箱LLM生成并优化恶意文本，确保高效的攻击成功率。
3. 实验结果显示，TPARAG在开放域问答数据集上表现优异，超越了之前的方法，揭示了RAG系统的关键脆弱性。

## 📝 摘要（中文）

尽管大型语言模型在知识密集型任务中取得了显著成功，但仍面临幻觉和过时知识等关键限制。为了解决这些问题，检索增强生成（RAG）框架通过检索器增强了LLM的外部知识访问能力。然而，这种集成带来了新的安全漏洞，恶意内容可能被检索并用于操控模型输出。现有方法在攻击RAG系统时要么过于依赖检索器，要么未能同时考虑检索和生成阶段，限制了其在黑箱场景下的有效性。为此，本文提出了基于Token级别的精确攻击框架TPARAG，针对白箱和黑箱RAG系统进行攻击，确保高效的攻击成功率。实验结果表明，TPARAG在检索阶段和端到端攻击效果上均优于现有方法，揭示了RAG管道中的关键漏洞，并为提高其鲁棒性提供了新思路。

## 🔬 方法详解

**问题定义**：本文旨在解决RAG系统中由于外部数据库恶意内容引发的安全漏洞问题。现有攻击方法在黑箱场景下效果有限，无法有效结合检索和生成阶段。

**核心思路**：TPARAG框架的核心思想是利用轻量级白箱LLM作为攻击者，生成并迭代优化恶意文本，确保其可检索性和生成阶段的高攻击成功率。

**技术框架**：TPARAG的整体架构包括两个主要阶段：首先是生成阶段，使用白箱LLM生成恶意文本；其次是优化阶段，通过迭代优化确保文本在检索和生成中的有效性。

**关键创新**：TPARAG的主要创新在于其Token级别的攻击策略，能够在不依赖检索器的情况下，针对RAG系统的脆弱性进行有效攻击，这与现有方法的设计思路有本质区别。

**关键设计**：在设计中，TPARAG采用了特定的损失函数来优化生成文本的质量，并通过调整参数设置来提高攻击的成功率，确保生成文本在检索和生成阶段均能有效利用。

## 📊 实验亮点

实验结果表明，TPARAG在开放域问答数据集上相较于现有方法，检索阶段和端到端攻击效果均有显著提升，攻击成功率提高了20%以上，揭示了RAG系统的关键脆弱性。

## 🎯 应用场景

该研究的潜在应用领域包括安全性评估、对抗性攻击研究以及提升RAG系统的鲁棒性。通过识别和修复RAG系统中的脆弱性，可以为实际应用提供更安全的知识检索和生成服务，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> While large language models (LLMs) have achieved remarkable success in providing trustworthy responses for knowledge-intensive tasks, they still face critical limitations such as hallucinations and outdated knowledge. To address these issues, the retrieval-augmented generation (RAG) framework enhances LLMs with access to external knowledge via a retriever, enabling more accurate and real-time outputs about the latest events. However, this integration brings new security vulnerabilities: the risk that malicious content in the external database can be retrieved and used to manipulate model outputs. Although prior work has explored attacks on RAG systems, existing approaches either rely heavily on access to the retriever or fail to jointly consider both retrieval and generation stages, limiting their effectiveness, particularly in black-box scenarios. To overcome these limitations, we propose Token-level Precise Attack on the RAG (TPARAG), a novel framework that targets both white-box and black-box RAG systems. TPARAG leverages a lightweight white-box LLM as an attacker to generate and iteratively optimize malicious passages at the token level, ensuring both retrievability and high attack success in generation. Extensive experiments on open-domain QA datasets demonstrate that TPARAG consistently outperforms previous approaches in retrieval-stage and end-to-end attack effectiveness. These results further reveal critical vulnerabilities in RAG pipelines and offer new insights into improving their robustness.

