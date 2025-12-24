---
layout: default
title: "TReF-6: Inferring Task-Relevant Frames from a Single Demonstration for One-Shot Skill Generalization"
---

# TReF-6: Inferring Task-Relevant Frames from a Single Demonstration for One-Shot Skill Generalization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00310" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00310v2</a>
  <a href="https://arxiv.org/pdf/2509.00310.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00310v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00310v2', 'TReF-6: Inferring Task-Relevant Frames from a Single Demonstration for One-Shot Skill Generalization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuxuan Ding, Shuangge Wang, Tesca Fitzgerald

**分类**: cs.RO, cs.AI

**发布日期**: 2025-08-30 (更新: 2025-09-28)

---

## 💡 一句话要点

**提出TReF-6以解决机器人单次示范泛化问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `任务相关框架` `动态运动原语` `一次性模仿学习` `轨迹几何` `机器人操作`

## 📋 核心要点

1. 现有方法在从单次示范中泛化时缺乏有效的空间表示，导致机器人难以理解和执行复杂任务。
2. TReF-6通过从轨迹几何中识别影响点，推断出任务相关框架，进而为动态运动原语提供参数化参考。
3. 实验结果表明，TReF-6在仿真中对轨迹噪声表现出良好的鲁棒性，并在实际操作中实现了一次性模仿学习。

## 📝 摘要（中文）

机器人在从单次示范中泛化时常面临缺乏可转移和可解释的空间表示的问题。本文提出TReF-6，一种从单一轨迹推断简化的六自由度任务相关框架的方法。该方法通过轨迹几何特征识别影响点，定义局部框架的原点，并作为参数化动态运动原语（DMP）的参考。推断出的框架通过视觉-语言模型进行语义基础化，并通过Grounded-SAM在新场景中进行定位，从而实现功能一致的技能泛化。我们在仿真中验证了TReF-6，并展示了其对轨迹噪声的鲁棒性。此外，我们在实际操作任务中部署了端到端的管道，证明TReF-6支持在多样物体配置下保持任务意图的一次性模仿学习。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人在单次示范中难以泛化的问题，现有方法缺乏有效的空间表示，导致机器人无法准确理解任务的空间结构。

**核心思路**：TReF-6的核心思路是通过轨迹几何特征识别影响点，定义局部框架的原点，从而为动态运动原语提供一个可转移的参数化参考。这样的设计使得机器人能够更好地理解任务的空间结构，超越传统的起始-目标模仿。

**技术框架**：TReF-6的整体架构包括影响点识别、任务相关框架推断、语义基础化和新场景定位等主要模块。首先，从轨迹中提取几何特征，识别影响点；然后，基于影响点推断任务相关框架；接着，通过视觉-语言模型进行语义基础化；最后，利用Grounded-SAM在新场景中进行定位。

**关键创新**：TReF-6的主要创新在于通过轨迹几何推断任务相关框架，提供了一种新的空间表示方式，使得动态运动原语的应用更加灵活和有效。这一方法与现有的基于起始-目标模仿的方式有本质区别。

**关键设计**：在设计中，影响点的识别算法是关键，确保其能够准确反映任务的空间结构。此外，动态运动原语的参数化设计和损失函数的选择也至关重要，以确保模型在多样物体配置下的泛化能力。

## 📊 实验亮点

实验结果显示，TReF-6在仿真环境中对轨迹噪声具有良好的鲁棒性，并在实际操作中实现了一次性模仿学习，能够在不同物体配置下保持任务意图，显著提升了机器人操作的灵活性和准确性。

## 🎯 应用场景

TReF-6在机器人操作领域具有广泛的应用潜力，尤其是在需要快速适应新环境和物体配置的任务中。该方法能够提高机器人在复杂任务中的灵活性和效率，未来可能在服务机器人、工业自动化和家庭助理等领域发挥重要作用。

## 📄 摘要（原文）

> Robots often struggle to generalize from a single demonstration due to the lack of a transferable and interpretable spatial representation. In this work, we introduce TReF-6, a method that infers a simplified, abstracted 6DoF Task-Relevant Frame from a single trajectory. Our approach identifies an influence point purely from the trajectory geometry to define the origin for a local frame, which serves as a reference for parameterizing a Dynamic Movement Primitive (DMP). This influence point captures the task's spatial structure, extending the standard DMP formulation beyond start-goal imitation. The inferred frame is semantically grounded via a vision-language model and localized in novel scenes by Grounded-SAM, enabling functionally consistent skill generalization. We validate TReF-6 in simulation and demonstrate robustness to trajectory noise. We further deploy an end-to-end pipeline on real-world manipulation tasks, showing that TReF-6 supports one-shot imitation learning that preserves task intent across diverse object configurations.

