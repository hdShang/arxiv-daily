---
layout: default
title: Rotary Masked Autoencoders are Versatile Learners
---

# Rotary Masked Autoencoders are Versatile Learners

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20535" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20535v2</a>
  <a href="https://arxiv.org/pdf/2505.20535.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20535v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20535v2', 'Rotary Masked Autoencoders are Versatile Learners')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Uros Zivanovic, Serafina Di Gioia, Andre Scaffidi, Martín de los Rios, Gabriella Contardo, Roberto Trotta

**分类**: cs.LG

**发布日期**: 2025-05-26 (更新: 2025-11-08)

**备注**: NeurIPS 2025 Camera Ready

---

## 💡 一句话要点

**提出Rotary Masked Autoencoder以解决时间序列学习问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `时间序列学习` `自注意力机制` `多模态学习` `深度学习` `表示学习`

## 📋 核心要点

1. 现有的Transformer方法在处理不规则时间序列时需要特殊化架构，导致计算复杂性增加。
2. RoMAE通过引入Rotary Positional Embedding，扩展了Masked Autoencoder，支持多维连续位置的学习。
3. RoMAE在多种模态上表现优异，尤其在复杂数据集上超越了专门的时间序列架构。

## 📝 摘要（中文）

现有的Transformer在处理不规则时间序列时通常需要对其基础架构进行特殊化，这会导致额外的计算开销和方法复杂性。本文提出了Rotary Masked Autoencoder（RoMAE），利用流行的Rotary Positional Embedding（RoPE）方法来处理连续位置。RoMAE是对Masked Autoencoder（MAE）的扩展，能够在不需要时间序列特定架构的情况下，实现多维连续位置的信息插值和表示学习。我们展示了RoMAE在多种模态下的表现，包括不规则和多变量时间序列、图像和音频，证明RoMAE在复杂数据集（如DESC ELAsTiCC挑战）上超越了专门的时间序列架构，同时在其他模态上保持了MAE的常规性能。此外，我们还研究了RoMAE重建嵌入连续位置的能力，表明在输入序列中包含学习到的嵌入会破坏RoPE的相对位置属性。

## 🔬 方法详解

**问题定义**：现有的Transformer架构在处理不规则时间序列时，通常需要进行特殊化设计，这导致了计算开销的增加和方法的复杂性。RoMAE旨在解决这一问题，提供一种通用的学习框架。

**核心思路**：RoMAE的核心思想是利用Rotary Positional Embedding（RoPE）来处理连续位置，从而避免时间序列特定的架构设计。通过这种方式，RoMAE能够在多种模态下进行有效的表示学习和插值。

**技术框架**：RoMAE的整体架构包括输入数据的嵌入、位置编码的引入、以及通过自注意力机制进行特征学习。该框架能够处理不规则和多维数据，保持了MAE的基本结构。

**关键创新**：RoMAE的主要创新在于其对Rotary Positional Embedding的应用，使得模型能够在不增加复杂性的情况下，处理多维连续位置的信息。这一设计与现有时间序列专用架构有本质区别。

**关键设计**：RoMAE在参数设置上保持了MAE的设计理念，采用了相似的损失函数和网络结构，同时引入了学习到的嵌入以增强模型的表达能力。

## 📊 实验亮点

RoMAE在DESC ELAsTiCC挑战数据集上表现优异，超越了专门设计的时间序列架构，展示了在复杂任务中的强大能力。实验结果表明，RoMAE在多模态学习中保持了MAE的性能，同时在特定任务上实现了显著提升。

## 🎯 应用场景

该研究的潜在应用领域包括金融市场分析、医疗健康监测、智能交通系统等，能够有效处理不规则和多维时间序列数据。RoMAE的通用性和高效性使其在实际应用中具有重要价值，未来可能推动更多领域的智能化发展。

## 📄 摘要（原文）

> Applying Transformers to irregular time-series typically requires specializations to their baseline architecture, which can result in additional computational overhead and increased method complexity. We present the Rotary Masked Autoencoder (RoMAE), which utilizes the popular Rotary Positional Embedding (RoPE) method for continuous positions. RoMAE is an extension to the Masked Autoencoder (MAE) that enables interpolation and representation learning with multidimensional continuous positional information while avoiding any time-series-specific architectural specializations. We showcase RoMAE's performance on a variety of modalities including irregular and multivariate time-series, images, and audio, demonstrating that RoMAE surpasses specialized time-series architectures on difficult datasets such as the DESC ELAsTiCC Challenge while maintaining MAE's usual performance across other modalities. In addition, we investigate RoMAE's ability to reconstruct the embedded continuous positions, demonstrating that including learned embeddings in the input sequence breaks RoPE's relative position property.

