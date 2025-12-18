---
layout: default
title: VisionSelector: End-to-End Learnable Visual Token Compression for Efficient Multimodal LLMs
---

# VisionSelector: End-to-End Learnable Visual Token Compression for Efficient Multimodal LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.16598" class="toolbar-btn" target="_blank">📄 arXiv: 2510.16598v1</a>
  <a href="https://arxiv.org/pdf/2510.16598.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.16598v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.16598v1', 'VisionSelector: End-to-End Learnable Visual Token Compression for Efficient Multimodal LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiaying Zhu, Yurui Zhu, Xin Lu, Wenrui Yan, Dong Li, Kunlin Liu, Xueyang Fu, Zheng-Jun Zha

**分类**: cs.CV

**发布日期**: 2025-10-18

**备注**: 22 pages, 8 figures

**🔗 代码/项目**: [GITHUB](https://github.com/JulietChoo/VisionSelector)

---

## 💡 一句话要点

**VisionSelector：端到端可学习的视觉Token压缩，提升多模态LLM效率**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `视觉Token压缩` `端到端学习` `Top-K选择` `课程学习`

## 📋 核心要点

1. 多模态大语言模型处理高分辨率图像时，视觉Token数量庞大，导致计算和内存瓶颈。
2. VisionSelector将Token压缩转化为端到端可学习的决策过程，自适应选择关键Token。
3. 实验表明，VisionSelector在各种压缩率下均表现出色，显著提升性能并加速预填充过程。

## 📝 摘要（中文）

多模态大型语言模型(MLLM)在高分辨率图像或多图像输入产生的大量视觉tokens时，面临着显著的计算和内存瓶颈。先前的token压缩技术通常受限于启发式规则，这可能导致关键信息的丢失。它们可能遭受诸如注意力沉没(attention sinks)等偏差，从而在激进的压缩率下导致性能急剧下降。为了解决这些限制，我们将token压缩重新定义为一个轻量级的即插即用框架，将其转化为端到端的可学习决策过程。具体来说，我们提出了VisionSelector，一个与MLLM骨干网络解耦的评分模块，它结合了可微分的Top-K机制和课程退火策略，以弥合训练-推理差距，从而能够以各种任意压缩率进行高效和自适应的token选择。VisionSelector非常轻量级，只有1285万个可训练参数，它展示了跨各种压缩率的泛化能力，并能自适应地识别关键tokens。这带来了在所有压缩预算下的卓越性能，通过在30%保留预算下保持MME的100%准确率，在10%保留预算下优于先前方法12.14%，以及预填充速度翻倍来证明。

## 🔬 方法详解

**问题定义**：多模态大型语言模型（MLLMs）在处理高分辨率图像或多图输入时，会产生大量的视觉tokens，这带来了显著的计算和内存负担。现有的token压缩方法通常依赖于启发式规则，这些规则可能会导致关键信息的丢失，并且容易受到注意力沉没等偏差的影响，从而在较高压缩率下导致性能显著下降。

**核心思路**：论文的核心思路是将token压缩问题重新定义为一个端到端可学习的决策过程。通过学习一个评分函数来评估每个视觉token的重要性，并选择最重要的token子集，从而在降低计算成本的同时，尽可能保留关键信息。这种方法避免了启发式规则的局限性，并允许模型自适应地学习哪些token对于下游任务最重要。

**技术框架**：VisionSelector是一个轻量级的即插即用模块，可以与现有的MLLM骨干网络集成。它主要包含一个评分模块，用于评估每个视觉token的重要性。该评分模块与MLLM骨干网络解耦，允许独立训练和优化。在训练过程中，采用可微分的Top-K机制来选择最重要的token子集。为了弥合训练和推理之间的差距，论文还引入了一种课程退火策略，逐步增加压缩率。

**关键创新**：VisionSelector的关键创新在于其端到端可学习的token压缩方法。与传统的基于启发式规则的方法不同，VisionSelector能够自适应地学习哪些token对于下游任务最重要。此外，可微分的Top-K机制和课程退火策略有效地解决了训练和推理之间的差距，使得VisionSelector能够在各种压缩率下保持良好的性能。

**关键设计**：VisionSelector的评分模块是一个轻量级的神经网络，其输入是视觉token，输出是每个token的重要性得分。Top-K机制选择得分最高的K个token。课程退火策略通过逐步降低保留的token数量，来提高模型在较高压缩率下的鲁棒性。损失函数的设计旨在最大化保留token的信息量，同时最小化压缩带来的性能损失。具体参数设置（如网络结构、学习率等）在论文中有详细描述。

## 📊 实验亮点

VisionSelector在多个基准测试中表现出色。在MME基准测试中，即使在30%的保留预算下，也能保持100%的准确率。在10%的保留预算下，VisionSelector的性能比现有方法高出12.14%。此外，VisionSelector还能将预填充速度提高一倍，显著提升了MLLM的效率。

## 🎯 应用场景

VisionSelector可应用于各种需要处理高分辨率图像或多图输入的MLLM应用场景，例如视觉问答、图像描述、视觉推理等。通过降低计算和内存需求，它可以使MLLM在资源受限的设备上运行，并提高处理速度。该研究对开发更高效、更实用的多模态人工智能系统具有重要意义。

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) encounter significant computational and memory bottlenecks from the massive number of visual tokens generated by high-resolution images or multi-image inputs. Previous token compression techniques are often constrained by heuristic rules that risk discarding critical information. They may suffer from biases, such as attention sinks, that lead to sharp performance drops under aggressive compression ratios. To address these limitations, we reformulate token compression as a lightweight plug-and-play framework that reformulates token compression into an end-to-end learnable decision process. To be specific, we propose VisionSelector, a scorer module decoupled from the MLLM backbone that incorporates a differentiable Top-K mechanism and a curriculum annealing strategy to bridge the training-inference gap, enabling efficient and adaptive token selection various arbitrary compression rates. Remarkably lightweight with only 12.85M trainable parameters, VisionSelector demonstrates generalization across various compression rates and adaptively identifying critical tokens. This leads to superior performance across all compression budgets, evidenced by preserving 100% accuracy on MME with 30% retention budget, outperforming prior methods by 12.14% at 10% retention budget, and doubling prefill speed. Our code is available at https://github.com/JulietChoo/VisionSelector .

