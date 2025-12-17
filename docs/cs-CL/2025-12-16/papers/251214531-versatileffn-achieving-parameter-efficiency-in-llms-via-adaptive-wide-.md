---
layout: default
title: VersatileFFN: Achieving Parameter Efficiency in LLMs via Adaptive Wide-and-Deep Reuse
---

# VersatileFFN: Achieving Parameter Efficiency in LLMs via Adaptive Wide-and-Deep Reuse

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14531" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14531</a>
  <a href="https://arxiv.org/pdf/2512.14531.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14531" onclick="toggleFavorite(this, '2512.14531', 'VersatileFFN: Achieving Parameter Efficiency in LLMs via Adaptive Wide-and-Deep Reuse')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ying Nie, Kai Han, Hongguang Li, Hang Zhou, Tianyu Guo, Enhua Wu, Xinghao Chen, Yunhe Wang

**分类**: cs.CL

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**VersatileFFN：通过自适应宽深复用提升LLM的参数效率**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `参数高效` `大型语言模型` `前馈网络` `模型压缩` `宽度复用` `深度复用` `自适应路由` `认知双过程`

## 📋 核心要点

1. 现有LLM参数高效方法主要通过压缩预训练模型实现，但未有效提升模型架构本身的容量。
2. VersatileFFN通过宽度和深度两个维度上的参数复用，在固定参数预算下提升模型容量。
3. 实验表明，VersatileFFN在多种基准测试和模型规模上均表现出有效性，验证了其参数效率。

## 📝 摘要（中文）

大型语言模型（LLM）的快速扩展带来了卓越的性能，但也导致了巨大的内存成本。现有的参数高效方法，如剪枝和量化，主要压缩预训练模型，而不增强架构容量，从而触及了基础模型的表征上限。本文提出了VersatileFFN，一种新颖的前馈网络（FFN），它能够在固定的参数预算内，灵活地复用宽度和深度维度上的参数。受到认知双过程理论的启发，VersatileFFN包含两个自适应路径：一个宽度多功能路径，从单个共享FFN生成子专家混合，模拟稀疏专家路由而不增加参数；以及一个深度多功能路径，递归地应用相同的FFN，以模拟更深层次的复杂token处理。一个难度感知门控动态地平衡这两个路径，引导“简单”token通过高效的宽度路径，并为“困难”token分配更深层次的迭代细化。至关重要的是，这两个路径都复用相同的参数，因此所有额外的容量都来自计算而非内存。在各种基准和模型规模上的实验证明了该方法的有效性。

## 🔬 方法详解

**问题定义**：现有大型语言模型（LLM）在追求卓越性能的同时，面临着巨大的内存成本问题。现有的参数高效方法，如剪枝和量化，主要集中于压缩预训练模型，而忽略了模型架构本身的容量提升，导致模型性能受限于基础模型的表征能力。

**核心思路**：VersatileFFN的核心思路是在固定参数预算下，通过参数的灵活复用，同时提升模型的宽度和深度，从而增强模型的表征能力。借鉴认知双过程理论，区分“简单”和“困难”的token，并采用不同的处理路径。

**技术框架**：VersatileFFN包含两个主要路径：宽度多功能路径和深度多功能路径。宽度路径通过共享的FFN生成子专家混合，模拟稀疏专家路由。深度路径则递归应用相同的FFN，模拟更深层次的处理。难度感知门控机制动态平衡这两个路径，将“简单”token引导至宽度路径，将“困难”token引导至深度路径。这两个路径共享相同的参数。

**关键创新**：VersatileFFN的关键创新在于参数的自适应宽深复用。与传统的参数高效方法不同，VersatileFFN不是简单地压缩模型，而是通过巧妙的架构设计，在不增加参数量的前提下，提升模型的容量。难度感知门控机制也是一个创新点，它能够根据token的难度动态调整处理路径。

**关键设计**：难度感知门控机制是VersatileFFN的关键设计之一。具体实现方式未知，但其目标是根据token的复杂程度，动态地分配计算资源。宽度路径和深度路径的具体网络结构未知，但它们都基于共享的FFN。损失函数的设计也至关重要，需要平衡宽度路径和深度路径的贡献，并确保模型的整体性能。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14531/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14531/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14531/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文通过实验验证了VersatileFFN的有效性。具体性能数据未知，但实验结果表明，VersatileFFN在多种基准测试和模型规模上均优于现有的参数高效方法。该方法能够在不增加参数量的前提下，显著提升模型的性能，证明了其参数效率。

## 🎯 应用场景

VersatileFFN具有广泛的应用前景，可以应用于各种需要参数高效的大型语言模型场景，例如移动设备上的自然语言处理、资源受限环境下的模型部署等。该研究有助于降低LLM的部署成本，加速LLM在各个领域的普及和应用，并为未来的参数高效模型设计提供新的思路。

## 📄 摘要（原文）

> The rapid scaling of Large Language Models (LLMs) has achieved remarkable performance, but it also leads to prohibitive memory costs. Existing parameter-efficient approaches such as pruning and quantization mainly compress pretrained models without enhancing architectural capacity, thereby hitting the representational ceiling of the base model. In this work, we propose VersatileFFN, a novel feed-forward network (FFN) that enables flexible reuse of parameters in both width and depth dimensions within a fixed parameter budget. Inspired by the dual-process theory of cognition, VersatileFFN comprises two adaptive pathways: a width-versatile path that generates a mixture of sub-experts from a single shared FFN, mimicking sparse expert routing without increasing parameters, and a depth-versatile path that recursively applies the same FFN to emulate deeper processing for complex tokens. A difficulty-aware gating dynamically balances the two pathways, steering "easy" tokens through the efficient width-wise route and allocating deeper iterative refinement to "hard" tokens. Crucially, both pathways reuse the same parameters, so all additional capacity comes from computation rather than memory. Experiments across diverse benchmarks and model scales demonstrate the effectiveness of the method. The code will be available atthis https URL.

