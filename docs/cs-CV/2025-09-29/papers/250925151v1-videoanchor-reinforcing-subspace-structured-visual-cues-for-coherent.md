---
layout: default
title: "VideoAnchor: Reinforcing Subspace-Structured Visual Cues for Coherent Visual-Spatial Reasoning"
---

# VideoAnchor: Reinforcing Subspace-Structured Visual Cues for Coherent Visual-Spatial Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25151" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25151v1</a>
  <a href="https://arxiv.org/pdf/2509.25151.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25151v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25151v1', 'VideoAnchor: Reinforcing Subspace-Structured Visual Cues for Coherent Visual-Spatial Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhaozhi Wang, Tong Zhang, Mingyue Guo, Yaowei Wang, Qixiang Ye

**分类**: cs.CV

**发布日期**: 2025-09-29

**备注**: 16 pages, 6 figures

**🔗 代码/项目**: [GITHUB](https://github.com/feufhd/VideoAnchor)

---

## 💡 一句话要点

**VideoAnchor：通过强化子空间结构视觉线索实现连贯的视觉-空间推理**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `视觉空间推理` `子空间聚类` `注意力机制` `视频理解`

## 📋 核心要点

1. 现有多模态大语言模型在视觉空间推理上存在不足，主要原因是视觉token容易被语言token掩盖，导致跨帧视觉线索识别不一致。
2. 论文提出VideoAnchor模块，利用稀疏子空间聚类的自表达属性，通过子空间亲和性强化跨帧视觉线索，无需重新训练即可实现。
3. 实验结果表明，VideoAnchor在VSI-Bench和Video-MME等空间相关任务上，使用不同骨干模型均取得了显著的性能提升。

## 📝 摘要（中文）

多模态大型语言模型(MLLMs)在视觉-语言对齐方面取得了显著进展，但在视觉-空间推理方面仍然存在局限性。我们首先指出，这种局限性源于注意力机制：视觉token被语言token所掩盖，导致模型无法跨帧一致地识别相同的视觉线索。为了解决这个挑战，我们提出了稀疏子空间聚类中的自表达属性与Transformer中的注意力机制之间的新颖联系。基于这一洞察，我们提出VideoAnchor，这是一个即插即用模块，它利用子空间亲和性来强化跨帧的视觉线索，而无需重新训练，从而有效地将注意力锚定到共享的视觉结构上。在多个基准测试和骨干模型上的大量实验表明，性能得到了持续提升，例如，在使用InternVL2-8B和Qwen2.5VL-72B时，在VSI-Bench和Video-MME（空间相关任务）上分别提高了3.2%和4.6%。定性分析表明，更连贯的子空间划分和更强的视觉基础。我们的代码将在https://github.com/feufhd/VideoAnchor上公开。

## 🔬 方法详解

**问题定义**：多模态大语言模型在处理视频时，由于视觉token容易被语言token主导，导致模型难以在不同帧之间保持对同一视觉线索的稳定关注，从而影响了视觉空间推理能力。现有方法缺乏有效机制来强化和保持视觉信息的连贯性。

**核心思路**：论文的核心思路是将视频帧中的视觉token视为高维空间中的数据点，并利用稀疏子空间聚类的思想，假设这些数据点位于若干个低维子空间中。通过计算token之间的子空间亲和性，可以识别出属于同一视觉结构的token，并以此来强化这些token的注意力权重。

**技术框架**：VideoAnchor是一个即插即用的模块，可以添加到现有的多模态大语言模型中。其主要流程包括：1) 从视频帧中提取视觉特征；2) 计算视觉token之间的子空间亲和性矩阵；3) 利用亲和性矩阵调整注意力权重，从而强化属于同一子空间的token；4) 将调整后的视觉特征输入到后续的语言模型中进行处理。

**关键创新**：该论文的关键创新在于将稀疏子空间聚类的自表达属性与Transformer的注意力机制联系起来，并提出了一种利用子空间亲和性来强化视觉线索的方法。与现有方法相比，VideoAnchor无需重新训练模型，即可有效地提升视觉空间推理能力。

**关键设计**：子空间亲和性矩阵的计算是关键。论文采用了一种基于稀疏表示的方法，通过求解一个稀疏编码问题来估计token之间的亲和性。具体来说，对于每个token，找到其他token的一个稀疏线性组合来表示它，组合系数即为亲和性。此外，论文还设计了一种注意力权重调整机制，根据亲和性矩阵来调整注意力权重，从而强化属于同一子空间的token。

## 📊 实验亮点

实验结果表明，VideoAnchor在VSI-Bench和Video-MME等空间相关任务上取得了显著的性能提升。例如，在使用InternVL2-8B模型时，VSI-Bench的性能提升了3.2%，Video-MME的性能提升了4.6%。此外，定性分析表明，VideoAnchor能够产生更连贯的子空间划分和更强的视觉基础，验证了该方法的有效性。

## 🎯 应用场景

VideoAnchor具有广泛的应用前景，可用于提升视频理解、视频问答、视频目标跟踪等任务的性能。该方法能够增强模型对视频中空间信息的理解，提高模型在复杂场景下的推理能力。未来，该技术有望应用于智能监控、自动驾驶、机器人导航等领域。

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) have achieved impressive progress in vision-language alignment, yet they remain limited in visual-spatial reasoning. We first identify that this limitation arises from the attention mechanism: visual tokens are overshadowed by language tokens, preventing the model from consistently recognizing the same visual cues across frames. To address this challenge, we draw a novel connection between the self-expressiveness property in sparse subspace clustering and the attention mechanism in Transformers. Building on this insight, we propose VideoAnchor, a plug-and-play module that leverages subspace affinities to reinforce visual cues across frames without retraining, effectively anchoring attention to shared visual structures. Extensive experiments across benchmarks and backbone models show consistent performance gains -- $e.g.$, 3.2% and 4.6% improvements on VSI-Bench and Video-MME (spatial-related tasks) with InternVL2-8B and Qwen2.5VL-72B -- while qualitative analyses demonstrate more coherent subspace partitions and stronger visual grounding. Our codes will be made public available at https://github.com/feufhd/VideoAnchor.

