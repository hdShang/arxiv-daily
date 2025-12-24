---
layout: default
title: "CoSPlan: Corrective Sequential Planning via Scene Graph Incremental Updates"
---

# CoSPlan: Corrective Sequential Planning via Scene Graph Incremental Updates

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.10342" class="toolbar-btn" target="_blank">📄 arXiv: 2512.10342v1</a>
  <a href="https://arxiv.org/pdf/2512.10342.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.10342v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.10342v1', 'CoSPlan: Corrective Sequential Planning via Scene Graph Incremental Updates')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shresth Grover, Priyank Pathak, Akash Kumar, Vibhav Vineet, Yogesh S Rawat

**分类**: cs.CV

**发布日期**: 2025-12-11

---

## 💡 一句话要点

**提出基于场景图增量更新的纠错序列规划方法CoSPlan，提升VLM在复杂任务中的推理能力。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `视觉语言模型` `序列规划` `场景图` `增量更新` `错误纠正` `机器人导航` `人工智能`

## 📋 核心要点

1. 现有视觉-语言模型在复杂序列规划任务中，难以有效检测和纠正错误步骤，导致性能瓶颈。
2. 论文提出场景图增量更新(SGI)方法，通过引入中间推理步骤，增强模型对序列的理解和推理能力。
3. 实验表明，SGI方法在CoSPlan基准测试中显著提升了VLMs的性能，并能泛化到其他规划任务。

## 📝 摘要（中文）

大规模视觉-语言模型(VLMs)在复杂推理方面表现出色，但在视觉序列规划（即执行多步骤动作以达到目标）方面的探索不足。实际序列规划常包含非最优步骤，对VLMs的检测和纠正能力提出挑战。我们提出了纠错序列规划基准(CoSPlan)，用于评估VLMs在易出错的、基于视觉的序列规划任务中的表现，涵盖迷宫导航、方块重排、图像重建和物体重组四个领域。CoSPlan评估两个关键能力：错误检测（识别非最优动作）和步骤完成（纠正并完成动作序列以达到目标）。即使采用思维链和场景图等先进推理技术，VLMs（如Intern-VLM和Qwen2）在CoSPlan上表现不佳，未能利用上下文线索达到目标。为此，我们提出了一种无需训练的方法，即场景图增量更新(SGI)，它在初始状态和目标状态之间引入中间推理步骤。SGI帮助VLMs进行序列推理，平均性能提升5.2%。除了提高纠错序列规划的可靠性外，SGI还推广到Plan-Bench和VQA等传统规划任务。

## 🔬 方法详解

**问题定义**：论文旨在解决视觉序列规划中，视觉-语言模型难以检测和纠正错误动作的问题。现有方法在处理包含错误步骤的序列规划任务时，往往无法有效利用上下文信息进行推理，导致规划失败。这限制了VLMs在实际场景中的应用。

**核心思路**：论文的核心思路是通过在初始状态和目标状态之间引入中间推理步骤，逐步更新场景图，从而帮助VLMs更好地理解序列规划任务。这种增量更新的方式使得模型能够更有效地利用上下文信息，检测并纠正错误动作。

**技术框架**：整体框架包括以下几个主要步骤：1) 输入初始状态和目标状态的视觉信息；2) 构建初始场景图；3) 通过VLMs生成中间动作和状态；4) 根据生成的动作更新场景图；5) 重复步骤3和4，直到达到目标状态。该框架通过迭代的方式，逐步完成序列规划任务。

**关键创新**：最重要的技术创新点是场景图增量更新(SGI)方法。与传统的端到端规划方法不同，SGI通过引入中间推理步骤，将复杂的序列规划任务分解为多个简单的子任务，从而降低了模型的推理难度。此外，SGI方法无需额外的训练，可以直接应用于现有的VLMs。

**关键设计**：SGI方法的关键设计在于如何有效地更新场景图。论文采用了一种基于规则的更新策略，根据生成的动作修改场景图中对象之间的关系。例如，如果模型预测将一个方块从A位置移动到B位置，则场景图中A位置的方块对象将被删除，B位置将添加一个新的方块对象。此外，论文还设计了一种置信度机制，用于评估生成动作的可靠性，并根据置信度调整场景图的更新幅度。

## 📊 实验亮点

实验结果表明，SGI方法在CoSPlan基准测试中取得了显著的性能提升，平均性能提升了5.2%。此外，SGI方法还能够泛化到Plan-Bench和VQA等传统规划任务，表明其具有良好的通用性。与Intern-VLM和Qwen2等基线模型相比，SGI方法能够更有效地利用上下文信息，从而更好地完成序列规划任务。

## 🎯 应用场景

该研究成果可应用于机器人导航、自动化装配、智能家居等领域。例如，在机器人导航中，机器人可以通过CoSPlan方法检测并纠正错误的导航指令，从而更安全、更有效地到达目的地。在自动化装配中，机器人可以利用该方法完成复杂的装配任务，并纠正人为错误或环境干扰导致的操作失误。该研究有助于提升智能系统的自主性和可靠性。

## 📄 摘要（原文）

> Large-scale Vision-Language Models (VLMs) exhibit impressive complex reasoning capabilities but remain largely unexplored in visual sequential planning, i.e., executing multi-step actions towards a goal. Additionally, practical sequential planning often involves non-optimal (erroneous) steps, challenging VLMs to detect and correct such steps. We propose Corrective Sequential Planning Benchmark (CoSPlan) to evaluate VLMs in error-prone, vision-based sequential planning tasks across 4 domains: maze navigation, block rearrangement, image reconstruction,and object reorganization. CoSPlan assesses two key abilities: Error Detection (identifying non-optimal action) and Step Completion (correcting and completing action sequences to reach the goal). Despite using state-of-the-art reasoning techniques such as Chain-of-Thought and Scene Graphs, VLMs (e.g. Intern-VLM and Qwen2) struggle on CoSPlan, failing to leverage contextual cues to reach goals. Addressing this, we propose a novel training-free method, Scene Graph Incremental updates (SGI), which introduces intermediate reasoning steps between the initial and goal states. SGI helps VLMs reason about sequences, yielding an average performance gain of 5.2%. In addition to enhancing reliability in corrective sequential planning, SGI generalizes to traditional planning tasks such as Plan-Bench and VQA.

