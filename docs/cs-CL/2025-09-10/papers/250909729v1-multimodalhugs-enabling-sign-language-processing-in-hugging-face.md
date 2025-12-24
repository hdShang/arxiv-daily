---
layout: default
title: "MultimodalHugs: Enabling Sign Language Processing in Hugging Face"
---

# MultimodalHugs: Enabling Sign Language Processing in Hugging Face

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09729" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09729v1</a>
  <a href="https://arxiv.org/pdf/2509.09729.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09729v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09729v1', 'MultimodalHugs: Enabling Sign Language Processing in Hugging Face')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gerard Sant, Zifan Jiang, Carlos Escolano, Amit Moryossef, Mathias Müller, Rico Sennrich, Sarah Ebling

**分类**: cs.CL, cs.AI, cs.MM

**发布日期**: 2025-09-10

---

## 💡 一句话要点

**MultimodalHugs：在Hugging Face中实现手语处理的框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `手语处理` `多模态学习` `Hugging Face` `自然语言处理` `姿势估计`

## 📋 核心要点

1. 手语处理研究受限于复杂且不规范的代码，导致实验重现性差，公平比较困难。
2. MultimodalHugs构建于Hugging Face之上，旨在支持更多样的数据模态和任务，并继承Hugging Face的优势。
3. 实验表明，MultimodalHugs可以处理手语姿势估计数据和文本字符像素数据等多种模态。

## 📝 摘要（中文）

近年来，手语处理(SLP)在自然语言处理领域的重要性日益增加。然而，与口语研究相比，SLP研究受到复杂且临时的代码阻碍，导致重现性低和不公平的比较。现有的为快速和可重复实验而构建的工具，如Hugging Face，不够灵活，无法无缝集成手语实验。我们对SLP研究人员进行的一项调查证实了这一观点。为了应对这些挑战，我们推出了MultimodalHugs，这是一个构建在Hugging Face之上的框架，它支持更多样化的数据模态和任务，同时继承了Hugging Face生态系统的优势。即使手语是我们的主要关注点，MultimodalHugs增加了一个抽象层，使其更广泛地适用于不符合Hugging Face标准模板的其他用例。我们提供了定量实验，以说明MultimodalHugs如何适应不同的模态，例如手语的姿势估计数据或文本字符的像素数据。

## 🔬 方法详解

**问题定义**：手语处理(SLP)领域缺乏一个统一、易于使用且可扩展的框架，导致研究人员需要编写大量的定制代码，降低了实验的可重复性和公平性。现有的工具，如Hugging Face，虽然在自然语言处理领域非常流行，但对手语等非标准模态的支持不足，无法直接应用于SLP任务。

**核心思路**：MultimodalHugs的核心思路是在Hugging Face的基础上构建一个抽象层，使其能够处理更多样化的数据模态和任务。通过引入新的数据表示和处理方式，MultimodalHugs扩展了Hugging Face的功能，使其能够更好地支持手语处理等任务。这种设计允许研究人员利用Hugging Face的现有工具和资源，同时又能够灵活地处理手语数据的特殊性。

**技术框架**：MultimodalHugs的整体架构包括以下几个主要模块：数据加载模块，负责加载和预处理各种手语数据，如视频、姿势估计数据等；模型构建模块，允许研究人员构建和训练各种手语处理模型，包括基于深度学习的模型；评估模块，用于评估模型的性能，并提供各种评估指标；以及集成模块，将MultimodalHugs与Hugging Face生态系统集成，方便研究人员使用Hugging Face的各种工具和资源。

**关键创新**：MultimodalHugs最重要的技术创新点在于其对多模态数据的支持。它通过引入新的数据表示和处理方式，使得Hugging Face能够处理手语等非标准模态的数据。此外，MultimodalHugs还提供了一套统一的API，方便研究人员构建和训练各种手语处理模型。与现有方法相比，MultimodalHugs更加灵活、易于使用且可扩展。

**关键设计**：MultimodalHugs的关键设计包括：使用统一的数据格式来表示各种手语数据；提供一套灵活的API，方便研究人员构建和训练各种手语处理模型；以及与Hugging Face生态系统的紧密集成。具体的参数设置、损失函数和网络结构取决于具体的SLP任务和模型选择，MultimodalHugs旨在提供一个灵活的平台，允许研究人员根据自己的需求进行定制。

## 📊 实验亮点

论文通过实验证明了MultimodalHugs能够有效地处理手语的姿势估计数据和文本字符的像素数据。虽然论文中没有给出具体的性能数据和提升幅度，但它展示了MultimodalHugs在处理多模态数据方面的潜力，并为手语处理领域的研究人员提供了一个有用的工具。

## 🎯 应用场景

MultimodalHugs可应用于手语翻译、手语识别、手语生成等多个领域。它能够帮助听力障碍人士更好地与社会交流，提高他们的生活质量。此外，该框架还可以促进手语处理领域的研究，加速相关技术的进步，并为其他多模态任务提供借鉴。

## 📄 摘要（原文）

> In recent years, sign language processing (SLP) has gained importance in the general field of Natural Language Processing. However, compared to research on spoken languages, SLP research is hindered by complex ad-hoc code, inadvertently leading to low reproducibility and unfair comparisons. Existing tools that are built for fast and reproducible experimentation, such as Hugging Face, are not flexible enough to seamlessly integrate sign language experiments. This view is confirmed by a survey we conducted among SLP researchers.
>   To address these challenges, we introduce MultimodalHugs, a framework built on top of Hugging Face that enables more diverse data modalities and tasks, while inheriting the well-known advantages of the Hugging Face ecosystem. Even though sign languages are our primary focus, MultimodalHugs adds a layer of abstraction that makes it more widely applicable to other use cases that do not fit one of the standard templates of Hugging Face. We provide quantitative experiments to illustrate how MultimodalHugs can accommodate diverse modalities such as pose estimation data for sign languages, or pixel data for text characters.

