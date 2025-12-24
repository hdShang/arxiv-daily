---
layout: default
title: Memorization or Interpolation ? Detecting LLM Memorization through Input Perturbation Analysis
---

# Memorization or Interpolation ? Detecting LLM Memorization through Input Perturbation Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03019" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03019v1</a>
  <a href="https://arxiv.org/pdf/2505.03019.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03019v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03019v1', 'Memorization or Interpolation ? Detecting LLM Memorization through Input Perturbation Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Albérick Euraste Djiré, Abdoul Kader Kaboré, Earl T. Barr, Jacques Klein, Tegawendé F. Bissyandé

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-05

---

## 💡 一句话要点

**提出PEARL以检测大型语言模型的记忆现象**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `记忆检测` `输入扰动` `模型评估` `数据隐私` `知识产权` `泛化能力`

## 📋 核心要点

1. 现有方法难以有效区分大型语言模型的记忆与泛化，导致对模型评估的可靠性产生疑虑。
2. PEARL通过输入扰动分析来检测记忆现象，评估模型对输入变化的敏感性，从而实现无需内部访问的检测。
3. 在Pythia模型上的实验结果表明，PEARL能够有效识别模型的记忆行为，并在GPT 4o模型中验证了其有效性。

## 📝 摘要（中文）

大型语言模型（LLMs）在处理大规模数据集时表现出色，但也可能出现逐字复述训练数据而非真正泛化的现象。这种记忆现象引发了关于数据隐私、知识产权和模型评估可靠性的重大担忧。本文提出了一种新方法PEARL，通过分析输入扰动来检测LLMs的记忆现象。PEARL评估LLM性能对输入扰动的敏感性，从而在不需要访问模型内部的情况下实现记忆检测。通过对Pythia开放模型的广泛实验，我们的发现为识别模型简单重复学习信息提供了稳健的框架。PEARL在GPT 4o模型上的应用不仅识别了经典文本和常见代码的记忆案例，还提供了证据表明某些数据（如《纽约时报》的新闻文章）可能是模型训练数据的一部分。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在训练数据上逐字复述而非真正泛化的问题。现有方法在识别记忆现象时存在局限，无法有效评估模型的真实表现。

**核心思路**：PEARL的核心思路是通过分析输入扰动对模型输出的一致性影响，来检测模型是否存在记忆现象。这种方法不依赖于模型的内部结构，具有较高的实用性。

**技术框架**：PEARL的整体架构包括输入扰动生成、模型输出评估和记忆检测三个主要模块。首先，通过对输入进行扰动生成多样化的测试样本；然后，评估模型在这些样本上的输出一致性；最后，基于一致性分析判断模型是否存在记忆现象。

**关键创新**：PEARL的最大创新在于其无需访问模型内部即可检测记忆现象，利用输入扰动的敏感性作为判断依据。这一方法与传统依赖模型内部机制的检测方法本质上不同。

**关键设计**：在PEARL中，输入扰动的类型和强度是关键设计参数，影响模型输出的一致性评估。此外，采用特定的损失函数来量化输出一致性，从而有效识别记忆行为。实验中还对不同类型的输入扰动进行了比较，以优化检测效果。

## 📊 实验亮点

在Pythia模型的实验中，PEARL成功识别了多种记忆案例，包括经典文本和常见代码的逐字复述。此外，在GPT 4o模型的应用中，PEARL提供了证据，表明某些数据如《纽约时报》的文章可能是模型训练数据的一部分，显示出其强大的检测能力。

## 🎯 应用场景

PEARL方法在大型语言模型的开发和评估中具有广泛的应用潜力，尤其是在需要确保数据隐私和知识产权的场景中。通过有效检测模型的记忆现象，研究人员和开发者可以更好地理解模型的行为，提升模型的可靠性和透明度，进而推动AI技术的健康发展。

## 📄 摘要（原文）

> While Large Language Models (LLMs) achieve remarkable performance through training on massive datasets, they can exhibit concerning behaviors such as verbatim reproduction of training data rather than true generalization. This memorization phenomenon raises significant concerns about data privacy, intellectual property rights, and the reliability of model evaluations. This paper introduces PEARL, a novel approach for detecting memorization in LLMs. PEARL assesses how sensitive an LLM's performance is to input perturbations, enabling memorization detection without requiring access to the model's internals. We investigate how input perturbations affect the consistency of outputs, enabling us to distinguish between true generalization and memorization. Our findings, following extensive experiments on the Pythia open model, provide a robust framework for identifying when the model simply regurgitates learned information. Applied on the GPT 4o models, the PEARL framework not only identified cases of memorization of classic texts from the Bible or common code from HumanEval but also demonstrated that it can provide supporting evidence that some data, such as from the New York Times news articles, were likely part of the training data of a given model.

