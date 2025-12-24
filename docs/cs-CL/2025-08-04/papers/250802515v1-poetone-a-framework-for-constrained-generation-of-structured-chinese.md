---
layout: default
title: "PoeTone: A Framework for Constrained Generation of Structured Chinese Songci with LLMs"
---

# PoeTone: A Framework for Constrained Generation of Structured Chinese Songci with LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.02515" class="toolbar-btn" target="_blank">📄 arXiv: 2508.02515v1</a>
  <a href="https://arxiv.org/pdf/2508.02515.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.02515v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.02515v1', 'PoeTone: A Framework for Constrained Generation of Structured Chinese Songci with LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhan Qu, Shuzhou Yuan, Michael Färber

**分类**: cs.CL, cs.LG

**发布日期**: 2025-08-04

---

## 💡 一句话要点

**提出PoeTone框架以实现结构化中文宋词的约束生成**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `宋词生成` `自动评估` `监督微调` `生成-评估架构` `文化传承` `中文诗歌`

## 📋 核心要点

1. 现有方法在生成结构化中文宋词时，难以满足严格的音韵和结构约束，导致生成质量不高。
2. 论文提出了一种新的生成-评估架构，利用自动评估框架作为反馈机制来优化LLMs的生成能力。
3. 通过对18个LLMs的评估，发现微调后的模型在形式符合度上提高了5.88%，显示出显著的性能提升。

## 📝 摘要（中文）

本文系统性地研究了大型语言模型（LLMs）在生成宋词这一具有严格结构、音调和韵律约束的古典中文诗歌形式方面的能力。我们首先开发了一个全面的多维评估框架，包括：形式符合度评分、基于LLMs的自动质量评估、人类评估和分类探测任务。利用该框架，我们评估了18个LLMs的生成性能，涵盖3个专有模型和15个开源模型，采用五种提示策略。最后，我们提出了生成-评估架构，其中评估框架作为自动评估者，通过反馈信号对三种轻量级开源LLMs进行监督微调，形式符合度提高了5.88%。我们的研究为LLMs在生成具有文化意义和形式约束的文学文本方面的优缺点提供了新见解。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在生成结构化中文宋词时面临的音韵和结构约束问题。现有方法往往无法有效满足这些严格的生成要求，导致生成结果不符合传统诗歌的标准。

**核心思路**：论文的核心思路是构建一个生成-评估架构，通过自动评估框架提供反馈信号，指导模型的微调过程，从而提升生成的质量和符合度。

**技术框架**：整体架构包括四个主要模块：评估框架（形式符合度评分、自动质量评估、人类评估和分类探测任务）、18个LLMs的性能评估、生成-评估架构的实现，以及基于反馈的模型微调。

**关键创新**：最重要的技术创新在于提出了生成-评估架构，使得评估框架不仅用于评估，还能作为反馈机制，直接影响模型的训练过程。这一设计与传统的生成模型训练方法有本质区别。

**关键设计**：在模型微调过程中，采用了监督微调（SFT）的方法，结合形式符合度评分作为损失函数，确保生成结果在结构和韵律上更符合宋词的要求。

## 📊 实验亮点

实验结果显示，经过微调的三种轻量级开源LLMs在形式符合度上提高了5.88%。这一提升相较于未微调模型表现出显著的性能改进，验证了生成-评估架构的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括中文诗歌创作、文化遗产保护以及教育领域的文学创作教学。通过提升LLMs在生成传统文化文本方面的能力，可以促进文化传承和创新，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> This paper presents a systematic investigation into the constrained generation capabilities of large language models (LLMs) in producing Songci, a classical Chinese poetry form characterized by strict structural, tonal, and rhyme constraints defined by Cipai templates. We first develop a comprehensive, multi-faceted evaluation framework that includes: (i) a formal conformity score, (ii) automated quality assessment using LLMs, (iii) human evaluation, and (iv) classification-based probing tasks. Using this framework, we evaluate the generative performance of 18 LLMs, including 3 proprietary models and 15 open-source models across four families, under five prompting strategies: zero-shot, one-shot, completion-based, instruction-tuned, and chain-of-thought. Finally, we propose a Generate-Critic architecture in which the evaluation framework functions as an automated critic. Leveraging the critic's feedback as a reward signal, we fine-tune three lightweight open-source LLMs via supervised fine-tuning (SFT), resulting in improvements of up to 5.88% in formal conformity. Our findings offer new insights into the generative strengths and limitations of LLMs in producing culturally significant and formally constrained literary texts.

