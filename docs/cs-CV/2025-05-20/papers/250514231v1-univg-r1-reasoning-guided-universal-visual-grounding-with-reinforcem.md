---
layout: default
title: "UniVG-R1: Reasoning Guided Universal Visual Grounding with Reinforcement Learning"
---

# UniVG-R1: Reasoning Guided Universal Visual Grounding with Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14231" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14231v1</a>
  <a href="https://arxiv.org/pdf/2505.14231.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14231v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14231v1', 'UniVG-R1: Reasoning Guided Universal Visual Grounding with Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sule Bai, Mingxing Li, Yong Liu, Jing Tang, Haoji Zhang, Lei Sun, Xiangxiang Chu, Yansong Tang

**分类**: cs.CV

**发布日期**: 2025-05-20

**🔗 代码/项目**: [PROJECT_PAGE](https://amap-ml.github.io/UniVG-R1-page/)

---

## 💡 一句话要点

**提出UniVG-R1以解决复杂多模态视觉定位问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态视觉定位` `推理引导` `强化学习` `思维链数据集` `零样本学习`

## 📋 核心要点

1. 现有视觉定位方法主要针对单一图像和简单文本，难以应对复杂的多模态指令和多图像场景。
2. 本文提出UniVG-R1，通过推理引导的多模态大语言模型和强化学习，提升模型的推理能力。
3. 实验结果显示，UniVG-R1在MIG-Bench上实现了9.1%的性能提升，并在多个基准上展现出强大的零样本泛化能力。

## 📝 摘要（中文）

传统的视觉定位方法主要集中在单图像场景和简单文本引用上。然而，将这些方法扩展到涉及隐含和复杂指令的真实场景，尤其是多图像的情况下，面临着重大挑战，主要是由于缺乏在多模态上下文中进行高级推理的能力。本文提出了UniVG-R1，这是一种基于推理引导的多模态大语言模型（MLLM），通过结合冷启动数据的强化学习（RL）来增强推理能力。我们首先构建了一个高质量的思维链（CoT）定位数据集，并通过监督微调引导模型走向正确的推理路径。随后，我们采用基于规则的强化学习来鼓励模型识别正确的推理链，从而激励其推理能力。实验结果表明，UniVG-R1在MIG-Bench上实现了9.1%的性能提升，并在四个图像和视频推理定位基准上实现了23.4%的零样本性能提升。

## 🔬 方法详解

**问题定义**：本文旨在解决复杂多模态视觉定位任务中推理能力不足的问题。现有方法在处理多图像和隐含指令时表现不佳，缺乏有效的推理机制。

**核心思路**：UniVG-R1通过构建高质量的思维链数据集，并结合强化学习来引导模型学习正确的推理路径，从而提升其在复杂场景下的表现。

**技术框架**：该方法包括数据集构建、监督微调和基于规则的强化学习三个主要阶段。首先，构建思维链数据集以指导模型学习；然后，通过微调增强模型的初步推理能力；最后，利用强化学习进一步优化推理链的选择。

**关键创新**：最重要的创新在于引入了推理引导的强化学习机制，并提出了难度感知的权重调整策略，以应对训练过程中样本难度偏差的问题。这一设计使得模型在复杂任务中表现更为出色。

**关键设计**：在模型训练中，采用了特定的损失函数来平衡推理链的选择，并设置了适当的超参数以优化学习过程。此外，难度感知权重调整策略的引入，确保了模型在不同难度样本上的学习效果。

## 📊 实验亮点

实验结果表明，UniVG-R1在MIG-Bench上实现了9.1%的性能提升，展现出强大的零样本泛化能力，在四个图像和视频推理定位基准上平均提升23.4%。这些结果表明该模型在复杂多模态视觉定位任务中的有效性和优越性。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、自动驾驶、机器人导航等需要理解复杂指令和多模态信息的场景。通过提升视觉定位的准确性和推理能力，UniVG-R1可以在实际应用中显著提高系统的智能水平和用户体验。未来，该技术可能推动更广泛的多模态交互和智能决策系统的发展。

## 📄 摘要（原文）

> Traditional visual grounding methods primarily focus on single-image scenarios with simple textual references. However, extending these methods to real-world scenarios that involve implicit and complex instructions, particularly in conjunction with multiple images, poses significant challenges, which is mainly due to the lack of advanced reasoning ability across diverse multi-modal contexts. In this work, we aim to address the more practical universal grounding task, and propose UniVG-R1, a reasoning guided multimodal large language model (MLLM) for universal visual grounding, which enhances reasoning capabilities through reinforcement learning (RL) combined with cold-start data. Specifically, we first construct a high-quality Chain-of-Thought (CoT) grounding dataset, annotated with detailed reasoning chains, to guide the model towards correct reasoning paths via supervised fine-tuning. Subsequently, we perform rule-based reinforcement learning to encourage the model to identify correct reasoning chains, thereby incentivizing its reasoning capabilities. In addition, we identify a difficulty bias arising from the prevalence of easy samples as RL training progresses, and we propose a difficulty-aware weight adjustment strategy to further strengthen the performance. Experimental results demonstrate the effectiveness of UniVG-R1, which achieves state-of-the-art performance on MIG-Bench with a 9.1% improvement over the previous method. Furthermore, our model exhibits strong generalizability, achieving an average improvement of 23.4% in zero-shot performance across four image and video reasoning grounding benchmarks. The project page can be accessed at https://amap-ml.github.io/UniVG-R1-page/.

