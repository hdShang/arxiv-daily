---
layout: default
title: Self-Reasoning Language Models: Unfold Hidden Reasoning Chains with Few Reasoning Catalyst
---

# Self-Reasoning Language Models: Unfold Hidden Reasoning Chains with Few Reasoning Catalyst

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14116" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14116v1</a>
  <a href="https://arxiv.org/pdf/2505.14116.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14116v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14116v1', 'Self-Reasoning Language Models: Unfold Hidden Reasoning Chains with Few Reasoning Catalyst')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongru Wang, Deng Cai, Wanjun Zhong, Shijue Huang, Jeff Z. Pan, Zeming Liu, Kam-Fai Wong

**分类**: cs.CL

**发布日期**: 2025-05-20

---

## 💡 一句话要点

**提出自推理语言模型以提升复杂推理任务的性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自推理模型` `长链推理` `自我训练` `推理催化剂` `复杂推理任务`

## 📋 核心要点

1. 现有方法在复杂推理任务中难以有效生成长链推理，导致性能受限。
2. 论文提出的自推理语言模型（SRLM）通过自我训练合成长链推理数据，提升模型推理能力。
3. SRLM在五个推理任务上实现了超过2.5分的平均提升，且多次采样时表现更佳，显示出显著的性能改进。

## 📝 摘要（中文）

推理时间扩展受到广泛关注，通过增加思维链的长度显著提升大型语言模型（LLMs）在复杂推理任务中的表现。这些更长的中间推理依据体现了人类认知中的多种元推理技能，如反思和分解，难以创建和获取。在本研究中，我们提出了自推理语言模型（SRLM），该模型能够合成更长的思维链数据，并通过自我训练迭代提升性能。通过结合少量示例（如1,000个样本）作为推理催化剂，SRLM不仅增强了模型的初始性能，还确保了后续迭代中更稳定和一致的改进。我们的SRLM在五个推理任务（MMLU、GSM8K、ARC-C、HellaSwag和BBH）上实现了超过2.5分的平均绝对提升，并在推理过程中通过多次采样获得更大改进，显示出SRLM在多样化和创造性推理路径上的优势。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型在复杂推理任务中生成长链推理的能力不足，现有方法难以有效创建和利用长链推理依据。

**核心思路**：提出自推理语言模型（SRLM），该模型通过自我训练合成更长的思维链数据，并利用少量示例作为推理催化剂，逐步提升模型性能。

**技术框架**：SRLM的整体架构包括数据合成模块、推理催化剂模块和自我训练模块。数据合成模块负责生成长链推理数据，推理催化剂模块提供示例以引导推理过程，自我训练模块则通过迭代优化模型性能。

**关键创新**：SRLM的主要创新在于其自我训练机制和推理催化剂的引入，使得模型能够在没有大量标注数据的情况下，逐步提升推理能力，区别于传统方法依赖于大量标注数据。

**关键设计**：在参数设置上，SRLM使用了特定的学习率和损失函数，以确保模型在自我训练过程中稳定收敛。同时，网络结构采用了Transformer架构，适应长链推理的需求。通过多次采样，模型能够探索更丰富的推理路径。

## 📊 实验亮点

SRLM在五个推理任务上实现了超过2.5分的平均绝对提升，且在64次采样时，平均提升达到7.89分，显示出其在复杂推理任务中的显著优势，超越了强基线模型。

## 🎯 应用场景

该研究的潜在应用领域包括教育、智能问答系统和自动化推理等。通过提升语言模型的推理能力，SRLM可以在复杂问题解决、知识推理和人机交互等场景中发挥重要作用，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Inference-time scaling has attracted much attention which significantly enhance the performance of Large Language Models (LLMs) in complex reasoning tasks by increasing the length of Chain-of-Thought. These longer intermediate reasoning rationales embody various meta-reasoning skills in human cognition, such as reflection and decomposition, being difficult to create and acquire. In this work, we introduce \textit{Self-Reasoning Language Model} (SRLM), where the model itself can synthesize longer CoT data and iteratively improve performance through self-training. By incorporating a few demonstration examples (i.e., 1,000 samples) on how to unfold hidden reasoning chains from existing responses, which act as a reasoning catalyst, we demonstrate that SRLM not only enhances the model's initial performance but also ensures more stable and consistent improvements in subsequent iterations. Our proposed SRLM achieves an average absolute improvement of more than $+2.5$ points across five reasoning tasks: MMLU, GSM8K, ARC-C, HellaSwag, and BBH on two backbone models. Moreover, it brings more improvements with more times of sampling during inference, such as absolute $+7.89$ average improvement with $64$ sampling times, revealing the in-depth, diverse and creative reasoning paths in SRLM against the strong baseline.

