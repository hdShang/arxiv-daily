---
layout: default
title: "MORE: Mobile Manipulation Rearrangement Through Grounded Language Reasoning"
---

# MORE: Mobile Manipulation Rearrangement Through Grounded Language Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03035" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03035v1</a>
  <a href="https://arxiv.org/pdf/2505.03035.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03035v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03035v1', 'MORE: Mobile Manipulation Rearrangement Through Grounded Language Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mohammad Mohammadi, Daniel Honerkamp, Martin Büchner, Matteo Cassinelli, Tim Welschehold, Fabien Despinoy, Igor Gilitschenski, Abhinav Valada

**分类**: cs.RO, cs.AI

**发布日期**: 2025-05-05

---

## 💡 一句话要点

**提出MORE以解决长距离移动操控中的重排问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `移动操控` `重排任务` `场景图` `实例区分` `主动过滤` `机器人规划` `基础模型`

## 📋 核心要点

1. 现有方法在处理大量物体和大规模环境时性能下降，难以应对复杂的移动操控任务。
2. MORE通过场景图表示环境，结合实例区分和主动过滤机制，提升了语言模型在重排任务中的能力。
3. 在81个多样化的重排任务中，MORE首次成功解决了显著比例的任务，超越了现有基准方法。

## 📝 摘要（中文）

自主长距离移动操控面临场景动态、未探索区域和错误恢复等多重挑战。尽管近期研究利用基础模型进行场景级机器人推理与规划，但在处理大量物体和大规模环境时，性能显著下降。为此，本文提出MORE，一种增强语言模型能力以解决零样本移动操控规划的重排任务的新方法。MORE利用场景图表示环境，结合实例区分，并引入主动过滤机制提取任务相关的子图，从而有效减轻幻觉现象并提高可靠性。我们在BEHAVIOR-1K基准上评估MORE，首次成功解决了大量重排任务，超越了近期的基础模型方法。

## 🔬 方法详解

**问题定义**：本文旨在解决长距离移动操控中的重排任务，现有方法在面对复杂场景时容易出现性能下降和错误恢复困难的问题。

**核心思路**：MORE通过引入场景图、实例区分和主动过滤机制，优化了任务相关信息的提取，进而提升了移动操控的规划能力。

**技术框架**：MORE的整体架构包括环境的场景图表示、实例区分模块和主动过滤机制，形成一个有界的规划问题，减少了不必要的计算和错误。

**关键创新**：MORE的主要创新在于通过场景图和主动过滤机制有效减轻了幻觉现象，提升了规划的可靠性，与现有方法相比具有显著的性能优势。

**关键设计**：在设计中，MORE采用了特定的损失函数以优化实例区分，并通过参数调节实现了对不同环境的适应性，确保了在室内外环境中的有效性。

## 📊 实验亮点

在81个重排任务的评估中，MORE成功解决了显著比例的任务，超越了最新的基础模型方法，展示了在复杂场景下的优越性能，提升幅度明显，标志着移动操控领域的重要进展。

## 🎯 应用场景

MORE的研究成果在家庭服务机器人、仓储自动化和智能交通系统等领域具有广泛的应用潜力。通过提升机器人在复杂环境中的自主重排能力，能够更好地满足人们的日常需求，提升生活质量和工作效率。

## 📄 摘要（原文）

> Autonomous long-horizon mobile manipulation encompasses a multitude of challenges, including scene dynamics, unexplored areas, and error recovery. Recent works have leveraged foundation models for scene-level robotic reasoning and planning. However, the performance of these methods degrades when dealing with a large number of objects and large-scale environments. To address these limitations, we propose MORE, a novel approach for enhancing the capabilities of language models to solve zero-shot mobile manipulation planning for rearrangement tasks. MORE leverages scene graphs to represent environments, incorporates instance differentiation, and introduces an active filtering scheme that extracts task-relevant subgraphs of object and region instances. These steps yield a bounded planning problem, effectively mitigating hallucinations and improving reliability. Additionally, we introduce several enhancements that enable planning across both indoor and outdoor environments. We evaluate MORE on 81 diverse rearrangement tasks from the BEHAVIOR-1K benchmark, where it becomes the first approach to successfully solve a significant share of the benchmark, outperforming recent foundation model-based approaches. Furthermore, we demonstrate the capabilities of our approach in several complex real-world tasks, mimicking everyday activities. We make the code publicly available at https://more-model.cs.uni-freiburg.de.

