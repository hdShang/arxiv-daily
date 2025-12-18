---
layout: default
title: SeBERTis: A Framework for Producing Classifiers of Security-Related Issue Reports
---

# SeBERTis: A Framework for Producing Classifiers of Security-Related Issue Reports

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15003" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15003v1</a>
  <a href="https://arxiv.org/pdf/2512.15003.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15003v1" onclick="toggleFavorite(this, '2512.15003v1', 'SeBERTis: A Framework for Producing Classifiers of Security-Related Issue Reports')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sogol Masoumzadeh, Yufei Li, Shane McIntosh, Dániel Varró, Lili Wei

**分类**: cs.CR, cs.LG, cs.SE

**发布日期**: 2025-12-17

**备注**: This is the author pre-print. The manuscript has been accepted for publication at SANER 2026!

---

## 💡 一句话要点

**SEBERTIS：一个用于生成安全相关问题报告分类器的框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `安全问题分类` `问题报告分析` `深度学习` `自然语言处理` `Masked Language Model` `语义替代` `软件安全`

## 📋 核心要点

1. 现有安全问题报告分类器依赖词汇线索，对复杂或未见过的安全问题检测率低，难以满足实际应用需求。
2. SEBERTIS框架通过训练深度神经网络，使其独立于词汇线索，利用语义替代进行Masked Language Model微调，提升泛化能力。
3. 实验表明，SEBERTIS在安全问题检测上显著优于现有机器学习和大型语言模型方法，F1分数最高提升74.53%。

## 📝 摘要（中文）

监控问题跟踪器的提交是软件维护的关键活动。一个主要目标是优先处理高风险、与安全相关的错误。如果能够及早识别这些错误，就可以降低传播到依赖产品和危及利益相关者利益的风险。为了帮助分类工程师完成这项任务，已经提出了几种自动检测技术，从机器学习（ML）模型到提示大型语言模型（LLM）。虽然在某种程度上很有希望，但先前的技术通常会记忆词汇线索作为决策捷径，从而导致对更复杂的提交的检测率较低。因此，这些分类器尚未达到实时检测安全相关问题的实际期望。为了解决这些限制，我们提出了SEBERTIS，一个训练深度神经网络（DNN）作为独立于词汇线索的分类器的框架，以便它们可以自信地检测完全未见过的安全相关问题。SEBERTIS利用微调双向Transformer架构作为Masked Language Models（MLM），在一系列语义等价的词汇到预测标签（我们称之为语义替代）上，当它们被替换为mask时。我们的SEBERTIS训练的分类器在检测10,000个GitHub问题报告的精选语料库中的安全相关问题时，实现了0.9880的F1分数，大大优于最先进的问题分类器，与基于ML的基线相比，检测精度、召回率和F1分数分别提高了14.44%-96.98%、15.40%-93.07%和14.90%-94.72%。我们的分类器也大大超过了LLM基线，精度、召回率和F1分数分别提高了23.20%-63.71%、36.68%-85.63%和39.49%-74.53%。

## 🔬 方法详解

**问题定义**：论文旨在解决安全相关问题报告的自动分类问题。现有方法主要依赖于词汇线索，容易受到对抗样本的攻击，并且对于未见过的安全漏洞类型泛化能力较差。这些方法无法有效识别复杂的、语义上不明显的安全问题，导致实际应用效果不佳。

**核心思路**：SEBERTIS的核心思路是训练一个不依赖于词汇线索的深度神经网络分类器。通过利用语义替代（Semantic Surrogates）进行Masked Language Model (MLM) 的微调，模型能够学习到更深层次的语义信息，从而提高对未见过的安全问题的识别能力。这种方法旨在使模型能够理解问题报告的含义，而不仅仅是记住关键词。

**技术框架**：SEBERTIS框架主要包含以下几个步骤：1) 数据预处理：收集并清洗安全问题报告数据集。2) 语义替代生成：为每个问题报告生成一系列语义等价的变体，作为语义替代。3) MLM微调：使用双向Transformer架构（如BERT）作为Masked Language Model，在包含语义替代的数据集上进行微调。4) 分类器训练：使用微调后的Transformer模型作为特征提取器，训练一个分类器来区分安全相关和非安全相关的问题报告。

**关键创新**：SEBERTIS的关键创新在于使用语义替代进行MLM微调，从而使模型能够学习到独立于词汇线索的语义表示。这种方法有效地解决了现有方法过度依赖词汇线索的问题，提高了模型的泛化能力和鲁棒性。

**关键设计**：SEBERTIS使用双向Transformer架构作为基础模型，并采用Masked Language Model的目标函数进行微调。语义替代的生成方式是关键，需要保证替代后的文本在语义上与原始文本尽可能接近。分类器的训练可以使用交叉熵损失函数，并采用合适的优化算法（如Adam）进行优化。具体的参数设置（如Transformer的层数、隐藏层大小、学习率等）需要根据具体数据集进行调整。

## 📊 实验亮点

SEBERTIS在包含10,000个GitHub问题报告的数据集上取得了显著的性能提升，F1分数达到0.9880。与基于机器学习的基线方法相比，SEBERTIS的精度、召回率和F1分数分别提高了14.44%-96.98%、15.40%-93.07%和14.90%-94.72%。与大型语言模型基线相比，精度、召回率和F1分数分别提高了23.20%-63.71%、36.68%-85.63%和39.49%-74.53%。

## 🎯 应用场景

SEBERTIS可应用于软件开发生命周期的多个阶段，例如问题跟踪、漏洞管理和安全审计。通过自动识别安全相关问题报告，可以帮助开发人员和安全工程师更快地响应潜在的安全威胁，降低软件漏洞带来的风险。该技术还可以用于构建智能安全分析系统，提高安全事件的检测和响应效率。

## 📄 摘要（原文）

> Monitoring issue tracker submissions is a crucial software maintenance activity. A key goal is the prioritization of high risk, security-related bugs. If such bugs can be recognized early, the risk of propagation to dependent products and endangerment of stakeholder benefits can be mitigated. To assist triage engineers with this task, several automatic detection techniques, from Machine Learning (ML) models to prompting Large Language Models (LLMs), have been proposed. Although promising to some extent, prior techniques often memorize lexical cues as decision shortcuts, yielding low detection rate specifically for more complex submissions. As such, these classifiers do not yet reach the practical expectations of a real-time detector of security-related issues. To address these limitations, we propose SEBERTIS, a framework to train Deep Neural Networks (DNNs) as classifiers independent of lexical cues, so that they can confidently detect fully unseen security-related issues. SEBERTIS capitalizes on fine-tuning bidirectional transformer architectures as Masked Language Models (MLMs) on a series of semantically equivalent vocabulary to prediction labels (which we call Semantic Surrogates) when they have been replaced with a mask. Our SEBERTIS-trained classifier achieves a 0.9880 F1-score in detecting security-related issues of a curated corpus of 10,000 GitHub issue reports, substantially outperforming state-of-the-art issue classifiers, with 14.44%-96.98%, 15.40%-93.07%, and 14.90%-94.72% higher detection precision, recall, and F1-score over ML-based baselines. Our classifier also substantially surpasses LLM baselines, with an improvement of 23.20%-63.71%, 36.68%-85.63%, and 39.49%-74.53% for precision, recall, and F1-score.

