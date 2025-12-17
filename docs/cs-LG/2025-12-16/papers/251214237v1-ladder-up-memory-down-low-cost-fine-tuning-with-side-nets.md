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

**提出Ladder Side Tuning方法，通过轻量级侧网络实现大语言模型低成本微调，显著降低内存需求。**

🎯 **匹配领域**: **强化学习**

**关键词**: `参数高效微调` `大语言模型` `内存优化` `侧网络` `轻量级微调` `自然语言理解` `扩展定律` `消费级GPU`

## 📋 核心要点

1. 现有PEFT方法如QLoRA虽减少可训练参数，但反向传播仍导致高内存占用，限制大模型在消费级GPU上的微调。
2. 提出Ladder Side Tuning（LST），添加轻量级侧网络，仅微调侧网络参数，大幅降低内存需求，同时保持性能。
3. 实验显示LST峰值内存降低50%，在12GB GPU上微调7B模型可行，性能与QLoRA相当，扩展定律相似。

## 📝 摘要（中文）

微调大语言模型（LLMs）常受限于商用GPU的内存容量。参数高效微调（PEFT）方法如QLoRA减少了可训练参数数量，但仍因完整模型的反向传播而产生高内存占用。本文重新审视了Ladder Side Tuning（LST），这是一种较少被探索的PEFT技术，通过添加轻量级侧网络，在保持与QLoRA相似计算扩展斜率的同时，将峰值内存降低50%。在涵盖自然语言理解、数学和LLM批评任务的不同下游基准测试中，LST平均性能与QLoRA相当，同时内存效率更高。这种效率使得在单个12GB消费级GPU上微调70亿参数模型成为可能，支持2k令牌上下文且无需梯度检查点——在这些条件下QLoRA会耗尽内存。除了内存效率，我们还建立了扩展定律，表明LST的扩展方式与QLoRA相似。通过利用Ladder的架构灵活性，我们引入了xLadder，这是一种深度扩展变体，通过交叉连接增加有效深度，并在固定参数数量下缩短思维链（CoT）。Ladder在内存受限时表现强劲；xLadder在此基础上实现了更深层推理，且无额外内存开销。

## 🔬 方法详解

论文核心方法是Ladder Side Tuning（LST），整体框架基于预训练大语言模型，添加一个轻量级侧网络（side network），该网络通过梯子状连接（ladder connections）与主模型交互。关键技术创新点在于仅微调侧网络参数，主模型参数保持冻结，从而大幅减少反向传播时的内存占用。与现有PEFT方法（如QLoRA）的主要区别在于：QLoRA通过量化等技术减少参数但仍在完整模型上进行反向传播，而LST通过侧网络实现参数高效，避免了主模型的反向传播开销，因此内存效率更高。此外，论文还提出了xLadder变体，通过交叉连接增加网络深度，提升推理能力。

## 📊 实验亮点

LST在多个下游任务中性能与QLoRA相当，峰值内存降低50%，支持在12GB GPU上微调7B参数模型（2k令牌上下文），无需梯度检查点，扩展定律显示与QLoRA相似扩展性。

## 🎯 应用场景

该研究适用于资源受限环境下的自然语言处理任务，如消费级GPU上的大语言模型微调，可应用于自然语言理解、数学推理、LLM批评等领域，降低部署成本，促进AI技术普及。

## 📄 摘要（原文）

> Fine-tuning large language models (LLMs) is often limited by the memory available on commodity GPUs. Parameter-efficient fine-tuning (PEFT) methods such as QLoRA reduce the number of trainable parameters, yet still incur high memory usage induced by the backward pass in the full model. We revisit Ladder Side Tuning (LST), a rarely explored PEFT technique that adds a lightweight side network, and show that it matches QLoRA's compute scaling slope while cutting peak memory by 50\%. Across different downstream benchmarks spanning natural language understanding, mathematical and LLM-critic tasks, LST has competitive performance with QLoRA's accuracy on average while being much more memory-efficient. This efficiency enables fine-tuning of 7B-parameter models on a single 12 GB consumer GPU with 2k-token contexts, requiring no gradient checkpointing\textemdash conditions under which QLoRA exhausts memory. Beyond memory efficiency, we also establish scaling laws showing that LST scales similarly to QLoRA. We exploit Ladder's architectural flexibility by introducing xLadder, a depth-extended variant that increases effective depth via cross-connections and shortens chain-of-thought (CoT) at fixed parameter count. Ladder is strong when memory is the bottleneck; xLadder builds on this by enabling deeper reasoning without additional memory overhead.

