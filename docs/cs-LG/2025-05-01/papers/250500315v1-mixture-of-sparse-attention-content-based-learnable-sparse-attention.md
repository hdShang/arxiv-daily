---
layout: default
title: "Mixture of Sparse Attention: Content-Based Learnable Sparse Attention via Expert-Choice Routing"
---

# Mixture of Sparse Attention: Content-Based Learnable Sparse Attention via Expert-Choice Routing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.00315" class="toolbar-btn" target="_blank">📄 arXiv: 2505.00315v1</a>
  <a href="https://arxiv.org/pdf/2505.00315.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.00315v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.00315v1', 'Mixture of Sparse Attention: Content-Based Learnable Sparse Attention via Expert-Choice Routing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Piotr Piękos, Róbert Csordás, Jürgen Schmidhuber

**分类**: cs.LG, cs.CL

**发布日期**: 2025-05-01

---

## 💡 一句话要点

**提出混合稀疏注意力机制以解决自注意力计算复杂度问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `稀疏注意力` `混合专家` `计算复杂度` `自然语言处理` `模型优化`

## 📋 核心要点

1. 现有的自注意力机制在计算复杂度上存在二次方的开销，导致效率低下。
2. 本文提出的混合稀疏注意力（MoSA）通过动态选择令牌，允许灵活的稀疏注意力模式，从而降低计算复杂度。
3. 实验结果显示，MoSA在相同计算预算下的困惑度比密集基线提高了27%，并且在训练时更快、内存占用更少。

## 📝 摘要（中文）

近年来，大型语言模型的进展突显了自注意力机制的二次方计算成本。尽管已有大量研究努力，亚二次方注意力方法在实际应用中仍表现不佳。本文假设动态学习的基于内容的稀疏性可以提高注意力机制的效率。我们提出了混合稀疏注意力（MoSA），这一新方法受到了专家选择路由的启发。MoSA动态选择每个注意力头的令牌，允许任意稀疏注意力模式。通过从长度为T的序列中选择k个令牌，MoSA将每个注意力头的计算复杂度从O(T^2)降低到O(k^2 + T)，从而在相同计算预算内使用更多的头，提升了专门化水平。实验表明，MoSA在测试的稀疏注意力变体中是唯一能够超越密集基线的方案，某些情况下在相同计算预算下的困惑度提升达27%。

## 🔬 方法详解

**问题定义**：本文旨在解决自注意力机制的高计算复杂度问题，现有的亚二次方注意力方法在实际应用中表现不佳，无法有效利用计算资源。

**核心思路**：提出混合稀疏注意力（MoSA），通过动态选择令牌来实现基于内容的稀疏性，从而降低每个注意力头的计算复杂度，提升模型的效率和性能。

**技术框架**：MoSA的整体架构包括多个注意力头，每个头根据输入序列动态选择k个令牌，计算复杂度从O(T^2)降低到O(k^2 + T)，使得在相同预算下可以使用更多的注意力头。

**关键创新**：MoSA的主要创新在于其动态选择机制，允许任意稀疏注意力模式，这与传统的密集注意力机制形成鲜明对比，能够在保持性能的同时显著降低计算资源的消耗。

**关键设计**：在实现中，MoSA使用了torch框架，尽管没有优化的内核，但在困惑度匹配的情况下，模型在墙钟时间上更快，训练时内存需求更少，同时显著减少了KV缓存的大小。

## 📊 实验亮点

实验结果表明，MoSA在相同计算预算下的困惑度比密集基线提高了27%。此外，MoSA在训练时速度更快，内存占用更少，并显著减少了KV缓存的大小，展示了其在资源使用上的优势。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、机器翻译和对话系统等。通过提高注意力机制的效率，MoSA能够在资源受限的环境中实现更高效的模型训练和推理，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Recent advances in large language models highlighted the excessive quadratic cost of self-attention. Despite the significant research efforts, subquadratic attention methods still suffer from inferior performance in practice. We hypothesize that dynamic, learned content-based sparsity can lead to more efficient attention mechanisms. We present Mixture of Sparse Attention (MoSA), a novel approach inspired by Mixture of Experts (MoE) with expert choice routing. MoSA dynamically selects tokens for each attention head, allowing arbitrary sparse attention patterns. By selecting $k$ tokens from a sequence of length $T$, MoSA reduces the computational complexity of each attention head from $O(T^2)$ to $O(k^2 + T)$. This enables using more heads within the same computational budget, allowing higher specialization. We show that among the tested sparse attention variants, MoSA is the only one that can outperform the dense baseline, sometimes with up to 27% better perplexity for an identical compute budget. MoSA can also reduce the resource usage compared to dense self-attention. Despite using torch implementation without an optimized kernel, perplexity-matched MoSA models are simultaneously faster in wall-clock time, require less memory for training, and drastically reduce the size of the KV-cache compared to the dense transformer baselines.

