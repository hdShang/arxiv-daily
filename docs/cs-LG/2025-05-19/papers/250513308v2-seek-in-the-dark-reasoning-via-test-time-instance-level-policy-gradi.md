---
layout: default
title: Seek in the Dark: Reasoning via Test-Time Instance-Level Policy Gradient in Latent Space
---

# Seek in the Dark: Reasoning via Test-Time Instance-Level Policy Gradient in Latent Space

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13308" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13308v2</a>
  <a href="https://arxiv.org/pdf/2505.13308.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13308v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13308v2', 'Seek in the Dark: Reasoning via Test-Time Instance-Level Policy Gradient in Latent Space')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hengli Li, Chenxi Li, Tong Wu, Xuekai Zhu, Yuxuan Wang, Zhaoxin Yu, Eric Hanchen Jiang, Song-Chun Zhu, Zixia Jia, Ying Nian Wu, Zilong Zheng

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-05-19 (更新: 2025-10-30)

---

## 💡 一句话要点

**提出LatentSeek以提升大语言模型的推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `推理能力` `大型语言模型` `潜在空间` `策略梯度` `测试时适应` `自生成奖励` `实验基准`

## 📋 核心要点

1. 现有方法在推理能力上仍面临挑战，尤其是在训练算法和新数据的可用性方面。
2. 论文提出LatentSeek框架，通过潜在空间进行测试时实例级适应，利用策略梯度优化推理过程。
3. 实验结果显示LatentSeek在GSM8K、MATH-500等基准上超越了传统方法，且收敛速度快。

## 📝 摘要（中文）

推理能力是人类智能的核心组成部分，但在追求通用人工智能（AGI）的过程中，仍然对大型语言模型（LLMs）构成重大挑战。尽管模型性能在训练规模法则下有所提升，但训练算法（如灾难性遗忘）和新训练数据的有限可用性仍然是显著问题。为此，论文提出了一种新框架LatentSeek，通过在模型的潜在空间中进行测试时实例级适应（TTIA），利用策略梯度迭代更新潜在表示，借助自生成的奖励信号进行引导。实验结果表明，LatentSeek在多个推理基准上超越了强基线，且在平均复杂度问题上通常在几次迭代内收敛，显示出潜在空间测试时扩展的潜力。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型在推理能力上的不足，尤其是现有方法在训练过程中面临的灾难性遗忘和数据稀缺问题。

**核心思路**：论文提出的LatentSeek框架通过在潜在空间中进行测试时实例级适应，利用策略梯度方法迭代更新潜在表示，以自生成的奖励信号为指导，从而提升推理能力。

**技术框架**：LatentSeek的整体架构包括潜在空间的表示学习、策略梯度优化和自生成奖励信号的设计。该框架通过多次迭代来优化潜在表示，增强模型的推理能力。

**关键创新**：LatentSeek的主要创新在于其在潜在空间中进行推理的能力，与传统方法集中在标记空间的策略形成鲜明对比。这种方法更有效地遵循测试时扩展法则。

**关键设计**：在设计中，LatentSeek采用了特定的损失函数来优化潜在表示，并通过策略梯度方法实现高效的迭代更新，确保模型在推理任务中的快速收敛。具体的参数设置和网络结构细节在实验部分进行了详细描述。

## 📊 实验亮点

实验结果表明，LatentSeek在GSM8K、MATH-500和AIME2024等推理基准上均显著超越了传统的Chain-of-Thought提示和基于微调的方法，通常在几次迭代内收敛，显示出其在推理任务中的高效性和可扩展性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能问答系统和自动推理等。通过提升大型语言模型的推理能力，LatentSeek可以在更复杂的任务中提供更准确的结果，推动人工智能在实际应用中的发展与落地。

## 📄 摘要（原文）

> Reasoning ability, a core component of human intelligence, continues to pose a significant challenge for Large Language Models (LLMs) in the pursuit of AGI. Although model performance has improved under the training scaling law, significant challenges remain, particularly with respect to training algorithms, such as catastrophic forgetting, and the limited availability of novel training data. As an alternative, test-time scaling enhances reasoning performance by increasing test-time computation without parameter updating. Unlike prior methods in this paradigm focused on token space, we propose leveraging latent space for more effective reasoning and better adherence to the test-time scaling law. We introduce LatentSeek, a novel framework that enhances LLM reasoning through Test-Time Instance-level Adaptation (TTIA) within the model's latent space. Specifically, LatentSeek leverages policy gradient to iteratively update latent representations, guided by self-generated reward signals. LatentSeek is evaluated on a range of reasoning benchmarks, including GSM8K, MATH-500, and AIME2024, across multiple LLM architectures. Results show that LatentSeek consistently outperforms strong baselines, such as Chain-of-Thought prompting and fine-tuning-based methods. Furthermore, our analysis demonstrates that LatentSeek is highly efficient, typically converging within a few iterations for problems of average complexity, while also benefiting from additional iterations, thereby highlighting the potential of test-time scaling in the latent space. These findings position LatentSeek as a lightweight, scalable, and effective solution for enhancing the reasoning capabilities of LLMs.

