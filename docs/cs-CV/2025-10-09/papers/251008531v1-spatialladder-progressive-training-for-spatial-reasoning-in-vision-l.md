---
layout: default
title: SpatialLadder: Progressive Training for Spatial Reasoning in Vision-Language Models
---

# SpatialLadder: Progressive Training for Spatial Reasoning in Vision-Language Models

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.08531" target="_blank" class="toolbar-btn">arXiv: 2510.08531v1</a>
    <a href="https://arxiv.org/pdf/2510.08531.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.08531v1" 
            onclick="toggleFavorite(this, '2510.08531v1', 'SpatialLadder: Progressive Training for Spatial Reasoning in Vision-Language Models')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Hongxing Li, Dingming Li, Zixuan Wang, Yuchen Yan, Hang Wu, Wenqi Zhang, Yongliang Shen, Weiming Lu, Jun Xiao, Yueting Zhuang

**分类**: cs.CV, cs.AI, cs.CL

**发布日期**: 2025-10-09

**备注**: Project Page: https://zju-real.github.io/SpatialLadder/ Code: https://github.com/ZJU-REAL/SpatialLadder

---

## 💡 一句话要点

**SpatialLadder：通过渐进式训练提升视觉语言模型中的空间推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `空间推理` `渐进式学习` `多模态数据集` `强化学习`

## 📋 核心要点

1. 现有视觉语言模型在空间推理方面表现不足，主要原因是缺乏对空间感知和理解的层级基础的构建。
2. 论文提出SpatialLadder方法，通过构建多模态数据集和设计三阶段渐进式训练框架，逐步提升模型的空间智能。
3. 实验结果表明，SpatialLadder模型在空间推理基准测试中取得了显著的性能提升，并保持了良好的泛化能力。

## 📝 摘要（中文）

本文提出了一种提升视觉语言模型（VLM）空间推理能力的综合方法。作者指出，现有方法缺乏对感知和理解的层级基础的建立，导致性能不佳。为了解决这个问题，作者构建了一个包含26610个样本的多模态数据集SpatialLadder-26k，涵盖了对象定位、单图像、多视角和视频空间推理任务。在此基础上，设计了一个三阶段渐进式训练框架，该框架首先通过对象定位建立空间感知，然后通过多维空间任务发展空间理解，最后通过强化学习和可验证的奖励来加强复杂推理。由此产生的SpatialLadder模型（30亿参数）在空间推理基准测试中取得了最先进的性能，平均比基线模型提高了23.4%，超过GPT-4o 20.8%，超过Gemini-2.0-Flash 10.1%。此外，SpatialLadder在领域外基准测试中保持了强大的泛化能力，提高了7.2%，表明从感知到推理的渐进式训练对于鲁棒的空间智能至关重要。

## 🔬 方法详解

**问题定义**：现有视觉语言模型在空间推理任务中表现不佳，无法有效理解和推理图像或视频中的空间关系。主要痛点在于，现有方法直接学习复杂的空间推理，而忽略了空间感知和理解的层级基础，导致模型难以泛化到新的场景。

**核心思路**：论文的核心思路是通过渐进式训练，逐步构建模型的空间智能。首先，通过对象定位建立空间感知；然后，通过多维空间任务发展空间理解；最后，通过强化学习加强复杂推理。这种由浅入深、循序渐进的方式，能够使模型更好地学习和掌握空间推理能力。

**技术框架**：SpatialLadder的整体框架包含三个主要阶段：(1) **空间感知阶段**：利用对象定位任务训练模型识别和定位图像中的物体。(2) **空间理解阶段**：通过单图像、多视角和视频空间推理任务，训练模型理解物体之间的空间关系。(3) **复杂推理阶段**：使用强化学习，通过可验证的奖励机制，训练模型进行更复杂的空间推理。

**关键创新**：论文的关键创新在于提出了一个渐进式训练框架，该框架模拟了人类学习空间推理的过程，从简单的感知到复杂的推理，逐步提升模型的空间智能。此外，SpatialLadder-26k数据集的构建也为该框架的训练提供了有力支持。

**关键设计**：SpatialLadder-26k数据集包含对象定位、单图像、多视角和视频空间推理任务，覆盖了不同的模态和难度级别。在训练过程中，使用了交叉熵损失函数进行对象定位，并设计了特定的奖励函数用于强化学习。模型采用3B参数的架构，具体网络结构细节未知。

## 📊 实验亮点

SpatialLadder模型在空间推理基准测试中取得了显著的性能提升，平均比基线模型提高了23.4%，超过GPT-4o 20.8%，超过Gemini-2.0-Flash 10.1%。更重要的是，SpatialLadder在领域外基准测试中也表现出色，提高了7.2%，证明了其良好的泛化能力。

## 🎯 应用场景

SpatialLadder的研究成果可应用于机器人导航、自动驾驶、智能监控、虚拟现实等领域。通过提升视觉语言模型的空间推理能力，可以使机器更好地理解周围环境，从而实现更智能、更自主的决策和行动。未来，该技术有望在智能家居、工业自动化等领域发挥重要作用。

## 📄 摘要（原文）

> Spatial reasoning remains a fundamental challenge for Vision-Language Models (VLMs), with current approaches struggling to achieve robust performance despite recent advances. We identify that this limitation stems from a critical gap: existing methods attempt to learn spatial reasoning directly without establishing the hierarchical foundations of perception and understanding. To address this challenge, we present a comprehensive methodology for building spatial intelligence progressively. We introduce SpatialLadder-26k, a multimodal dataset containing 26,610 samples spanning object localization, single image, multi-view, and video spatial reasoning tasks, constructed through a standardized pipeline that ensures systematic coverage across modalities. Building on this dataset, we design a three-stage progressive training framework that (1) establishes spatial perception through object localization, (2) develops spatial understanding through multi-dimensional spatial tasks, and (3) strengthens complex reasoning via reinforcement learning with verifiable rewards. This approach yields SpatialLadder, a 3B-parameter model that achieves state-of-the-art performance on spatial reasoning benchmarks, with 23.4% average improvement over the base model, surpassing GPT-4o by 20.8% and Gemini-2.0-Flash by 10.1%. Notably, SpatialLadder maintains strong generalization with 7.2% improvement on out-of-domain benchmarks, demonstrating that progressive training from perception to reasoning is essential for robust spatial intelligence.

