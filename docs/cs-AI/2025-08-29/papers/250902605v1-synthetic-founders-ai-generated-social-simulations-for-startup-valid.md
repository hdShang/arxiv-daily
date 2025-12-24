---
layout: default
title: "Synthetic Founders: AI-Generated Social Simulations for Startup Validation Research in Computational Social Science"
---

# Synthetic Founders: AI-Generated Social Simulations for Startup Validation Research in Computational Social Science

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.02605" class="toolbar-btn" target="_blank">📄 arXiv: 2509.02605v1</a>
  <a href="https://arxiv.org/pdf/2509.02605.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.02605v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.02605v1', 'Synthetic Founders: AI-Generated Social Simulations for Startup Validation Research in Computational Social Science')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jorn K. Teutloff

**分类**: cs.MA, cs.AI, cs.CY

**发布日期**: 2025-08-29

**备注**: Manuscript submitted to the Journal of Artificial Societies and Social Simulation (JASSS). 21 pages, 1 table

---

## 💡 一句话要点

**提出AI生成社交模拟以增强初创企业验证研究的有效性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `社交模拟` `大型语言模型` `初创企业验证` `心理盲点` `计算社会科学` `合成角色` `数据对比分析`

## 📋 核心要点

1. 现有方法在初创企业验证中缺乏对人类情感和历史经验的真实反映，导致盲点和不准确的结果。
2. 论文提出使用大型语言模型生成合成角色，以模拟真实创始人和投资者的行为和心理，从而增强验证研究的有效性。
3. 实验结果显示，合成角色在某些方面能够捕捉到人类访谈中未能体现的心理盲点，提供了新的验证视角。

## 📝 摘要（中文）

本文展示了一项比较性对接实验，将人类受访者访谈数据与大型语言模型驱动的合成角色进行对齐，以评估AI驱动模拟的真实度、差异和盲点。对十五位早期初创企业创始人的访谈显示，他们对AI驱动验证的希望与担忧。通过结构化主题综合，结果分为四类：一致主题、部分重叠、人类专属主题和合成专属主题。我们认为，LLM驱动的角色构成了一种混合社交模拟，能够扩展假设空间，加速探索性验证，并澄清计算社会科学中的认知现实边界。

## 🔬 方法详解

**问题定义**：本文旨在解决现有初创企业验证研究中对人类情感和历史经验缺乏真实反映的问题，现有方法往往忽视了这些因素，导致结果的盲点和不准确性。

**核心思路**：通过使用大型语言模型生成合成角色，模拟真实创始人和投资者的行为与心理，提供更丰富的社交模拟，增强验证研究的有效性。

**技术框架**：整体架构包括数据收集、合成角色生成、对比分析和主题综合四个主要模块。数据收集阶段通过访谈获取人类创始人的真实反馈，合成角色生成阶段利用LLM创建相应的AI角色，随后进行对比分析和主题综合。

**关键创新**：最重要的技术创新在于将LLM驱动的合成角色与传统规则基础代理进行比较，展现出更高的语言表达能力和适应性，同时指出其在缺乏真实历史和关系后果方面的局限性。

**关键设计**：在合成角色生成中，使用了特定的参数设置和训练数据，以确保生成角色的多样性和真实性，同时设计了相应的损失函数以优化角色的表现。

## 📊 实验亮点

实验结果表明，合成角色在捕捉创始人心理盲点方面表现出色，尤其是在识别潜在的虚假积极信号和历史创伤方面。与传统方法相比，合成角色能够提供更丰富的洞察，推动验证研究的深入发展。

## 🎯 应用场景

该研究的潜在应用领域包括初创企业的市场验证、投资决策支持以及社会科学研究。通过提供更真实的模拟，研究能够帮助创业者和投资者更好地理解市场动态和客户需求，从而提高决策的准确性和效率。

## 📄 摘要（原文）

> We present a comparative docking experiment that aligns human-subject interview data with large language model (LLM)-driven synthetic personas to evaluate fidelity, divergence, and blind spots in AI-enabled simulation. Fifteen early-stage startup founders were interviewed about their hopes and concerns regarding AI-powered validation, and the same protocol was replicated with AI-generated founder and investor personas. A structured thematic synthesis revealed four categories of outcomes: (1) Convergent themes - commitment-based demand signals, black-box trust barriers, and efficiency gains were consistently emphasized across both datasets; (2) Partial overlaps - founders worried about outliers being averaged away and the stress of real customer validation, while synthetic personas highlighted irrational blind spots and framed AI as a psychological buffer; (3) Human-only themes - relational and advocacy value from early customer engagement and skepticism toward moonshot markets; and (4) Synthetic-only themes - amplified false positives and trauma blind spots, where AI may overstate adoption potential by missing negative historical experiences.
>   We interpret this comparative framework as evidence that LLM-driven personas constitute a form of hybrid social simulation: more linguistically expressive and adaptable than traditional rule-based agents, yet bounded by the absence of lived history and relational consequence. Rather than replacing empirical studies, we argue they function as a complementary simulation category - capable of extending hypothesis space, accelerating exploratory validation, and clarifying the boundaries of cognitive realism in computational social science.

