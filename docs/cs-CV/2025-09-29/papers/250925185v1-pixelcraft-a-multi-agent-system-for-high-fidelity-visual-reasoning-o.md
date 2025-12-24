---
layout: default
title: "PixelCraft: A Multi-Agent System for High-Fidelity Visual Reasoning on Structured Images"
---

# PixelCraft: A Multi-Agent System for High-Fidelity Visual Reasoning on Structured Images

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25185" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25185v1</a>
  <a href="https://arxiv.org/pdf/2509.25185.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25185v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25185v1', 'PixelCraft: A Multi-Agent System for High-Fidelity Visual Reasoning on Structured Images')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shuoshuo Zhang, Zijian Li, Yizhen Zhang, Jingjing Fu, Lei Song, Jiang Bian, Jun Zhang, Yujiu Yang, Rui Wang

**分类**: cs.CV

**发布日期**: 2025-09-29

**🔗 代码/项目**: [GITHUB](https://github.com/microsoft/PixelCraft)

---

## 💡 一句话要点

**PixelCraft：用于结构化图像高保真视觉推理的多智能体系统**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多智能体系统` `视觉推理` `结构化图像` `多模态学习` `图表理解`

## 📋 核心要点

1. 多模态大语言模型在处理结构化图像时，容易出现感知错误，导致错误的结论，现有基于视觉线索的方法效果有限。
2. PixelCraft 提出了一种多智能体系统，通过高保真图像处理和灵活的视觉推理，提升模型在结构化图像上的理解能力。
3. 实验表明，PixelCraft 显著提高了视觉推理性能，并在图表和几何基准测试中为高级 MLLM 设定了新的标准。

## 📝 摘要（中文）

针对多模态大语言模型（MLLM）在结构化图像（如图表和几何图形）上表现不佳的问题，本文提出了PixelCraft，一种新型多智能体系统，旨在实现高保真图像处理和灵活的视觉推理。该系统包含调度器、规划器、推理器、评论器以及一组视觉工具智能体。为实现高保真处理，构建了高质量语料库并对MLLM进行微调，使其成为 grounding 模型，其像素级定位与传统计算机视觉（CV）算法集成在工具智能体中。在此基础上，PixelCraft 通过工具选择、智能体讨论和自我批评的动态三阶段工作流程，促进灵活的视觉推理。此外，与简单附加历史图像的线性推理模式不同，PixelCraft 维护图像记忆，使规划器能够自适应地回顾早期的视觉步骤，探索替代推理分支，并在讨论期间动态调整推理轨迹。在具有挑战性的图表和几何基准上的大量实验表明，PixelCraft 显著提高了高级 MLLM 的视觉推理性能，为结构化图像推理设定了新标准。

## 🔬 方法详解

**问题定义**：现有的多模态大语言模型在处理结构化图像（如图表、几何图形）时，容易出现感知上的偏差，进而导致推理错误。现有的基于视觉线索的方法，由于图像处理的保真度不高，以及推理模式的线性与僵化，限制了其在复杂结构化图像任务上的有效性。

**核心思路**：PixelCraft 的核心思路是构建一个多智能体系统，每个智能体负责不同的视觉处理和推理任务，通过智能体之间的协作和讨论，实现高保真图像处理和灵活的视觉推理。通过像素级别的定位信息和传统计算机视觉算法的结合，提升图像处理的精度。

**技术框架**：PixelCraft 系统包含五个主要模块：调度器（Dispatcher）、规划器（Planner）、推理器（Reasoner）、评论器（Critics）和一组视觉工具智能体。调度器负责任务分配，规划器负责制定推理计划，推理器执行推理步骤，评论器评估推理结果，工具智能体执行具体的视觉处理任务。整个流程包含工具选择、智能体讨论和自我批评三个阶段。系统维护一个图像记忆，允许规划器回顾之前的步骤，探索不同的推理分支。

**关键创新**：PixelCraft 的关键创新在于其多智能体架构和动态推理流程。与传统的线性推理模式不同，PixelCraft 允许智能体之间进行讨论和协作，并能够根据讨论结果动态调整推理轨迹。此外，通过高质量语料库的训练，提升了 grounding 模型的像素级定位精度，实现了高保真图像处理。

**关键设计**：PixelCraft 通过构建高质量的语料库，并对 MLLM 进行微调，得到 grounding 模型。该模型能够进行像素级别的定位，为工具智能体提供精确的视觉信息。在推理过程中，规划器会根据当前状态和历史信息，动态选择合适的工具智能体，并调整推理步骤。评论器会对推理结果进行评估，并提供反馈，指导推理过程的改进。

## 📊 实验亮点

PixelCraft 在图表和几何基准测试中取得了显著的性能提升，超越了现有的方法。实验结果表明，PixelCraft 能够更准确地理解结构化图像，并进行更有效的视觉推理。具体性能数据和对比基线信息需要在论文原文中查找。

## 🎯 应用场景

PixelCraft 的潜在应用领域包括：自动化图表分析、智能几何问题求解、医学图像诊断、工业质检等。该研究的实际价值在于提升了多模态大语言模型在结构化图像理解方面的能力，为更智能的人机交互和决策支持提供了可能。未来，该技术有望应用于更广泛的视觉推理任务，并促进人工智能在各个领域的应用。

## 📄 摘要（原文）

> Structured images (e.g., charts and geometric diagrams) remain challenging for multimodal large language models (MLLMs), as perceptual slips can cascade into erroneous conclusions. Intermediate visual cues can steer reasoning; however, existing cue-based methods are constrained with low-fidelity image processing and linear, rigid reasoning patterns, limiting their effectiveness on complex structured-image tasks. In this paper, we propose PixelCraft, a novel multi-agent system for high-fidelity image processing and flexible visual reasoning on structured images. The system comprises a dispatcher, a planner, a reasoner, critics, and a set of visual tool agents. To achieve high-fidelity processing, we construct a high-quality corpus and fine-tune an MLLM into a grounding model, whose pixel-level localizations are integrated with traditional computer vision (CV) algorithms in tool agents. Building on this foundation, PixelCraft facilitates flexible visual reasoning through a dynamic three-stage workflow of tool selection, agent discussion, and self-criticism. Moreover, unlike prior linear reasoning patterns that simply append historical images, PixelCraft maintains an image memory to allow the planner to adaptively revisit earlier visual steps, explore alternative reasoning branches, and dynamically adjust the reasoning trajectory during discussion. Extensive experiments on challenging chart and geometry benchmarks demonstrate that PixelCraft significantly improves visual reasoning performance for advanced MLLMs, setting a new standard for structured image reasoning. Our code will be available at https://github.com/microsoft/PixelCraft.

