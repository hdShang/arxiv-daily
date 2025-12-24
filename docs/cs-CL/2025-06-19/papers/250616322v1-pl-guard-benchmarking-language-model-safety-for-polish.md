---
layout: default
title: "PL-Guard: Benchmarking Language Model Safety for Polish"
---

# PL-Guard: Benchmarking Language Model Safety for Polish

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16322" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16322v1</a>
  <a href="https://arxiv.org/pdf/2506.16322.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16322v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16322v1', 'PL-Guard: Benchmarking Language Model Safety for Polish')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aleksandra Krasnodębska, Karolina Seweryn, Szymon Łukasik, Wojciech Kusa

**分类**: cs.CL

**发布日期**: 2025-06-19

**备注**: Accepted to the 10th Workshop on Slavic Natural Language Processing

---

## 💡 一句话要点

**提出PL-Guard以解决波兰语语言模型安全性评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语言模型` `安全性评估` `波兰语` `对抗样本` `机器学习` `数据集构建` `模型微调`

## 📋 核心要点

1. 现有的语言模型安全性评估工具主要集中在高资源语言，导致波兰语等语言的安全性研究不足。
2. 本文提出了一个手动注释的波兰语安全分类基准数据集，并创建了对抗扰动样本以测试模型的鲁棒性。
3. 实验结果显示，基于HerBERT的分类器在多种条件下表现优异，尤其是在对抗性测试中取得了最佳性能。

## 📝 摘要（中文）

尽管在确保大型语言模型（LLMs）安全性方面的努力不断增加，但现有的安全评估和审查工具仍然主要集中在英语和其他高资源语言上，导致大多数全球语言未得到充分研究。为了解决这一问题，本文引入了一个手动注释的波兰语语言模型安全分类基准数据集，并创建了针对这些样本的对抗扰动变体，以挑战模型的鲁棒性。我们进行了系列实验，评估了不同规模和架构的LLM和分类器模型，结果表明，基于HerBERT的分类器在对抗条件下表现最佳。

## 🔬 方法详解

**问题定义**：本文旨在解决波兰语语言模型安全性评估不足的问题。现有方法在多语言环境中存在偏见，缺乏对波兰语的深入研究。

**核心思路**：通过构建一个手动注释的波兰语安全分类基准数据集，并生成对抗扰动样本，来评估和提高语言模型的安全性和鲁棒性。

**技术框架**：研究包括数据集构建、模型训练和性能评估三个主要阶段。首先，手动标注数据集，然后对不同模型进行微调，最后通过实验评估模型性能。

**关键创新**：最重要的创新在于引入了针对波兰语的安全性基准数据集和对抗样本，这在现有文献中尚属首次，填补了多语言安全性评估的空白。

**关键设计**：研究中使用了Llama-Guard-3-8B、基于HerBERT的分类器和PLLum等模型，采用不同组合的注释数据进行训练，评估时与公开的防护模型进行对比。

## 📊 实验亮点

实验结果显示，基于HerBERT的分类器在多种对抗条件下表现最佳，整体性能超过其他模型，尤其在对抗样本测试中表现出色，展示了显著的鲁棒性提升。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体内容审查、在线平台的用户生成内容监控以及任何需要确保语言模型输出安全性的场景。通过提升波兰语模型的安全性，能够更好地服务于波兰语用户，减少有害内容的传播。

## 📄 摘要（原文）

> Despite increasing efforts to ensure the safety of large language models (LLMs), most existing safety assessments and moderation tools remain heavily biased toward English and other high-resource languages, leaving majority of global languages underexamined. To address this gap, we introduce a manually annotated benchmark dataset for language model safety classification in Polish. We also create adversarially perturbed variants of these samples designed to challenge model robustness. We conduct a series of experiments to evaluate LLM-based and classifier-based models of varying sizes and architectures. Specifically, we fine-tune three models: Llama-Guard-3-8B, a HerBERT-based classifier (a Polish BERT derivative), and PLLuM, a Polish-adapted Llama-8B model. We train these models using different combinations of annotated data and evaluate their performance, comparing it against publicly available guard models. Results demonstrate that the HerBERT-based classifier achieves the highest overall performance, particularly under adversarial conditions.

