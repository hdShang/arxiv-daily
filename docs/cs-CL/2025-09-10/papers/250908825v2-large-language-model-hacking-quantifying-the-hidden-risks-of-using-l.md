---
layout: default
title: "Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation"
---

# Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.08825" class="toolbar-btn" target="_blank">📄 arXiv: 2509.08825v2</a>
  <a href="https://arxiv.org/pdf/2509.08825.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.08825v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.08825v2', 'Large Language Model Hacking: Quantifying the Hidden Risks of Using LLMs for Text Annotation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Joachim Baumann, Paul Röttger, Aleksandra Urman, Albert Wendsjö, Flor Miriam Plaza-del-Arco, Johannes B. Gruber, Dirk Hovy

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-09-10 (更新: 2025-10-06)

---

## 💡 一句话要点

**量化LLM文本标注的潜在风险：揭示LLM破解现象及应对策略**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `文本标注` `LLM破解` `风险评估` `社会科学研究`

## 📋 核心要点

1. 现有方法依赖LLM进行文本标注，但模型选择和提示策略的差异可能导致偏差和错误结论。
2. 论文提出“LLM破解”概念，指配置选择导致错误结论的现象，并研究有意和意外的破解风险。
3. 实验表明LLM破解风险高，即使是先进模型也易受影响，人工标注和回归校正可有效缓解。

## 📝 摘要（中文）

大型语言模型（LLM）正迅速改变社会科学研究，通过自动化数据标注和文本分析等劳动密集型任务。然而，LLM的输出结果因研究人员的实施选择（如模型选择或提示策略）而异，这可能引入系统性偏差和随机误差，进而导致I型（假阳性）、II型（假阴性）、S型（错误符号）或M型（夸大效应）错误。我们将这种配置选择导致错误结论的现象称为LLM破解。研究表明，有意的LLM破解非常简单。通过复制21项已发表社会科学研究中的37项数据标注任务，我们证明，只需少量提示释义，几乎任何结果都可以呈现为具有统计学意义。除了有意操纵，对来自18个不同LLM的1300万个标签在2361个实际假设上的分析表明，即使遵循标准研究实践，也存在意外LLM破解的高风险。对于最先进的LLM，大约31%的假设得出不正确的结论，而对于较小的语言模型，这一比例为一半。虽然更高的任务性能和更强的通用模型能力降低了LLM破解风险，但即使是高度准确的模型仍然容易受到影响。LLM破解的风险随着效应量的增加而降低，表明需要对接近显著性阈值的基于LLM的发现进行更严格的验证。我们分析了21种缓解技术，发现人工标注为防止假阳性提供了关键保护。常见的回归估计器校正技术可以恢复有效的推断，但需要在I型和II型错误之间进行权衡。最后，我们发布了一系列实用的建议，以防止LLM破解。

## 🔬 方法详解

**问题定义**：论文旨在解决使用大型语言模型（LLM）进行文本标注时，由于模型选择、提示工程等配置选择不当，导致研究结论出现偏差甚至错误的“LLM破解”问题。现有方法缺乏对这种风险的量化评估和有效缓解措施，使得研究结果的可靠性受到威胁。

**核心思路**：论文的核心思路是量化LLM在文本标注任务中产生错误结论的风险，并分析不同因素（如模型大小、任务难度、提示策略）对该风险的影响。通过模拟真实的研究场景，评估有意和意外的LLM破解发生的可能性，并探索有效的缓解策略。

**技术框架**：论文的技术框架主要包括以下几个阶段：1) 选取已发表的社会科学研究作为基准，复制其数据标注任务。2) 使用不同的LLM和提示策略进行标注，并分析结果的差异。3) 通过统计分析，量化LLM破解的风险，并识别导致错误的因素。4) 评估不同的缓解技术（如人工标注、回归校正）的效果。

**关键创新**：论文的关键创新在于：1) 首次提出了“LLM破解”的概念，并对其进行了量化评估。2) 揭示了即使是先进的LLM也存在较高的破解风险，并分析了风险的影响因素。3) 评估了多种缓解技术的效果，为研究人员提供了实用的建议。

**关键设计**：论文的关键设计包括：1) 选取具有代表性的社会科学研究作为基准，保证了研究的实际意义。2) 使用多种LLM和提示策略，覆盖了不同的配置选择。3) 采用严格的统计分析方法，量化了LLM破解的风险。4) 评估了多种缓解技术，并给出了实用的建议。

## 📊 实验亮点

研究表明，即使是最先进的LLM，在约31%的假设中也会得出不正确的结论。通过少量提示释义，几乎任何结果都可以呈现为具有统计学意义。人工标注为防止假阳性提供了关键保护，而常见的回归估计器校正技术可以恢复有效的推断。

## 🎯 应用场景

该研究成果可应用于社会科学、自然语言处理等领域，帮助研究人员在使用LLM进行文本标注时，更好地评估和控制风险，提高研究结果的可靠性。同时，该研究也为LLM的安全性评估和风险管理提供了新的思路。

## 📄 摘要（原文）

> Large language models are rapidly transforming social science research by enabling the automation of labor-intensive tasks like data annotation and text analysis. However, LLM outputs vary significantly depending on the implementation choices made by researchers (e.g., model selection or prompting strategy). Such variation can introduce systematic biases and random errors, which propagate to downstream analyses and cause Type I (false positive), Type II (false negative), Type S (wrong sign), or Type M (exaggerated effect) errors. We call this phenomenon where configuration choices lead to incorrect conclusions LLM hacking.
>   We find that intentional LLM hacking is strikingly simple. By replicating 37 data annotation tasks from 21 published social science studies, we show that, with just a handful of prompt paraphrases, virtually anything can be presented as statistically significant.
>   Beyond intentional manipulation, our analysis of 13 million labels from 18 different LLMs across 2361 realistic hypotheses shows that there is also a high risk of accidental LLM hacking, even when following standard research practices. We find incorrect conclusions in approximately 31% of hypotheses for state-of-the-art LLMs, and in half the hypotheses for smaller language models. While higher task performance and stronger general model capabilities reduce LLM hacking risk, even highly accurate models remain susceptible. The risk of LLM hacking decreases as effect sizes increase, indicating the need for more rigorous verification of LLM-based findings near significance thresholds. We analyze 21 mitigation techniques and find that human annotations provide crucial protection against false positives. Common regression estimator correction techniques can restore valid inference but trade off Type I vs. Type II errors.
>   We publish a list of practical recommendations to prevent LLM hacking.

