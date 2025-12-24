---
layout: default
title: "MANZANO: A Simple and Scalable Unified Multimodal Model with a Hybrid Vision Tokenizer"
---

# MANZANO: A Simple and Scalable Unified Multimodal Model with a Hybrid Vision Tokenizer

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16197" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16197v1</a>
  <a href="https://arxiv.org/pdf/2509.16197.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16197v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16197v1', 'MANZANO: A Simple and Scalable Unified Multimodal Model with a Hybrid Vision Tokenizer')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yanghao Li, Rui Qian, Bowen Pan, Haotian Zhang, Haoshuo Huang, Bowen Zhang, Jialing Tong, Haoxuan You, Xianzhi Du, Zhe Gan, Hyunjik Kim, Chao Jia, Zhenbang Wang, Yinfei Yang, Mingfei Gao, Zi-Yi Dou, Wenze Hu, Chang Gao, Dongxu Li, Philipp Dufter, Zirui Wang, Guoli Yin, Zhengdong Zhang, Chen Chen, Yang Zhao, Ruoming Pang, Zhifeng Chen

**分类**: cs.CV, cs.CL, cs.LG

**发布日期**: 2025-09-19

---

## 💡 一句话要点

**Manzano：一种基于混合视觉Token的简单可扩展统一多模态模型**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `统一模型` `视觉理解` `视觉生成` `混合Token` `大语言模型` `扩散模型`

## 📋 核心要点

1. 现有开源多模态大语言模型在视觉内容理解和生成能力之间存在性能权衡。
2. Manzano通过混合图像分词器和统一训练方案，实现了理解和生成能力的可扩展联合学习。
3. Manzano在统一模型中取得了领先成果，并在文本丰富的评估中与专用模型竞争。

## 📝 摘要（中文）

本文提出Manzano，一个简单且可扩展的统一框架，通过将混合图像分词器与精心设计的训练方案相结合，显著降低了现有开放源代码模型在视觉内容理解和生成能力之间的性能权衡。该框架使用一个共享的视觉编码器，通过两个轻量级适配器，在公共语义空间中为图像到文本的理解生成连续嵌入，为文本到图像的生成生成离散token。统一的自回归LLM以文本和图像token的形式预测高层语义，辅助扩散解码器随后将图像token转换为像素。这种架构以及统一的理解和生成数据训练方案，实现了两种能力的可扩展联合学习。Manzano在统一模型中实现了最先进的结果，并且在富文本评估中与专用模型相比具有竞争力。研究表明，任务冲突最小，并且模型规模的扩大带来了持续的收益，验证了混合分词器的设计选择。

## 🔬 方法详解

**问题定义**：现有统一多模态大语言模型在视觉内容理解（image-to-text）和视觉内容生成（text-to-image）之间存在性能瓶颈。即，为了提升理解能力，往往牺牲生成能力，反之亦然。开源模型难以同时兼顾两种能力，限制了其应用范围。

**核心思路**：Manzano的核心思路是使用一个共享的视觉编码器，并在此基础上构建两个轻量级的适配器，分别用于图像到文本的理解（生成连续嵌入）和文本到图像的生成（生成离散token）。通过这种混合tokenization方法，模型可以在一个共同的语义空间中处理两种模态，从而减少任务冲突，并实现两种能力的可扩展联合学习。

**技术框架**：Manzano的整体架构包含以下几个主要模块：1) 共享视觉编码器：负责提取图像的视觉特征。2) 图像到文本适配器：将视觉特征转换为连续嵌入，用于图像理解任务。3) 文本到图像适配器：将视觉特征转换为离散token，用于图像生成任务。4) 统一自回归LLM：预测文本和图像token形式的高层语义。5) 扩散解码器：将图像token转换为像素，生成最终图像。训练过程采用统一的训练方案，同时利用理解和生成数据进行联合训练。

**关键创新**：Manzano的关键创新在于其混合视觉tokenization方法。传统的视觉模型通常只使用一种tokenization方式，要么是连续嵌入，要么是离散token。Manzano同时使用两种tokenization方式，并针对不同的任务选择合适的tokenization方式。这种混合方法可以更好地平衡理解和生成能力，并减少任务冲突。

**关键设计**：Manzano的关键设计包括：1) 轻量级适配器：使用轻量级适配器可以减少模型参数量，并提高训练效率。2) 统一训练方案：使用统一的训练方案可以同时优化理解和生成能力。3) 辅助扩散解码器：使用扩散解码器可以将图像token转换为高质量的图像。

## 📊 实验亮点

Manzano在统一模型中实现了最先进的结果，并在文本丰富的评估中与专用模型相比具有竞争力。实验结果表明，Manzano在理解和生成任务上都取得了显著的性能提升，并且模型规模的扩大带来了持续的收益。这些结果验证了Manzano的混合tokenization方法和统一训练方案的有效性。

## 🎯 应用场景

Manzano具有广泛的应用前景，例如：多模态对话系统、图像描述生成、视觉内容创作、教育娱乐等。该模型可以用于构建更智能、更自然的交互式应用，并为用户提供更丰富的视觉体验。未来，Manzano有望成为多模态人工智能领域的重要基石。

## 📄 摘要（原文）

> Unified multimodal Large Language Models (LLMs) that can both understand and generate visual content hold immense potential. However, existing open-source models often suffer from a performance trade-off between these capabilities. We present Manzano, a simple and scalable unified framework that substantially reduces this tension by coupling a hybrid image tokenizer with a well-curated training recipe. A single shared vision encoder feeds two lightweight adapters that produce continuous embeddings for image-to-text understanding and discrete tokens for text-to-image generation within a common semantic space. A unified autoregressive LLM predicts high-level semantics in the form of text and image tokens, with an auxiliary diffusion decoder subsequently translating the image tokens into pixels. The architecture, together with a unified training recipe over understanding and generation data, enables scalable joint learning of both capabilities. Manzano achieves state-of-the-art results among unified models, and is competitive with specialist models, particularly on text-rich evaluation. Our studies show minimal task conflicts and consistent gains from scaling model size, validating our design choice of a hybrid tokenizer.

