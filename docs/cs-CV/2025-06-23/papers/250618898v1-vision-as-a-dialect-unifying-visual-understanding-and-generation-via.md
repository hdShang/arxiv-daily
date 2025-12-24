---
layout: default
title: "Vision as a Dialect: Unifying Visual Understanding and Generation via Text-Aligned Representations"
---

# Vision as a Dialect: Unifying Visual Understanding and Generation via Text-Aligned Representations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.18898" class="toolbar-btn" target="_blank">📄 arXiv: 2506.18898v1</a>
  <a href="https://arxiv.org/pdf/2506.18898.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.18898v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.18898v1', 'Vision as a Dialect: Unifying Visual Understanding and Generation via Text-Aligned Representations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiaming Han, Hao Chen, Yang Zhao, Hanyu Wang, Qi Zhao, Ziyan Yang, Hao He, Xiangyu Yue, Lu Jiang

**分类**: cs.CV, cs.AI, cs.CL, cs.MM

**发布日期**: 2025-06-23

**备注**: Project page: https://tar.csuhan.com

---

## 💡 一句话要点

**提出多模态框架以统一视觉理解与生成**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态框架` `视觉理解` `生成模型` `文本对齐` `跨模态融合` `高保真输出` `自回归模型` `扩散模型`

## 📋 核心要点

1. 现有多模态方法在视觉理解与生成之间缺乏有效的统一，导致跨模态任务的效率低下。
2. 本文提出的TA-Tok通过文本对齐的方式将图像转换为离散标记，整合视觉与文本信息，形成统一的表示。
3. 实验结果显示，Tar在多个基准测试中表现优异，收敛速度更快，训练效率更高，超越了现有的多模态LLM方法。

## 📝 摘要（中文）

本文提出了一种多模态框架，旨在通过共享的离散语义表示来统一视觉理解与生成。核心是文本对齐的标记器（TA-Tok），该标记器利用大型语言模型的词汇将图像转换为离散标记。通过将视觉和文本整合到一个扩展的词汇空间中，我们的多模态LLM Tar实现了跨模态输入和输出，无需特定于模态的设计。此外，论文提出了规模自适应的编码和解码方法，以平衡效率与视觉细节，并引入生成去标记器以生成高保真视觉输出。为满足多样化的解码需求，我们使用了两种互补的去标记器：快速自回归模型和基于扩散的模型。通过先进的预训练任务，增强模态融合，实验结果表明Tar在多个基准测试中与现有多模态LLM方法相匹配或超越，展现出更快的收敛速度和更高的训练效率。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多模态方法在视觉理解与生成之间缺乏有效统一的问题，导致跨模态任务的效率低下和效果不佳。

**核心思路**：论文的核心思路是通过文本对齐的标记器（TA-Tok）将图像转换为离散标记，从而实现视觉与文本的统一表示，消除模态特定设计的需求。

**技术框架**：整体架构包括TA-Tok模块、跨模态LLM Tar、规模自适应编码解码模块以及生成去标记器。TA-Tok负责将图像转化为离散标记，Tar实现跨模态输入输出，解码模块则根据需求生成高保真视觉输出。

**关键创新**：最重要的技术创新在于提出了TA-Tok和生成去标记器的结合，利用文本对齐的方式实现了视觉与文本的深度融合，与现有方法相比，显著提升了跨模态任务的效率和效果。

**关键设计**：在设计上，采用了规模自适应的编码和解码策略，以平衡效率与视觉细节，同时引入了快速自回归模型和基于扩散的去标记器，以满足不同的解码需求。

## 📊 实验亮点

实验结果表明，Tar在多个基准测试中表现优异，收敛速度比现有多模态LLM方法快，训练效率提高了显著，具体性能数据未详述，但整体效果超越了现有方法。

## 🎯 应用场景

该研究的潜在应用领域包括智能视觉系统、自动化内容生成、跨模态检索等。通过统一的视觉理解与生成框架，可以提升多模态任务的效率和效果，推动人工智能在实际应用中的发展与创新。

## 📄 摘要（原文）

> This paper presents a multimodal framework that attempts to unify visual understanding and generation within a shared discrete semantic representation. At its core is the Text-Aligned Tokenizer (TA-Tok), which converts images into discrete tokens using a text-aligned codebook projected from a large language model's (LLM) vocabulary. By integrating vision and text into a unified space with an expanded vocabulary, our multimodal LLM, Tar, enables cross-modal input and output through a shared interface, without the need for modality-specific designs. Additionally, we propose scale-adaptive encoding and decoding to balance efficiency and visual detail, along with a generative de-tokenizer to produce high-fidelity visual outputs. To address diverse decoding needs, we utilize two complementary de-tokenizers: a fast autoregressive model and a diffusion-based model. To enhance modality fusion, we investigate advanced pre-training tasks, demonstrating improvements in both visual understanding and generation. Experiments across benchmarks show that Tar matches or surpasses existing multimodal LLM methods, achieving faster convergence and greater training efficiency. Code, models, and data are available at https://tar.csuhan.com

