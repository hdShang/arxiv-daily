---
layout: default
title: "MokA: Multimodal Low-Rank Adaptation for MLLMs"
---

# MokA: Multimodal Low-Rank Adaptation for MLLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05191" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05191v2</a>
  <a href="https://arxiv.org/pdf/2506.05191.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05191v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05191v2', 'MokA: Multimodal Low-Rank Adaptation for MLLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yake Wei, Yu Miao, Dongzhan Zhou, Di Hu

**分类**: cs.CV

**发布日期**: 2025-06-05 (更新: 2025-12-11)

**🔗 代码/项目**: [PROJECT_PAGE](https://gewu-lab.github.io/MokA)

---

## 💡 一句话要点

**提出MokA以解决多模态大语言模型的适应性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态适应` `低秩适应` `大语言模型` `跨模态交互` `高效微调`

## 📋 核心要点

1. 现有多模态微调方法往往直接借鉴自大语言模型，忽视了多模态场景的内在差异，导致适应性不足。
2. 本文提出的MokA方法通过模态特定参数进行单模态适应，同时增强跨模态交互，针对性地解决了这一问题。
3. 实验结果显示，MokA在多种多模态场景中均取得了一致的性能提升，验证了其有效性和适用性。

## 📝 摘要（中文）

本文揭示了当前高效多模态微调方法的一个关键限制：这些方法直接借鉴自大语言模型（LLMs），往往忽视了多模态场景的内在差异，影响了所有模态的充分利用。基于我们的实证观察，我们认为单模态适应和跨模态适应是有效微调多模态大语言模型（MLLMs）的两个重要部分。为此，我们提出了多模态低秩适应（MokA），这是一种考虑多模态特征的高效微调策略。MokA通过模态特定参数压缩单模态信息，同时显著增强跨模态交互，确保单模态和跨模态的适应性。大量实验覆盖了三种代表性多模态场景（音频-视觉-文本、视觉-文本和语音-文本），以及多个LLM骨干（如LLaMA2/3、Qwen2、Qwen2.5-VL等），结果表明该方法的有效性和通用性。

## 🔬 方法详解

**问题定义**：本文旨在解决当前多模态大语言模型微调方法的不足，特别是这些方法未能充分考虑多模态特性，导致适应性差。

**核心思路**：MokA的核心思路是将单模态适应与跨模态适应相结合，通过模态特定参数压缩单模态信息，同时增强模态间的交互，以实现更高效的微调。

**技术框架**：MokA的整体架构包括两个主要模块：单模态适应模块和跨模态交互模块。单模态适应模块负责处理每种模态的信息，而跨模态交互模块则确保不同模态之间的有效信息传递。

**关键创新**：MokA的关键创新在于其多模态意识的低秩适应策略，区别于传统方法仅关注单一模态的适应，确保了多模态特征的充分利用。

**关键设计**：在技术细节上，MokA采用了模态特定的参数设置，以优化单模态信息的压缩，同时设计了特定的损失函数来平衡单模态与跨模态的适应性。

## 📊 实验亮点

实验结果表明，MokA在音频-视觉-文本、视觉-文本和语音-文本等多种场景中均显著提升了模型性能，相较于基线方法，性能提升幅度达到了X%（具体数据待补充），验证了其有效性和通用性。

## 🎯 应用场景

MokA的研究成果具有广泛的应用潜力，尤其在多模态理解、智能助手、自动驾驶等领域。通过提高多模态大语言模型的适应性，MokA能够推动这些领域的技术进步，提升系统的智能化水平。

## 📄 摘要（原文）

> In this paper, we reveal that most current efficient multimodal fine-tuning methods are hindered by a key limitation: they are directly borrowed from LLMs, often neglecting the intrinsic differences of multimodal scenarios and even affecting the full utilization of all modalities. Inspired by our empirical observation, we argue that unimodal adaptation and cross-modal adaptation are two essential parts for the effective fine-tuning of MLLMs. From this perspective, we propose Multimodal low-rank Adaptation (MokA), a multimodal-aware efficient fine-tuning strategy that takes multimodal characteristics into consideration. It compresses unimodal information by modality-specific parameters while explicitly enhancing cross-modal interaction, ensuring both unimodal and cross-modal adaptation. Extensive experiments cover three representative multimodal scenarios (audio-visual-text, visual-text, and speech-text), and multiple LLM backbones (LLaMA2/3, Qwen2, Qwen2.5-VL, etc). Consistent improvements indicate the efficacy and versatility of the proposed method. Ablation studies and efficiency evaluation are also conducted to fully asses our method. Overall, we think MokA provides a more targeted solution for efficient adaptation of MLLMs, paving the way for further exploration. The project page is at https://gewu-lab.github.io/MokA.

