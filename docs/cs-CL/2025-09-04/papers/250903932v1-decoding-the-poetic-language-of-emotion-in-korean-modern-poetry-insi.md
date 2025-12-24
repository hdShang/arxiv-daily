---
layout: default
title: "Decoding the Poetic Language of Emotion in Korean Modern Poetry: Insights from a Human-Labeled Dataset and AI Modeling"
---

# Decoding the Poetic Language of Emotion in Korean Modern Poetry: Insights from a Human-Labeled Dataset and AI Modeling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03932" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03932v1</a>
  <a href="https://arxiv.org/pdf/2509.03932.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03932v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03932v1', 'Decoding the Poetic Language of Emotion in Korean Modern Poetry: Insights from a Human-Labeled Dataset and AI Modeling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Iro Lim, Haein Ji, Byungjun Kim

**分类**: cs.CL, cs.CY, cs.LG

**发布日期**: 2025-09-04

**备注**: 30 pages, 13 tables, 2 figures, Digital Humanities and Social Sciences Korea Conference, James Joo-Jin Kim Center for Korean Studies, University of Pennsylvania, Philadelphia, USA

---

## 💡 一句话要点

**提出KPoEM数据集以解决现代韩诗情感分析问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `情感分析` `现代诗歌` `数据集构建` `韩语模型` `多标签分类` `文化特性` `计算方法` `文学分析`

## 📋 核心要点

1. 现有的文本情感分类方法在处理比喻性和文化特定的诗歌时存在不足，尤其是现代韩国诗歌。
2. 本研究提出KPoEM数据集，构建了一个多标签情感数据集，并在此基础上微调韩语模型，以提高情感识别能力。
3. 实验结果表明，KPoEM模型在情感识别上取得了显著提升，F1-micro得分从0.34提升至0.60，展示了其有效性。

## 📝 摘要（中文）

本研究介绍了KPoEM（韩国诗歌情感映射），这是一个用于现代韩国诗歌计算情感分析的新数据集。尽管基于文本的情感分类在大型语言模型中取得了显著进展，但由于其比喻性语言和文化特性，诗歌，特别是韩国诗歌，仍然未被充分探索。我们构建了一个包含7,662条条目的多标签情感数据集，其中包括来自483首诗的7,007条行级条目和615条作品级条目，标注了来自五位影响力韩国诗人的44个细分情感类别。经过在该数据集上微调的最先进的韩语模型显著优于之前的模型，F1-micro得分达到0.60，而基于通用语料库训练的模型仅为0.34。KPoEM模型通过顺序微调进行训练，首先在通用语料库上，然后在KPoEM数据集上，不仅增强了识别时间和文化特定情感表达的能力，还强有力地保留了现代韩国诗歌的核心情感。该研究将计算方法与文学分析相结合，为通过结构化数据定量探索诗歌情感提供了新的可能性。

## 🔬 方法详解

**问题定义**：本研究旨在解决现代韩国诗歌情感分析中的挑战，现有方法在处理诗歌的比喻性语言和文化特性时表现不佳，导致情感识别的准确性不足。

**核心思路**：论文的核心思路是构建一个专门针对现代韩国诗歌的多标签情感数据集KPoEM，并基于该数据集微调韩语语言模型，以提高情感分类的准确性和文化适应性。

**技术框架**：整体架构包括数据集构建、模型选择与微调两个主要阶段。首先，收集和标注现代韩国诗歌数据，然后使用预训练的韩语语言模型进行顺序微调，先在通用语料库上训练，再在KPoEM数据集上进行细化。

**关键创新**：最重要的技术创新点在于KPoEM数据集的构建和模型的顺序微调策略，这使得模型能够更好地捕捉到时间和文化特定的情感表达，与传统方法相比，显著提升了情感识别的能力。

**关键设计**：在模型训练中，采用了特定的损失函数以优化多标签分类效果，并在网络结构上进行了调整，以适应情感类别的多样性和复杂性。

## 📊 实验亮点

实验结果显示，KPoEM模型在情感识别任务中取得了显著的性能提升，F1-micro得分从0.34提升至0.60，表明该模型在处理现代韩国诗歌的情感分析方面具有更强的能力，成功捕捉了文化和情感的细微差别。

## 🎯 应用场景

该研究的潜在应用领域包括文学分析、情感计算和文化研究等。通过KPoEM数据集和相应的模型，研究人员可以更深入地探索现代韩国诗歌中的情感表达，为相关领域的研究提供新的工具和视角，促进跨文化的情感理解与交流。

## 📄 摘要（原文）

> This study introduces KPoEM (Korean Poetry Emotion Mapping) , a novel dataset for computational emotion analysis in modern Korean poetry. Despite remarkable progress in text-based emotion classification using large language models, poetry-particularly Korean poetry-remains underexplored due to its figurative language and cultural specificity. We built a multi-label emotion dataset of 7,662 entries, including 7,007 line-level entries from 483 poems and 615 work-level entries, annotated with 44 fine-grained emotion categories from five influential Korean poets. A state-of-the-art Korean language model fine-tuned on this dataset significantly outperformed previous models, achieving 0.60 F1-micro compared to 0.34 from models trained on general corpora. The KPoEM model, trained through sequential fine-tuning-first on general corpora and then on the KPoEM dataset-demonstrates not only an enhanced ability to identify temporally and culturally specific emotional expressions, but also a strong capacity to preserve the core sentiments of modern Korean poetry. This study bridges computational methods and literary analysis, presenting new possibilities for the quantitative exploration of poetic emotions through structured data that faithfully retains the emotional and cultural nuances of Korean literature.

