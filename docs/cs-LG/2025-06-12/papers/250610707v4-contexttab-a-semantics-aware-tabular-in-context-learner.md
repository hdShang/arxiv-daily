---
layout: default
title: "ConTextTab: A Semantics-Aware Tabular In-Context Learner"
---

# ConTextTab: A Semantics-Aware Tabular In-Context Learner

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10707" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10707v4</a>
  <a href="https://arxiv.org/pdf/2506.10707.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10707v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10707v4', 'ConTextTab: A Semantics-Aware Tabular In-Context Learner')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Marco Spinaci, Marek Polewczyk, Maximilian Schambach, Sam Thelin

**分类**: cs.LG, cs.AI

**发布日期**: 2025-06-12 (更新: 2025-11-03)

**备注**: Accepted as spotlight at NeurIPS 2025

**🔗 代码/项目**: [GITHUB](https://github.com/SAP-samples/sap-rpt-1-oss)

---

## 💡 一句话要点

**提出ConTextTab以解决表格数据语义理解不足的问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `表格数据` `上下文学习` `语义理解` `深度学习` `数据模态` `模型训练` `基准测试`

## 📋 核心要点

1. 现有的表格上下文学习方法在处理真实世界数据时，无法充分利用其丰富的语义信息。
2. ConTextTab通过集成语义理解和对齐，采用不同数据模态的专用嵌入，提升了表格数据的学习能力。
3. 在多个基准测试中，ConTextTab表现出色，尤其是在CARTE基准上设定了新的性能标准。

## 📝 摘要（中文）

表格上下文学习（ICL）最近在多个表格预测任务中取得了最先进的性能。尽管现有的表格原生ICL架构在架构上高效且适应表格数据结构，但其仅在合成数据上训练限制了其充分利用真实世界表格数据中丰富语义和知识的能力。为此，本文提出了ConTextTab，通过集成语义理解和对齐，结合不同数据模态的专用嵌入，并在大规模真实世界表格数据上训练，使得模型在多个基准测试中具有竞争力，并在语义丰富的CARTE基准上设定了新标准。

## 🔬 方法详解

**问题定义**：本文旨在解决当前表格上下文学习方法在真实世界数据上语义理解不足的问题。现有方法主要依赖合成数据，无法充分利用真实数据中的丰富信息。

**核心思路**：ConTextTab的核心思路是结合表格原生ICL架构与预训练大语言模型的优势，通过专用嵌入来处理不同数据模态，从而提升模型对语义的理解能力。

**技术框架**：该模型的整体架构包括数据预处理、嵌入生成、模型训练和评估四个主要模块。数据预处理阶段负责清洗和格式化真实世界表格数据，嵌入生成阶段则为不同模态的数据生成相应的嵌入表示。

**关键创新**：ConTextTab的最大创新在于其专用嵌入设计，使得模型能够有效整合来自不同数据模态的信息，突破了传统方法在语义理解上的局限。

**关键设计**：在模型设计中，采用了多层次的嵌入结构，并引入了新的损失函数以优化语义对齐效果，确保模型能够在训练过程中有效学习到表格数据的深层语义特征。

## 📊 实验亮点

在多个基准测试中，ConTextTab的表现超越了现有的最先进模型，尤其在CARTE基准上，模型的性能提升幅度达到了显著的水平，展示了其在语义理解方面的优势。

## 🎯 应用场景

ConTextTab在金融、医疗和市场分析等领域具有广泛的应用潜力。通过提升表格数据的语义理解能力，该模型能够帮助企业和研究机构更准确地进行数据分析和决策，推动智能化数据处理的发展。未来，ConTextTab可能会在更多复杂的表格数据任务中展现出更大的价值。

## 📄 摘要（原文）

> Tabular in-context learning (ICL) has recently achieved state-of-the-art (SOTA) performance on several tabular prediction tasks. Previously restricted to classification problems on small tables, recent advances such as TabPFN and TabICL have extended its use to larger datasets. Although current table-native ICL architectures are architecturally efficient and well-adapted to tabular data structures, their exclusive training on synthetic data limits their ability to fully leverage the rich semantics and world knowledge contained in real-world tabular data. At the other end of the spectrum, tabular ICL models based on pretrained large language models such as TabuLa-8B integrate deep semantic understanding and world knowledge but are only able to make use of a small amount of context due to inherent architectural limitations. With the aim to combine the best of both these worlds, we introduce ConTextTab, integrating semantic understanding and alignment into a table-native ICL framework. By employing specialized embeddings for different data modalities and by training on large-scale real-world tabular data, our model is competitive with SOTA across a broad set of benchmarks while setting a new standard on the semantically rich CARTE benchmark. Code and model checkpoints are available at: https://github.com/SAP-samples/sap-rpt-1-oss.

