---
layout: default
title: "EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models"
---

# EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10100" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10100v1</a>
  <a href="https://arxiv.org/pdf/2506.10100.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10100v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10100v1', 'EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yantai Yang, Yuhao Wang, Zichen Wen, Luo Zhongwei, Chang Zou, Zhipeng Zhang, Chuan Wen, Linfeng Zhang

**分类**: cs.CV

**发布日期**: 2025-06-11

---

## 💡 一句话要点

**提出EfficientVLA以解决VLA模型的加速与压缩问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作` `模型加速` `无训练框架` `多模态融合` `计算冗余`

## 📋 核心要点

1. 现有的VLA模型在推理时面临高计算和内存需求，限制了其实际应用。
2. EfficientVLA通过无训练的方式，系统性地消除VLA模型中的计算和内存瓶颈，整合多种冗余利用策略。
3. 在CogACT模型上，EfficientVLA实现了1.93倍的推理速度提升，FLOPs减少至28.9%，成功率仅下降0.6%。

## 📝 摘要（中文）

视觉-语言-动作（VLA）模型，尤其是基于扩散的架构，展现了在具身智能方面的变革潜力，但由于固有的冗余和推理时的高计算与内存需求，面临严重挑战。现有的加速方法往往只针对孤立的低效环节，无法全面解决VLA管道中的各种计算和内存瓶颈，限制了其实际应用。本文提出EfficientVLA，一个结构化且无训练的推理加速框架，通过系统性地消除这些障碍，综合利用多方面的冗余。EfficientVLA整合了三种针对性策略：语言模块中功能不重要层的剪枝、通过任务感知策略优化视觉处理路径，以及在迭代扩散动作头中通过缓存和重用关键中间特征来缓解时间计算冗余。应用于标准VLA模型CogACT，EfficientVLA实现了1.93倍的推理加速，FLOPs降低至28.9%，在SIMPLER基准测试中仅有0.6%的成功率下降。

## 🔬 方法详解

**问题定义**：本文旨在解决视觉-语言-动作（VLA）模型在推理过程中面临的高计算和内存需求问题。现有方法往往只针对单一低效环节，未能全面解决整个VLA管道中的多种计算和内存瓶颈。

**核心思路**：EfficientVLA的核心思路是通过无训练的方式，系统性地消除VLA模型中的冗余，整合多种策略以提升推理效率和降低资源消耗。

**技术框架**：EfficientVLA的整体架构包括三个主要模块：语言模块的剪枝、视觉处理路径的优化和扩散动作头的时间计算冗余缓解。这些模块协同工作，形成一个高效的推理框架。

**关键创新**：本研究的关键创新在于通过系统性分析和整合多种冗余，提出了一种无训练的推理加速框架，显著提升了VLA模型的推理效率，与现有方法相比，提供了更全面的解决方案。

**关键设计**：在语言模块中，通过分析层间冗余进行功能不重要层的剪枝；在视觉处理路径中，采用任务感知策略选择紧凑且多样的视觉标记；在扩散动作头中，通过缓存和重用关键中间特征来减少时间计算冗余。具体的参数设置和网络结构细节在论文中有详细描述。

## 📊 实验亮点

在CogACT模型上，EfficientVLA实现了1.93倍的推理速度提升，FLOPs降低至28.9%，并且在SIMPLER基准测试中仅有0.6%的成功率下降，显示出其在加速和压缩方面的显著效果。

## 🎯 应用场景

EfficientVLA的研究成果在多个领域具有潜在应用价值，包括机器人控制、智能助手和多模态交互系统。通过提升VLA模型的推理效率，该框架能够支持更复杂的任务和实时应用，推动具身智能的发展。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models, particularly diffusion-based architectures, demonstrate transformative potential for embodied intelligence but are severely hampered by high computational and memory demands stemming from extensive inherent and inference-time redundancies. While existing acceleration efforts often target isolated inefficiencies, such piecemeal solutions typically fail to holistically address the varied computational and memory bottlenecks across the entire VLA pipeline, thereby limiting practical deployability. We introduce EfficientVLA, a structured and training-free inference acceleration framework that systematically eliminates these barriers by cohesively exploiting multifaceted redundancies. EfficientVLA synergistically integrates three targeted strategies: (1) pruning of functionally inconsequential layers from the language module, guided by an analysis of inter-layer redundancies; (2) optimizing the visual processing pathway through a task-aware strategy that selects a compact, diverse set of visual tokens, balancing task-criticality with informational coverage; and (3) alleviating temporal computational redundancy within the iterative diffusion-based action head by strategically caching and reusing key intermediate features. We apply our method to a standard VLA model CogACT, yielding a 1.93X inference speedup and reduces FLOPs to 28.9%, with only a 0.6% success rate drop in the SIMPLER benchmark.

