---
layout: default
title: "ProxyAttn: Guided Sparse Attention via Representative Heads"
---

# ProxyAttn: Guided Sparse Attention via Representative Heads

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24745" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24745v1</a>
  <a href="https://arxiv.org/pdf/2509.24745.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24745v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24745v1', 'ProxyAttn: Guided Sparse Attention via Representative Heads')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yixuan Wang, Huang He, Siqi Bao, Hua Wu, Haifeng Wang, Qingfu Zhu, Wanxiang Che

**分类**: cs.CL, cs.LG

**发布日期**: 2025-09-29

**备注**: 14pages, 5figures

**🔗 代码/项目**: [GITHUB](https://github.com/wyxstriker/ProxyAttn)

---

## 💡 一句话要点

**ProxyAttn：通过代表性注意力头引导的稀疏注意力机制，加速长文本处理。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `稀疏注意力` `长文本处理` `大型语言模型` `注意力机制加速` `代表性注意力头`

## 📋 核心要点

1. 现有块稀疏注意力方法在长文本处理中面临高稀疏率下性能下降的挑战，因为其块重要性估计过于粗糙。
2. ProxyAttn通过选择代表性注意力头，并利用其得分近似所有头的得分，从而实现更精确的块重要性评估。
3. 实验表明，ProxyAttn在多种模型和基准测试中，显著提升了性能和效率，实现了高达10.3倍的注意力加速。

## 📝 摘要（中文）

注意力机制的二次复杂度限制了大型语言模型（LLM）在长文本任务上的效率。最近，动态估计块重要性的方法实现了高效的块稀疏注意力，显著加速了LLM的长文本预填充。然而，它们粗粒度的估计不可避免地导致在高稀疏率下的性能下降。本文提出了ProxyAttn，一种无需训练的稀疏注意力算法，通过压缩注意力头的维度来实现更精确的块估计。基于对多个注意力头之间相似性的观察，我们使用池化的代表性注意力头的分数来近似所有头的分数。为了解决不同头之间的不同稀疏性，我们还提出了一种块感知的动态预算估计方法。通过将来自代表性代理头的分数与多头动态预算相结合，我们以较低的计算成本实现了更细粒度的块重要性评估。在各种主流模型和广泛基准上的实验证实了注意力头之间潜在的相似性。利用细粒度的估计，所提出的方法与现有方法相比，在性能和效率方面都取得了显著的提升。更准确地说，ProxyAttn可以在不显著损失性能的情况下，实现高达10.3倍的注意力加速和2.4倍的预填充加速。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型在处理长文本时，由于注意力机制的二次复杂度而导致的效率瓶颈问题。现有的块稀疏注意力方法虽然能够加速计算，但由于其粗粒度的块重要性估计，在高稀疏率下会造成显著的性能损失。

**核心思路**：论文的核心思路是利用多个注意力头之间的相似性，通过少量“代表性”的注意力头来近似所有注意力头的行为。具体来说，选择一部分注意力头作为代理（Proxy），并使用它们的得分来估计整个注意力块的重要性。这样可以在降低计算复杂度的同时，保持较高的估计精度。

**技术框架**：ProxyAttn算法主要包含以下几个阶段：1) **代表性注意力头选择**：选择一部分注意力头作为代理头。选择策略未知，论文中可能默认随机选择或使用某种启发式方法。2) **代理头得分计算**：计算这些代理头的注意力得分。3) **块重要性估计**：使用代理头的得分来近似整个注意力块的重要性。4) **动态预算分配**：根据块的重要性，动态地为每个块分配计算资源。5) **稀疏注意力计算**：只对重要的块进行注意力计算，从而实现加速。

**关键创新**：ProxyAttn的关键创新在于利用注意力头之间的相似性，通过代理头来近似整个注意力块的重要性。这种方法能够在降低计算复杂度的同时，保持较高的估计精度，从而在高稀疏率下也能获得较好的性能。与现有方法相比，ProxyAttn的块重要性估计更加精细，能够更准确地识别重要的块。

**关键设计**：论文提出了块感知的动态预算估计方法，以解决不同头之间的不同稀疏性。具体的技术细节，如代表性注意力头的选择策略、代理头得分的池化方法、以及动态预算分配的具体算法，在论文中可能没有详细描述，需要进一步研究代码才能确定。损失函数未知，网络结构与原始Transformer保持一致。

## 📊 实验亮点

ProxyAttn在多种主流模型和基准测试中取得了显著的性能提升。实验结果表明，ProxyAttn可以在不显著损失性能的情况下，实现高达10.3倍的注意力加速和2.4倍的预填充加速。这表明ProxyAttn能够有效地降低计算复杂度，并提升长文本处理的效率。

## 🎯 应用场景

ProxyAttn可应用于各种需要处理长文本的大型语言模型，例如文档摘要、机器翻译、问答系统等。通过加速注意力计算，ProxyAttn能够提升这些应用的处理速度和效率，使其能够处理更长的文本，并降低计算成本。该方法还有潜力应用于其他类型的注意力机制，例如视觉Transformer等。

## 📄 摘要（原文）

> The quadratic complexity of attention mechanisms limits the efficiency of Large Language Models (LLMs) on long-text tasks. Recently, methods that dynamically estimate block importance have enabled efficient block sparse attention, leading to significant acceleration in long-text pre-filling of LLMs. However, their coarse-grained estimation inevitably leads to performance degradation at high sparsity rates. In this work, we propose ProxyAttn, a training-free sparse attention algorithm that achieves more precise block estimation by compressing the dimension of attention heads. Based on our observation of the similarity among multiple attention heads, we use the scores of pooled representative heads to approximate the scores for all heads. To account for the varying sparsity among heads, we also propose a block-aware dynamic budget estimation method. By combining the scores from representative proxy heads with multi-head dynamic budgets, we achieve a more fine-grained block importance evaluation at low computational cost. Experiments on a variety of mainstream models and extensive benchmarks confirm the underlying similarity among attention heads. Leveraging a fine-grained estimation, the proposed method achieves substantial gains in performance and efficiency compared to existing methods. More precisely, ProxyAttn can achieve up to 10.3x attention acceleration and 2.4x prefilling acceleration without significant performance loss. Our code is available at https://github.com/wyxstriker/ProxyAttn.

