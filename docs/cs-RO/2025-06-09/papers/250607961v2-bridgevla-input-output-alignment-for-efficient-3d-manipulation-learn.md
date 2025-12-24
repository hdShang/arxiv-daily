---
layout: default
title: "BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models"
---

# BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.07961" class="toolbar-btn" target="_blank">📄 arXiv: 2506.07961v2</a>
  <a href="https://arxiv.org/pdf/2506.07961.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.07961v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.07961v2', 'BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Peiyan Li, Yixiang Chen, Hongtao Wu, Xiao Ma, Xiangnan Wu, Yan Huang, Liang Wang, Tao Kong, Tieniu Tan

**分类**: cs.RO, cs.AI

**发布日期**: 2025-06-09 (更新: 2025-10-14)

**备注**: NeurIPS 2025

---

## 💡 一句话要点

**提出BridgeVLA以解决3D操控学习中的低样本效率问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言模型` `3D操控学习` `动作预测` `样本效率` `机器人技术`

## 📋 核心要点

1. 现有方法在3D信号的利用上存在不足，导致动作预测的样本效率低下。
2. BridgeVLA通过将3D输入投影到2D图像并使用2D热图进行动作预测，解决了输入输出对齐的问题。
3. 实验结果显示，BridgeVLA在多个基准测试中表现优异，成功率显著提高，展示了其卓越的样本效率。

## 📝 摘要（中文）

近年来，利用预训练的视觉-语言模型（VLMs）构建视觉-语言-动作（VLA）模型成为有效机器人操控学习的一种有前景的方法。然而，现有方法在动作预测中很少将3D信号纳入VLMs，并未充分利用3D数据固有的空间结构，导致样本效率低下。本文提出了BridgeVLA，一个新颖的3D VLA模型，通过将3D输入投影到多个2D图像，确保与VLM主干的输入对齐，并利用2D热图进行动作预测，从而在一致的2D图像空间内统一输入和输出。大量实验表明，该方法能够高效有效地学习3D操控，并在三个模拟基准上超越了最先进的基线方法。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视觉-语言-动作模型在3D操控学习中低样本效率的问题。现有方法未能充分利用3D数据的空间结构，导致动作预测效果不佳。

**核心思路**：BridgeVLA的核心思路是将3D输入投影到多个2D图像中，以确保与VLM主干的输入对齐，并通过2D热图进行动作预测，从而统一输入和输出空间。

**技术框架**：BridgeVLA的整体架构包括三个主要模块：3D输入投影模块、2D热图生成模块和下游策略学习模块。首先，3D输入被转换为多个2D图像，然后生成相应的2D热图，最后进行策略学习以实现动作预测。

**关键创新**：BridgeVLA的主要创新在于其输入输出的对齐机制，通过将3D数据有效地映射到2D空间，显著提高了样本效率和学习效果。这一设计与现有方法的本质区别在于更好地利用了2D图像的特征。

**关键设计**：在关键设计上，BridgeVLA采用了可扩展的预训练方法，使VLM主干具备预测2D热图的能力，此外，损失函数的设计也针对2D热图的准确性进行了优化。

## 📊 实验亮点

在实验中，BridgeVLA在RLBench中将平均成功率从81.4%提升至88.2%，在COLOSSEUM中从56.7%提升至64.0%。在GemBench中，BridgeVLA超越了所有对比基线方法。在真实机器人实验中，BridgeVLA的表现比最先进的基线方法平均提高32%。

## 🎯 应用场景

BridgeVLA的研究成果在机器人操控、智能制造和人机交互等领域具有广泛的应用潜力。通过提高3D操控学习的效率，该模型能够帮助机器人更好地理解和执行复杂的任务，进而推动智能机器人技术的进步与普及。

## 📄 摘要（原文）

> Recently, leveraging pre-trained vision-language models (VLMs) for building vision-language-action (VLA) models has emerged as a promising approach to effective robot manipulation learning. However, only few methods incorporate 3D signals into VLMs for action prediction, and they do not fully leverage the spatial structure inherent in 3D data, leading to low sample efficiency. In this paper, we introduce BridgeVLA, a novel 3D VLA model that (1) projects 3D inputs to multiple 2D images, ensuring input alignment with the VLM backbone, and (2) utilizes 2D heatmaps for action prediction, unifying the input and output spaces within a consistent 2D image space. In addition, we propose a scalable pre-training method that equips the VLM backbone with the capability to predict 2D heatmaps before downstream policy learning. Extensive experiments show the proposed method is able to learn 3D manipulation efficiently and effectively. BridgeVLA outperforms state-of-the-art baseline methods across three simulation benchmarks. In RLBench, it improves the average success rate from 81.4% to 88.2%. In COLOSSEUM, it demonstrates significantly better performance in challenging generalization settings, boosting the average success rate from 56.7% to 64.0%. In GemBench, it surpasses all the comparing baseline methods in terms of average success rate. In real-robot experiments, BridgeVLA outperforms a state-of-the-art baseline method by 32% on average. It generalizes robustly in multiple out-of-distribution settings, including visual disturbances and unseen instructions. Remarkably, it is able to achieve a success rate of 96.8% on 10+ tasks with only 3 trajectories per task, highlighting its extraordinary sample efficiency. Project Website:https://bridgevla.github.io/

