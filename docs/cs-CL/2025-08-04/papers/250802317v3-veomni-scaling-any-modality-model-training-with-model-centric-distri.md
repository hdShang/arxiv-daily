---
layout: default
title: "VeOmni: Scaling Any Modality Model Training with Model-Centric Distributed Recipe Zoo"
---

# VeOmni: Scaling Any Modality Model Training with Model-Centric Distributed Recipe Zoo

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.02317" class="toolbar-btn" target="_blank">📄 arXiv: 2508.02317v3</a>
  <a href="https://arxiv.org/pdf/2508.02317.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.02317v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.02317v3', 'VeOmni: Scaling Any Modality Model Training with Model-Centric Distributed Recipe Zoo')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qianli Ma, Yaowei Zheng, Zhelun Shi, Zhongkai Zhao, Bin Jia, Ziyue Huang, Zhiqi Lin, Youjie Li, Jiacheng Yang, Yanghua Peng, Zhi Zhang, Xin Liu

**分类**: cs.CL, cs.AI, cs.DC

**发布日期**: 2025-08-04 (更新: 2025-08-07)

---

## 💡 一句话要点

**提出VeOmni以解决多模态大模型训练效率低下问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `大模型训练` `分布式计算` `模型中心设计` `高效并行`

## 📋 核心要点

1. 现有的多模态大模型训练方法在可扩展性和工程效率上存在显著不足，难以满足大规模训练的需求。
2. VeOmni通过模块化设计和模型中心的分布式配方，将通信与计算解耦，实现了高效的3D并行训练。
3. 实验结果表明，VeOmni能够以超过2800个token/秒的速度训练300亿参数的多模态模型，并支持扩展到16万的上下文长度。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）的进展推动了多模态理解和生成的显著进展。然而，由于处理多样化模态所需的异构模型架构，训练多模态LLMs仍然面临重大挑战。现有框架通常将模型定义与并行逻辑纠缠在一起，导致可扩展性有限和工程开销巨大。本文提出了VeOmni，一个模块化和高效的训练框架，以加速多模态LLMs的开发。VeOmni引入了模型中心的分布式配方，将通信与计算解耦，实现了多模态LLMs的高效3D并行。VeOmni还具有灵活的配置接口，支持以最小的代码更改无缝集成新模态。使用VeOmni，一个具有300亿参数的多模态专家模型可以以每GPU超过2800个token/秒的吞吐量进行训练，并通过128个GPU扩展到16万的上下文长度，展示了其在训练大型多模态LLMs方面的卓越效率和可扩展性。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态大模型训练中的可扩展性和效率问题。现有方法通常将模型定义与并行逻辑混合，导致工程开销大且难以扩展。

**核心思路**：VeOmni的核心思路是通过模块化设计和模型中心的分布式配方，将通信与计算解耦，从而实现高效的3D并行训练。这种设计使得不同模态的集成变得更加灵活和高效。

**技术框架**：VeOmni的整体架构包括多个模块，主要包括模型定义模块、通信模块和计算模块。通过将这些模块分开，VeOmni能够在不同的硬件资源上实现高效的并行计算。

**关键创新**：VeOmni的关键创新在于其模型中心的分布式配方，能够有效地解耦通信与计算，显著提高了训练效率和可扩展性。这与现有方法的紧耦合设计形成了鲜明对比。

**关键设计**：在VeOmni中，关键的参数设置和网络结构设计使得在不同GPU之间的负载均衡得以优化。此外，灵活的配置接口支持快速集成新模态，减少了代码更改的需求。

## 📊 实验亮点

实验结果显示，VeOmni能够以超过2800个token/秒的速度训练一个300亿参数的多模态专家模型，并且在128个GPU上扩展到16万的上下文长度。这一性能显著优于现有的训练框架，展示了其在大规模多模态训练中的优势。

## 🎯 应用场景

VeOmni的研究成果在多个领域具有广泛的应用潜力，包括自然语言处理、计算机视觉和多模态交互等。其高效的训练框架能够加速多模态模型的开发，推动智能系统在复杂任务中的表现提升，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Recent advances in large language models (LLMs) have driven impressive progress in omni-modal understanding and generation. However, training omni-modal LLMs remains a significant challenge due to the heterogeneous model architectures required to process diverse modalities, necessitating sophisticated system design for efficient large-scale training. Existing frameworks typically entangle model definition with parallel logic, incurring limited scalability and substantial engineering overhead for end-to-end omni-modal training. We present VeOmni, a modular and efficient training framework to accelerate the development of omni-modal LLMs. VeOmni introduces model-centric distributed recipes that decouples communication from computation, enabling efficient 3D parallelism on omni-modal LLMs. VeOmni also features a flexible configuration interface supporting seamless integration of new modalities with minimal code change. Using VeOmni, a omni-modal mixture-of-experts (MoE) model with 30B parameters can be trained with over 2,800 tokens/sec/GPU throughput and scale to 160K context lengths via 3D parallelism on 128 GPUs, showcasing its superior efficiency and scalability for training large omni-modal LLMs.

