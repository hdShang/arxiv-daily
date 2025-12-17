---
layout: default
title: Ladder Up, Memory Down: Low-Cost Fine-Tuning With Side Nets
---

# Ladder Up, Memory Down: Low-Cost Fine-Tuning With Side Nets

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14237" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14237</a>
  <a href="https://arxiv.org/pdf/2512.14237.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14237" onclick="toggleFavorite(this, '2512.14237', 'Ladder Up, Memory Down: Low-Cost Fine-Tuning With Side Nets')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Estelle Zheng, Nathan Cerisara, Sébastien Warichet, Emmanuel Helbert, Christophe Cerisara

**分类**: cs.CL, cs.LG

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出Ladder Side Tuning，以低成本微调大型语言模型，显著降低内存占用。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `参数高效微调` `大型语言模型` `内存优化` `侧网络` `Ladder Side Tuning`

## 📋 核心要点

1. 现有PEFT方法如QLoRA虽然减少了训练参数，但完整模型反向传播导致内存占用仍然很高。
2. Ladder Side Tuning (LST) 通过增加轻量级侧网络，在保证性能的同时显著降低内存占用。
3. LST在多个下游任务上与QLoRA性能相当，内存占用减半，并可扩展到更深层次的推理。

## 📝 摘要（中文）

微调大型语言模型（LLM）通常受限于消费级GPU的内存。参数高效微调（PEFT）方法如QLoRA虽然减少了可训练参数的数量，但由于完整模型中的反向传播，仍然会产生较高的内存使用量。本文重新审视了Ladder Side Tuning（LST），一种很少被探索的PEFT技术，它增加了一个轻量级的侧网络，并表明它在计算扩展斜率上与QLoRA相匹配，同时将峰值内存减少了50%。在涵盖自然语言理解、数学和LLM-critic任务的不同下游基准测试中，LST的性能与QLoRA的准确性相比具有竞争力，同时内存效率更高。这种效率使得可以在单个12GB消费级GPU上使用2k-token上下文微调7B参数模型，而无需梯度检查点——在这些条件下，QLoRA会耗尽内存。除了内存效率之外，本文还建立了缩放定律，表明LST的缩放方式与QLoRA类似。本文通过引入xLadder来利用Ladder的架构灵活性，xLadder是一种深度扩展的变体，通过交叉连接增加有效深度，并在固定参数数量下缩短思维链（CoT）。当内存是瓶颈时，Ladder表现强劲；xLadder在此基础上通过无需额外内存开销即可实现更深层次的推理。

## 🔬 方法详解

**问题定义**：现有参数高效微调方法（如QLoRA）在微调大型语言模型时，虽然减少了可训练参数的数量，但由于需要进行完整模型的反向传播，仍然会消耗大量的GPU内存，限制了在资源受限的设备上的应用。尤其是在长文本场景下，内存需求更加严峻。

**核心思路**：论文的核心思路是利用Ladder Side Tuning (LST) 这种相对较少被研究的参数高效微调技术，通过引入一个轻量级的侧网络，在主模型之外进行参数更新。这样可以在不修改或微调主模型参数的情况下，实现对下游任务的适配，从而显著降低内存占用。

**技术框架**：LST 的整体架构是在预训练的 Transformer 模型旁边添加一个并行的、轻量级的侧网络（Ladder Network）。输入数据同时输入到主模型和侧网络。主模型的输出和侧网络的输出进行融合，得到最终的预测结果。在训练过程中，只更新侧网络的参数，而主模型的参数保持固定。xLadder 是 LST 的一个变体，通过增加侧网络的深度和引入跨层连接，来增强模型的推理能力。

**关键创新**：LST 的关键创新在于其高效的内存利用率。通过只训练侧网络，避免了对整个大型语言模型进行反向传播，从而显著降低了内存需求。xLadder 的创新在于通过扩展侧网络的深度和引入跨层连接，在不增加过多参数的情况下，提升了模型的推理能力。

**关键设计**：LST 的关键设计包括侧网络的结构选择（例如，可以使用较小的 Transformer 模型或 MLP），以及主模型和侧网络输出的融合方式（例如，可以使用加权平均或拼接）。xLadder 的关键设计在于跨层连接的引入，这允许信息在侧网络的不同层之间流动，从而增强了模型的表达能力。损失函数通常采用交叉熵损失，用于衡量模型预测结果与真实标签之间的差异。

## 📊 实验亮点

实验结果表明，LST 在内存效率方面优于 QLoRA，在多个下游任务上取得了与 QLoRA 相当甚至更好的性能。LST 能够在一个 12GB 的消费级 GPU 上微调 7B 参数的模型，而 QLoRA 在相同条件下会耗尽内存。此外，xLadder 通过增加侧网络的深度，在不增加过多参数的情况下，提升了模型的推理能力。

## 🎯 应用场景

该研究成果可应用于资源受限的场景下的大型语言模型微调，例如在消费级GPU或边缘设备上进行模型适配。这使得更多用户能够利用大型语言模型的能力，而无需昂贵的硬件设备。此外，该方法还可以应用于需要快速迭代和部署的场景，因为其训练效率更高。

## 📄 摘要（原文）

> Fine-tuning large language models (LLMs) is often limited by the memory available on commodity GPUs. Parameter-efficient fine-tuning (PEFT) methods such as QLoRA reduce the number of trainable parameters, yet still incur high memory usage induced by the backward pass in the full model. We revisit Ladder Side Tuning (LST), a rarely explored PEFT technique that adds a lightweight side network, and show that it matches QLoRA's compute scaling slope while cutting peak memory by 50\%. Across different downstream benchmarks spanning natural language understanding, mathematical and LLM-critic tasks, LST has competitive performance with QLoRA's accuracy on average while being much more memory-efficient. This efficiency enables fine-tuning of 7B-parameter models on a single 12 GB consumer GPU with 2k-token contexts, requiring no gradient checkpointing\textemdash conditions under which QLoRA exhausts memory. Beyond memory efficiency, we also establish scaling laws showing that LST scales similarly to QLoRA. We exploit Ladder's architectural flexibility by introducing xLadder, a depth-extended variant that increases effective depth via cross-connections and shortens chain-of-thought (CoT) at fixed parameter count. Ladder is strong when memory is the bottleneck; xLadder builds on this by enabling deeper reasoning without additional memory overhead.

