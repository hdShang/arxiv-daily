---
layout: default
title: "Evaluating LLMs Without Oracle Feedback: Agentic Annotation Evaluation Through Unsupervised Consistency Signals"
---

# Evaluating LLMs Without Oracle Feedback: Agentic Annotation Evaluation Through Unsupervised Consistency Signals

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.08809" class="toolbar-btn" target="_blank">📄 arXiv: 2509.08809v1</a>
  <a href="https://arxiv.org/pdf/2509.08809.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.08809v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.08809v1', 'Evaluating LLMs Without Oracle Feedback: Agentic Annotation Evaluation Through Unsupervised Consistency Signals')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Cheng Chen, Haiyan Yin, Ivor Tsang

**分类**: cs.CL

**发布日期**: 2025-09-10

**备注**: 11 pages, 10 figures

**期刊**: Published ICLR 2025 Workshop on Scaling Self-Improving Foundation Models without Human Supervision

---

## 💡 一句话要点

**提出基于一致性信号的Agentic标注评估方法，无需人工反馈评估LLM标注质量。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `无监督学习` `标注质量评估` `一致性信号` `Agentic标注` `模型选择` `自然语言处理`

## 📋 核心要点

1. 现有方法难以在缺乏人工反馈的动态环境中评估LLM标注质量，成本高且效率低。
2. 提出Agentic标注范式，利用学生模型与LLM协作，通过一致性信号进行无监督评估和改进。
3. 引入CAI比率作为无监督评估指标，实验表明其与LLM准确率呈强正相关，可用于模型选择。

## 📝 摘要（中文）

大型语言模型（LLM）与基于提示的任务结合，显著降低了数据标注成本和对人工标注者的依赖。然而，在缺乏人工反馈的动态、无监督环境中，评估其标注质量仍然具有挑战性，传统方法也难以奏效。为了解决这个问题，我们提出了一种新颖的agentic标注范式，其中学生模型与噪声教师（LLM）协作，在不依赖人工反馈的情况下评估和改进标注质量。学生模型作为一种无监督反馈机制，采用基于用户偏好的多数投票策略来评估LLM输出的一致性。为了系统地衡量LLM生成标注的可靠性，我们引入了一致和不一致（CAI）比率，这是一种新的无监督评估指标。CAI比率不仅量化了有限用户偏好下噪声教师的标注质量，而且在模型选择中起着关键作用，能够在动态、无监督环境中识别出鲁棒的LLM。应用于跨四个LLM的十个开放领域NLP数据集，CAI比率与LLM准确率呈强正相关，使其成为实际环境中无监督评估和模型选择的重要工具。

## 🔬 方法详解

**问题定义**：论文旨在解决在缺乏人工标注的情况下，如何有效评估大型语言模型（LLM）生成的标注质量的问题。现有方法依赖于人工反馈或预先标注好的数据集，这在动态变化的环境中成本高昂且难以扩展。因此，需要一种无监督的方法来评估LLM标注的可靠性，并进行模型选择。

**核心思路**：论文的核心思路是利用一个学生模型作为无监督的反馈机制，与LLM（作为噪声教师）进行协作。学生模型通过评估LLM生成标注的一致性来判断其质量。如果LLM的标注在不同情况下表现出较高的一致性，则认为其标注质量较高。这种方法避免了对人工标注的依赖，可以在动态、无监督的环境中进行评估。

**技术框架**：整体框架包含一个噪声教师（LLM）和一个学生模型。LLM负责生成标注，学生模型负责评估这些标注的一致性。具体流程如下：1) LLM对输入数据进行标注，生成多个候选标注结果；2) 学生模型基于用户偏好，对这些候选标注结果进行多数投票，选择最一致的标注；3) 计算一致和不一致（CAI）比率，作为评估LLM标注质量的指标。

**关键创新**：论文的关键创新在于提出了Agentic标注范式和CAI比率。Agentic标注范式通过引入学生模型，实现了无监督的标注质量评估。CAI比率则提供了一种量化标注一致性的方法，可以用于模型选择和性能监控。与现有方法相比，该方法无需人工标注，更具灵活性和可扩展性。

**关键设计**：CAI比率的计算是关键设计之一。它基于学生模型的多数投票结果，统计一致的标注和不一致的标注数量，然后计算它们的比率。用户偏好通过prompt工程融入到学生模型的多数投票策略中。论文中没有明确提及损失函数或网络结构，因为学生模型主要依赖于prompt和多数投票策略，而非复杂的神经网络结构。

## 📊 实验亮点

实验结果表明，CAI比率与LLM的准确率之间存在显著的正相关关系。在十个开放领域的NLP数据集上，CAI比率能够有效地评估不同LLM的标注质量，并帮助选择性能最佳的模型。该方法在无需人工标注的情况下，实现了与人工评估相近的效果。

## 🎯 应用场景

该研究成果可应用于各种需要大规模数据标注的自然语言处理任务，例如情感分析、文本分类、信息抽取等。尤其适用于数据标注成本高昂或难以获取人工标注的场景。该方法能够帮助用户在无监督环境下选择合适的LLM，并监控其标注质量，从而提高下游任务的性能。

## 📄 摘要（原文）

> Large Language Models (LLMs), when paired with prompt-based tasks, have significantly reduced data annotation costs and reliance on human annotators. However, evaluating the quality of their annotations remains challenging in dynamic, unsupervised environments where oracle feedback is scarce and conventional methods fail. To address this challenge, we propose a novel agentic annotation paradigm, where a student model collaborates with a noisy teacher (the LLM) to assess and refine annotation quality without relying on oracle feedback. The student model, acting as an unsupervised feedback mechanism, employs a user preference-based majority voting strategy to evaluate the consistency of the LLM outputs. To systematically measure the reliability of LLM-generated annotations, we introduce the Consistent and Inconsistent (CAI) Ratio, a novel unsupervised evaluation metric. The CAI Ratio not only quantifies the annotation quality of the noisy teacher under limited user preferences but also plays a critical role in model selection, enabling the identification of robust LLMs in dynamic, unsupervised environments. Applied to ten open-domain NLP datasets across four LLMs, the CAI Ratio demonstrates a strong positive correlation with LLM accuracy, establishing it as an essential tool for unsupervised evaluation and model selection in real-world settings.

