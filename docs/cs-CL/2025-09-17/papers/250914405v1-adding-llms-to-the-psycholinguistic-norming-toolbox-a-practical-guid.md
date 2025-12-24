---
layout: default
title: "Adding LLMs to the psycholinguistic norming toolbox: A practical guide to getting the most out of human ratings"
---

# Adding LLMs to the psycholinguistic norming toolbox: A practical guide to getting the most out of human ratings

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.14405" class="toolbar-btn" target="_blank">📄 arXiv: 2509.14405v1</a>
  <a href="https://arxiv.org/pdf/2509.14405.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.14405v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.14405v1', 'Adding LLMs to the psycholinguistic norming toolbox: A practical guide to getting the most out of human ratings')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Javier Conde, María Grandury, Tairan Fu, Carlos Arriaga, Gonzalo Martínez, Thomas Clark, Sean Trott, Clarence Gerald Green, Pedro Reviriego, Marc Brysbaert

**分类**: cs.CL

**发布日期**: 2025-09-17

---

## 💡 一句话要点

**提出一种利用大型语言模型增强心理语言学规范数据集的方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `心理语言学` `大型语言模型` `词汇规范` `数据增强` `模型微调`

## 📋 核心要点

1. 心理语言学规范数据获取困难，现有方法成本高昂且效率低下，限制了相关研究的开展。
2. 利用大型语言模型预测词汇特征，结合人类规范数据进行验证，从而高效扩充数据集。
3. 通过案例研究表明，该方法在词汇熟悉度估计方面表现出色，微调模型后Spearman相关性达到0.9。

## 📝 摘要（中文）

词汇级别的心理语言学规范为语言处理理论提供了经验支持。然而，获取这些基于人类的测量数据并非总是可行或直接。一个有前景的方法是使用大型语言模型（LLM）直接预测这些特征，从而扩充人类规范数据集，这种做法在心理语言学和认知科学中正迅速普及。然而，这种方法的新颖性（以及LLM相对的不可理解性）需要采用严格的方法论，指导研究人员完成这一过程，展示可能的方法范围，并阐明那些不易察觉但可能在某些情况下使LLM的使用不切实际的局限性。本文提出了一种使用LLM估计词汇特征的综合方法，其中包含实践建议和我们自身经验中获得的教训。我们的方法涵盖了基础LLM的直接使用和模型的微调，后者可以在某些情况下产生显著的性能提升。本指南的一个主要重点是使用人类“金标准”规范来验证LLM生成的数据。我们还提出了一个实现我们方法论并支持商业和开源模型的软件框架。我们通过一个关于估计英语单词熟悉度的案例研究来说明所提出的方法。使用基础模型，我们与人类评分实现了0.8的Spearman相关性，而使用微调模型时，相关性提高到0.9。这种方法论、框架和最佳实践旨在为未来利用LLM进行心理语言学和词汇研究提供参考。

## 🔬 方法详解

**问题定义**：论文旨在解决心理语言学中词汇特征规范数据获取困难的问题。传统方法依赖于耗时耗力的人工标注，成本高昂且难以大规模扩展。现有方法缺乏效率和可扩展性，阻碍了心理语言学和认知科学的深入研究。

**核心思路**：论文的核心思路是利用大型语言模型（LLM）强大的语言理解和生成能力，直接预测词汇的心理语言学特征。通过将LLM作为一种“代理标注者”，可以快速生成大量的词汇特征数据，从而有效扩充现有的人工标注数据集。这种方法旨在降低数据获取成本，提高研究效率。

**技术框架**：该方法包含以下主要阶段：1) 选择合适的LLM（包括基础模型和可微调模型）；2) 设计合适的提示语（prompt），引导LLM生成目标词汇特征；3) 使用人工标注的“金标准”数据验证LLM生成的数据，评估其准确性和可靠性；4) （可选）对LLM进行微调，以进一步提高其预测性能；5) 使用开发的软件框架实现整个流程，支持商业和开源模型。

**关键创新**：该方法最重要的创新点在于将LLM引入心理语言学规范数据的生成过程，并提出了一套完整的、可验证的LLM应用方法论。与传统的人工标注方法相比，该方法具有更高的效率和可扩展性。此外，该方法强调使用人工标注数据验证LLM生成的数据，确保数据的质量和可靠性。

**关键设计**：在提示语设计方面，需要根据不同的词汇特征进行调整，以引导LLM生成准确的预测结果。在模型微调方面，可以使用人工标注数据作为训练集，采用合适的损失函数（例如均方误差）来优化LLM的参数。论文还开发了一个软件框架，方便研究人员使用和管理LLM，并进行数据验证和分析。

## 📊 实验亮点

论文通过英语词汇熟悉度估计的案例研究，验证了该方法的可行性和有效性。使用基础LLM时，与人工标注数据的Spearman相关性达到0.8，而使用微调后的LLM，相关性进一步提高到0.9。实验结果表明，该方法能够显著提高词汇特征估计的效率和准确性，为心理语言学研究提供了新的工具。

## 🎯 应用场景

该研究成果可广泛应用于心理语言学、认知科学、自然语言处理等领域。例如，可以利用该方法快速构建大规模的词汇情感、联想、具体性等规范数据集，为情感分析、文本理解、机器翻译等任务提供更丰富的资源。此外，该方法还可以用于研究不同语言之间的词汇特征差异，促进跨语言的认知研究。

## 📄 摘要（原文）

> Word-level psycholinguistic norms lend empirical support to theories of language processing. However, obtaining such human-based measures is not always feasible or straightforward. One promising approach is to augment human norming datasets by using Large Language Models (LLMs) to predict these characteristics directly, a practice that is rapidly gaining popularity in psycholinguistics and cognitive science. However, the novelty of this approach (and the relative inscrutability of LLMs) necessitates the adoption of rigorous methodologies that guide researchers through this process, present the range of possible approaches, and clarify limitations that are not immediately apparent, but may, in some cases, render the use of LLMs impractical.
>   In this work, we present a comprehensive methodology for estimating word characteristics with LLMs, enriched with practical advice and lessons learned from our own experience. Our approach covers both the direct use of base LLMs and the fine-tuning of models, an alternative that can yield substantial performance gains in certain scenarios. A major emphasis in the guide is the validation of LLM-generated data with human "gold standard" norms. We also present a software framework that implements our methodology and supports both commercial and open-weight models.
>   We illustrate the proposed approach with a case study on estimating word familiarity in English. Using base models, we achieved a Spearman correlation of 0.8 with human ratings, which increased to 0.9 when employing fine-tuned models. This methodology, framework, and set of best practices aim to serve as a reference for future research on leveraging LLMs for psycholinguistic and lexical studies.

