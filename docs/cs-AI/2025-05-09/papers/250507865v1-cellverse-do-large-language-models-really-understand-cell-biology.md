---
layout: default
title: "CellVerse: Do Large Language Models Really Understand Cell Biology?"
---

# CellVerse: Do Large Language Models Really Understand Cell Biology?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07865" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07865v1</a>
  <a href="https://arxiv.org/pdf/2505.07865.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07865v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07865v1', 'CellVerse: Do Large Language Models Really Understand Cell Biology?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fan Zhang, Tianyu Liu, Zhihong Zhu, Hao Wu, Haixin Wang, Donghao Zhou, Yefeng Zheng, Kun Wang, Xian Wu, Pheng-Ann Heng

**分类**: q-bio.QM, cs.AI, cs.CL, q-bio.CB

**发布日期**: 2025-05-09

---

## 💡 一句话要点

**提出CellVerse以评估大语言模型在细胞生物学中的应用**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `细胞生物学` `大语言模型` `单细胞分析` `多组学数据` `问答基准` `药物反应预测` `模型评估`

## 📋 核心要点

1. 现有方法在细胞生物学的语言驱动分析任务中缺乏全面评估，尤其是LLMs的表现尚不理想。
2. 论文提出CellVerse基准，整合多种单细胞多组学数据，涵盖细胞类型注释、药物反应预测等任务。
3. 实验表明，现有LLMs在药物反应预测任务中未能显著超越随机猜测，显示出改进空间。

## 📝 摘要（中文）

近期研究表明，将单细胞数据建模为自然语言的可行性，以及利用强大的大语言模型（LLMs）理解细胞生物学的潜力。然而，LLMs在语言驱动的单细胞分析任务中的表现尚未得到全面评估。为此，我们提出了CellVerse，一个统一的语言中心问答基准，整合了四种单细胞多组学数据，并涵盖了细胞类型注释、药物反应预测和扰动分析三个层级的单细胞分析任务。实验结果显示，现有的专业模型在CellVerse的所有子任务中均未能做出合理决策，而一些通用模型表现出初步的理解能力。当前LLMs的表现未达到预期，尤其在药物反应预测任务中，评估的LLMs未显示出显著的性能提升。CellVerse为LLMs在细胞生物学中的应用提供了首次大规模的实证展示。

## 🔬 方法详解

**问题定义**：本论文旨在解决大语言模型在细胞生物学分析中的应用效果评估问题。现有方法未能充分验证LLMs在单细胞数据分析中的能力，尤其是在多种任务中的表现。

**核心思路**：CellVerse通过构建一个统一的问答基准，整合不同类型的单细胞多组学数据，提供了一个系统化的评估平台，以便更好地理解LLMs在细胞生物学中的应用潜力。

**技术框架**：CellVerse的整体架构包括数据整合、任务定义和模型评估三个主要模块。数据整合部分涵盖了四种单细胞多组学数据，任务定义则包括细胞类型注释、药物反应预测和基因扰动分析，最后通过对14种LLMs的评估来验证模型的性能。

**关键创新**：CellVerse的最大创新在于其系统化的评估框架，首次将多种单细胞数据与LLMs结合，揭示了当前模型在细胞生物学分析中的局限性。

**关键设计**：在实验中，选择了从160M到671B参数规模的14种LLMs，采用标准化的评估指标，确保结果的可比性和可靠性。

## 📊 实验亮点

实验结果显示，现有的专业模型（如C2S-Pythia）在CellVerse的所有子任务中均未能做出合理决策，而通用模型（如Qwen、Llama、GPT等）则表现出初步的理解能力。然而，在药物反应预测任务中，所有评估的LLMs均未显著超越随机猜测，表明当前模型的性能仍有较大提升空间。

## 🎯 应用场景

CellVerse的研究成果具有广泛的应用潜力，尤其在生物医学研究和药物开发领域。通过提升LLMs在细胞生物学中的应用能力，未来可能促进个性化医疗和精准治疗的发展，推动生物学研究的进步。

## 📄 摘要（原文）

> Recent studies have demonstrated the feasibility of modeling single-cell data as natural languages and the potential of leveraging powerful large language models (LLMs) for understanding cell biology. However, a comprehensive evaluation of LLMs' performance on language-driven single-cell analysis tasks still remains unexplored. Motivated by this challenge, we introduce CellVerse, a unified language-centric question-answering benchmark that integrates four types of single-cell multi-omics data and encompasses three hierarchical levels of single-cell analysis tasks: cell type annotation (cell-level), drug response prediction (drug-level), and perturbation analysis (gene-level). Going beyond this, we systematically evaluate the performance across 14 open-source and closed-source LLMs ranging from 160M to 671B on CellVerse. Remarkably, the experimental results reveal: (1) Existing specialist models (C2S-Pythia) fail to make reasonable decisions across all sub-tasks within CellVerse, while generalist models such as Qwen, Llama, GPT, and DeepSeek family models exhibit preliminary understanding capabilities within the realm of cell biology. (2) The performance of current LLMs falls short of expectations and has substantial room for improvement. Notably, in the widely studied drug response prediction task, none of the evaluated LLMs demonstrate significant performance improvement over random guessing. CellVerse offers the first large-scale empirical demonstration that significant challenges still remain in applying LLMs to cell biology. By introducing CellVerse, we lay the foundation for advancing cell biology through natural languages and hope this paradigm could facilitate next-generation single-cell analysis.

