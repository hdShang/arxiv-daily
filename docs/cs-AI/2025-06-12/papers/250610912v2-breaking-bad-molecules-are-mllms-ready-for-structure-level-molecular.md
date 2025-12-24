---
layout: default
title: "Breaking Bad Molecules: Are MLLMs Ready for Structure-Level Molecular Detoxification?"
---

# Breaking Bad Molecules: Are MLLMs Ready for Structure-Level Molecular Detoxification?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10912" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10912v2</a>
  <a href="https://arxiv.org/pdf/2506.10912.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10912v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10912v2', 'Breaking Bad Molecules: Are MLLMs Ready for Structure-Level Molecular Detoxification?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fei Lin, Ziyang Gong, Cong Wang, Yonglin Tian, Tengchao Zhang, Xue Yang, Gen Luo, Fei-Yue Wang

**分类**: cs.AI, cs.CL

**发布日期**: 2025-06-12 (更新: 2025-06-18)

---

## 💡 一句话要点

**提出ToxiMol基准以解决分子毒性修复问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `分子毒性修复` `多模态大语言模型` `毒性评估` `数据集构建` `药物开发`

## 📋 核心要点

1. 现有的分子毒性修复方法缺乏系统性定义和基准，导致药物开发中的毒性问题难以有效解决。
2. 本文提出了ToxiMol基准任务，构建了涵盖多种毒性机制的标准化数据集，并设计了机制感知的提示注释流程。
3. 实验评估显示，尽管当前MLLMs在毒性修复任务上仍面临挑战，但在毒性理解和结构感知编辑方面展现出潜力。

## 📝 摘要（中文）

毒性是早期药物开发失败的主要原因之一。尽管分子设计和属性预测已有所进展，但分子毒性修复这一任务尚未得到系统定义或基准化。为填补这一空白，本文提出了ToxiMol，这是首个针对多模态大语言模型（MLLMs）在分子毒性修复方面的基准任务。我们构建了一个标准化的数据集，涵盖11个主要任务和560个具有代表性的毒性分子，并设计了一个机制感知和任务自适应的提示注释流程。同时，提出了自动化评估框架ToxiEval，整合了毒性终点预测、合成可及性、药物相似性和结构相似性，形成高通量评估链。实验结果表明，尽管当前的MLLMs在此任务上仍面临重大挑战，但它们在毒性理解、语义约束遵循和结构感知分子编辑方面开始展现出有希望的能力。

## 🔬 方法详解

**问题定义**：本文旨在解决分子毒性修复的具体问题，现有方法在系统性定义和基准化方面存在不足，导致毒性修复效果不佳。

**核心思路**：论文的核心思路是通过构建ToxiMol基准任务，利用多模态大语言模型（MLLMs）进行分子毒性修复，设计机制感知的提示注释流程以提高修复效果。

**技术框架**：整体架构包括数据集构建、提示注释流程和自动化评估框架ToxiEval，主要模块涵盖毒性终点预测、合成可及性、药物相似性和结构相似性。

**关键创新**：最重要的技术创新点在于首次提出了针对分子毒性修复的标准化基准任务，并设计了机制感知的提示注释流程，显著提升了修复的有效性。

**关键设计**：关键设计包括标准化数据集的构建，涵盖多种毒性机制，提示注释流程的机制感知能力，以及自动化评估框架的高通量评估链。具体参数设置和损失函数的选择在实验中进行了详细分析。

## 📊 实验亮点

实验结果显示，尽管当前的MLLMs在分子毒性修复任务上仍面临显著挑战，但在毒性理解、语义约束遵循和结构感知分子编辑方面展现出一定的潜力，具体性能提升幅度尚未明确。

## 🎯 应用场景

该研究的潜在应用领域包括药物开发、化学合成和环境科学等。通过有效的分子毒性修复，能够加速新药的研发进程，降低药物开发中的风险，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Toxicity remains a leading cause of early-stage drug development failure. Despite advances in molecular design and property prediction, the task of molecular toxicity repair - generating structurally valid molecular alternatives with reduced toxicity - has not yet been systematically defined or benchmarked. To fill this gap, we introduce ToxiMol, the first benchmark task for general-purpose Multimodal Large Language Models (MLLMs) focused on molecular toxicity repair. We construct a standardized dataset covering 11 primary tasks and 560 representative toxic molecules spanning diverse mechanisms and granularities. We design a prompt annotation pipeline with mechanism-aware and task-adaptive capabilities, informed by expert toxicological knowledge. In parallel, we propose an automated evaluation framework, ToxiEval, which integrates toxicity endpoint prediction, synthetic accessibility, drug-likeness, and structural similarity into a high-throughput evaluation chain for repair success. We systematically assess nearly 30 mainstream general-purpose MLLMs and design multiple ablation studies to analyze key factors such as evaluation criteria, candidate diversity, and failure attribution. Experimental results show that although current MLLMs still face significant challenges on this task, they begin to demonstrate promising capabilities in toxicity understanding, semantic constraint adherence, and structure-aware molecule editing.

