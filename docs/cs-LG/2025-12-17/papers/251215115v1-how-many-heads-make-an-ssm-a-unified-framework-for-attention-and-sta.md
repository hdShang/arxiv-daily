---
layout: default
title: How Many Heads Make an SSM? A Unified Framework for Attention and State Space Models
---

# How Many Heads Make an SSM? A Unified Framework for Attention and State Space Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15115" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15115v1</a>
  <a href="https://arxiv.org/pdf/2512.15115.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15115v1" onclick="toggleFavorite(this, '2512.15115v1', 'How Many Heads Make an SSM? A Unified Framework for Attention and State Space Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ali Ghodsi

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-17

---

## 💡 一句话要点

**提出统一框架，分析Attention和状态空间模型(SSM)的表达能力与训练权衡。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `序列建模` `状态空间模型` `注意力机制` `统一框架` `表达能力` `梯度传播` `理论分析`

## 📋 核心要点

1. 现有序列模型架构多样，缺乏统一的理论理解来权衡表达能力和训练难度。
2. 提出统一框架，通过输入相关的交互算子显式地表示Attention和SSM的共性。
3. 理论分析揭示了Attention和SSM在表达能力和梯度传播上的根本权衡。

## 📝 摘要（中文）

序列建模产生了多种架构，从经典循环神经网络到现代Transformer和状态空间模型(SSM)，但对于表达能力和训练权衡的统一理论理解仍然有限。我们引入了一个统一框架，通过输入相关的有效交互算子$W_{ij}(X)$来表示广泛的序列映射类别，明确了两种重复出现的构造模式：(i) 统一分解框架（显式）（注意力式混合），其中$W_{ij}(X)$通过应用于共享值映射的标量系数而变化，以及(ii) 结构化动态（隐式）（状态空间递归），其中$W_{ij}$由潜在的动态系统引起。使用这个框架，我们推导出了三个理论结果。首先，我们建立了交互秩间隙：统一分解框架中的模型，例如单头注意力，被限制在低维算子跨度内，并且不能表示某些结构化动态映射。其次，我们证明了一个等价（头数）定理，表明在我们的多头分解类中，表示一个线性SSM，其滞后算子跨越长度为n的序列上的k维子空间需要且可以用H=k个头来实现。第三，我们证明了一个梯度高速公路结果，表明注意力层允许具有距离无关梯度路径的输入，而稳定的线性动态表现出距离相关的梯度衰减。总之，这些结果形式化了代数表达能力（交互/算子跨度）和长程梯度传播之间的基本权衡，为现代序列架构设计提供了理论基础。

## 🔬 方法详解

**问题定义**：论文旨在解决序列建模领域中，不同架构（如RNN、Transformer、SSM）之间缺乏统一理论框架的问题。现有方法难以解释这些架构在表达能力和训练效率上的差异，阻碍了新型序列模型的有效设计。

**核心思路**：论文的核心思路是构建一个统一的数学框架，将不同的序列模型架构表示为输入相关的有效交互算子。通过分析这些算子的性质，可以揭示不同架构在表达能力和梯度传播上的内在联系与权衡。该框架将Attention机制和状态空间模型视为两种不同的交互模式：显式的分解交互（Attention）和隐式的结构化动态交互（SSM）。

**技术框架**：该框架的核心是使用一个输入相关的有效交互算子 $W_{ij}(X)$ 来表示序列映射。该算子描述了序列中第 i 个位置和第 j 个位置之间的交互强度。论文提出了两种主要的构造模式：

1. **统一分解框架（显式）**：类似于Attention机制，通过标量系数对共享的值映射进行加权混合。

2. **结构化动态（隐式）**：类似于SSM，通过潜在的动态系统来诱导交互算子。

基于此框架，论文推导出了三个关键的理论结果：交互秩间隙、头数等价定理和梯度高速公路结果。

**关键创新**：最重要的技术创新点在于提出了一个统一的框架，能够同时表示Attention机制和状态空间模型，并在此基础上进行理论分析。与以往针对特定架构的分析不同，该框架能够揭示不同架构之间的共性和差异，为序列模型的设计提供了更通用的指导。

**关键设计**：论文的关键设计包括：

1.  **交互算子 $W_{ij}(X)$ 的定义**：该算子是连接不同架构的关键，其具体形式取决于所表示的架构。

2.  **两种构造模式的区分**：显式分解交互和隐式结构化动态交互代表了两种不同的建模思路。

3.  **理论结果的推导**：通过数学推导，论文建立了交互秩、头数和梯度传播等关键性质之间的联系。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15115v1/experiment_results_full.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15115v1/experiment_gradient_flow.png" alt="fig_1" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文证明了单头Attention模型存在交互秩间隙，无法表示某些结构化动态映射。头数等价定理表明，表示k维线性SSM需要且仅需要k个头。梯度高速公路结果揭示了Attention和SSM在梯度传播上的差异，Attention允许距离无关的梯度路径，而SSM则表现出距离相关的梯度衰减。

## 🎯 应用场景

该研究成果可应用于序列建模的各个领域，例如自然语言处理、语音识别、时间序列分析等。通过理解不同架构的表达能力和训练权衡，可以指导新型序列模型的有效设计，提升模型性能和训练效率。此外，该框架还可以用于分析现有模型的局限性，并针对性地进行改进。

## 📄 摘要（原文）

> Sequence modeling has produced diverse architectures -- from classical recurrent neural networks to modern Transformers and state space models (SSMs) -- yet a unified theoretical understanding of expressivity and trainability trade-offs remains limited. We introduce a unified framework that represents a broad class of sequence maps via an input-dependent effective interaction operator $W_{ij}(X)$, making explicit two recurring construction patterns: (i) the Unified Factorized Framework (Explicit) (attention-style mixing), in which $W_{ij}(X)$ varies through scalar coefficients applied to shared value maps, and (ii) Structured Dynamics (Implicit) (state-space recurrences), in which $W_{ij}$ is induced by a latent dynamical system. Using this framework, we derive three theoretical results. First, we establish the Interaction Rank Gap: models in the Unified Factorized Framework, such as single-head attention, are constrained to a low-dimensional operator span and cannot represent certain structured dynamical maps. Second, we prove an Equivalence (Head-Count) Theorem showing that, within our multi-head factorized class, representing a linear SSM whose lag operators span a $k$-dimensional subspace on length-$n$ sequences requires and is achievable with $H=k$ heads. Third, we prove a Gradient Highway Result, showing that attention layers admit inputs with distance-independent gradient paths, whereas stable linear dynamics exhibit distance-dependent gradient attenuation. Together, these results formalize a fundamental trade-off between algebraic expressivity (interaction/operator span) and long-range gradient propagation, providing theoretical grounding for modern sequence architecture design.

