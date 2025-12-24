---
layout: default
title: "Relic: Enhancing Reward Model Generalization for Low-Resource Indic Languages with Few-Shot Examples"
---

# Relic: Enhancing Reward Model Generalization for Low-Resource Indic Languages with Few-Shot Examples

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16502" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16502v1</a>
  <a href="https://arxiv.org/pdf/2506.16502.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16502v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16502v1', 'Relic: Enhancing Reward Model Generalization for Low-Resource Indic Languages with Few-Shot Examples')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Soumya Suvra Ghosal, Vaibhav Singh, Akash Ghosh, Soumyabrata Pal, Subhadip Baidya, Sriparna Saha, Dinesh Manocha

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-19

---

## 💡 一句话要点

**提出RELIC框架以解决低资源印地语奖励模型泛化问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `奖励模型` `低资源语言` `上下文学习` `成对排名` `语言模型`

## 📋 核心要点

1. 现有的多语言奖励模型主要依赖高资源语言的数据，导致低资源印地语的奖励信号不可靠。
2. RELIC框架通过成对排名目标训练检索器，从高资源语言中选择有效的上下文示例，提升低资源语言的奖励模型性能。
3. 在Bodo语言的实验中，RELIC在准确性上分别比零-shot提示和现有方法提高了12.81%和10.13%。

## 📝 摘要（中文）

奖励模型对于将大型语言模型（LLMs）与人类偏好对齐至关重要。然而，大多数开源多语言奖励模型主要在高资源语言的偏好数据集上训练，导致在低资源印地语中产生不可靠的奖励信号。收集这些语言的大规模高质量偏好数据代价高昂，使得基于偏好的训练方法不切实际。为了解决这一挑战，本文提出了RELIC，一个用于低资源印地语奖励建模的新型上下文学习框架。RELIC通过成对排名目标训练检索器，从辅助高资源语言中选择最有效的上下文示例，以突出偏好和非偏好响应之间的区别。大量实验表明，RELIC显著提高了低资源印地语的奖励模型准确性，超越了现有示例选择方法。

## 🔬 方法详解

**问题定义**：本文旨在解决低资源印地语奖励模型泛化能力不足的问题。现有方法主要依赖于高资源语言的偏好数据，导致在低资源语言中效果不佳。

**核心思路**：RELIC框架通过成对排名目标训练检索器，选择高资源语言中的上下文示例，以有效区分偏好和非偏好响应，从而提升低资源语言的奖励模型性能。

**技术框架**：RELIC的整体架构包括数据检索模块和奖励模型训练模块。首先，利用检索器从高资源语言中选择示例，然后将这些示例用于训练低资源语言的奖励模型。

**关键创新**：RELIC的主要创新在于通过成对排名的方式选择上下文示例，这种方法在低资源语言的奖励建模中显著提高了准确性，与传统的示例选择方法相比具有本质区别。

**关键设计**：在参数设置上，RELIC使用了特定的损失函数来优化检索器的选择能力，并采用了适合低资源语言的网络结构，以确保模型的有效性和泛化能力。

## 📊 实验亮点

在实验中，RELIC在Bodo语言的奖励模型上取得了显著提升，准确性比零-shot提示提高了12.81%，比现有的示例选择方法提高了10.13%。这些结果表明RELIC在低资源语言奖励建模中的有效性和优越性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、机器翻译和人机交互等。RELIC框架能够有效提升低资源语言的模型性能，具有重要的实际价值，未来可为更多低资源语言的研究提供支持，促进语言技术的公平性和可及性。

## 📄 摘要（原文）

> Reward models are essential for aligning large language models (LLMs) with human preferences. However, most open-source multilingual reward models are primarily trained on preference datasets in high-resource languages, resulting in unreliable reward signals for low-resource Indic languages. Collecting large-scale, high-quality preference data for these languages is prohibitively expensive, making preference-based training approaches impractical. To address this challenge, we propose RELIC, a novel in-context learning framework for reward modeling in low-resource Indic languages. RELIC trains a retriever with a pairwise ranking objective to select in-context examples from auxiliary high-resource languages that most effectively highlight the distinction between preferred and less-preferred responses. Extensive experiments on three preference datasets- PKU-SafeRLHF, WebGPT, and HH-RLHF-using state-of-the-art open-source reward models demonstrate that RELIC significantly improves reward model accuracy for low-resource Indic languages, consistently outperforming existing example selection methods. For example, on Bodo-a low-resource Indic language-using a LLaMA-3.2-3B reward model, RELIC achieves a 12.81% and 10.13% improvement in accuracy over zero-shot prompting and state-of-the-art example selection method, respectively.

