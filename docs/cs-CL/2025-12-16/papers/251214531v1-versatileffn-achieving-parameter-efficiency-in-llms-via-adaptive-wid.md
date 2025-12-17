---
layout: default
title: VersatileFFN: Achieving Parameter Efficiency in LLMs via Adaptive Wide-and-Deep Reuse
---

# VersatileFFN: Achieving Parameter Efficiency in LLMs via Adaptive Wide-and-Deep Reuse

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14531" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14531v1</a>
  <a href="https://arxiv.org/pdf/2512.14531.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14531v1" onclick="toggleFavorite(this, '2512.14531v1', 'VersatileFFN: Achieving Parameter Efficiency in LLMs via Adaptive Wide-and-Deep Reuse')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ying Nie, Kai Han, Hongguang Li, Hang Zhou, Tianyu Guo, Enhua Wu, Xinghao Chen, Yunhe Wang

**分类**: cs.CL

**发布日期**: 2025-12-16

**🔗 代码/项目**: [GITHUB](https://github.com/huawei-noah/noah-research/tree)

---

## 💡 一句话要点

**提出VersatileFFN，通过自适应宽度和深度复用提升LLM参数效率**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `参数高效` `前馈网络` `参数复用` `宽度和深度` `自适应路由` `计算复用`

## 📋 核心要点

1. 现有LLM参数高效方法主要通过压缩模型实现，难以突破原始模型的能力上限。
2. VersatileFFN通过宽度和深度两个维度上的参数复用，在固定参数预算下提升模型容量。
3. 实验表明，该方法在多种基准测试和模型规模上均表现出有效性。

## 📝 摘要（中文）

大型语言模型（LLM）的快速扩展带来了卓越的性能，但也导致了巨大的内存成本。现有的参数高效方法，如剪枝和量化，主要压缩预训练模型，而不增强架构容量，从而触及基础模型的表示上限。本文提出了VersatileFFN，一种新颖的前馈网络（FFN），它能够在固定参数预算内灵活地复用宽度和深度维度上的参数。受到认知双过程理论的启发，VersatileFFN包含两个自适应路径：一个宽度多功能路径，从单个共享FFN生成混合子专家，模拟稀疏专家路由而不增加参数；以及一个深度多功能路径，递归地应用相同的FFN来模拟更深层次的处理，以应对复杂的token。一个难度感知门控动态地平衡这两个路径，引导“简单”的token通过高效的宽度路径，并将更深层次的迭代细化分配给“困难”的token。至关重要的是，这两个路径都复用相同的参数，因此所有额外的容量都来自计算而非内存。在各种基准和模型规模上的实验证明了该方法的有效性。

## 🔬 方法详解

**问题定义**：现有的大型语言模型在追求性能的同时，也面临着巨大的内存开销。参数高效方法，如剪枝和量化，虽然可以压缩模型，但通常无法提升模型的表达能力，受限于原始模型的性能上限。因此，如何在有限的参数预算下，提升LLM的性能和容量是一个关键问题。

**核心思路**：VersatileFFN的核心思路是通过参数复用，在不增加参数数量的前提下，提升模型的宽度和深度。借鉴认知双过程理论，模型设计了宽度多功能路径和深度多功能路径，分别处理“简单”和“困难”的token。通过难度感知门控机制，动态地分配计算资源，实现参数的有效利用。

**技术框架**：VersatileFFN主要包含两个路径：宽度多功能路径和深度多功能路径。宽度多功能路径通过共享的FFN生成混合子专家，模拟稀疏专家路由。深度多功能路径则递归地应用相同的FFN，模拟更深层次的处理。难度感知门控模块根据token的难度，动态地平衡这两个路径的计算资源分配。整体架构旨在通过计算复用提升模型容量，而非增加参数数量。

**关键创新**：VersatileFFN的关键创新在于其参数复用机制，它在宽度和深度两个维度上实现了参数的灵活复用。与传统的参数高效方法不同，VersatileFFN不是简单地压缩模型，而是通过计算复用提升模型的表达能力。难度感知门控机制也是一个创新点，它能够根据token的难度动态地分配计算资源，从而实现更有效的参数利用。

**关键设计**：宽度多功能路径采用混合专家（Mixture of Experts, MoE）的思想，但避免了MoE中参数数量的增加。深度多功能路径通过递归应用FFN实现深度扩展，递归次数可以根据计算资源进行调整。难度感知门控模块的设计需要仔细考虑如何准确评估token的难度，并根据难度动态调整两个路径的权重。具体的参数设置和损失函数需要根据具体的任务和数据集进行调整。

## 📊 实验亮点

论文在多个基准测试和模型规模上验证了VersatileFFN的有效性。实验结果表明，在相同的参数预算下，VersatileFFN能够显著提升LLM的性能。具体的性能提升幅度取决于具体的任务和数据集，但总体趋势是VersatileFFN能够有效地提升模型的表达能力和泛化能力。

## 🎯 应用场景

VersatileFFN具有广泛的应用前景，可以应用于各种需要高效利用参数的大型语言模型场景，例如移动设备上的轻量级LLM部署、资源受限环境下的模型训练和推理等。该方法可以降低LLM的部署成本，并提升其在资源受限环境下的性能，加速LLM的普及和应用。

## 📄 摘要（原文）

> The rapid scaling of Large Language Models (LLMs) has achieved remarkable performance, but it also leads to prohibitive memory costs. Existing parameter-efficient approaches such as pruning and quantization mainly compress pretrained models without enhancing architectural capacity, thereby hitting the representational ceiling of the base model. In this work, we propose VersatileFFN, a novel feed-forward network (FFN) that enables flexible reuse of parameters in both width and depth dimensions within a fixed parameter budget. Inspired by the dual-process theory of cognition, VersatileFFN comprises two adaptive pathways: a width-versatile path that generates a mixture of sub-experts from a single shared FFN, mimicking sparse expert routing without increasing parameters, and a depth-versatile path that recursively applies the same FFN to emulate deeper processing for complex tokens. A difficulty-aware gating dynamically balances the two pathways, steering "easy" tokens through the efficient width-wise route and allocating deeper iterative refinement to "hard" tokens. Crucially, both pathways reuse the same parameters, so all additional capacity comes from computation rather than memory. Experiments across diverse benchmarks and model scales demonstrate the effectiveness of the method. The code will be available at https://github.com/huawei-noah/noah-research/tree/master/VersatileFFN.

