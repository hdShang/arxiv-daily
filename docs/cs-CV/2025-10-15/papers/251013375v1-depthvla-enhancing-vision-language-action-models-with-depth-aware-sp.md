---
layout: default
title: DepthVLA: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning
---

# DepthVLA: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.13375" class="toolbar-btn" target="_blank">📄 arXiv: 2510.13375v1</a>
  <a href="https://arxiv.org/pdf/2510.13375.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.13375v1" onclick="toggleFavorite(this, '2510.13375v1', 'DepthVLA: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tianyuan Yuan, Yicheng Liu, Chenhao Lu, Zhuoguang Chen, Tao Jiang, Hang Zhao

**分类**: cs.CV

**发布日期**: 2025-10-15

---

## 💡 一句话要点

**DepthVLA：通过深度感知的空间推理增强视觉-语言-动作模型**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作模型` `深度学习` `空间推理` `机器人操作` `深度感知`

## 📋 核心要点

1. 现有VLA模型在精确空间推理任务中表现不佳，原因是VLM的空间推理能力不足，且依赖大量动作数据预训练。
2. DepthVLA通过预训练的深度预测模块显式地引入空间感知，采用混合Transformer架构，实现端到端的空间推理增强。
3. 实验结果表明，DepthVLA在真实世界和模拟环境中均优于现有方法，显著提升了VLA模型的性能。

## 📝 摘要（中文）

视觉-语言-动作(VLA)模型最近展示了令人印象深刻的泛化和语言引导的操作能力。然而，由于视觉-语言模型(VLM)固有的空间推理能力有限，它们在需要精确空间推理的任务上的性能会下降。现有的VLA依赖于大量的动作数据预训练，以将VLM定位在3D空间中，这降低了训练效率，并且对于准确的空间理解仍然是不够的。在这项工作中，我们提出了DepthVLA，一个简单而有效的VLA架构，它通过预训练的深度预测模块显式地结合了空间感知。DepthVLA采用混合Transformer的设计，统一了VLM、深度Transformer和动作专家，并具有完全共享的注意力机制，形成了一个具有增强空间推理能力的端到端模型。在真实世界和模拟环境中的大量评估表明，DepthVLA优于最先进的方法，在真实世界任务中取得了78.5% vs. 65.0%的进展，在LIBERO模拟器中取得了94.9% vs. 93.6%的进展，在Simpler模拟器中取得了74.8% vs. 58.8%的进展。我们的代码将公开发布。

## 🔬 方法详解

**问题定义**：现有的视觉-语言-动作(VLA)模型在处理需要精确空间推理的任务时面临挑战。这些模型依赖于视觉-语言模型(VLM)，而VLM本身的空间推理能力有限。为了弥补这一缺陷，现有方法通常采用大量的动作数据进行预训练，以使VLM能够理解3D空间。然而，这种方法效率低下，并且仍然无法保证准确的空间理解。

**核心思路**：DepthVLA的核心思路是通过显式地引入深度信息来增强VLA模型的空间感知能力。该方法利用预训练的深度预测模块来估计场景的深度图，并将深度信息融入到VLA模型的处理流程中。通过这种方式，模型可以更准确地理解场景的3D结构，从而提高空间推理的性能。

**技术框架**：DepthVLA的整体架构是一个混合Transformer模型，它由三个主要模块组成：一个视觉-语言模型(VLM)，一个深度Transformer和一个动作专家。VLM负责处理视觉和语言输入，深度Transformer负责处理深度信息，动作专家负责生成动作指令。这三个模块通过完全共享的注意力机制进行连接，从而实现端到端的训练。

**关键创新**：DepthVLA的关键创新在于显式地将深度信息融入到VLA模型的处理流程中。与现有方法相比，DepthVLA不需要依赖大量的动作数据进行预训练，而是通过预训练的深度预测模块来获取深度信息。这种方法不仅提高了训练效率，而且还能够更准确地理解场景的3D结构。

**关键设计**：DepthVLA的关键设计包括：1) 使用预训练的深度预测模块来估计场景的深度图；2) 使用深度Transformer来处理深度信息；3) 使用完全共享的注意力机制来连接VLM、深度Transformer和动作专家；4) 使用端到端的训练方法来优化整个模型。

## 📊 实验亮点

DepthVLA在真实世界和模拟环境中都取得了显著的性能提升。在真实世界任务中，DepthVLA的性能提升了78.5%，而现有最佳方法仅为65.0%。在LIBERO模拟器中，DepthVLA的性能提升到了94.9%，而现有最佳方法为93.6%。在Simpler模拟器中，DepthVLA的性能提升到了74.8%，而现有最佳方法为58.8%。这些结果表明，DepthVLA能够有效地提高VLA模型的空间推理能力。

## 🎯 应用场景

DepthVLA具有广泛的应用前景，例如机器人操作、自动驾驶、虚拟现实和增强现实等领域。它可以帮助机器人更准确地理解周围环境，从而执行更复杂的任务。在自动驾驶领域，它可以提高车辆对周围环境的感知能力，从而提高驾驶安全性。在虚拟现实和增强现实领域，它可以提供更逼真的3D体验。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models have recently shown impressive generalization and language-guided manipulation capabilities. However, their performance degrades on tasks requiring precise spatial reasoning due to limited spatial reasoning inherited from Vision-Language Models (VLMs). Existing VLAs rely on extensive action-data pretraining to ground VLMs in 3D space, which reduces training efficiency and is still insufficient for accurate spatial understanding. In this work, we present DepthVLA, a simple yet effective VLA architecture that explicitly incorporates spatial awareness through a pretrained depth prediction module. DepthVLA adopts a mixture-of-transformers design that unifies a VLM, a depth transformer, and an action expert with fully shared attentions, forming an end-to-end model with enhanced spatial reasoning. Extensive evaluations in both real-world and simulated environments show that DepthVLA outperforms state-of-the-art approaches, achieving 78.5% vs. 65.0% progress in real-world tasks, 94.9% vs. 93.6% in the LIBERO simulator, and 74.8% vs. 58.8% in the Simpler simulator. Our code will be made publicly available.

