---
layout: default
title: "OrthAlign: Orthogonal Subspace Decomposition for Non-Interfering Multi-Objective Alignment"
---

# OrthAlign: Orthogonal Subspace Decomposition for Non-Interfering Multi-Objective Alignment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24610" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24610v2</a>
  <a href="https://arxiv.org/pdf/2509.24610.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24610v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24610v2', 'OrthAlign: Orthogonal Subspace Decomposition for Non-Interfering Multi-Objective Alignment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Liang Lin, Zhihao Xu, Junhao Dong, Jian Zhao, Yuchen Yuan, Guibin Zhang, Miao Yu, Yiming Zhang, Zhengtao Yao, Huahui Yi, Dongrui Liu, Xinfeng Li, Kun Wang

**分类**: cs.LG, cs.CL

**发布日期**: 2025-09-29 (更新: 2025-09-30)

---

## 💡 一句话要点

**OrthAlign：正交子空间分解解决大模型多目标对齐中的冲突问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型对齐` `多目标优化` `正交子空间分解` `梯度冲突` `参数更新`

## 📋 核心要点

1. 现有大模型对齐方法在多目标优化时，难以避免不同偏好间的冲突和权衡，导致性能下降。
2. OrthAlign通过正交子空间分解，将参数更新空间分解为互不干扰的子空间，从而解决梯度冲突。
3. 实验表明，OrthAlign在多个偏好维度上实现了显著的性能提升，并保证了训练的稳定性。

## 📝 摘要（中文）

大型语言模型（LLM）对齐在解决多个人类偏好时面临一个关键困境：在一个维度上的改进常常以牺牲其他维度为代价，从而在诸如helpfulness和harmlessness等相互竞争的目标之间产生不可避免的权衡。以往的工作主要集中于基于约束的优化算法和数据选择策略来缓解冲突，但这些方法忽略了在参数层面直接解决冲突的根本问题。本文提出OrthAlign，这是一种创新的方法，它通过利用正交子空间分解来从根本上解决多目标偏好对齐中的梯度级冲突，从而开创了一种新的范例。OrthAlign策略性地将参数更新空间分解为正交子空间，确保针对不同偏好的优化发生在数学上互不干扰的方向上。在此基础上，我们提供了理论保证，证明当参数增量满足正交子空间约束和谱范数界限时，所得到的更新表现出线性Lipschitz增长而不是指数不稳定，从而确保所有偏好维度上的稳定收敛。大量实验表明：I. 在helpful、harmless和truthful维度上进行多目标对齐后，OrthAlign实现了34.61%到50.89%的最大单偏好改进。II. 平均总体奖励提高了13.96%。

## 🔬 方法详解

**问题定义**：大型语言模型对齐旨在使模型的行为符合人类的偏好，例如helpfulness（乐于助人）、harmlessness（无害）和truthfulness（真实）。然而，直接优化这些目标通常会导致冲突，即提高一个目标的性能可能会降低另一个目标的性能。现有的方法，如基于约束的优化和数据选择，试图缓解这些冲突，但未能从根本上解决参数层面的冲突问题。

**核心思路**：OrthAlign的核心思想是将参数更新空间分解为多个正交子空间，每个子空间对应一个特定的偏好目标。通过在这些正交子空间中进行优化，可以确保不同偏好目标的更新互不干扰，从而避免冲突和权衡。这种方法类似于在多维空间中寻找相互垂直的方向，使得沿着一个方向的移动不会影响其他方向的位置。

**技术框架**：OrthAlign的整体框架包括以下几个主要步骤：1. **梯度计算**：计算模型在每个偏好目标上的梯度。2. **子空间分解**：使用正交子空间分解技术，将参数更新空间分解为多个正交子空间，每个子空间对应一个偏好目标。3. **梯度投影**：将每个偏好目标的梯度投影到其对应的正交子空间中。4. **参数更新**：使用投影后的梯度更新模型参数。5. **稳定性保证**：通过谱范数约束，确保参数更新的稳定性。

**关键创新**：OrthAlign最重要的技术创新点在于其使用正交子空间分解来解决多目标对齐中的梯度冲突。与现有方法不同，OrthAlign直接在参数层面解决冲突，而不是试图通过约束或数据选择来缓解冲突。这种方法可以更有效地避免不同偏好目标之间的权衡，并提高整体性能。

**关键设计**：OrthAlign的关键设计包括：1. **正交子空间分解方法**：具体采用何种正交化方法（例如Gram-Schmidt正交化）来分解参数空间。2. **谱范数约束**：为了保证训练的稳定性，论文引入了谱范数约束来限制参数更新的幅度。3. **损失函数设计**：针对不同的偏好目标，设计合适的损失函数来指导模型的训练。

## 📊 实验亮点

OrthAlign在helpful、harmless和truthful三个维度上进行了实验，结果表明，该方法在多目标对齐后，实现了34.61%到50.89%的最大单偏好改进。此外，OrthAlign的平均总体奖励提高了13.96%，证明了其在解决多目标冲突方面的有效性。这些结果表明，OrthAlign是一种有前景的多目标对齐方法。

## 🎯 应用场景

OrthAlign技术可应用于各种需要多目标对齐的大型语言模型应用场景，例如对话系统、内容生成和智能助手。通过确保不同目标之间的平衡，可以提高模型的整体性能和用户满意度。该技术还有潜力应用于其他机器学习领域，例如多任务学习和强化学习。

## 📄 摘要（原文）

> Large language model (LLM) alignment faces a critical dilemma when addressing multiple human preferences: improvements in one dimension frequently come at the expense of others, creating unavoidable trade-offs between competing objectives like helpfulness and harmlessness. While prior work mainly focuses on constraint-based optimization algorithms and data selection strategies to mitigate conflicts, these approaches overlook the fundamental issue of resolving conflicts directly at the parameter level. In this paper, we present OrthAlign, an innovative approach that pioneers a new paradigm by leveraging orthogonal subspace decomposition to fundamentally resolve gradient-level conflicts in multi-objective preference alignment. OrthAlign strategically decomposes parameter update spaces into orthogonal subspaces, ensuring that optimization toward different preferences occurs in mathematically non-interfering directions. Building upon this, we provide theoretical guarantees demonstrating that when parameter increments satisfy both orthogonal subspace constraints and spectral norm bounds, the resulting updates exhibit linear Lipschitz growth rather than exponential instability, ensuring stable convergence across all preference dimensions. Extensive experiments show that: I. OrthAlign achieves maximum single-preference improvements ranging from 34.61% to 50.89% after multiple-objective alignment across helpful, harmless, and truthful dimensions. II. With an average overall reward improvement of 13.96%.

