---
layout: default
title: "CAC-CoT: Connector-Aware Compact Chain-of-Thought for Efficient Reasoning Data Synthesis Across Dual-System Cognitive Tasks"
---

# CAC-CoT: Connector-Aware Compact Chain-of-Thought for Efficient Reasoning Data Synthesis Across Dual-System Cognitive Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18743" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18743v2</a>
  <a href="https://arxiv.org/pdf/2508.18743.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18743v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18743v2', 'CAC-CoT: Connector-Aware Compact Chain-of-Thought for Efficient Reasoning Data Synthesis Across Dual-System Cognitive Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sunguk Choi, Yonghoon Kwon, Heondeuk Lee

**分类**: cs.AI, cs.CL

**发布日期**: 2025-08-26 (更新: 2025-09-15)

**备注**: Accepted at EMNLP 2025 findings

---

## 💡 一句话要点

**提出CAC-CoT以提升双系统认知任务中的推理效率**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长链推理` `连接器感知` `推理效率` `大型语言模型` `系统-1任务`

## 📋 核心要点

1. 现有的长链推理方法在处理快速直观的任务时，往往导致性能下降和效率低下。
2. CAC-CoT方法通过限制推理过程中的连接短语数量，旨在引导模型生成更简洁的推理链。
3. 实验结果显示，CAC-CoT在多个基准测试中显著提升了性能，尤其是在系统-1任务中表现优异。

## 📝 摘要（中文）

长链推理（CoT）提示有助于大型语言模型（LLMs）解决复杂问题，但过长的推理链会在快速直观的“系统-1”任务中降低性能。本文提出了连接器感知紧凑链推理（CAC-CoT）方法，限制推理使用固定的连接短语，从而引导模型生成简洁且结构良好的解释。尽管方法简单，但在通用LLMs上实现了高质量的训练效果。CAC-CoT在GSM8K上达到了约85%的准确率，在GPQA（系统-2）上约为40%，同时在S1-Bench（系统-1）上也达到了约85%，超出基线20%以上。其推理链平均约300个标记，约为基线长度的三分之一，在不损失准确性的情况下提高了效率。

## 🔬 方法详解

**问题定义**：本文旨在解决长链推理在快速直观任务中性能下降的问题。现有方法在处理此类任务时，推理链过长导致效率低下。

**核心思路**：CAC-CoT方法通过限制推理中使用的连接短语数量，促使模型生成简洁且结构化的推理链，从而提高推理效率。

**技术框架**：CAC-CoT的整体架构包括输入处理、连接短语选择、推理生成和输出优化四个主要模块。模型首先接收输入，然后选择固定的连接短语，最后生成推理结果并进行优化。

**关键创新**：CAC-CoT的主要创新在于其连接器感知的设计，通过限制推理链的长度，显著提高了在系统-1任务中的表现，与传统方法相比，提供了更高的效率和准确性。

**关键设计**：在参数设置上，CAC-CoT使用了固定的连接短语集，损失函数设计为优化推理链的简洁性和准确性，网络结构上则采用了通用的LLM架构，确保了方法的广泛适用性。

## 📊 实验亮点

CAC-CoT在GSM8K上达到了约85%的准确率，在GPQA上约为40%，在S1-Bench上也达到了约85%，超出基线20%以上。其推理链平均长度约为300个标记，显著提高了推理效率。

## 🎯 应用场景

CAC-CoT方法在教育、智能问答和人机交互等领域具有广泛的应用潜力。通过提高推理效率，该方法能够帮助用户更快速地获取信息，提升决策质量，未来可能在智能助手和自动化系统中发挥重要作用。

## 📄 摘要（原文）

> Long chain-of-thought (CoT) prompting helps Large Language Models (LLMs) solve difficult problems, but very long traces often slow or even degrade performance on fast, intuitive "System-1" tasks. We introduce Connector-Aware Compact CoT (CAC-CoT) -- a method that deliberately restricts reasoning to a small, fixed set of connector phrases, steering the model toward concise and well -- structured explanations. Despite its simplicity, our synthetic method with general-purpose LLMs yields a high-quality training quality. CAC-CoT achieves approximately 85% on GSM8K and approximately 40% on GPQA (System-2) while also achieving approximately 85% on S1-Bench (System-1), surpassing the baseline by over 20%. Its reasoning traces average approximately 300 tokens(ART), about one-third the length of baseline traces, delivering higher efficiency without loss of accuracy.

