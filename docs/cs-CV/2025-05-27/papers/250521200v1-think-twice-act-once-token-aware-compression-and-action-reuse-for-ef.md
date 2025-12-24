---
layout: default
title: "Think Twice, Act Once: Token-Aware Compression and Action Reuse for Efficient Inference in Vision-Language-Action Models"
---

# Think Twice, Act Once: Token-Aware Compression and Action Reuse for Efficient Inference in Vision-Language-Action Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21200" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21200v1</a>
  <a href="https://arxiv.org/pdf/2505.21200.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21200v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21200v1', 'Think Twice, Act Once: Token-Aware Compression and Action Reuse for Efficient Inference in Vision-Language-Action Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xudong Tan, Yaoxin Yang, Peng Ye, Jialin Zheng, Bizhe Bai, Xinyi Wang, Jia Hao, Tao Chen

**分类**: cs.CV

**发布日期**: 2025-05-27

---

## 💡 一句话要点

**提出FlashVLA以解决VLA模型推理效率低下问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作` `动作重用` `推理效率` `边缘计算` `自然语言处理`

## 📋 核心要点

1. 现有VLA模型在推理过程中面临高计算成本和延迟，限制了其在实时和边缘应用中的部署。
2. 本文提出FlashVLA框架，通过动作重用和视觉token选择策略，显著提高VLA模型的推理效率。
3. 实验结果显示，FlashVLA在保持任务成功率的同时，FLOPs减少55.7%，延迟降低36.0%，展现了其有效性。

## 📝 摘要（中文）

视觉-语言-动作（VLA）模型作为一种强大的通用机器人控制范式，通过自然语言指令进行操作。然而，由于大规模的token计算和自回归解码，推理成本高，给实时部署和边缘应用带来了显著挑战。本文提出FlashVLA，这是第一个无需训练且即插即用的加速框架，能够在VLA模型中实现动作重用。FlashVLA通过token感知的动作重用机制和信息引导的视觉token选择策略，提高了推理效率。实验结果表明，FlashVLA在LIBERO基准上将FLOPs减少了55.7%，延迟降低了36.0%，任务成功率仅下降0.7%。

## 🔬 方法详解

**问题定义**：本文旨在解决视觉-语言-动作（VLA）模型在推理过程中面临的高计算成本和延迟问题。现有方法主要集中于架构优化，未能有效应对连续动作步骤的高相似性和视觉token的冗余性。

**核心思路**：FlashVLA通过识别VLA模型中的冗余性，提出了一种token感知的动作重用机制，避免在稳定动作步骤中进行冗余解码，同时采用信息引导的视觉token选择策略，剔除低贡献的token，从而提高推理效率。

**技术框架**：FlashVLA框架包括两个主要模块：动作重用模块和视觉token选择模块。动作重用模块负责识别和重用相似的动作步骤，而视觉token选择模块则通过信息引导策略选择对任务贡献较大的token。

**关键创新**：FlashVLA的主要创新在于其训练-free的设计，允许在不需要重新训练模型的情况下实现加速。这一设计与现有方法的本质区别在于其关注于动作步骤和token的冗余性，而非单纯的架构优化。

**关键设计**：在FlashVLA中，动作重用机制通过分析连续动作的相似性来实现，而视觉token选择则基于信息增益进行token的筛选。具体的参数设置和损失函数设计未在摘要中详细说明，需参考原文获取更多技术细节。

## 📊 实验亮点

实验结果表明，FlashVLA在LIBERO基准上实现了显著的性能提升，FLOPs减少了55.7%，延迟降低了36.0%，而任务成功率仅下降0.7%。这些结果展示了FlashVLA在实现轻量级、低延迟VLA推理方面的有效性，具有重要的实际应用价值。

## 🎯 应用场景

FlashVLA的研究成果具有广泛的应用潜力，尤其是在需要实时响应的机器人控制和智能助手等领域。其高效的推理能力使得VLA模型能够在边缘设备上运行，从而推动自然语言处理与机器人技术的结合，提升人机交互的智能化水平。未来，FlashVLA可能会在更多复杂任务中得到应用，进一步推动智能系统的发展。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models have emerged as a powerful paradigm for general-purpose robot control through natural language instructions. However, their high inference cost-stemming from large-scale token computation and autoregressive decoding-poses significant challenges for real-time deployment and edge applications. While prior work has primarily focused on architectural optimization, we take a different perspective by identifying a dual form of redundancy in VLA models: (i) high similarity across consecutive action steps, and (ii) substantial redundancy in visual tokens. Motivated by these observations, we propose FlashVLA, the first training-free and plug-and-play acceleration framework that enables action reuse in VLA models. FlashVLA improves inference efficiency through a token-aware action reuse mechanism that avoids redundant decoding across stable action steps, and an information-guided visual token selection strategy that prunes low-contribution tokens. Extensive experiments on the LIBERO benchmark show that FlashVLA reduces FLOPs by 55.7% and latency by 36.0%, with only a 0.7% drop in task success rate. These results demonstrate the effectiveness of FlashVLA in enabling lightweight, low-latency VLA inference without retraining.

