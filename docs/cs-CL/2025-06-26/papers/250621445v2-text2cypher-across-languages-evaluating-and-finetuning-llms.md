---
layout: default
title: "Text2Cypher Across Languages: Evaluating and Finetuning LLMs"
---

# Text2Cypher Across Languages: Evaluating and Finetuning LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21445" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21445v2</a>
  <a href="https://arxiv.org/pdf/2506.21445.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21445v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21445v2', 'Text2Cypher Across Languages: Evaluating and Finetuning LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Makbule Gulcin Ozsoy, William Tai

**分类**: cs.CL, cs.IR

**发布日期**: 2025-06-26 (更新: 2025-09-04)

---

## 💡 一句话要点

**提出多语言Text2Cypher评估与微调方法以提升数据库查询生成**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `多语言处理` `数据库查询` `自然语言接口` `跨语言评估` `微调技术` `Cypher查询生成`

## 📋 核心要点

1. 现有的Text2Cypher方法主要集中在英语，其他语言的评估和性能分析相对不足，导致多语言查询生成系统的构建面临挑战。
2. 本文通过创建多语言数据集并评估基础和微调的LLMs，提出了一种新的跨语言比较方法，以解决现有研究的局限性。
3. 实验结果表明，微调基础模型在多语言数据集上能显著缩小语言间的性能差距，提升了查询生成的均衡性和准确性。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）的进步使得自然语言接口能够将用户问题转化为数据库查询，如Text2SQL、Text2SPARQL和Text2Cypher。尽管这些接口提高了数据库的可访问性，但大多数研究集中在英语上，其他语言的评估相对有限。本文研究了基础和微调的LLMs在多语言Text2Cypher任务上的表现，创建并发布了一个多语言数据集，通过将英语问题翻译成西班牙语和土耳其语，同时保留原始的Cypher查询，从而实现公平的跨语言比较。我们发现，英语的表现最佳，其次是西班牙语，土耳其语表现最低，这与训练数据的可用性和语言特征的差异有关。微调结果显示，英语微调提高了整体准确性，但扩大了语言间的表现差距，而多语言微调则缩小了这一差距，提升了性能的均衡性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有Text2Cypher方法在多语言环境下的评估不足，尤其是非英语语言的表现较差，影响了数据库查询生成的普适性和可用性。

**核心思路**：通过创建一个多语言数据集，将英语问题翻译为西班牙语和土耳其语，并保留原始的Cypher查询，从而实现公平的跨语言性能比较。

**技术框架**：研究包括数据集的构建、模型的评估和微调两个主要阶段。首先，构建多语言数据集；其次，使用标准化的提示和评估指标对基础模型进行评估和微调。

**关键创新**：本文的创新在于引入了多语言数据集的构建和评估方法，强调了微调对不同语言间性能差距的影响，尤其是多语言微调的优势。

**关键设计**：在微调过程中，设置了不同的训练数据集，包括仅英语和多语言数据集，采用标准化的评估指标来衡量模型性能，确保了实验的可重复性和结果的可靠性。

## 📊 实验亮点

实验结果显示，基础模型在英语上的表现最佳，西班牙语次之，而土耳其语表现最低。微调基础模型在英语数据集上提升了准确性，但扩大了语言间差距；而多语言微调则显著缩小了这一差距，提升了性能均衡性。

## 🎯 应用场景

该研究的潜在应用领域包括多语言数据库查询生成、跨语言信息检索和自然语言处理系统的开发。通过提升不同语言间的查询生成能力，能够使得更多用户无障碍地访问和利用数据库，具有重要的实际价值和社会影响。

## 📄 摘要（原文）

> Recent advances in large language models (LLMs) have enabled natural language interfaces that translate user questions into database queries, such as Text2SQL, Text2SPARQL, and Text2Cypher. While these interfaces enhance database accessibility, most research today focuses on English, with limited evaluation in other languages. This paper investigates the performance of both foundational and finetuned LLMs on the Text2Cypher task across multiple languages. We create and release a multilingual dataset by translating English questions into Spanish and Turkish while preserving the original Cypher queries, enabling fair cross-lingual comparison. Using standardized prompts and metrics, we evaluate several foundational models and observe a consistent performance pattern: highest on English, followed by Spanish, and lowest on Turkish. We attribute this to differences in training data availability and linguistic features. We also examine the impact of translating task prompts into Spanish and Turkish. Results show little to no change in evaluation metrics, suggesting prompt translation has minor impact. Furthermore, we finetune a foundational model on two datasets: one in English only, and one multilingual. Finetuning on English improves overall accuracy but widens the performance gap between languages. In contrast, multilingual finetuning narrows the gap, resulting in more balanced performance. Our findings highlight the importance for multilingual evaluation and training to build more inclusive and robust query generation systems.

