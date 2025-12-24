---
layout: default
title: "MoKA: Mixture of Kronecker Adapters"
---

# MoKA: Mixture of Kronecker Adapters

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03527" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03527v1</a>
  <a href="https://arxiv.org/pdf/2508.03527.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03527v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03527v1', 'MoKA: Mixture of Kronecker Adapters')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mohammadreza Sadeghi, Mahsa Ghazvini Nejad, MirHamed Jafarzadeh Asl, Yu Gu, Yuanhao Yu, Masoud Asgharian, Vahid Partovi Nia

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-08-05

---

## 💡 一句话要点

**提出MoKA以解决低秩适配器表达能力不足的问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `参数高效微调` `克罗内克适配器` `门控机制` `低秩适配器` `自然语言处理` `模型压缩` `深度学习`

## 📋 核心要点

1. 现有低秩适配器在表达能力上受到秩约束的限制，无法有效应对复杂任务。
2. 本文提出的MoKA通过混合克罗内克积建模权重更新，结合门控机制提升适应性。
3. 实验表明，MoKA在多个任务中超越PEFT基线，参数可训练性减少27倍，性能显著提升。

## 📝 摘要（中文）

参数高效微调（PEFT）对于降低大型语言模型（LLMs）的计算开销至关重要。低秩适配器虽然能有效控制参数规模，但由于秩约束，其表达能力有限，影响复杂任务的性能。本文提出了混合克罗内克适配器（MoKA），通过将权重更新建模为克罗内克积的混合，克服了这一限制。MoKA采用门控机制评估每个克罗内克因子的相对重要性，增强了适应性。同时，MoKA实现了秩灵活性，在参数效率与准确性之间提供了更好的平衡。通过标准矩阵运算重构克罗内克计算，确保了硬件效率，便于在GPU优化硬件上部署。实验结果表明，MoKA在指令调优和常识推理任务中超越了PEFT基线，并将可训练参数减少了多达27倍，达到了性能与参数效率的最佳平衡。

## 🔬 方法详解

**问题定义**：本文旨在解决低秩适配器在复杂任务中表达能力不足的问题。现有方法由于秩约束，无法充分利用模型的潜力，导致性能下降。

**核心思路**：MoKA通过将权重更新建模为克罗内克积的混合，结合门控机制来评估各个克罗内克因子的相对重要性，从而增强适应性和表达能力。

**技术框架**：MoKA的整体架构包括权重更新的混合建模、门控机制和标准矩阵运算的重构。主要模块包括克罗内克适配器、门控网络和优化算法。

**关键创新**：MoKA的核心创新在于引入了混合克罗内克积的概念，打破了传统低秩适配器的限制，使得模型在保持参数效率的同时，能够更好地适应复杂任务。

**关键设计**：在设计上，MoKA采用了灵活的秩设置和门控机制，确保了每个克罗内克因子的有效性。此外，通过标准矩阵运算的重构，提升了计算效率，便于在GPU上高效运行。

## 📊 实验亮点

在实验中，MoKA在指令调优和常识推理任务上超越了现有的PEFT基线，表现出更高的性能和效率。具体而言，MoKA将可训练参数减少了多达27倍，同时在性能上达到了最先进的水平，展现了其在参数效率与准确性之间的优越平衡。

## 🎯 应用场景

MoKA的研究成果在自然语言处理、机器翻译和对话系统等领域具有广泛的应用潜力。其高效的参数利用和出色的性能表现，能够为大型语言模型的实际部署提供更为灵活和高效的解决方案，推动智能系统的进一步发展。

## 📄 摘要（原文）

> Parameter-efficient fine-tuning (PEFT) is essential for reducing the computational overhead of large language models (LLMs). Low-rank family adapters are commonly used to control the parameter size efficiently while maintaining the generative power of LLMs. However, their limited expressiveness due to the rank constraint often restricts their performance on complex tasks. We propose Mixture of Kronecker Adapters (MoKA), a new generation of Kronecker adapters that addresses this limitation by modeling weight updates as a mixture of Kronecker products. Our proposed adapter leverages a gating mechanism that measures the importance of each Kronecker factor, enabling more expressive adaptation. Moreover, MoKA enables a rank flexibility that provides a better trade-off between parameter efficiency and accuracy. To ensure hardware efficiency, we reformulate Kronecker computations using standard matrix operations, allowing seamless deployment on GPU-optimized hardware. We conduct extensive experiments on instruction-tuning and commonsense reasoning tasks using low-bit quantized versions of LLaMA2-7B and LLaMA3-8B models. MoKA not only outperforms PEFT baselines, but also reduces the number of trainable parameters up to 27x, achieving state-of-the-art trade-offs between performance and parameter efficiency.

