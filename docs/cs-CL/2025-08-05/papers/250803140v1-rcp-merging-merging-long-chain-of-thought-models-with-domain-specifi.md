---
layout: default
title: "RCP-Merging: Merging Long Chain-of-Thought Models with Domain-Specific Models by Considering Reasoning Capability as Prior"
---

# RCP-Merging: Merging Long Chain-of-Thought Models with Domain-Specific Models by Considering Reasoning Capability as Prior

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03140" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03140v1</a>
  <a href="https://arxiv.org/pdf/2508.03140.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03140v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03140v1', 'RCP-Merging: Merging Long Chain-of-Thought Models with Domain-Specific Models by Considering Reasoning Capability as Prior')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junyao Yang, Jianwei Wang, Huiping Zhuang, Cen Chen, Ziqian Zeng

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-05

**备注**: 15 pages, 7 figures

---

## 💡 一句话要点

**提出RCP-Merging以解决长链推理模型与领域特定模型融合问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长链推理` `模型融合` `领域特定模型` `推理能力` `生物医学` `金融` `大型语言模型` `资源效率`

## 📋 核心要点

1. 现有模型融合方法在合并领域特定LLMs与长链推理模型时，常导致推理能力下降和输出混乱等问题。
2. 本文提出RCP-Merging框架，通过将推理模型权重视为先验，利用推理能力指标实现有效的模型融合。
3. 在生物医学和金融领域的实验中，RCP-Merging显著提升了任务性能，分别提高了9.5%和9.2%。

## 📝 摘要（中文）

大型语言模型（LLMs）具备长链推理（CoT）能力，称为推理模型，展现出卓越的复杂问题解决能力。为在不增加计算和数据成本的情况下创建具备长CoT能力和领域特定知识的双能力模型，模型融合成为一种高效的方法。然而，现有融合方法在合并领域特定LLMs与长CoT模型时面临推理能力下降、输出混乱等挑战。为此，本文提出RCP-Merging框架，旨在将领域特定LLMs与长CoT能力模型有效融合，同时保持原领域的模型性能。通过将推理模型权重视为基础先验，利用推理能力指标保留核心长CoT能力模型权重，并选择性融合必要的领域特定权重。实验结果表明，RCP-Merging在生物医学和金融领域的任务性能提升了9.5%和9.2%，且未显著损害原有的长CoT推理能力。

## 🔬 方法详解

**问题定义**：本文旨在解决长链推理模型与领域特定模型融合时推理能力下降的问题。现有方法在融合过程中常出现输出混乱和性能下降的现象。

**核心思路**：RCP-Merging框架通过将推理模型的权重视为基础先验，利用推理能力指标来保留长链推理模型的核心权重，同时选择性地融合领域特定的权重，从而实现有效的模型融合。

**技术框架**：该框架主要包括两个阶段：首先，评估推理模型的权重和领域特定模型的权重；其次，基于推理能力指标进行权重的选择性融合，确保保留推理能力的同时引入领域知识。

**关键创新**：RCP-Merging的创新在于引入推理能力指标作为融合的先验，确保在合并过程中不损害长链推理能力，这是与现有方法的本质区别。

**关键设计**：在参数设置上，选择了适当的推理能力指标，并设计了特定的损失函数以平衡推理能力与领域知识的融合，确保模型在两个领域的性能均得到提升。

## 📊 实验亮点

实验结果显示，RCP-Merging在生物医学和金融领域的任务性能分别提升了9.5%和9.2%，显著优于现有最先进的方法，同时保持了长链推理能力的完整性。

## 🎯 应用场景

该研究具有广泛的应用潜力，尤其在生物医学和金融等领域，可以有效提升领域特定任务的性能。未来，RCP-Merging框架可扩展至其他领域，推动多领域知识的融合与应用，提升智能系统的综合能力。

## 📄 摘要（原文）

> Large Language Models (LLMs) with long chain-of-thought (CoT) capability, termed Reasoning Models, demonstrate superior intricate problem-solving abilities through multi-step long CoT reasoning. To create a dual-capability model with long CoT capability and domain-specific knowledge without substantial computational and data costs, model merging emerges as a highly resource-efficient method. However, significant challenges lie in merging domain-specific LLMs with long CoT ones since nowadays merging methods suffer from reasoning capability degradation, even gibberish output and output collapse. To overcome this, we introduce RCP-Merging: Merging Long Chain-of-Thought Models with Domain-Specific Models by Considering Reasoning Capability as Prior, a novel merging framework designed to integrate domain-specific LLMs with long CoT capability, meanwhile maintaining model performance in the original domain. Treating reasoning model weights as foundational prior, our method utilizes a reasoning capability indicator to preserve core long CoT capability model weights while selectively merging essential domain-specific weights. We conducted extensive experiments on Qwen2.5-7B, Llama3.1-8B, and Qwen2.5-1.5B models in BioMedicine and Finance domains. Our results show that RCP-Merging successfully merges a reasoning model with domain-specific ones, improving domain task performance by 9.5% and 9.2% over state-of-the-art methods, without significantly harming the original long CoT reasoning capability.

