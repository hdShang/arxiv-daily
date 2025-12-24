---
layout: default
title: "LLMSynthor: Macro-Aligned Micro-Records Synthesis with Large Language Models"
---

# LLMSynthor: Macro-Aligned Micro-Records Synthesis with Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14752" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14752v2</a>
  <a href="https://arxiv.org/pdf/2505.14752.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14752v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14752v2', 'LLMSynthor: Macro-Aligned Micro-Records Synthesis with Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yihong Tang, Menglin Kong, Junlin He, Tong Nie, Lijun Sun

**分类**: cs.LG

**发布日期**: 2025-05-20 (更新: 2025-10-11)

---

## 💡 一句话要点

**提出LLMSynthor以解决宏观数据与微观记录不一致问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `宏观数据` `微观记录` `数据合成` `社会科学` `城市研究` `统计保真度`

## 📋 核心要点

1. 现有方法在大规模收集细粒度微观数据时面临挑战，导致宏观数据与微观行为不一致。
2. LLMSynthor通过将预训练的LLM转化为宏观感知的模拟器，生成与目标宏观统计一致的微观记录。
3. 跨领域实验表明，LLMSynthor在现实性和统计保真度上表现优异，具有广泛的应用潜力。

## 📝 摘要（中文）

宏观对齐的微观记录对于社会科学和城市研究中的可信模拟至关重要。现有方法难以大规模收集细粒度数据，LLMSynthor通过将预训练的大型语言模型（LLM）转变为宏观感知的模拟器，生成与目标宏观统计一致的真实微观记录。该方法通过迭代生成合成数据集，最小化合成记录与目标聚合之间的差异。通过将LLM视为非参数copula，模型能够捕捉变量之间的真实联合依赖关系。LLM提议采样提高了效率，指导LLM提出针对性的记录批次，从而有效纠正差异，同时保持模型先验的真实性。跨领域评估显示，LLMSynthor在现实性、统计保真度和实际效用方面表现出色，适用于经济学、社会科学和城市研究。

## 🔬 方法详解

**问题定义**：本论文旨在解决宏观数据与微观记录之间的不一致性问题。现有方法在大规模收集细粒度数据时存在实用性不足的痛点，导致模拟结果的可信度降低。

**核心思路**：LLMSynthor的核心思路是利用预训练的大型语言模型（LLM）作为宏观感知的模拟器，生成符合目标宏观统计的微观记录。通过迭代生成数据集，最小化合成记录与目标聚合之间的差异，从而提高模拟的真实性。

**技术框架**：整体架构包括数据生成、差异最小化和提议采样三个主要模块。在每一步中，LLM生成记录批次，并通过反馈机制调整生成策略，以减少与目标统计的偏差。

**关键创新**：最重要的技术创新在于将LLM视为非参数copula，能够捕捉变量之间的真实联合依赖关系。这一设计使得生成的微观记录在统计特性上更为真实，与现有方法相比具有显著优势。

**关键设计**：在参数设置上，LLM提议采样通过指定变量范围和数量来引导生成过程，确保生成的记录既符合目标统计，又保持真实感。损失函数设计上，重点关注合成记录与目标聚合之间的差异，确保生成的微观数据在统计上具有保真度。

## 📊 实验亮点

实验结果显示，LLMSynthor在多个领域（如流动性、电子商务和人口）中表现出强大的现实性和统计保真度。与基线方法相比，LLMSynthor在生成的微观记录的真实性和一致性上有显著提升，具体性能数据未提供，但整体效果显著。

## 🎯 应用场景

LLMSynthor的研究成果在经济学、社会科学和城市研究等领域具有广泛的应用潜力。通过生成与真实行为一致的微观记录，研究人员可以更准确地模拟复杂社会现象，如疫情传播、人口流动和电子商务行为，从而为政策制定和城市规划提供更可靠的数据支持。

## 📄 摘要（原文）

> Macro-aligned micro-records are crucial for credible simulations in social science and urban studies. For example, epidemic models are only reliable when individual-level mobility and contacts mirror real behavior, while aggregates match real-world statistics like case counts or travel flows. However, collecting such fine-grained data at scale is impractical, leaving researchers with only macro-level data. LLMSynthor addresses this by turning a pretrained LLM into a macro-aware simulator that generates realistic micro-records consistent with target macro-statistics. It iteratively builds synthetic datasets: in each step, the LLM generates batches of records to minimize discrepancies between synthetic and target aggregates. Treating the LLM as a nonparametric copula allows the model to capture realistic joint dependencies among variables. To improve efficiency, LLM Proposal Sampling guides the LLM to propose targeted record batches, specifying variable ranges and counts, to efficiently correct discrepancies while preserving realism grounded in the model's priors. Evaluations across domains (mobility, e-commerce, population) show that LLMSynthor achieves strong realism, statistical fidelity, and practical utility, making it broadly applicable to economics, social science, and urban studies.

