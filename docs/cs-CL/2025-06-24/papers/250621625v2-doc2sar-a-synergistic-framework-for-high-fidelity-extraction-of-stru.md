---
layout: default
title: "Doc2SAR: A Synergistic Framework for High-Fidelity Extraction of Structure-Activity Relationships from Scientific Documents"
---

# Doc2SAR: A Synergistic Framework for High-Fidelity Extraction of Structure-Activity Relationships from Scientific Documents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21625" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21625v2</a>
  <a href="https://arxiv.org/pdf/2506.21625.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21625v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21625v2', 'Doc2SAR: A Synergistic Framework for High-Fidelity Extraction of Structure-Activity Relationships from Scientific Documents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiaxi Zhuang, Kangning Li, Jue Hou, Mingjun Xu, Zhifeng Gao, Hengxing Cai

**分类**: cs.CL, cs.AI, cs.IR

**发布日期**: 2025-06-24 (更新: 2025-10-11)

---

## 💡 一句话要点

**提出Doc2SAR以解决科学文献中结构-活性关系提取问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `结构-活性关系` `文献提取` `多模态大语言模型` `监督微调` `药物发现` `材料科学` `光学化学结构识别`

## 📋 核心要点

1. 现有方法在提取结构-活性关系时面临文档格式多样性和准确性不足的挑战。
2. 论文提出Doc2SAR框架，结合领域特定工具与经过微调的多模态大语言模型，以提高提取准确性。
3. 实验结果显示，Doc2SAR在DocSAR-200基准上实现了80.78%的整体表格召回率，超越了GPT-4o模型51.48%。

## 📝 摘要（中文）

从科学文献和专利中提取分子结构-活性关系（SAR）对药物发现和材料研究至关重要。然而，由于文档格式的异质性和现有方法的局限性，这一任务仍然具有挑战性。基于规则的方法依赖于严格的模板，无法在多样的文档布局中进行泛化，而通用的多模态大语言模型（MLLMs）在布局检测和光学化学结构识别（OCSR）等专业任务上缺乏足够的准确性和可靠性。为了解决这些挑战，我们引入了DocSAR-200，这是一个专门为评估SAR提取方法而设计的200份科学文献的严格注释基准。此外，我们提出了Doc2SAR，这是一种新颖的协同框架，将领域特定工具与经过监督微调（SFT）的MLLMs相结合。广泛的实验表明，Doc2SAR在各种文档类型上实现了最先进的性能，显著超越了领先的端到端基线。

## 🔬 方法详解

**问题定义**：本论文旨在解决从科学文献中提取结构-活性关系（SAR）时面临的文档格式异质性和现有方法准确性不足的问题。现有的基于规则的方法无法适应多样的文档布局，而通用的多模态大语言模型在特定任务上表现不佳。

**核心思路**：论文提出Doc2SAR框架，结合领域特定的工具与经过监督微调的多模态大语言模型（MLLMs），以提高对结构-活性关系的提取准确性和可靠性。通过这种协同设计，Doc2SAR能够更好地处理不同格式的文档。

**技术框架**：Doc2SAR的整体架构包括数据预处理、布局检测、光学化学结构识别（OCSR）和结果提取四个主要模块。首先，对输入文档进行预处理，然后使用布局检测模块识别文档结构，接着通过OCSR模块提取化学结构，最后整合结果以获得SAR信息。

**关键创新**：Doc2SAR的核心创新在于其协同框架，结合了领域特定工具与MLLMs的优势，显著提高了提取的准确性和效率。这一设计与传统的基于规则的方法和单一使用MLLMs的方法本质上不同。

**关键设计**：在关键设计方面，Doc2SAR采用了针对特定任务的损失函数，并优化了网络结构以适应不同文档格式的需求。同时，通过监督微调技术，增强了模型在特定任务上的表现。实验中使用的参数设置经过精心调整，以确保最佳性能。

## 📊 实验亮点

Doc2SAR在DocSAR-200基准上实现了80.78%的整体表格召回率，超越了现有的端到端基线模型GPT-4o，提升幅度达到51.48%。这一结果表明Doc2SAR在不同文档类型上的优越性能，展示了其在实际应用中的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括药物发现、材料科学以及生物信息学等领域，能够帮助研究人员更高效地从大量文献中提取关键信息，推动科学研究的进展。未来，Doc2SAR可能在自动化文献分析和知识图谱构建中发挥重要作用，提升科研效率。

## 📄 摘要（原文）

> Extracting molecular structure-activity relationships (SARs) from scientific literature and patents is essential for drug discovery and materials research. However, this task remains challenging due to heterogeneous document formats and limitations of existing methods. Specifically, rule-based approaches relying on rigid templates fail to generalize across diverse document layouts, while general-purpose multimodal large language models (MLLMs) lack sufficient accuracy and reliability for specialized tasks, such as layout detection and optical chemical structure recognition (OCSR). To address these challenges, we introduce DocSAR-200, a rigorously annotated benchmark of 200 scientific documents designed specifically for evaluating SAR extraction methods. Additionally, we propose Doc2SAR, a novel synergistic framework that integrates domain-specific tools with MLLMs enhanced via supervised fine-tuning (SFT). Extensive experiments demonstrate that Doc2SAR achieves state-of-the-art performance across various document types, significantly outperforming leading end-to-end baselines. Specifically, Doc2SAR attains an overall Table Recall of 80.78% on DocSAR-200, exceeding end2end GPT-4o by 51.48%. Furthermore, Doc2SAR demonstrates practical usability through efficient inference and is accompanied by a web app.

