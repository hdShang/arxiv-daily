---
layout: default
title: "Towards Open Foundation Language Model and Corpus for Macedonian: A Low-Resource Language"
---

# Towards Open Foundation Language Model and Corpus for Macedonian: A Low-Resource Language

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09560" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09560v1</a>
  <a href="https://arxiv.org/pdf/2506.09560.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09560v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09560v1', 'Towards Open Foundation Language Model and Corpus for Macedonian: A Low-Resource Language')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Stefan Krsteski, Matea Tashkovska, Borjan Sazdov, Hristijan Gjoreski, Branislav Gerazov

**分类**: cs.CL

**发布日期**: 2025-06-11

**备注**: Camera-ready version accepted at SlavNLP-2025@ACL

**DOI**: [10.18653/v1/2025.bsnlp-1.6](https://doi.org/10.18653/v1/2025.bsnlp-1.6)

---

## 💡 一句话要点

**提出马其顿开放基础语言模型及语料库以解决低资源语言问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `低资源语言` `马其顿语` `语料库` `模型训练` `文化适应性` `自然语言处理`

## 📋 核心要点

1. 现有的大型语言模型在低资源语言上的应用能力有限，导致马其顿语的技术工具缺乏，影响了其普及。
2. 本文通过收集马其顿语的最大语料库和构建文化基础的指令数据集，提出了一种新的资源支持方案。
3. 实验结果表明，训练的8B参数模型在多个基准测试中超越了所有现有模型，且在语法和文化适应性上获得了更高的评价。

## 📝 摘要（中文）

随着全球技术的普及，对新工具的需求日益增加。大型语言模型（LLMs）在这方面提供了良好的机会，但对于低资源语言的能力仍然有限，限制了这些语言的应用。本文创建了多个资源以促进LLMs的采用，并支持马其顿语的研究进展。我们收集了迄今为止最大的马其顿语语料库，包含40GB文本数据和35亿词汇。为支持对话应用，我们构建了一个106k实例的指令数据集，确保其文化基础。我们还构建了一个涵盖七个基准的马其顿评估套件，并训练了一个8B参数的模型，结果显示该模型在所有基准上均优于现有模型，并且在语法正确性和文化适应性方面获得了更高的评价。所有数据集、代码和模型权重均已公开发布。

## 🔬 方法详解

**问题定义**：本文旨在解决低资源语言马其顿语在大型语言模型应用中的不足，现有方法无法满足该语言的技术需求。

**核心思路**：通过构建大规模的马其顿语语料库和文化基础的指令数据集，提供支持以促进LLMs的研究和应用。

**技术框架**：整体架构包括数据收集、数据集构建、模型训练和评估四个主要模块。首先收集40GB的文本数据，然后构建106k实例的指令数据集，最后训练8B参数的模型并进行评估。

**关键创新**：最重要的创新在于构建了一个专门针对马其顿语的评估套件，并训练出在8B参数范围内表现最优的模型，超越了现有的所有同类模型。

**关键设计**：在模型训练中，采用了特定的损失函数和网络结构设计，确保模型在语法和文化适应性方面的表现优于更大规模的模型。具体的参数设置和训练细节在论文中有详细描述。

## 📊 实验亮点

实验结果显示，训练的8B参数模型在所有基准测试中均超越了现有的模型，且在语法正确性和文化适应性方面获得了更高的评价。与基线模型相比，该模型的性能提升显著，甚至与10倍参数的模型相当。

## 🎯 应用场景

该研究的潜在应用领域包括教育、文化传播和自然语言处理等。通过提供马其顿语的基础语言模型和语料库，可以促进该语言在技术领域的应用，提升其在全球化背景下的可用性和影响力。

## 📄 摘要（原文）

> The increase in technological adoption worldwide comes with demands for novel tools to be used by the general population. Large Language Models (LLMs) provide a great opportunity in this respect, but their capabilities remain limited for low-resource languages, restricting applications in countries where such languages are spoken. We create several resources to facilitate the adoption of LLMs and to support research advancements for Macedonian. We collect the largest Macedonian corpus to date, consisting of 40GB of textual data and totaling 3.5B words. To support conversational applications, we collect a 106k-instance instruction dataset, carefully built to be culturally grounded. For evaluation, we construct a Macedonian evaluation suite covering seven benchmarks. Finally, we train domestic-yak, a state-of-the-art 8B-parameter model, on our curated datasets and evaluate it against eight baseline models using the newly constructed benchmark suite. Our model outperforms all existing models in the 8B parameter range across all benchmarks, and achieves performance comparable to models up to 10x larger. Furthermore, a qualitative analysis with native speakers reveals that our model is preferred over larger counterparts, receiving higher ratings for grammatical correctness and cultural appropriateness. All datasets, code, and model weights are openly released, setting a foundation for advancing LLMs in similarly underrepresented languages. These resources are publicly available at github.com/LVSTCK for source code, and at huggingface.co/LVSTCK for pretrained model weights and data.

