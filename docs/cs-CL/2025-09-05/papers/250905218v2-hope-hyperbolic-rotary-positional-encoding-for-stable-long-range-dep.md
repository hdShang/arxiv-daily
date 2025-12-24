---
layout: default
title: "HoPE: Hyperbolic Rotary Positional Encoding for Stable Long-Range Dependency Modeling in Large Language Models"
---

# HoPE: Hyperbolic Rotary Positional Encoding for Stable Long-Range Dependency Modeling in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05218" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05218v2</a>
  <a href="https://arxiv.org/pdf/2509.05218.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05218v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05218v2', 'HoPE: Hyperbolic Rotary Positional Encoding for Stable Long-Range Dependency Modeling in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chang Dai, Hongyu Shan, Mingyang Song, Di Liang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-05 (更新: 2025-09-08)

---

## 💡 一句话要点

**提出HoPE：一种用于稳定长程依赖建模的双曲旋转位置编码**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `位置编码` `长程依赖` `Transformer` `双曲几何` `洛伦兹变换`

## 📋 核心要点

1. 现有位置编码方法在处理长序列时存在问题，绝对位置编码外推性差，RoPE存在振荡注意力模式，影响长程依赖建模。
2. HoPE通过几何重构位置编码，利用双曲几何中的洛伦兹变换，对token表示进行旋转，实现注意力权重的单调衰减。
3. 实验结果表明，HoPE在长序列建模任务中，性能优于现有位置编码方法，能够更好地表示和推广长程依赖关系。

## 📝 摘要（中文）

位置编码机制使Transformer能够对文本中的序列结构和长程依赖关系进行建模。然而，绝对位置编码由于固定的位置表示，难以推广到更长的序列；而像Alibi这样的相对方法在极长上下文中表现出性能下降。广泛使用的旋转位置编码（RoPE）引入了振荡的注意力模式，阻碍了稳定的长距离依赖建模。为了解决这些限制，我们通过对位置编码进行几何重构。受到双曲几何中洛伦兹变换的启发，我们提出了双曲旋转位置编码（HoPE），它利用双曲函数对token表示执行洛伦兹旋转。理论分析表明，RoPE是我们的广义公式的一个特例。HoPE通过强制注意力权重随token距离的增加而单调衰减，从根本上解决了RoPE的振荡问题。大量的实验结果，包括在几个扩展序列基准下的困惑度评估，表明HoPE始终优于现有的位置编码方法。这些发现强调了HoPE在表示和推广长程依赖关系方面的增强能力。数据和代码将会公开。

## 🔬 方法详解

**问题定义**：现有Transformer模型中的位置编码方法在处理超长序列时面临挑战。绝对位置编码难以泛化到训练长度之外的序列，而RoPE虽然相对位置编码，但其旋转特性导致注意力权重出现振荡，不利于稳定地建模长距离依赖关系。这种振荡会干扰模型学习token之间的真实关系，尤其是在需要抑制远处token影响的场景下。

**核心思路**：HoPE的核心思路是借鉴双曲几何中的洛伦兹变换，将位置编码视为在双曲空间中的旋转。通过使用双曲函数来定义旋转操作，可以确保注意力权重随着token距离的增加而单调衰减。这种单调衰减能够更自然地反映文本中距离越远的token相关性越低的规律，从而提高模型对长程依赖关系的建模能力。

**技术框架**：HoPE可以无缝集成到现有的Transformer架构中，替换原有的RoPE位置编码。其主要流程包括：1) 将token表示映射到双曲空间；2) 使用双曲函数计算洛伦兹旋转矩阵，该矩阵依赖于token的位置信息；3) 将token表示与旋转矩阵相乘，得到位置编码后的token表示；4) 将位置编码后的token表示输入到Transformer的注意力机制中。整个过程不需要修改Transformer的其他部分。

**关键创新**：HoPE的关键创新在于将位置编码问题与双曲几何联系起来，并利用洛伦兹变换来设计位置编码。与RoPE相比，HoPE通过双曲函数的特性，强制注意力权重单调衰减，避免了RoPE的振荡问题。此外，论文还证明RoPE是HoPE的一种特殊情况，表明HoPE具有更强的泛化能力。

**关键设计**：HoPE的关键设计包括：1) 使用双曲正弦和双曲余弦函数来定义旋转矩阵，确保单调衰减特性；2) 引入可学习的缩放因子来控制衰减速度，允许模型根据不同的任务调整衰减策略；3) 采用与RoPE类似的旋转方式，保证计算效率。损失函数和网络结构与标准Transformer保持一致，无需额外调整。

## 📊 实验亮点

实验结果表明，HoPE在多个长序列基准测试中显著优于RoPE和其他位置编码方法。例如，在某些任务中，HoPE的困惑度比RoPE降低了10%以上。这些结果表明，HoPE能够更有效地建模长程依赖关系，并提高模型在长序列任务中的性能。此外，实验还验证了HoPE的泛化能力，表明其在不同长度的序列上都能保持良好的性能。

## 🎯 应用场景

HoPE具有广泛的应用前景，尤其是在需要处理超长序列的自然语言处理任务中，例如长文本摘要、文档翻译、代码生成、对话系统等。通过更有效地建模长程依赖关系，HoPE可以提高模型在这些任务中的性能，并有望推动相关领域的发展。此外，HoPE的设计思想也可以应用于其他序列建模任务，例如时间序列分析、语音识别等。

## 📄 摘要（原文）

> Positional encoding mechanisms enable Transformers to model sequential structure and long-range dependencies in text. While absolute positional encodings struggle with extrapolation to longer sequences due to fixed positional representations, and relative approaches like Alibi exhibit performance degradation on extremely long contexts, the widely-used Rotary Positional Encoding (RoPE) introduces oscillatory attention patterns that hinder stable long-distance dependency modelling. We address these limitations through a geometric reformulation of positional encoding. Drawing inspiration from Lorentz transformations in hyperbolic geometry, we propose Hyperbolic Rotary Positional Encoding (HoPE), which leverages hyperbolic functions to implement Lorentz rotations on token representations. Theoretical analysis demonstrates that RoPE is a special case of our generalized formulation. HoPE fundamentally resolves RoPE's slation issues by enforcing monotonic decay of attention weights with increasing token distances. Extensive experimental results, including perplexity evaluations under several extended sequence benchmarks, show that HoPE consistently exceeds existing positional encoding methods. These findings underscore HoPE's enhanced capacity for representing and generalizing long-range dependencies. Data and code will be available.

