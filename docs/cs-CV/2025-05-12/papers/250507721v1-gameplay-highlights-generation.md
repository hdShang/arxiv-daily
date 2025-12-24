---
layout: default
title: Gameplay Highlights Generation
---

# Gameplay Highlights Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07721" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07721v1</a>
  <a href="https://arxiv.org/pdf/2505.07721.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07721v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07721v1', 'Gameplay Highlights Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Vignesh Edithal, Le Zhang, Ilia Blank, Imran Junejo

**分类**: cs.CV

**发布日期**: 2025-05-12

---

## 💡 一句话要点

**提出自动生成游戏精彩片段以提升玩家分享体验**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `游戏精彩片段` `多模态视频理解` `事件检测` `自然语言监督` `转移学习` `ONNX推理` `社交媒体分享`

## 📋 核心要点

1. 现有的精彩片段检测方法依赖于昂贵的游戏开发者合作或特定于游戏的工程，限制了其普适性和效率。
2. 本研究通过微调多模态视频理解模型X-CLIP，结合人类注释数据集，实现了无需特定游戏工程的精彩片段自动生成。
3. 实验结果显示，微调后的模型在未见过的游戏视频中准确率超过90%，并在低资源游戏上表现出良好的转移学习效果。

## 📝 摘要（中文）

本研究旨在通过自动生成游戏精彩片段，帮助玩家在社交媒体上分享他们的游戏体验，从而节省时间并提高观众参与度。我们首先识别视频中有趣事件的时间间隔，然后将其连接。为此，我们开发了一个包含人类注释的游戏事件检测数据集。传统的精彩片段检测技术需要与游戏开发者进行昂贵的合作，而基于OCR的技术则需要针对每个游戏进行昂贵的工程。我们对多模态通用视频理解模型X-CLIP进行了微调，使其能够在多个游戏中泛化，而无需针对每个游戏进行工程。实验结果表明，该模型在未见过的第一人称射击游戏中能够以超过90%的准确率检测有趣事件，并在低资源游戏上表现出转移学习的迹象。为了使模型适用于生产环境，我们使用ONNX库实现跨平台推理。

## 🔬 方法详解

**问题定义**：本研究解决的是如何自动生成游戏精彩片段的问题。现有方法通常需要与游戏开发者合作，或依赖于特定游戏的OCR技术，导致成本高且难以推广。

**核心思路**：论文的核心思路是利用微调的多模态视频理解模型X-CLIP，通过识别视频中的有趣事件并将其连接，自动生成精彩片段。这种设计避免了对每个游戏进行昂贵的工程。

**技术框架**：整体架构包括数据集构建、事件检测模型的训练和推理。首先，构建包含人类注释的游戏事件数据集；然后，微调X-CLIP模型以提高事件检测能力；最后，使用ONNX库实现跨平台推理。

**关键创新**：最重要的技术创新在于通过自然语言监督提升了模型的性能，使其能够在多个游戏中泛化，而无需针对每个游戏进行单独的工程。

**关键设计**：在模型训练中，采用了特定的损失函数和参数设置，以优化事件检测的准确性。同时，使用ONNX库的后训练量化工具，减少模型大小和推理时间，确保模型在生产环境中的高效运行。

## 📊 实验亮点

实验结果表明，微调后的X-CLIP模型在未见过的第一人称射击游戏中能够以超过90%的准确率检测有趣事件。此外，该模型在低资源游戏上表现出显著的转移学习效果，显示出在小数据集上训练时的优势。

## 🎯 应用场景

该研究的潜在应用场景包括游戏直播、社交媒体分享和游戏回顾等领域。通过自动生成精彩片段，玩家可以更轻松地分享他们的游戏体验，从而提高观众的参与度和互动性。此外，该技术还可以为游戏开发者提供用户行为分析的工具，帮助他们优化游戏设计。

## 📄 摘要（原文）

> In this work, we enable gamers to share their gaming experience on social media by automatically generating eye-catching highlight reels from their gameplay session Our automation will save time for gamers while increasing audience engagement. We approach the highlight generation problem by first identifying intervals in the video where interesting events occur and then concatenate them. We developed an in-house gameplay event detection dataset containing interesting events annotated by humans using VIA video annotator. Traditional techniques for highlight detection such as game engine integration requires expensive collaboration with game developers. OCR techniques which detect patches of specific images or texts require expensive per game engineering and may not generalize across game UI and different language. We finetuned a multimodal general purpose video understanding model such as X-CLIP using our dataset which generalizes across multiple games in a genre without per game engineering. Prompt engineering was performed to improve the classification performance of this multimodal model. Our evaluation showed that such a finetuned model can detect interesting events in first person shooting games from unseen gameplay footage with more than 90% accuracy. Moreover, our model performed significantly better on low resource games (small dataset) when trained along with high resource games, showing signs of transfer learning. To make the model production ready, we used ONNX libraries to enable cross platform inference. These libraries also provide post training quantization tools to reduce model size and inference time for deployment. ONNX runtime libraries with DirectML backend were used to perform efficient inference on Windows OS. We show that natural language supervision in the X-CLIP model leads to data efficient and highly performant video recognition models.

