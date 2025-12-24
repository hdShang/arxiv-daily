---
layout: default
title: Assessing the Chemical Intelligence of Large Language Models
---

# Assessing the Chemical Intelligence of Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07735" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07735v2</a>
  <a href="https://arxiv.org/pdf/2505.07735.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07735v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07735v2', 'Assessing the Chemical Intelligence of Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nicholas T. Runcie, Charlotte M. Deane, Fergus Imrie

**分类**: cs.LG

**发布日期**: 2025-05-12 (更新: 2025-07-10)

---

## 💡 一句话要点

**提出ChemIQ基准以评估大型语言模型的化学智能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `化学智能` `推理模型` `ChemIQ基准` `有机化学` `结构解析` `SMILES转化` `NMR数据`

## 📋 核心要点

1. 现有的化学任务评估方法主要依赖选择题，无法真实反映模型的推理能力和实际应用。
2. 本文提出ChemIQ基准，要求模型生成简答题回答，评估其在有机化学中的推理能力。
3. 实验结果显示，推理模型的正确率显著高于非推理模型，且能够完成复杂的化学任务，如SMILES字符串转化和NMR数据解析。

## 📝 摘要（中文）

大型语言模型（LLMs）是一种多功能工具，广泛应用于各个领域。近期，推理模型的出现显著提升了它们在数学和软件工程等高级问题解决领域的能力。本文评估了推理模型在化学任务中的表现，提出了一个名为ChemIQ的新基准，包含816个问题，重点考察有机化学的核心概念。与以往主要使用选择题的基准不同，我们的方法要求模型构建简答题回答，更贴近实际应用。推理模型在最高推理模式下的正确率为50%-57%，显著优于非推理模型的3%-7%。我们的研究表明，最新的推理模型在某些情况下能够进行高级化学推理。

## 🔬 方法详解

**问题定义**：本文旨在评估大型语言模型在化学任务中的推理能力，现有方法主要依赖选择题，无法真实反映模型的推理过程和能力。

**核心思路**：通过构建ChemIQ基准，要求模型生成简答题回答，能够更好地评估其在有机化学中的推理能力，反映真实的化学应用场景。

**技术框架**：整体架构包括数据集构建、模型训练和评估三个主要阶段。数据集包含816个问题，模型通过推理能力进行回答，最后评估其正确率和推理过程。

**关键创新**：最重要的创新在于提出了ChemIQ基准，要求模型生成简答题回答，区别于以往的选择题评估，能够更真实地反映模型的推理能力。

**关键设计**：在模型评估中，采用了不同的推理模式，推理模式的提升显著提高了模型的回答正确率，且模型能够处理复杂的化学结构解析任务。具体参数设置和损失函数未详细披露，需进一步研究。

## 📊 实验亮点

实验结果显示，推理模型在最高推理模式下的正确率达50%-57%，显著高于非推理模型的3%-7%。此外，Gemini Pro 2.5能够正确生成约90%的SMILES字符串，并成功解析包含25个重原子的结构，展示了其在化学推理中的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括化学教育、药物设计和材料科学等。通过提升大型语言模型在化学推理方面的能力，可以为化学研究提供更智能的辅助工具，促进科研效率的提升。未来，随着模型能力的进一步增强，可能会在更多化学相关领域发挥重要作用。

## 📄 摘要（原文）

> Large Language Models are versatile, general-purpose tools with a wide range of applications. Recently, the advent of "reasoning models" has led to substantial improvements in their abilities in advanced problem-solving domains such as mathematics and software engineering. In this work, we assessed the ability of reasoning models to perform chemistry tasks directly, without any assistance from external tools. We created a novel benchmark, called ChemIQ, consisting of 816 questions assessing core concepts in organic chemistry, focused on molecular comprehension and chemical reasoning. Unlike previous benchmarks, which primarily use multiple choice formats, our approach requires models to construct short-answer responses, more closely reflecting real-world applications. The reasoning models, OpenAI's o3-mini, Google's Gemini Pro 2.5, and DeepSeek R1, answered 50%-57% of questions correctly in the highest reasoning modes, with higher reasoning levels significantly increasing performance on all tasks. These models substantially outperformed the non-reasoning models which achieved only 3%-7% accuracy. We found that Large Language Models can now convert SMILES strings to IUPAC names, a task earlier models were unable to perform. Additionally, we show that the latest reasoning models can elucidate structures from 1D and 2D 1H and 13C NMR data, with Gemini Pro 2.5 correctly generating SMILES strings for around 90% of molecules containing up to 10 heavy atoms, and in one case solving a structure comprising 25 heavy atoms. For each task, we found evidence that the reasoning process mirrors that of a human chemist. Our results demonstrate that the latest reasoning models can, in some cases, perform advanced chemical reasoning.

