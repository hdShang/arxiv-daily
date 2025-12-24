---
layout: default
title: "Spatial-LLaVA: Enhancing Large Language Models with Spatial Referring Expressions for Visual Understanding"
---

# Spatial-LLaVA: Enhancing Large Language Models with Spatial Referring Expressions for Visual Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.12194" class="toolbar-btn" target="_blank">📄 arXiv: 2505.12194v1</a>
  <a href="https://arxiv.org/pdf/2505.12194.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.12194v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.12194v1', 'Spatial-LLaVA: Enhancing Large Language Models with Spatial Referring Expressions for Visual Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xuefei Sun, Doncey Albin, Cecilia Mauceri, Dusty Woods, Christoffer Heckman

**分类**: cs.RO

**发布日期**: 2025-05-18

---

## 💡 一句话要点

**提出Spatial-LLaVA以解决视觉理解中的空间关系问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `空间关系` `视觉理解` `SUN-Spot数据集` `自主导航` `互动机器人` `空间指称表达`

## 📋 核心要点

1. 现有多模态大语言模型在处理空间关系和独特物体定位等特定任务时表现不佳，尤其在数据稀缺的情况下。
2. 本文提出了Spatial-LLaVA模型，利用SUN-Spot v2.0数据集，通过对话数据训练，增强模型对空间指称表达的理解能力。
3. 实验结果显示，Spatial-LLaVA在零-shot视觉空间推理基准数据集上提升了3.15%，显著优于以往方法。

## 📝 摘要（中文）

多模态大语言模型（MLLMs）在理解视觉与文本输入方面表现出色，但在处理特定任务时，如物体间的空间关系或在相似特征物体中定位独特目标物体时，常常表现不佳。为此，本文引入了SUN-Spot v2.0数据集，包含90k图像-文本对及地标物体的额外注释。我们提出的Spatial-LLaVA模型通过对话数据训练，确保图像中物体与文本中提及的物体之间的强对齐，从而有效学习空间指称表达。Spatial-LLaVA在零-shot视觉空间推理基准数据集上超越了之前的方法，提升幅度为3.15%。该模型在自主导航和互动机器人等实际场景中具有重要应用价值。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态大语言模型在特定任务中对空间关系理解不足的问题，现有方法在数据稀缺情况下表现不佳，无法准确定位物体。

**核心思路**：提出Spatial-LLaVA，通过SUN-Spot v2.0数据集训练，利用对话数据生成的强对齐机制，确保图像与文本之间的物体对应关系，从而有效学习空间指称表达。

**技术框架**：整体架构包括数据集构建、模型训练和评估三个主要模块。数据集构建阶段引入了Set-of-Marks提示，模型训练阶段使用对话数据，评估阶段通过零-shot方式验证模型性能。

**关键创新**：最重要的创新在于引入了Set-of-Marks提示机制，增强了图像中物体与文本中提及物体的对齐，避免了语义信息的偏见。

**关键设计**：模型训练中采用了特定的损失函数以优化对齐效果，网络结构设计上注重对空间指称表达的学习，确保模型在实际应用中的准确性。

## 📊 实验亮点

在零-shot视觉空间推理基准数据集上，Spatial-LLaVA模型的性能提升达3.15%，显著优于以往的多模态大语言模型。这一结果表明，模型在理解空间指称表达方面的有效性和准确性。

## 🎯 应用场景

Spatial-LLaVA在自主导航和互动机器人等领域具有广泛的应用潜力。其对空间关系的精准理解能够提升机器人在复杂环境中的决策能力，增强人机交互的自然性和有效性。未来，该技术可能在智能家居、自动驾驶等场景中发挥重要作用。

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) have demonstrated remarkable abilities in comprehending visual input alongside text input. Typically, these models are trained on extensive data sourced from the internet, which are sufficient for general tasks such as scene understanding and question answering. However, they often underperform on specialized tasks where online data is scarce, such as determining spatial relationships between objects or localizing unique target objects within a group of objects sharing similar features. In response to this challenge, we introduce the SUN-Spot v2.0 dataset1, now comprising a total of 90k image-caption pairs and additional annotations on the landmark objects. Each image-caption pair utilizes Set-of-Marks prompting as an additional indicator, mapping each landmark object in the image to the corresponding object mentioned in the caption. Furthermore, we present Spatial-LLaVA, an MLLM trained on conversational data generated by a state-of-the-art language model using the SUNSpot v2.0 dataset. Our approach ensures a robust alignment between the objects in the images and their corresponding object mentions in the captions, enabling our model to learn spatial referring expressions without bias from the semantic information of the objects. Spatial-LLaVA outperforms previous methods by 3.15% on the zero-shot Visual Spatial Reasoning benchmark dataset. Spatial-LLaVA is specifically designed to precisely understand spatial referring expressions, making it highly applicable for tasks in real-world scenarios such as autonomous navigation and interactive robotics, where precise object recognition is critical.

