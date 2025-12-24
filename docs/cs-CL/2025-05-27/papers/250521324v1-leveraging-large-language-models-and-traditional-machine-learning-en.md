---
layout: default
title: Leveraging large language models and traditional machine learning ensembles for ADHD detection from narrative transcripts
---

# Leveraging large language models and traditional machine learning ensembles for ADHD detection from narrative transcripts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21324" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21324v1</a>
  <a href="https://arxiv.org/pdf/2505.21324.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21324v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21324v1', 'Leveraging large language models and traditional machine learning ensembles for ADHD detection from narrative transcripts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuxin Zhu, Yuting Guo, Noah Marchuck, Abeed Sarker, Yun Wang

**分类**: cs.CL

**发布日期**: 2025-05-27

---

## 💡 一句话要点

**提出基于大语言模型与传统机器学习集成的ADHD检测方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `机器学习` `ADHD检测` `文本分类` `集成学习` `临床应用` `自然语言处理`

## 📋 核心要点

1. 现有方法在精神病学文本分类中对复杂叙述数据的处理能力不足，难以有效识别ADHD相关的语言线索。
2. 本研究提出了一种集成框架，结合大语言模型和传统机器学习模型，通过多数投票机制提升分类准确性。
3. 实验结果显示，集成模型在召回率上优于最佳单一模型（SVM），同时保持了竞争力的精确度，F1分数达到0.71。

## 📝 摘要（中文）

尽管大语言模型（LLMs）迅速发展，但其与传统监督机器学习技术的结合在医学数据中的应用仍未得到充分探索。尤其在精神病学领域，叙述数据常常展现出细腻的语言和上下文复杂性，能够从多模型的结合中受益。本研究提出了一种集成框架，通过整合LLaMA3、RoBERTa和支持向量机（SVM）分类器，自动分类注意力缺陷/多动障碍（ADHD）诊断。实验结果表明，该集成模型在F1分数上达到了0.71，超越了单一模型，展示了混合架构在精神病学文本分类中的潜力。

## 🔬 方法详解

**问题定义**：本研究旨在解决注意力缺陷/多动障碍（ADHD）诊断中的文本分类问题。现有方法在处理复杂的叙述数据时，往往无法充分捕捉语言的细微差别和上下文信息，导致分类效果不佳。

**核心思路**：本研究的核心思路是通过集成多种模型，结合大语言模型的语义理解能力与传统机器学习模型的可解释性，提升ADHD诊断的分类性能。通过这种方式，可以更好地识别与ADHD相关的语言特征。

**技术框架**：整体架构包括三个主要模块：LLaMA3模型用于捕捉长距离语义结构，RoBERTa模型经过临床叙述的微调，SVM分类器则基于TF-IDF特征进行训练。最终通过多数投票机制将各模型的预测结果进行整合。

**关键创新**：本研究的关键创新在于将大语言模型与传统机器学习模型相结合，形成一个混合架构。这种方法不仅提升了模型的预测能力，还增强了对ADHD相关语言线索的敏感性，区别于以往单一模型的应用。

**关键设计**：在模型设计中，LLaMA3和RoBERTa的选择基于其在语言理解上的优势，而SVM则利用TF-IDF特征进行有效的文本表示。集成模型的训练过程中，采用了多数投票机制以提高预测的鲁棒性。

## 📊 实验亮点

实验结果显示，集成模型在F1分数上达到了0.71，相较于最佳单一模型（SVM）在召回率上有显著提升，同时保持了竞争力的精确度。这表明集成方法在识别ADHD相关语言特征方面具有更强的敏感性。

## 🎯 应用场景

该研究的潜在应用领域包括精神健康评估、临床诊断支持系统以及教育领域的个性化学习方案。通过提高ADHD的检测准确性，可以帮助医生更好地识别和干预相关患者，进而改善患者的生活质量。未来，该方法有望推广至其他精神疾病的文本分类任务中。

## 📄 摘要（原文）

> Despite rapid advances in large language models (LLMs), their integration with traditional supervised machine learning (ML) techniques that have proven applicability to medical data remains underexplored. This is particularly true for psychiatric applications, where narrative data often exhibit nuanced linguistic and contextual complexity, and can benefit from the combination of multiple models with differing characteristics. In this study, we introduce an ensemble framework for automatically classifying Attention-Deficit/Hyperactivity Disorder (ADHD) diagnosis (binary) using narrative transcripts. Our approach integrates three complementary models: LLaMA3, an open-source LLM that captures long-range semantic structure; RoBERTa, a pre-trained transformer model fine-tuned on labeled clinical narratives; and a Support Vector Machine (SVM) classifier trained using TF-IDF-based lexical features. These models are aggregated through a majority voting mechanism to enhance predictive robustness. The dataset includes 441 instances, including 352 for training and 89 for validation. Empirical results show that the ensemble outperforms individual models, achieving an F$_1$ score of 0.71 (95\% CI: [0.60-0.80]). Compared to the best-performing individual model (SVM), the ensemble improved recall while maintaining competitive precision. This indicates the strong sensitivity of the ensemble in identifying ADHD-related linguistic cues. These findings demonstrate the promise of hybrid architectures that leverage the semantic richness of LLMs alongside the interpretability and pattern recognition capabilities of traditional supervised ML, offering a new direction for robust and generalizable psychiatric text classification.

