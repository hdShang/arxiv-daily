---
layout: default
title: "From Long to Lean: Performance-aware and Adaptive Chain-of-Thought Compression via Multi-round Refinement"
---

# From Long to Lean: Performance-aware and Adaptive Chain-of-Thought Compression via Multi-round Refinement

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22144" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22144v1</a>
  <a href="https://arxiv.org/pdf/2509.22144.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22144v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22144v1', 'From Long to Lean: Performance-aware and Adaptive Chain-of-Thought Compression via Multi-round Refinement')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jianzhi Yan, Le Liu, Youcheng Pan, Shiwei Chen, Zike Yuan, Yang Xiang, Buzhou Tang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-26

**备注**: 17 pages, 8 figures

**🔗 代码/项目**: [GITHUB](https://github.com/Leon221220/MACC)

---

## 💡 一句话要点

**提出MACC框架，通过多轮细化自适应压缩CoT，提升推理效率与准确率。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `Chain-of-Thought` `CoT压缩` `多轮细化` `自适应压缩` `性能预测` `token弹性` `推理效率`

## 📋 核心要点

1. CoT推理虽提升复杂任务性能，但其冗长性导致推理延迟过高，限制了实际应用。
2. MACC框架通过多轮细化自适应压缩CoT，利用token弹性现象优化压缩深度，提升效率。
3. 实验表明，MACC在准确率上优于现有方法，显著降低CoT长度和推理延迟，且性能可预测。

## 📝 摘要（中文）

Chain-of-Thought (CoT) 推理在复杂任务上表现出色，但由于其冗长性导致推理延迟显著。本文提出多轮自适应Chain-of-Thought压缩（MACC）框架，该框架利用token弹性现象（即过小的token预算反而会增加输出长度）通过多轮细化逐步压缩CoT。这种自适应策略使MACC能够确定每个输入的最佳压缩深度。实验结果表明，MACC在平均准确率上比最先进的基线提高了5.6%，同时平均减少了47个token的CoT长度，并显著降低了延迟。此外，我们证明了测试时性能（准确率和token长度）可以使用可解释的特征（如训练集上的困惑度和压缩率）进行可靠预测。在不同模型上进行评估表明，该方法无需重复微调即可实现高效的模型选择和预测，证明CoT压缩既有效又可预测。代码将在https://github.com/Leon221220/MACC 上发布。

## 🔬 方法详解

**问题定义**：论文旨在解决Chain-of-Thought (CoT) 推理中由于冗长性导致的推理延迟问题。现有方法在压缩CoT时，往往采用固定的压缩策略，无法根据不同输入的特性进行自适应调整，导致压缩效果不佳，甚至可能降低模型性能。此外，如何有效预测压缩后的性能也是一个挑战。

**核心思路**：论文的核心思路是利用token弹性现象，即在token预算过小的情况下，模型为了满足输出需求反而会生成更长的文本。通过多轮细化，逐步压缩CoT，并根据每一轮的压缩效果自适应地调整压缩深度，从而在保证准确率的同时，尽可能地减少CoT的长度和推理延迟。

**技术框架**：MACC框架主要包含以下几个阶段：1) 初始CoT生成：使用原始的CoT方法生成初始的推理链。2) 多轮压缩：通过逐步减少token预算，对CoT进行多轮压缩。3) 性能预测：利用训练集上的困惑度和压缩率等特征，预测测试时性能。4) 自适应调整：根据性能预测结果，自适应地选择最佳的压缩深度。

**关键创新**：MACC的关键创新在于：1) 提出了多轮细化的CoT压缩方法，能够逐步优化压缩效果。2) 利用token弹性现象，避免过度压缩导致性能下降。3) 提出了基于困惑度和压缩率的性能预测方法，能够有效指导压缩深度的选择。4) 实现了自适应的CoT压缩，能够根据不同输入的特性进行优化。

**关键设计**：在多轮压缩阶段，论文采用了不同的token预算进行压缩，并监控每一轮的压缩效果。性能预测模型使用了困惑度和压缩率作为输入特征，并采用线性回归模型进行预测。自适应调整策略则根据性能预测结果，选择能够最大化准确率并最小化token长度的压缩深度。具体的损失函数和网络结构等技术细节在论文中未详细说明，属于未知信息。

## 📊 实验亮点

实验结果表明，MACC在多个数据集上取得了显著的性能提升。例如，在平均准确率上，MACC比最先进的基线提高了5.6%，同时平均减少了47个token的CoT长度。此外，实验还验证了性能预测方法的有效性，证明可以使用训练集上的特征可靠地预测测试时性能。这些结果表明，MACC是一种有效且可预测的CoT压缩方法。

## 🎯 应用场景

MACC框架可应用于各种需要高效推理的场景，例如对话系统、智能问答、知识图谱推理等。通过压缩CoT，可以显著降低推理延迟，提高用户体验。此外，MACC的性能预测能力可以帮助开发者选择合适的模型和压缩策略，从而优化系统性能。该研究对于推动CoT推理在实际应用中的落地具有重要意义。

## 📄 摘要（原文）

> Chain-of-Thought (CoT) reasoning improves performance on complex tasks but introduces significant inference latency due to verbosity. We propose Multiround Adaptive Chain-of-Thought Compression (MACC), a framework that leverages the token elasticity phenomenon--where overly small token budgets can paradoxically increase output length--to progressively compress CoTs via multiround refinement. This adaptive strategy allows MACC to determine the optimal compression depth for each input. Our method achieves an average accuracy improvement of 5.6 percent over state-of-the-art baselines, while also reducing CoT length by an average of 47 tokens and significantly lowering latency. Furthermore, we show that test-time performance--accuracy and token length--can be reliably predicted using interpretable features like perplexity and compression rate on the training set. Evaluated across different models, our method enables efficient model selection and forecasting without repeated fine-tuning, demonstrating that CoT compression is both effective and predictable. Our code will be released in https://github.com/Leon221220/MACC.

