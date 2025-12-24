---
layout: default
title: "FUNCanon: Learning Pose-Aware Action Primitives via Functional Object Canonicalization for Generalizable Robotic Manipulation"
---

# FUNCanon: Learning Pose-Aware Action Primitives via Functional Object Canonicalization for Generalizable Robotic Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.19102" class="toolbar-btn" target="_blank">📄 arXiv: 2509.19102v1</a>
  <a href="https://arxiv.org/pdf/2509.19102.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.19102v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.19102v1', 'FUNCanon: Learning Pose-Aware Action Primitives via Functional Object Canonicalization for Generalizable Robotic Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongli Xu, Lei Zhang, Xiaoyue Hu, Boyang Zhong, Kaixin Bai, Zoltán-Csaba Márton, Zhenshan Bing, Zhaopeng Chen, Alois Christian Knoll, Jianwei Zhang

**分类**: cs.RO, cs.AI, cs.CV

**发布日期**: 2025-09-23

**备注**: project website: https://sites.google.com/view/funcanon, 11 pages

---

## 💡 一句话要点

**FUNCanon：通过功能对象规范化学习姿态感知动作原语，实现通用机器人操作**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `机器人操作` `动作原语` `功能对象规范化` `扩散模型` `模仿学习`

## 📋 核心要点

1. 端到端演示学习的通用机器人技能通常导致任务特定的策略，难以泛化到训练分布之外。
2. FunCanon通过功能对象规范化，将长时程操作任务分解为可重用的动作块，并利用扩散模型学习策略。
3. 实验表明，该方法在模拟和真实环境中均表现出良好的类别泛化能力和跨任务行为重用能力。

## 📝 摘要（中文）

本文提出了一种名为FunCanon的框架，旨在将长时程操作任务分解为一系列动作块，每个动作块由执行者、动词和对象定义。这种分解方式将策略学习聚焦于动作本身，而非孤立的任务，从而实现组合性和重用性。为了使策略具有姿态感知能力和类别泛化能力，我们执行功能对象规范化，以进行功能对齐和自动操作轨迹转移，利用大型视觉语言模型中的可供性线索将对象映射到共享的功能框架中。基于此对齐数据训练的以对象为中心和以动作为中心的扩散策略FuncDiffuser，能够自然地尊重对象的可供性和姿态，从而简化学习并提高泛化能力。在模拟和真实世界基准上的实验表明，该方法具有类别级别的泛化能力、跨任务行为重用能力和鲁棒的sim2real部署能力，表明功能规范化为复杂操作领域中的可扩展模仿学习提供了强大的归纳偏置。

## 🔬 方法详解

**问题定义**：现有端到端机器人操作学习方法泛化性差，难以适应新的对象类别和任务。它们通常学习任务特定的策略，无法在不同场景中重用。此外，缺乏对对象姿态的有效建模，导致策略对对象姿态变化敏感。

**核心思路**：将长时程操作任务分解为一系列动作原语（action primitives），每个动作原语由执行者、动词和对象定义。通过功能对象规范化，将不同对象映射到共享的功能框架中，从而实现跨对象类别的泛化。利用扩散模型学习动作策略，使其能够生成符合对象可供性和姿态的操作轨迹。

**技术框架**：FunCanon框架包含以下几个主要模块：1) 动作块分解模块：将长时程任务分解为一系列动作块。2) 功能对象规范化模块：利用视觉语言模型提取对象的可供性线索，并将对象映射到共享的功能框架中。3) 扩散策略学习模块：基于规范化后的数据训练扩散策略FuncDiffuser，使其能够生成符合对象可供性和姿态的操作轨迹。

**关键创新**：1) 提出功能对象规范化方法，利用视觉语言模型提取对象的可供性线索，实现跨对象类别的泛化。2) 将长时程任务分解为动作原语，使策略学习聚焦于动作本身，而非孤立的任务，从而实现组合性和重用性。3) 提出FuncDiffuser，一种以对象为中心和以动作为中心的扩散策略，能够自然地尊重对象的可供性和姿态。

**关键设计**：功能对象规范化模块使用预训练的视觉语言模型（如CLIP）提取对象的可供性线索。扩散策略FuncDiffuser使用Transformer架构，以对象姿态、目标姿态和动作块作为输入，生成操作轨迹。损失函数包括轨迹重构损失和动作一致性损失。

## 📊 实验亮点

在模拟和真实世界基准上的实验表明，FunCanon框架具有良好的类别泛化能力、跨任务行为重用能力和鲁棒的sim2real部署能力。例如，在抓取任务中，该方法能够成功抓取训练集中未见过的对象类别，并且能够将学习到的抓取技能应用于新的任务中。与现有方法相比，该方法在泛化性和鲁棒性方面均有显著提升。

## 🎯 应用场景

该研究成果可应用于各种机器人操作任务，例如家庭服务机器人、工业自动化机器人和医疗机器人。通过学习通用的动作原语，机器人可以更好地适应新的对象类别和任务，从而提高其通用性和智能化水平。该方法还可以用于机器人技能的迁移学习和组合，从而加速机器人技能的开发和部署。

## 📄 摘要（原文）

> General-purpose robotic skills from end-to-end demonstrations often leads to task-specific policies that fail to generalize beyond the training distribution. Therefore, we introduce FunCanon, a framework that converts long-horizon manipulation tasks into sequences of action chunks, each defined by an actor, verb, and object. These chunks focus policy learning on the actions themselves, rather than isolated tasks, enabling compositionality and reuse. To make policies pose-aware and category-general, we perform functional object canonicalization for functional alignment and automatic manipulation trajectory transfer, mapping objects into shared functional frames using affordance cues from large vision language models. An object centric and action centric diffusion policy FuncDiffuser trained on this aligned data naturally respects object affordances and poses, simplifying learning and improving generalization ability. Experiments on simulated and real-world benchmarks demonstrate category-level generalization, cross-task behavior reuse, and robust sim2real deployment, showing that functional canonicalization provides a strong inductive bias for scalable imitation learning in complex manipulation domains. Details of the demo and supplemental material are available on our project website https://sites.google.com/view/funcanon.

