---
layout: default
title: "PersianMedQA: Evaluating Large Language Models on a Persian-English Bilingual Medical Question Answering Benchmark"
---

# PersianMedQA: Evaluating Large Language Models on a Persian-English Bilingual Medical Question Answering Benchmark

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00250" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00250v3</a>
  <a href="https://arxiv.org/pdf/2506.00250.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00250v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00250v3', 'PersianMedQA: Evaluating Large Language Models on a Persian-English Bilingual Medical Question Answering Benchmark')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mohammad Javad Ranjbar Kalahroodi, Amirhossein Sheikholselami, Sepehr Karimi, Sepideh Ranjbar Kalahroodi, Heshaam Faili, Azadeh Shakery

**分类**: cs.CL, cs.IT

**发布日期**: 2025-05-30 (更新: 2025-08-10)

**🔗 代码/项目**: [HUGGINGFACE](https://huggingface.co/datasets/MohammadJRanjbar)

---

## 💡 一句话要点

**提出PersianMedQA以评估双语医疗问答中的大型语言模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `医学问答` `波斯语` `双语评估` `数据集构建` `文化背景` `模型评估`

## 📋 核心要点

1. 现有大型语言模型在医学领域的应用仍存在可靠性不足的问题，尤其是在低资源语言的环境中。
2. 本文提出了PersianMedQA数据集，包含波斯语医学问题，旨在评估LLMs在双语环境下的表现。
3. 实验结果表明，闭源通用模型在波斯语和英语中的准确率显著高于波斯语微调模型，翻译影响也被深入分析。

## 📝 摘要（中文）

大型语言模型（LLMs）在自然语言处理（NLP）基准测试中表现出色，但在高风险领域如医学，尤其是低资源语言的可靠性仍未得到充分探讨。本文介绍了PersianMedQA，一个包含20,785个经过专家验证的波斯语医学多项选择题的数据集，旨在评估LLMs在波斯语和英语中的表现。我们对40个最先进的模型进行了基准测试，结果显示闭源通用模型（如GPT-4.1）在波斯语和英语中均表现优异，而波斯语微调模型表现不佳。我们还分析了翻译的影响，发现某些问题在波斯语中才能正确回答。PersianMedQA为评估双语和文化背景下的医学推理提供了基础。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在医学领域，尤其是在波斯语环境中的可靠性不足问题。现有方法在低资源语言的应用效果不理想，缺乏针对性的评估基准。

**核心思路**：通过构建PersianMedQA数据集，包含经过专家验证的波斯语医学问题，提供一个双语评估平台，以便更好地评估和比较不同模型的表现。

**技术框架**：整体架构包括数据集构建、模型选择与评估。数据集涵盖14年伊朗国家医学考试的多项选择题，模型评估则包括零-shot和链式思维（CoT）设置。

**关键创新**：PersianMedQA数据集的构建是本文的核心创新，填补了低资源语言医学问答评估的空白，并提供了文化背景下的医学推理能力评估。

**关键设计**：在实验中，采用了40个最先进的模型进行评估，特别关注了模型的语言适应性和领域适应性，发现模型大小并不足以保证性能，需结合强大的领域知识。

## 📊 实验亮点

实验结果显示，闭源通用模型（如GPT-4.1）在波斯语中达到了83.09%的准确率，在英语中为80.7%。相比之下，波斯语微调模型如Dorna的表现显著低下，仅为34.9%。此外，翻译分析表明，3-10%的问题在波斯语中才能正确回答，强调了文化和临床背景的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括医学教育、临床决策支持和医疗信息检索等。通过提供一个双语评估平台，PersianMedQA能够帮助开发更可靠的医疗问答系统，促进低资源语言的医学信息获取，提升医疗服务的可及性和准确性。

## 📄 摘要（原文）

> Large Language Models (LLMs) have achieved remarkable performance on a wide range of Natural Language Processing (NLP) benchmarks, often surpassing human-level accuracy. However, their reliability in high-stakes domains such as medicine, particularly in low-resource languages, remains underexplored. In this work, we introduce PersianMedQA, a large-scale dataset of 20,785 expert-validated multiple-choice Persian medical questions from 14 years of Iranian national medical exams, spanning 23 medical specialties and designed to evaluate LLMs in both Persian and English. We benchmark 40 state-of-the-art models, including general-purpose, Persian fine-tuned, and medical LLMs, in zero-shot and chain-of-thought (CoT) settings. Our results show that closed-source general models (e.g., GPT-4.1) consistently outperform all other categories, achieving 83.09% accuracy in Persian and 80.7% in English, while Persian fine-tuned models such as Dorna underperform significantly (e.g., 34.9% in Persian), often struggling with both instruction-following and domain reasoning. We also analyze the impact of translation, showing that while English performance is generally higher, 3-10% of questions can only be answered correctly in Persian due to cultural and clinical contextual cues that are lost in translation. Finally, we demonstrate that model size alone is insufficient for robust performance without strong domain or language adaptation. PersianMedQA provides a foundation for evaluating bilingual and culturally grounded medical reasoning in LLMs. The PersianMedQA dataset is available: https://huggingface.co/datasets/MohammadJRanjbar/PersianMedQA .

