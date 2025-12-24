---
layout: default
title: "DualSparse-MoE: Coordinating Tensor/Neuron-Level Sparsity with Expert Partition and Reconstruction"
---

# DualSparse-MoE: Coordinating Tensor/Neuron-Level Sparsity with Expert Partition and Reconstruction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18376" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18376v1</a>
  <a href="https://arxiv.org/pdf/2508.18376.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18376v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18376v1', 'DualSparse-MoE: Coordinating Tensor/Neuron-Level Sparsity with Expert Partition and Reconstruction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weilin Cai, Le Qin, Shwai He, Junwei Cui, Ang Li, Jiayi Huang

**分类**: cs.LG, cs.DC

**发布日期**: 2025-08-25

---

## 💡 一句话要点

**提出DualSparse-MoE以解决MoE模型的计算效率与准确性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `混合专家` `稀疏性` `模型优化` `计算效率` `深度学习`

## 📋 核心要点

1. 现有的MoE模型在计算效率和激活模式的不可预测性方面存在显著挑战，影响了其在实际应用中的表现。
2. 本文提出DualSparse-MoE，通过后训练专家分区实现张量和神经元层面的双重稀疏性，从而提高模型的效率和准确性。
3. 实验结果显示，采用约25%的计算丢弃率，平均准确度仅下降0.08%-0.28%，同时实现了显著的计算加速。

## 📝 摘要（中文）

Mixture of Experts (MoE)已成为构建大型语言模型的主流架构，通过减少每个token的计算量来实现模型扩展。尽管这种稀疏性提高了效率，但MoE仍面临巨大的计算规模和不可预测的激活模式等挑战。本文提出了DualSparse-MoE，识别出预训练MoE模块在张量和神经元层面的双重稀疏性，作为提高准确性和效率的关键因素。与以往通过更细粒度的专家设计增加张量级稀疏性不同，本文引入了后训练专家分区，以在不重新训练的情况下诱导稀疏性，从而在后续的微调和推理中增强效率和准确性。实验结果表明，采用该方法的约25%计算丢弃率仅导致0.08%-0.28%的平均准确度下降，同时几乎所有计算丢弃的程度都能一致地带来相应的计算加速。

## 🔬 方法详解

**问题定义**：本文旨在解决MoE模型在计算效率和激活模式不可预测性方面的挑战。现有方法在提高张量级稀疏性时，往往需要重新训练，导致效率低下。

**核心思路**：本文提出后训练专家分区的方法，能够在不重新训练的情况下诱导张量和神经元层面的稀疏性，从而保持模型的数学一致性，并在微调和推理阶段提升效率与准确性。

**技术框架**：DualSparse-MoE的整体架构包括动态张量级计算丢弃和静态神经元级重构两个主要模块。动态丢弃根据输入的特征动态选择激活的专家，而静态重构则在推理阶段保持模型的稳定性。

**关键创新**：最重要的技术创新在于引入了后训练专家分区的概念，允许在不重新训练的情况下实现双重稀疏性，这与以往需要重新训练的稀疏化方法本质上有所不同。

**关键设计**：在设计中，设置了约25%的计算丢弃率，并通过负载不平衡感知来优化专家并行性，从而在保持较低准确度下降的同时实现了1.41倍的加速。具体参数和损失函数的设计细节在实验部分进行了详细讨论。

## 📊 实验亮点

实验结果表明，采用约25%的计算丢弃率，平均准确度仅下降0.08%-0.28%。此外，结合负载不平衡感知的专家并行性优化，实现了1.41倍的MoE模块加速，显示出显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括大型语言模型的高效推理和部署，尤其是在资源受限的环境中。通过提高MoE模型的计算效率，能够在保持较高准确度的同时，降低计算成本，推动智能应用的普及与发展。

## 📄 摘要（原文）

> Mixture of Experts (MoE) has become a mainstream architecture for building Large Language Models (LLMs) by reducing per-token computation while enabling model scaling. It can be viewed as partitioning a large Feed-Forward Network (FFN) at the tensor level into fine-grained sub-FFNs, or experts, and activating only a sparse subset for each input. While this sparsity improves efficiency, MoE still faces substantial challenges due to their massive computational scale and unpredictable activation patterns.
>   To enable efficient MoE deployment, we identify dual sparsity at the tensor and neuron levels in pre-trained MoE modules as a key factor for both accuracy and efficiency. Unlike prior work that increases tensor-level sparsity through finer-grained expert design during pre-training, we introduce post-training expert partitioning to induce such sparsity without retraining. This preserves the mathematical consistency of model transformations and enhances both efficiency and accuracy in subsequent fine-tuning and inference. Building upon this, we propose DualSparse-MoE, an inference system that integrates dynamic tensor-level computation dropping with static neuron-level reconstruction to deliver significant efficiency gains with minimal accuracy loss.
>   Experimental results show that enforcing an approximate 25% drop rate with our approach reduces average accuracy by only 0.08%-0.28% across three prevailing MoE models, while nearly all degrees of computation dropping consistently yield proportional computational speedups. Furthermore, incorporating load-imbalance awareness into expert parallelism achieves a 1.41x MoE module speedup with just 0.5% average accuracy degradation.

