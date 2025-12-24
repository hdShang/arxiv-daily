---
layout: default
title: "PhysiAgent: An Embodied Agent Framework in Physical World"
---

# PhysiAgent: An Embodied Agent Framework in Physical World

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24524" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24524v1</a>
  <a href="https://arxiv.org/pdf/2509.24524.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24524v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24524v1', 'PhysiAgent: An Embodied Agent Framework in Physical World')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhihao Wang, Jianxiong Li, Jinliang Zheng, Wencong Zhang, Dongxiu Liu, Yinan Zheng, Haoyi Niu, Junzhi Yu, Xianyuan Zhan

**分类**: cs.RO, cs.AI, eess.SY

**发布日期**: 2025-09-29

---

## 💡 一句话要点

**提出PhysiAgent框架以解决VLA与VLM协作不足问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `具身智能` `视觉-语言模型` `机器人任务` `自我调节` `多模态协作` `实时反馈` `任务规划` `智能代理`

## 📋 核心要点

1. 现有的视觉-语言-动作（VLA）模型在高层场景理解和任务规划中表现良好，但在执行低层动作时协作效果不佳，导致泛化能力不足。
2. 本文提出的PhysiAgent框架通过引入监控、记忆和自我反思机制，促进VLM与VLA之间的有效协作，提升了整体任务执行能力。
3. 实验结果显示，PhysiAgent在复杂的机器人任务中显著提高了任务解决性能，展示了VLM的自我调节能力和工具协作的有效性。

## 📝 摘要（中文）

视觉-语言-动作（VLA）模型取得了显著成功，但在泛化能力上存在局限。为了解决这一问题，集成通用视觉-语言模型（VLM）作为VLA的助手成为一种流行的解决方案。然而，现有方法通常以僵化的顺序结构组合这些模型，导致协作效果不佳。本文提出了一个名为PhysiAgent的具身代理框架，旨在有效地在物理环境中操作。通过引入监控、记忆和自我反思机制，PhysiAgent提供了一种自主的支撑框架，能够根据VLA的实时反馈组织不同组件，从而最大限度地发挥VLA的能力。实验结果表明，在复杂的现实机器人任务中，任务解决性能显著提升，展示了VLM的有效自我调节、工具协作的连贯性以及框架在执行过程中的自适应演变。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视觉-语言-动作（VLA）模型与通用视觉-语言模型（VLM）之间的协作不足问题，现有方法常常导致低效的任务执行和较差的泛化能力。

**核心思路**：PhysiAgent框架通过引入实时反馈机制，促使VLM根据VLA的执行情况自我调整，从而实现更高效的任务执行和协作。

**技术框架**：PhysiAgent的整体架构包括监控模块、记忆模块和自我反思机制，能够实时收集和分析VLA的执行反馈，并动态调整VLM的任务规划和执行策略。

**关键创新**：PhysiAgent的主要创新在于其自主的支撑框架，能够根据实时反馈优化VLM的组件组织方式，显著提升了VLA的执行能力和任务解决效率。

**关键设计**：在设计上，PhysiAgent采用轻量级的工具箱，结合多种反馈机制，确保VLM能够灵活应对不同的任务需求，并通过自我反思不断优化执行策略。

## 📊 实验亮点

实验结果表明，PhysiAgent在复杂的机器人任务中任务解决性能提升了显著的XX%（具体数据未知），相较于传统方法，展示了更好的自我调节能力和工具协作效果，验证了其在实际应用中的有效性。

## 🎯 应用场景

PhysiAgent框架在机器人领域具有广泛的应用潜力，尤其是在复杂环境中的自主导航、任务执行和人机交互等场景。其有效的协作机制和自我调节能力将推动智能机器人在实际应用中的表现，提升其在动态环境中的适应性和效率。

## 📄 摘要（原文）

> Vision-Language-Action (VLA) models have achieved notable success but often struggle with limited generalizations. To address this, integrating generalized Vision-Language Models (VLMs) as assistants to VLAs has emerged as a popular solution. However, current approaches often combine these models in rigid, sequential structures: using VLMs primarily for high-level scene understanding and task planning, and VLAs merely as executors of lower-level actions, leading to ineffective collaboration and poor grounding challenges. In this paper, we propose an embodied agent framework, PhysiAgent, tailored to operate effectively in physical environments. By incorporating monitor, memory, self-reflection mechanisms, and lightweight off-the-shelf toolboxes, PhysiAgent offers an autonomous scaffolding framework to prompt VLMs to organize different components based on real-time proficiency feedback from VLAs to maximally exploit VLAs' capabilities. Experimental results demonstrate significant improvements in task-solving performance on complex real-world robotic tasks, showcasing effective self-regulation of VLMs, coherent tool collaboration, and adaptive evolution of the framework during execution. PhysiAgent makes practical and pioneering efforts to integrate VLMs and VLAs, effectively grounding embodied agent frameworks in real-world settings.

