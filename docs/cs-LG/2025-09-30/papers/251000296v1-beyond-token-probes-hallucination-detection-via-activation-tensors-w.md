---
layout: default
title: "Beyond Token Probes: Hallucination Detection via Activation Tensors with ACT-ViT"
---

# Beyond Token Probes: Hallucination Detection via Activation Tensors with ACT-ViT

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.00296" class="toolbar-btn" target="_blank">📄 arXiv: 2510.00296v1</a>
  <a href="https://arxiv.org/pdf/2510.00296.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00296v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.00296v1', 'Beyond Token Probes: Hallucination Detection via Activation Tensors with ACT-ViT')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guy Bar-Shalom, Fabrizio Frasca, Yaniv Galron, Yftah Ziser, Haggai Maron

**分类**: cs.LG

**发布日期**: 2025-09-30

**备注**: Published in NeurIPS 2025

**🔗 代码/项目**: [GITHUB](https://github.com/BarSGuy/ACT-ViT)

---

## 💡 一句话要点

**提出ACT-ViT，利用激活张量检测大语言模型中的幻觉问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `幻觉检测` `大语言模型` `激活张量` `Vision Transformer` `多模型训练`

## 📋 核心要点

1. 现有幻觉检测方法依赖于特定LLM的token探测，泛化能力和效率受限。
2. ACT-ViT将激活张量视为图像，利用Vision Transformer学习跨LLM的通用幻觉模式。
3. 实验表明，ACT-ViT在多LLM训练下性能显著提升，并具备良好的零样本和迁移学习能力。

## 📝 摘要（中文）

检测大型语言模型生成文本中的幻觉对于其安全部署至关重要。虽然探测分类器显示出潜力，但它们仅在孤立的层-token对上运行，并且是特定于LLM的，限制了其有效性并阻碍了跨LLM应用。本文提出了一种新方法来解决这些缺点。我们构建在激活数据在两个轴（层×token）上的自然序列结构之上，并提倡将完整的激活张量视为图像。我们设计了ACT-ViT，一个受Vision Transformer启发的模型，可以有效且高效地应用于激活张量，并支持同时在来自多个LLM的数据上进行训练。通过包含各种LLM和数据集的全面实验，我们证明了ACT-ViT始终优于传统的探测技术，同时保持了极高的部署效率。特别是，我们表明我们的架构受益于多LLM训练，在未见过的数据集上实现了强大的零样本性能，并且可以通过微调有效地转移到新的LLM。

## 🔬 方法详解

**问题定义**：现有的大语言模型幻觉检测方法，例如token探测，通常针对特定模型设计，泛化能力差，需要为每个模型单独训练。此外，这些方法通常只关注激活的局部信息，忽略了层与token之间的上下文关系。

**核心思路**：本文的核心思路是将大语言模型的激活张量视为图像，利用Vision Transformer (ViT) 学习激活张量中的全局和上下文信息，从而检测幻觉。这种方法可以跨不同的LLM进行泛化，并且能够利用多LLM数据进行联合训练，提高模型的鲁棒性和泛化能力。

**技术框架**：ACT-ViT的整体架构包括以下几个主要步骤：1. 从LLM中提取激活张量（layers x tokens x hidden_size）。2. 将激活张量reshape成类似于图像的格式。3. 使用Vision Transformer对激活张量进行编码，提取特征。4. 使用分类器基于提取的特征预测是否存在幻觉。

**关键创新**：ACT-ViT的关键创新在于将激活张量视为图像，并利用Vision Transformer进行处理。这使得模型能够学习到激活张量中的全局和上下文信息，从而提高幻觉检测的准确性和泛化能力。此外，ACT-ViT支持多LLM训练，可以利用来自不同模型的激活数据进行联合训练，进一步提高模型的鲁棒性。

**关键设计**：ACT-ViT使用了标准的Vision Transformer架构，包括Patch Embedding、Transformer Encoder和MLP Head。Patch Embedding将激活张量分割成小的patch，然后将每个patch映射到高维向量。Transformer Encoder由多个Transformer Block组成，每个Block包含Multi-Head Self-Attention和Feed Forward Network。MLP Head用于将Transformer Encoder的输出映射到最终的预测结果。损失函数使用了标准的交叉熵损失函数。

## 📊 实验亮点

ACT-ViT在多个LLM和数据集上进行了评估，结果表明其性能始终优于传统的token探测方法。ACT-ViT在多LLM训练下性能显著提升，并且在未见过的数据集上实现了强大的零样本性能。此外，ACT-ViT可以通过微调有效地迁移到新的LLM，降低了部署成本。

## 🎯 应用场景

ACT-ViT可用于提高大型语言模型生成内容的可靠性和安全性，例如自动文本摘要、机器翻译、对话系统等。通过检测和减少幻觉，可以提升用户对LLM的信任度，并降低错误信息传播的风险。该技术还有助于开发更安全、更可靠的AI应用。

## 📄 摘要（原文）

> Detecting hallucinations in Large Language Model-generated text is crucial for their safe deployment. While probing classifiers show promise, they operate on isolated layer-token pairs and are LLM-specific, limiting their effectiveness and hindering cross-LLM applications. In this paper, we introduce a novel approach to address these shortcomings. We build on the natural sequential structure of activation data in both axes (layers $\times$ tokens) and advocate treating full activation tensors akin to images. We design ACT-ViT, a Vision Transformer-inspired model that can be effectively and efficiently applied to activation tensors and supports training on data from multiple LLMs simultaneously. Through comprehensive experiments encompassing diverse LLMs and datasets, we demonstrate that ACT-ViT consistently outperforms traditional probing techniques while remaining extremely efficient for deployment. In particular, we show that our architecture benefits substantially from multi-LLM training, achieves strong zero-shot performance on unseen datasets, and can be transferred effectively to new LLMs through fine-tuning. Full code is available at https://github.com/BarSGuy/ACT-ViT.

