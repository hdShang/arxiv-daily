---
layout: default
title: "LLM-OREF: An Open Relation Extraction Framework Based on Large Language Models"
---

# LLM-OREF: An Open Relation Extraction Framework Based on Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15089" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15089v1</a>
  <a href="https://arxiv.org/pdf/2509.15089.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15089v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15089v1', 'LLM-OREF: An Open Relation Extraction Framework Based on Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongyao Tu, Liang Zhang, Yujie Lin, Xin Lin, Haibo Zhang, Long Zhang, Jinsong Su

**分类**: cs.CL

**发布日期**: 2025-09-18

**🔗 代码/项目**: [GITHUB](https://github.com/XMUDeepLIT/LLM-OREF.git)

---

## 💡 一句话要点

**提出基于大语言模型的开放关系抽取框架LLM-OREF，无需人工干预即可预测新关系。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `开放关系抽取` `大语言模型` `少样本学习` `自校正推理` `关系发现`

## 📋 核心要点

1. 现有开放关系抽取方法依赖人工标注，限制了其在实际应用中的可行性。
2. LLM-OREF框架利用大语言模型的理解和生成能力，直接预测新关系，无需人工干预。
3. 该框架包含关系发现、关系去噪和关系预测三个阶段，通过自校正推理策略提升预测准确性。

## 📝 摘要（中文）

开放关系抽取(OpenRE)的目标是开发一种能够泛化到训练期间未遇到的新关系的关系抽取模型。现有的研究主要将OpenRE形式化为聚类任务，首先基于实例之间的相似性对所有测试实例进行聚类，然后手动为每个聚类分配一个新的关系。然而，它们对人工标注的依赖限制了它们的实用性。在本文中，我们提出了一个基于大语言模型(LLM)的OpenRE框架，该框架利用LLM强大的语言理解和生成能力，直接预测测试实例的新关系，无需人工干预。具体来说，我们的框架由两个核心组件组成：(1)关系发现器(RD)，旨在基于由具有已知关系的训练实例形成的*演示*来预测测试实例的新关系；(2)关系预测器(RP)，用于在由其自身实例组成的*演示*的指导下，从$n$个候选关系中为测试实例选择最可能的关系。为了增强我们的框架预测新关系的能力，我们设计了一种由关系发现、关系去噪和关系预测三个阶段组成的自校正推理策略。在第一阶段，我们使用RD初步预测所有测试实例的新关系。接下来，我们应用RP通过交叉验证方法从RD的预测结果中为每个新关系选择一些高可靠性的测试实例。在第三阶段，我们基于由这些可靠的测试实例构建的演示，使用RP重新预测所有测试实例的关系。在三个OpenRE数据集上的大量实验证明了我们框架的有效性。

## 🔬 方法详解

**问题定义**：开放关系抽取旨在识别文本中实体之间的关系，并且能够泛化到训练集中未出现过的关系类型。现有方法通常依赖于聚类，然后需要人工标注聚类结果，这限制了其可扩展性和自动化程度。因此，如何自动地发现和预测新的关系类型是该论文要解决的核心问题。

**核心思路**：该论文的核心思路是利用大语言模型（LLM）强大的语言理解和生成能力，直接从文本中推断出新的关系类型，而无需依赖人工标注。通过构建合适的提示（prompt）和利用少样本学习（few-shot learning）的能力，让LLM能够理解文本的语义并生成相应的关系描述。

**技术框架**：LLM-OREF框架包含两个核心组件和一个自校正推理策略。关系发现器（RD）负责基于训练集中已知关系的实例，为测试实例预测新的关系。关系预测器（RP）则用于从多个候选关系中选择最有可能的关系。自校正推理策略包含三个阶段：关系发现（使用RD进行初步预测）、关系去噪（使用RP选择高可靠性实例）和关系预测（基于高可靠性实例重新预测所有实例的关系）。

**关键创新**：该论文的关键创新在于提出了一个完全基于大语言模型的开放关系抽取框架，无需人工干预即可完成新关系的发现和预测。通过自校正推理策略，可以有效地提高预测的准确性和可靠性。与传统方法相比，该方法更加自动化和可扩展。

**关键设计**：框架的关键设计包括：(1) 如何构建有效的提示（prompt）来引导LLM进行关系发现和预测；(2) 如何设计关系去噪策略，以选择高可靠性的实例；(3) 如何利用少样本学习，让LLM能够快速适应新的关系类型。具体的技术细节，例如prompt的具体形式、损失函数等，论文中可能没有详细说明。

## 📊 实验亮点

实验结果表明，LLM-OREF框架在三个开放关系抽取数据集上取得了显著的性能提升。具体的数据和提升幅度在摘要中没有给出，但强调了该框架的有效性。代码已开源，方便研究者复现和进一步研究。

## 🎯 应用场景

该研究成果可应用于知识图谱构建、信息抽取、问答系统等领域。通过自动发现和抽取新的关系，可以丰富知识图谱的内容，提高问答系统的准确性，并为其他自然语言处理任务提供支持。该方法无需人工干预的特性，使其在处理大规模文本数据时具有显著优势。

## 📄 摘要（原文）

> The goal of open relation extraction (OpenRE) is to develop an RE model that can generalize to new relations not encountered during training. Existing studies primarily formulate OpenRE as a clustering task. They first cluster all test instances based on the similarity between the instances, and then manually assign a new relation to each cluster. However, their reliance on human annotation limits their practicality. In this paper, we propose an OpenRE framework based on large language models (LLMs), which directly predicts new relations for test instances by leveraging their strong language understanding and generation abilities, without human intervention. Specifically, our framework consists of two core components: (1) a relation discoverer (RD), designed to predict new relations for test instances based on \textit{demonstrations} formed by training instances with known relations; and (2) a relation predictor (RP), used to select the most likely relation for a test instance from $n$ candidate relations, guided by \textit{demonstrations} composed of their instances. To enhance the ability of our framework to predict new relations, we design a self-correcting inference strategy composed of three stages: relation discovery, relation denoising, and relation prediction. In the first stage, we use RD to preliminarily predict new relations for all test instances. Next, we apply RP to select some high-reliability test instances for each new relation from the prediction results of RD through a cross-validation method. During the third stage, we employ RP to re-predict the relations of all test instances based on the demonstrations constructed from these reliable test instances. Extensive experiments on three OpenRE datasets demonstrate the effectiveness of our framework. We release our code at https://github.com/XMUDeepLIT/LLM-OREF.git.

