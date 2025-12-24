---
layout: default
title: Learning Hierarchical Domain Models Through Environment-Grounded Interaction
---

# Learning Hierarchical Domain Models Through Environment-Grounded Interaction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13497" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13497v3</a>
  <a href="https://arxiv.org/pdf/2505.13497.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13497v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13497v3', 'Learning Hierarchical Domain Models Through Environment-Grounded Interaction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Claudius Kienle, Benjamin Alt, Oleg Arenz, Jan Peters

**分类**: cs.RO, cs.AI

**发布日期**: 2025-05-15 (更新: 2025-10-01)

---

## 💡 一句话要点

**提出LODGE框架以解决开放世界任务建模问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `领域模型` `自主学习` `开放世界` `层次抽象` `环境交互` `机器人技术` `任务规划`

## 📋 核心要点

1. 现有方法依赖于单一的通用领域模型，无法有效应对开放世界环境中的多样化任务。
2. 本文提出LODGE框架，通过层次抽象和自动仿真实现自主领域学习，动态生成任务特定模型。
3. 实验表明，LODGE在两个国际规划竞赛领域和一个机器人组装领域中，模型准确性和任务成功率显著高于现有方法。

## 📝 摘要（中文）

领域模型使自主代理能够通过生成可解释的计划来解决长时间跨度的任务。然而，在开放世界环境中，单一的通用领域模型无法捕捉任务的多样性，因此代理必须动态生成适合特定任务的模型。大型语言模型（LLMs）虽然能够生成这些领域模型，但高错误率限制了其适用性。为此，本文提出了LODGE框架，通过环境基础的交互实现自主领域学习。LODGE基于层次抽象和自动化仿真，识别并纠正抽象层之间以及模型与环境之间的不一致性。实验结果表明，LODGE在准确性和任务成功率上优于现有方法，且所需环境交互极少，无需人类反馈或演示。

## 🔬 方法详解

**问题定义**：本文旨在解决开放世界环境中，单一领域模型无法适应多样化任务的问题。现有方法通常依赖大量人类反馈，限制了自主部署的能力。

**核心思路**：LODGE框架通过环境基础的交互和层次抽象，自动生成和修正领域模型，确保模型与环境的一致性，从而实现自主学习。

**技术框架**：LODGE的整体架构包括环境交互模块、层次抽象模块和自动仿真模块。环境交互模块负责收集环境反馈，层次抽象模块生成任务特定的模型，而自动仿真模块则用于验证和修正模型。

**关键创新**：LODGE的主要创新在于其层次化的模型生成和自动化的环境交互，显著减少了对人类反馈的依赖，与传统方法相比，提升了自主学习的能力。

**关键设计**：LODGE设计了高效的抽象层次结构，采用了特定的损失函数来优化模型一致性，并利用低级技能集进行任务执行，确保了模型的可执行性和准确性。

## 📊 实验亮点

实验结果显示，LODGE在两个国际规划竞赛领域和一个机器人组装领域中，模型准确性提高了显著的比例，任务成功率也高于现有方法，且所需的环境交互次数极少，完全不依赖人类反馈或演示。

## 🎯 应用场景

该研究的潜在应用领域包括自主机器人、智能家居系统和复杂任务规划等。通过实现自主领域学习，LODGE框架能够在动态环境中快速适应不同任务，提高系统的灵活性和效率，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Domain models enable autonomous agents to solve long-horizon tasks by producing interpretable plans. However, in open-world environments, a single general domain model cannot capture the variety of tasks, so agents must generate suitable task-specific models on the fly. Large Language Models (LLMs), with their implicit common knowledge, can generate such domains, but suffer from high error rates that limit their applicability. Hence, related work relies on extensive human feed-back or prior knowledge, which undermines autonomous, open-world deployment. In this work, we propose LODGE, a framework for autonomous domain learning from LLMs and environment grounding. LODGE builds on hierarchical abstractions and automated simulations to identify and correct inconsistencies between abstraction layers and between the model and environment. Our framework is task-agnostic, as it generates predicates, operators, and their preconditions and effects, while only assuming access to a simulator and a set of generic, executable low-level skills. Experiments on two International Planning Competition ( IPC) domains and a robotic assembly domain show that LODGE yields more accurate domain models and higher task success than existing methods, requiring remarkably few environment interactions and no human feedback or demonstrations.

