---
layout: default
title: Product of Experts with LLMs: Boosting Performance on ARC Is a Matter of Perspective
---

# Product of Experts with LLMs: Boosting Performance on ARC Is a Matter of Perspective

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07859" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07859v2</a>
  <a href="https://arxiv.org/pdf/2505.07859.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07859v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07859v2', 'Product of Experts with LLMs: Boosting Performance on ARC Is a Matter of Perspective')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Daniel Franzen, Jan Disselhoff, David Hartmann

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-05-08 (更新: 2025-06-11)

**备注**: ICML 2025 camera-ready; 15 pages, 6 figures, 5 tables

---

## 💡 一句话要点

**提出基于专家模型的LLM方法以提升ARC-AGI表现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `抽象推理` `大型语言模型` `数据增强` `深度优先搜索` `模型评分`

## 📋 核心要点

1. ARC-AGI对LLMs的抽象推理能力提出了严峻挑战，现有方法在解决任务时表现不佳。
2. 本研究通过任务特定的数据增强和深度优先搜索算法，生成多样化的候选解，并利用LLM进行评分。
3. 实验结果显示，我们的方法在ARC-AGI评估集上取得71.6%的得分，展现出优于现有公开方法的性能。

## 📝 摘要（中文）

抽象与推理语料库（ARC-AGI）对大型语言模型（LLMs）提出了重大挑战，暴露了其在抽象推理能力上的局限性。本研究通过在训练、生成和评分阶段利用任务特定的数据增强，并采用深度优先搜索算法生成多样化的高概率候选解。同时，我们将LLM不仅用作生成器，还用作评分器，利用其输出概率选择最有前景的解。我们的方法在公共ARC-AGI评估集上取得了71.6%的得分（286.5/400解决任务），展示了在公开可用方法中的领先表现。尽管同时期的闭源工作报告了更高的得分，但我们的方法在透明性、可重复性和极低的推理成本方面具有显著优势，平均每个任务仅需约2美分的成本（假设Nvidia 4090 GPU的价格为36美分/小时）。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型在抽象与推理语料库（ARC-AGI）中的表现不足，现有方法在处理复杂推理任务时存在局限性，导致解决率低下。

**核心思路**：我们提出了一种结合任务特定数据增强和深度优先搜索的策略，利用LLM的生成和评分能力，提升模型的推理效果。通过这种方式，我们能够生成多样化且高概率的候选解，从而提高最终的解决率。

**技术框架**：整体方法分为三个主要阶段：数据增强、候选解生成和评分。首先，在训练阶段进行数据增强；其次，使用深度优先搜索算法生成候选解；最后，利用LLM对候选解进行评分，选择最优解。

**关键创新**：本研究的创新点在于将LLM同时作为生成器和评分器，利用其输出概率进行解的选择。这种双重角色的设计使得模型在透明性和可重复性上优于其他方法。

**关键设计**：在参数设置上，我们优化了数据增强的策略，并设计了高效的深度优先搜索算法。此外，LLM的输出概率被用作评分标准，确保选择的候选解具有较高的成功率。具体的损失函数和网络结构细节在论文中进行了详细描述。

## 📊 实验亮点

我们的实验结果显示，所提方法在ARC-AGI评估集上取得了71.6%的得分，成功解决了286.5个任务，显著优于现有公开方法。同时，推理成本仅为每个任务约2美分，展现出极高的性价比。

## 🎯 应用场景

该研究的潜在应用领域包括教育、智能问答系统和复杂决策支持等。通过提升LLM在抽象推理任务中的表现，可以为各类需要高水平推理能力的应用提供更可靠的支持，推动智能系统的进一步发展。

## 📄 摘要（原文）

> The Abstraction and Reasoning Corpus (ARC-AGI) poses a significant challenge for large language models (LLMs), exposing limitations in their abstract reasoning abilities. In this work, we leverage task-specific data augmentations throughout the training, generation, and scoring phases, and employ a depth-first search algorithm to generate diverse, high-probability candidate solutions. Furthermore, we utilize the LLM not only as a generator but also as a scorer, using its output probabilities to select the most promising solutions. Our method achieves a score of 71.6% (286.5/400 solved tasks) on the public ARC-AGI evaluation set, demonstrating state-of-the-art performance among publicly available approaches. While concurrent closed-source work has reported higher scores, our method distinguishes itself through its transparency, reproducibility, and remarkably low inference cost, averaging only around 2ct per task on readily available hardware (we assume a price of 36ct/hour for a Nvidia 4090 GPU).

