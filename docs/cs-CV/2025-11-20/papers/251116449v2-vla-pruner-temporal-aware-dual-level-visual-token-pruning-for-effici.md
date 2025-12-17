---
layout: default
title: VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference
---

# VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.16449" class="toolbar-btn" target="_blank">📄 arXiv: 2511.16449v2</a>
  <a href="https://arxiv.org/pdf/2511.16449.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.16449v2" onclick="toggleFavorite(this, '2511.16449v2', 'VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziyan Liu, Yeqiu Chen, Hongyi Cai, Tao Lin, Shuo Yang, Zheng Liu, Bo Zhao

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-20 (更新: 2025-11-21)

---

## 💡 一句话要点

**VLA-Pruner：面向高效视觉-语言-动作推理的时序感知双层视觉Token剪枝**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `视觉-语言-动作模型` `Token剪枝` `具身智能` `机器人操作` `时间连续性` `双层重要性` `高效推理`

## 📋 核心要点

1. 现有VLA模型的Token剪枝方法忽略了VLA双系统特性，导致动作生成所需关键信息丢失，性能下降。
2. VLA-Pruner利用VLA模型的双系统特性和机器人操作的时间连续性，采用双层重要性准则进行Token选择。
3. 实验表明，VLA-Pruner在多种VLA架构和机器人任务中实现了SOTA性能，验证了其有效性。

## 📝 摘要（中文）

视觉-语言-动作（VLA）模型在具身智能领域展现出巨大潜力，但处理连续视觉流的高昂计算成本严重限制了它们的实时部署。Token剪枝（保留显著的视觉token并丢弃冗余的token）已成为加速视觉-语言模型（VLM）的有效方法，为高效VLA提供了一种解决方案。然而，这些VLM特定的token剪枝方法仅基于语义显著性指标（例如，prefill attention）选择token，而忽略了VLA固有的高层语义理解和低层动作执行的双系统特性。因此，这些方法倾向于保留语义线索的token，丢弃对动作生成至关重要的信息，并显著降低VLA性能。为了弥合这一差距，我们提出了VLA-Pruner，一种通用的即插即用VLA特定token剪枝方法，它与VLA模型的双系统特性相一致，并利用了机器人操作中的时间连续性。具体来说，VLA-Pruner采用双层重要性准则进行视觉token保留：用于语义级别相关性的视觉-语言prefill attention，以及通过时间平滑估计的用于动作级别重要性的动作解码attention。基于此准则，VLA-Pruner提出了一种新颖的双层token选择策略，该策略自适应地保留了一组紧凑且信息丰富的视觉token，用于在给定的计算预算下进行语义理解和动作执行。实验表明，VLA-Pruner在多种VLA架构和不同的机器人任务中实现了最先进的性能。

## 🔬 方法详解

**问题定义**：现有VLA模型的token剪枝方法主要针对VLM设计，仅考虑语义显著性，忽略了VLA任务中动作执行的重要性。这导致剪枝后的token集合偏向于语义信息，而丢失了对动作生成至关重要的视觉信息，最终降低了VLA模型的性能。现有方法未能充分利用VLA任务的特性，特别是高层语义理解和低层动作执行的双系统特性，以及机器人操作中的时间连续性。

**核心思路**：VLA-Pruner的核心思路是设计一种VLA任务特定的token剪枝方法，该方法能够同时考虑语义理解和动作执行的重要性。通过引入双层重要性准则，分别评估token在语义层面的相关性和在动作层面的重要性，从而自适应地保留对两者都重要的token。此外，利用机器人操作的时间连续性，通过时间平滑来更准确地估计动作解码attention，提高动作级别重要性的评估精度。

**技术框架**：VLA-Pruner是一个即插即用的模块，可以集成到现有的VLA模型中。其主要流程包括：1) 使用视觉-语言prefill attention评估token的语义级别相关性；2) 使用时间平滑的动作解码attention评估token的动作级别重要性；3) 基于双层重要性准则，采用双层token选择策略，自适应地保留一组紧凑且信息丰富的视觉token。

**关键创新**：VLA-Pruner的关键创新在于提出了双层重要性准则和双层token选择策略。双层重要性准则能够同时考虑语义理解和动作执行的重要性，避免了现有方法偏向语义信息的缺陷。双层token选择策略能够根据给定的计算预算，自适应地平衡语义和动作信息，从而在保证性能的同时实现高效的token剪枝。

**关键设计**：VLA-Pruner的关键设计包括：1) 使用视觉-语言prefill attention作为语义级别相关性的度量；2) 使用时间平滑的动作解码attention作为动作级别重要性的度量，具体的时间平滑方法未知；3) 设计双层token选择策略，该策略的具体实现方式未知，但目标是根据双层重要性准则，在计算预算的约束下，选择最佳的token子集。

## 📊 实验亮点

VLA-Pruner在多个VLA架构和不同的机器人任务中实现了SOTA性能。具体性能数据未知，但论文强调VLA-Pruner能够显著提高VLA模型的效率，同时保持甚至提升其性能，克服了现有token剪枝方法在VLA任务中的局限性。

## 🎯 应用场景

VLA-Pruner可应用于各种需要实时视觉-语言-动作推理的机器人任务，例如机器人导航、物体操作、人机协作等。通过降低VLA模型的计算成本，VLA-Pruner能够提高机器人在资源受限环境中的部署能力，并促进更高效、更智能的机器人应用。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models have shown great promise for embodied AI, yet the heavy computational cost of processing continuous visual streams severely limits their real-time deployment. Token pruning (keeping salient visual tokens and dropping redundant ones) has emerged as an effective approach for accelerating Vision-Language Models (VLMs), offering a solution for efficient VLA. However, these VLM-specific token pruning methods select tokens based solely on semantic salience metrics (e.g., prefill attention), while overlooking the VLA's intrinsic dual-system nature of high-level semantic understanding and low-level action execution. Consequently, these methods bias token retention toward semantic cues, discard critical information for action generation, and significantly degrade VLA performance. To bridge this gap, we propose VLA-Pruner, a versatile plug-and-play VLA-specific token prune method that aligns with the dual-system nature of VLA models and exploits the temporal continuity in robot manipulation. Specifically, VLA-Pruner adopts a dual-level importance criterion for visual token retention: vision-language prefill attention for semantic-level relevance and action decode attention, estimated via temporal smoothing, for action-level importance. Based on this criterion, VLA-Pruner proposes a novel dual-level token selection strategy that adaptively preserves a compact, informative set of visual tokens for both semantic understanding and action execution under given compute budget. Experiments show that VLA-Pruner achieves state-of-the-art performance across multiple VLA architectures and diverse robotic tasks.

