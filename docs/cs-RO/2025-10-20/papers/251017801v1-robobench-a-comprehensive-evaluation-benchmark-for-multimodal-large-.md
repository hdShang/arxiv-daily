---
layout: default
title: Robobench: A Comprehensive Evaluation Benchmark for Multimodal Large Language Models as Embodied Brain
---

# Robobench: A Comprehensive Evaluation Benchmark for Multimodal Large Language Models as Embodied Brain

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.17801" target="_blank" class="toolbar-btn">arXiv: 2510.17801v1</a>
    <a href="https://arxiv.org/pdf/2510.17801.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.17801v1" 
            onclick="toggleFavorite(this, '2510.17801v1', 'Robobench: A Comprehensive Evaluation Benchmark for Multimodal Large Language Models as Embodied Brain')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Yulin Luo, Chun-Kai Fan, Menghang Dong, Jiayu Shi, Mengdi Zhao, Bo-Wen Zhang, Cheng Chi, Jiaming Liu, Gaole Dai, Rongyu Zhang, Ruichuan An, Kun Wu, Zhengping Che, Shaoxuan Xie, Guocai Yao, Zhongxia Zhao, Pengwei Wang, Guang Liu, Zhongyuan Wang, Tiejun Huang, Shanghang Zhang

**分类**: cs.RO, cs.CV

**发布日期**: 2025-10-20

---

## 💡 一句话要点

**RoboBench：用于评估多模态大语言模型作为具身智能大脑的综合基准**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `具身智能` `多模态大语言模型` `机器人操作` `评估基准` `认知能力`

## 📋 核心要点

1. 现有具身智能基准测试在评估高层次推理能力时，存在维度不完整和任务真实性不足的问题，难以全面评估认知能力。
2. RoboBench通过定义指令理解、感知推理、泛化规划、可供性预测和失败分析五个维度，系统评估MLLM作为具身大脑的能力。
3. RoboBench包含来自真实机器人数据的多样化数据集，并引入MLLM作为世界模拟器的评估框架，以确保评估的真实性和可行性。

## 📝 摘要（中文）

构建能够在动态、非结构化环境中感知、推理和行动的机器人仍然是一个核心挑战。最近的具身系统通常采用双系统范式，其中系统2处理高层次推理，而系统1执行低层次控制。本文将系统2称为具身大脑，强调其在操作任务中作为推理和决策认知核心的作用。因此，对具身大脑进行系统评估至关重要。然而，现有的基准侧重于执行成功，或者当针对高层次推理时，存在维度不完整和任务真实性有限的问题，只能提供认知能力的局部图景。为了弥合这一差距，我们引入了RoboBench，一个系统地评估多模态大语言模型（MLLM）作为具身大脑的基准。受操作流程中关键角色的驱动，RoboBench定义了五个维度——指令理解、感知推理、泛化规划、可供性预测和失败分析——涵盖14种能力、25个任务和6092个QA对。为了确保真实性，我们从大规模真实机器人数据中整理了跨不同具身、属性丰富的对象和多视角场景的数据集。对于规划，RoboBench引入了一个评估框架，即MLLM作为世界模拟器。它通过模拟预测的计划是否可以实现关键的对象状态变化来评估具身可行性。对14个MLLM的实验揭示了根本的局限性：在隐式指令理解、时空推理、跨场景规划、细粒度可供性理解和执行失败诊断方面的困难。RoboBench提供了一个全面的支架来量化高层次认知，并指导下一代具身MLLM的开发。

## 🔬 方法详解

**问题定义**：现有具身智能系统评估侧重于执行成功率，或在高层推理评估中存在维度不全、任务不够真实的问题。这导致无法全面评估多模态大语言模型（MLLM）作为具身大脑的认知能力，尤其是在复杂操作任务中。现有方法难以有效诊断MLLM在指令理解、推理规划、可供性预测和错误分析等方面的不足。

**核心思路**：RoboBench的核心思路是构建一个综合性的评估基准，从多个维度系统地评估MLLM在具身环境中的认知能力。通过定义指令理解、感知推理、泛化规划、可供性预测和失败分析五个关键维度，并设计相应的任务和评估指标，RoboBench旨在全面量化MLLM作为具身大脑的能力。此外，引入MLLM作为世界模拟器的概念，评估规划方案的具身可行性。

