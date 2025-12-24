---
layout: default
title: "MolmoAct: Action Reasoning Models that can Reason in Space"
---

# MolmoAct: Action Reasoning Models that can Reason in Space

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.07917" class="toolbar-btn" target="_blank">📄 arXiv: 2508.07917v4</a>
  <a href="https://arxiv.org/pdf/2508.07917.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.07917v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.07917v4', 'MolmoAct: Action Reasoning Models that can Reason in Space')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jason Lee, Jiafei Duan, Haoquan Fang, Yuquan Deng, Shuo Liu, Boyang Li, Bohan Fang, Jieyu Zhang, Yi Ru Wang, Sangho Lee, Winson Han, Wilbert Pumacay, Angelica Wu, Rose Hendrix, Karen Farley, Eli VanderBilt, Ali Farhadi, Dieter Fox, Ranjay Krishna

**分类**: cs.RO

**发布日期**: 2025-08-11 (更新: 2025-09-18)

**备注**: Updated GR00T result to N1.5

---

## 💡 一句话要点

**提出MolmoAct以解决机器人行动推理不足的问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人推理` `深度学习` `空间规划` `多模态感知` `开放指令跟随`

## 📋 核心要点

1. 现有机器人模型在感知与控制之间缺乏有效的推理能力，导致适应性和泛化能力不足。
2. MolmoAct通过三阶段管道集成感知、规划和控制，提升了机器人在复杂任务中的表现。
3. 在多个基准测试中，MolmoAct实现了显著的性能提升，尤其是在长时间任务和开放指令跟随方面。

## 📝 摘要（中文）

推理是有目的行动的核心，但大多数机器人基础模型直接将感知和指令映射到控制，这限制了适应性、泛化能力和语义基础。我们提出了行动推理模型（ARMs），通过结构化的三阶段管道集成感知、规划和控制。MolmoAct将观察和指令编码为深度感知标记，生成可编辑的中级空间计划，并预测精确的低级动作，从而实现可解释和可引导的行为。实验结果显示，MolmoAct在多个任务上表现优异，超越了现有基线，并首次发布了包含超过10,000条高质量机器人轨迹的MolmoAct数据集。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有机器人基础模型在感知与控制之间缺乏有效推理的问题。这些模型通常直接将感知信息和指令映射到控制指令，导致适应性和泛化能力不足，无法处理复杂的任务场景。

**核心思路**：MolmoAct的核心思路是通过结构化的三阶段管道，将感知、规划和控制有效结合。该模型首先将观察和指令编码为深度感知标记，然后生成可编辑的中级空间计划，最后预测精确的低级动作，从而实现可解释和可引导的行为。

**技术框架**：MolmoAct的整体架构包括三个主要模块：深度感知标记生成模块、中级空间计划生成模块和低级动作预测模块。每个模块在处理信息时都考虑了空间和时间的上下文，从而提升了模型的整体性能。

**关键创新**：MolmoAct的主要创新在于其三阶段的结构化推理过程，使得机器人能够在复杂环境中进行有效的空间推理和决策。这一设计与现有方法的直接映射方式形成了鲜明对比，显著提升了模型的适应性和解释能力。

**关键设计**：在模型设计中，MolmoAct采用了深度感知标记来捕捉环境信息，并使用可编辑的轨迹生成中级空间计划。此外，模型在训练过程中引入了多种损失函数，以优化不同阶段的输出，确保最终动作的准确性和可控性。

## 📊 实验亮点

MolmoAct在多个基准测试中表现出色：在SimperEnv视觉匹配任务中实现70.5%的零-shot准确率，超越了现有的闭源模型；在LIBERO任务中平均成功率达到86.6%，比ThinkAct提升6.3%；在真实世界微调中，单臂任务进展提升10%，双臂任务进展提升22.7%。此外，模型在开放指令跟随和轨迹引导方面获得了最高的人类偏好评分。

## 🎯 应用场景

MolmoAct的研究成果在多个领域具有广泛的应用潜力，包括服务机器人、自动驾驶、智能制造等。通过提升机器人在复杂环境中的推理能力，该模型能够更好地执行任务并适应动态变化的场景，未来可能推动机器人技术的进一步发展和普及。

## 📄 摘要（原文）

> Reasoning is central to purposeful action, yet most robotic foundation models map perception and instructions directly to control, which limits adaptability, generalization, and semantic grounding. We introduce Action Reasoning Models (ARMs), a class of robotic foundation models that integrate perception, planning, and control through a structured three-stage pipeline. Our model, MolmoAct, encodes observations and instructions into depth-aware perception tokens, generates mid-level spatial plans as editable trajectory traces, and predicts precise low-level actions, enabling explainable and steerable behavior. MolmoAct-7B-D achieves strong performance across simulation and real-world settings: 70.5% zero-shot accuracy on SimplerEnv Visual Matching tasks, surpassing closed-source Pi-0 and GR00T N1.5; 86.6% average success on LIBERO, including an additional 6.3% gain over ThinkAct on long-horizon tasks; and in real-world fine-tuning, an additional 10% (single-arm) and an additional 22.7% (bimanual) task progression over Pi-0-FAST. It also outperforms baselines by an additional 23.3% on out-of-distribution generalization and achieves top human-preference scores for open-ended instruction following and trajectory steering. Furthermore, we release, for the first time, the MolmoAct Dataset -- a mid-training robot dataset comprising over 10,000 high quality robot trajectories across diverse scenarios and tasks. Training with this dataset yields an average 5.5% improvement in general performance over the base model. We release all model weights, training code, our collected dataset, and our action reasoning dataset, establishing MolmoAct as both a state-of-the-art robotics foundation model and an open blueprint for building ARMs that transform perception into purposeful action through structured reasoning. Blogpost: https://allenai.org/blog/molmoact

