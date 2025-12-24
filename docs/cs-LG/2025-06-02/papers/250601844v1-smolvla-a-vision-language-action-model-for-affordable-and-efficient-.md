---
layout: default
title: "SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics"
---

# SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.01844" class="toolbar-btn" target="_blank">📄 arXiv: 2506.01844v1</a>
  <a href="https://arxiv.org/pdf/2506.01844.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.01844v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.01844v1', 'SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mustafa Shukor, Dana Aubakirova, Francesco Capuano, Pepijn Kooijmans, Steven Palma, Adil Zouitine, Michel Aractingi, Caroline Pascal, Martino Russi, Andres Marafioti, Simon Alibert, Matthieu Cord, Thomas Wolf, Remi Cadene

**分类**: cs.LG, cs.RO

**发布日期**: 2025-06-02

**备注**: 24 pages. Code and assets: https://github.com/huggingface/lerobot

---

## 💡 一句话要点

**提出SmolVLA以解决现有VLA模型的高成本问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `机器人技术` `多模态学习` `小型化模型` `异步推理` `自然语言处理` `社区驱动`

## 📋 核心要点

1. 现有的视觉语言行动模型通常参数庞大，导致高昂的训练和推理成本，限制了其在实际应用中的可行性。
2. SmolVLA通过设计为小型且高效的模型，能够在单个GPU上训练，并在消费级硬件上部署，从而降低成本。
3. 实验结果表明，SmolVLA在多个基准测试中表现出与10倍更大模型相当的性能，显示出其高效性和实用性。

## 📝 摘要（中文）

视觉语言模型（VLMs）在大规模多模态数据集上进行预训练，能够编码丰富的视觉和语言知识，为机器人技术提供了强大的基础。现有的视觉语言行动（VLA）模型通常参数庞大，导致高昂的训练成本和有限的实际应用能力。本文提出SmolVLA，一个小型、高效且以社区为驱动的VLA模型，显著降低了训练和推理成本，同时保持了竞争力的性能。SmolVLA设计为可在单个GPU上训练，并可在消费级GPU或CPU上部署。通过引入异步推理堆栈，SmolVLA提高了响应速度，允许更高的控制率和分块动作生成。尽管体积小，SmolVLA的性能与10倍更大模型相当，并在多个模拟和真实世界的机器人基准上进行了评估，所有代码、预训练模型和训练数据均已公开。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视觉语言行动模型（VLA）在训练和推理过程中面临的高成本问题。现有模型通常需要数十亿参数，导致训练资源消耗巨大，限制了其在实际机器人应用中的可行性。

**核心思路**：SmolVLA的核心思路是设计一个小型且高效的VLA模型，能够在单个GPU上进行训练，并在消费级硬件上实现部署，从而降低整体成本和提高可用性。通过异步推理堆栈的引入，SmolVLA能够将感知与动作预测解耦，提高响应速度。

**技术框架**：SmolVLA的整体架构包括多个模块：首先是视觉和语言的输入模块，然后是感知与动作预测模块，最后是动作执行模块。异步推理堆栈允许感知和动作预测在不同的时间段内进行，从而提高控制率。

**关键创新**：SmolVLA的主要创新在于其小型化设计和异步推理机制，使其在保持性能的同时显著降低了训练和推理成本。这与现有的庞大VLA模型形成鲜明对比。

**关键设计**：在模型设计中，SmolVLA采用了优化的网络结构和损失函数，以确保在小型化的同时不牺牲性能。此外，模型的训练过程经过精心调整，以适应单GPU环境，确保高效性。

## 📊 实验亮点

在多个模拟和真实世界的机器人基准测试中，SmolVLA的性能与参数量为10倍的现有VLA模型相当，显示出其在小型化和高效性方面的显著优势。实验结果表明，SmolVLA在训练和推理成本上大幅降低，且能够实现更高的控制率，提升了机器人任务的响应速度。

## 🎯 应用场景

SmolVLA的潜在应用领域包括家庭服务机器人、教育机器人以及工业自动化等场景。其高效性和低成本特性使得中小型企业和个人开发者能够更容易地实现自然语言驱动的机器人控制，推动机器人技术的普及与应用。未来，SmolVLA可能会在更多的机器人任务中得到应用，促进人机交互的自然化。

## 📄 摘要（原文）

> Vision-language models (VLMs) pretrained on large-scale multimodal datasets encode rich visual and linguistic knowledge, making them a strong foundation for robotics. Rather than training robotic policies from scratch, recent approaches adapt VLMs into vision-language-action (VLA) models that enable natural language-driven perception and control. However, existing VLAs are typically massive--often with billions of parameters--leading to high training costs and limited real-world deployability. Moreover, they rely on academic and industrial datasets, overlooking the growing availability of community-collected data from affordable robotic platforms. In this work, we present SmolVLA, a small, efficient, and community-driven VLA that drastically reduces both training and inference costs, while retaining competitive performance. SmolVLA is designed to be trained on a single GPU and deployed on consumer-grade GPUs or even CPUs. To further improve responsiveness, we introduce an asynchronous inference stack decoupling perception and action prediction from action execution, allowing higher control rates with chunked action generation. Despite its compact size, SmolVLA achieves performance comparable to VLAs that are 10x larger. We evaluate SmolVLA on a range of both simulated as well as real-world robotic benchmarks and release all code, pretrained models, and training data.