**技术框架**：RoboBench的整体框架包含以下几个主要组成部分：1) 数据集：包含来自真实机器人数据的多样化场景、对象和任务，涵盖不同的具身平台和视角。2) 评估维度：定义了指令理解、感知推理、泛化规划、可供性预测和失败分析五个维度，每个维度包含多个能力。3) 评估任务：为每个能力设计了具体的评估任务，包括问答、规划等。4) 评估指标：针对每个任务设计了相应的评估指标，用于量化MLLM的性能。5) MLLM作为世界模拟器：用于评估规划方案的具身可行性，通过模拟预测的计划是否能实现关键对象状态变化。

**关键创新**：RoboBench的关键创新在于其综合性的评估维度和MLLM作为世界模拟器的评估框架。与现有基准相比，RoboBench更全面地覆盖了MLLM在具身环境中的认知能力，并引入了具身可行性的评估，从而更真实地反映了MLLM在实际机器人应用中的性能。此外，RoboBench的数据集来自真实机器人数据，保证了评估的真实性和可靠性。

**关键设计**：RoboBench的关键设计包括：1) 数据集的构建：从大规模真实机器人数据中收集，包含多样化的场景、对象和任务。2) 评估维度的选择：基于操作任务的关键环节，定义了指令理解、感知推理、泛化规划、可供性预测和失败分析五个维度。3) 评估任务的设计：针对每个能力设计了具体的评估任务，例如，指令理解包括隐式指令理解和歧义指令理解等。4) MLLM作为世界模拟器的实现：通过prompting MLLM来预测执行动作后的环境状态变化，并评估预测结果的准确性。

## 📊 实验亮点

在对14个MLLM的实验中，RoboBench揭示了现有模型在隐式指令理解、时空推理、跨场景规划、细粒度可供性理解和执行失败诊断方面的局限性。这些结果表明，现有MLLM在具身智能应用中仍有很大的提升空间，RoboBench为未来的研究提供了明确的方向。

## 🎯 应用场景

RoboBench可用于评估和改进多模态大语言模型在机器人操作任务中的性能，推动具身智能的发展。其应用领域包括家庭服务机器人、工业自动化、医疗辅助机器人等。通过RoboBench的评估，可以更好地了解MLLM在具身环境中的优势和不足，从而指导下一代具身智能系统的设计和开发。

## 📄 摘要（原文）

> Building robots that can perceive, reason, and act in dynamic, unstructured environments remains a core challenge. Recent embodied systems often adopt a dual-system paradigm, where System 2 handles high-level reasoning while System 1 executes low-level control. In this work, we refer to System 2 as the embodied brain, emphasizing its role as the cognitive core for reasoning and decision-making in manipulation tasks. Given this role, systematic evaluation of the embodied brain is essential. Yet existing benchmarks emphasize execution success, or when targeting high-level reasoning, suffer from incomplete dimensions and limited task realism, offering only a partial picture of cognitive capability. To bridge this gap, we introduce RoboBench, a benchmark that systematically evaluates multimodal large language models (MLLMs) as embodied brains. Motivated by the critical roles across the full manipulation pipeline, RoboBench defines five dimensions-instruction comprehension, perception reasoning, generalized planning, affordance prediction, and failure analysis-spanning 14 capabilities, 25 tasks, and 6092 QA pairs. To ensure realism, we curate datasets across diverse embodiments, attribute-rich objects, and multi-view scenes, drawing from large-scale real robotic data. For planning, RoboBench introduces an evaluation framework, MLLM-as-world-simulator. It evaluate embodied feasibility by simulating whether predicted plans can achieve critical object-state changes. Experiments on 14 MLLMs reveal fundamental limitations: difficulties with implicit instruction comprehension, spatiotemporal reasoning, cross-scenario planning, fine-grained affordance understanding, and execution failure diagnosis. RoboBench provides a comprehensive scaffold to quantify high-level cognition, and guide the development of next-generation embodied MLLMs. The project page is in https://robo-bench.github.io.

