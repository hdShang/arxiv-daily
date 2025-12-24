---
layout: default
title: "PAC Bench: Do Foundation Models Understand Prerequisites for Executing Manipulation Policies?"
---

# PAC Bench: Do Foundation Models Understand Prerequisites for Executing Manipulation Policies?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23725" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23725v1</a>
  <a href="https://arxiv.org/pdf/2506.23725.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23725v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23725v1', 'PAC Bench: Do Foundation Models Understand Prerequisites for Executing Manipulation Policies?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Atharva Gundawar, Som Sagar, Ransalu Senanayake

**分类**: cs.RO, cs.AI

**发布日期**: 2025-06-30

---

## 💡 一句话要点

**提出PAC Bench以评估基础模型对操作策略执行前提的理解能力**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言模型` `机器人操作` `物理推理` `基准评估` `属性理解` `可供性` `约束分析`

## 📋 核心要点

1. 现有的视觉-语言模型在执行机器人操作时，往往缺乏对物体基本物理属性和操作前提的深入理解。
2. 本文提出PAC Bench基准，旨在系统评估VLMs对操作可执行性所需的核心属性、可供性和约束的理解能力。
3. 实验结果显示，当前VLMs在理解基本物理概念方面存在显著不足，强调了改进的必要性和研究方向。

## 📝 摘要（中文）

视觉-语言模型（VLMs）在通用机器人操作中越来越重要，能够实现物理推理、策略生成和故障检测等任务。然而，它们在这些高层应用中的能力往往假设了对低层物理前提的深刻理解，而这一能力尚未得到验证。为填补这一关键空白，本文提出了PAC Bench，一个全面的基准，系统评估VLMs对核心属性、可供性和约束（PAC）的理解。PAC Bench包含超过30,000个注释，涵盖673张真实世界图像、100个真实场景和120个独特的模拟约束场景。评估结果显示当前VLMs在理解基本物理概念方面存在显著差距，强调了其在可靠机器人操作中的局限性，并指向了未来研究的关键领域。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视觉-语言模型在执行机器人操作时对低层物理前提理解不足的问题。现有模型在训练过程中往往忽视了物体的基本物理属性和操作前提，导致其在实际应用中的可靠性不足。

**核心思路**：PAC Bench基准通过系统评估模型对核心属性、可供性和约束的理解，填补了这一关键空白。该基准设计了多样化的数据集，以确保全面评估模型的能力。

**技术框架**：PAC Bench的整体架构包括数据集构建、模型评估和结果分析三个主要模块。数据集包含真实图像和模拟场景，评估过程则通过对比不同VLMs的表现来进行。

**关键创新**：PAC Bench的主要创新在于其系统性地评估VLMs对物理概念的理解能力，提供了一个标准化的基准，推动了对物理推理的深入研究。与现有方法相比，PAC Bench更注重模型在实际操作中的可执行性。

**关键设计**：PAC Bench包含超过30,000个注释，涵盖673张真实图像、100个真实场景和120个模拟约束场景，确保了评估的全面性和准确性。

## 📊 实验亮点

实验结果显示，当前的视觉-语言模型在理解基本物理概念方面存在显著差距，评估结果表明，模型在执行操作策略时的准确性和可靠性均低于预期。这一发现强调了针对物理推理能力的进一步研究和模型改进的必要性。

## 🎯 应用场景

该研究的潜在应用领域包括机器人操作、智能家居和自动化制造等。通过提高视觉-语言模型对物理前提的理解能力，PAC Bench能够促进更可靠的机器人系统开发，从而提升自动化任务的效率和安全性。未来，PAC Bench有望成为评估和改进机器人智能的重要工具。

## 📄 摘要（原文）

> Vision-Language Models (VLMs) are increasingly pivotal for generalist robot manipulation, enabling tasks such as physical reasoning, policy generation, and failure detection. However, their proficiency in these high-level applications often assumes a deep understanding of low-level physical prerequisites, a capability that remains largely unverified. For robots to perform actions reliably, they must comprehend intrinsic object properties (e.g., material, weight), action affordances (e.g., graspable, stackable), and physical constraints (e.g., stability, reachability, or an object's state, such as being closed). Despite the widespread use of VLMs in manipulation tasks, we argue that off-the-shelf models may lack this granular, physically grounded understanding, as such prerequisites are often overlooked during training.
>   To address this critical gap, we introduce PAC Bench, a comprehensive benchmark designed to systematically evaluate VLMs on their understanding of core Properties, Affordances, and Constraints (PAC) from a task executability perspective. PAC Bench features a diverse dataset with over 30,000 annotations, comprising 673 real-world images (115 object classes, 15 property types, and 1 to 3 affordances defined per class), 100 real-world humanoid-view scenarios, and 120 unique simulated constraint scenarios across four tasks.
>   Our evaluations reveal significant gaps in the ability of current VLMs to grasp fundamental physical concepts, highlighting limitations in their suitability for reliable robot manipulation and pointing to key areas for targeted research. PAC Bench also serves as a standardized benchmark for rigorously evaluating physical reasoning in VLMs and guiding the development of more robust, physically grounded models for robotic applications.
>   Project Page: https://pacbench.github.io/

