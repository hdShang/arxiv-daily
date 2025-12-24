---
layout: default
title: "seq-JEPA: Autoregressive Predictive Learning of Invariant-Equivariant World Models"
---

# seq-JEPA: Autoregressive Predictive Learning of Invariant-Equivariant World Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03176" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03176v2</a>
  <a href="https://arxiv.org/pdf/2505.03176.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03176v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03176v2', 'seq-JEPA: Autoregressive Predictive Learning of Invariant-Equivariant World Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hafez Ghaemi, Eilif Muller, Shahab Bakhtiari

**分类**: cs.CV, cs.AI, cs.LG

**发布日期**: 2025-05-06 (更新: 2025-05-22)

---

## 💡 一句话要点

**提出seq-JEPA以解决自监督学习中的表示灵活性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `自监督学习` `视觉表示` `等变性` `不变性` `Transformer` `序列建模` `路径整合`

## 📋 核心要点

1. 现有自监督学习方法在学习视觉表示时，往往面临高层不变性与细粒度等变性任务之间的性能权衡问题。
2. 本文提出的seq-JEPA框架通过引入架构归纳偏置，能够同时学习对变换等变和不变的表示，避免了双重预测器的依赖。
3. 实验证明，seq-JEPA在等变和不变基准上均表现优异，且在路径整合和预测学习等任务中展现出强大的能力。

## 📝 摘要（中文）

当前的自监督算法通常依赖于数据增强和掩蔽等变换来学习视觉表示。这些方法通过对图像的两个视图施加不变性或等变性来实现。然而，这种主流的双视图范式限制了所学表示在下游任务中的灵活性，导致高层不变性任务与细粒度等变性任务之间的性能权衡。本文提出了seq-JEPA，一个世界建模框架，通过引入架构归纳偏置到联合嵌入预测架构中，解决了这一权衡问题。seq-JEPA同时学习了两个架构上分隔的表示：一个对指定变换等变，另一个对其不变。该模型处理不同视图的短序列，并通过变换嵌入来预测下一个观察的表示。实验证明，seq-JEPA在等变和不变基准上均表现出色，且在需要聚合观察序列的任务中表现尤为突出。

## 🔬 方法详解

**问题定义**：本文旨在解决现有自监督学习方法在处理视觉表示时的灵活性不足问题，尤其是在高层不变性与细粒度等变性任务之间的性能权衡。

**核心思路**：seq-JEPA通过引入架构归纳偏置，设计了一个能够同时学习等变和不变表示的框架，避免了对双重等变性预测器或损失项的依赖。

**技术框架**：该模型处理不同视图的短序列，每个编码视图与产生下一个观察的相对变换嵌入连接。经过Transformer编码器后，输出一个聚合表示，并通过预测头条件化该表示以预测下一个观察的表示。

**关键创新**：seq-JEPA的主要创新在于其架构设计，能够在不牺牲等变性和不变性之间的性能的情况下，学习到两种不同的表示。这与现有方法的双视图范式形成了显著对比。

**关键设计**：模型通过处理视图-动作对来学习，采用Transformer编码器进行聚合，关键参数设置和损失函数设计未在摘要中详细说明，具体细节未知。

## 📊 实验亮点

在实验中，seq-JEPA在等变和不变基准上均表现出色，具体性能数据未在摘要中提供。该模型在路径整合和预测学习等任务中展现了强大的能力，显示出其在处理观察序列方面的优势。

## 🎯 应用场景

seq-JEPA的研究成果在多个领域具有潜在应用价值，包括机器人导航、视频理解和人机交互等。其能够有效处理序列数据的能力，使其在需要聚合多次观察的信息的任务中表现出色，未来可能推动自监督学习在更复杂场景中的应用。

## 📄 摘要（原文）

> Current self-supervised algorithms commonly rely on transformations such as data augmentation and masking to learn visual representations. This is achieved by enforcing invariance or equivariance with respect to these transformations after encoding two views of an image. This dominant two-view paradigm often limits the flexibility of learned representations for downstream adaptation by creating performance trade-offs between high-level invariance-demanding tasks such as image classification and more fine-grained equivariance-related tasks. In this work, we proposes \emph{seq-JEPA}, a world modeling framework that introduces architectural inductive biases into joint-embedding predictive architectures to resolve this trade-off. Without relying on dual equivariance predictors or loss terms, seq-JEPA simultaneously learns two architecturally segregated representations: one equivariant to specified transformations and another invariant to them. To do so, our model processes short sequences of different views (observations) of inputs. Each encoded view is concatenated with an embedding of the relative transformation (action) that produces the next observation in the sequence. These view-action pairs are passed through a transformer encoder that outputs an aggregate representation. A predictor head then conditions this aggregate representation on the upcoming action to predict the representation of the next observation. Empirically, seq-JEPA demonstrates strong performance on both equivariant and invariant benchmarks without sacrificing one for the other. Furthermore, it excels at tasks that inherently require aggregating a sequence of observations, such as path integration across actions and predictive learning across eye movements.

