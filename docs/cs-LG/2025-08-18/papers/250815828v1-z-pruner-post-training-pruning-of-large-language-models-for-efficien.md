---
layout: default
title: "Z-Pruner: Post-Training Pruning of Large Language Models for Efficiency without Retraining"
---

# Z-Pruner: Post-Training Pruning of Large Language Models for Efficiency without Retraining

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.15828" class="toolbar-btn" target="_blank">📄 arXiv: 2508.15828v1</a>
  <a href="https://arxiv.org/pdf/2508.15828.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.15828v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.15828v1', 'Z-Pruner: Post-Training Pruning of Large Language Models for Efficiency without Retraining')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Samiul Basir Bhuiyan, Md. Sazzad Hossain Adib, Mohammed Aman Bhuiyan, Muhammad Rafsan Kabir, Moshiur Farazi, Shafin Rahman, Nabeel Mohammed

**分类**: cs.LG, cs.CL

**发布日期**: 2025-08-18

**备注**: Accepted at AICCSA 2025

**🔗 代码/项目**: [GITHUB](https://github.com/sazzadadib/Z-Pruner)

---

## 💡 一句话要点

**提出Z-Pruner以解决大语言模型后训练剪枝效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `后训练剪枝` `大型语言模型` `模型稀疏化` `自然语言处理` `性能优化`

## 📋 核心要点

1. 现有的后训练剪枝方法往往导致性能显著下降或需要昂贵的微调，限制了其实际应用。
2. Z-Pruner通过结合权重更新幅度和激活模式，有效识别和消除冗余参数，实现了模型的稀疏化。
3. 实验结果显示，Z-Pruner在多个大型语言模型上表现优异，取得了最低的困惑度和最高的零-shot准确率。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）在自然语言处理任务中取得了显著进展，但模型规模的不断扩大给部署、可扩展性和能效带来了挑战。为了解决这些问题，后训练剪枝成为一种有前景的方法，可以在不需要重新训练的情况下减少模型大小和推理延迟。然而，许多现有的剪枝方法会导致显著的性能下降或需要计算成本高昂的微调。本文提出了Z-Pruner，这是一种新颖的后训练剪枝方法，旨在有效识别和消除冗余参数。Z-Pruner利用权重更新幅度和激活模式，具有模型无关性、效率高和易于实现的特点。实验结果表明，Z-Pruner在多个标准语言基准测试中超越了现有的剪枝方法，取得了最低的困惑度分数和最高的零-shot准确率。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型后训练剪枝过程中性能下降和微调需求高的问题。现有方法在剪枝后往往需要重新训练，增加了计算成本和复杂性。

**核心思路**：Z-Pruner的核心思路是利用权重更新幅度和激活模式来识别冗余参数，从而在不进行重新训练的情况下实现模型稀疏化。这种设计使得剪枝过程更加高效且不损失性能。

**技术框架**：Z-Pruner的整体架构包括参数识别、剪枝决策和模型评估三个主要模块。首先，通过分析权重更新和激活模式来识别冗余参数；然后，基于这些信息进行剪枝；最后，评估剪枝后的模型性能。

**关键创新**：Z-Pruner的主要创新在于其模型无关性和高效性，能够在不同的LLM架构上应用，而不需要进行复杂的微调。这与传统方法形成鲜明对比，后者通常依赖于大量的权重更新。

**关键设计**：在Z-Pruner中，参数设置和剪枝策略经过精心设计，以确保在剪枝过程中尽量减少性能损失。具体的损失函数和网络结构设计使得剪枝过程更加高效，能够在多个标准基准上进行验证。

## 📊 实验亮点

实验结果表明，Z-Pruner在多个大型语言模型（如LLaMA-2、LLaMA-3和OPT）上表现优异，取得了最低的困惑度分数和最高的零-shot准确率，超越了现有的剪枝方法，显示出显著的性能提升。

## 🎯 应用场景

Z-Pruner的潜在应用场景包括自然语言处理、对话系统和文本生成等领域。通过有效减少模型大小和推理延迟，Z-Pruner能够提升大型语言模型在实际应用中的可用性和能效，推动更广泛的商业化应用。未来，该方法可能会影响更多领域的模型优化和部署策略。

## 📄 摘要（原文）

> Large language models (LLMs) have rapidly advanced in recent years, achieving remarkable performance across a wide range of natural language processing tasks. However, this progress has come at the cost of increasingly large model sizes, which pose significant challenges for deployment, scalability, and energy efficiency. To address these limitations, post-training pruning has emerged as a promising approach for reducing model size and inference latency without the need for retraining. Despite these advantages, many existing pruning methods result in substantial performance degradation or require computationally expensive fine-tuning. In this work, we introduce Z-Pruner, a novel post-training pruning method designed to induce sparsity in pretrained LLMs without any retraining. Unlike conventional approaches, Z-Pruner leverages both weight update magnitudes and activation patterns to identify and eliminate redundant parameters more effectively. Our method is model-agnostic, efficient, and easy to implement. We evaluate Z-Pruner using multiple widely-used LLM architectures, including LLaMA-2, LLaMA-3, and OPT, across a diverse set of standard language benchmarks. Experimental results demonstrate that Z-Pruner surpasses state-of-the-art pruning methods that require intensive weight updates. Specifically, Z-Pruner achieves the lowest perplexity scores and the highest overall average score for zero-shot accuracy. We have made the corresponding codes publicly available at https://github.com/sazzadadib/Z-Pruner.

