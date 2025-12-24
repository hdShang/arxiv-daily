---
layout: default
title: "Free Draft-and-Verification: Toward Lossless Parallel Decoding for Diffusion Large Language Models"
---

# Free Draft-and-Verification: Toward Lossless Parallel Decoding for Diffusion Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.00294" class="toolbar-btn" target="_blank">📄 arXiv: 2510.00294v2</a>
  <a href="https://arxiv.org/pdf/2510.00294.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00294v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.00294v2', 'Free Draft-and-Verification: Toward Lossless Parallel Decoding for Diffusion Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shutong Wu, Jiawei Zhang

**分类**: cs.LG, cs.AI

**发布日期**: 2025-09-30 (更新: 2025-11-01)

---

## 💡 一句话要点

**提出FreeDave算法，实现扩散大语言模型无损并行解码，显著提升推理速度。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `扩散语言模型` `并行解码` `无损解码` `推理加速` `候选生成与验证`

## 📋 核心要点

1. 扩散语言模型并行解码面临质量下降问题，现有算法在加速推理的同时牺牲了生成性能。
2. FreeDave算法通过并行生成候选和验证，在计算资源充足时，保证与静态解码结果一致。
3. 实验表明，FreeDave在数学推理和代码生成任务中，推理速度提升高达3.78倍，且不损失性能。

## 📝 摘要（中文）

扩散大语言模型(DLLMs)作为一种新的语言建模范式，超越了自回归的下一个token预测。得益于其双向注意力机制，DLLMs更善于捕捉上下文之间的联系，因此在诸如著名的“反转诅咒”或数据受限场景下的学习等挑战中表现出独特的优势。此外，利用其固有的建模基础，DLLMs在并行解码算法的高效推理方面具有巨大的潜力，从而能够实现每步多token预测。然而，高质量的生成通常需要解码步数等于序列长度，这相当于每步解码一个token。现有的并行解码算法虽然能加速推理，但会产生次优的解码路径，从而导致性能显著下降。为了克服这一挑战，我们提出了一种名为Free Draft-and-Verification (FreeDave) 的新型快速解码算法，该算法专为DLLMs设计，可在不进行任何模型修改或添加额外模块的情况下实现无损并行解码。具体来说，我们提出了一种并行解码的候选生成和验证算法，从理论上保证，在提供足够的计算和内存预算的情况下，可以使用最少的模型前向调用来重现静态解码生成的相同序列。通过在不同DLLMs的数学推理和代码生成基准上进行广泛的评估，FreeDave被证明可以在不降低性能的情况下将推理吞吐量提高高达3.78倍。

## 🔬 方法详解

**问题定义**：论文旨在解决扩散大语言模型（DLLMs）在推理过程中，为了加速解码而采用并行解码算法时，性能显著下降的问题。现有的并行解码算法通常会产生次优的解码路径，导致生成质量降低，无法充分发挥DLLMs的优势。

**核心思路**：FreeDave的核心思路是并行生成多个候选token，然后通过验证机制选择最优的token序列。该方法旨在通过足够的计算和内存资源，保证最终生成的序列与静态解码（即每步只生成一个token）的结果完全一致，从而实现无损的并行解码。

**技术框架**：FreeDave算法主要包含两个阶段：候选生成阶段和验证阶段。在候选生成阶段，算法并行地生成多个可能的token序列。在验证阶段，算法对这些候选序列进行评估，选择与静态解码结果最接近的序列作为最终输出。整个过程无需修改原始的DLLM模型或引入额外的模块。

**关键创新**：FreeDave的关键创新在于其并行解码的候选生成和验证机制，该机制能够在保证生成质量的前提下，显著提高解码速度。与现有的并行解码算法不同，FreeDave旨在实现无损解码，即在计算资源充足的情况下，保证生成结果与静态解码完全一致。

**关键设计**：FreeDave的关键设计包括：1) 并行生成候选token的数量；2) 验证阶段的评估指标，用于衡量候选序列与静态解码结果的接近程度；3) 计算和内存资源的分配策略，以保证算法能够在合理的时间内完成解码。

## 📊 实验亮点

实验结果表明，FreeDave算法在数学推理和代码生成任务中，能够在不降低性能的情况下，将推理吞吐量提高高达3.78倍。该算法在不同DLLMs上均表现出良好的加速效果，证明了其通用性和有效性。与现有的并行解码算法相比，FreeDave实现了无损解码，避免了性能下降的问题。

## 🎯 应用场景

FreeDave算法可广泛应用于需要快速推理的扩散大语言模型场景，例如实时对话系统、代码生成、数学问题求解等。该算法的无损并行解码特性，使其在保证生成质量的同时，显著提升推理效率，具有重要的实际应用价值和潜力。未来，该算法可以进一步扩展到其他类型的生成模型，并与其他优化技术相结合，以实现更高的推理速度和更好的生成效果。

## 📄 摘要（原文）

> Diffusion Large Language Models (DLLMs) have emerged as a new paradigm of language modeling beyond autoregressive next-token prediction. Thanks to their bidirectional attention mechanism, DLLMs are more capable of capturing the connection of context, and thus show unique advantages in challenges like the famous "reversal curse" or learning under data-constrained scenarios. In addition, taking advantage of their inherent modeling foundations, DLLMs have the great potential of efficient inference with parallel decoding algorithms, which enable multi-token prediction per step. However, the high generation quality often requires the number of decoding steps equal to the sequence length, which performs a one-token-per-step decoding, and existing parallel decoding algorithms, which yield suboptimal decoding paths, bring inference speedup at the cost of non-negligible performance degradation. To overcome this challenge, we introduce Free Draft-and-Verification (FreeDave), a novel fast decoding algorithm tailored for DLLMs that achieves lossless parallel decoding without any model modification or extra modules. Specifically, we propose an algorithm of parallel-decoded candidate generation and verification, which is theoretically guaranteed to use the fewest model forward calls to reproduce the same sequence generated by static decoding when enough computation and memory budget is provided. By extensive evaluations on math reasoning and code generation benchmarks across different DLLMs, FreeDave is proven to boost the inference throughput up to $3.78\times$ without performance degradation.

