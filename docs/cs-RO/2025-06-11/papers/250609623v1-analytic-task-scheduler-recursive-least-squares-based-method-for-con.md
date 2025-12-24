---
layout: default
title: "Analytic Task Scheduler: Recursive Least Squares Based Method for Continual Learning in Embodied Foundation Models"
---

# Analytic Task Scheduler: Recursive Least Squares Based Method for Continual Learning in Embodied Foundation Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09623" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09623v1</a>
  <a href="https://arxiv.org/pdf/2506.09623.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09623v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09623v1', 'Analytic Task Scheduler: Recursive Least Squares Based Method for Continual Learning in Embodied Foundation Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lipei Xie, Yingxin Li, Huiping Zhuang

**分类**: cs.RO

**发布日期**: 2025-06-11

**🔗 代码/项目**: [GITHUB](https://github.com/MIAA-Embodied-AI/AnalyticTaskScheduler)

---

## 💡 一句话要点

**提出分析任务调度器以解决持续学习中的遗忘问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `持续学习` `灾难性遗忘` `具身基础模型` `递归最小二乘法` `任务调度` `动态模型选择` `机器人控制`

## 📋 核心要点

1. 现有的具身基础模型在持续学习新技能时容易出现灾难性遗忘，无法有效保留先前学习的知识。
2. 本文提出的分析任务调度器（ATS）通过任务特定模型库和递归最小二乘法调度器，解决了任务识别和模型选择的问题。
3. 在真实机器人平台上进行的实验表明，ATS在抵抗遗忘和适应任务变化方面表现优于现有方法。

## 📝 摘要（中文）

具身基础模型在人工智能与物理世界的交互中至关重要，能够整合多模态输入以理解人类意图并控制机器人。然而，这些模型在持续学习新技能时面临灾难性遗忘的问题。为了解决这一问题，本文提出了分析任务调度器（ATS），一个新颖的持续学习框架。ATS由任务特定模型库和使用递归最小二乘法（RLS）训练的分析调度器组成，能够实现任务识别和动态模型选择，同时避免任务间的参数干扰。该调度器通过统计量增量更新参数，无需回顾历史数据，从而实现抗遗忘学习。我们在真实机器人平台上验证了ATS，结果表明其在遗忘抵抗和任务适应性方面表现优异。

## 🔬 方法详解

**问题定义**：本文旨在解决具身基础模型在持续学习过程中面临的灾难性遗忘问题。现有方法往往无法有效保留先前学习的技能，导致新技能的学习干扰旧技能的表现。

**核心思路**：提出的分析任务调度器（ATS）通过构建任务特定模型库和使用递归最小二乘法（RLS）进行调度，能够实现任务的准确识别和动态模型选择，从而避免参数干扰。

**技术框架**：ATS的整体架构包括任务特定模型库和分析调度器。每个模型在单一任务上独立微调，调度器通过学习语言指令与任务模型之间的映射来进行动态选择。

**关键创新**：ATS的主要创新在于其使用递归最小二乘法进行参数更新，允许调度器仅通过统计量（自相关和交叉相关矩阵）进行增量学习，避免了对历史数据的依赖。

**关键设计**：在设计中，ATS的调度器通过统计量更新参数，确保了学习过程的抗遗忘特性。此外，模型库的独立微调策略有效降低了任务间的参数干扰。

## 📊 实验亮点

实验结果显示，ATS在真实机器人平台上表现出色，相较于基线方法，其在遗忘抵抗能力上提升显著，能够更好地适应任务变化，具体性能数据和提升幅度在实验中得到了验证。

## 🎯 应用场景

该研究的潜在应用领域包括机器人控制、智能家居、自动驾驶等需要持续学习和适应的场景。通过有效解决遗忘问题，ATS能够提升具身基础模型在复杂动态环境中的实用性和可靠性，推动智能系统的进一步发展。

## 📄 摘要（原文）

> Embodied foundation models are crucial for Artificial Intelligence (AI) interacting with the physical world by integrating multi-modal inputs, such as proprioception, vision and language, to understand human intentions and generate actions to control robots. While these models demonstrate strong generalization and few-shot learning capabilities, they face significant challenges in continually acquiring new skills without forgetting previously learned skills, a problem known as catastrophic forgetting. To address this issue, we propose the Analytic Task Scheduler (ATS), a novel framework for continual learning in embodied foundation models. ATS consists of a task-specific model library, where each model is fine-tuned independently on a single task, and an analytic scheduler trained using recursive least squares (RLS) to learn the mapping between language instructions and task-specific models. This architecture enables accurate task recognition and dynamic model selection while fundamentally avoiding parameter interference across tasks. The scheduler updates its parameters incrementally using only statistics (autocorrelation and cross-correlation matrices), enabling forgetting-resistant learning without the need to revisit historical data. We validate ATS on a real-world robot platform (RM65B), demonstrating superior resistance to forgetting and strong adaptability to task variations. The results highlight ATS as an effective, scalable, and deployable solution for continual learning in embodied foundation models operating in complex, dynamic environments. Our code will be available at https://github.com/MIAA-Embodied-AI/AnalyticTaskScheduler

