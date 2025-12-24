---
layout: default
title: Making Large Language Models Efficient Dense Retrievers
---

# Making Large Language Models Efficient Dense Retrievers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20612" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20612v1</a>
  <a href="https://arxiv.org/pdf/2512.20612.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20612v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20612v1', 'Making Large Language Models Efficient Dense Retrievers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yibin Lei, Shwai He, Ang Li, Andrew Yates

**分类**: cs.IR, cs.CL

**发布日期**: 2025-12-23

---

## 💡 一句话要点

**提出EffiR框架，通过MLP压缩提升LLM密集检索器的效率，保持性能。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `密集检索` `大型语言模型` `模型压缩` `层冗余` `MLP压缩`

## 📋 核心要点

1. 现有基于LLM的密集检索器参数量巨大，计算效率低，限制了其应用。
2. EffiR框架通过分析LLM层冗余，重点压缩MLP层，保留关键的注意力层。
3. 实验表明，EffiR在保持性能的同时，显著降低了模型大小和推理成本。

## 📝 摘要（中文）

最近的研究表明，直接微调大型语言模型（LLM）用于密集检索可以获得强大的性能，但其庞大的参数量导致计算效率低下。虽然之前的研究揭示了LLM在生成任务中存在显著的层冗余，但当这些模型被用于检索任务时，是否存在类似的冗余仍然不清楚，因为检索任务需要将整个序列编码成固定的表示，而不是迭代地生成token。为此，我们对基于LLM的密集检索器中的层冗余进行了全面的分析。我们发现，与生成设置相比，MLP层更易于修剪，而注意力层对于语义聚合仍然至关重要。基于这一洞察，我们提出了EffiR，一个用于开发高效检索器的框架，该框架通过粗到精的策略（粗粒度的深度缩减，然后是细粒度的宽度缩减）执行大规模的MLP压缩，并结合特定于检索的微调。在不同的BEIR数据集和LLM骨干网络上，EffiR在保持全尺寸模型性能的同时，显著降低了模型大小和推理成本。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）作为密集检索器时计算效率低下的问题。现有方法直接微调整个LLM，参数量巨大，推理成本高昂。虽然LLM在生成任务中存在层冗余已被发现，但检索任务的层冗余情况尚不明确。

**核心思路**：论文的核心思路是发现并利用LLM在检索任务中的层冗余，特别是MLP层的冗余，通过压缩MLP层来降低模型大小和推理成本，同时保留注意力层以维持语义聚合能力。

**技术框架**：EffiR框架包含以下主要阶段：1) 层冗余分析：分析LLM中不同层的可修剪性，发现MLP层更易于修剪。2) 粗粒度深度缩减：移除部分MLP层，降低模型深度。3) 细粒度宽度缩减：对剩余的MLP层进行权重剪枝，进一步降低模型宽度。4) 检索特定微调：对压缩后的模型进行微调，以恢复性能。

**关键创新**：最重要的技术创新点在于发现了LLM在检索任务中MLP层和注意力层不同的重要性，并据此设计了针对性的压缩策略。与现有方法不同，EffiR不是均匀地压缩所有层，而是重点压缩冗余的MLP层，保留关键的注意力层。

**关键设计**：EffiR采用了粗到精的压缩策略，首先进行深度缩减，然后进行宽度缩减。深度缩减通过移除整个MLP层来实现，宽度缩减通过权重剪枝来实现。此外，论文还使用了检索特定的微调方法，例如对比学习，以优化压缩后的模型。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20612v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20612v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20612v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，EffiR在多个BEIR数据集上，使用不同的LLM骨干网络，都能在保持全尺寸模型性能的同时，显著降低模型大小和推理成本。具体的性能数据和提升幅度在论文中进行了详细的展示。

## 🎯 应用场景

该研究成果可应用于各种信息检索场景，例如搜索引擎、问答系统、推荐系统等。通过降低LLM密集检索器的计算成本，可以使其更容易部署在资源受限的环境中，并提高检索效率，从而提升用户体验。

## 📄 摘要（原文）

> Recent work has shown that directly fine-tuning large language models (LLMs) for dense retrieval yields strong performance, but their substantial parameter counts make them computationally inefficient. While prior studies have revealed significant layer redundancy in LLMs for generative tasks, it remains unclear whether similar redundancy exists when these models are adapted for retrieval tasks, which require encoding entire sequences into fixed representations rather than generating tokens iteratively. To this end, we conduct a comprehensive analysis of layer redundancy in LLM-based dense retrievers. We find that, in contrast to generative settings, MLP layers are substantially more prunable, while attention layers remain critical for semantic aggregation. Building on this insight, we propose EffiR, a framework for developing efficient retrievers that performs large-scale MLP compression through a coarse-to-fine strategy (coarse-grained depth reduction followed by fine-grained width reduction), combined with retrieval-specific fine-tuning. Across diverse BEIR datasets and LLM backbones, EffiR achieves substantial reductions in model size and inference cost while preserving the performance of full-size models.

