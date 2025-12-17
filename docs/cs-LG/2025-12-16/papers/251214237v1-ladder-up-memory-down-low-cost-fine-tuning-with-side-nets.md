---
layout: default
title: Ladder Up, Memory Down: Low-Cost Fine-Tuning With Side Nets
---

# Ladder Up, Memory Down: Low-Cost Fine-Tuning With Side Nets

**arXiv**: [2512.14237v1](https://arxiv.org/abs/2512.14237) | [PDF](https://arxiv.org/pdf/2512.14237.pdf)

**作者**: Estelle Zheng, Nathan Cerisara, Sébastien Warichet, Emmanuel Helbert, Christophe Cerisara

**分类**: cs.CL, cs.LG

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出Ladder Side Tuning方法以解决大语言模型微调中的内存瓶颈问题**

**关键词**: `参数高效微调` `大语言模型` `内存优化` `侧网络` `轻量级架构` `扩展定律` `下游任务` `消费级GPU`

## 📋 核心要点

1. 现有PEFT方法如QLoRA虽减少可训练参数，但反向传播仍导致高内存占用，限制大模型微调。
2. 提出Ladder Side Tuning（LST），添加轻量级侧网络，通过侧向连接优化，显著降低内存需求。
3. 实验显示LST在多个基准任务中性能与QLoRA相当，峰值内存降低50%，支持7B模型在12GB GPU上微调。

## 📝 摘要（中文）

微调大语言模型（LLMs）常受限于商用GPU的内存容量。参数高效微调（PEFT）方法如QLoRA虽减少了可训练参数数量，但完整模型的反向传播仍导致高内存占用。本文重新审视了Ladder Side Tuning（LST），这是一种较少被探索的PEFT技术，通过添加轻量级侧网络，在保持与QLoRA相似计算扩展斜率的同时，将峰值内存降低50%。在涵盖自然语言理解、数学和LLM批评任务的不同下游基准测试中，LST平均性能与QLoRA相当，同时内存效率更高。这种效率使得在单个12GB消费级GPU上微调70亿参数模型成为可能，支持2k令牌上下文且无需梯度检查点——在这些条件下QLoRA会耗尽内存。除了内存效率，我们还建立了扩展定律，表明LST的扩展方式与QLoRA相似。通过利用Ladder的架构灵活性，我们引入了xLadder，这是一种深度扩展变体，通过交叉连接增加有效深度，并在固定参数数量下缩短思维链（CoT）。Ladder在内存受限时表现强劲；xLadder在此基础上实现了更深层推理而无额外内存开销。

## 🔬 方法详解

论文核心方法是Ladder Side Tuning（LST），一种参数高效微调技术。整体框架基于预训练大语言模型，添加一个轻量级侧网络（side network），通过侧向连接（ladder connections）将主模型的中间层输出与侧网络集成，仅训练侧网络参数，从而减少内存占用。关键技术创新点包括：利用侧网络实现高效反向传播，避免完整模型梯度计算；引入xLadder变体，通过交叉连接（cross-connections）增加网络深度，提升推理能力。与现有方法如QLoRA的主要区别在于：LST侧重于架构优化，通过侧网络降低内存，而QLoRA基于量化技术；LST在内存效率上更优，支持更大上下文长度。

## 📊 实验亮点

最重要的实验结果是LST在多个下游基准测试中平均性能与QLoRA相当，同时峰值内存降低50%。具体地，LST支持在单个12GB GPU上微调7B参数模型，处理2k令牌上下文且无需梯度检查点，而QLoRA在相同条件下内存耗尽。扩展定律分析显示LST与QLoRA具有相似的计算扩展斜率。

## 🎯 应用场景

该研究适用于大语言模型在资源受限环境下的微调，如消费级GPU部署、边缘计算或内存敏感场景。潜在应用包括自然语言处理任务（如文本分类、问答）、数学推理和AI批评系统，提升模型定制化能力的同时降低硬件成本。

## 📄 摘要（原文）

> Fine-tuning large language models (LLMs) is often limited by the memory available on commodity GPUs. Parameter-efficient fine-tuning (PEFT) methods such as QLoRA reduce the number of trainable parameters, yet still incur high memory usage induced by the backward pass in the full model. We revisit Ladder Side Tuning (LST), a rarely explored PEFT technique that adds a lightweight side network, and show that it matches QLoRA's compute scaling slope while cutting peak memory by 50\%. Across different downstream benchmarks spanning natural language understanding, mathematical and LLM-critic tasks, LST has competitive performance with QLoRA's accuracy on average while being much more memory-efficient. This efficiency enables fine-tuning of 7B-parameter models on a single 12 GB consumer GPU with 2k-token contexts, requiring no gradient checkpointing\textemdash conditions under which QLoRA exhausts memory. Beyond memory efficiency, we also establish scaling laws showing that LST scales similarly to QLoRA. We exploit Ladder's architectural flexibility by introducing xLadder, a depth-extended variant that increases effective depth via cross-connections and shortens chain-of-thought (CoT) at fixed parameter count. Ladder is strong when memory is the bottleneck; xLadder builds on this by enabling deeper reasoning without additional memory overhead.

