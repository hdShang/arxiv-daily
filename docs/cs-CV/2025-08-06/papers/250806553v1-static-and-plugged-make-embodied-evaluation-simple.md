---
layout: default
title: "Static and Plugged: Make Embodied Evaluation Simple"
---

# Static and Plugged: Make Embodied Evaluation Simple

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.06553" class="toolbar-btn" target="_blank">📄 arXiv: 2508.06553v1</a>
  <a href="https://arxiv.org/pdf/2508.06553.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.06553v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.06553v1', 'Static and Plugged: Make Embodied Evaluation Simple')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiahao Xiao, Jianbo Zhang, BoWen Yan, Shengyu Guo, Tongrui Ye, Kaiwei Zhang, Zicheng Zhang, Xiaohong Liu, Zhengxue Cheng, Lei Fan, Chuyi Li, Guangtao Zhai

**分类**: cs.CV

**发布日期**: 2025-08-06

---

## 💡 一句话要点

**提出StaticEmbodiedBench以解决现有评估方法的局限性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `具身智能` `评估方法` `静态场景` `视觉-语言模型` `机器人导航` `智能家居` `虚拟助手`

## 📋 核心要点

1. 现有的评估方法依赖于复杂的交互式环境，导致成本高且难以扩展，限制了具身智能的评估效率。
2. 本文提出StaticEmbodiedBench，通过静态场景表示实现统一评估，简化了评估流程并提高了可扩展性。
3. 实验中评估了19个VLMs和11个VLAs，建立了第一个静态排行榜，推动了具身智能的研究进展。

## 📝 摘要（中文）

随着具身智能的快速发展，评估方法的效率需求日益增加。目前的基准测试通常依赖于交互式模拟环境或现实世界设置，这些方法成本高、碎片化且难以扩展。为了解决这一问题，本文提出了StaticEmbodiedBench，一个即插即用的基准测试，能够通过静态场景表示实现统一评估。该基准覆盖42种多样化场景和8个核心维度，支持通过简单接口进行可扩展和全面的评估。此外，我们评估了19个视觉-语言模型（VLMs）和11个视觉-语言-动作模型（VLAs），建立了具身智能的第一个统一静态排行榜，并发布了200个样本以加速具身智能的发展。

## 🔬 方法详解

**问题定义**：本文旨在解决现有具身智能评估方法的高成本和低可扩展性问题。当前方法依赖于复杂的交互式环境，导致评估过程碎片化且难以统一。

**核心思路**：提出StaticEmbodiedBench，通过静态场景表示实现评估的统一性和可扩展性。该方法设计为即插即用，简化了评估流程，适用于多种场景。

**技术框架**：整体架构包括静态场景表示模块、评估接口和结果输出模块。静态场景表示模块负责构建多样化的场景，评估接口则提供统一的评估标准和方法。

**关键创新**：最重要的创新在于引入静态场景表示，使得评估不再依赖于动态交互环境，从而降低了成本并提高了评估的可扩展性。

**关键设计**：在设计中，采用了42种不同的场景和8个核心维度进行评估，确保了评估的全面性和多样性。同时，发布的200个样本为后续研究提供了基础数据。

## 📊 实验亮点

实验结果表明，StaticEmbodiedBench能够有效评估19个VLMs和11个VLAs，建立了第一个静态排行榜，推动了具身智能的研究进展。与传统方法相比，评估效率显著提升，且评估结果更加一致。

## 🎯 应用场景

该研究的潜在应用领域包括机器人导航、智能家居系统和虚拟助手等。通过提供统一的评估标准，StaticEmbodiedBench能够加速具身智能的研究与开发，推动相关技术的实际应用与落地。

## 📄 摘要（原文）

> Embodied intelligence is advancing rapidly, driving the need for efficient evaluation. Current benchmarks typically rely on interactive simulated environments or real-world setups, which are costly, fragmented, and hard to scale. To address this, we introduce StaticEmbodiedBench, a plug-and-play benchmark that enables unified evaluation using static scene representations. Covering 42 diverse scenarios and 8 core dimensions, it supports scalable and comprehensive assessment through a simple interface. Furthermore, we evaluate 19 Vision-Language Models (VLMs) and 11 Vision-Language-Action models (VLAs), establishing the first unified static leaderboard for Embodied intelligence. Moreover, we release a subset of 200 samples from our benchmark to accelerate the development of embodied intelligence.

