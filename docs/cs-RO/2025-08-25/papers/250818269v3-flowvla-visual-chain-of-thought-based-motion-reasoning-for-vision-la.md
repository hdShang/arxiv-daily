---
layout: default
title: "FlowVLA: Visual Chain of Thought-based Motion Reasoning for Vision-Language-Action Models"
---

# FlowVLA: Visual Chain of Thought-based Motion Reasoning for Vision-Language-Action Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18269" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18269v3</a>
  <a href="https://arxiv.org/pdf/2508.18269.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18269v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18269v3', 'FlowVLA: Visual Chain of Thought-based Motion Reasoning for Vision-Language-Action Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhide Zhong, Haodong Yan, Junfeng Li, Xiangchen Liu, Xin Gong, Tianran Zhang, Wenxuan Song, Jiayi Chen, Xinhu Zheng, Hesheng Wang, Haoang Li

**分类**: cs.RO

**发布日期**: 2025-08-25 (更新: 2025-10-07)

**🔗 代码/项目**: [PROJECT_PAGE](https://irpn-lab.github.io/FlowVLA/)

---

## 💡 一句话要点

**提出FlowVLA以解决视觉-语言-动作模型中的运动推理问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱四：生成式动作 (Generative Motion)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作` `运动推理` `自回归Transformer` `光流预测` `机器人操作` `多模态学习`

## 📋 核心要点

1. 现有的VLA模型在运动推理方面存在不足，直接预测未来帧的外观导致视觉预测不够合理。
2. 本文提出了视觉思维链（Visual CoT）概念，要求模型在生成未来帧之前，先进行运动动态推理。
3. FlowVLA在机器人操作基准测试中表现出色，生成的视觉预测更为连贯，策略性能达到最先进水平，样本效率显著提升。

## 📝 摘要（中文）

许多视觉-语言-动作（VLA）模型依赖于通过下一帧预测训练的内部世界模型。然而，这种方法直接预测未来帧的外观，缺乏对潜在动态的明确推理，导致视觉预测不够合理且策略学习效率低下。为了解决这一问题，本文引入了视觉思维链（Visual Chain of Thought，Visual CoT），要求模型在生成未来帧之前，首先推理运动动态。我们提出了FlowVLA，这是一种自回归Transformer，明确将这一推理过程表示为$v_t ightarrow f_t ightarrow v_{t+1}$，其中$f_t$是固有编码运动的中间光流预测。通过强制模型遵循由$f_t$编码的运动计划，该过程自然地将动态预测的预训练目标与动作生成的下游任务对齐。实验结果表明，FlowVLA不仅生成更连贯且物理上合理的视觉预测，还在策略性能上达到了最先进水平，并显著提高了样本效率。

## 🔬 方法详解

**问题定义**：本文旨在解决现有VLA模型在运动推理方面的不足，现有方法直接预测未来帧，缺乏对运动动态的明确推理，导致生成的视觉预测不够合理。

**核心思路**：本文提出视觉思维链（Visual CoT），要求模型首先推理运动动态，然后再生成未来帧。这一设计使得动态预测的预训练目标与下游动作生成任务相对齐。

**技术框架**：FlowVLA采用自回归Transformer架构，整体流程为$v_t ightarrow f_t ightarrow v_{t+1}$，其中$f_t$是光流预测，模型通过这一中间步骤进行运动推理。

**关键创新**：FlowVLA的核心创新在于引入了运动推理步骤，将光流预测作为中间表示，显著提高了生成的视觉预测的物理合理性和连贯性。

**关键设计**：在模型设计中，采用了自回归机制和光流预测模块，损失函数结合了动态预测和动作生成的目标，以确保模型在训练过程中能够有效学习运动动态。

## 📊 实验亮点

实验结果显示，FlowVLA在机器人操作基准测试中生成的视觉预测比现有方法更为连贯且物理上合理，策略性能达到了最先进水平，样本效率显著提高，具体提升幅度未知。

## 🎯 应用场景

该研究的潜在应用领域包括机器人操作、自动驾驶、虚拟现实等，能够为这些领域提供更为合理的视觉预测和决策支持。未来，FlowVLA可能推动更高效的多模态学习和人机交互技术的发展。

## 📄 摘要（原文）

> Many Vision-Language-Action (VLA) models are built upon an internal world model trained via next-frame prediction ``$v_t \rightarrow v_{t+1}$''. However, this paradigm attempts to predict the future frame's appearance directly, without explicitly reasoning about the underlying dynamics. \textbf{This lack of an explicit motion reasoning step} often leads to physically implausible visual forecasts and inefficient policy learning. To address this limitation, we introduce the \textbf{Visual Chain of Thought (Visual CoT)}, a paradigm that compels the model to first reason about \textbf{motion dynamics} before generating the future frame. We instantiate this paradigm by proposing \textbf{FlowVLA}, an autoregressive Transformer that explicitly materializes this reasoning process as ``$v_t \rightarrow f_t \rightarrow v_{t+1}$'', where $f_t$ is an intermediate optical flow prediction that inherently encodes motion. By forcing the model to first follow the motion plan encoded by $f_t$, this process inherently \textbf{aligns the pre-training objective of dynamics prediction with the downstream task of action generation.} We conduct experiments on challenging robotics manipulation benchmarks, as well as real-robot evaluations. Our FlowVLA not only generates \textbf{more coherent and physically plausible visual predictions}, but also achieves state-of-the-art policy performance with \textbf{substantially improved sample efficiency}, pointing toward a more principled foundation for world modeling in VLAs. Project page: https://irpn-lab.github.io/FlowVLA/

