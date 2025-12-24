---
layout: default
title: "LOTFormer: Doubly-Stochastic Linear Attention via Low-Rank Optimal Transport"
---

# LOTFormer: Doubly-Stochastic Linear Attention via Low-Rank Optimal Transport

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23436" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23436v1</a>
  <a href="https://arxiv.org/pdf/2509.23436.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23436v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23436v1', 'LOTFormer: Doubly-Stochastic Linear Attention via Low-Rank Optimal Transport')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ashkan Shahbazi, Chayne Thrash, Yikun Bai, Keaton Hamm, Navid NaderiAlizadeh, Soheil Kolouri

**分类**: cs.LG

**发布日期**: 2025-09-27

---

## 💡 一句话要点

**LOTFormer：通过低秩最优传输实现双重随机线性注意力机制，提升长序列建模效率。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `线性注意力` `最优传输` `双重随机` `低秩近似` `长序列建模`

## 📋 核心要点

1. 传统Transformer注意力机制的二次复杂度限制了其在长序列上的应用，容易过度关注少量token。
2. LOTFormer通过低秩最优传输，将注意力矩阵约束为双重随机，保证信息均衡流动，提升鲁棒性。
3. 实验表明，LOTFormer在长序列基准测试中超越了现有线性注意力和基于传输的方法，兼顾精度与效率。

## 📝 摘要（中文）

Transformer在各种模态中都表现出高效性。然而，标准softmax注意力机制的二次复杂度对将其扩展到长上下文窗口构成了根本障碍。大量工作通过线性注意力来解决这个问题，线性注意力将注意力重新表述为核函数，并用有限的特征图来近似它，以实现线性时间计算。与计算扩展正交，大多数注意力机制——无论是二次的还是线性的——都会产生行归一化的映射，这些映射可能会过度关注少数几个token，从而降低鲁棒性和信息流。强制执行双重随机注意力可以通过平衡行和列之间的token参与来缓解这个问题，但现有的双重随机注意力机制通常会引入大量的开销，从而破坏可扩展性。我们提出了LOTFormer，这是一种既是线性时间又是双重随机的原则性注意力机制。我们的方法利用了注意力图和查询和键度量之间的传输计划之间的联系。核心思想是通过将其限制在具有小支撑的可学习枢轴度量上来约束传输计划为低秩。具体来说，我们解决了两个熵最优传输问题（queries → pivot 和 pivot → keys）并将它们组合成一个条件（粘合）耦合。这产生了一个注意力矩阵，该矩阵可证明是双重随机的，秩最多为r << n，并在O(nr)时间内应用于值，而无需形成完整的n × n映射。枢轴位置和质量是端到端学习的。在经验上，LOTFormer在Long Range Arena基准测试中取得了最先进的结果，在准确性和效率方面都超过了之前的线性和基于传输的注意力方法。

## 🔬 方法详解

**问题定义**：Transformer模型中的标准softmax注意力机制计算复杂度为O(n^2)，其中n是序列长度。这使得Transformer难以处理长序列。此外，softmax注意力倾向于生成行归一化的注意力权重，导致模型过度关注少数几个token，降低了模型的鲁棒性和信息流动性。

**核心思路**：LOTFormer的核心思想是将注意力机制视为查询和键之间的最优传输问题。通过引入一个低秩的枢轴度量，将原本的直接传输问题分解为两个子问题：查询到枢轴的传输和枢轴到键的传输。这种分解使得注意力矩阵具有低秩性质，从而降低了计算复杂度。同时，通过最优传输的性质，保证了注意力矩阵是双重随机的，从而平衡了token之间的参与度。

**技术框架**：LOTFormer包含以下主要步骤：1. **枢轴度量学习**：学习一组枢轴点的位置和权重。2. **查询到枢轴的传输**：计算查询和枢轴之间的最优传输计划。3. **枢轴到键的传输**：计算枢轴和键之间的最优传输计划。4. **注意力矩阵构建**：将两个传输计划组合成一个条件耦合，得到最终的注意力矩阵。5. **值加权**：使用注意力矩阵对值进行加权，得到最终的输出。

**关键创新**：LOTFormer的关键创新在于：1. **低秩最优传输**：通过引入低秩枢轴度量，将注意力计算的复杂度从O(n^2)降低到O(nr)，其中r是枢轴点的数量，通常远小于n。2. **双重随机注意力**：通过最优传输的性质，保证了注意力矩阵是双重随机的，从而平衡了token之间的参与度，提高了模型的鲁棒性。

**关键设计**：LOTFormer的关键设计包括：1. **熵正则化**：在最优传输问题中引入熵正则化项，以保证传输计划的光滑性。2. **枢轴点数量的选择**：枢轴点的数量r需要根据具体的任务和数据集进行调整，以平衡计算复杂度和模型性能。3. **端到端学习**：枢轴点的位置和权重以及其他模型参数都是通过端到端的方式进行学习的。

## 📊 实验亮点

LOTFormer在Long Range Arena (LRA) 基准测试中取得了state-of-the-art的结果，超越了之前的线性注意力和基于传输的方法。具体来说，LOTFormer在多个LRA任务上都取得了显著的性能提升，同时保持了较高的计算效率。例如，在Pathfinder任务上，LOTFormer的准确率超过了现有最佳方法。

## 🎯 应用场景

LOTFormer适用于需要处理长序列数据的各种应用场景，例如：长文本建模、音频处理、视频理解、基因组分析等。其高效的计算复杂度和鲁棒性使其能够处理更大规模的数据，并提高模型的性能。未来，LOTFormer有望成为长序列建模领域的重要技术。

## 📄 摘要（原文）

> Transformers have proven highly effective across a wide range of modalities. However, the quadratic complexity of the standard softmax attention mechanism poses a fundamental barrier to scaling them to long context windows. A large body of work addresses this with linear attention, which reformulates attention as a kernel function and approximates it with finite feature maps to achieve linear-time computation. Orthogonal to computational scaling, most attention mechanisms -- both quadratic and linear -- produce row-normalized maps that can over-focus on a few tokens, degrading robustness and information flow. Enforcing doubly-stochastic attention alleviates this by balancing token participation across rows and columns, but existing doubly-stochastic attention mechanisms typically introduce substantial overhead, undermining scalability. We propose LOTFormer, a principled attention mechanism that is simultaneously linear-time and doubly-stochastic. Our approach exploits the connection between attention maps and transportation plans between query and key measures. The central idea is to constrain the transport plan to be low-rank by conditioning it on a learnable pivot measure with small support. Concretely, we solve two entropic optimal transport problems (queries $\to$ pivot and pivot $\to$ keys) and compose them into a conditional (glued) coupling. This yields an attention matrix that is provably doubly-stochastic, has rank at most $r \ll n$, and applies to values in $O(nr)$ time without forming the full $n \times n$ map. The pivot locations and masses are learned end-to-end. Empirically, LOTFormer achieves state-of-the-art results on the Long Range Arena benchmark, surpassing prior linear and transport-based attention methods in both accuracy and efficiency.

