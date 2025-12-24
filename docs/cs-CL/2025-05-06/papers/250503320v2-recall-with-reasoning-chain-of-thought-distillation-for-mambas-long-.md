---
layout: default
title: Recall with Reasoning: Chain-of-Thought Distillation for Mamba's Long-Context Memory and Extrapolation
---

# Recall with Reasoning: Chain-of-Thought Distillation for Mamba's Long-Context Memory and Extrapolation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03320" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03320v2</a>
  <a href="https://arxiv.org/pdf/2505.03320.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03320v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03320v2', 'Recall with Reasoning: Chain-of-Thought Distillation for Mamba\'s Long-Context Memory and Extrapolation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junyu Ma, Tianqing Fang, Zhisong Zhang, Hongming Zhang, Haitao Mi, Dong Yu

**分类**: cs.CL

**发布日期**: 2025-05-06 (更新: 2025-06-03)

---

## 💡 一句话要点

**提出Recall with Reasoning方法以提升Mamba的长上下文记忆能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长上下文记忆` `链式思维` `蒸馏训练` `自然语言处理` `模型微调`

## 📋 核心要点

1. 现有方法在处理超长序列时性能下降，无法充分利用Mamba的长上下文潜力。
2. 提出的RwR方法通过蒸馏链式思维总结，增强Mamba在长上下文中的回忆和推理能力。
3. 实验结果显示，RwR在长上下文任务上显著优于对比基线，且短上下文性能未受影响。

## 📝 摘要（中文）

Mamba在理论上具备无限上下文潜力，但在实际应用中，当序列长度远超训练长度时，其性能受到限制。本研究通过一种简单而有效的方法Recall with Reasoning（RwR），探索解锁Mamba的长上下文记忆能力。RwR通过从教师模型中蒸馏链式思维（CoT）总结，将这些总结作为CoT提示预置于微调过程中，教会Mamba主动回忆和推理长上下文。实验结果表明，RwR在LONGMEMEVAL和HELMET数据集上显著提升了Mamba的长上下文性能，相较于类似预训练条件下的Transformer/混合基线，同时保持了短上下文能力，且无需对架构进行更改。

## 🔬 方法详解

**问题定义**：本论文旨在解决Mamba在处理超长序列时性能不足的问题。现有方法在面对超过训练长度的序列时，无法有效利用其长上下文记忆能力，导致性能下降。

**核心思路**：论文提出的RwR方法通过蒸馏链式思维总结，作为提示引导Mamba进行长上下文的回忆和推理。这种设计旨在提升模型在长上下文任务中的表现，同时保持其短上下文能力。

**技术框架**：RwR方法的整体架构包括两个主要阶段：首先，从教师模型中提取链式思维总结；其次，在微调过程中将这些总结作为提示输入Mamba模型。该方法不需要对Mamba的架构进行任何修改。

**关键创新**：RwR的核心创新在于通过链式思维总结的蒸馏，使得模型能够在长上下文中进行有效的推理和回忆。这一方法与传统的上下文处理方式有本质区别，后者往往依赖于固定的上下文窗口。

**关键设计**：在RwR中，关键的设计包括如何选择和生成链式思维总结，以及在微调过程中如何有效地将这些总结整合进模型输入。损失函数的设计也确保了模型在长上下文和短上下文任务上的平衡性能。

## 📊 实验亮点

实验结果表明，RwR方法在LONGMEMEVAL和HELMET数据集上显著提升了Mamba的长上下文性能，超过了同类Transformer和混合基线，且在短上下文任务中保持了原有的性能水平，展示了RwR的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和信息检索等。通过提升模型在长上下文任务中的表现，RwR方法可以在更复杂的场景中应用，如长篇文章理解和多轮对话生成，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Mamba's theoretical infinite-context potential is limited in practice when sequences far exceed training lengths. This work explores unlocking Mamba's long-context memory ability by a simple-yet-effective method, Recall with Reasoning (RwR), by distilling chain-of-thought (CoT) summarization from a teacher model. Specifically, RwR prepends these summarization as CoT prompts during fine-tuning, teaching Mamba to actively recall and reason over long contexts. Experiments on LONGMEMEVAL and HELMET show RwR boosts Mamba's long-context performance against comparable Transformer/hybrid baselines under similar pretraining conditions, while preserving short-context capabilities, all without architectural changes.

