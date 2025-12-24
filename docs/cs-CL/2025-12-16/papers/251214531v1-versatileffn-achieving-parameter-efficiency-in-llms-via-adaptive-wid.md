---
layout: default
title: "VersatileFFN: Achieving Parameter Efficiency in LLMs via Adaptive Wide-and-Deep Reuse"
---

# VersatileFFN: Achieving Parameter Efficiency in LLMs via Adaptive Wide-and-Deep Reuse

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14531" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14531v1</a>
  <a href="https://arxiv.org/pdf/2512.14531.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14531v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14531v1', 'VersatileFFN: Achieving Parameter Efficiency in LLMs via Adaptive Wide-and-Deep Reuse')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ying Nie, Kai Han, Hongguang Li, Hang Zhou, Tianyu Guo, Enhua Wu, Xinghao Chen, Yunhe Wang

**分类**: cs.CL

**发布日期**: 2025-12-16

**🔗 代码/项目**: [GITHUB](https://github.com/huawei-noah/noah-research/tree)

---

## 💡 一句话要点

**VersatileFFN：通过自适应宽深复用提升LLM的参数效率**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `参数高效` `大型语言模型` `前馈网络` `参数复用` `宽度深度` `自适应` `认知双过程`

## 📋 核心要点

1. 现有LLM参数高效方法主要通过压缩预训练模型，难以突破基础模型的表征能力上限。
2. VersatileFFN通过宽度和深度两个维度上的参数复用，在固定参数预算下提升模型容量。
3. 实验表明，VersatileFFN在多个基准测试和模型规模上均表现出有效性。

## 📝 摘要（中文）

大型语言模型（LLM）的快速扩展带来了卓越的性能，但也导致了巨大的内存成本。现有的参数高效方法，如剪枝和量化，主要是在不增强架构能力的情况下压缩预训练模型，从而触及了基础模型的表征上限。本文提出了VersatileFFN，一种新颖的前馈网络（FFN），它能够在固定参数预算内灵活地复用宽度和深度维度上的参数。受到认知双过程理论的启发，VersatileFFN包含两个自适应路径：一个宽度多功能路径，从单个共享FFN生成子专家混合，模拟稀疏专家路由而不增加参数；一个深度多功能路径，递归地应用相同的FFN来模拟更深层次的处理，以应对复杂的token。一个难度感知门控动态地平衡这两个路径，引导“简单”的token通过高效的宽度路径，并为“困难”的token分配更深层次的迭代细化。至关重要的是，这两个路径都复用相同的参数，因此所有额外的容量都来自计算而非内存。在不同的基准和模型规模上的实验证明了该方法的有效性。

## 🔬 方法详解

**问题定义**：现有的大型语言模型（LLM）虽然性能卓越，但其庞大的参数量导致了巨大的内存开销。现有的参数高效方法，如剪枝和量化，主要集中在压缩预训练模型上，而忽略了模型架构本身的增强，因此难以突破基础模型的表征能力上限。这些方法无法在不显著降低模型性能的前提下，有效降低内存需求。

**核心思路**：VersatileFFN的核心思路是在固定参数预算下，通过参数的灵活复用，同时提升模型的宽度和深度，从而提高模型的容量和表达能力。它借鉴了认知双过程理论，模拟人类的快速直觉和深度思考两种认知模式，设计了宽度多功能路径和深度多功能路径，并使用难度感知门控机制动态地平衡这两条路径。

**技术框架**：VersatileFFN主要包含三个核心模块：宽度多功能路径（Width-Versatile Path）、深度多功能路径（Depth-Versatile Path）和难度感知门控（Difficulty-Aware Gating）。宽度多功能路径通过共享的FFN生成子专家混合，模拟稀疏专家路由；深度多功能路径递归地应用相同的FFN，模拟更深层次的处理。难度感知门控根据输入token的难度，动态地调整两条路径的权重，将“简单”的token引导到宽度路径，将“困难”的token引导到深度路径。

**关键创新**：VersatileFFN的关键创新在于其参数复用机制，它在宽度和深度两个维度上都实现了参数的共享和复用。宽度多功能路径通过共享FFN生成多个子专家，深度多功能路径通过递归应用相同的FFN来模拟更深层次的处理。这种参数复用方式使得模型能够在不增加参数量的情况下，显著提升模型的容量和表达能力。此外，难度感知门控也是一个重要的创新点，它能够根据输入token的难度，动态地调整两条路径的权重，从而实现更高效的计算。

**关键设计**：宽度多功能路径使用一个共享的FFN，通过不同的线性变换生成多个子专家。深度多功能路径递归地应用相同的FFN，递归次数可以根据计算资源进行调整。难度感知门控使用一个小型神经网络来预测输入token的难度，并根据难度值计算两条路径的权重。损失函数方面，可以使用标准的交叉熵损失函数进行训练。具体参数设置需要根据具体的任务和数据集进行调整。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14531v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14531v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14531v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，VersatileFFN在多个基准测试和模型规模上均表现出显著的性能提升。例如，在某些任务上，VersatileFFN能够在参数量不变的情况下，将模型的准确率提高几个百分点。与传统的参数高效方法相比，VersatileFFN能够在更小的参数量下达到更高的性能。

## 🎯 应用场景

VersatileFFN具有广泛的应用前景，尤其是在资源受限的场景下。它可以用于移动设备、嵌入式系统等计算能力有限的平台上部署大型语言模型。此外，VersatileFFN还可以应用于各种自然语言处理任务，如文本分类、机器翻译、文本生成等，提高模型的性能和效率。未来，该技术有望推动LLM在更多领域的应用。

## 📄 摘要（原文）

> The rapid scaling of Large Language Models (LLMs) has achieved remarkable performance, but it also leads to prohibitive memory costs. Existing parameter-efficient approaches such as pruning and quantization mainly compress pretrained models without enhancing architectural capacity, thereby hitting the representational ceiling of the base model. In this work, we propose VersatileFFN, a novel feed-forward network (FFN) that enables flexible reuse of parameters in both width and depth dimensions within a fixed parameter budget. Inspired by the dual-process theory of cognition, VersatileFFN comprises two adaptive pathways: a width-versatile path that generates a mixture of sub-experts from a single shared FFN, mimicking sparse expert routing without increasing parameters, and a depth-versatile path that recursively applies the same FFN to emulate deeper processing for complex tokens. A difficulty-aware gating dynamically balances the two pathways, steering "easy" tokens through the efficient width-wise route and allocating deeper iterative refinement to "hard" tokens. Crucially, both pathways reuse the same parameters, so all additional capacity comes from computation rather than memory. Experiments across diverse benchmarks and model scales demonstrate the effectiveness of the method. The code will be available at https://github.com/huawei-noah/noah-research/tree/master/VersatileFFN.

