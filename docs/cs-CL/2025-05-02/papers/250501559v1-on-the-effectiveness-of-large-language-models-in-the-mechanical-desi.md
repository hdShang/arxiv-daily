---
layout: default
title: On the effectiveness of Large Language Models in the mechanical design domain
---

# On the effectiveness of Large Language Models in the mechanical design domain

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.01559" class="toolbar-btn" target="_blank">📄 arXiv: 2505.01559v1</a>
  <a href="https://arxiv.org/pdf/2505.01559.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.01559v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.01559v1', 'On the effectiveness of Large Language Models in the mechanical design domain')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Daniele Grandi, Fabian Riquelme

**分类**: cs.CL, cs.LG

**发布日期**: 2025-05-02

---

## 💡 一句话要点

**评估大型语言模型在机械设计领域的有效性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `机械设计` `无监督学习` `模型优化` `语义理解`

## 📋 核心要点

1. 核心问题：现有方法在机械设计领域的语言理解能力不足，导致模型性能不佳。
2. 方法要点：论文提出通过无监督学习任务评估大型语言模型在机械工程领域的表现，重点关注模型架构的优化。
3. 实验或效果：通过调整学习率、丢弃率等参数，模型在二元句子对分类任务中取得了0.62的准确率，零样本分类任务的准确率为0.386。

## 📝 摘要（中文）

本研究旨在理解大型语言模型在机械工程领域的表现。我们利用ABC数据集中设计师为整体装配和各个部件分配的语义数据，经过预处理后，开发了两种无监督任务来评估不同模型架构在特定领域数据上的表现：二元句子对分类任务和零样本分类任务。通过针对过拟合的调整，我们的模型在二元句子对分类任务中取得了0.62的准确率，而在零样本分类任务中则显著超越基线，达到了0.386的顶级分类准确率。结果揭示了在该领域学习语言时出现的特定失败模式。

## 🔬 方法详解

**问题定义**：本研究旨在解决大型语言模型在机械设计领域的应用效果不足的问题。现有方法在处理领域特定语言时，往往无法有效捕捉语义信息，导致模型性能不理想。

**核心思路**：论文的核心思路是利用无监督学习任务来评估和优化大型语言模型在机械工程领域的表现。通过设计二元句子对分类和零样本分类任务，研究者能够更好地理解模型在特定领域数据上的学习能力。

**技术框架**：整体架构包括数据预处理、模型训练和评估三个主要阶段。首先，对ABC数据集进行清洗和格式化，然后使用不同的模型架构进行训练，最后通过设定的无监督任务评估模型性能。

**关键创新**：最重要的技术创新点在于通过无监督学习任务评估模型在特定领域的表现，并针对过拟合进行优化，显著提升了模型的准确性。与现有方法相比，本研究提供了更具针对性的评估方式。

**关键设计**：在模型训练中，研究者调整了学习率、丢弃率、序列长度，并增加了多头注意力层，以应对过拟合问题。这些设计使得模型在二元句子对分类任务中达到了0.62的准确率。

## 📊 实验亮点

在实验中，模型在二元句子对分类任务中取得了0.62的准确率，而在零样本分类任务中达到了0.386的顶级分类准确率，显著超越了基线。这些结果表明，经过优化的模型在特定领域的语言理解能力有了显著提升。

## 🎯 应用场景

该研究的潜在应用领域包括机械设计自动化、智能制造和工程教育等。通过提升大型语言模型在机械设计领域的表现，可以为设计师提供更智能的辅助工具，提升设计效率和准确性，推动行业的数字化转型。

## 📄 摘要（原文）

> In this work, we seek to understand the performance of large language models in the mechanical engineering domain. We leverage the semantic data found in the ABC dataset, specifically the assembly names that designers assigned to the overall assemblies, and the individual semantic part names that were assigned to each part. After pre-processing the data we developed two unsupervised tasks to evaluate how different model architectures perform on domain-specific data: a binary sentence-pair classification task and a zero-shot classification task. We achieved a 0.62 accuracy for the binary sentence-pair classification task with a fine-tuned model that focuses on fighting over-fitting: 1) modifying learning rates, 2) dropout values, 3) Sequence Length, and 4) adding a multi-head attention layer. Our model on the zero-shot classification task outperforms the baselines by a wide margin, and achieves a top-1 classification accuracy of 0.386. The results shed some light on the specific failure modes that arise when learning from language in this domain.

