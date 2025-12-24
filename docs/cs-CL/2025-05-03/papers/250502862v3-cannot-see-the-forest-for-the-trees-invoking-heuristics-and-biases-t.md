---
layout: default
title: "Cannot See the Forest for the Trees: Invoking Heuristics and Biases to Elicit Irrational Choices of LLMs"
---

# Cannot See the Forest for the Trees: Invoking Heuristics and Biases to Elicit Irrational Choices of LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02862" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02862v3</a>
  <a href="https://arxiv.org/pdf/2505.02862.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02862v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02862v3', 'Cannot See the Forest for the Trees: Invoking Heuristics and Biases to Elicit Irrational Choices of LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haoming Yang, Ke Ma, Xiaojun Jia, Yingfei Sun, Qianqian Xu, Qingming Huang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-03 (更新: 2025-06-27)

---

## 💡 一句话要点

**提出ICRT框架以解决LLMs的安全机制脆弱问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `越狱攻击` `大型语言模型` `安全机制` `启发式` `有害性评估` `认知分解` `相关性偏见` `排名聚合`

## 📋 核心要点

1. 现有方法往往依赖暴力优化或手动设计，未能有效揭示LLMs在现实场景中的潜在风险。
2. 我们提出的ICRT框架通过认知分解和相关性偏见，简化恶意提示并增强语义对齐，从而诱导有害输出。
3. 实验结果显示，ICRT能够有效绕过主流LLMs的安全机制，生成高风险内容，提供了新的防御思路。

## 📝 摘要（中文）

尽管大型语言模型（LLMs）表现出色，但它们仍然容易受到越狱攻击，可能会破坏其安全机制。现有研究通常依赖于暴力优化或手动设计，未能揭示现实场景中的潜在风险。为此，我们提出了一种新颖的越狱攻击框架ICRT，灵感来源于人类认知中的启发式和偏见。我们利用简化效应，通过认知分解降低恶意提示的复杂性，同时利用相关性偏见重新组织提示，有效增强语义对齐并诱导有害输出。此外，我们引入了一种基于排名的有害性评估指标，超越传统的成功与失败二元范式，通过使用排名聚合方法（如Elo、HodgeRank和Rank Centrality）全面量化生成内容的有害性。实验结果表明，我们的方法能够持续绕过主流LLMs的安全机制并生成高风险内容，为越狱攻击风险提供了深入见解，并有助于更强的防御策略。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型（LLMs）在面对越狱攻击时的安全脆弱性。现有方法多依赖于暴力优化或手动设计，未能有效识别和应对现实场景中的潜在风险。

**核心思路**：我们提出的ICRT框架灵感来源于人类认知中的启发式和偏见，通过认知分解降低恶意提示的复杂性，同时利用相关性偏见重新组织提示，以增强语义对齐并诱导有害输出。

**技术框架**：ICRT框架主要包括两个阶段：第一阶段是通过认知分解简化恶意提示，第二阶段是利用相关性偏见对提示进行重组。整个流程通过引入基于排名的有害性评估指标进行评估。

**关键创新**：本研究的创新点在于引入了基于排名的有害性评估方法，超越了传统的二元成功与失败评估，能够更全面地量化生成内容的有害性。

**关键设计**：在参数设置上，我们采用了排名聚合方法如Elo、HodgeRank和Rank Centrality，以确保评估的准确性和有效性。

## 📊 实验亮点

实验结果表明，ICRT框架能够有效绕过主流LLMs的安全机制，生成高风险内容。与传统方法相比，我们的评估指标在量化有害性方面表现出更高的准确性和全面性，提供了新的研究视角。

## 🎯 应用场景

该研究的潜在应用领域包括安全性评估、内容生成和人机交互等。通过深入理解LLMs的脆弱性，能够为开发更强的防御策略提供理论支持，进而提升人工智能系统的安全性和可靠性。

## 📄 摘要（原文）

> Despite the remarkable performance of Large Language Models (LLMs), they remain vulnerable to jailbreak attacks, which can compromise their safety mechanisms. Existing studies often rely on brute-force optimization or manual design, failing to uncover potential risks in real-world scenarios. To address this, we propose a novel jailbreak attack framework, ICRT, inspired by heuristics and biases in human cognition. Leveraging the simplicity effect, we employ cognitive decomposition to reduce the complexity of malicious prompts. Simultaneously, relevance bias is utilized to reorganize prompts, enhancing semantic alignment and inducing harmful outputs effectively. Furthermore, we introduce a ranking-based harmfulness evaluation metric that surpasses the traditional binary success-or-failure paradigm by employing ranking aggregation methods such as Elo, HodgeRank, and Rank Centrality to comprehensively quantify the harmfulness of generated content. Experimental results show that our approach consistently bypasses mainstream LLMs' safety mechanisms and generates high-risk content, providing insights into jailbreak attack risks and contributing to stronger defense strategies.

