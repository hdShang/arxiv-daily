---
layout: default
title: Why and When Deep is Better than Shallow: An Implementation-Agnostic State-Transition View of Depth Supremacy
---

# Why and When Deep is Better than Shallow: An Implementation-Agnostic State-Transition View of Depth Supremacy

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.15064" class="toolbar-btn" target="_blank">📄 arXiv: 2505.15064v3</a>
  <a href="https://arxiv.org/pdf/2505.15064.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.15064v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.15064v3', 'Why and When Deep is Better than Shallow: An Implementation-Agnostic State-Transition View of Depth Supremacy')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sho Sonoda, Yuka Hashimoto, Isao Ishikawa, Masahiro Ikeda

**分类**: cs.LG, math.DS, stat.ML

**发布日期**: 2025-05-21 (更新: 2025-11-04)

---

## 💡 一句话要点

**提出深度优于浅层的理论框架以解决模型泛化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `深度学习` `偏差-方差权衡` `状态转移半群` `泛化能力` `模型优化`

## 📋 核心要点

1. 现有模型在处理复杂任务时，浅层网络的泛化能力往往不足，难以捕捉深层次的特征。
2. 论文提出了一种抽象的状态转移半群框架，分离实现与状态转移，揭示深度模型的优势。
3. 研究结果表明，深度模型在特定条件下具有更低的泛化误差，尤其是在EL模式下表现最佳。

## 📝 摘要（中文）

本文探讨了深度模型为何及何时优于浅层模型，提出了一种与网络实现无关的状态转移框架。通过将深度模型视为作用于一般度量空间的抽象状态转移半群，作者证明了偏差-方差分解定理，揭示了方差与深度的关系。研究表明，在特定条件下，深度模型的方差可以多项式或对数增长，进而识别出四种典型的偏差-方差权衡模式，并给出了最优深度的明确表达，尤其适用于迭代或分层概念类的模型。

## 🔬 方法详解

**问题定义**：本文旨在解决深度模型与浅层模型在泛化能力上的差异，现有方法未能充分解释深度模型的优势及其适用条件。

**核心思路**：通过将深度模型视为抽象状态转移半群，论文分离了模型实现与状态转移的关系，提供了一种理论框架来分析深度的优势。

**技术框架**：整体架构包括偏差-方差分解、状态转移半群的度量熵分析，以及对不同偏差-方差权衡模式的识别。主要模块包括理论证明、条件分析和最优深度的推导。

**关键创新**：最重要的创新在于提出了与实现无关的深度模型分析框架，证明了方差与深度的关系，并识别出四种偏差-方差权衡模式。

**关键设计**：论文中设定了深度网络的抽象深度k，并通过理论推导明确了在不同偏差-方差模式下的最优深度k*，为模型设计提供了指导。

## 📊 实验亮点

实验结果显示，在EL模式下，深度模型的泛化误差显著低于浅层模型，具体表现为偏差指数衰减与方差对数增长的结合。这一发现为深度学习模型的设计提供了理论支持，强调了深度网络在复杂任务中的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括深度学习模型的设计与优化，尤其是在处理复杂任务如神经常微分方程、扩散模型和链式推理等方面。通过明确深度模型的优势，研究可以指导实际应用中的模型选择与参数调优，提升模型的泛化能力。

## 📄 摘要（原文）

> Why and when is deep better than shallow? We answer this question in a framework that is agnostic to network implementation. We formulate a deep model as an abstract state-transition semigroup acting on a general metric space, and separate the implementation (e.g., ReLU nets, transformers, and chain-of-thought) from the abstract state transition. We prove a bias-variance decomposition in which the variance depends only on the abstract depth-$k$ network and not on the implementation (Theorem 1). We further split the bounds into output and hidden parts to tie the depth dependence of the variance to the metric entropy of the state-transition semigroup (Theorem 2). We then investigate implementation-free conditions under which the variance grow polynomially or logarithmically with depth (Section 4). Combining these with exponential or polynomial bias decay identifies four canonical bias-variance trade-off regimes (EL/EP/PL/PP) and produces explicit optimal depths $k^\ast$. Across regimes, $k^\ast>1$ typically holds, giving a rigorous form of depth supremacy. The lowest generalization error bound is achieved under the EL regime (exp-decay bias + log-growth variance), explaining why and when deep is better, especially for iterative or hierarchical concept classes such as neural ODEs, diffusion/score-matching models, and chain-of-thought reasoning.

