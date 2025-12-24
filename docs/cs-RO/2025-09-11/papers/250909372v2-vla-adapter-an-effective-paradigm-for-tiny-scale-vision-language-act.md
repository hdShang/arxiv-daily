---
layout: default
title: "VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model"
---

# VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09372" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09372v2</a>
  <a href="https://arxiv.org/pdf/2509.09372.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09372v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09372v2', 'VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yihao Wang, Pengxiang Ding, Lingxiao Li, Can Cui, Zirui Ge, Xinyang Tong, Wenxuan Song, Han Zhao, Wei Zhao, Pengxu Hou, Siteng Huang, Yifan Tang, Wenhui Wang, Ru Zhang, Jianyi Liu, Donglin Wang

**分类**: cs.RO

**发布日期**: 2025-09-11 (更新: 2025-09-22)

**备注**: 28 pages; Project page: https://vla-adapter.github.io/; Github: https://github.com/OpenHelix-Team/VLA-Adapter; HuggingFace: https://huggingface.co/VLA-Adapter

**🔗 代码/项目**: [PROJECT_PAGE](https://vla-adapter.github.io/)

---

## 💡 一句话要点

**VLA-Adapter：一种高效的微型视觉-语言-动作模型范式**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作模型` `机器人控制` `Bridge Attention` `轻量级模型` `迁移学习`

## 📋 核心要点

1. 现有VLA模型依赖大规模VLM预训练，成本高昂，如何降低对大型VLM的依赖是核心问题。
2. VLA-Adapter通过分析VL条件的重要性，设计带Bridge Attention的轻量级策略模块，自主注入最优条件。
3. 实验表明，VLA-Adapter仅用0.5B参数骨干网络即可达到SOTA性能，且推理速度快，单GPU 8小时即可训练完成。

## 📝 摘要（中文）

视觉-语言-动作(VLA)模型通常通过在机器人数据上预训练大规模视觉-语言模型(VLM)来弥合感知和动作空间之间的差距。虽然这种方法极大地提高了性能，但也带来了巨大的训练成本。本文研究了如何有效地将视觉-语言(VL)表示桥接到动作(A)。我们引入了VLA-Adapter，这是一种旨在减少VLA模型对大型VLM和广泛预训练的依赖的新范式。为此，我们首先系统地分析了各种VL条件的有效性，并提出了关于哪些条件对于桥接感知和动作空间至关重要的关键发现。基于这些见解，我们提出了一个带有Bridge Attention的轻量级策略模块，该模块自主地将最佳条件注入到动作空间中。通过这种方式，我们的方法仅使用0.5B参数的骨干网络即可实现高性能，而无需任何机器人数据预训练。在模拟和真实机器人基准上的大量实验表明，VLA-Adapter不仅实现了最先进的性能水平，而且还提供了迄今为止最快的推理速度。此外，由于所提出的先进桥接范式，VLA-Adapter能够在单个消费级GPU上仅用8小时训练一个强大的VLA模型，大大降低了部署VLA模型的门槛。

## 🔬 方法详解

**问题定义**：VLA模型旨在连接视觉、语言和动作空间，实现机器人等智能体的自主决策。现有方法依赖于大规模视觉-语言模型（VLM）的预训练，这带来了巨大的计算和数据成本，限制了VLA模型的部署和应用。因此，如何降低VLA模型对大规模VLM的依赖，同时保持甚至提升性能，是本文要解决的关键问题。现有方法的痛点在于预训练成本高，模型体积大，推理速度慢。

**核心思路**：本文的核心思路是通过分析不同视觉-语言（VL）条件对动作空间的影响，找出最有效的条件，并设计一个轻量级的策略模块，将这些关键条件自主地注入到动作空间中。这种方法避免了对整个VLM进行微调或重新训练，从而大大降低了计算成本和数据需求。核心在于找到VL信息到Action的有效桥梁。

**技术框架**：VLA-Adapter的整体框架包括以下几个主要模块：1) 视觉编码器：用于提取视觉特征。2) 语言编码器：用于提取语言指令的特征。3) 策略模块：包含Bridge Attention机制，用于融合视觉和语言特征，并生成动作指令。该模块是VLA-Adapter的核心，负责将VL表示桥接到动作空间。整个流程是：输入视觉信息和语言指令，分别通过编码器提取特征，然后通过策略模块融合特征并生成动作。

**关键创新**：VLA-Adapter的关键创新在于Bridge Attention机制和轻量级策略模块的设计。Bridge Attention能够自适应地选择和融合最相关的视觉和语言特征，从而更有效地指导动作生成。与现有方法相比，VLA-Adapter不需要对整个VLM进行微调，而是通过一个轻量级的策略模块来实现VL到A的桥接，大大降低了计算成本。本质区别在于从依赖大规模预训练转变为高效的条件注入。

**关键设计**：Bridge Attention机制是关键设计之一，它通过学习注意力权重来确定哪些视觉和语言特征对动作生成最重要。策略模块采用轻量级网络结构，以减少计算量和参数量。损失函数的设计也至关重要，需要平衡动作的准确性和平滑性。具体的参数设置（如注意力头的数量、网络层数等）需要根据具体任务进行调整。论文中提到使用0.5B参数的骨干网络，并在单个消费级GPU上进行训练。

## 📊 实验亮点

VLA-Adapter在模拟和真实机器人基准测试中均取得了最先进的性能。该模型仅使用0.5B参数的骨干网络，无需任何机器人数据预训练。在推理速度方面，VLA-Adapter也达到了目前报道的最快水平。更重要的是，该模型可以在单个消费级GPU上仅用8小时完成训练，大大降低了VLA模型的训练门槛。

## 🎯 应用场景

VLA-Adapter在机器人控制、自动驾驶、智能家居等领域具有广泛的应用前景。它可以使机器人能够理解人类的指令，并根据视觉信息做出相应的动作。由于其训练成本低、推理速度快，VLA-Adapter有望加速VLA模型在实际场景中的部署和应用，实现更智能、更灵活的人机交互。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models typically bridge the gap between perceptual and action spaces by pre-training a large-scale Vision-Language Model (VLM) on robotic data. While this approach greatly enhances performance, it also incurs significant training costs. In this paper, we investigate how to effectively bridge vision-language (VL) representations to action (A). We introduce VLA-Adapter, a novel paradigm designed to reduce the reliance of VLA models on large-scale VLMs and extensive pre-training. To this end, we first systematically analyze the effectiveness of various VL conditions and present key findings on which conditions are essential for bridging perception and action spaces. Based on these insights, we propose a lightweight Policy module with Bridge Attention, which autonomously injects the optimal condition into the action space. In this way, our method achieves high performance using only a 0.5B-parameter backbone, without any robotic data pre-training. Extensive experiments on both simulated and real-world robotic benchmarks demonstrate that VLA-Adapter not only achieves state-of-the-art level performance, but also offers the fast inference speed reported to date. Furthermore, thanks to the proposed advanced bridging paradigm, VLA-Adapter enables the training of a powerful VLA model in just 8 hours on a single consumer-grade GPU, greatly lowering the barrier to deploying the VLA model. Project page: https://vla-adapter.github.io/.

