---
layout: default
title: "CoViPAL: Layer-wise Contextualized Visual Token Pruning for Large Vision-Language Models"
---

# CoViPAL: Layer-wise Contextualized Visual Token Pruning for Large Vision-Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.17243" class="toolbar-btn" target="_blank">📄 arXiv: 2508.17243v2</a>
  <a href="https://arxiv.org/pdf/2508.17243.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.17243v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.17243v2', 'CoViPAL: Layer-wise Contextualized Visual Token Pruning for Large Vision-Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zicong Tang, Ziyang Ma, Suqing Wang, Zuchao Li, Lefei Zhang, Hai Zhao, Yun Li, Qianren Wang

**分类**: cs.CV, cs.AI, cs.CL

**发布日期**: 2025-08-24 (更新: 2025-08-30)

**备注**: Accepted by EMNLP 2025

---

## 💡 一句话要点

**提出CoViPAL以解决大规模视觉语言模型中的视觉标记冗余问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `多模态学习` `视觉标记修剪` `上下文化` `计算效率`

## 📋 核心要点

1. 现有方法在浅层中缺乏足够的上下文信息，导致冗余视觉标记的修剪效果不佳。
2. CoViPAL通过层级上下文化的修剪方法，利用插件式修剪模块有效预测和移除冗余视觉标记。
3. 实验结果显示，CoViPAL在多个基准测试中表现优异，超越了传统的无训练和有训练修剪方法。

## 📝 摘要（中文）

大规模视觉语言模型（LVLMs）处理由文本标记和从图像或视频中提取的视觉标记组成的多模态输入。由于丰富的视觉信息，单张图像可以生成成千上万的视觉标记，导致在预填充阶段的高计算成本和解码时的显著内存开销。现有方法尝试修剪冗余视觉标记，但在浅层中由于缺乏足够的上下文信息而面临挑战。本文提出CoViPAL，一种层级上下文化视觉标记修剪方法，采用轻量级的插件式修剪模块（PPM）在视觉标记被LVLM处理之前预测并移除冗余标记。实验表明，CoViPAL在相同标记预算下超越了无训练修剪方法，并在可比监督下超越了基于训练的方法，提供了一种可扩展且高效的解决方案，以提高LVLM的推理效率而不影响准确性。

## 🔬 方法详解

**问题定义**：本文旨在解决大规模视觉语言模型中视觉标记的冗余问题。现有方法在浅层中由于上下文信息不足，难以有效修剪冗余标记，导致计算和内存开销增加。

**核心思路**：CoViPAL提出了一种层级上下文化的视觉标记修剪方法，利用上下文信号来识别和移除冗余视觉标记，从而提高模型的推理效率。通过这种方式，即使在浅层也能有效修剪冗余标记。

**技术框架**：该方法的整体架构包括一个插件式修剪模块（PPM），该模块在视觉标记被LVLM处理之前进行冗余标记的预测和移除。PPM是轻量级的、模型无关的，能够与多种LVLM架构无缝集成。

**关键创新**：CoViPAL的主要创新在于其层级上下文化的修剪策略，能够在浅层中有效识别冗余视觉标记，而现有方法往往无法做到这一点。

**关键设计**：PPM的设计确保其轻量性和模型无关性，能够适应不同的LVLM架构。具体的参数设置和损失函数设计尚未详细说明，需进一步研究。

## 📊 实验亮点

在多个基准测试中，CoViPAL在相同的标记预算下超越了无训练修剪方法，并在可比监督下超越了基于训练的方法，显示出显著的性能提升。具体数据尚未提供，需参考原文进行详细了解。

## 🎯 应用场景

CoViPAL的研究成果在多模态学习、计算机视觉和自然语言处理等领域具有广泛的应用潜力。通过提高大规模视觉语言模型的推理效率，该方法可以在实时图像和视频分析、智能助手、自动驾驶等场景中发挥重要作用，推动相关技术的进步与应用。

## 📄 摘要（原文）

> Large Vision-Language Models (LVLMs) process multimodal inputs consisting of text tokens and vision tokens extracted from images or videos. Due to the rich visual information, a single image can generate thousands of vision tokens, leading to high computational costs during the prefilling stage and significant memory overhead during decoding. Existing methods attempt to prune redundant vision tokens, revealing substantial redundancy in visual representations. However, these methods often struggle in shallow layers due to the lack of sufficient contextual information. We argue that many visual tokens are inherently redundant even in shallow layers and can be safely and effectively pruned with appropriate contextual signals. In this work, we propose CoViPAL, a layer-wise contextualized visual token pruning method that employs a Plug-and-Play Pruning Module (PPM) to predict and remove redundant vision tokens before they are processed by the LVLM. The PPM is lightweight, model-agnostic, and operates independently of the LVLM architecture, ensuring seamless integration with various models. Extensive experiments on multiple benchmarks demonstrate that CoViPAL outperforms training-free pruning methods under equal token budgets and surpasses training-based methods with comparable supervision. CoViPAL offers a scalable and efficient solution to improve inference efficiency in LVLMs without compromising accuracy.

