---
layout: default
title: DLP: Dynamic Layerwise Pruning in Large Language Models
---

# DLP: Dynamic Layerwise Pruning in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23807" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23807v3</a>
  <a href="https://arxiv.org/pdf/2505.23807.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23807v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23807v3', 'DLP: Dynamic Layerwise Pruning in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuli Chen, Bo Cheng, Jiale Han, Yingying Zhang, Yingting Li, Shuhao Zhang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-27 (更新: 2025-06-03)

**备注**: Accepted by ICML 2025

**🔗 代码/项目**: [GITHUB](https://github.com/ironartisan/DLP)

---

## 💡 一句话要点

**提出动态层级剪枝方法以提升大语言模型的推理效率**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `动态剪枝` `大语言模型` `模型压缩` `推理效率` `参数高效微调`

## 📋 核心要点

1. 现有的均匀层级剪枝方法在高稀疏度下常导致模型性能显著下降，无法有效利用不同层的贡献。
2. 动态层级剪枝（DLP）通过结合模型权重与输入激活信息，自适应地为每层分配剪枝率，从而优化剪枝效果。
3. 实验表明，DLP在70%稀疏度下显著降低了LLaMA2-7B的困惑度，并提高了模型的准确率，展示了其优越性。

## 📝 摘要（中文）

剪枝技术近年来被广泛应用于减少大语言模型（LLMs）的参数规模并提高推理效率。现有的主流剪枝方法通常依赖于均匀的层级剪枝策略，这在高稀疏度下可能导致性能严重下降。为了解决这一问题，本文提出了一种新颖的方法——动态层级剪枝（DLP），该方法通过整合模型权重与输入激活信息，自适应地确定每一层的相对重要性，从而相应地分配剪枝率。实验结果表明，DLP在多个LLM中有效地保持了高稀疏度下的模型性能，尤其是在70%稀疏度时，DLP使LLaMA2-7B的困惑度降低了7.79，并提高了2.7%的平均准确率。DLP还与多种现有的LLM压缩技术兼容，并可无缝集成到参数高效微调（PEFT）中。

## 🔬 方法详解

**问题定义**：本文旨在解决现有均匀层级剪枝方法在高稀疏度下导致的性能下降问题。这些方法未能充分考虑不同层在模型中的重要性，导致剪枝效果不佳。

**核心思路**：动态层级剪枝（DLP）通过分析模型权重与输入激活信息，动态调整每层的剪枝率，从而更有效地保留重要层的信息，减少性能损失。

**技术框架**：DLP的整体架构包括三个主要模块：1) 权重分析模块，评估各层的重要性；2) 激活信息模块，捕捉输入数据对层的影响；3) 剪枝决策模块，根据分析结果动态调整剪枝率。

**关键创新**：DLP的核心创新在于其自适应剪枝策略，区别于传统方法的固定剪枝率，能够根据模型状态和输入动态调整，显著提升了模型在高稀疏度下的性能。

**关键设计**：在DLP中，关键参数包括剪枝率的动态计算公式，损失函数设计考虑了模型性能与稀疏度之间的平衡，网络结构则保持了原有模型的完整性，以确保剪枝后的模型仍具备良好的表达能力。

## 📊 实验亮点

实验结果显示，在70%稀疏度下，DLP使LLaMA2-7B的困惑度降低了7.79，平均准确率提高了2.7%。这些结果相较于现有最先进的方法，展示了DLP在保持模型性能方面的显著优势。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和文本生成等大语言模型相关任务。通过提升模型的推理效率和减少计算资源消耗，DLP可以在边缘计算和移动设备上实现更高效的应用，具有重要的实际价值和广泛的未来影响。

## 📄 摘要（原文）

> Pruning has recently been widely adopted to reduce the parameter scale and improve the inference efficiency of Large Language Models (LLMs). Mainstream pruning techniques often rely on uniform layerwise pruning strategies, which can lead to severe performance degradation at high sparsity levels. Recognizing the varying contributions of different layers in LLMs, recent studies have shifted their focus toward non-uniform layerwise pruning. However, these approaches often rely on pre-defined values, which can result in suboptimal performance. To overcome these limitations, we propose a novel method called Dynamic Layerwise Pruning (DLP). This approach adaptively determines the relative importance of each layer by integrating model weights with input activation information, assigning pruning rates accordingly. Experimental results show that DLP effectively preserves model performance at high sparsity levels across multiple LLMs. Specifically, at 70% sparsity, DLP reduces the perplexity of LLaMA2-7B by 7.79 and improves the average accuracy by 2.7% compared to state-of-the-art methods. Moreover, DLP is compatible with various existing LLM compression techniques and can be seamlessly integrated into Parameter-Efficient Fine-Tuning (PEFT). We release the code at https://github.com/ironartisan/DLP to facilitate future research.

