---
layout: default
title: "Decoupling Reasoning and Perception: An LLM-LMM Framework for Faithful Visual Reasoning"
---

# Decoupling Reasoning and Perception: An LLM-LMM Framework for Faithful Visual Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23322" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23322v1</a>
  <a href="https://arxiv.org/pdf/2509.23322.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23322v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23322v1', 'Decoupling Reasoning and Perception: An LLM-LMM Framework for Faithful Visual Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongrui Jia, Chaoya Jiang, Shikun Zhang, Wei Ye

**分类**: cs.CV

**发布日期**: 2025-09-27

---

## 💡 一句话要点

**提出解耦推理与感知的LLM-LMM框架，提升视觉推理的可靠性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉推理` `大型语言模型` `大型多模态模型` `解耦推理` `思维链`

## 📋 核心要点

1. 现有LMM在长链视觉推理中过度依赖文本逻辑，忽略视觉信息，导致推理错误。
2. 论文提出解耦推理与感知的框架，利用LLM进行推理，LMM专注于视觉信息提取。
3. 该框架无需额外训练，显著减少了无根据的推理步骤，提高了视觉推理的准确性。

## 📝 摘要（中文）

大型语言模型(LLM)的推理能力显著提升，特别是利用扩展的思维链(CoT)推理。受此启发，研究人员将这些范式扩展到大型多模态模型(LMM)。然而，一个关键限制是：随着推理链的扩展，LMM越来越依赖于文本逻辑，逐渐失去对底层视觉信息的依赖。这导致推理路径偏离图像内容，最终导致错误的结论。为了解决这个问题，我们引入了一个非常简单但有效的免训练视觉推理流程。核心概念是将推理和感知过程解耦。强大的LLM负责高层次的推理，策略性地询问LMM以提取逻辑链所需的特定视觉信息。LMM则专门作为视觉问答引擎，按需提供必要的感知细节。这种轻量级的即插即用方法不需要额外的训练或架构更改。全面的评估验证了我们的框架有效地控制了视觉推理过程，从而显著减少了视觉上无根据的推理步骤，并大大提高了推理的保真度。

## 🔬 方法详解

**问题定义**：论文旨在解决大型多模态模型（LMM）在视觉推理过程中，随着推理链的延长，越来越依赖文本逻辑而忽略视觉信息，从而导致推理结果与图像内容不符的问题。现有方法的痛点在于推理和感知过程耦合在一起，导致LMM难以保持对视觉信息的准确理解和利用。

**核心思路**：论文的核心思路是将推理和感知过程解耦。具体来说，利用大型语言模型（LLM）强大的推理能力来 orchestrate 高层次的推理过程，并让大型多模态模型（LMM）专注于视觉信息的提取。LLM根据推理的需要，有策略地向LMM提问，获取特定的视觉信息，从而避免LMM在推理过程中过度依赖文本逻辑。

**技术框架**：整体框架包含两个主要模块：LLM推理模块和LMM视觉问答模块。LLM作为推理引擎，负责生成推理链，并根据推理步骤的需要，向LMM提出视觉问题。LMM作为视觉信息提取引擎，接收LLM提出的问题，并根据图像内容给出答案。LLM接收LMM的答案后，继续进行推理，直到得出最终结论。整个过程是一个迭代的问答过程，LLM负责推理，LMM负责提供视觉信息。

**关键创新**：最重要的技术创新点在于解耦推理和感知过程。与现有方法相比，该方法不再让LMM同时负责推理和感知，而是将这两个任务分别交给LLM和LMM，从而充分发挥各自的优势。这种解耦的设计可以有效避免LMM在推理过程中过度依赖文本逻辑，从而提高视觉推理的准确性。

**关键设计**：该框架的关键设计在于LLM和LMM之间的交互方式。LLM需要能够根据推理的需要，生成合适的视觉问题，并能够有效地利用LMM提供的答案。LMM需要能够准确地理解LLM提出的问题，并能够从图像中提取出相关的视觉信息。论文中没有提及具体的参数设置、损失函数或网络结构，因为该方法是免训练的，不需要对LLM或LMM进行额外的训练。

## 📊 实验亮点

该论文提出的框架在视觉推理任务上取得了显著的性能提升。通过解耦推理和感知过程，有效地减少了视觉上无根据的推理步骤，并大大提高了推理的保真度。具体实验数据未在摘要中给出，但强调了该框架的有效性。

## 🎯 应用场景

该研究成果可应用于各种需要视觉推理的场景，例如智能客服、自动驾驶、医疗诊断等。通过提高视觉推理的准确性和可靠性，可以提升这些应用的智能化水平，并为用户提供更优质的服务。未来，该方法可以进一步扩展到更复杂的视觉推理任务，例如视频理解、三维场景理解等。

## 📄 摘要（原文）

> Significant advancements in the reasoning capabilities of Large Language Models (LLMs) are now driven by test-time scaling laws, particularly those leveraging extended Chain-of-Thought (CoT) reasoning. Inspired by these breakthroughs, researchers have extended these paradigms to Large Multimodal Models (LMMs). However, a critical limitation emerges: as their reasoning chains extend, LMMs increasingly rely on textual logic, progressively losing grounding in the underlying visual information. This leads to reasoning paths that diverge from the image content, culminating in erroneous conclusions. To address this, we introduce a strikingly simple yet effective training-free visual-reasoning pipeline. The core concept is to decouple the reasoning and perception processes. A powerful LLM orchestrates the high-level reasoning, strategically interrogating a LMM to extract specific visual information required for its logical chain. The LMM, in turn, functions exclusively as a visual question-answering engine, supplying the necessary perceptual details on demand. This lightweight, plug-and-play approach requires no additional training or architectural changes. Comprehensive evaluations validate that our framework effectively governs the visual reasoning process, leading to a significant reduction in visually-unfounded reasoning steps and a substantial improvement in reasoning fidelity.

