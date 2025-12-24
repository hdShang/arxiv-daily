---
layout: default
title: Enhancing Multimodal Continual Instruction Tuning with BranchLoRA
---

# Enhancing Multimodal Continual Instruction Tuning with BranchLoRA

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.02041" class="toolbar-btn" target="_blank">📄 arXiv: 2506.02041v1</a>
  <a href="https://arxiv.org/pdf/2506.02041.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.02041v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.02041v1', 'Enhancing Multimodal Continual Instruction Tuning with BranchLoRA')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Duzhen Zhang, Yong Ren, Zhong-Zhi Li, Yahan Yu, Jiahua Dong, Chenxing Li, Zhilong Ji, Jinfeng Bai

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-31

**备注**: Accepted by ACL2025 Main Conference

---

## 💡 一句话要点

**提出BranchLoRA以解决多模态持续指令调优中的灾难性遗忘问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态持续指令调优` `灾难性遗忘` `BranchLoRA` `混合专家` `任务特定路由器` `灵活调优机制` `多模态大型语言模型`

## 📋 核心要点

1. 现有的多模态持续指令调优方法容易受到灾难性遗忘的影响，导致模型性能随时间下降。
2. 本文提出了BranchLoRA框架，通过引入调优-冻结机制和任务特定路由器，提升了模型的效率和性能。
3. 实验结果显示，BranchLoRA在最新的MCIT基准上显著超越了MoELoRA，且在不同规模的MLLM中均表现优越。

## 📝 摘要（中文）

多模态持续指令调优（MCIT）旨在不断微调多模态大型语言模型（MLLMs），以与人类意图在连续任务中保持一致。现有方法通常依赖于混合专家（MoE）LoRA框架来保留先前的指令对齐，但由于简单求和聚合所有LoRA块，容易导致灾难性遗忘（CF），从而影响长期性能。本文识别了MoELoRA框架在MCIT背景下的关键参数低效问题，并提出了BranchLoRA，一个不对称框架，以提高效率和性能。为减轻CF，BranchLoRA引入了灵活的调优-冻结机制，使分支能够专注于任务内知识，同时促进任务间协作。此外，逐步引入任务特定路由器，确保随着时间的推移实现最佳分支分配，而不是偏向最近的任务。通过引入任务选择器，自动将测试输入路由到适当的路由器，无需任务身份。大量实验表明，BranchLoRA显著优于MoELoRA，并在各种MLLM规模上保持其优势。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态持续指令调优中的灾难性遗忘问题。现有的MoELoRA框架通过简单求和聚合LoRA块，导致模型在处理新任务时遗忘旧任务的信息，影响长期性能。

**核心思路**：提出BranchLoRA框架，通过引入灵活的调优-冻结机制，使得不同分支能够专注于特定任务的知识，同时促进任务间的协作，从而减轻灾难性遗忘的影响。

**技术框架**：BranchLoRA的整体架构包括多个分支，每个分支专注于特定任务的知识，并通过任务特定路由器进行动态路由。任务选择器负责在推理时自动将输入路由到相应的分支，无需显式的任务身份信息。

**关键创新**：BranchLoRA的主要创新在于其不对称的框架设计和灵活的调优-冻结机制，与现有的MoELoRA方法相比，能够更有效地管理任务间的知识共享与保留。

**关键设计**：在设计中，BranchLoRA引入了任务特定的路由器，以确保随着时间的推移实现最佳的分支分配。此外，调优-冻结机制的灵活性允许模型在不同任务间进行有效的知识迁移，减少了灾难性遗忘的风险。

## 📊 实验亮点

在最新的MCIT基准上，BranchLoRA显著优于MoELoRA，具体表现为在不同规模的多模态大型语言模型中，性能提升幅度达到XX%（具体数据未知），有效减少了灾难性遗忘现象。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、自动化客服和多模态交互系统等，能够有效提升模型在连续任务中的表现，满足用户不断变化的需求。未来，BranchLoRA可能在更多复杂的多模态任务中展现出更大的价值，推动人工智能的智能化进程。

## 📄 摘要（原文）

> Multimodal Continual Instruction Tuning (MCIT) aims to finetune Multimodal Large Language Models (MLLMs) to continually align with human intent across sequential tasks. Existing approaches often rely on the Mixture-of-Experts (MoE) LoRA framework to preserve previous instruction alignments. However, these methods are prone to Catastrophic Forgetting (CF), as they aggregate all LoRA blocks via simple summation, which compromises performance over time. In this paper, we identify a critical parameter inefficiency in the MoELoRA framework within the MCIT context. Based on this insight, we propose BranchLoRA, an asymmetric framework to enhance both efficiency and performance. To mitigate CF, we introduce a flexible tuning-freezing mechanism within BranchLoRA, enabling branches to specialize in intra-task knowledge while fostering inter-task collaboration. Moreover, we incrementally incorporate task-specific routers to ensure an optimal branch distribution over time, rather than favoring the most recent task. To streamline inference, we introduce a task selector that automatically routes test inputs to the appropriate router without requiring task identity. Extensive experiments on the latest MCIT benchmark demonstrate that BranchLoRA significantly outperforms MoELoRA and maintains its superiority across various MLLM sizes.

