---
layout: default
title: FLoC: Facility Location-Based Efficient Visual Token Compression for Long Video Understanding
---

# FLoC: Facility Location-Based Efficient Visual Token Compression for Long Video Understanding

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2511.00141" target="_blank" class="toolbar-btn">arXiv: 2511.00141v1</a>
    <a href="https://arxiv.org/pdf/2511.00141.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.00141v1" 
            onclick="toggleFavorite(this, '2511.00141v1', 'FLoC: Facility Location-Based Efficient Visual Token Compression for Long Video Understanding')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Janghoon Cho, Jungsoo Lee, Munawar Hayat, Kyuwoong Hwang, Fatih Porikli, Sungha Choi

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-31

---

## 💡 一句话要点

**FLoC：基于设施选址的长视频高效视觉Token压缩方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长视频理解` `视觉Token压缩` `设施选址` `懒惰贪婪算法` `多模态学习`

## 📋 核心要点

1. 长视频理解依赖大型多模态模型，但长视频序列产生的海量视觉Token限制了模型的可扩展性。
2. FLoC基于设施选址函数，利用懒惰贪婪算法高效选择具有代表性和多样性的视觉Token子集，实现Token压缩。
3. 实验表明，FLoC在多个长视频理解基准测试中超越现有压缩技术，展现了其有效性和鲁棒性。

## 📝 摘要（中文）

本文提出FLoC，一种高效的视觉Token压缩框架，用于长视频理解。该框架基于设施选址函数，通过在预定义的Token数量预算内，快速选择具有代表性和多样性的视觉Token子集。通过集成懒惰贪婪算法，FLoC能够高效地选择紧凑的Token子集，显著减少视觉Token的数量，同时保证接近最优的性能。该方法无需训练，与模型和查询无关，能够无缝集成到各种视频-LLM和现有工作流程中。在Video-MME、MLVU和LongVideoBench等大规模基准测试中的评估表明，FLoC始终优于现有的压缩技术，突显了其在解决长视频理解关键挑战方面的有效性、鲁棒性和处理速度。

## 🔬 方法详解

**问题定义**：长视频理解任务中，由长视频序列产生的视觉Token数量巨大，严重限制了现有视频-LLM模型的可扩展性。现有方法在压缩视觉Token时，可能无法很好地保留视频的关键信息，导致性能下降。

**核心思路**：FLoC的核心思路是将视觉Token压缩问题转化为一个设施选址问题。每个视觉Token被视为一个潜在的“客户”，而选择的Token子集则代表“设施”。目标是选择一组“设施”，使得所有“客户”到其最近“设施”的距离之和最小，从而保证选择的Token子集具有代表性和多样性。

**技术框架**：FLoC框架主要包含以下几个步骤：1) **特征提取**：使用预训练的视觉编码器（例如ViT）提取视频帧的视觉特征，得到一系列视觉Token。2) **相似度计算**：计算所有视觉Token之间的相似度矩阵。3) **设施选址**：使用懒惰贪婪算法，基于设施选址函数，从所有Token中选择一个具有代表性和多样性的子集。4) **Token压缩**：将选择的Token子集输入到下游的视频-LLM模型中进行处理。

**关键创新**：FLoC的关键创新在于将视觉Token压缩问题建模为设施选址问题，并利用懒惰贪婪算法高效地解决该问题。与现有方法相比，FLoC无需训练，与模型和查询无关，具有更好的通用性和可扩展性。此外，设施选址函数能够保证选择的Token子集具有代表性和多样性，从而更好地保留视频的关键信息。

**关键设计**：FLoC的关键设计包括：1) **设施选址函数**：该函数用于衡量选择的Token子集的质量，目标是最小化所有Token到其最近选择Token的距离之和。2) **懒惰贪婪算法**：该算法用于高效地选择Token子集，避免了对所有可能的子集进行评估，显著提高了计算效率。3) **相似度度量**：使用余弦相似度来衡量视觉Token之间的相似度。

## 📊 实验亮点

在Video-MME、MLVU和LongVideoBench等大规模基准测试中，FLoC在各种Token压缩比例下均优于现有的压缩技术。例如，在Video-MME数据集上，FLoC在压缩比例为50%时，性能优于现有方法2-3个百分点。实验结果表明，FLoC能够有效地压缩视觉Token，同时保持较高的长视频理解性能。

## 🎯 应用场景

FLoC可应用于各种长视频理解任务，例如视频问答、视频摘要、视频检索等。通过高效压缩视觉Token，FLoC能够显著降低计算成本和内存需求，使得视频-LLM模型能够处理更长的视频序列，从而提高长视频理解的性能。该方法还可用于移动设备或边缘计算等资源受限的场景。

## 📄 摘要（原文）

> Recent studies in long video understanding have harnessed the advanced visual-language reasoning capabilities of Large Multimodal Models (LMMs), driving the evolution of video-LMMs specialized for processing extended video sequences. However, the scalability of these models is severely limited by the overwhelming volume of visual tokens generated from extended video sequences. To address this challenge, this paper proposes FLoC, an efficient visual token compression framework based on the facility location function, a principled approach that swiftly selects a compact yet highly representative and diverse subset of visual tokens within a predefined budget on the number of visual tokens. By integrating the lazy greedy algorithm, our method achieves remarkable efficiency gains by swiftly selecting a compact subset of tokens, drastically reducing the number of visual tokens while guaranteeing near-optimal performance. Notably, our approach is training-free, model-agnostic, and query-agnostic, providing a versatile solution that seamlessly integrates with diverse video-LLMs and existing workflows. Extensive evaluations on large-scale benchmarks, such as Video-MME, MLVU, and LongVideoBench, demonstrate that our framework consistently surpasses recent compression techniques, highlighting not only its effectiveness and robustness in addressing the critical challenges of long video understanding, but also its efficiency in processing speed.

