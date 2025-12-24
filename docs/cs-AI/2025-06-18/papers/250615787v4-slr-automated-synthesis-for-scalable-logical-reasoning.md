---
layout: default
title: "SLR: Automated Synthesis for Scalable Logical Reasoning"
---

# SLR: Automated Synthesis for Scalable Logical Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15787" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15787v4</a>
  <a href="https://arxiv.org/pdf/2506.15787.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15787v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15787v4', 'SLR: Automated Synthesis for Scalable Logical Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lukas Helff, Ahmad Omar, Felix Friedrich, Antonia Wüst, Hikaru Shindo, Rupert Mitchell, Tim Woydt, Patrick Schramowski, Wolfgang Stammer, Kristian Kersting

**分类**: cs.AI, cs.CL, cs.LG

**发布日期**: 2025-06-18 (更新: 2025-08-06)

---

## 💡 一句话要点

**提出SLR框架以实现可扩展的逻辑推理自动合成**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `逻辑推理` `自动合成` `大型语言模型` `课程学习` `验证程序` `推理能力` `无监督学习`

## 📋 核心要点

1. 现有方法在逻辑推理任务中常常依赖人工注释，缺乏自动化和可扩展性，导致效率低下。
2. SLR框架通过自动合成任务提示、验证程序和真实规则，提供了一种无需人工干预的逻辑推理训练方法。
3. 实验结果表明，SLR显著提升了Llama-3-8B的推理准确率，并在计算成本上优于其他推理模型。

## 📝 摘要（中文）

我们介绍了SLR，一个端到端框架，用于通过可扩展的逻辑推理系统评估和训练大型语言模型（LLMs）。SLR根据用户的任务规范，自动合成（i）归纳推理任务的指令提示，（ii）可在模型输出上执行的验证程序，以提供可验证的奖励，以及（iii）潜在的真实规则。该过程完全自动化、可扩展，无需人工注释，并提供对任务难度的精确控制。使用SLR，我们创建了SLR-Bench，一个包含19,000个提示的基准，分为20个逐步增加关系、算术和递归复杂度的课程级别。大规模评估显示，当前的LLMs能够生成语法上有效的规则，但在正确的逻辑推理方面常常失败。最近的推理LLMs表现有所改善，但测试时计算成本极高，达到每1,000个提示超过300美元。最后，通过SLR的课程学习，Llama-3-8B在SLR-Bench上的准确率翻倍，以较低的计算成本达到了与Gemini-Flash-Thinking相当的水平。此外，这些推理能力在广泛的已建立基准上具有良好的泛化能力，突显了SLR在下游推理中的有效性。

## 🔬 方法详解

**问题定义**：论文旨在解决现有逻辑推理模型在任务合成和评估中的低效率和高成本问题，尤其是依赖人工注释的局限性。

**核心思路**：SLR框架通过自动化合成指令提示、验证程序和潜在规则，提供了一种高效的逻辑推理训练方式，避免了人工干预。

**技术框架**：SLR的整体架构包括三个主要模块：任务提示合成模块、验证程序生成模块和真实规则提取模块。用户输入任务规范后，系统自动生成相应的内容。

**关键创新**：SLR的主要创新在于其完全自动化的合成过程，能够在无人工注释的情况下，精确控制任务的难度，并生成多样化的推理任务。

**关键设计**：在设计中，SLR采用了特定的损失函数来优化模型输出的准确性，并通过课程学习策略逐步增加任务复杂度，以提高模型的推理能力。

## 📊 实验亮点

实验结果显示，通过SLR框架，Llama-3-8B在SLR-Bench上的准确率翻倍，达到了与Gemini-Flash-Thinking相当的水平，且计算成本显著降低，展示了SLR在逻辑推理任务中的优越性。

## 🎯 应用场景

该研究的潜在应用领域包括教育、人工智能助手和自动化决策系统。SLR框架能够为各种逻辑推理任务提供高效的训练和评估方法，具有广泛的实际价值和未来影响，尤其是在需要高效推理的场景中。

## 📄 摘要（原文）

> We introduce SLR, an end-to-end framework for systematic evaluation and training of Large Language Models (LLMs) via Scalable Logical Reasoning. Given a user's task specification, SLR automatically synthesizes (i) an instruction prompt for an inductive reasoning task, (ii) a validation program, executable on model outputs to provide verifiable rewards, and (iii) the latent ground-truth rule. This process is fully automated, scalable, requires no human annotations, and offers precise control over task difficulty. Using SLR, we create SLR-Bench, a benchmark comprising 19k prompts organized into 20 curriculum levels that progressively increase in relational, arithmetic, and recursive complexity. Large-scale evaluation reveals that contemporary LLMs readily produce syntactically valid rules, yet often fail at correct logical inference. Recent reasoning LLMs demonstrate improved performance but incur very high test-time computation, with costs exceeding $300 for just 1,000 prompts. Finally, curriculum learning via SLR doubles Llama-3-8B accuracy on SLR-Bench, achieving parity with Gemini-Flash-Thinking at a fraction of computational cost. Moreover, these reasoning capabilities generalize to a wide range of established benchmarks, underscoring the effectiveness of SLR for downstream reasoning.

