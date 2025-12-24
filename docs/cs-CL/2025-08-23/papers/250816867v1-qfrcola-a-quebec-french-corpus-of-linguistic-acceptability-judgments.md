---
layout: default
title: "QFrCoLA: a Quebec-French Corpus of Linguistic Acceptability Judgments"
---

# QFrCoLA: a Quebec-French Corpus of Linguistic Acceptability Judgments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.16867" class="toolbar-btn" target="_blank">📄 arXiv: 2508.16867v1</a>
  <a href="https://arxiv.org/pdf/2508.16867.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.16867v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.16867v1', 'QFrCoLA: a Quebec-French Corpus of Linguistic Acceptability Judgments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: David Beauchemin, Richard Khoury

**分类**: cs.CL

**发布日期**: 2025-08-23

**备注**: Accepted to EMNLP 2025

---

## 💡 一句话要点

**提出QFrCoLA数据集以评估法语语言模型的语言判断能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语言模型` `魁北克法语` `可接受性判断` `数据集构建` `Transformer模型` `语言评估` `机器学习`

## 📋 核心要点

1. 现有的语言模型在语言知识的内化方面理解有限，缺乏有效的评估标准。
2. QFrCoLA数据集提供了一个包含魁北克法语的可接受性判断的二元数据集，旨在填补这一空白。
3. 实验结果显示，微调的Transformer模型在QFrCoLA基准测试中优于其他方法，揭示了其在语言判断能力上的优势。

## 📝 摘要（中文）

大型基于Transformer的语言模型在多种下游任务中表现出色，但对其语言知识的内在理解仍有限。本文介绍了QFrCoLA（魁北克法语语言可接受性判断语料库），该数据集包含25,153个领域内和2,675个领域外的句子。通过QFrCoLA及其他七个语言可接受性判断语料库，本文对七种语言模型进行了基准测试。结果表明，经过微调的Transformer语言模型在大多数语言中表现良好，而零样本分类的大型语言模型在该任务上表现不佳。QFrCoLA基准测试显示，微调的Transformer模型优于其他方法，且预训练的跨语言模型在魁北克法语的语言判断能力上表现欠佳。该数据集为基准测试语言模型的语言判断能力提供了挑战性数据。

## 🔬 方法详解

**问题定义**：本文旨在解决现有语言模型在魁北克法语的语言判断能力评估不足的问题。现有方法未能有效捕捉语言模型的语言知识内化情况。

**核心思路**：通过构建QFrCoLA数据集，提供一个包含魁北克法语的可接受性判断的标准化数据集，以便对语言模型进行系统评估。该设计旨在通过具体的语言规范示例来评估模型的语言判断能力。

**技术框架**：整体架构包括数据集构建、模型选择与微调、以及基准测试三个主要阶段。数据集构建阶段涉及收集和标注魁北克法语句子，模型选择与微调阶段则使用七种不同的语言模型进行训练和评估。

**关键创新**：QFrCoLA数据集的构建是本文的主要创新点，它提供了一个专注于语言规范而非说话者感受的评估标准。这与现有方法的主观性评估形成鲜明对比。

**关键设计**：在实验中，采用了多种语言模型的微调策略，使用了标准的二元分类损失函数，并在模型训练中关注魁北克法语的特定语言特征。

## 📊 实验亮点

实验结果显示，经过微调的Transformer语言模型在QFrCoLA基准测试中表现优异，平均性能超过其他测试方法。特别是，微调模型在魁北克法语的语言判断能力上显著优于零样本分类的大型语言模型，表明微调策略在该任务中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理中的语言模型评估、语言教学、以及语言学研究。通过提供标准化的评估数据集，QFrCoLA能够帮助研究人员更好地理解和改进语言模型的语言判断能力，推动相关技术的发展。未来，该数据集可能会被扩展至其他语言或方言，进一步提升其应用价值。

## 📄 摘要（原文）

> Large and Transformer-based language models perform outstandingly in various downstream tasks. However, there is limited understanding regarding how these models internalize linguistic knowledge, so various linguistic benchmarks have recently been proposed to facilitate syntactic evaluation of language models across languages. This paper introduces QFrCoLA (Quebec-French Corpus of Linguistic Acceptability Judgments), a normative binary acceptability judgments dataset comprising 25,153 in-domain and 2,675 out-of-domain sentences. Our study leverages the QFrCoLA dataset and seven other linguistic binary acceptability judgment corpora to benchmark seven language models. The results demonstrate that, on average, fine-tuned Transformer-based LM are strong baselines for most languages and that zero-shot binary classification large language models perform poorly on the task. However, for the QFrCoLA benchmark, on average, a fine-tuned Transformer-based LM outperformed other methods tested. It also shows that pre-trained cross-lingual LLMs selected for our experimentation do not seem to have acquired linguistic judgment capabilities during their pre-training for Quebec French. Finally, our experiment results on QFrCoLA show that our dataset, built from examples that illustrate linguistic norms rather than speakers' feelings, is similar to linguistic acceptability judgment; it is a challenging dataset that can benchmark LM on their linguistic judgment capabilities.

