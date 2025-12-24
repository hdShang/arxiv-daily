---
layout: default
title: "MMTok: Multimodal Coverage Maximization for Efficient Inference of VLMs"
---

# MMTok: Multimodal Coverage Maximization for Efficient Inference of VLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18264" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18264v1</a>
  <a href="https://arxiv.org/pdf/2508.18264.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18264v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18264v1', 'MMTok: Multimodal Coverage Maximization for Efficient Inference of VLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sixun Dong, Juhua Hu, Mian Zhang, Ming Yin, Yanjie Fu, Qi Qian

**分类**: cs.CV

**发布日期**: 2025-08-25

**备注**: Project page: https://project.ironieser.cc/mmtok

---

## 💡 一句话要点

**提出MMTok以解决视觉语言模型的冗余推理效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `多模态融合` `推理效率` `覆盖率优化` `信息选择` `深度学习` `模型剪枝`

## 📋 核心要点

1. 现有方法在处理视觉语言模型时，往往仅依赖单一模态信息，导致冗余视觉标记影响推理效率。
2. 本文提出MMTok方法，通过最大覆盖率标准同时优化视觉和文本标记的选择，以提高推理效率。
3. 实验结果显示，MMTok在多个基准数据集上表现优异，尤其在LLaVA-NeXT-13B上实现了1.87倍的速度提升。

## 📝 摘要（中文）

视觉语言模型（VLMs）在通过语言指令理解视觉内容方面表现出色，但视觉标记的冗余性导致推理效率下降。现有的许多算法仅依赖单一模态信息进行剪枝，忽视了视觉语言任务的多模态特性。为此，本文提出了一种利用视觉和文本标记选择信息丰富的视觉标记的方法，基于覆盖率标准优化视觉标记的子集选择问题。通过在不同的基准数据集上进行广泛评估，结果表明多模态信息的结合显著优于单模态基线，且在POPE数据集上实现了1.87倍的速度提升，同时保持了98.7%的原始性能。

## 🔬 方法详解

**问题定义**：本文旨在解决视觉语言模型推理过程中视觉标记的冗余性问题。现有方法通常只利用单一模态信息进行剪枝，未能充分利用多模态特性，导致推理效率低下。

**核心思路**：论文提出通过最大覆盖率标准，结合视觉和文本标记的信息，选择出最具信息量的视觉标记，从而提高推理效率。这样的设计充分利用了多模态信息的互补性。

**技术框架**：整体方法分为三个主要模块：首先，定义子集选择问题为最大覆盖问题；其次，优化视觉标记的子集以覆盖文本标记和原始视觉标记；最后，采用VLM代理进一步提升文本标记的质量，以指导视觉剪枝。

**关键创新**：最重要的创新点在于提出了一种基于覆盖率的多模态信息选择标准，克服了现有方法仅依赖单一模态的局限性，显著提升了推理效率。

**关键设计**：在参数设置上，采用了适应性选择机制，以确保选择的视觉标记能够最大程度上覆盖文本信息。损失函数设计上，结合了覆盖率和信息量的权衡，以优化选择过程。

## 📊 实验亮点

实验结果表明，MMTok在POPE数据集上实现了1.87倍的速度提升，同时保持了98.7%的原始性能。此外，在LLaVA-1.5-7B模型中，仅使用四个视觉标记仍能保留87.7%的原始性能，显示出其在视觉标记选择上的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能监控、自动驾驶、机器人视觉等需要高效处理视觉和语言信息的场景。通过提高视觉语言模型的推理效率，MMTok可以在实时应用中显著提升系统的响应速度和准确性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Vision-Language Models (VLMs) demonstrate impressive performance in understanding visual content with language instruction by converting visual input to vision tokens. However, redundancy in vision tokens results in the degenerated inference efficiency of VLMs. While many algorithms have been proposed to reduce the number of vision tokens, most of them apply only unimodal information (i.e., vision/text) for pruning and ignore the inherent multimodal property of vision-language tasks. Moreover, it lacks a generic criterion that can be applied to different modalities. To mitigate this limitation, in this work, we propose to leverage both vision and text tokens to select informative vision tokens by the criterion of coverage. We first formulate the subset selection problem as a maximum coverage problem. Afterward, a subset of vision tokens is optimized to cover the text tokens and the original set of vision tokens, simultaneously. Finally, a VLM agent can be adopted to further improve the quality of text tokens for guiding vision pruning. The proposed method MMTok is extensively evaluated on benchmark datasets with different VLMs. The comparison illustrates that vision and text information are complementary, and combining multimodal information can surpass the unimodal baseline with a clear margin. Moreover, under the maximum coverage criterion on the POPE dataset, our method achieves a 1.87x speedup while maintaining 98.7% of the original performance on LLaVA-NeXT-13B. Furthermore, with only four vision tokens, it still preserves 87.7% of the original performance on LLaVA-1.5-7B. These results highlight the effectiveness of coverage in token selection.

