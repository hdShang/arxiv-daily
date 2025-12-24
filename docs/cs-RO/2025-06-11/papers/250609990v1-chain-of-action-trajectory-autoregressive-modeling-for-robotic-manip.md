---
layout: default
title: "Chain-of-Action: Trajectory Autoregressive Modeling for Robotic Manipulation"
---

# Chain-of-Action: Trajectory Autoregressive Modeling for Robotic Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09990" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09990v1</a>
  <a href="https://arxiv.org/pdf/2506.09990.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09990v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09990v1', 'Chain-of-Action: Trajectory Autoregressive Modeling for Robotic Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenbo Zhang, Tianrun Hu, Yanyuan Qiao, Hanbo Zhang, Yuchu Qin, Yang Li, Jiajun Liu, Tao Kong, Lingqiao Liu, Xiao Ma

**分类**: cs.RO, cs.CV, cs.LG

**发布日期**: 2025-06-11

---

## 💡 一句话要点

**提出Chain-of-Action以解决机器人操作中的轨迹生成问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人操作` `轨迹生成` `自回归建模` `反向推理` `视觉-运动策略` `动态停止` `多标记预测`

## 📋 核心要点

1. 现有方法通常是前向预测下一步动作，难以有效生成完整的操作轨迹。
2. 论文提出的Chain-of-Action通过反向推理生成整个轨迹，结合任务特定目标，提升了轨迹生成的准确性。
3. CoA在60个RLBench任务和8个真实世界操作任务中表现出色，达到了最先进的性能水平。

## 📝 摘要（中文）

本文提出了一种新颖的视觉-运动策略范式Chain-of-Action（CoA），基于轨迹自回归建模。与传统方法不同，CoA通过任务特定目标的显式反向推理生成整个轨迹，采用行动级的思维链（CoT）过程。该过程在单一自回归结构中统一：第一个标记对应于编码任务特定目标的稳定关键帧动作，后续动作标记在初始关键帧和先前预测动作的条件下自回归生成。这种反向动作推理强制执行了从全局到局部的结构，使每个局部动作紧密受最终目标的约束。CoA还结合了四个互补设计：连续动作标记表示、动态停止以生成可变长度轨迹、反向时间集成和多标记预测，以平衡动作块建模与全局结构。因此，CoA在保持视觉-运动策略的灵活性和简单性的同时，展现出强大的空间泛化能力。实证结果表明，CoA在60个RLBench任务和8个真实世界操作任务中达到了最先进的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人操作中轨迹生成的挑战，现有方法往往依赖于前向预测，导致生成的轨迹不够准确和灵活。

**核心思路**：Chain-of-Action（CoA）通过反向推理生成整个轨迹，利用任务特定目标和行动级思维链（CoT）过程，使得每个局部动作都能紧密围绕最终目标进行设计。

**技术框架**：CoA的整体架构包括：首先生成一个稳定的关键帧动作，随后在此基础上自回归生成后续动作标记。该框架支持动态停止和可变长度轨迹生成。

**关键创新**：CoA的核心创新在于其反向动作推理机制，与传统前向预测方法本质上不同，使得轨迹生成更具全局一致性和局部精确性。

**关键设计**：CoA采用连续动作标记表示，动态停止机制以适应不同任务需求，反向时间集成以增强模型的稳定性，以及多标记预测以平衡动作块建模与全局结构。具体参数设置和损失函数设计在实验中进行了优化。

## 📊 实验亮点

在实验中，Chain-of-Action在60个RLBench任务和8个真实世界操作任务中均表现优异，达到了最先进的性能，显示出相较于现有方法的显著提升，具体性能数据未详述。

## 🎯 应用场景

该研究在机器人操作、自动化制造和人机交互等领域具有广泛的应用潜力。通过提升机器人在复杂任务中的轨迹生成能力，CoA能够显著提高操作效率和准确性，推动智能机器人技术的发展。

## 📄 摘要（原文）

> We present Chain-of-Action (CoA), a novel visuo-motor policy paradigm built upon Trajectory Autoregressive Modeling. Unlike conventional approaches that predict next step action(s) forward, CoA generates an entire trajectory by explicit backward reasoning with task-specific goals through an action-level Chain-of-Thought (CoT) process. This process is unified within a single autoregressive structure: (1) the first token corresponds to a stable keyframe action that encodes the task-specific goals; and (2) subsequent action tokens are generated autoregressively, conditioned on the initial keyframe and previously predicted actions. This backward action reasoning enforces a global-to-local structure, allowing each local action to be tightly constrained by the final goal. To further realize the action reasoning structure, CoA incorporates four complementary designs: continuous action token representation; dynamic stopping for variable-length trajectory generation; reverse temporal ensemble; and multi-token prediction to balance action chunk modeling with global structure. As a result, CoA gives strong spatial generalization capabilities while preserving the flexibility and simplicity of a visuo-motor policy. Empirically, we observe CoA achieves the state-of-the-art performance across 60 RLBench tasks and 8 real-world manipulation tasks.

