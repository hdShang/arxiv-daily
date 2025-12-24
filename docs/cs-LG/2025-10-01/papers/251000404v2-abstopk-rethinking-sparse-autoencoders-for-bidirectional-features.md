---
layout: default
title: "AbsTopK: Rethinking Sparse Autoencoders For Bidirectional Features"
---

# AbsTopK: Rethinking Sparse Autoencoders For Bidirectional Features

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.00404" class="toolbar-btn" target="_blank">📄 arXiv: 2510.00404v2</a>
  <a href="https://arxiv.org/pdf/2510.00404.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00404v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.00404v2', 'AbsTopK: Rethinking Sparse Autoencoders For Bidirectional Features')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xudong Zhu, Mohammad Mahdi Khalili, Zhihui Zhu

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-10-01 (更新: 2025-10-02)

---

## 💡 一句话要点

**提出AbsTopK以解决稀疏自编码器的双向特征表示问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `稀疏自编码器` `双向特征` `可解释性` `大型语言模型` `语义表示` `机器学习` `深度学习`

## 📋 核心要点

1. 现有稀疏自编码器在表示双向概念时存在局限，导致语义轴碎片化，限制了表示的完整性。
2. 本文提出AbsTopK SAE，通过对最大幅度激活值进行硬阈值处理，保留正负激活，解决双向特征表示问题。
3. 在四个大型语言模型和七个探测与引导任务的实验中，AbsTopK在重构保真度和可解释性上均有显著提升。

## 📝 摘要（中文）

稀疏自编码器（SAEs）作为大型语言模型（LLMs）可解释性的重要技术，旨在将隐藏状态分解为有意义的语义特征。尽管已有多种SAE变体被提出，但缺乏从原始字典学习框架推导SAEs的原则性框架。本文通过展开稀疏编码的近端梯度方法，提出了这样一个框架。我们揭示了现有SAEs的一个基本局限性：其稀疏性诱导正则化器强制非负性，导致单一特征无法表示双向概念。为了解决这一问题，我们提出了AbsTopK SAE，通过对最大幅度激活值进行硬阈值处理，保留正负激活，从而揭示更丰富的双向概念表示。实验结果表明，AbsTopK在重构保真度、可解释性方面均有所提升，并且能够让单一特征编码对立概念。

## 🔬 方法详解

**问题定义**：本文旨在解决现有稀疏自编码器在表示双向概念时的局限性，现有方法的稀疏性诱导正则化器强制非负性，导致特征表示的碎片化和冗余。

**核心思路**：我们提出AbsTopK SAE，基于$	ext{l}_0$稀疏性约束，通过对最大幅度激活值进行硬阈值处理，保留正负激活，从而实现更丰富的双向概念表示。

**技术框架**：整体框架包括稀疏编码的近端梯度方法展开，AbsTopK的特征提取模块，以及重构和可解释性评估模块。

**关键创新**：AbsTopK SAE的核心创新在于其能够同时保留正负激活，打破了现有SAEs的非负性约束，从而实现双向概念的有效表示。

**关键设计**：在AbsTopK中，我们设计了硬阈值处理机制，确保最大幅度激活值的保留，同时在损失函数中引入了新的稀疏性约束，以优化特征表示的完整性。

## 📊 实验亮点

实验结果表明，AbsTopK在重构保真度上显著提升，且在可解释性方面超越了现有的SAE变体。与需要标注数据的监督方法Difference-in-Mean相比，AbsTopK的表现相当甚至更优，展示了其在无监督学习中的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、图像理解和多模态学习等。通过提升稀疏自编码器的可解释性和表示能力，AbsTopK SAE能够为理解大型语言模型的内部机制提供更有效的工具，进而推动相关领域的研究与应用发展。

## 📄 摘要（原文）

> Sparse autoencoders (SAEs) have emerged as powerful techniques for interpretability of large language models (LLMs), aiming to decompose hidden states into meaningful semantic features. While several SAE variants have been proposed, there remains no principled framework to derive SAEs from the original dictionary learning formulation. In this work, we introduce such a framework by unrolling the proximal gradient method for sparse coding. We show that a single-step update naturally recovers common SAE variants, including ReLU, JumpReLU, and TopK. Through this lens, we reveal a fundamental limitation of existing SAEs: their sparsity-inducing regularizers enforce non-negativity, preventing a single feature from representing bidirectional concepts (e.g., male vs. female). This structural constraint fragments semantic axes into separate, redundant features, limiting representational completeness. To address this issue, we propose AbsTopK SAE, a new variant derived from the $\ell_0$ sparsity constraint that applies hard thresholding over the largest-magnitude activations. By preserving both positive and negative activations, AbsTopK uncovers richer, bidirectional conceptual representations. Comprehensive experiments across four LLMs and seven probing and steering tasks show that AbsTopK improves reconstruction fidelity, enhances interpretability, and enables single features to encode contrasting concepts. Remarkably, AbsTopK matches or even surpasses the Difference-in-Mean method, a supervised approach that requires labeled data for each concept and has been shown in prior work to outperform SAEs.

