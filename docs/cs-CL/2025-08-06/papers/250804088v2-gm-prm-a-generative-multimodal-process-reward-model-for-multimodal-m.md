---
layout: default
title: "GM-PRM: A Generative Multimodal Process Reward Model for Multimodal Mathematical Reasoning"
---

# GM-PRM: A Generative Multimodal Process Reward Model for Multimodal Mathematical Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04088" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04088v2</a>
  <a href="https://arxiv.org/pdf/2508.04088.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04088v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04088v2', 'GM-PRM: A Generative Multimodal Process Reward Model for Multimodal Mathematical Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jianghangfan Zhang, Yibo Yan, Kening Zheng, Xin Zou, Song Dai, Xuming Hu

**分类**: cs.CL

**发布日期**: 2025-08-06 (更新: 2025-08-07)

---

## 💡 一句话要点

**提出GM-PRM以解决多模态数学推理中的错误纠正问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态推理` `过程奖励模型` `数学推理` `错误纠正` `生成模型` `智能教育` `深度学习`

## 📋 核心要点

1. 现有的多模态过程奖励模型在复杂数学推理中仅能识别错误，无法进行有效的纠正，导致推理能力受限。
2. GM-PRM通过将过程奖励模型转变为主动推理协作者，提供细致的推理步骤分析，并具备纠正错误的能力。
3. 实验结果显示，GM-PRM在多个基准测试中表现优异，显著提升了策略模型的性能，且数据效率高，仅需20K样本进行训练。

## 📝 摘要（中文）

多模态大型语言模型（MLLMs）在复杂的多步骤数学推理中表现出色，但在视觉感知或逻辑推理的微小错误上常常导致完全失败。现有的过程奖励模型（PRMs）只能作为二元验证器，无法纠正错误且缺乏解释能力。为了解决这些不足，本文提出了生成多模态过程奖励模型（GM-PRM），将PRM从被动评判者转变为主动推理协作者。GM-PRM不仅提供每个推理步骤的细致分析，还能生成纠正错误步骤的版本，从而引导策略模型朝更有前景的推理轨迹发展。实验表明，GM-PRM在多个多模态数学基准测试中取得了最先进的结果，显著提升了策略模型的性能，且仅需20K样本的训练数据。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态数学推理中存在的错误识别与纠正问题。现有的过程奖励模型（PRMs）只能作为被动的错误验证工具，无法提供有效的纠正方案，导致推理过程中的错误无法得到修正。

**核心思路**：GM-PRM的核心思想是将过程奖励模型转变为主动的推理协作者，通过生成每个推理步骤的细致分析，并在识别到错误时生成纠正版本，从而引导策略模型朝更优的推理路径发展。

**技术框架**：GM-PRM的整体架构包括三个主要模块：推理步骤分析模块、错误识别与纠正模块，以及基于生成的纠正信息引导策略模型的推理轨迹模块。每个模块协同工作，确保推理过程的高效性与准确性。

**关键创新**：GM-PRM的最大创新在于其纠正能力，能够在识别到错误后生成纠正版本，区别于传统的PRMs仅能进行错误识别。这种主动纠正机制显著提升了推理的准确性和多样性。

**关键设计**：在设计上，GM-PRM采用了细粒度的损失函数，以确保每个推理步骤的意图、视觉对齐和逻辑合理性都能得到有效评估。同时，网络结构经过优化，以提高生成纠正版本的质量和效率。

## 📊 实验亮点

在多个多模态数学基准测试中，GM-PRM实现了最先进的结果，策略模型性能显著提升，数据效率高，仅需20K样本进行训练。与传统方法相比，GM-PRM在推理准确性和多样性上均有显著改善。

## 🎯 应用场景

GM-PRM的研究成果在教育、自动化推理系统和智能辅导工具等领域具有广泛的应用潜力。通过提升多模态数学推理的准确性和效率，该模型能够为学生提供更有效的学习支持，并推动智能系统在复杂推理任务中的应用。

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) demonstrate remarkable capabilities but often struggle with complex, multi-step mathematical reasoning, where minor errors in visual perception or logical deduction can lead to complete failure. While Process Reward Models (PRMs) offer step-by-step supervision, existing multimodal PRMs are limited to being binary verifiers that can identify but not correct errors, offering little explanatory power. To address these deficiencies, we introduce the Generative Multimodal Process Reward Model (GM-PRM), a novel paradigm that transforms the PRM from a passive judge into an active reasoning collaborator. Instead of a simple scalar score, GM-PRM provides a fine-grained, interpretable analysis of each reasoning step, evaluating its step intent, visual alignment, and logical soundness. More critically, GM-PRM is trained to generate a corrected version of the first erroneous step it identifies. This unique corrective capability enables our new test-time inference strategy, Refined Best-of-N (Refined-BoN). This framework actively enhances solution quality by using the PRM's generated correction to guide the policy model toward a more promising reasoning trajectory, thereby improving the diversity and correctness of the solution pool. We demonstrate that GM-PRM achieves state-of-the-art results on multiple multimodal math benchmarks, significantly boosting policy model performance with remarkable data efficiency, requiring only a 20K-sample training dataset. Our code will be released upon acceptance.

