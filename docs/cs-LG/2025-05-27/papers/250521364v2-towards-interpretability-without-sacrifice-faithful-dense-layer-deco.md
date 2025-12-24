---
layout: default
title: Towards Interpretability Without Sacrifice: Faithful Dense Layer Decomposition with Mixture of Decoders
---

# Towards Interpretability Without Sacrifice: Faithful Dense Layer Decomposition with Mixture of Decoders

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21364" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21364v2</a>
  <a href="https://arxiv.org/pdf/2505.21364.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21364v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21364v2', 'Towards Interpretability Without Sacrifice: Faithful Dense Layer Decomposition with Mixture of Decoders')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: James Oldfield, Shawn Im, Sharon Li, Mihalis A. Nicolaou, Ioannis Patras, Grigorios G Chrysos

**分类**: cs.LG, cs.AI

**发布日期**: 2025-05-27 (更新: 2025-10-22)

**备注**: Accepted at NeurIPS 2025

**🔗 代码/项目**: [GITHUB](https://github.com/james-oldfield/MxD/)

---

## 💡 一句话要点

**提出混合解码器以解决多层感知机可解释性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多层感知机` `可解释性` `混合解码器` `稀疏性` `自然语言处理` `机器学习` `模型优化`

## 📋 核心要点

1. 现有方法在实现可解释性时未能忠实重建原始映射，导致模型性能下降。
2. 论文提出通过层级稀疏性来解决准确性与可解释性之间的权衡，引入混合解码器（MxDs）。
3. 实验结果表明，MxDs在稀疏性-准确性方面显著优于现有方法，尤其在参数量达到30亿的语言模型中。

## 📝 摘要（中文）

多层感知机（MLP）是大型语言模型的重要组成部分，但其密集表示使得理解、编辑和引导变得困难。现有方法通过神经元级稀疏性学习可解释的近似，但未能忠实重建原始映射，显著增加模型的下一个标记交叉熵损失。本文倡导转向层级稀疏性，以克服稀疏层近似中的准确性权衡。我们引入混合解码器（MxDs），它通过灵活的张量分解，将预训练的密集层扩展为数万个专用子层。实验表明，MxDs在语言模型的稀疏性-准确性边界上显著超越了最先进的方法，展示了设计可解释且忠实分解的新前景。

## 🔬 方法详解

**问题定义**：本文旨在解决多层感知机（MLP）在可解释性方面的不足，现有方法通过神经元级稀疏性未能忠实重建原始映射，导致性能下降。

**核心思路**：论文提出通过层级稀疏性来克服稀疏层近似中的准确性权衡，引入混合解码器（MxDs），将密集层扩展为多个专用子层，以保持表达能力。

**技术框架**：MxDs通过灵活的张量分解实现，每个稀疏激活的MxD子层执行全秩权重的线性变换，整体架构包括多个子层和解码器的组合。

**关键创新**：MxDs的主要创新在于其能够在高稀疏性下保持原始解码器的表达能力，与现有方法相比，提供了更高的准确性和可解释性。

**关键设计**：MxDs的设计包括对稀疏性进行优化的参数设置，损失函数的选择，以及网络结构的灵活性，以确保在稀疏激活下仍能实现有效的特征学习。

## 📊 实验亮点

实验结果显示，MxDs在稀疏性-准确性边界上显著超越了最先进的方法，如Transcoders，尤其在参数量达到30亿的语言模型中，提升幅度明显，展示了其在可解释性与性能之间的优越平衡。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、机器翻译和对话系统等。通过提供可解释且忠实的模型分解，MxDs有助于提高模型的透明度和可控性，进而推动人工智能系统在实际应用中的信任度和接受度。

## 📄 摘要（原文）

> Multilayer perceptrons (MLPs) are an integral part of large language models, yet their dense representations render them difficult to understand, edit, and steer. Recent methods learn interpretable approximations via neuron-level sparsity, yet fail to faithfully reconstruct the original mapping--significantly increasing model's next-token cross-entropy loss. In this paper, we advocate for moving to layer-level sparsity to overcome the accuracy trade-off in sparse layer approximation. Under this paradigm, we introduce Mixture of Decoders (MxDs). MxDs generalize MLPs and Gated Linear Units, expanding pre-trained dense layers into tens of thousands of specialized sublayers. Through a flexible form of tensor factorization, each sparsely activating MxD sublayer implements a linear transformation with full-rank weights--preserving the original decoders' expressive capacity even under heavy sparsity. Experimentally, we show that MxDs significantly outperform state-of-the-art methods (e.g., Transcoders) on the sparsity-accuracy frontier in language models with up to 3B parameters. Further evaluations on sparse probing and feature steering demonstrate that MxDs learn similarly specialized features of natural language--opening up a promising new avenue for designing interpretable yet faithful decompositions. Our code is included at: https://github.com/james-oldfield/MxD/.

