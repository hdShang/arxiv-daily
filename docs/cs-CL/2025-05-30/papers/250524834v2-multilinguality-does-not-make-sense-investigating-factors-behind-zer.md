---
layout: default
title: Multilinguality Does not Make Sense: Investigating Factors Behind Zero-Shot Transfer in Sense-Aware Tasks
---

# Multilinguality Does not Make Sense: Investigating Factors Behind Zero-Shot Transfer in Sense-Aware Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24834" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24834v2</a>
  <a href="https://arxiv.org/pdf/2505.24834.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24834v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24834v2', 'Multilinguality Does not Make Sense: Investigating Factors Behind Zero-Shot Transfer in Sense-Aware Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Roksana Goworek, Haim Dubossarsky

**分类**: cs.CL

**发布日期**: 2025-05-30 (更新: 2025-10-16)

**备注**: accepted to EMNLP 2025 Main

---

## 💡 一句话要点

**探讨多语言性对零-shot迁移的影响，提出新见解**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `跨语言迁移` `零-shot学习` `多义性` `词汇语义变化` `低资源语言` `自然语言处理` `模型评估`

## 📋 核心要点

1. 现有研究普遍假设多语言训练能提升零-shot迁移效果，但缺乏实证支持。
2. 论文通过分析多义性和词汇语义变化任务，提出多语言性并非迁移的必要条件，强调其他因素的重要性。
3. 研究结果显示，预训练和微调数据的差异等因素更能解释迁移效果，提供了新的研究基线和模型。

## 📝 摘要（中文）

跨语言迁移是现代自然语言处理的核心，使模型能够在与训练语言不同的语言中执行任务。常见假设认为，训练更多语言会改善零-shot迁移。本文在多义性和词汇语义变化等感知任务上进行测试，发现多语言性并非有效迁移的必要条件。通过对28种语言的大规模分析，结果表明，预训练和微调数据的差异以及评估工件等其他因素更能解释多语言性的感知优势。此外，研究团队还发布了微调模型，并提供了实证基线以支持未来研究。尽管重点关注两项感知任务，但研究结果为跨语言迁移提供了更广泛的见解，尤其是针对低资源语言。

## 🔬 方法详解

**问题定义**：本文旨在探讨在感知任务中，多语言性对零-shot迁移的影响。现有方法普遍认为多语言训练能够提升迁移效果，但缺乏实证数据支持这一观点。

**核心思路**：研究通过对28种语言进行大规模分析，验证多语言性并非有效迁移的必要条件，强调预训练和微调数据的差异等其他因素在迁移中的重要性。

**技术框架**：研究采用了大规模的跨语言数据集，分析了多义性和词汇语义变化任务的迁移效果，比较了不同语言间的迁移性能。主要模块包括数据预处理、模型训练和评估。

**关键创新**：论文的创新点在于提出了多语言性并非迁移效果的决定性因素，挑战了现有的假设，强调了数据质量和模型训练过程中的其他变量。

**关键设计**：在实验中，研究团队设置了多种预训练和微调策略，采用了不同的损失函数和评估指标，以确保结果的可靠性和可重复性。

## 📊 实验亮点

实验结果表明，在多义性和词汇语义变化任务中，模型在不同语言间的迁移效果并不依赖于多语言训练。具体而言，预训练和微调数据的差异能够更好地解释迁移性能的变化，提供了新的实证基线，推动了相关研究的进展。

## 🎯 应用场景

该研究的潜在应用领域包括低资源语言的自然语言处理任务，尤其是在多语言环境下的机器翻译、情感分析和信息检索等。研究结果为未来的跨语言模型设计提供了新的思路，可能会影响多语言模型的开发和应用策略。

## 📄 摘要（原文）

> Cross-lingual transfer is central to modern NLP, enabling models to perform tasks in languages different from those they were trained on. A common assumption is that training on more languages improves zero-shot transfer. We test this on sense-aware tasks-polysemy and lexical semantic change-and find that multilinguality is not necessary for effective transfer. Our large-scale analysis across 28 languages reveals that other factors, such as differences in pretraining and fine-tuning data and evaluation artifacts, better explain the perceived benefits of multilinguality. We also release fine-tuned models and provide empirical baselines to support future research. While focused on two sense-aware tasks, our findings offer broader insights into cross-lingual transfer, especially for low-resource languages.

