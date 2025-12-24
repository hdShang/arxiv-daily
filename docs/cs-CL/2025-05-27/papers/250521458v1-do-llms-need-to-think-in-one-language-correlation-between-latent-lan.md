---
layout: default
title: Do LLMs Need to Think in One Language? Correlation between Latent Language and Task Performance
---

# Do LLMs Need to Think in One Language? Correlation between Latent Language and Task Performance

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21458" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21458v1</a>
  <a href="https://arxiv.org/pdf/2505.21458.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21458v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21458v1', 'Do LLMs Need to Think in One Language? Correlation between Latent Language and Task Performance')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shintaro Ozaki, Tatsuya Hiraoka, Hiroto Otake, Hiroki Ouchi, Masaru Isonuma, Benjamin Heinzerling, Kentaro Inui, Taro Watanabe, Yusuke Miyao, Yohei Oseki, Yu Takagi

**分类**: cs.CL

**发布日期**: 2025-05-27

---

## 💡 一句话要点

**探讨潜在语言一致性对LLM任务性能的影响**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `潜在语言` `下游任务` `语言适应性` `机器翻译` `跨文化交流`

## 📋 核心要点

1. 现有研究较少探讨潜在语言与下游任务性能之间的关系，导致对其影响的理解不足。
2. 论文提出通过变换输入提示语言，分析潜在语言一致性与任务性能的相关性，以验证潜在语言的重要性。
3. 实验结果显示，潜在语言的一致性并非总是优化下游任务性能的必要条件，模型能够适应目标语言。

## 📝 摘要（中文）

大型语言模型（LLMs）被认为使用一种称为潜在语言的内部语言来处理信息，该语言可能与输入或输出语言不同。然而，潜在语言与输入和输出语言之间的差异如何影响下游任务性能仍然未被充分探索。我们的研究假设，始终在潜在语言中思考可以增强下游任务性能。为此，我们在多个下游任务中变换输入提示语言，并分析潜在语言一致性与任务性能之间的相关性。实验结果表明，保持潜在语言的一致性并不总是对下游任务性能最优的必要条件，因为模型能够在最终层附近调整其内部表示以匹配目标语言，从而减少一致性对整体性能的影响。

## 🔬 方法详解

**问题定义**：本论文旨在探讨潜在语言与下游任务性能之间的关系，现有方法未能充分揭示潜在语言对任务表现的影响。

**核心思路**：通过在多个下游任务中变换输入提示语言，验证潜在语言的一致性是否能增强任务性能，提出潜在语言的重要性。

**技术框架**：研究设计包括创建多样化的问题数据集，涵盖翻译和地理文化等领域，进行多种大型语言模型的实验，分析其性能表现。

**关键创新**：论文的创新在于系统性地研究潜在语言一致性对任务性能的影响，发现模型在最终层能够调整内部表示以适应目标语言，从而降低一致性的重要性。

**关键设计**：在实验中，设置了不同的输入提示语言，采用了多种大型语言模型进行对比，关注模型在翻译和地理文化任务中的表现差异。

## 📊 实验亮点

实验结果表明，保持潜在语言一致性并不总是优化下游任务性能的必要条件。在翻译和地理文化任务中，模型能够有效适应目标语言，减少一致性对性能的影响，展示出模型的灵活性和适应性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、机器翻译和跨文化交流等。通过深入理解潜在语言对任务性能的影响，可以优化大型语言模型的设计，提高其在多语言环境下的适应能力，进而推动智能助手、翻译工具等实际应用的发展。

## 📄 摘要（原文）

> Large Language Models (LLMs) are known to process information using a proficient internal language consistently, referred to as latent language, which may differ from the input or output languages. However, how the discrepancy between the latent language and the input and output language affects downstream task performance remains largely unexplored. While many studies research the latent language of LLMs, few address its importance in influencing task performance. In our study, we hypothesize that thinking in latent language consistently enhances downstream task performance. To validate this, our work varies the input prompt languages across multiple downstream tasks and analyzes the correlation between consistency in latent language and task performance. We create datasets consisting of questions from diverse domains such as translation and geo-culture, which are influenced by the choice of latent language. Experimental results across multiple LLMs on translation and geo-culture tasks, which are sensitive to the choice of language, indicate that maintaining consistency in latent language is not always necessary for optimal downstream task performance. This is because these models adapt their internal representations near the final layers to match the target language, reducing the impact of consistency on overall performance.

