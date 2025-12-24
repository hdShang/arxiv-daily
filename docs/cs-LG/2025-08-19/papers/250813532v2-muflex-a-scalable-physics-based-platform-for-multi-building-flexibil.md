---
layout: default
title: "MuFlex: A Scalable, Physics-based Platform for Multi-Building Flexibility Analysis and Coordination"
---

# MuFlex: A Scalable, Physics-based Platform for Multi-Building Flexibility Analysis and Coordination

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13532" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13532v2</a>
  <a href="https://arxiv.org/pdf/2508.13532.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13532v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13532v2', 'MuFlex: A Scalable, Physics-based Platform for Multi-Building Flexibility Analysis and Coordination')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziyan Wu, Ivan Korolija, Rui Tang

**分类**: cs.LG, eess.SY

**发布日期**: 2025-08-19 (更新: 2025-11-27)

**🔗 代码/项目**: [GITHUB](https://github.com/BuildNexusX/MuFlex)

---

## 💡 一句话要点

**提出MuFlex以解决多建筑灵活性协调问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱四：生成式动作 (Generative Motion)**

**关键词**: `建筑灵活性` `强化学习` `多建筑协调` `能源管理` `开源平台` `智能建筑` `可再生能源` `EnergyPlus`

## 📋 核心要点

1. 现有建筑控制测试平台多集中于单一建筑，缺乏对多建筑灵活性协调的支持，且通常依赖简化模型，无法全面捕捉物理复杂性。
2. MuFlex平台通过实现EnergyPlus建筑模型间的同步信息交换，提供了一个模块化、标准化的RL实现，解决了多建筑协调的需求。
3. 在案例研究中，MuFlex成功协调了四栋办公楼的需求灵活性，使用SAC算法有效降低了近12%的聚合峰值需求，确保了室内舒适度。

## 📝 摘要（中文）

随着可再生能源在电网中的渗透增加，维持系统平衡需要建筑聚合体的协调需求灵活性。尽管强化学习（RL）因其无模型特性在建筑控制中得到广泛应用，但现有的建筑测试平台大多针对单一建筑，缺乏多建筑的灵活性协调能力。为此，本文开发了MuFlex，一个可扩展的开源平台，支持多建筑灵活性协调。MuFlex实现了EnergyPlus建筑模型之间的同步信息交换，并遵循最新的OpenAI Gym接口，提供模块化的标准化RL实现。通过案例研究，使用Soft Actor-Critic（SAC）算法协调四栋办公楼的需求灵活性，结果表明，协调后聚合峰值需求减少了近12%，同时保持了室内舒适度。

## 🔬 方法详解

**问题定义**：本文旨在解决现有建筑控制平台在多建筑灵活性协调方面的不足，尤其是缺乏对物理复杂性的全面捕捉和灵活的输入输出设置。

**核心思路**：MuFlex通过提供一个可扩展的开源平台，允许建筑模型之间的同步信息交换，进而实现多建筑的灵活性协调，采用最新的OpenAI Gym接口以增强其适用性。

**技术框架**：MuFlex的整体架构包括多个模块，主要包括EnergyPlus建筑模型、信息交换机制和RL算法实现，确保不同建筑间的协调与控制。

**关键创新**：MuFlex的核心创新在于其开放源代码和模块化设计，使其能够适应多种控制场景，并且能够捕捉建筑间的物理交互，区别于传统的简化模型或数据驱动方法。

**关键设计**：MuFlex在参数设置上灵活，支持多种输入输出格式，损失函数和网络结构均可根据具体应用进行调整，以适应不同的控制策略和需求。

## 📊 实验亮点

在实验中，MuFlex成功协调了四栋办公楼的需求灵活性，使用SAC算法将聚合峰值需求降低了近12%。这一结果不仅保持了室内舒适度，还展示了MuFlex在多建筑协调中的有效性，具有显著的实际应用价值。

## 🎯 应用场景

MuFlex平台具有广泛的应用潜力，特别是在智能建筑管理、能源调度和可再生能源集成等领域。通过协调多建筑的需求灵活性，能够有效提升电网的稳定性和可持续性，推动智能城市的发展。

## 📄 摘要（原文）

> With the increasing penetration of renewable generation on the power grid, maintaining system balance requires coordinated demand flexibility from aggregations of buildings. Reinforcement learning (RL) has been widely explored for building controls because of its model-free nature. Open-source simulation testbeds are essential not only for training RL agents but also for fairly benchmarking control strategies. However, most building-sector testbeds target single buildings; multi-building platforms are relatively limited and typically rely on simplified models (e.g., Resistanc-Capacitance) or data-driven approaches, which lack the ability to fully capture the physical intricacies and intermediate variables necessary for interpreting control performance. Moreover, these platforms often impose fixed inputs, outputs, and model formats, restricting their applicability as benchmarking tools across diverse control scenarios. To address these gaps, MuFlex, a scalable, open-source platform for multi-building flexibility coordination, was developed. MuFlex enables synchronous information exchange across EnergyPlus building models and adheres to the latest OpenAI Gym interface, providing a modular, standardized RL implementation. The platform's capabilities were demonstrated in a case study coordinating demand flexibility across four office buildings using the Soft Actor-Critic (SAC) algorithm. The results show that under four buildings' coordination, SAC effectively reduced the aggregated peak demand by nearly 12% with maintained indoor comfort to ensure the power demand below the threshold. The platform is released open-source on GitHub: https://github.com/BuildNexusX/MuFlex.

