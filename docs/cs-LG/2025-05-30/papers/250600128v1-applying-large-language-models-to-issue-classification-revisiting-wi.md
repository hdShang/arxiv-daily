---
layout: default
title: Applying Large Language Models to Issue Classification: Revisiting with Extended Data and New Models
---

# Applying Large Language Models to Issue Classification: Revisiting with Extended Data and New Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00128" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00128v1</a>
  <a href="https://arxiv.org/pdf/2506.00128.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00128v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00128v1', 'Applying Large Language Models to Issue Classification: Revisiting with Extended Data and New Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gabriel Aracena, Kyle Luster, Fabio Santos, Igor Steinmacher, Marco A. Gerosa

**分类**: cs.SE, cs.LG

**发布日期**: 2025-05-30

**备注**: 35 pages, 2 figures, 9 tables, Pre-print for Science of Computer Programming

---

## 💡 一句话要点

**提出基于大语言模型的自动化问题分类方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `缺陷分类` `自动化流程` `软件工程` `机器学习`

## 📋 核心要点

1. 现有的手动缺陷分类方法费时且难以扩展，自动化流程往往依赖于大规模数据集进行训练。
2. 本文提出了一种基于大语言模型的缺陷分类方法，旨在减少对大量训练数据的需求，同时保持分类的准确性。
3. 实验结果表明，GPT-4o模型在缺陷分类中表现优异，F1得分达80.7%，显著高于DeepSeek R1的59.33%。

## 📝 摘要（中文）

有效的缺陷报告优先级划分在软件工程中有助于优化资源分配和信息恢复。然而，手动分类缺陷既费时又缺乏可扩展性。许多开源软件项目采用自动化流程进行分类，但通常依赖于大量数据集进行训练。本文研究了一种基于大语言模型（LLMs）的自动化缺陷分类方法，旨在减少对大规模训练数据的依赖，同时保持分类的可靠性。研究中，我们选择了两种主要的大语言模型进行比较，结果显示GPT-4o在NLBSE 2024竞赛中的缺陷分类表现最佳，其F1得分比DeepSeek R1高出20%。

## 🔬 方法详解

**问题定义**：本文旨在解决软件工程中缺陷报告分类的效率低下和可扩展性不足的问题。现有的手动分类方法耗时且难以适应大规模项目的需求。

**核心思路**：通过利用大语言模型的强大能力，开发一种自动化的缺陷分类系统，减少对大规模训练数据的依赖，同时确保分类的可靠性。

**技术框架**：研究中采用了两种主要的大语言模型进行比较，构建了一个包含数据预处理、模型训练和评估的整体框架。

**关键创新**：最重要的创新在于使用大语言模型进行缺陷分类，显著提高了分类准确性，并减少了对大量数据集的需求。与传统方法相比，这种方法在准确性和效率上都有所提升。

**关键设计**：在模型训练中，采用了针对特定任务的微调策略，选择了合适的损失函数和超参数设置，以优化模型性能。

## 📊 实验亮点

实验结果显示，GPT-4o模型在NLBSE 2024竞赛中的缺陷分类任务中取得了80.7%的F1得分，显著高于DeepSeek R1的59.33%。此外，增加数据集规模并未提升F1得分，表明该方法在数据需求上的优势。

## 🎯 应用场景

该研究的潜在应用领域包括开源软件项目的缺陷管理、软件开发生命周期中的问题追踪和优先级划分。通过自动化缺陷分类，开发团队可以更高效地分配资源，提升软件质量和开发效率。未来，该方法有望推广到其他领域的文本分类任务中。

## 📄 摘要（原文）

> Effective prioritization of issue reports in software engineering helps to optimize resource allocation and information recovery. However, manual issue classification is laborious and lacks scalability. As an alternative, many open source software (OSS) projects employ automated processes for this task, yet this method often relies on large datasets for adequate training. Traditionally, machine learning techniques have been used for issue classification. More recently, large language models (LLMs) have emerged as powerful tools for addressing a range of software engineering challenges, including code and test generation, mapping new requirements to legacy software endpoints, and conducting code reviews. The following research investigates an automated approach to issue classification based on LLMs. By leveraging the capabilities of such models, we aim to develop a robust system for prioritizing issue reports, mitigating the necessity for extensive training data while also maintaining reliability in classification. In our research, we developed an LLM-based approach for accurately labeling issues by selecting two of the most prominent large language models. We then compared their performance across multiple datasets. Our findings show that GPT-4o achieved the best results in classifying issues from the NLBSE 2024 competition. Moreover, GPT-4o outperformed DeepSeek R1, achieving an F1 score 20% higher when both models were trained on the same dataset from the NLBSE 2023 competition, which was ten times larger than the NLBSE 2024 dataset. The fine-tuned GPT-4o model attained an average F1 score of 80.7%, while the fine-tuned DeepSeek R1 model achieved 59.33%. Increasing the dataset size did not improve the F1 score, reducing the dependence on massive datasets for building an efficient solution to issue classification.

