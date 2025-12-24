---
layout: default
title: "Visual-Aware CoT: Achieving High-Fidelity Visual Consistency in Unified Models"
---

# Visual-Aware CoT: Achieving High-Fidelity Visual Consistency in Unified Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19686" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19686v1</a>
  <a href="https://arxiv.org/pdf/2512.19686.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19686v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19686v1', 'Visual-Aware CoT: Achieving High-Fidelity Visual Consistency in Unified Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zixuan Ye, Quande Liu, Cong Wei, Yuanxing Zhang, Xintao Wang, Pengfei Wan, Kun Gai, Wenhan Luo

**分类**: cs.CV

**发布日期**: 2025-12-22

**备注**: Project Page: https://zixuan-ye.github.io/VACoT/

---

## 💡 一句话要点

**提出Visual-Aware CoT，提升统一模型在多模态生成中视觉一致性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态生成` `视觉一致性` `统一模型` `链式思考` `自适应视觉规划` `迭代视觉校正` `flow-GRPO`

## 📋 核心要点

1. 现有统一模型在多模态生成中，忽略了与参考图像的视觉上下文一致性，导致关键视觉特征丢失。
2. 提出Visual-Aware CoT，通过自适应视觉规划和迭代视觉校正，显式地引导模型保持视觉一致性。
3. 实验表明，该方法在多模态生成任务中，显著优于现有零样本和文本CoT模型，提升视觉一致性。

## 📝 摘要（中文）

本文提出了一种名为Visual-Aware Chain-of-Thought (CoT) 的方法，旨在提高统一模型在多模态生成任务中的视觉一致性。现有方法在生成过程中主要关注文本与文本提示的一致性，忽略了与视觉参考图像的视觉上下文一致性，导致无法保持关键视觉特征（如人物ID、物体属性、风格）。为了解决这个问题，本文将视觉上下文一致性融入到统一模型的推理过程中，通过自适应视觉规划（生成结构化的视觉检查列表，确定需要保持一致性的视觉元素）和迭代视觉校正（在检查列表的指导下进行自我反思并迭代优化生成结果）来显式地促使模型保持视觉一致性。通过监督微调来训练模型进行视觉检查规划、自我反思和自我优化，并使用flow-GRPO通过定制的视觉检查奖励来进一步增强视觉一致性。实验结果表明，本文方法在多模态生成任务中优于零样本统一模型和基于文本CoT的模型，证明了其更高的视觉上下文一致性。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态生成任务中，统一模型生成的图像与参考图像在视觉上下文上不一致的问题。现有方法主要关注文本提示的一致性，忽略了视觉参考图像的关键视觉特征，例如人物身份、物体属性和风格等，导致生成结果质量下降。

**核心思路**：论文的核心思路是将视觉上下文一致性显式地融入到统一模型的推理过程中。通过让模型学习如何识别和保持关键的视觉元素，从而提高生成结果的视觉保真度。这种方法模拟了人类在进行图像生成时的思考过程，即先确定需要保持的视觉特征，然后在生成过程中不断检查和修正。

**技术框架**：整体框架包含两个主要模块：自适应视觉规划和迭代视觉校正。首先，自适应视觉规划模块生成一个结构化的视觉检查列表，用于确定需要保持一致性的视觉元素。然后，迭代视觉校正模块在检查列表的指导下，进行自我反思，并迭代地优化生成结果。整个过程通过监督微调进行训练，并使用flow-GRPO进一步增强视觉一致性。

**关键创新**：论文的关键创新在于将视觉上下文一致性显式地建模到统一模型的推理过程中。通过自适应视觉规划和迭代视觉校正，模型能够更好地理解和保持视觉特征，从而生成更高质量的图像。与现有方法相比，该方法更加关注视觉信息，并能够有效地解决视觉不一致的问题。

**关键设计**：在自适应视觉规划模块中，使用监督学习来训练模型生成视觉检查列表。在迭代视觉校正模块中，使用flow-GRPO来进一步增强视觉一致性，通过定制的视觉检查奖励来引导模型生成更符合视觉上下文的图像。具体的网络结构和参数设置在论文中有详细描述，但具体数值未知。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19686v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19686v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19686v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该方法在多模态生成任务中显著优于零样本统一模型和基于文本CoT的模型，证明了其更高的视觉上下文一致性。具体的性能数据和提升幅度在论文中有详细描述，但具体数值未知。实验结果表明，该方法能够有效地保持关键视觉特征，生成更高质量的图像。

## 🎯 应用场景

该研究成果可应用于图像编辑、图像生成、视频生成等领域，例如，可以用于生成具有特定风格或属性的图像，或者用于修复图像中的视觉不一致性。该方法在虚拟现实、游戏开发、广告设计等领域具有广泛的应用前景，能够提升用户体验和创作效率。

## 📄 摘要（原文）

> Recently, the introduction of Chain-of-Thought (CoT) has largely improved the generation ability of unified models. However, it is observed that the current thinking process during generation mainly focuses on the text consistency with the text prompt, ignoring the \textbf{visual context consistency} with the visual reference images during the multi-modal generation, e.g., multi-reference generation. The lack of such consistency results in the failure in maintaining key visual features (like human ID, object attribute, style). To this end, we integrate the visual context consistency into the reasoning of unified models, explicitly motivating the model to sustain such consistency by 1) Adaptive Visual Planning: generating structured visual check list to figure out the visual element of needed consistency keeping, and 2) Iterative Visual Correction: performing self-reflection with the guidance of check lists and refining the generated result in an iterative manner. To achieve this, we use supervised finetuning to teach the model how to plan the visual checking, conduct self-reflection and self-refinement, and use flow-GRPO to further enhance the visual consistency through a customized visual checking reward. The experiments show that our method outperforms both zero-shot unified models and those with text CoTs in multi-modal generation, demonstrating higher visual context consistency.

