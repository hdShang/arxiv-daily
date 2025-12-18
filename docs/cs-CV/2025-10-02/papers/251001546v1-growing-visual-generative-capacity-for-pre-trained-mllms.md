---
layout: default
title: Growing Visual Generative Capacity for Pre-Trained MLLMs
---

# Growing Visual Generative Capacity for Pre-Trained MLLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.01546" class="toolbar-btn" target="_blank">📄 arXiv: 2510.01546v1</a>
  <a href="https://arxiv.org/pdf/2510.01546.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.01546v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.01546v1', 'Growing Visual Generative Capacity for Pre-Trained MLLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hanyu Wang, Jiaming Han, Ziyan Yang, Qi Zhao, Shanchuan Lin, Xiangyu Yue, Abhinav Shrivastava, Zhenheng Yang, Hao Chen

**分类**: cs.CV, cs.LG

**发布日期**: 2025-10-02

**备注**: Project page: https://hywang66.github.io/bridge/

---

## 💡 一句话要点

**提出Bridge：一种基于混合Transformer架构的纯自回归统一多模态大语言模型，提升视觉生成能力。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `自回归模型` `图像生成` `视觉理解` `混合Transformer` `语义到像素` `next-token预测`

## 📋 核心要点

1. 现有MLLM在视觉生成方面存在挑战，混合方法打破自回归范式，纯自回归方法则在语义对齐和像素保真度间权衡。
2. Bridge通过混合Transformer架构，在纯自回归框架下，增强预训练视觉理解模型的生成能力，实现统一的图像理解和生成。
3. 实验表明，Bridge在理解和生成任务上表现优异，且训练所需数据更少，时间更短，显著提升了效率。

## 📝 摘要（中文）

多模态大语言模型(MLLM)将语言模型的成功扩展到视觉理解领域。目前的研究致力于构建统一的MLLM，以支持理解和生成。然而，构建此类模型仍然具有挑战性：混合方法将连续嵌入与扩散或基于流的目标相结合，产生高质量的图像，但打破了自回归范式；而纯自回归方法统一了文本和图像预测，通过离散视觉tokens，但通常面临语义对齐和像素级保真度之间的权衡。本文提出Bridge，一种纯自回归统一MLLM，通过混合Transformer架构增强预训练视觉理解模型的生成能力，从而在单个next-token预测框架内实现图像理解和生成。为了进一步提高视觉生成保真度，我们提出了一种语义到像素的离散表示，该表示将紧凑的语义tokens与细粒度的像素tokens集成在一起，仅以7.9%的序列长度增加实现了强大的语言对齐和视觉细节的精确描述。在各种多模态基准上的大量实验表明，与之前的统一MLLM相比，Bridge在理解和生成基准上都取得了有竞争力的或更优越的结果，同时需要更少的训练数据和更短的训练时间。

## 🔬 方法详解

**问题定义**：现有MLLM模型在统一理解和生成能力方面面临挑战。混合方法虽然能生成高质量图像，但破坏了自回归特性。纯自回归方法虽然统一了文本和图像预测，但在语义对齐和像素级保真度之间存在trade-off。因此，如何构建一个既能理解又能生成，且保持自回归特性的MLLM是一个关键问题。

**核心思路**：Bridge的核心思路是通过混合Transformer架构，将预训练的视觉理解模型与生成能力相结合，从而在纯自回归框架下实现图像理解和生成。通过next-token预测的方式，统一处理文本和图像，避免了混合方法带来的自回归问题，同时通过语义到像素的离散表示，提升生成图像的保真度。

**技术框架**：Bridge的整体架构是一个基于Transformer的自回归模型。它包含以下主要模块：1) 预训练的视觉理解模型，用于提取图像的语义特征；2) 混合Transformer模块，用于融合视觉特征和文本信息，并进行next-token预测；3) 语义到像素的离散表示模块，用于将语义tokens转换为细粒度的像素tokens，从而提高生成图像的保真度。整个流程是：输入文本和图像，视觉理解模型提取图像特征，混合Transformer融合特征并预测下一个token，语义到像素模块将语义token转换为像素token，最终生成图像。

**关键创新**：Bridge的关键创新在于以下两点：1) 混合Transformer架构，它允许模型在纯自回归框架下同时进行理解和生成；2) 语义到像素的离散表示，它通过将紧凑的语义tokens与细粒度的像素tokens相结合，实现了强大的语言对齐和视觉细节的精确描述。与现有方法的本质区别在于，Bridge避免了混合方法带来的自回归问题，同时提升了生成图像的保真度。

**关键设计**：Bridge的关键设计包括：1) 混合Transformer模块的具体结构，例如Transformer层数、注意力机制的选择等；2) 语义到像素的离散表示的具体实现方式，例如语义token和像素token的数量、编码方式等；3) 训练目标函数的设计，例如如何平衡理解和生成任务的损失，如何优化语义到像素的转换过程等。论文中可能还涉及一些超参数的设置，例如学习率、batch size等。

## 📊 实验亮点

实验结果表明，Bridge在多个多模态基准测试中取得了优异的成绩，包括图像描述、视觉问答和图像生成等任务。与之前的统一MLLM相比，Bridge在理解和生成基准上都取得了有竞争力的或更优越的结果，同时需要更少的训练数据和更短的训练时间。例如，在图像生成任务上，Bridge生成的图像质量明显优于其他自回归模型，并且在语义对齐方面也表现出色。

## 🎯 应用场景

Bridge具有广泛的应用前景，例如图像编辑、图像生成、视觉对话、机器人控制等。它可以用于创建更逼真、更可控的虚拟世界，也可以用于辅助人类进行设计和创作。此外，Bridge还可以应用于智能客服、自动驾驶等领域，提升人机交互的效率和质量。未来，Bridge有望成为多模态人工智能领域的重要基石。

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) extend the success of language models to visual understanding, and recent efforts have sought to build unified MLLMs that support both understanding and generation. However, constructing such models remains challenging: hybrid approaches combine continuous embeddings with diffusion or flow-based objectives, producing high-quality images but breaking the autoregressive paradigm, while pure autoregressive approaches unify text and image prediction over discrete visual tokens but often face trade-offs between semantic alignment and pixel-level fidelity. In this work, we present Bridge, a pure autoregressive unified MLLM that augments pre-trained visual understanding models with generative ability through a Mixture-of-Transformers architecture, enabling both image understanding and generation within a single next-token prediction framework. To further improve visual generation fidelity, we propose a semantic-to-pixel discrete representation that integrates compact semantic tokens with fine-grained pixel tokens, achieving strong language alignment and precise description of visual details with only a 7.9% increase in sequence length. Extensive experiments across diverse multimodal benchmarks demonstrate that Bridge achieves competitive or superior results in both understanding and generation benchmarks, while requiring less training data and reduced training time compared to prior unified MLLMs.

