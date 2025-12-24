---
layout: default
title: "Thoughtbubbles: an Unsupervised Method for Parallel Thinking in Latent Space"
---

# Thoughtbubbles: an Unsupervised Method for Parallel Thinking in Latent Space

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.00219" class="toolbar-btn" target="_blank">📄 arXiv: 2510.00219v1</a>
  <a href="https://arxiv.org/pdf/2510.00219.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00219v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.00219v1', 'Thoughtbubbles: an Unsupervised Method for Parallel Thinking in Latent Space')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Houjun Liu, Shikhar Murty, Christopher D. Manning, Róbert Csordás

**分类**: cs.LG, cs.AI, cs.CL, cs.NE

**发布日期**: 2025-09-30

**备注**: 10 pages, 6 figures

---

## 💡 一句话要点

**提出Thoughtbubbles，一种在隐空间进行并行自适应计算的无监督Transformer方法。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自适应计算` `并行计算` `Transformer` `预训练` `隐空间` `残差流` `语言建模`

## 📋 核心要点

1. 现有方法依赖显式思维链，无法在预训练阶段应用，且仅限于串行自然语言，限制了推理计算的扩展。
2. Thoughtbubbles通过学习fork或删除残差流，在隐空间中实现并行自适应计算，无需显式思维链。
3. 实验表明，Thoughtbubbles在多个数据集上优于标准解码器LM和非自适应并行计算方法，尤其是在零样本任务中。

## 📝 摘要（中文）

当前扩展Transformer推理期计算的方法依赖于训练模型在生成答案之前输出显式的思维链token。虽然这些方法很强大，但它们受到限制，因为它们不能应用于预训练，并且仅限于串行生成的自然语言verbalization来扩展推理期计算。本文提出了Thoughtbubbles，一种Transformer变体，它通过学习fork或删除残差流，在隐空间中原生执行并行自适应计算。因此，需要大量计算的token可以在网络中间形成克隆残差的“bubble”，以进行额外的思考。关键的是，这种行为仅通过语言建模损失在预训练期间学习。在1.5亿到7.72亿参数规模的预训练后，Thoughtbubbles在OpenWebText和peS2o困惑度以及HellaSwag和LAMBADA等零样本评估中，优于标准解码器LM以及非自适应并行计算方法。我们方法的隐式性质使得自适应计算能够从预训练时开始学习，从而为统一推理模型的训练和测试时行为铺平了道路。

## 🔬 方法详解

**问题定义**：现有Transformer模型在推理时扩展计算能力的方法，例如思维链（Chain-of-Thought），依赖于在训练时显式地生成中间推理步骤。这种方法的痛点在于：1）无法在预训练阶段应用，限制了模型的能力；2）推理过程被限制为串行的自然语言生成，效率较低。

**核心思路**：Thoughtbubbles的核心思想是在Transformer的隐空间中进行并行自适应计算。模型学习如何根据输入token的复杂程度，动态地“fork”（复制）或“delete”（删除）残差流。对于需要更多计算的token，模型会创建一个“bubble”——即多个并行的残差流，从而增加计算资源。这种方法的关键在于，它是隐式的，不需要显式的思维链，并且可以在预训练阶段学习。

**技术框架**：Thoughtbubbles基于标准的Transformer架构，但引入了可学习的门控机制来控制残差流的fork和delete。具体来说，在Transformer的每一层，模型会根据当前的残差流计算出一个门控值，该门控值决定是否复制或删除该残差流。如果门控值较高，则复制残差流，形成一个“bubble”；如果门控值较低，则删除残差流，减少计算量。最终，所有并行的残差流会通过一个聚合层合并成一个单一的残差流，用于后续的计算。

**关键创新**：Thoughtbubbles最重要的创新点在于其隐式的并行自适应计算机制。与依赖显式思维链的方法不同，Thoughtbubbles不需要预先定义推理步骤，而是通过学习自动地分配计算资源。这种方法更加灵活，并且可以在预训练阶段学习，从而更好地利用大规模无标注数据。

**关键设计**：Thoughtbubbles的关键设计包括：1）可学习的门控机制，用于控制残差流的fork和delete；2）损失函数，除了标准的语言建模损失外，还可以加入正则化项，以鼓励模型学习稀疏的残差流结构；3）残差流的聚合方式，例如可以使用加权平均或注意力机制来合并并行的残差流。

## 📊 实验亮点

Thoughtbubbles在OpenWebText和peS2o数据集上实现了更低的困惑度，表明其语言建模能力有所提升。在HellaSwag和LAMBADA等零样本任务中，Thoughtbubbles也优于标准解码器LM和非自适应并行计算方法，验证了其在复杂推理任务中的有效性。这些结果表明，Thoughtbubbles能够有效地学习自适应计算，并在各种任务中取得显著的性能提升。

## 🎯 应用场景

Thoughtbubbles具有广泛的应用前景，可以应用于各种需要复杂推理的任务，例如问答、文本摘要、机器翻译等。其隐式并行计算的特性，使其能够更好地利用硬件资源，提高推理效率。此外，由于Thoughtbubbles可以在预训练阶段学习，因此可以更好地利用大规模无标注数据，提高模型的泛化能力。未来，Thoughtbubbles有望成为构建更强大、更高效的推理模型的重要技术。

## 📄 摘要（原文）

> Current approaches for scaling inference-time compute in transformers rely on training them to emit explicit chain-of-thought tokens before producing an answer. While these methods are powerful, they are limited because they cannot be applied during pretraining and are limited to only serially-generated, natural-language verbalization to scale inference-time compute. In this work, we propose Thoughtbubbles, a transformer variant that natively performs parallel adaptive computation in latent space by learning to fork or delete residual streams. Thus, tokens that require a large amount of computation can form a "bubble" of cloned residuals in the middle of the network for additional thinking. Crucially, this behavior is learned during pretraining with only language modeling loss. Thoughtbubbles outperforms both standard decoder LMs as well as non-adaptive parallel computation approaches on OpenWebText and peS2o perplexity and in zero-shot evaluations such as HellaSwag and LAMBADA after pretraining across 150M to 772M parameter scales. The implicit nature of our method enables adaptive computation to be learned starting at pretraining time, paving the way to unify train and test-time behavior for reasoning models.

