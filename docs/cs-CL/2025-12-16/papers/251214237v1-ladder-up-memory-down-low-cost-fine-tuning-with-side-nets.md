---
layout: default
title: Ladder Up, Memory Down: Low-Cost Fine-Tuning With Side Nets
---

# Ladder Up, Memory Down: Low-Cost Fine-Tuning With Side Nets

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14237" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14237v1</a>
  <a href="https://arxiv.org/pdf/2512.14237.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14237v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14237v1', 'Ladder Up, Memory Down: Low-Cost Fine-Tuning With Side Nets')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Estelle Zheng, Nathan Cerisara, Sébastien Warichet, Emmanuel Helbert, Christophe Cerisara

**分类**: cs.CL, cs.LG

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出Ladder Side Tuning以解决大语言模型微调的内存瓶颈问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `微调` `内存效率` `参数高效微调` `Ladder Side Tuning` `机器学习` `自然语言处理` `深度学习`

## 📋 核心要点

1. 现有的微调方法在大语言模型的训练中面临内存限制，尤其是在使用普通GPU时。
2. 本文提出Ladder Side Tuning（LST），通过引入轻量级侧网络来提高内存效率，同时保持计算性能。
3. 实验结果表明，LST在多个基准测试中与QLoRA的准确性相当，但内存使用效率提高了50%。

## 📝 摘要（中文）

微调大型语言模型（LLMs）通常受到普通GPU可用内存的限制。参数高效微调（PEFT）方法如QLoRA减少了可训练参数的数量，但在全模型的反向传播中仍然消耗大量内存。本文重新审视了Ladder Side Tuning（LST），这一较少被探索的PEFT技术，通过添加轻量级侧网络，展示了其在计算规模上与QLoRA相匹配，同时将峰值内存减少了50%。在不同的下游基准测试中，LST在自然语言理解、数学和LLM评估任务上表现出与QLoRA相当的准确性，同时显著提高了内存效率，使得在单个12GB消费级GPU上以2k-token上下文微调7B参数模型成为可能，且无需梯度检查点。除了内存效率外，本文还建立了LST的扩展规律，表明其与QLoRA的扩展性相似。通过引入xLadder，LST在不增加内存开销的情况下，增强了推理深度。

## 🔬 方法详解

**问题定义**：本文旨在解决在普通GPU上微调大型语言模型时的内存瓶颈问题。现有的PEFT方法如QLoRA虽然减少了可训练参数，但在反向传播过程中仍然消耗大量内存，限制了模型的训练能力。

**核心思路**：论文提出Ladder Side Tuning（LST），通过添加一个轻量级的侧网络来降低内存消耗，同时保持与QLoRA相似的计算性能。这种设计使得在内存受限的环境中，仍能有效微调大型模型。

**技术框架**：LST的整体架构包括主网络和侧网络，主网络负责主要的计算任务，而侧网络则通过辅助计算来减轻主网络的内存负担。该方法在不同的下游任务中进行评估，以验证其有效性。

**关键创新**：LST的主要创新在于引入了轻量级侧网络，显著降低了微调过程中的内存需求，同时保持了与QLoRA相当的性能。这一方法在内存成为瓶颈的情况下表现尤为突出。

**关键设计**：在设计中，LST采用了特定的参数设置和网络结构，以确保侧网络的轻量性和有效性。此外，xLadder作为LST的扩展版本，通过交叉连接增加了有效深度，进一步提升了推理能力，而不增加额外的内存开销。

## 📊 实验亮点

实验结果显示，LST在多个下游基准测试中表现出与QLoRA相当的准确性，同时内存使用效率提高了50%。在单个12GB的消费级GPU上，LST能够有效微调7B参数的模型，且无需梯度检查点，这在QLoRA中是不可行的。整体来看，LST在内存受限的环境中展现出了优越的性能。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、机器翻译和对话系统等。通过提高大语言模型的微调效率，LST能够使得更多研究者和开发者在资源有限的情况下，利用大型模型进行创新和开发，从而推动相关技术的进步与应用。未来，LST及其变体有望在更多实际场景中得到应用，尤其是在需要高效计算资源的情况下。

## 📄 摘要（原文）

> Fine-tuning large language models (LLMs) is often limited by the memory available on commodity GPUs. Parameter-efficient fine-tuning (PEFT) methods such as QLoRA reduce the number of trainable parameters, yet still incur high memory usage induced by the backward pass in the full model. We revisit Ladder Side Tuning (LST), a rarely explored PEFT technique that adds a lightweight side network, and show that it matches QLoRA's compute scaling slope while cutting peak memory by 50\%. Across different downstream benchmarks spanning natural language understanding, mathematical and LLM-critic tasks, LST has competitive performance with QLoRA's accuracy on average while being much more memory-efficient. This efficiency enables fine-tuning of 7B-parameter models on a single 12 GB consumer GPU with 2k-token contexts, requiring no gradient checkpointing\textemdash conditions under which QLoRA exhausts memory. Beyond memory efficiency, we also establish scaling laws showing that LST scales similarly to QLoRA. We exploit Ladder's architectural flexibility by introducing xLadder, a depth-extended variant that increases effective depth via cross-connections and shortens chain-of-thought (CoT) at fixed parameter count. Ladder is strong when memory is the bottleneck; xLadder builds on this by enabling deeper reasoning without additional memory overhead.

