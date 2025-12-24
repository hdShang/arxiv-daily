---
layout: default
title: "LESS: Large Language Model Enhanced Semi-Supervised Learning for Speech Foundational Models Using in-the-wild Data"
---

# LESS: Large Language Model Enhanced Semi-Supervised Learning for Speech Foundational Models Using in-the-wild Data

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04586" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04586v2</a>
  <a href="https://arxiv.org/pdf/2506.04586.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04586v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04586v2', 'LESS: Large Language Model Enhanced Semi-Supervised Learning for Speech Foundational Models Using in-the-wild Data')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wen Ding, Fan Qian

**分类**: cs.CL, cs.SD, eess.AS

**发布日期**: 2025-06-05 (更新: 2025-09-19)

**备注**: Submitted to ICASSP 2026

---

## 💡 一句话要点

**提出LESS框架以解决真实环境下语音模型的半监督学习挑战**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `半监督学习` `语音识别` `大型语言模型` `伪标签修正` `数据过滤` `自然语言处理` `真实环境数据`

## 📋 核心要点

1. 现有的语音基础模型在真实环境数据上应用半监督学习时，面临声学特性复杂导致的伪标签质量问题。
2. LESS框架通过大型语言模型修正伪标签，并结合数据过滤策略，提升伪标签的准确性和可靠性。
3. 在实验中，LESS在多个数据集上均取得显著提升，字错误率降低3.8%，BLEU分数分别提高0.8和0.7。

## 📝 摘要（中文）

尽管现有的语音基础模型能够生成高质量的文本伪标签，但在真实环境数据上应用半监督学习仍然面临挑战，因为这些数据的声学特性比经过整理的数据集更复杂。为了解决这一问题，本文提出了LESS（大型语言模型增强的半监督学习）框架，该框架利用大型语言模型（LLMs）来修正在真实环境数据上生成的伪标签。在LESS框架中，来自无监督数据的自动语音识别（ASR）或自动语音翻译（AST）生成的伪标签文本通过LLM进行精炼，并通过数据过滤策略进一步改进。在普通话ASR和西班牙语到英语AST的评估中，LESS在WenetSpeech上实现了3.8%的绝对字错误率降低，在Callhome和Fisher测试集上分别实现了BLEU分数的0.8和0.7的提升，显示出LESS在多种语言、任务和领域中的有效性。我们已将该方法的实现开源，以促进该领域的进一步研究。

## 🔬 方法详解

**问题定义**：论文要解决的问题是如何在真实环境数据上有效应用半监督学习，现有方法在处理复杂声学特性时生成的伪标签质量较低，影响模型性能。

**核心思路**：论文提出的核心思路是利用大型语言模型（LLMs）对伪标签进行修正，从而提高伪标签的质量，并通过数据过滤策略进一步优化数据集。

**技术框架**：LESS框架主要包括伪标签生成模块（ASR或AST）、LLM修正模块和数据过滤模块。首先生成伪标签，然后通过LLM进行精炼，最后应用数据过滤策略提升数据质量。

**关键创新**：LESS的关键创新在于将大型语言模型引入伪标签修正过程，显著提高了伪标签的准确性，与传统方法相比，LESS能够更好地应对复杂的真实环境数据。

**关键设计**：在设计上，LESS框架采用了特定的损失函数来优化伪标签的修正过程，并在网络结构上结合了LLM的特性，以确保伪标签的高质量输出。

## 📊 实验亮点

LESS在多个评估中表现出色，WenetSpeech数据集上实现了3.8%的字错误率降低，Callhome和Fisher测试集的BLEU分数分别提高了0.8和0.7，显示出该框架在多语言和多任务场景下的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括语音识别、语音翻译和其他自然语言处理任务，能够显著提升在真实环境下的模型性能。LESS框架的开源实现为相关领域的研究提供了新的工具和思路，推动了语音技术的进步。

## 📄 摘要（原文）

> Although state-of-the-art Speech Foundation Models can produce high-quality text pseudo-labels, applying Semi-Supervised Learning (SSL) for in-the-wild real-world data remains challenging due to its richer and more complex acoustics compared to curated datasets. To address the challenges, we introduce LESS (Large Language Model Enhanced Semi-supervised Learning), a versatile framework that uses Large Language Models (LLMs) to correct pseudo-labels generated on in-the-wild data. In the LESS framework, pseudo-labeled text from Automatic Speech Recognition (ASR) or Automatic Speech Translation (AST) of the unsupervised data is refined by an LLM, and further improved by a data filtering strategy. Across Mandarin ASR and Spanish-to-English AST evaluations, LESS delivers consistent gains, with an absolute Word Error Rate reduction of 3.8% on WenetSpeech, and BLEU score increase of 0.8 and 0.7, achieving 34.0 on Callhome and 64.7 on Fisher testsets respectively. These results highlight LESS's effectiveness across diverse languages, tasks, and domains. We have released the recipe as open source to facilitate further research in this area.

