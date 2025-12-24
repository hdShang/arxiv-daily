---
layout: default
title: "Bias after Prompting: Persistent Discrimination in Large Language Models"
---

# Bias after Prompting: Persistent Discrimination in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.08146" class="toolbar-btn" target="_blank">📄 arXiv: 2509.08146v2</a>
  <a href="https://arxiv.org/pdf/2509.08146.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.08146v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.08146v2', 'Bias after Prompting: Persistent Discrimination in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nivedha Sivakumar, Natalie Mackraz, Samira Khorshidi, Krishna Patel, Barry-John Theobald, Luca Zappella, Nicholas Apostoloff

**分类**: cs.CL, cs.LG

**发布日期**: 2025-09-09 (更新: 2025-11-19)

---

## 💡 一句话要点

**揭示Prompting后的大语言模型偏见：持续存在的歧视现象**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `偏见转移` `Prompting` `公平性` `因果模型`

## 📋 核心要点

1. 现有研究低估了Prompting方法引入的偏见风险，认为预训练模型的偏见不会转移到调整后的模型。
2. 该研究通过分析因果模型中Prompt调整后的偏见转移现象，揭示了Prompting方法可能引入并放大偏见。
3. 实验表明，即使采用流行的Prompting去偏见策略，也无法始终如一地减少跨模型、任务和人口统计的偏见转移。

## 📝 摘要（中文）

先前关于偏见转移假设（BTH）的研究可能存在一个危险的假设，即预训练的大语言模型（LLM）中的偏见不会转移到经过调整的模型中。本文通过在因果模型中研究prompt调整下的BTH，从而否定了这一假设，因为prompting是实际应用中一种非常流行和易于使用的调整策略。与之前的工作相反，我们发现偏见可以通过prompting转移，并且流行的基于prompt的缓解方法并不能始终如一地防止偏见转移。具体而言，内在偏见与prompt调整后的偏见之间的相关性在不同的人口统计和任务中保持中等到强烈的水平——例如，在共指消解中性别（rho >= 0.94），在问答中年龄（rho >= 0.98）和宗教（rho >= 0.69）。此外，我们发现当改变少量样本组成参数（如样本大小、刻板印象内容、职业分布和代表性平衡）时，偏见仍然高度相关（rho >= 0.90）。我们评估了几种基于prompt的去偏见策略，发现不同的方法有不同的优势，但没有一种方法能够始终如一地减少跨模型、任务或人口统计的偏见转移。这些结果表明，纠正内在模型中的偏见，并可能提高推理能力，可以防止偏见传播到下游任务。

## 🔬 方法详解

**问题定义**：现有研究未能充分认识到Prompting方法在大型语言模型中引入和传播偏见的风险。尽管Prompting是一种广泛使用的模型调整策略，但之前的研究可能错误地认为预训练模型中的偏见不会转移到通过Prompting调整后的模型中。这种假设忽略了Prompting可能放大或改变原有偏见的可能性，导致下游任务中出现不公平或歧视性的结果。

**核心思路**：本文的核心思路是通过实证研究来验证Prompting是否会导致偏见转移，并评估现有Prompting去偏见策略的有效性。研究人员通过设计一系列实验，系统地分析了内在偏见与Prompt调整后的偏见之间的相关性，以及不同Prompting参数对偏见转移的影响。

**技术框架**：该研究的技术框架主要包括以下几个步骤：1) 选择具有代表性的大型语言模型和下游任务；2) 设计不同的Prompting策略，包括少量样本学习和不同的Prompt组成方式；3) 使用预定义的偏见评估指标来衡量模型在不同Prompt下的偏见程度；4) 分析内在偏见与Prompt调整后的偏见之间的相关性，以及不同Prompting参数对偏见转移的影响；5) 评估几种流行的Prompting去偏见策略的有效性。

**关键创新**：该研究的关键创新在于：1) 验证了Prompting会导致偏见转移，否定了之前研究中关于偏见不会转移的假设；2) 系统地分析了不同Prompting参数对偏见转移的影响，揭示了Prompting策略的复杂性；3) 评估了现有Prompting去偏见策略的有效性，发现这些策略并不能始终如一地减少偏见转移。

**关键设计**：研究中关键的设计包括：1) 选择了具有代表性的下游任务，如共指消解和问答，以评估不同任务下的偏见转移情况；2) 设计了不同的Prompting策略，包括改变样本大小、刻板印象内容、职业分布和代表性平衡等参数，以分析不同Prompting参数对偏见转移的影响；3) 使用了预定义的偏见评估指标，如性别、年龄和宗教偏见，以量化模型在不同Prompt下的偏见程度。

## 📊 实验亮点

实验结果表明，内在偏见与Prompt调整后的偏见之间存在很强的相关性，例如在共指消解中性别（rho >= 0.94），在问答中年龄（rho >= 0.98）和宗教（rho >= 0.69）。即使改变少量样本组成参数，偏见仍然高度相关（rho >= 0.90）。现有的Prompting去偏见策略并不能始终如一地减少偏见转移。

## 🎯 应用场景

该研究成果对大型语言模型的公平性和可靠性具有重要意义。它可以应用于开发更公平、更负责任的AI系统，例如在招聘、信贷评估和法律决策等领域。未来的研究可以探索更有效的去偏见策略，并开发能够自动检测和缓解Prompting引入的偏见的工具。

## 📄 摘要（原文）

> A dangerous assumption that can be made from prior work on the bias transfer hypothesis (BTH) is that biases do not transfer from pre-trained large language models (LLMs) to adapted models. We invalidate this assumption by studying the BTH in causal models under prompt adaptations, as prompting is an extremely popular and accessible adaptation strategy used in real-world applications. In contrast to prior work, we find that biases can transfer through prompting and that popular prompt-based mitigation methods do not consistently prevent biases from transferring. Specifically, the correlation between intrinsic biases and those after prompt adaptation remain moderate to strong across demographics and tasks -- for example, gender (rho >= 0.94) in co-reference resolution, and age (rho >= 0.98) and religion (rho >= 0.69) in question answering. Further, we find that biases remain strongly correlated when varying few-shot composition parameters, such as sample size, stereotypical content, occupational distribution and representational balance (rho >= 0.90). We evaluate several prompt-based debiasing strategies and find that different approaches have distinct strengths, but none consistently reduce bias transfer across models, tasks or demographics. These results demonstrate that correcting bias, and potentially improving reasoning ability, in intrinsic models may prevent propagation of biases to downstream tasks.

