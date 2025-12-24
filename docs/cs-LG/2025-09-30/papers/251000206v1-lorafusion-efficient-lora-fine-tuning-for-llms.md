---
layout: default
title: "LoRAFusion: Efficient LoRA Fine-Tuning for LLMs"
---

# LoRAFusion: Efficient LoRA Fine-Tuning for LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.00206" class="toolbar-btn" target="_blank">📄 arXiv: 2510.00206v1</a>
  <a href="https://arxiv.org/pdf/2510.00206.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00206v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.00206v1', 'LoRAFusion: Efficient LoRA Fine-Tuning for LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhanda Zhu, Qidong Su, Yaoyao Ding, Kevin Song, Shang Wang, Gennady Pekhimenko

**分类**: cs.LG, cs.AI, cs.DC

**发布日期**: 2025-09-30

**备注**: Accepted by EuroSys 2026

**DOI**: [10.1145/3767295.3769331](https://doi.org/10.1145/3767295.3769331)

**🔗 代码/项目**: [GITHUB](https://github.com/CentML/lorafusion)

---

## 💡 一句话要点

**LoRAFusion：一种高效的LLM LoRA微调系统，通过内核融合和自适应批处理优化性能。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `LoRA微调` `参数高效微调` `大语言模型` `内核融合` `自适应批处理` `GPU优化` `并发微调`

## 📋 核心要点

1. 现有LoRA微调系统存在冗余内存访问和无法并发微调多个LoRA适配器的低效问题，导致运行时开销大和GPU资源利用率低。
2. LoRAFusion通过图分割融合内存受限操作，消除不必要的内存访问，并设计自适应批处理算法，实现多任务并发微调。
3. 实验结果表明，LoRAFusion在端到端性能上优于Megatron-LM和mLoRA，并且融合内核可作为现有LoRA系统的即插即用替代品。

## 📝 摘要（中文）

LoRA（Low-Rank Adaptation）已成为大语言模型（LLM）参数高效微调（PEFT）的主流方法，它在显著降低GPU内存使用的同时，保持了微调模型在下游任务上的竞争力。然而，现有LoRA微调系统存在两个主要低效之处：一是由于大型激活张量的冗余内存访问导致显著的运行时开销；二是错失了在同一组GPU上并发微调多个共享相同基础模型的独立LoRA适配器的机会。为了解决这些问题，我们提出了LoRAFusion，一种高效的LLM LoRA微调系统。在内核层面，我们提出了一种图分割方法，融合了内存受限的操作，消除了不必要的内存访问，并保留了计算受限GEMM的性能，而无需重新计算或同步。在调度层面，LoRAFusion引入了一种自适应批处理算法，用于多任务微调。它首先将LoRA适配器分成组，以有意地错开跨任务的批处理执行，然后解决每个组内的装箱问题，以生成平衡的、依赖感知的微批次。与Megatron-LM相比，LoRAFusion实现了高达1.96倍（平均1.47倍）的端到端加速，与最先进的多LoRA微调系统mLoRA相比，实现了高达1.46倍（平均1.29倍）的改进。我们的融合内核实现了高达1.39倍（平均1.27倍）的内核性能提升，可以直接作为现有LoRA系统中的即插即用替代品。我们已在https://github.com/CentML/lorafusion开源了LoRAFusion。

## 🔬 方法详解

**问题定义**：现有LoRA微调方法在处理大型语言模型时，由于需要频繁访问内存中的激活张量，导致显著的运行时开销。此外，现有系统通常无法有效地并发微调多个独立的LoRA适配器，从而无法充分利用GPU资源，导致训练效率低下。这些问题限制了LoRA在实际应用中的性能和可扩展性。

**核心思路**：LoRAFusion的核心思路是通过内核融合和自适应批处理来优化LoRA微调过程。内核融合旨在减少内存访问次数，提高计算效率；自适应批处理则旨在实现多个LoRA适配器的并发微调，从而提高GPU利用率。通过将内存受限的操作融合到计算密集型的GEMM操作中，减少了数据在GPU内存和计算单元之间的传输，从而提高了整体性能。

**技术框架**：LoRAFusion的整体框架包括两个主要部分：融合内核和自适应批处理调度器。融合内核通过图分割技术，将多个内存受限的操作融合为一个计算密集型的操作，从而减少内存访问次数。自适应批处理调度器则根据LoRA适配器的依赖关系和计算需求，动态地调整批处理大小和执行顺序，从而实现多个LoRA适配器的并发微调。

**关键创新**：LoRAFusion的关键创新在于其融合内核和自适应批处理调度器。融合内核通过图分割技术，实现了内存访问和计算的优化，从而提高了内核的执行效率。自适应批处理调度器则通过动态调整批处理大小和执行顺序，实现了多个LoRA适配器的并发微调，从而提高了GPU利用率。

**关键设计**：在融合内核中，关键的设计在于如何选择合适的图分割策略，以最大程度地减少内存访问次数，同时保持计算密集型操作的性能。在自适应批处理调度器中，关键的设计在于如何根据LoRA适配器的依赖关系和计算需求，动态地调整批处理大小和执行顺序，以实现最佳的并发微调效果。论文采用了一种基于装箱问题的优化算法来解决这个问题。

## 📊 实验亮点

LoRAFusion相比Megatron-LM实现了高达1.96倍（平均1.47倍）的端到端加速，相比最先进的多LoRA微调系统mLoRA实现了高达1.46倍（平均1.29倍）的性能提升。融合内核实现了高达1.39倍（平均1.27倍）的内核性能提升，可直接作为现有LoRA系统的即插即用替代品。

## 🎯 应用场景

LoRAFusion可广泛应用于各种需要对大型语言模型进行高效微调的场景，例如自然语言处理、机器翻译、文本生成等。它能够显著降低微调成本，提高微调效率，并支持多个任务的并发微调，从而加速LLM在实际应用中的部署和迭代。

## 📄 摘要（原文）

> Low-Rank Adaptation (LoRA) has become the leading Parameter-Efficient Fine-Tuning (PEFT) method for Large Language Models (LLMs), as it significantly reduces GPU memory usage while maintaining competitive fine-tuned model quality on downstream tasks. Despite these benefits, we identify two key inefficiencies in existing LoRA fine-tuning systems. First, they incur substantial runtime overhead due to redundant memory accesses on large activation tensors. Second, they miss the opportunity to concurrently fine-tune multiple independent LoRA adapters that share the same base model on the same set of GPUs. This leads to missed performance gains such as reduced pipeline bubbles, better communication overlap, and improved GPU load balance.
>   To address these issues, we introduce LoRAFusion, an efficient LoRA fine-tuning system for LLMs. At the kernel level, we propose a graph-splitting method that fuses memory-bound operations. This design eliminates unnecessary memory accesses and preserves the performance of compute-bound GEMMs without incurring the cost of recomputation or synchronization. At the scheduling level, LoRAFusion introduces an adaptive batching algorithm for multi-job fine-tuning. It first splits LoRA adapters into groups to intentionally stagger batch execution across jobs, and then solves a bin-packing problem within each group to generate balanced, dependency-aware microbatches. LoRAFusion achieves up to $1.96\times$ ($1.47\times$ on average) end-to-end speedup compared to Megatron-LM, and up to $1.46\times$ ($1.29\times$ on average) improvement over mLoRA, the state-of-the-art multi-LoRA fine-tuning system. Our fused kernel achieves up to $1.39\times$ ($1.27\times$ on average) kernel performance improvement and can directly serve as a plug-and-play replacement in existing LoRA systems. We open-source LoRAFusion at https://github.com/CentML/lorafusion.

