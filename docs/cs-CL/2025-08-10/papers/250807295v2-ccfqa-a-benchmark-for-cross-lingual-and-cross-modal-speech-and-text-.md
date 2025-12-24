---
layout: default
title: "CCFQA: A Benchmark for Cross-Lingual and Cross-Modal Speech and Text Factuality Evaluation"
---

# CCFQA: A Benchmark for Cross-Lingual and Cross-Modal Speech and Text Factuality Evaluation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.07295" class="toolbar-btn" target="_blank">📄 arXiv: 2508.07295v2</a>
  <a href="https://arxiv.org/pdf/2508.07295.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.07295v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.07295v2', 'CCFQA: A Benchmark for Cross-Lingual and Cross-Modal Speech and Text Factuality Evaluation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yexing Du, Kaiyuan Liu, Youcheng Pan, Zheng Chu, Bo Yang, Xiaocheng Feng, Ming Liu, Yang Xiang

**分类**: cs.CL

**发布日期**: 2025-08-10 (更新: 2025-12-01)

**备注**: Accepted in AAAI 2026

**🔗 代码/项目**: [GITHUB](https://github.com/yxduir/ccfqa)

---

## 💡 一句话要点

**提出CCFQA基准以解决多语言多模态事实性评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `跨语言评估` `事实性评估` `语音理解` `迁移学习` `大型语言模型` `问答系统`

## 📋 核心要点

1. 现有的多模态大型语言模型评估主要集中于英语，缺乏对多语言和语音输入的有效评估。
2. 提出CCFQA基准，包含8种语言的平行语音-文本事实性问题，系统评估MLLMs的跨语言和跨模态能力。
3. 实验表明，当前MLLMs在CCFQA基准上表现不佳，同时提出的少量迁移学习策略显著提升了多语言问答性能。

## 📝 摘要（中文）

随着大型语言模型（LLMs）在多语言环境中的普及，确保无幻觉的事实性变得尤为重要。然而，现有的多模态大型语言模型（MLLMs）评估基准主要集中于文本或视觉模态，并且主要以英语为主，这在处理多语言输入时尤其存在评估空白。为此，我们提出了一种新的跨语言和跨模态事实性基准（CCFQA），该基准包含8种语言的平行语音-文本事实性问题，旨在系统评估MLLMs的跨语言和跨模态事实性能力。实验结果表明，当前的MLLMs在CCFQA基准上仍面临重大挑战。此外，我们提出了一种少量迁移学习策略，有效地将LLMs在英语中的问答能力转移到多语言口语问答任务中，仅使用5次训练便实现了与GPT-4o-mini-Audio的竞争性表现。我们将CCFQA作为基础研究资源发布，以促进MLLMs在语音理解能力上的发展。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有多模态大型语言模型在多语言和语音输入下的事实性评估不足的问题。现有方法主要集中于英语文本和视觉模态，导致在多语言环境中评估效果不佳。

**核心思路**：提出CCFQA基准，通过设计平行的语音-文本事实性问题，系统性地评估MLLMs在跨语言和跨模态的事实性能力，填补现有评估的空白。

**技术框架**：CCFQA基准包含多个模块，包括多语言数据集构建、事实性问题设计和评估指标制定。实验中采用少量迁移学习策略，将英语问答能力迁移至多语言口语问答任务。

**关键创新**：CCFQA基准是首个专注于多语言和多模态的事实性评估工具，显著提升了对MLLMs的评估能力，尤其是在语音输入方面。

**关键设计**：在数据集构建中，采用了8种语言的平行语音-文本对，并设计了相应的评估指标。少量迁移学习策略通过5-shot训练实现了与GPT-4o-mini-Audio的竞争性表现。

## 📊 实验亮点

实验结果显示，当前的多模态大型语言模型在CCFQA基准上面临显著挑战，尤其是在处理多语言和语音输入时。同时，采用的少量迁移学习策略在5-shot训练下实现了与GPT-4o-mini-Audio相当的性能，展示了良好的迁移能力。

## 🎯 应用场景

该研究的潜在应用领域包括多语言语音助手、跨语言信息检索和多模态人机交互等。通过提升多模态大型语言模型的事实性评估能力，能够更好地服务于全球用户，推动多语言技术的发展和应用。

## 📄 摘要（原文）

> As Large Language Models (LLMs) are increasingly popularized in the multilingual world, ensuring hallucination-free factuality becomes markedly crucial. However, existing benchmarks for evaluating the reliability of Multimodal Large Language Models (MLLMs) predominantly focus on textual or visual modalities with a primary emphasis on English, which creates a gap in evaluation when processing multilingual input, especially in speech. To bridge this gap, we propose a novel Cross-lingual and Cross-modal Factuality benchmark (CCFQA). Specifically, the CCFQA benchmark contains parallel speech-text factual questions across 8 languages, designed to systematically evaluate MLLMs' cross-lingual and cross-modal factuality capabilities. Our experimental results demonstrate that current MLLMs still face substantial challenges on the CCFQA benchmark. Furthermore, we propose a few-shot transfer learning strategy that effectively transfers the Question Answering (QA) capabilities of LLMs in English to multilingual Spoken Question Answering (SQA) tasks, achieving competitive performance with GPT-4o-mini-Audio using just 5-shot training. We release CCFQA as a foundational research resource to promote the development of MLLMs with more robust and reliable speech understanding capabilities. Our code and dataset are available at https://github.com/yxduir/ccfqa.

