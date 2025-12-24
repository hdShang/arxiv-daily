---
layout: default
title: "EVTP-IVS: Effective Visual Token Pruning For Unifying Instruction Visual Segmentation In Multi-Modal Large Language Models"
---

# EVTP-IVS: Effective Visual Token Pruning For Unifying Instruction Visual Segmentation In Multi-Modal Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.11886" class="toolbar-btn" target="_blank">📄 arXiv: 2508.11886v1</a>
  <a href="https://arxiv.org/pdf/2508.11886.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.11886v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.11886v1', 'EVTP-IVS: Effective Visual Token Pruning For Unifying Instruction Visual Segmentation In Multi-Modal Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenhui Zhu, Xiwen Chen, Zhipeng Wang, Shao Tang, Sayan Ghosh, Xuanzhao Dong, Rajat Koner, Yalin Wang

**分类**: cs.CV, cs.AI, cs.CL, cs.LG, eess.IV

**发布日期**: 2025-08-16

---

## 💡 一句话要点

**提出EVTP-IVS以解决多模态大语言模型中的视觉分割效率问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `指令视觉分割` `多模态大语言模型` `视觉标记修剪` `推理效率` `空间信息整合` `信息论分析` `视频处理` `图像处理`

## 📋 核心要点

1. 现有多模态大语言模型在指令视觉分割任务中推理成本高，尤其是在视频处理时，成为主要瓶颈。
2. 提出了一种新的视觉标记修剪方法EVTP-IV，通过整合空间信息选择具有代表性的标记子集，以加速推理过程。
3. 实验结果显示，EVTP-IV在视频任务上实现了最高5倍的速度提升，在图像任务上实现了3.5倍的速度提升，同时保持了相似的准确性。

## 📝 摘要（中文）

本论文针对指令视觉分割（IVS）任务，提出了一种新的视觉标记修剪方法EVTP-IV，以提高多模态大语言模型（MLLMs）在图像和视频处理中的推理效率。研究发现，视觉标记的子集覆盖率与分割性能之间存在显著相关性，因此设计了一种简单有效的标记修剪方法，选择一个紧凑且空间上具有代表性的标记子集以加速推理。通过信息论分析支持设计思路，实验结果表明，该方法在视频任务上实现了最高5倍的速度提升，在图像任务上实现了3.5倍的速度提升，同时仅使用20%的标记保持了相当的准确性。该方法在不同的修剪比例下均优于现有的最先进修剪基线。

## 🔬 方法详解

**问题定义**：本论文旨在解决指令视觉分割（IVS）任务中多模态大语言模型的推理效率问题。现有方法在处理视频时推理成本高，导致性能瓶颈。

**核心思路**：论文提出了一种名为EVTP-IV的视觉标记修剪方法，通过分析视觉标记的子集覆盖率与分割性能的关系，设计了一种选择紧凑且空间上具有代表性的标记子集的策略，以加速推理。

**技术框架**：整体架构包括三个主要模块：首先是视觉标记的采样与分析，其次是基于k中心算法的标记修剪，最后是信息论分析以支持设计决策。

**关键创新**：最重要的创新点在于将空间信息整合到标记选择过程中，确保所选标记能够更好地覆盖输入数据的特征。这一设计与现有方法的本质区别在于其强调空间代表性，而不仅仅是数量。

**关键设计**：在参数设置上，论文使用了信息论中的覆盖率指标来评估标记的有效性，并在损失函数中引入了与标记选择相关的权重，以优化标记的选择过程。

## 📊 实验亮点

实验结果表明，EVTP-IV在视频任务上实现了最高5倍的速度提升，在图像任务上实现了3.5倍的速度提升，同时仅使用20%的标记保持了相似的准确性。此外，该方法在不同的修剪比例下均优于现有的最先进修剪基线，显示出其广泛的适用性和有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能监控、自动驾驶、视频分析等场景，能够显著提高多模态大语言模型在处理复杂视觉任务时的效率和准确性。未来，随着技术的不断发展，该方法有望在实时视觉理解和交互式应用中发挥更大作用。

## 📄 摘要（原文）

> Instructed Visual Segmentation (IVS) tasks require segmenting objects in images or videos based on natural language instructions. While recent multimodal large language models (MLLMs) have achieved strong performance on IVS, their inference cost remains a major bottleneck, particularly in video. We empirically analyze visual token sampling in MLLMs and observe a strong correlation between subset token coverage and segmentation performance. This motivates our design of a simple and effective token pruning method that selects a compact yet spatially representative subset of tokens to accelerate inference. In this paper, we introduce a novel visual token pruning method for IVS, called EVTP-IV, which builds upon the k-center by integrating spatial information to ensure better coverage. We further provide an information-theoretic analysis to support our design. Experiments on standard IVS benchmarks show that our method achieves up to 5X speed-up on video tasks and 3.5X on image tasks, while maintaining comparable accuracy using only 20% of the tokens. Our method also consistently outperforms state-of-the-art pruning baselines under varying pruning ratios.

