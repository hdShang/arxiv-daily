---
layout: default
title: DeCo: Task Decomposition and Skill Composition for Zero-Shot Generalization in Long-Horizon 3D Manipulation
---

# DeCo: Task Decomposition and Skill Composition for Zero-Shot Generalization in Long-Horizon 3D Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.00527" class="toolbar-btn" target="_blank">📄 arXiv: 2505.00527v1</a>
  <a href="https://arxiv.org/pdf/2505.00527.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.00527v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.00527v1', 'DeCo: Task Decomposition and Skill Composition for Zero-Shot Generalization in Long-Horizon 3D Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zixuan Chen, Junhui Yin, Yangtao Chen, Jing Huo, Pinzhuo Tian, Jieqi Shi, Yiwen Hou, Yinchuan Li, Yang Gao

**分类**: cs.RO

**发布日期**: 2025-05-01

---

## 💡 一句话要点

**提出DeCo以解决长时间3D操作任务的零-shot泛化问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长时间3D操作` `多任务模仿学习` `零-shot泛化` `任务分解` `技能组合` `视觉-语言模型` `机器人技术`

## 📋 核心要点

1. 现有的多任务模仿学习模型在处理新颖的长时间3D操作任务时，泛化能力不足，面临显著挑战。
2. DeCo通过将模仿学习演示分解为原子任务，并构建原子技能数据集，提升了模型的零-shot泛化能力。
3. 在实验中，DeCo在三种多任务IL模型上实现了显著的成功率提升，尤其是在真实世界实验中表现出色。

## 📝 摘要（中文）

在语言条件下的多任务模仿学习（IL）模型推广到新颖的长时间3D操作任务中仍然是一个重大挑战。为此，我们提出了DeCo（任务分解与技能组合），这是一个与多种多任务IL模型兼容的模型无关框架，旨在增强其对新颖组合长时间3D操作任务的零-shot泛化能力。DeCo首先基于夹具与物体之间的物理交互，将IL演示分解为一组模块化的原子任务，并构建一个原子训练数据集，使模型能够在模仿学习过程中学习多样化的可重用原子技能。在推理时，DeCo利用视觉-语言模型（VLM）解析新长时间任务的高层指令，检索相关的原子技能，并动态调度其执行；空间感知技能链模块确保顺畅、无碰撞的技能顺序转换。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有多任务模仿学习模型在新颖长时间3D操作任务中的零-shot泛化能力不足的问题。现有方法在处理复杂任务时，往往无法有效应对任务的组合性和长时间性。

**核心思路**：DeCo的核心思路是通过任务分解和技能组合，将复杂的操作任务拆分为更小的原子任务，使得模型能够学习和重用这些原子技能，从而提升其泛化能力。

**技术框架**：DeCo的整体架构包括两个主要模块：任务分解模块和技能调度模块。任务分解模块负责将IL演示分解为原子任务，技能调度模块则在推理时根据高层指令动态调度原子技能的执行。

**关键创新**：DeCo的主要创新在于其任务分解与技能组合的框架设计，使得模型能够在未见过的任务上进行有效的零-shot学习。这一设计与传统方法的本质区别在于其模块化和重用性。

**关键设计**：在关键设计上，DeCo使用了视觉-语言模型（VLM）来解析任务指令，并结合空间感知技能链模块，确保技能之间的顺畅过渡。此外，原子训练数据集的构建也为模型提供了丰富的学习素材。

## 📊 实验亮点

在实验中，DeCo在三种多任务IL模型（RVT-2、3DDA和ARP）上分别实现了66.67%、21.53%和57.92%的成功率提升，尤其在真实世界实验中，基于DeCo的模型在仅训练6个原子任务的情况下成功完成9个新任务，平均成功率提升达53.33%。

## 🎯 应用场景

该研究的潜在应用领域包括机器人操作、自动化制造和人机交互等。通过提升模型在复杂任务中的泛化能力，DeCo可以在多种实际场景中实现更高效的任务执行，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Generalizing language-conditioned multi-task imitation learning (IL) models to novel long-horizon 3D manipulation tasks remains a significant challenge. To address this, we propose DeCo (Task Decomposition and Skill Composition), a model-agnostic framework compatible with various multi-task IL models, designed to enhance their zero-shot generalization to novel, compositional, long-horizon 3D manipulation tasks. DeCo first decomposes IL demonstrations into a set of modular atomic tasks based on the physical interaction between the gripper and objects, and constructs an atomic training dataset that enables models to learn a diverse set of reusable atomic skills during imitation learning. At inference time, DeCo leverages a vision-language model (VLM) to parse high-level instructions for novel long-horizon tasks, retrieve the relevant atomic skills, and dynamically schedule their execution; a spatially-aware skill-chaining module then ensures smooth, collision-free transitions between sequential skills. We evaluate DeCo in simulation using DeCoBench, a benchmark specifically designed to assess zero-shot generalization of multi-task IL models in compositional long-horizon 3D manipulation. Across three representative multi-task IL models (RVT-2, 3DDA, and ARP), DeCo achieves success rate improvements of 66.67%, 21.53%, and 57.92%, respectively, on 12 novel compositional tasks. Moreover, in real-world experiments, a DeCo-enhanced model trained on only 6 atomic tasks successfully completes 9 novel long-horizon tasks, yielding an average success rate improvement of 53.33% over the base multi-task IL model. Video demonstrations are available at: https://deco226.github.io.

