---
layout: default
title: "The Translation Barrier Hypothesis: Multilingual Generation with Large Language Models Suffers from Implicit Translation Failure"
---

# The Translation Barrier Hypothesis: Multilingual Generation with Large Language Models Suffers from Implicit Translation Failure

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.22724" class="toolbar-btn" target="_blank">📄 arXiv: 2506.22724v2</a>
  <a href="https://arxiv.org/pdf/2506.22724.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.22724v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.22724v2', 'The Translation Barrier Hypothesis: Multilingual Generation with Large Language Models Suffers from Implicit Translation Failure')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Niyati Bafna, Tianjian Li, Kenton Murray, David R. Mortensen, David Yarowsky, Hale Sirin, Daniel Khashabi

**分类**: cs.CL

**发布日期**: 2025-06-28 (更新: 2025-10-20)

**备注**: 28 pages, incl. appendix

---

## 💡 一句话要点

**提出翻译障碍假说以解决多语言生成质量问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多语言生成` `翻译障碍` `大型语言模型` `低资源语言` `任务解决` `隐含失败` `语言对比分析`

## 📋 核心要点

1. 现有大型语言模型在多语言生成中对中低资源语言的支持不足，导致生成质量低下。
2. 本文提出翻译障碍假说，认为任务解决成功但翻译失败是导致低质量输出的主要原因。
3. 通过对108对语言的实验，发现翻译障碍在大多数语言对的错误中占主导地位，尤其在低资源语言中更为严重。

## 📝 摘要（中文）

多语言生成在大型语言模型（LLMs）中，尤其是中低资源语言的生成质量往往较差，但其原因尚不明确。本文首先展示了隐含的任务解决与翻译管道，模型在目标语言无关的方式下解决任务，然后将答案概念翻译为目标语言。我们假设翻译阶段的失败是导致最终输出质量低下的重要原因，并将其形式化为翻译障碍假说。通过对108对语言的词汇翻译任务进行量化分析，我们发现翻译障碍在大多数语言对的错误中占主导地位，尤其在低资源目标语言中表现尤为严重。我们的结果强调了端到端多语言生成中的一个重要瓶颈，为未来提升LLMs的多语言能力提供了参考。

## 🔬 方法详解

**问题定义**：本文要解决的问题是大型语言模型在多语言生成中，尤其是中低资源语言的生成质量低下。现有方法未能有效识别任务解决与翻译之间的关系，导致输出质量不佳。

**核心思路**：论文提出翻译障碍假说，认为模型在解决任务时虽然成功，但在翻译阶段出现隐含失败，从而影响最终输出质量。通过量化分析，明确各阶段对最终结果的影响。

**技术框架**：整体架构包括两个主要阶段：第一阶段为任务解决，模型在目标语言无关的情况下生成答案；第二阶段为翻译，将生成的答案概念翻译为目标语言。

**关键创新**：最重要的技术创新点在于提出了翻译障碍假说，明确了任务解决与翻译之间的隐含关系，并量化了其对生成质量的影响。这与现有方法的主要区别在于关注翻译阶段的失败。

**关键设计**：在实验中，使用了108对语言进行词汇翻译任务，设计了相应的评估指标，以量化翻译障碍对错误的贡献。具体的参数设置和损失函数设计未在摘要中详细说明，需参考完整论文。

## 📊 实验亮点

实验结果表明，翻译障碍在大多数语言对的错误中占主导地位，尤其在低资源语言中，翻译失败的影响尤为显著。这一发现为未来的多语言生成研究提供了重要的方向和改进依据。

## 🎯 应用场景

该研究的潜在应用领域包括多语言翻译系统、跨语言信息检索和多语言对话系统等。通过识别和解决翻译障碍，未来的研究可以显著提升大型语言模型在多语言生成中的表现，促进不同语言之间的交流与理解。

## 📄 摘要（原文）

> Multilingual generation with large language models (LLMs) is often of poor quality for mid- to low-resource languages, but the causes for this are not well-understood. We first demonstrate the existence of an implicit task-solving-->translation pipeline for generation, whereby the model first solves the required task in a largely target-language-agnostic manner, and subsequently translates answer concepts into the intended target language. We hypothesize that the failure of the translation stage, despite task-solving success, is an important culprit for the observed low quality of final outputs, and formalize this as the translation barrier hypothesis. We quantify the extent to which either stage in the pipeline is responsible for final failure for a word translation task across 108 language pairs, and find that the translation barrier explains a dominant portion of error for a majority of language pairs, and is especially severe for low-resource target languages. Our results highlight an important bottleneck for end-to-end multilingual generation, relevant for future work seeking to improve multilinguality in LLMs.

