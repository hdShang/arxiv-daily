---
layout: default
title: Learning to Generate Human-Human-Object Interactions from Textual Descriptions
---

# Learning to Generate Human-Human-Object Interactions from Textual Descriptions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.20446" class="toolbar-btn" target="_blank">📄 arXiv: 2511.20446v1</a>
  <a href="https://arxiv.org/pdf/2511.20446.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.20446v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.20446v1', 'Learning to Generate Human-Human-Object Interactions from Textual Descriptions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jeonghyeon Na, Sangwon Baik, Inhee Lee, Junyoung Lee, Hanbyul Joo

**分类**: cs.CV

**发布日期**: 2025-11-25

**备注**: Project Page: https://tlb-miss.github.io/hhoi/

---

## 💡 一句话要点

**提出HHOI生成框架，从文本描述生成人-人-物交互场景，并构建了相关数据集。**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)** **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `人-人-物交互` `HHOI生成` `扩散模型` `文本生成图像` `多主体交互`

## 📋 核心要点

1. 现有方法难以理解复杂、上下文相关的人际互动行为，尤其是在涉及多个个体和场景物体时。
2. 论文提出一种新颖的HHOI生成框架，通过解耦人-物和人-人交互，并结合扩散模型实现高质量生成。
3. 实验表明，该方法在文本驱动的HHOI生成任务上优于现有方法，并可扩展到多人运动生成。

## 📝 摘要（中文）

本文提出了一种新的研究问题，即建模涉及物体的两个人之间的人-人-物交互(HHOI)。为了解决HHOI专用数据集的缺乏问题，我们构建了一个新的HHOI数据集，并提出了一种利用图像生成模型合成HHOI数据的方法。我们首先从HHOI中提取出单个人-物交互(HOI)和人-人交互(HHI)，并使用基于分数的扩散模型训练文本到HOI和文本到HHI模型。最后，我们提出了一个统一的生成框架，集成了这两个独立的模型，能够在单个高级采样过程中合成完整的HHOI。我们的方法将HHOI生成扩展到多人设置，实现涉及两个以上个体的交互。实验结果表明，我们的方法能够根据文本描述生成逼真的HHOI，优于以往仅关注单人HOI的方法。此外，我们还介绍了涉及物体的多人运动生成作为我们框架的一个应用。

## 🔬 方法详解

**问题定义**：现有方法主要集中于单个人与物体的交互(HOI)生成，忽略了人与人之间的交互关系，以及这种关系如何受到物体的影响。因此，现有方法无法生成复杂的人-人-物交互(HHOI)场景，缺乏对多主体交互行为的建模能力。

**核心思路**：论文的核心思路是将HHOI分解为两个更简单的子问题：人-物交互(HOI)和人-人交互(HHI)。通过分别建模这两个子问题，然后将它们集成到一个统一的生成框架中，从而实现HHOI的生成。这种解耦的方式降低了建模的复杂性，并允许利用现有的HOI和HHI数据。

**技术框架**：该框架包含以下几个主要模块：1) 数据集构建：收集并标注HHOI数据，并从中提取HOI和HHI数据。2) 文本到HOI模型：使用基于分数的扩散模型，根据文本描述生成HOI。3) 文本到HHI模型：使用基于分数的扩散模型，根据文本描述生成HHI。4) 统一生成框架：将HOI和HHI模型集成到一个框架中，通过联合采样生成完整的HHOI场景。

**关键创新**：该论文的关键创新在于提出了HHOI的概念，并设计了一个解耦的生成框架来解决这个问题。与现有方法相比，该方法能够显式地建模人与人之间的交互关系，并将其与人与物体的交互关系相结合，从而生成更逼真、更符合上下文的交互场景。此外，该方法还提出了一个数据合成策略，用于解决HHOI数据集的缺乏问题。

**关键设计**：论文使用了基于分数的扩散模型作为HOI和HHI生成器的核心。扩散模型通过逐步添加噪声到数据中，然后学习如何从噪声中恢复数据，从而实现高质量的生成。此外，论文还设计了一个统一的采样过程，用于将HOI和HHI模型集成在一起，生成完整的HHOI场景。具体的损失函数和网络结构细节在论文中有详细描述，但摘要中未明确提及。

## 📊 实验亮点

实验结果表明，该方法在文本驱动的HHOI生成任务上优于现有方法。通过定性和定量评估，证明了该方法能够生成更逼真、更符合文本描述的HHOI场景。此外，该方法还成功地应用于多人运动生成任务，展示了其在复杂场景下的泛化能力。具体的性能指标和对比基线在论文中进行了详细的展示。

## 🎯 应用场景

该研究成果可应用于虚拟现实、游戏开发、社交机器人等领域。例如，可以用于生成更逼真的虚拟社交场景，训练社交机器人理解和模拟人类的交互行为，以及辅助设计更符合人类习惯的交互界面。未来，该技术有望扩展到更复杂的多人交互场景，并应用于智能监控、行为分析等领域。

## 📄 摘要（原文）

> The way humans interact with each other, including interpersonal distances, spatial configuration, and motion, varies significantly across different situations. To enable machines to understand such complex, context-dependent behaviors, it is essential to model multiple people in relation to the surrounding scene context. In this paper, we present a novel research problem to model the correlations between two people engaged in a shared interaction involving an object. We refer to this formulation as Human-Human-Object Interactions (HHOIs). To overcome the lack of dedicated datasets for HHOIs, we present a newly captured HHOIs dataset and a method to synthesize HHOI data by leveraging image generative models. As an intermediary, we obtain individual human-object interaction (HOIs) and human-human interaction (HHIs) from the HHOIs, and with these data, we train an text-to-HOI and text-to-HHI model using score-based diffusion model. Finally, we present a unified generative framework that integrates the two individual model, capable of synthesizing complete HHOIs in a single advanced sampling process. Our method extends HHOI generation to multi-human settings, enabling interactions involving more than two individuals. Experimental results show that our method generates realistic HHOIs conditioned on textual descriptions, outperforming previous approaches that focus only on single-human HOIs. Furthermore, we introduce multi-human motion generation involving objects as an application of our framework.

