---
layout: default
title: "TableMoE: Neuro-Symbolic Routing for Structured Expert Reasoning in Multimodal Table Understanding"
---

# TableMoE: Neuro-Symbolic Routing for Structured Expert Reasoning in Multimodal Table Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21393" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21393v1</a>
  <a href="https://arxiv.org/pdf/2506.21393.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21393v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21393v1', 'TableMoE: Neuro-Symbolic Routing for Structured Expert Reasoning in Multimodal Table Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junwen Zhang, Pu Chen, Yin Zhang

**分类**: cs.AI

**发布日期**: 2025-06-26

**备注**: 43 pages and 11 figures

---

## 💡 一句话要点

**提出TableMoE以解决多模态表格理解中的复杂性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态理解` `神经符号推理` `表格数据` `结构化推理` `专家模型` `数据集构建` `性能评估`

## 📋 核心要点

1. 现有多模态大型语言模型在处理复杂表格时表现不佳，尤其是在结构复杂和视觉退化的情况下。
2. 本文提出TableMoE，通过神经符号路由机制动态路由表格元素到专门的专家，以实现更稳健的推理。
3. 实验结果显示，TableMoE在多个WildStruct基准上显著超越现有模型，验证了其有效性和鲁棒性。

## 📝 摘要（中文）

在现实场景中，多模态表格理解面临结构复杂性、符号密度和视觉退化等挑战。现有的多模态大型语言模型在这些WildStruct条件下表现不佳。为此，本文提出了TableMoE，一种专为多模态表格数据设计的神经符号混合连接专家架构。TableMoE引入了创新的神经符号路由机制，通过预测潜在语义令牌角色并动态路由表格元素到专门的专家，从而实现稳健的结构化推理。我们还构建了大规模的TableMoE-Align数据集，并发布了四个WildStruct基准进行评估，实验结果表明TableMoE显著超越现有最先进模型。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态表格理解中的结构复杂性和视觉退化问题。现有方法在这些WildStruct条件下表现不佳，导致性能和泛化能力有限。

**核心思路**：TableMoE的核心思路是通过神经符号路由机制，预测表格元素的潜在语义角色，并将其动态路由到专门的专家，以实现更高效的结构化推理。

**技术框架**：TableMoE采用混合连接专家架构，主要模块包括神经符号路由机制、专家模型（如Table-to-HTML、Table-to-JSON、Table-to-Code）以及基于信心的门控策略。

**关键创新**：最重要的创新是神经符号路由机制，它通过符号推理图来指导路由决策，显著提升了模型在复杂表格理解中的表现。

**关键设计**：在设计中，TableMoE使用了信心感知的门控策略，确保表格元素能够被有效地分配给合适的专家，同时引入了大规模的TableMoE-Align数据集进行预训练。

## 📊 实验亮点

实验结果表明，TableMoE在四个WildStruct基准上均显著超越现有最先进模型，具体性能提升幅度达到XX%（具体数据未知），验证了其在复杂表格理解中的有效性和鲁棒性。

## 🎯 应用场景

TableMoE的潜在应用场景包括金融、科学、生物医学和工业等领域，能够有效处理复杂的表格数据，提升数据分析和决策支持的能力。未来，该模型有望在多模态数据理解和智能问答系统中发挥重要作用。

## 📄 摘要（原文）

> Multimodal understanding of tables in real-world contexts is challenging due to the complexity of structure, symbolic density, and visual degradation (blur, skew, watermarking, incomplete structures or fonts, multi-span or hierarchically nested layouts). Existing multimodal large language models (MLLMs) struggle with such WildStruct conditions, resulting in limited performance and poor generalization. To address these challenges, we propose TableMoE, a neuro-symbolic Mixture-of-Connector-Experts (MoCE) architecture specifically designed for robust, structured reasoning over multimodal table data. TableMoE features an innovative Neuro-Symbolic Routing mechanism, which predicts latent semantic token roles (e.g., header, data cell, axis, formula) and dynamically routes table elements to specialized experts (Table-to-HTML, Table-to-JSON, Table-to-Code) using a confidence-aware gating strategy informed by symbolic reasoning graphs. To facilitate effective alignment-driven pretraining, we introduce the large-scale TableMoE-Align dataset, consisting of 1.2M table-HTML-JSON-code quadruples across finance, science, biomedicine and industry, utilized exclusively for model pretraining. For evaluation, we curate and release four challenging WildStruct benchmarks: WMMFinQA, WMMTatQA, WMMTabDialog, and WMMFinanceMath, designed specifically to stress-test models under real-world multimodal degradation and structural complexity. Experimental results demonstrate that TableMoE significantly surpasses existing state-of-the-art models. Extensive ablation studies validate each core component, emphasizing the critical role of Neuro-Symbolic Routing and structured expert alignment. Through qualitative analyses, we further showcase TableMoE's interpretability and enhanced robustness, underscoring the effectiveness of integrating neuro-symbolic reasoning for multimodal table understanding.

