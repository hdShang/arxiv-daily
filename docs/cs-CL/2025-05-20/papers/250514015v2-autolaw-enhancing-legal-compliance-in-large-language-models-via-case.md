---
layout: default
title: AUTOLAW: Enhancing Legal Compliance in Large Language Models via Case Law Generation and Jury-Inspired Deliberation
---

# AUTOLAW: Enhancing Legal Compliance in Large Language Models via Case Law Generation and Jury-Inspired Deliberation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14015" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14015v2</a>
  <a href="https://arxiv.org/pdf/2505.14015.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14015v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14015v2', 'AUTOLAW: Enhancing Legal Compliance in Large Language Models via Case Law Generation and Jury-Inspired Deliberation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tai D. Nguyen, Long H. Pham, Jun Sun

**分类**: cs.CL

**发布日期**: 2025-05-20 (更新: 2025-06-19)

---

## 💡 一句话要点

**提出AutoLaw以解决法律合规性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `法律合规` `大型语言模型` `对抗性数据生成` `陪审团审议` `动态合成案例法`

## 📋 核心要点

1. 现有法律评估方法缺乏适应性，无法有效应对地方性法律的多样性，限制了其在动态监管环境中的应用。
2. AutoLaw通过对抗性数据生成和陪审团启发的审议过程，动态合成案例法以适应地方法规，提升法律合规性。
3. 实验结果显示，AutoLaw在三个基准测试中显著提高了违规检测率，证明了其在法律合规性评估中的有效性。

## 📝 摘要（中文）

随着领域特定的大型语言模型（LLMs）在法律等领域的快速发展，亟需考虑区域法律差异的框架，以确保合规性和可信度。现有的法律评估基准往往缺乏适应性，无法应对多样化的地方性法律背景，限制了其在动态变化的监管环境中的实用性。为了解决这些问题，本文提出了AutoLaw，一个结合对抗性数据生成与陪审团启发的审议过程的新型违规检测框架，以增强LLMs的法律合规性。与静态方法不同，AutoLaw动态合成案例法以反映地方法规，并利用基于LLM的“陪审员”模拟司法决策。通过在三个基准（Law-SG、Case-SG和Unfair-TOS）上的评估，结果表明AutoLaw在提高违规检测率方面的有效性，展示了其在法律敏感应用中的可扩展性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有法律评估方法在适应地方性法律差异方面的不足，尤其是在动态变化的监管环境中，现有方法无法有效检测法律合规性问题。

**核心思路**：AutoLaw的核心思路是结合对抗性数据生成与陪审团启发的审议过程，通过动态合成案例法来反映地方法规，并利用LLM模拟陪审员的决策过程，以提高法律合规性。

**技术框架**：AutoLaw的整体架构包括两个主要模块：对抗性数据生成模块和陪审团审议模块。前者负责生成符合地方法律的案例法，后者则通过对生成的案例进行审议，模拟司法决策过程。

**关键创新**：AutoLaw的最大创新在于其动态合成案例法的能力和陪审团启发的审议机制，这与传统静态法律评估方法形成鲜明对比，能够更好地适应地方法律的变化。

**关键设计**：在关键设计方面，AutoLaw采用了基于LLM的陪审员选择机制，通过对生成案例的法律专业性进行评分，确保审议过程的公正性和准确性。

## 📊 实验亮点

实验结果表明，AutoLaw在Law-SG、Case-SG和Unfair-TOS三个基准测试中，利用对抗性数据生成显著提高了LLM的区分能力，而陪审团投票策略则使违规检测率显著提升，展示了该框架的有效性和适应性。

## 🎯 应用场景

该研究的潜在应用领域包括法律合规性检测、法律咨询服务和智能法律助手等。AutoLaw能够为法律专业人士提供更为精准的合规性评估工具，提升法律服务的效率与准确性，未来可能在法律技术行业产生深远影响。

## 📄 摘要（原文）

> The rapid advancement of domain-specific large language models (LLMs) in fields like law necessitates frameworks that account for nuanced regional legal distinctions, which are critical for ensuring compliance and trustworthiness. Existing legal evaluation benchmarks often lack adaptability and fail to address diverse local contexts, limiting their utility in dynamically evolving regulatory landscapes. To address these gaps, we propose AutoLaw, a novel violation detection framework that combines adversarial data generation with a jury-inspired deliberation process to enhance legal compliance of LLMs. Unlike static approaches, AutoLaw dynamically synthesizes case law to reflect local regulations and employs a pool of LLM-based "jurors" to simulate judicial decision-making. Jurors are ranked and selected based on synthesized legal expertise, enabling a deliberation process that minimizes bias and improves detection accuracy. Evaluations across three benchmarks: Law-SG, Case-SG (legality), and Unfair-TOS (policy), demonstrate AutoLaw's effectiveness: adversarial data generation improves LLM discrimination, while the jury-based voting strategy significantly boosts violation detection rates. Our results highlight the framework's ability to adaptively probe legal misalignments and deliver reliable, context-aware judgments, offering a scalable solution for evaluating and enhancing LLMs in legally sensitive applications.

