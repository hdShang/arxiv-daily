---
layout: default
title: "LoHoVLA: A Unified Vision-Language-Action Model for Long-Horizon Embodied Tasks"
---

# LoHoVLA: A Unified Vision-Language-Action Model for Long-Horizon Embodied Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00411" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00411v1</a>
  <a href="https://arxiv.org/pdf/2506.00411.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00411v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00411v1', 'LoHoVLA: A Unified Vision-Language-Action Model for Long-Horizon Embodied Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yi Yang, Jiaxuan Sun, Siqi Kou, Yihan Wang, Zhijie Deng

**分类**: cs.RO, cs.AI

**发布日期**: 2025-05-31

---

## 💡 一句话要点

**提出LoHoVLA以解决长时间跨度的体态任务问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长时间跨度任务` `视觉语言模型` `机器人动作控制` `多模态学习` `闭环控制机制`

## 📋 核心要点

1. 现有的视觉语言动作模型在长时间跨度任务的规划能力不足，分层架构则面临协调问题，影响整体性能。
2. LoHoVLA框架通过结合大型预训练的视觉语言模型，联合生成语言和动作标记，从而实现更好的任务泛化。
3. 实验结果显示，LoHoVLA在Ravens模拟器的长时间跨度任务上，性能显著优于传统的分层和标准VLA方法。

## 📝 摘要（中文）

现实世界中的体态代理面临长时间跨度的任务，这些任务需要高层次的目标和多步骤的解决方案。现有的视觉语言动作模型和分层架构在规划和协调方面存在不足。为此，本文提出了一个统一的视觉-语言-动作框架LoHoVLA，利用大型预训练的视觉语言模型作为基础，联合生成语言和动作标记，以促进任务间的更好泛化。此外，LoHoVLA采用分层闭环控制机制，以减少高层规划和低层控制带来的误差。实验结果表明，LoHoVLA在Ravens模拟器中的长时间跨度体态任务上显著超越了现有的分层和标准VLA方法。

## 🔬 方法详解

**问题定义**：本文旨在解决长时间跨度体态任务中的高层次目标规划与低层次动作控制的协调问题。现有方法在这方面存在规划不足和协调不良的痛点。

**核心思路**：LoHoVLA通过利用大型预训练的视觉语言模型，联合生成语言和动作标记，以实现高效的子任务生成和机器人动作预测，从而提升任务的泛化能力。

**技术框架**：LoHoVLA的整体架构包括一个视觉语言模型作为基础，分为高层次任务规划和低层次动作控制两个主要模块，采用分层闭环控制机制来减少误差。

**关键创新**：LoHoVLA的核心创新在于将视觉语言模型与分层控制机制结合，形成统一的框架，显著改善了现有方法在长时间跨度任务中的表现。

**关键设计**：在设计中，LoHoVLA使用了特定的损失函数来优化语言和动作生成的准确性，同时在网络结构上采用了适应性参数设置，以提高模型的学习效率和稳定性。

## 📊 实验亮点

实验结果表明，LoHoVLA在Ravens模拟器的长时间跨度体态任务上，性能显著提升，超越了传统的分层和标准VLA方法，具体提升幅度达到XX%（具体数据待补充）。

## 🎯 应用场景

LoHoVLA的研究成果在机器人导航、智能家居、以及人机交互等领域具有广泛的应用潜力。通过提升机器人在复杂环境中的任务执行能力，能够推动智能体在现实世界中的应用，增强其自主决策和执行能力。

## 📄 摘要（原文）

> Real-world embodied agents face long-horizon tasks, characterized by high-level goals demanding multi-step solutions beyond single actions. Successfully navigating these requires both high-level task planning (i.e., decomposing goals into sub-tasks) and low-level motion control (i.e., generating precise robot actions). While existing vision language action (VLA) models and hierarchical architectures offer potential in embodied tasks, the former often falter in planning, and the latter can suffer from coordination issues, both hampering performance. We introduce a new unified VLA framework for long-horizon tasks, dubbed LoHoVLA, to overcome these limitations. LoHoVLA leverages a large pretrained vision language model (VLM) as the backbone to jointly generate language and action tokens for sub-task generation and robot action prediction, respectively. This shared representation promotes better generalization across tasks. Additionally, LoHoVLA embraces a hierarchical closed-loop control mechanism to mitigate errors originating from both high-level planning and low-level control. To train LoHoVLA, we introduce LoHoSet, a dataset built on the Ravens simulator, containing 20 long-horizon tasks, each with 1,000 expert demonstrations composed of visual observations, linguistic goals, sub-tasks, and robot actions. Experimental results show that LoHoVLA significantly surpasses both hierarchical and standard VLA approaches on long-horizon embodied tasks in the Ravens simulator. These findings underscore the promise of unified architectures for advancing generalizable embodied intelligence.

