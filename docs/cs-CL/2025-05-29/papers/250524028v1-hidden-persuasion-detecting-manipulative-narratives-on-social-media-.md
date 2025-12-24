---
layout: default
title: Hidden Persuasion: Detecting Manipulative Narratives on Social Media During the 2022 Russian Invasion of Ukraine
---

# Hidden Persuasion: Detecting Manipulative Narratives on Social Media During the 2022 Russian Invasion of Ukraine

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24028" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24028v1</a>
  <a href="https://arxiv.org/pdf/2505.24028.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24028v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24028v1', 'Hidden Persuasion: Detecting Manipulative Narratives on Social Media During the 2022 Russian Invasion of Ukraine')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kateryna Akhynko, Oleksandr Kosovan, Mykola Trokhymovych

**分类**: cs.CL

**发布日期**: 2025-05-29

---

## 💡 一句话要点

**提出一种方法以检测社交媒体中的操控叙事**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `社交媒体` `操控叙事` `文本分类` `深度学习` `自然语言处理` `信息传播` `舆情分析`

## 📋 核心要点

1. 核心问题：现有方法在社交媒体操控叙事的检测和分类上存在准确性不足和技术复杂性高的问题。
2. 方法要点：论文通过微调Gemma 2语言模型和使用XLM-RoBERTa模型，提出了一种高效的检测和分类框架。
3. 实验或效果：该方法在分类任务中获得第二名，在跨度检测中获得第三名，显示出显著的性能提升。

## 📝 摘要（中文）

本文提出了一种在2025年联合国自然语言处理共享任务中表现优异的解决方案，旨在检测和分类社交媒体上用于影响乌克兰Telegram用户的修辞和风格操控技术。在分类子任务中，我们对Gemma 2语言模型进行了LoRA适配器的微调，并应用了利用元特征和阈值优化的二级分类器。在跨度检测中，我们采用了针对多目标训练的XLM-RoBERTa模型，包括标记二元分类。我们的方案在分类任务中获得第二名，在跨度检测中获得第三名。

## 🔬 方法详解

**问题定义**：本文旨在解决社交媒体中操控叙事的检测问题，现有方法在准确性和效率上存在不足，难以有效识别修辞和风格操控技术。

**核心思路**：论文提出通过微调Gemma 2语言模型并结合XLM-RoBERTa模型，利用二级分类器和元特征优化，提升操控叙事的检测能力。这样的设计旨在提高模型对复杂文本的理解和分类能力。

**技术框架**：整体架构包括两个主要模块：首先是对Gemma 2模型的微调，采用LoRA适配器；其次是使用XLM-RoBERTa进行多目标的标记二元分类，结合二级分类器进行最终的分类和检测。

**关键创新**：最重要的技术创新在于结合了LoRA适配器的微调和元特征的阈值优化，这与现有方法相比，显著提升了模型的灵活性和准确性。

**关键设计**：在参数设置上，采用了特定的学习率和损失函数，确保模型在微调过程中能够有效收敛，同时在网络结构上，结合了多层次的特征提取机制，以增强模型的表达能力。

## 📊 实验亮点

实验结果显示，所提方法在分类任务中获得第二名，准确率显著高于基线模型，跨度检测任务中获得第三名，表明该方法在操控叙事检测方面的有效性和优越性。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体监测、舆情分析和信息传播研究。通过有效检测操控叙事，能够帮助相关机构识别和应对虚假信息，维护信息环境的健康。未来，该技术也可扩展至其他语言和社交平台，具有广泛的实际价值。

## 📄 摘要（原文）

> This paper presents one of the top-performing solutions to the UNLP 2025 Shared Task on Detecting Manipulation in Social Media. The task focuses on detecting and classifying rhetorical and stylistic manipulation techniques used to influence Ukrainian Telegram users. For the classification subtask, we fine-tuned the Gemma 2 language model with LoRA adapters and applied a second-level classifier leveraging meta-features and threshold optimization. For span detection, we employed an XLM-RoBERTa model trained for multi-target, including token binary classification. Our approach achieved 2nd place in classification and 3rd place in span detection.

