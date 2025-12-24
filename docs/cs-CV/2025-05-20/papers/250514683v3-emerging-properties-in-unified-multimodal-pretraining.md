---
layout: default
title: Emerging Properties in Unified Multimodal Pretraining
---

# Emerging Properties in Unified Multimodal Pretraining

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14683" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14683v3</a>
  <a href="https://arxiv.org/pdf/2505.14683.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14683v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14683v3', 'Emerging Properties in Unified Multimodal Pretraining')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chaorui Deng, Deyao Zhu, Kunchang Li, Chenhui Gou, Feng Li, Zeyu Wang, Shu Zhong, Weihao Yu, Xiaonan Nie, Ziang Song, Guang Shi, Haoqi Fan

**分类**: cs.CV

**发布日期**: 2025-05-20 (更新: 2025-07-27)

**备注**: 37 pages, 17 figures

---

## 💡 一句话要点

**提出BAGEL模型以解决多模态理解与生成的挑战**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态理解` `多模态生成` `预训练模型` `复杂推理` `开源模型` `图像操作` `视频预测`

## 📋 核心要点

1. 现有多模态模型在理解和生成能力上存在不足，难以处理复杂的多模态推理任务。
2. BAGEL模型通过统一的解码器架构，利用大规模交错数据进行预训练，支持多模态理解与生成。
3. 实验结果表明，BAGEL在多模态生成和理解任务上显著优于现有开源模型，展现出先进的推理能力。

## 📝 摘要（中文）

本研究介绍了BAGEL，一个开源的基础模型，原生支持多模态理解与生成。BAGEL是一个统一的解码器模型，预训练于来自大规模交错文本、图像、视频和网络数据的数万亿个标记。通过这种多样化的数据，BAGEL展现出在复杂多模态推理方面的新兴能力，显著超越了现有的开源统一模型，在标准基准测试中表现出色，具备自由形式图像操作、未来帧预测、3D操作和世界导航等高级多模态推理能力。为促进多模态研究的发展，研究团队分享了关键发现、预训练细节、数据创建协议，并向社区发布了代码和检查点。

## 🔬 方法详解

**问题定义**：本研究旨在解决现有多模态模型在理解与生成能力上的不足，尤其是在复杂推理任务中的表现不佳。现有方法往往无法有效整合多种模态的信息，导致性能受限。

**核心思路**：BAGEL模型采用统一的解码器架构，能够同时处理多模态数据，通过预训练于大规模交错数据集，提升模型的多模态理解与生成能力。这样的设计使得模型能够在多种任务中展现出更强的适应性和灵活性。

**技术框架**：BAGEL的整体架构为解码器模型，主要模块包括数据预处理、模型训练和推理阶段。模型通过大规模的文本、图像、视频等数据进行预训练，确保其在多模态任务中的表现。

**关键创新**：BAGEL的主要创新在于其统一的解码器设计和大规模交错数据的使用，这与传统的多模态模型在架构和数据处理上存在本质区别，后者通常采用分开处理不同模态的方法。

**关键设计**：在模型设计中，BAGEL采用了特定的损失函数来优化多模态任务的表现，并在网络结构上进行了优化，以适应不同模态的数据特性。

## 📊 实验亮点

在标准基准测试中，BAGEL模型在多模态生成和理解任务上显著超越了现有开源统一模型，展现出更高的性能。具体而言，BAGEL在复杂推理任务中表现出色，具备自由形式图像操作和未来帧预测等能力，提升幅度达到XX%。

## 🎯 应用场景

BAGEL模型的潜在应用场景包括智能助手、自动内容生成、虚拟现实和增强现实等领域。其强大的多模态理解与生成能力可以为用户提供更自然的交互体验，推动相关技术的进步与应用。

## 📄 摘要（原文）

> Unifying multimodal understanding and generation has shown impressive capabilities in cutting-edge proprietary systems. In this work, we introduce BAGEL, an open-source foundational model that natively supports multimodal understanding and generation. BAGEL is a unified, decoder-only model pretrained on trillions of tokens curated from large-scale interleaved text, image, video, and web data. When scaled with such diverse multimodal interleaved data, BAGEL exhibits emerging capabilities in complex multimodal reasoning. As a result, it significantly outperforms open-source unified models in both multimodal generation and understanding across standard benchmarks, while exhibiting advanced multimodal reasoning abilities such as free-form image manipulation, future frame prediction, 3D manipulation, and world navigation. In the hope of facilitating further opportunities for multimodal research, we share the key findings, pretraining details, data creation protocal, and release our code and checkpoints to the community. The project page is at https://bagel-ai.org/

