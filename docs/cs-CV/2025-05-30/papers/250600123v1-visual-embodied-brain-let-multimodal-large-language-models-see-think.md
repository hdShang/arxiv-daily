---
layout: default
title: "Visual Embodied Brain: Let Multimodal Large Language Models See, Think, and Control in Spaces"
---

# Visual Embodied Brain: Let Multimodal Large Language Models See, Think, and Control in Spaces

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00123" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00123v1</a>
  <a href="https://arxiv.org/pdf/2506.00123.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00123v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00123v1', 'Visual Embodied Brain: Let Multimodal Large Language Models See, Think, and Control in Spaces')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gen Luo, Ganlin Yang, Ziyang Gong, Guanzhou Chen, Haonan Duan, Erfei Cui, Ronglei Tong, Zhi Hou, Tianyi Zhang, Zhe Chen, Shenglong Ye, Lewei Lu, Jingbo Wang, Wenhai Wang, Jifeng Dai, Yu Qiao, Rongrong Ji, Xizhou Zhu

**分类**: cs.CV, cs.RO

**发布日期**: 2025-05-30

---

## 💡 一句话要点

**提出VeBrain框架以解决多模态大语言模型在机器人控制中的整合问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `机器人控制` `视觉空间推理` `数据集构建` `智能决策` `人机交互` `适应性学习`

## 📋 核心要点

1. 现有方法难以将多模态理解、视觉空间推理和物理交互能力统一，限制了其在机器人控制中的应用。
2. 本文提出的VeBrain框架通过将机器人控制转化为文本任务，统一了不同任务的目标和映射空间，提升了多模态能力的整合。
3. 在13个多模态基准和5个空间智能基准上，VeBrain相较于现有模型Qwen2.5-VL表现出显著提升，尤其在四足机器人任务中提升幅度达50%。

## 📝 摘要（中文）

多模态大语言模型（MLLMs）的显著进展引起了将其扩展到物理实体（如四足机器人）的关注。这通常要求MLLMs不仅具备多模态理解能力，还需整合视觉空间推理和物理交互能力。然而，现有方法因其基本差异而难以统一这些能力。本文提出了视觉具身大脑（VeBrain），这是一个用于现实世界感知、推理和控制的统一框架。VeBrain将机器人控制重新表述为基于文本的MLLM任务，从而统一了不同任务的目标和映射空间。此外，提出了一种新型机器人适配器，将MLLM的文本控制信号转换为真实机器人的运动策略。通过VeBrain-600k数据集的构建，展示了VeBrain在多模态基准和空间智能基准上的优越性能。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多模态大语言模型在机器人控制中的能力整合问题，现有方法因能力差异而难以统一，限制了其应用效果。

**核心思路**：VeBrain框架通过将机器人控制任务重新表述为文本任务，利用MLLM的强大语言理解能力，统一了多种任务的目标和映射空间，从而实现更高效的控制和推理。

**技术框架**：VeBrain的整体架构包括感知模块、推理模块和控制模块。感知模块负责获取环境信息，推理模块进行决策分析，控制模块则将决策转化为具体的机器人动作。

**关键创新**：VeBrain的主要创新在于提出了一种新的机器人适配器，将文本控制信号有效转换为机器人的运动策略，解决了多模态任务之间的整合问题。

**关键设计**：在数据处理上，VeBrain-600k数据集经过数百小时的收集和注释，采用多模态链式思维（CoT）方法，将不同能力整合为单一对话，提升了模型的学习效果。

## 📊 实验亮点

在实验中，VeBrain在13个多模态基准和5个空间智能基准上表现优异，相较于Qwen2.5-VL在MMVet基准上提升了5.6%，在四足机器人任务中实现了50%的平均提升，展示了其强大的适应性和灵活性。

## 🎯 应用场景

VeBrain框架具有广泛的应用潜力，尤其在智能机器人、自动化控制和人机交互等领域。其高效的多模态理解和控制能力将推动机器人在复杂环境中的自主决策和操作，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> The remarkable progress of Multimodal Large Language Models (MLLMs) has attracted increasing attention to extend them to physical entities like legged robot. This typically requires MLLMs to not only grasp multimodal understanding abilities, but also integrate visual-spatial reasoning and physical interaction capabilities. Nevertheless,existing methods struggle to unify these capabilities due to their fundamental differences.In this paper, we present the Visual Embodied Brain (VeBrain), a unified framework for perception, reasoning, and control in real world. VeBrain reformulates robotic control into common text-based MLLM tasks in the 2D visual space, thus unifying the objectives and mapping spaces of different tasks. Then, a novel robotic adapter is proposed to convert textual control signals from MLLMs to motion policies of real robots. From the data perspective, we further introduce VeBrain-600k, a high-quality instruction dataset encompassing various capabilities of VeBrain. In VeBrain-600k, we take hundreds of hours to collect, curate and annotate the data, and adopt multimodal chain-of-thought(CoT) to mix the different capabilities into a single conversation. Extensive experiments on 13 multimodal benchmarks and 5 spatial intelligence benchmarks demonstrate the superior performance of VeBrain to existing MLLMs like Qwen2.5-VL. When deployed to legged robots and robotic arms, VeBrain shows strong adaptability, flexibility, and compositional capabilities compared to existing methods. For example, compared to Qwen2.5-VL, VeBrain not only achieves substantial gains on MMVet by +5.6%, but also excels in legged robot tasks with +50% average gains.

