---
layout: default
title: "CronusVLA: Towards Efficient and Robust Manipulation via Multi-Frame Vision-Language-Action Modeling"
---

# CronusVLA: Towards Efficient and Robust Manipulation via Multi-Frame Vision-Language-Action Modeling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.19816" class="toolbar-btn" target="_blank">📄 arXiv: 2506.19816v2</a>
  <a href="https://arxiv.org/pdf/2506.19816.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.19816v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.19816v2', 'CronusVLA: Towards Efficient and Robust Manipulation via Multi-Frame Vision-Language-Action Modeling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hao Li, Shuai Yang, Yilun Chen, Xinyi Chen, Xiaoda Yang, Yang Tian, Hanqing Wang, Tai Wang, Dahua Lin, Feng Zhao, Jiangmiao Pang

**分类**: cs.RO, cs.CV

**发布日期**: 2025-06-24 (更新: 2025-10-30)

**备注**: 39 pages, 24 figures

---

## 💡 一句话要点

**提出CronusVLA以解决单帧图像在机器人操作中的局限性**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作` `多帧建模` `机器人操作` `鲁棒性评估` `特征聚合`

## 📋 核心要点

1. 现有的视觉-语言-动作模型受限于单帧图像，未能有效利用多帧历史信息，导致计算开销和推理延迟。
2. CronusVLA通过单帧预训练和多帧后训练的两阶段过程，扩展了单帧VLA模型，提升了多帧信息的利用效率。
3. 在多个模拟和真实环境中，CronusVLA在SimplerEnv上取得70.9%的成功率，相较于OpenVLA在LIBERO上提升了26.8%。

## 📝 摘要（中文）

近年来，基于预训练视觉-语言模型的视觉-语言-动作（VLA）模型在机器人操作中表现出色。然而，这些模型受限于单帧图像范式，未能充分利用多帧历史提供的时间信息。本文提出CronusVLA，一个统一框架，将单帧VLA模型扩展到多帧范式。CronusVLA采用两阶段过程：首先在大规模的具身数据集上进行单帧预训练，建立有效的具身视觉-语言基础；其次进行多帧后训练，通过特征块聚合历史信息，适应视觉-语言主干的预测。实验结果表明，CronusVLA在多帧建模的挑战中表现出色，具有更高的性能和观察鲁棒性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视觉-语言-动作模型在单帧图像范式下的局限性，特别是未能充分利用多帧历史信息的问题。这导致了计算开销和推理延迟的增加。

**核心思路**：CronusVLA的核心思路是通过两阶段的训练过程，首先在大规模数据集上进行单帧预训练，然后进行多帧后训练，以适应多帧信息的处理。这种设计旨在有效整合时间信息，提高模型的性能和鲁棒性。

**技术框架**：CronusVLA的整体架构包括两个主要阶段：第一阶段是单帧预训练，使用自回归预测动作标记；第二阶段是多帧后训练，将视觉-语言主干的预测从离散标记转变为可学习特征，并通过特征块聚合历史信息。

**关键创新**：CronusVLA的关键创新在于其多帧后训练机制，通过特征块聚合历史信息，显著提升了模型在多帧建模中的表现。这一方法与现有单帧模型的本质区别在于其对时间信息的有效利用。

**关键设计**：在设计上，CronusVLA采用了特征块聚合技术，允许模型在处理多帧信息时减少计算负担。此外，损失函数的设置和网络结构的优化也为模型的性能提升提供了支持。

## 📊 实验亮点

实验结果显示，CronusVLA在SimplerEnv上取得了70.9%的成功率，相较于OpenVLA在LIBERO上提升了26.8%。此外，在SimplerEnv-OR基准测试中，CronusVLA展现出最高的鲁棒性分数，证明了其在处理时间和空间干扰方面的优势。

## 🎯 应用场景

CronusVLA的研究成果在机器人操作、自动化制造和智能家居等领域具有广泛的应用潜力。通过提升机器人在复杂环境中的操作能力，该模型能够实现更高效的任务执行和更强的适应性，未来可能推动智能机器人在实际场景中的广泛部署。

## 📄 摘要（原文）

> Recent vision-language-action (VLA) models built on pretrained vision-language models (VLMs) have demonstrated strong performance in robotic manipulation. However, these models remain constrained by the single-frame image paradigm and fail to fully leverage the temporal information offered by multi-frame histories, as directly feeding multiple frames into VLM backbones incurs substantial computational overhead and inference latency. We propose CronusVLA, a unified framework that extends single-frame VLA models to the multi-frame paradigm. CronusVLA follows a two-stage process: (1) Single-frame pretraining on large-scale embodied datasets with autoregressive prediction of action tokens, establishing an effective embodied vision-language foundation; (2) Multi-frame post-training, which adapts the prediction of the vision-language backbone from discrete tokens to learnable features, and aggregates historical information via feature chunking. CronusVLA effectively addresses the existing challenges of multi-frame modeling while enhancing performance and observational robustness. To evaluate the robustness under temporal and spatial disturbances, we introduce SimplerEnv-OR, a novel benchmark featuring 24 types of observational disturbances and 120 severity levels. Experiments across three embodiments in simulated and real-world environments demonstrate that CronusVLA achieves leading performance and superior robustness, with a 70.9% success rate on SimplerEnv, a 26.8% improvement over OpenVLA on LIBERO, and the highest robustness score on SimplerEnv-OR. These results highlight the potential of efficient multi-frame adaptation in VLA models for more powerful and robust real-world deployment.

