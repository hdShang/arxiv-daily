---
layout: default
title: Linear Representation Transferability Hypothesis: Leveraging Small Models to Steer Large Models
---

# Linear Representation Transferability Hypothesis: Leveraging Small Models to Steer Large Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00653" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00653v3</a>
  <a href="https://arxiv.org/pdf/2506.00653.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00653v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00653v3', 'Linear Representation Transferability Hypothesis: Leveraging Small Models to Steer Large Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Femi Bello, Anubrata Das, Fanzhi Zeng, Fangcong Yin, Liu Leqi

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-05-31 (更新: 2025-06-04)

---

## 💡 一句话要点

**提出线性表示可转移假设以引导大模型行为**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `表示学习` `知识转移` `仿射变换` `模型蒸馏` `自然语言处理` `计算机视觉` `深度学习`

## 📋 核心要点

1. 现有方法在不同规模的模型之间缺乏有效的表示对齐机制，导致小模型的知识无法有效转移到大模型。
2. 论文提出线性表示可转移假设，认为不同模型的表示空间之间存在仿射变换，从而实现小模型对大模型的引导。
3. 实验结果表明，学习到的仿射映射能够有效保持引导向量的语义效果，支持了LRT假设的有效性。

## 📝 摘要（中文）

本文假设相似架构的神经网络在相似数据上训练时，能够学习到与学习任务相关的共享表示。我们扩展了这一概念框架，提出了线性表示可转移（LRT）假设，即不同模型的表示空间之间存在仿射变换。通过学习不同规模模型的隐藏状态之间的仿射映射，我们验证了小模型的引导向量在转移到大模型时能够保持其语义效果。这一发现表明，小模型学习的表示可以有效引导大模型的行为，并为理解不同规模模型之间的表示对齐提供了新的方向。

## 🔬 方法详解

**问题定义**：本文旨在解决不同规模模型之间表示对齐的问题。现有方法未能有效利用小模型的知识来指导大模型的行为，导致知识转移效率低下。

**核心思路**：论文提出线性表示可转移假设，认为不同模型的表示空间之间存在仿射变换。通过学习这些变换，可以将小模型的引导向量有效转移到大模型中，从而实现知识的有效利用。

**技术框架**：整体架构包括模型训练、隐藏状态提取、仿射映射学习和引导向量转移四个主要模块。首先训练不同规模的模型，然后提取其隐藏状态，接着学习隐藏状态之间的仿射映射，最后验证引导向量的转移效果。

**关键创新**：最重要的技术创新在于提出了线性表示可转移假设，并通过实验证实了小模型的引导向量在大模型中保持语义效果的能力。这一创新为模型间的知识转移提供了新的理论基础。

**关键设计**：在实验中，采用了特定的损失函数来优化仿射映射的学习，并设计了适应不同规模模型的网络结构，以确保引导向量的有效转移。

## 📊 实验亮点

实验结果显示，学习到的仿射映射能够有效保持引导向量的语义效果，支持了LRT假设的有效性。具体而言，转移后的引导向量在大模型中的表现与小模型相似，验证了小模型知识转移的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、计算机视觉等需要模型知识转移的场景。通过有效利用小模型的知识，可以在资源受限的情况下提升大模型的性能，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> It has been hypothesized that neural networks with similar architectures trained on similar data learn shared representations relevant to the learning task. We build on this idea by extending the conceptual framework where representations learned across models trained on the same data can be expressed as linear combinations of a \emph{universal} set of basis features. These basis features underlie the learning task itself and remain consistent across models, regardless of scale. From this framework, we propose the \textbf{Linear Representation Transferability (LRT)} Hypothesis -- that there exists an affine transformation between the representation spaces of different models. To test this hypothesis, we learn affine mappings between the hidden states of models of different sizes and evaluate whether steering vectors -- directions in hidden state space associated with specific model behaviors -- retain their semantic effect when transferred from small to large language models using the learned mappings. We find strong empirical evidence that such affine mappings can preserve steering behaviors. These findings suggest that representations learned by small models can be used to guide the behavior of large models, and that the LRT hypothesis may be a promising direction on understanding representation alignment across model scales.

