---
layout: default
title: Ultrasound Report Generation with Multimodal Large Language Models for Standardized Texts
---

# Ultrasound Report Generation with Multimodal Large Language Models for Standardized Texts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08838" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08838v2</a>
  <a href="https://arxiv.org/pdf/2505.08838.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08838v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08838v2', 'Ultrasound Report Generation with Multimodal Large Language Models for Standardized Texts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Peixuan Ge, Tongkun Su, Faqin Lv, Baoliang Zhao, Peng Zhang, Chi Hong Wong, Liang Yao, Yu Sun, Zenan Wang, Pak Kin Wong, Ying Hu

**分类**: eess.IV, cs.AI, cs.CV

**发布日期**: 2025-05-13 (更新: 2025-05-19)

---

## 💡 一句话要点

**提出多模态大语言模型以解决超声报告生成问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `超声报告生成` `多模态大语言模型` `标准化文本` `多语言支持` `视觉变换器` `临床应用` `文本生成`

## 📋 核心要点

1. 超声报告生成面临图像多样性和操作者依赖性等挑战，缺乏一致的数据集使得自动化变得困难。
2. 本研究提出了一个统一框架，结合多语言训练和标准化文本，支持多器官的超声报告生成。
3. 实验结果显示，与KMVE方法相比，本方法在多个指标上均有显著提升，且减少了内容错误。

## 📝 摘要（中文）

超声报告生成是一项具有挑战性的任务，主要由于超声图像的多样性、操作者的依赖性以及对标准化文本的需求。与X光和CT不同，超声成像缺乏一致的数据集，导致自动化困难。本研究提出了一个统一框架，用于多器官和多语言的超声报告生成，整合了基于片段的多语言训练，并利用超声报告的标准化特性。通过将模块化文本片段与多样的成像数据对齐，并策划双语英汉数据集，该方法在不同器官和语言之间实现了一致且临床准确的文本生成。通过选择性解冻视觉变换器（ViT）进行微调，进一步改善了文本与图像的对齐。与之前的最先进KMVE方法相比，我们的方法在BLEU分数上相对提升约2%，在ROUGE-L上约提升3%，在CIDEr上约提升15%，同时显著减少了缺失或错误内容等错误。通过将多器官和多语言报告生成统一为一个可扩展的框架，本研究展示了在实际临床工作流程中的强大潜力。

## 🔬 方法详解

**问题定义**：本论文旨在解决超声报告生成中的多样性和标准化问题。现有方法面临图像变异性大、操作者依赖性强以及缺乏一致数据集的痛点，导致自动化生成困难。

**核心思路**：论文提出的核心思路是通过整合多语言和多器官的训练，利用模块化文本片段与成像数据对齐，从而实现标准化的超声报告生成。

**技术框架**：整体架构包括数据预处理、模块化文本片段生成、图像与文本对齐及多语言支持等主要模块。通过构建双语数据集，增强了模型的泛化能力。

**关键创新**：本研究的主要创新在于将多器官和多语言报告生成统一为一个框架，显著提升了文本生成的准确性和一致性，区别于现有方法的片段化处理。

**关键设计**：在模型设计中，采用选择性解冻的方式对视觉变换器（ViT）进行微调，优化了文本与图像的对齐效果，损失函数设计上注重生成文本的流畅性和准确性。

## 📊 实验亮点

实验结果表明，与KMVE方法相比，本研究在BLEU分数上提升约2%，ROUGE-L提升约3%，CIDEr提升约15%。同时，显著减少了报告生成中的缺失或错误内容，展示了方法的有效性和可靠性。

## 🎯 应用场景

该研究的潜在应用领域包括医疗影像学、临床报告生成及人工智能辅助诊断等。通过实现标准化的超声报告生成，能够提高临床工作流程的效率，减少人为错误，提升医疗服务质量，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Ultrasound (US) report generation is a challenging task due to the variability of US images, operator dependence, and the need for standardized text. Unlike X-ray and CT, US imaging lacks consistent datasets, making automation difficult. In this study, we propose a unified framework for multi-organ and multilingual US report generation, integrating fragment-based multilingual training and leveraging the standardized nature of US reports. By aligning modular text fragments with diverse imaging data and curating a bilingual English-Chinese dataset, the method achieves consistent and clinically accurate text generation across organ sites and languages. Fine-tuning with selective unfreezing of the vision transformer (ViT) further improves text-image alignment. Compared to the previous state-of-the-art KMVE method, our approach achieves relative gains of about 2\% in BLEU scores, approximately 3\% in ROUGE-L, and about 15\% in CIDEr, while significantly reducing errors such as missing or incorrect content. By unifying multi-organ and multi-language report generation into a single, scalable framework, this work demonstrates strong potential for real-world clinical workflows.

