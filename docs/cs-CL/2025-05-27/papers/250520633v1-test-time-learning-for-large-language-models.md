---
layout: default
title: Test-Time Learning for Large Language Models
---

# Test-Time Learning for Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20633" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20633v1</a>
  <a href="https://arxiv.org/pdf/2505.20633.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20633v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20633v1', 'Test-Time Learning for Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jinwu Hu, Zhitian Zhang, Guohao Chen, Xutao Wen, Chao Shuai, Wei Luo, Bin Xiao, Yuanqing Li, Mingkui Tan

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-05-27

**备注**: Accepted by ICML2025

---

## 💡 一句话要点

**提出测试时学习方法以提升大语言模型在特定领域的适应性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `测试时学习` `无标签数据` `低秩适应` `领域适应` `自我监督学习` `样本高效学习`

## 📋 核心要点

1. 现有大语言模型在特定领域的泛化能力不足，难以处理语言的多样性和分布变化。
2. 本文提出的测试时学习方法通过最小化输入困惑度，利用无标签数据自我增强模型性能。
3. 实验结果显示，TLM在领域知识适应上相较于原始LLMs性能提升至少20%。

## 📝 摘要（中文）

尽管大语言模型（LLMs）通过广泛的预训练展现了显著的能力，但在特定领域的泛化和处理语言变异方面仍面临挑战。本文提出了一种测试时学习（TTL）范式，称为TLM，旨在利用无标签测试数据动态适应目标领域。我们提供了实证证据和理论见解，表明通过最小化输入困惑度可以提高LLMs的预测准确性。此外，我们引入了一种样本高效学习策略，重点选择高困惑度样本进行模型优化。最后，为了减轻灾难性遗忘并确保适应的稳定性，我们采用低秩适应（LoRA）进行轻量级模型更新。实验结果表明，TLM在领域知识适应方面比原始LLMs提升至少20%。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在特定领域适应性不足的问题，现有方法在处理无标签数据时面临困惑度高导致的预测不准确。

**核心思路**：论文提出通过最小化输入困惑度来优化模型性能，利用无标签测试数据进行自我监督学习，从而实现动态适应。

**技术框架**：整体流程包括数据输入、困惑度计算、样本选择和模型更新四个主要模块。首先计算无标签数据的困惑度，然后选择高困惑度样本进行模型优化，最后进行轻量级更新。

**关键创新**：最重要的创新在于引入了样本高效学习策略，主动选择高困惑度样本进行优化，这与传统方法的被动学习形成鲜明对比。

**关键设计**：采用低秩适应（LoRA）进行模型更新，避免全参数优化带来的灾难性遗忘，同时保留模型的原始知识。损失函数设计上侧重于困惑度最小化，以提升预测准确性。

## 📊 实验亮点

实验结果表明，TLM在领域知识适应方面的性能提升显著，较原始大语言模型提高至少20%。通过引入样本高效学习策略，模型在处理高困惑度样本时表现出更强的优化能力，验证了提出方法的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和领域特定的知识提取等。通过提升大语言模型在特定领域的适应能力，可以更好地满足行业需求，推动智能助手和自动化系统的发展，未来可能在教育、医疗和金融等多个领域产生深远影响。

## 📄 摘要（原文）

> While Large Language Models (LLMs) have exhibited remarkable emergent capabilities through extensive pre-training, they still face critical limitations in generalizing to specialized domains and handling diverse linguistic variations, known as distribution shifts. In this paper, we propose a Test-Time Learning (TTL) paradigm for LLMs, namely TLM, which dynamically adapts LLMs to target domains using only unlabeled test data during testing. Specifically, we first provide empirical evidence and theoretical insights to reveal that more accurate predictions from LLMs can be achieved by minimizing the input perplexity of the unlabeled test data. Based on this insight, we formulate the Test-Time Learning process of LLMs as input perplexity minimization, enabling self-supervised enhancement of LLM performance. Furthermore, we observe that high-perplexity samples tend to be more informative for model optimization. Accordingly, we introduce a Sample Efficient Learning Strategy that actively selects and emphasizes these high-perplexity samples for test-time updates. Lastly, to mitigate catastrophic forgetting and ensure adaptation stability, we adopt Low-Rank Adaptation (LoRA) instead of full-parameter optimization, which allows lightweight model updates while preserving more original knowledge from the model. We introduce the AdaptEval benchmark for TTL and demonstrate through experiments that TLM improves performance by at least 20% compared to original LLMs on domain knowledge adaptation.

