---
layout: default
title: "SIRI: Scaling Iterative Reinforcement Learning with Interleaved Compression"
---

# SIRI: Scaling Iterative Reinforcement Learning with Interleaved Compression

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25176" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25176v1</a>
  <a href="https://arxiv.org/pdf/2509.25176.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25176v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25176v1', 'SIRI: Scaling Iterative Reinforcement Learning with Interleaved Compression')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haoming Wen, Yushi Bai, Juanzi Li, Jie Tang

**分类**: cs.LG, cs.CL

**发布日期**: 2025-09-29

**备注**: In submission

---

## 💡 一句话要点

**SIRI：通过交错压缩扩展迭代强化学习，提升大型推理模型的效率与准确性。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `强化学习` `大型语言模型` `推理效率` `模型压缩` `迭代训练` `动态规划` `token优化` `AIME24`

## 📋 核心要点

1. 大型推理模型存在重复思考模式，减少冗余token常导致性能下降，如何在效率与性能间取得平衡是核心问题。
2. SIRI通过交错压缩和扩展推理预算，动态调整rollout长度，迫使模型在有限上下文中进行精确决策，提高推理密度。
3. 实验表明，SIRI在降低token使用量的同时显著提升性能，例如在AIME24上，SIRI-low性能提升43.2%，token使用量减少46.9%。

## 📝 摘要（中文）

本文提出了一种简单而有效的强化学习方法SIRI，即通过交错压缩扩展的迭代强化学习，用于大型推理模型(LRM)，以实现更高效和准确的推理。现有研究表明LRM中存在重复的思考模式，而减少这些模式通常会牺牲性能。本文表明，通过一种在训练期间迭代地交替压缩和扩展推理预算的训练机制，可以克服这种权衡，具体方法是动态调整最大rollout长度。压缩阶段缩短rollout长度，迫使模型在有限的上下文中做出精确且有价值的决策，从而有效地减少冗余token并增加推理密度。扩展阶段则放宽长度限制，为模型在长时程设置中探索和规划提供空间。值得注意的是，我们发现经过每个压缩-扩展循环后，即使模型的输出长度减少，其性能也会提高，从而稳步地将其推向性能-效率权衡的帕累托前沿。在DeepSeek-R1-Distill-Qwen-1.5B上训练，经过三次迭代后，SIRI-low在AIME24上的性能提高了43.2%，同时减少了46.9%的token使用量，而SIRI-high实现了与其他所有方法相比最高的准确率。我们的发现揭示了在训练期间周期性地振荡LRM的输出截断长度以动态平衡推理中的探索和效率的潜力，从而收敛到两者之间的最佳“甜蜜点”。我们的模型已公开。

## 🔬 方法详解

**问题定义**：论文旨在解决大型推理模型（LRM）中存在的推理效率问题，具体表现为模型在推理过程中存在大量的重复思考模式，导致token使用量大，推理速度慢。现有方法试图通过减少token使用来提高效率，但往往会牺牲模型的推理性能，无法在效率和性能之间取得平衡。

**核心思路**：SIRI的核心思路是通过迭代地交替压缩和扩展推理预算来动态平衡探索和效率。压缩阶段迫使模型在有限的上下文中做出更精确的决策，减少冗余token；扩展阶段则允许模型在更长的horizon中进行探索和规划。通过这种周期性的调整，模型可以逐步学习到更高效的推理策略，最终达到性能和效率的“甜蜜点”。

**技术框架**：SIRI的训练过程包含多个迭代循环，每个循环包含两个阶段：压缩阶段和扩展阶段。在压缩阶段，模型的最大rollout长度被缩短，迫使模型在有限的上下文中进行推理。在扩展阶段，模型的最大rollout长度被放宽，允许模型进行更长远的规划。这两个阶段交替进行，直到模型收敛。

**关键创新**：SIRI的关键创新在于提出了一种交错压缩和扩展的训练机制，能够动态地调整模型的推理预算，从而在性能和效率之间取得更好的平衡。与现有方法相比，SIRI不需要手动设计复杂的token压缩策略，而是通过训练自动学习到最优的推理策略。

**关键设计**：SIRI的关键设计在于rollout长度的动态调整策略。具体来说，在压缩阶段，rollout长度会逐渐减小，迫使模型做出更精确的决策。在扩展阶段，rollout长度会逐渐增大，允许模型进行更长远的规划。rollout长度的具体调整策略（例如，减小/增大的幅度）可以根据具体的任务和模型进行调整。论文中并未明确给出具体的rollout长度调整函数，这部分可能需要根据实际情况进行探索。

## 📊 实验亮点

SIRI在DeepSeek-R1-Distill-Qwen-1.5B模型上进行了实验，结果表明，经过三次迭代后，SIRI-low在AIME24数据集上的性能提高了43.2%，同时token使用量减少了46.9%。SIRI-high实现了与其他所有方法相比最高的准确率。这些结果表明，SIRI能够有效地提高大型推理模型的效率和准确性。

## 🎯 应用场景

SIRI方法具有广泛的应用前景，可以应用于各种需要高效推理的大型语言模型任务中，例如问答系统、对话生成、代码生成等。通过降低token使用量，SIRI可以显著降低模型的计算成本和延迟，使其更易于部署在资源受限的环境中。此外，SIRI还可以提高模型的推理准确性，使其能够更好地解决复杂的推理问题。

## 📄 摘要（原文）

> We introduce SIRI, Scaling Iterative Reinforcement Learning with Interleaved Compression, a simple yet effective RL approach for Large Reasoning Models (LRMs) that enables more efficient and accurate reasoning. Existing studies have observed repetitive thinking patterns in LRMs, and attempts to reduce them often come at the cost of performance. In this paper, we show that this trade-off can be overcome through a training regime that iteratively alternates between compressing and expanding the reasoning budget, by dynamically adjusting the maximum rollout length during training. The compression phase cuts the rollout length, forcing the model to make precise and valuable decisions within a limited context, which effectively reduces redundant tokens and increases reasoning density. The expansion phase then relaxes the length limit, providing space for the model to explore and plan in long-horizon settings. Remarkably, we find that after each compression-expansion cycle, the model's performance improves even as its output length decreases, steadily pushing it closer to the Pareto frontier in the performance-efficiency trade-off. Training on DeepSeek-R1-Distill-Qwen-1.5B, SIRI-low improves performance on AIME24 by 43.2% while reducing token usage by 46.9% after three iterations, and SIRI-high achieves the highest accuracy compared to all other methods (Figure 1). Our findings shed light on the potential of periodically oscillating the LRM's output truncation length during training to dynamically balance exploration and efficiency in reasoning, converging towards an optimal "sweet spot" between the two. Our models are publicly available.

