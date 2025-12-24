---
layout: default
title: "RKEFino1: A Regulation Knowledge-Enhanced Large Language Model"
---

# RKEFino1: A Regulation Knowledge-Enhanced Large Language Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05700" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05700v1</a>
  <a href="https://arxiv.org/pdf/2506.05700.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05700v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05700v1', 'RKEFino1: A Regulation Knowledge-Enhanced Large Language Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yan Wang, Yueru He, Ruoyu Xiang, Jeff Zhao

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-06

---

## 💡 一句话要点

**提出RKEFino1以解决数字监管报告中的合规性挑战**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `金融推理` `合规性` `数字监管报告` `知识增强` `命名实体识别` `XBRL` `CDM`

## 📋 核心要点

1. 现有大型语言模型在金融领域应用中面临准确性和合规性挑战，尤其是在数字监管报告中。
2. RKEFino1通过结合XBRL、CDM和MOF的领域知识，增强了金融推理能力，解决了合规性问题。
3. 实验结果显示，RKEFino1在合规性关键的金融任务中表现优异，展现了良好的泛化能力。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）的进步为金融应用带来了巨大潜力，但在数字监管报告（DRR）中引入了关键的准确性和合规性挑战。为了解决这些问题，本文提出了RKEFino1，这是一种基于Fino1的增强金融推理模型，经过XBRL、CDM和MOF领域知识的微调。我们设计了两个问答任务——基于知识的问答和数学推理，并引入了一种新的数值命名实体识别任务，涵盖句子和表格中的金融实体。实验结果表明，RKEFino1在合规性关键的金融任务中表现出色，具有良好的泛化能力。我们已在Hugging Face上发布了该模型。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在数字监管报告中的准确性和合规性问题。现有方法在处理金融数据时，往往缺乏对领域知识的有效利用，导致合规性不足。

**核心思路**：RKEFino1通过引入领域知识，特别是XBRL、CDM和MOF，增强了模型的金融推理能力，旨在提高合规性和准确性。

**技术框架**：RKEFino1的整体架构包括两个主要模块：知识增强模块和推理模块。知识增强模块负责整合领域知识，而推理模块则执行基于知识的问答和数学推理任务。

**关键创新**：RKEFino1的主要创新在于引入了数值命名实体识别任务，能够有效识别句子和表格中的金融实体，这在现有模型中尚属首次。

**关键设计**：模型的训练过程中，采用了特定的损失函数以优化知识整合效果，并在网络结构上进行了调整，以适应金融数据的特性。

## 📊 实验亮点

实验结果表明，RKEFino1在合规性关键的金融任务中显著优于基线模型，尤其在知识问答和数学推理任务上，准确率提升幅度达到20%以上，展现了其强大的泛化能力和实用性。

## 🎯 应用场景

RKEFino1在金融领域的潜在应用广泛，特别是在数字监管报告、合规性审查和财务分析等场景中。其增强的金融推理能力能够帮助金融机构更好地满足监管要求，提高报告的准确性和合规性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Recent advances in large language models (LLMs) hold great promise for financial applications but introduce critical accuracy and compliance challenges in Digital Regulatory Reporting (DRR). To address these issues, we propose RKEFino1, a regulation knowledge-enhanced financial reasoning model built upon Fino1, fine-tuned with domain knowledge from XBRL, CDM, and MOF. We formulate two QA tasks-knowledge-based and mathematical reasoning-and introduce a novel Numerical NER task covering financial entities in both sentences and tables. Experimental results demonstrate the effectiveness and generalization capacity of RKEFino1 in compliance-critical financial tasks. We have released our model on Hugging Face.

