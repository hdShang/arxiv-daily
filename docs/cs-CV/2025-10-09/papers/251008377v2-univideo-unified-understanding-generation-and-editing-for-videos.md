---
layout: default
title: UniVideo: Unified Understanding, Generation, and Editing for Videos
---

# UniVideo: Unified Understanding, Generation, and Editing for Videos

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.08377" target="_blank" class="toolbar-btn">arXiv: 2510.08377v2</a>
    <a href="https://arxiv.org/pdf/2510.08377.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.08377v2" 
            onclick="toggleFavorite(this, '2510.08377v2', 'UniVideo: Unified Understanding, Generation, and Editing for Videos')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Cong Wei, Quande Liu, Zixuan Ye, Qiulin Wang, Xintao Wang, Pengfei Wan, Kun Gai, Wenhu Chen

**分类**: cs.CV

**发布日期**: 2025-10-09 (更新: 2025-10-21)

**备注**: Project Website https://congwei1230.github.io/UniVideo/

---

## 💡 一句话要点

**UniVideo：统一视频理解、生成与编辑的多模态框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频生成` `视频编辑` `多模态学习` `统一建模` `扩散模型` `大型语言模型` `指令学习`

## 📋 核心要点

1. 现有多模态模型主要集中在图像领域，视频理解、生成和编辑任务缺乏统一建模。
2. UniVideo采用双流架构，结合MLLM进行指令理解，MMDiT进行视频生成，实现多任务统一。
3. 实验表明，UniVideo在多项视频生成和编辑任务上超越了特定任务的SOTA模型，并具备任务组合能力。

## 📝 摘要（中文）

本文提出了UniVideo，一个通用的框架，将统一建模扩展到视频领域。UniVideo采用双流设计，结合了用于指令理解的多模态大型语言模型（MLLM）和用于视频生成的多模态扩散Transformer（MMDiT）。这种设计能够准确地解释复杂的多模态指令，同时保持视觉一致性。基于此架构，UniVideo将各种视频生成和编辑任务统一在单一的多模态指令范式下，并对它们进行联合训练。大量实验表明，UniVideo在文本/图像到视频生成、上下文视频生成和上下文视频编辑方面与最先进的特定任务基线相匹配或超过它们。值得注意的是，UniVideo的统一设计实现了两种形式的泛化。首先，UniVideo支持任务组合，例如通过在单个指令中集成多个功能来将编辑与风格迁移相结合。其次，即使没有经过自由形式视频编辑的显式训练，UniVideo也能将其编辑能力从大规模图像编辑数据转移到此设置，处理诸如绿屏角色或更改视频中的材质等未见过的指令。除了这些核心功能外，UniVideo还支持基于视觉提示的视频生成，其中MLLM解释视觉提示并在合成过程中指导MMDiT。为了促进未来的研究，我们将发布我们的模型和代码。

## 🔬 方法详解

**问题定义**：现有统一多模态模型主要集中在图像领域，缺乏对视频理解、生成和编辑任务的统一建模能力。针对视频的生成和编辑任务通常需要针对特定任务设计模型，泛化能力和组合能力较弱。

**核心思路**：UniVideo的核心思路是将视频理解、生成和编辑任务统一到一个多模态指令范式下，通过一个统一的模型来处理不同的任务。该模型通过双流架构，分别处理指令理解和视频生成，从而实现对复杂指令的准确理解和视觉一致性的视频生成。

**技术框架**：UniVideo采用双流架构。第一路是多模态大型语言模型（MLLM），负责理解输入的文本或图像指令。第二路是多模态扩散Transformer（MMDiT），负责根据MLLM的输出生成或编辑视频。MLLM将指令编码成视觉特征，然后MMDiT利用这些特征生成视频。整个框架通过联合训练，学习不同任务之间的共享知识。

**关键创新**：UniVideo的关键创新在于其统一的建模方式和双流架构。它将不同的视频生成和编辑任务统一到一个框架下，避免了为每个任务单独设计模型。双流架构使得模型能够同时处理指令理解和视频生成，从而实现更准确和一致的结果。此外，UniVideo还展示了从图像编辑到视频编辑的迁移能力，以及任务组合能力。

**关键设计**：MLLM采用预训练的语言模型，并进行多模态微调，以理解文本和图像指令。MMDiT采用扩散模型架构，通过逐步去噪的方式生成视频。损失函数包括生成损失和指令对齐损失，以确保生成的视频与指令一致。具体的网络结构和参数设置未在摘要中详细说明，需要参考论文全文。

## 📊 实验亮点

UniVideo在文本/图像到视频生成、上下文视频生成和上下文视频编辑方面与最先进的特定任务基线相匹配或超过它们。更重要的是，UniVideo展现了强大的泛化能力，能够将图像编辑能力迁移到视频编辑，并支持任务组合，例如将编辑与风格迁移结合。这些结果表明UniVideo具有很强的实用性和潜力。

## 🎯 应用场景

UniVideo具有广泛的应用前景，包括视频内容创作、视频编辑、虚拟现实、游戏开发等领域。它可以用于生成各种类型的视频，例如动画、特效视频、产品演示视频等。此外，UniVideo还可以用于视频编辑，例如修改视频内容、改变视频风格、添加特效等。该研究的实际价值在于降低了视频创作和编辑的门槛，提高了效率，并为用户提供了更多的创作可能性。

## 📄 摘要（原文）

> Unified multimodal models have shown promising results in multimodal content generation and editing but remain largely limited to the image domain. In this work, we present UniVideo, a versatile framework that extends unified modeling to the video domain. UniVideo adopts a dual-stream design, combining a Multimodal Large Language Model (MLLM) for instruction understanding with a Multimodal DiT (MMDiT) for video generation. This design enables accurate interpretation of complex multimodal instructions while preserving visual consistency. Built on this architecture, UniVideo unifies diverse video generation and editing tasks under a single multimodal instruction paradigm and is jointly trained across them. Extensive experiments demonstrate that UniVideo matches or surpasses state-of-the-art task-specific baselines in text/image-to-video generation, in-context video generation and in-context video editing. Notably, the unified design of UniVideo enables two forms of generalization. First, UniVideo supports task composition, such as combining editing with style transfer, by integrating multiple capabilities within a single instruction. Second, even without explicit training on free-form video editing, UniVideo transfers its editing capability from large-scale image editing data to this setting, handling unseen instructions such as green-screening characters or changing materials within a video. Beyond these core capabilities, UniVideo also supports visual-prompt-based video generation, where the MLLM interprets visual prompts and guides the MMDiT during synthesis. To foster future research, we will release our model and code.

