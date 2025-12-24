---
layout: default
title: "S2Sent: Nested Selectivity Aware Sentence Representation Learning"
---

# S2Sent: Nested Selectivity Aware Sentence Representation Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18164" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18164v1</a>
  <a href="https://arxiv.org/pdf/2508.18164.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18164v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18164v1', 'S2Sent: Nested Selectivity Aware Sentence Representation Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jianxiang Zang, Nijia Mo, Yonda Wei, Meiling Ning, Hui Liu

**分类**: cs.CL

**发布日期**: 2025-08-25

---

## 💡 一句话要点

**提出S2Sent以优化Transformer句子表示学习中的语义选择问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `句子表示` `Transformer` `对比学习` `嵌套选择` `语义感知` `信息冗余` `自然语言处理` `深度学习`

## 📋 核心要点

1. 现有的基于Transformer的句子表示学习方法在不同块的语义感知能力上存在差异，导致信息冗余和语义损失问题。
2. 本文提出的S2Sent机制通过参数化的嵌套选择器，结合空间选择和嵌套频率选择，优化了句子表示的融合过程。
3. 实验结果显示，S2Sent在多个基准测试中显著提升了性能，且额外的参数和推理延迟几乎可以忽略不计。

## 📝 摘要（中文）

当前主流的句子表示学习方法结合了基于Transformer的编码器与对比学习，通常依赖于编码器最后一个Transformer块的隐藏状态。然而，不同块在语义感知能力上存在差异。为此，本文提出了一种句子表示选择机制S2Sent，集成了参数化的嵌套选择器，旨在优化跨块表示融合的语义冗余与损失。该选择器通过空间选择和嵌套频率选择来实现低信息冗余的融合，并捕捉嵌入特征之间的依赖关系。实验结果表明，S2Sent在基线方法上显著提升了性能，同时保持了参数和推理延迟的微小增加。

## 🔬 方法详解

**问题定义**：本文旨在解决基于Transformer的句子表示学习中，不同块的语义感知能力差异导致的语义冗余和信息损失问题。现有方法通常依赖于最后一个块的隐藏状态，未能充分利用其他块的潜力。

**核心思路**：S2Sent通过引入一个参数化的嵌套选择器，进行空间选择和嵌套频率选择，以优化句子表示的融合过程。这种设计旨在平衡信息冗余与语义损失，提升整体表示质量。

**技术框架**：S2Sent的整体架构包括Transformer编码器和嵌套选择器两个主要模块。编码器提取句子的初步表示，而嵌套选择器则在此基础上进行进一步的选择和融合。

**关键创新**：S2Sent的主要创新在于其空间选择机制，采用自门控机制获取自适应权重，从而实现低冗余的融合。此外，嵌套频率选择通过不同的DCT基函数替代GAP，降低了语义损失。

**关键设计**：在设计中，选择器的参数化设置和自门控机制是关键，确保了选择过程的灵活性和适应性。损失函数的设计也考虑了信息冗余与语义保留的平衡。整体网络结构保持了较低的参数量和推理延迟。

## 📊 实验亮点

实验结果表明，S2Sent在多个基准数据集上显著超越了现有基线方法，提升幅度达到XX%（具体数据待补充），同时保持了额外参数和推理延迟的微小增加，显示出其高集成性和可扩展性。

## 🎯 应用场景

该研究的潜在应用场景包括自然语言处理中的句子表示、文本分类、情感分析等任务。通过优化句子表示的质量，S2Sent能够提升下游任务的性能，具有广泛的实际价值和影响力，尤其是在需要高效语义理解的领域。

## 📄 摘要（原文）

> The combination of Transformer-based encoders with contrastive learning represents the current mainstream paradigm for sentence representation learning. This paradigm is typically based on the hidden states of the last Transformer block of the encoder. However, within Transformer-based encoders, different blocks exhibit varying degrees of semantic perception ability. From the perspective of interpretability, the semantic perception potential of knowledge neurons is modulated by stimuli, thus rational cross-block representation fusion is a direction worth optimizing. To balance the semantic redundancy and loss across block fusion, we propose a sentence representation selection mechanism S\textsuperscript{2}Sent, which integrates a parameterized nested selector downstream of the Transformer-based encoder. This selector performs spatial selection (SS) and nested frequency selection (FS) from a modular perspective. The SS innovatively employs a spatial squeeze based self-gating mechanism to obtain adaptive weights, which not only achieves fusion with low information redundancy but also captures the dependencies between embedding features. The nested FS replaces GAP with different DCT basis functions to achieve spatial squeeze with low semantic loss. Extensive experiments have demonstrated that S\textsuperscript{2}Sent achieves significant improvements over baseline methods with negligible additional parameters and inference latency, while highlighting high integrability and scalability.

