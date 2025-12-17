---
layout: default
title: Sparser Block-Sparse Attention via Token Permutation
---

# Sparser Block-Sparse Attention via Token Permutation

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.21270" target="_blank" class="toolbar-btn">arXiv: 2510.21270v1</a>
    <a href="https://arxiv.org/pdf/2510.21270.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.21270v1" 
            onclick="toggleFavorite(this, '2510.21270v1', 'Sparser Block-Sparse Attention via Token Permutation')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Xinghao Wang, Pengyu Wang, Dong Zhang, Chenkun Tan, Shaojun Zhou, Zhaoxiang Liu, Shiguo Lian, Fangxu Liu, Kai Song, Xipeng Qiu

**分类**: cs.CL, cs.AI, cs.CV

**发布日期**: 2025-10-24

**🔗 代码/项目**: [GITHUB](https://github.com/xinghaow99/pbs-attn)

---

## 💡 一句话要点

**提出基于Token置换的稀疏块注意力机制PBS-Attn，加速长文本LLM预填充。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长文本处理` `稀疏注意力` `块稀疏性` `Token置换` `大型语言模型` `计算效率` `FlashAttention`

## 📋 核心要点

1. 长文本处理中，自注意力机制的平方复杂度是LLM扩展上下文长度的主要瓶颈。
2. 论文提出PBS-Attn，通过token置换增加块稀疏性，提升计算效率，且易于集成。
3. 实验表明，PBS-Attn在精度上优于现有块稀疏方法，并接近完整注意力，加速高达2.75倍。

## 📝 摘要（中文）

扩展大型语言模型（LLM）的上下文长度具有显著优势，但计算成本很高。这种成本主要源于自注意力机制，其相对于序列长度的$O(N^2)$复杂度对内存和延迟构成了主要瓶颈。幸运的是，注意力矩阵通常是稀疏的，特别是对于长序列，这表明存在优化的机会。块稀疏注意力已经成为一种有前途的解决方案，它将序列划分为块，并跳过部分块的计算。然而，这种方法的有效性高度依赖于底层的注意力模式，这可能导致次优的块级稀疏性。例如，单个块内查询的重要键token可能分散在许多其他块中，导致计算冗余。在这项工作中，我们提出了一种置换块稀疏注意力（PBS-Attn），这是一种即插即用的方法，它利用注意力的置换属性来增加块级稀疏性并提高LLM预填充的计算效率。我们在具有挑战性的真实长上下文数据集上进行了全面的实验，表明PBS-Attn在模型精度方面始终优于现有的块稀疏注意力方法，并且与完整注意力基线非常接近。在我们的定制置换FlashAttention内核的支持下，PBS-Attn在长上下文预填充中实现了高达2.75倍的端到端加速，证实了其在实际应用中的可行性。

## 🔬 方法详解

**问题定义**：论文旨在解决长文本处理中，自注意力机制计算复杂度过高的问题。现有块稀疏注意力方法虽然能降低计算量，但其性能受限于底层注意力模式，可能导致次优的块级稀疏性和计算冗余。

**核心思路**：论文的核心思路是利用token置换的特性，重新排列token的顺序，使得原本分散在不同块中的重要token能够集中到少数块中，从而提高块稀疏性，减少不必要的计算。通过置换操作，使得注意力更加集中，从而提升效率。

**技术框架**：PBS-Attn是一个即插即用的模块，可以嵌入到现有的Transformer架构中。其主要流程包括：1) 输入序列分块；2) 对每个块内的token进行置换；3) 进行块稀疏注意力计算；4) 对输出进行逆置换，恢复原始顺序。整个过程无需修改原有的模型结构，易于集成。

**关键创新**：论文的关键创新在于提出了基于token置换的块稀疏注意力机制。与传统的块稀疏方法不同，PBS-Attn不是简单地跳过某些块的计算，而是通过置换操作改变了注意力模式，使得注意力更加集中，从而提高了块稀疏性的有效性。此外，论文还定制了permuted-FlashAttention内核，进一步提升了计算效率。

**关键设计**：论文的关键设计包括：1) 置换策略的选择：论文可能探索了不同的置换策略，例如随机置换、基于注意力权重的置换等，以找到最优的置换方式。2) 块大小的设置：块大小的选择会影响块稀疏性的效果，需要根据具体的任务和数据集进行调整。3) 定制的permuted-FlashAttention内核：该内核针对置换后的数据进行了优化，能够充分利用硬件资源，提高计算效率。

## 📊 实验亮点

实验结果表明，PBS-Attn在长上下文数据集上优于现有的块稀疏注意力方法，并且在模型精度上与完整注意力基线非常接近。更重要的是，通过定制的permuted-FlashAttention内核，PBS-Attn在长上下文预填充中实现了高达2.75倍的端到端加速，证明了其在实际应用中的可行性。

## 🎯 应用场景

PBS-Attn可应用于需要处理长文本的各种场景，如文档摘要、机器翻译、代码生成、对话系统等。通过降低计算成本，该方法能够支持更长的上下文长度，从而提升模型的性能和泛化能力。此外，PBS-Attn的即插即用特性使其易于集成到现有的LLM中，具有广泛的应用前景。

## 📄 摘要（原文）

> Scaling the context length of large language models (LLMs) offers significant benefits but is computationally expensive. This expense stems primarily from the self-attention mechanism, whose $O(N^2)$ complexity with respect to sequence length presents a major bottleneck for both memory and latency. Fortunately, the attention matrix is often sparse, particularly for long sequences, suggesting an opportunity for optimization. Block-sparse attention has emerged as a promising solution that partitions sequences into blocks and skips computation for a subset of these blocks. However, the effectiveness of this method is highly dependent on the underlying attention patterns, which can lead to sub-optimal block-level sparsity. For instance, important key tokens for queries within a single block may be scattered across numerous other blocks, leading to computational redundancy. In this work, we propose Permuted Block-Sparse Attention (\textbf{PBS-Attn}), a plug-and-play method that leverages the permutation properties of attention to increase block-level sparsity and enhance the computational efficiency of LLM prefilling. We conduct comprehensive experiments on challenging real-world long-context datasets, demonstrating that PBS-Attn consistently outperforms existing block-sparse attention methods in model accuracy and closely matches the full attention baseline. Powered by our custom permuted-FlashAttention kernels, PBS-Attn achieves an end-to-end speedup of up to $2.75\times$ in long-context prefilling, confirming its practical viability. Code available at https://github.com/xinghaow99/pbs-attn

