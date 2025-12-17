---
layout: default
title: MATRIX: Multimodal Agent Tuning for Robust Tool-Use Reasoning
---

# MATRIX: Multimodal Agent Tuning for Robust Tool-Use Reasoning

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.08567" target="_blank" class="toolbar-btn">arXiv: 2510.08567v3</a>
    <a href="https://arxiv.org/pdf/2510.08567.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.08567v3" 
            onclick="toggleFavorite(this, '2510.08567v3', 'MATRIX: Multimodal Agent Tuning for Robust Tool-Use Reasoning')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Tajamul Ashraf, Umair Nawaz, Abdelrahman M. Shaker, Rao Anwer, Philip Torr, Fahad Shahbaz Khan, Salman Khan

**分类**: cs.CV, cs.AI, cs.CL

**发布日期**: 2025-10-09 (更新: 2025-10-21)

**备注**: We have come across a recent approach that has not been properly attributed at the time of submission and compared in a fair setting. Therefore, we would like to withdraw the paper to address these concerns

**🔗 代码/项目**: [GITHUB](https://github.com/mbzuai-oryx/MATRIX)

---

## 💡 一句话要点

**提出MATRIX框架，通过多模态Agent调优实现稳健的工具使用推理**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `视觉语言模型` `工具使用` `强化学习` `模仿学习` `偏好学习` `Agent调优`

## 📋 核心要点

1. 现有VLM在工具使用推理方面受限于高质量多模态数据的稀缺以及高昂的人工标注成本。
2. 提出MATRIX框架，通过自动合成多模态轨迹和偏好对，实现VLM控制器的稳健工具使用推理。
3. 实验结果表明，MATRIX在多个基准测试中超越了现有开源和闭源VLM，证明了其有效性。

## 📝 摘要（中文）

视觉语言模型(VLMs)越来越多地被部署为控制器，用于访问外部工具以进行复杂的推理和决策，但其有效性仍然受到高质量多模态轨迹稀缺和手动标注成本的限制。本文提出了一种以视觉为中心Agent调优框架，该框架自动合成多模态轨迹，生成逐步偏好对，并训练VLM控制器以实现稳健的工具使用推理。该流程首先构建M-TRACE，一个包含28.5K多模态任务和177K验证轨迹的大规模数据集，从而实现基于模仿的轨迹调优。在此基础上，开发了MATRIX Agent，一个在M-TRACE上进行微调的控制器，用于逐步工具推理。为了实现更精细的对齐，进一步引入了Pref-X，一个包含11K自动生成的偏好对的集合，并通过逐步偏好学习对其进行优化。在Agent-X、GTA和GAIA三个基准测试中，MATRIX始终优于开源和闭源VLM，展示了可扩展且有效的多模态工具使用。

## 🔬 方法详解

**问题定义**：现有视觉语言模型在复杂推理和决策任务中，需要借助外部工具，但缺乏足够的高质量多模态数据来训练和优化这些模型，同时人工标注成本过高，限制了模型的性能提升。现有方法难以有效地利用有限的数据进行训练，导致工具使用推理能力不足。

**核心思路**：论文的核心思路是通过自动生成大规模的多模态轨迹数据和偏好对数据，来解决数据稀缺问题。通过模仿学习和偏好学习，对VLM控制器进行微调，从而提升其工具使用推理能力。这种方法避免了昂贵的人工标注，并能够有效地利用合成数据进行模型训练。

**技术框架**：MATRIX框架包含以下几个主要阶段：1) **M-TRACE数据集构建**：自动合成大规模多模态任务和验证轨迹。2) **Agent初始化**：在M-TRACE数据集上进行模仿学习，训练得到MATRIX Agent。3) **Pref-X数据集构建**：自动生成偏好对数据，用于偏好学习。4) **偏好学习**：利用Pref-X数据集对MATRIX Agent进行微调，进一步提升性能。

**关键创新**：论文的关键创新在于提出了一种自动生成多模态轨迹和偏好对数据的方法，从而解决了VLM在工具使用推理方面的数据稀缺问题。这种方法能够有效地利用合成数据进行模型训练，避免了昂贵的人工标注，并显著提升了模型的性能。

**关键设计**：M-TRACE数据集包含28.5K多模态任务和177K验证轨迹。Pref-X数据集包含11K自动生成的偏好对。MATRIX Agent基于VLM进行微调，采用模仿学习和偏好学习相结合的方式进行训练。损失函数包括模仿学习损失和偏好学习损失。具体VLM架构和超参数设置在论文中有详细描述（此处未知，根据论文补充）。

## 📊 实验亮点

实验结果表明，MATRIX在Agent-X、GTA和GAIA三个基准测试中均取得了显著的性能提升，超越了现有的开源和闭源VLM。具体来说，MATRIX在各项指标上均优于对比方法，证明了其在多模态工具使用推理方面的有效性和优越性。具体的性能提升幅度需要在论文中查找具体数据。

## 🎯 应用场景

该研究成果可应用于各种需要视觉语言模型进行复杂推理和决策的场景，例如机器人控制、智能助手、游戏AI等。通过提升VLM的工具使用推理能力，可以实现更智能、更自主的系统，从而提高生产效率和用户体验。未来，该方法可以扩展到更多模态和更复杂的任务中。

## 📄 摘要（原文）

> Vision language models (VLMs) are increasingly deployed as controllers with access to external tools for complex reasoning and decision-making, yet their effectiveness remains limited by the scarcity of high-quality multimodal trajectories and the cost of manual annotation. We address this challenge with a vision-centric agent tuning framework that automatically synthesizes multimodal trajectories, generates step-wise preference pairs, and trains a VLM controller for robust tool-use reasoning. Our pipeline first constructs M-TRACE, a large-scale dataset of 28.5K multimodal tasks with 177K verified trajectories, enabling imitation-based trajectory tuning. Building on this, we develop MATRIX Agent, a controller finetuned on M-TRACE for step-wise tool reasoning. To achieve finer alignment, we further introduce Pref-X, a set of 11K automatically generated preference pairs, and optimize MATRIX on it via step-wise preference learning. Across three benchmarks, Agent-X, GTA, and GAIA, MATRIX consistently surpasses both open- and closed-source VLMs, demonstrating scalable and effective multimodal tool use. Our data and code is avaliable at https://github.com/mbzuai-oryx/MATRIX.

