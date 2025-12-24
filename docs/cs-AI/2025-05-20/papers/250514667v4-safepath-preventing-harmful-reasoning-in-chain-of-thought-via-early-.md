---
layout: default
title: "SAFEPATH: Preventing Harmful Reasoning in Chain-of-Thought via Early Alignment"
---

# SAFEPATH: Preventing Harmful Reasoning in Chain-of-Thought via Early Alignment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14667" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14667v4</a>
  <a href="https://arxiv.org/pdf/2505.14667.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14667v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14667v4', 'SAFEPATH: Preventing Harmful Reasoning in Chain-of-Thought via Early Alignment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wonje Jeung, Sangyeon Yoon, Minsuk Kahng, Albert No

**分类**: cs.AI, cs.CL

**发布日期**: 2025-05-20 (更新: 2025-10-23)

**备注**: Accepted at NeurIPS 2025. Code and models are available at https://ai-isl.github.io/safepath

---

## 💡 一句话要点

**提出SAFEPATH以解决大型推理模型的安全性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型推理模型` `安全对齐` `推理深度` `越狱攻击` `轻量级方法` `AI安全性` `计算效率`

## 📋 核心要点

1. 现有安全对齐方法在减少有害输出的同时，往往会降低推理深度，导致复杂任务中的显著权衡。
2. SAFEPATH通过在推理开始时发出短小的安全引导，针对有害提示进行轻量级对齐，同时保持后续推理过程的自主性。
3. 实验结果显示，SAFEPATH在DeepSeek-R1-Distill-Llama-8B模型中，有害响应减少90.0%，并阻止83.3%的越狱尝试，计算效率显著提升。

## 📝 摘要（中文）

大型推理模型（LRMs）在复杂问题解决中表现出色，但其结构化推理路径在面对有害提示时可能导致不安全的输出。现有的安全对齐方法虽然能减少有害输出，但往往会降低推理深度，并在复杂的多步骤任务中面临显著的权衡，同时也容易受到复杂的越狱攻击。为此，本文提出SAFEPATH，这是一种轻量级的对齐方法，通过在推理开始时针对有害提示发出短小的8-token安全引导，同时保持其余推理过程不受监督。实验证明，SAFEPATH有效减少有害输出，同时保持推理性能，具体表现为在DeepSeek-R1-Distill-Llama-8B模型中，有害响应减少高达90.0%，并阻止83.3%的越狱尝试，同时计算需求比直接拒绝方法少295.9倍，比SafeChain少314.1倍。我们还提出了一种无需微调的零-shot变体，并分析了现有方法在推理中心模型中的泛化能力，揭示了关键的缺口和新的安全AI方向。

## 🔬 方法详解

**问题定义**：本文旨在解决大型推理模型在面对有害提示时产生不安全输出的问题。现有方法虽然能减少有害输出，但往往会降低推理深度，并在复杂任务中面临权衡，同时易受越狱攻击。

**核心思路**：SAFEPATH的核心思路是通过在推理开始时发出短小的安全引导，来应对有害提示，同时保持后续推理过程的自主性。这种设计旨在减少有害输出的同时，尽量不影响模型的推理能力。

**技术框架**：SAFEPATH的整体架构包括两个主要阶段：首先，在接收到有害提示时，模型发出8-token的安全引导；其次，模型在后续推理过程中保持自主推理，不受监督。

**关键创新**：SAFEPATH的主要创新在于其轻量级的对齐方法，通过短小的安全引导实现了对有害提示的有效响应，与现有方法相比，显著提高了计算效率和推理性能。

**关键设计**：在关键设计上，SAFEPATH采用了特定的参数设置和损失函数，以确保安全引导的有效性，同时优化了模型的推理过程，确保在减少有害输出的同时，保持推理深度。

## 📊 实验亮点

实验结果表明，SAFEPATH在DeepSeek-R1-Distill-Llama-8B模型中，有害响应减少高达90.0%，并成功阻止了83.3%的越狱尝试。此外，该方法的计算需求比直接拒绝方法少295.9倍，比SafeChain少314.1倍，显示出显著的效率优势。

## 🎯 应用场景

SAFEPATH的研究成果在多个领域具有潜在应用价值，尤其是在需要安全性和可靠性的AI系统中，如医疗诊断、金融决策和自动驾驶等。通过有效减少有害输出，该方法能够提升AI系统的安全性，降低风险，推动更安全的人工智能应用的发展。

## 📄 摘要（原文）

> Large Reasoning Models (LRMs) have become powerful tools for complex problem solving, but their structured reasoning pathways can lead to unsafe outputs when exposed to harmful prompts. Existing safety alignment methods reduce harmful outputs but can degrade reasoning depth, leading to significant trade-offs in complex, multi-step tasks, and remain vulnerable to sophisticated jailbreak attacks. To address this, we introduce SAFEPATH, a lightweight alignment method that fine-tunes LRMs to emit a short, 8-token Safety Primer at the start of their reasoning, in response to harmful prompts, while leaving the rest of the reasoning process unsupervised. Empirical results across multiple benchmarks indicate that SAFEPATH effectively reduces harmful outputs while maintaining reasoning performance. Specifically, SAFEPATH reduces harmful responses by up to 90.0% and blocks 83.3% of jailbreak attempts in the DeepSeek-R1-Distill-Llama-8B model, while requiring 295.9x less compute than Direct Refusal and 314.1x less than SafeChain. We further introduce a zero-shot variant that requires no fine-tuning. In addition, we provide a comprehensive analysis of how existing methods in LLMs generalize, or fail, when applied to reasoning-centric models, revealing critical gaps and new directions for safer AI.

